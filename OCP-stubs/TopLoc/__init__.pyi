import OCP.TopLoc
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.NCollection
import OCP.Standard
import io
__all__  = [
"TopLoc_Datum3D",
"TopLoc_IndexedMapOfLocation",
"TopLoc_ItemLocation",
"TopLoc_Location",
"TopLoc_MapLocationHasher",
"TopLoc_MapOfLocation",
"TopLoc_SListNodeOfItemLocation",
"TopLoc_SListOfItemLocation",
"HashCode",
"ShallowDump"
]
class TopLoc_Datum3D(OCP.Standard.Standard_Transient):
    """
    Describes a coordinate transformation, i.e. a change to an elementary 3D coordinate system, or position in 3D space. A Datum3D is always described relative to the default datum. The default datum is described relative to itself: its origin is (0,0,0), and its axes are (1,0,0) (0,1,0) (0,0,1).Describes a coordinate transformation, i.e. a change to an elementary 3D coordinate system, or position in 3D space. A Datum3D is always described relative to the default datum. The default datum is described relative to itself: its origin is (0,0,0), and its axes are (1,0,0) (0,1,0) (0,0,1).Describes a coordinate transformation, i.e. a change to an elementary 3D coordinate system, or position in 3D space. A Datum3D is always described relative to the default datum. The default datum is described relative to itself: its origin is (0,0,0), and its axes are (1,0,0) (0,1,0) (0,0,1).
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Form(self) -> OCP.gp.gp_TrsfForm: 
        """
        Return transformation form.
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
    def ShallowDump(self,S : io.BytesIO) -> None: 
        """
        Writes the contents of this Datum3D to the stream S.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns a gp_Trsf which, when applied to this datum, produces the default datum.
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Returns a gp_Trsf which, when applied to this datum, produces the default datum.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
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
class TopLoc_IndexedMapOfLocation(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : TopLoc_Location) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopLoc_IndexedMapOfLocation) -> TopLoc_IndexedMapOfLocation: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : TopLoc_Location) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopLoc_IndexedMapOfLocation) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : TopLoc_Location) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> TopLoc_Location: 
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
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : TopLoc_Location) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : TopLoc_Location) -> None: 
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
    def __init__(self,theOther : TopLoc_IndexedMapOfLocation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopLoc_ItemLocation():
    """
    An ItemLocation is an elementary coordinate system in a Location.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def __init__(self,D : TopLoc_Datum3D,P : int) -> None: ...
    pass
class TopLoc_Location():
    """
    A Location is a composite transition. It comprises a series of elementary reference coordinates, i.e. objects of type TopLoc_Datum3D, and the powers to which these objects are raised.
    """
    def Divided(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        Returns <me> / <Other>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def FirstDatum(self) -> TopLoc_Datum3D: 
        """
        Returns the first elementary datum of the Location. Use the NextLocation function recursively to access the other data comprising this location. Exceptions Standard_NoSuchObject if this location is empty.

        Returns the first elementary datum of the Location. Use the NextLocation function recursively to access the other data comprising this location. Exceptions Standard_NoSuchObject if this location is empty.
        """
    def FirstPower(self) -> int: 
        """
        Returns the power elevation of the first elementary datum. Exceptions Standard_NoSuchObject if this location is empty.

        Returns the power elevation of the first elementary datum. Exceptions Standard_NoSuchObject if this location is empty.
        """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value for this local coordinate system. This value is used, with map tables, to store and retrieve the object easily, and is in the range [1, theUpperBound].
        """
    def Identity(self) -> None: 
        """
        Resets this location to the Identity transformation.

        Resets this location to the Identity transformation.
        """
    def Inverted(self) -> TopLoc_Location: 
        """
        Returns the inverse of <me>.
        """
    def IsDifferent(self,Other : TopLoc_Location) -> bool: 
        """
        Returns true if this location and the location Other do not have the same elementary data, i.e. do not contain the same series of TopLoc_Datum3D and respective powers. This method is an alias for operator !=.
        """
    def IsEqual(self,Other : TopLoc_Location) -> bool: 
        """
        Returns true if this location and the location Other have the same elementary data, i.e. contain the same series of TopLoc_Datum3D and respective powers. This method is an alias for operator ==.
        """
    def IsIdentity(self) -> bool: 
        """
        Returns true if this location is equal to the Identity transformation.

        Returns true if this location is equal to the Identity transformation.
        """
    def Multiplied(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        Returns <me> * <Other>, the elementary datums are concatenated.
        """
    def NextLocation(self) -> TopLoc_Location: 
        """
        Returns a Location representing <me> without the first datum. We have the relation :

        Returns a Location representing <me> without the first datum. We have the relation :
        """
    def Powered(self,pwr : int) -> TopLoc_Location: 
        """
        Returns me at the power <pwr>. If <pwr> is zero returns Identity. <pwr> can be lower than zero (usual meaning for powers).
        """
    def Predivided(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        Returns <Other>.Inverted() * <me>.
        """
    def ShallowDump(self,S : io.BytesIO) -> None: 
        """
        Prints the contents of <me> on the stream .
        """
    def Transformation(self) -> OCP.gp.gp_Trsf: 
        """
        Returns the transformation associated to the coordinate system.
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
    @overload
    def __init__(self,D : TopLoc_Datum3D) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __mul__(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        None
        """
    def __rmul__(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        None
        """
    def __truediv__(self,Other : TopLoc_Location) -> TopLoc_Location: 
        """
        None
        """
    pass
class TopLoc_MapLocationHasher():
    """
    Purpose: The DefaultHasher is a Hasher that is used by default in NCollection maps. To compute the hash code of the key is used the global function HashCode. To compare two keys is used the global function IsEqual.
    """
    @staticmethod
    def HashCode_s(theKey : TopLoc_Location,theUpperBound : int) -> int: 
        """
        Returns hash code for the given key, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theKey1 : TopLoc_Location,theKey2 : TopLoc_Location) -> bool: 
        """
        None
        """
    pass
class TopLoc_MapOfLocation(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : TopLoc_Location) -> bool: 
        """
        Add
        """
    def Added(self,K : TopLoc_Location) -> TopLoc_Location: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopLoc_MapOfLocation) -> TopLoc_MapOfLocation: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : TopLoc_Location) -> bool: ...
    def Differ(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : TopLoc_MapOfLocation,theRight : TopLoc_MapOfLocation) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : TopLoc_MapOfLocation) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : TopLoc_MapOfLocation) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : TopLoc_MapOfLocation,theRight : TopLoc_MapOfLocation) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : TopLoc_Location) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : TopLoc_MapOfLocation,theRight : TopLoc_MapOfLocation) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : TopLoc_MapOfLocation,theRight : TopLoc_MapOfLocation) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : TopLoc_MapOfLocation) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopLoc_MapOfLocation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopLoc_SListNodeOfItemLocation(OCP.Standard.Standard_Transient):
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
    def Tail(self) -> TopLoc_SListOfItemLocation: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> TopLoc_ItemLocation: 
        """
        None

        None
        """
    def __init__(self,I : TopLoc_ItemLocation,aTail : TopLoc_SListOfItemLocation) -> None: ...
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
class TopLoc_SListOfItemLocation():
    """
    An SListOfItemLocation is a LISP like list of Items. An SListOfItemLocation is : . Empty. . Or it has a Value and a Tail which is an other SListOfItemLocation.
    """
    def Assign(self,Other : TopLoc_SListOfItemLocation) -> TopLoc_SListOfItemLocation: 
        """
        Sets a list from an other one. The lists are shared. The list itself is returned.
        """
    def Clear(self) -> None: 
        """
        Sets the list to be empty.
        """
    def Construct(self,anItem : TopLoc_ItemLocation) -> None: 
        """
        Replaces the list by a list with <anItem> as Value and the list <me> as tail.
        """
    def IsEmpty(self) -> bool: 
        """
        Returne true if this list is empty
        """
    def More(self) -> bool: 
        """
        Returns True if the iterator has a current value. This is !IsEmpty()
        """
    def Next(self) -> None: 
        """
        Moves the iterator to the next object in the list. If the iterator is empty it will stay empty. This is ToTail()
        """
    def Tail(self) -> TopLoc_SListOfItemLocation: 
        """
        Returns the current tail of the list. On an empty list the tail is the list itself.
        """
    def ToTail(self) -> None: 
        """
        Replaces the list <me> by its tail.
        """
    def Value(self) -> TopLoc_ItemLocation: 
        """
        Returns the current value of the list. An error is raised if the list is empty.
        """
    @overload
    def __init__(self,anItem : TopLoc_ItemLocation,aTail : TopLoc_SListOfItemLocation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Other : TopLoc_SListOfItemLocation) -> None: ...
    pass
def HashCode(theLocation : TopLoc_Location,theUpperBound : int) -> int:
    """
    Computes a hash code for the given location, in the range [1, theUpperBound]
    """
@overload
def ShallowDump(me : TopLoc_Location,S : io.BytesIO) -> None:
    """
    None

    None
    """
@overload
def ShallowDump(me : TopLoc_Datum3D,S : io.BytesIO) -> None:
    pass
