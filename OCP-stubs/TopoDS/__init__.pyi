import OCP.TopoDS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopLoc
import OCP.TCollection
import OCP.Message
import OCP.TopAbs
import OCP.Standard
import io
__all__  = [
"TopoDS",
"TopoDS_AlertAttribute",
"TopoDS_AlertWithShape",
"TopoDS_Builder",
"TopoDS_Shape",
"TopoDS_Compound",
"TopoDS_Edge",
"TopoDS_Face",
"TopoDS_FrozenShape",
"TopoDS_HShape",
"TopoDS_Iterator",
"TopoDS_LockedShape",
"TopoDS_CompSolid",
"TopoDS_Shell",
"TopoDS_Solid",
"TopoDS_TShape",
"TopoDS_TCompound",
"TopoDS_TEdge",
"TopoDS_TFace",
"TopoDS_TCompSolid",
"TopoDS_TShell",
"TopoDS_TSolid",
"TopoDS_TVertex",
"TopoDS_TWire",
"TopoDS_UnCompatibleShapes",
"TopoDS_Vertex",
"TopoDS_Wire",
"HashCode",
"TopoDS_Mismatch"
]
class TopoDS():
    """
    Provides methods to cast objects of class TopoDS_Shape to be objects of more specialized sub-classes. Types are verified, thus in the example below, the first two blocks are correct but the third is rejected by the compiler.
    """
    @staticmethod
    @overload
    def CompSolid_s(arg0 : TopoDS_Shape) -> TopoDS_CompSolid: 
        """
        Casts shape S to the more specialized return type, CompSolid. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def CompSolid_s(S : TopoDS_Shape) -> TopoDS_CompSolid: ...
    @staticmethod
    @overload
    def Compound_s(S : TopoDS_Shape) -> TopoDS_Compound: 
        """
        Casts shape S to the more specialized return type, Compound. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Compound_s(arg0 : TopoDS_Shape) -> TopoDS_Compound: ...
    @staticmethod
    @overload
    def Edge_s(S : TopoDS_Shape) -> TopoDS_Edge: 
        """
        Casts shape S to the more specialized return type, Edge Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Edge_s(arg0 : TopoDS_Shape) -> TopoDS_Edge: ...
    @staticmethod
    @overload
    def Face_s(S : TopoDS_Shape) -> TopoDS_Face: 
        """
        Casts shape S to the more specialized return type, Face. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Face_s(arg0 : TopoDS_Shape) -> TopoDS_Face: ...
    @staticmethod
    @overload
    def Shell_s(S : TopoDS_Shape) -> TopoDS_Shell: 
        """
        Casts shape S to the more specialized return type, Shell. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Shell_s(arg0 : TopoDS_Shape) -> TopoDS_Shell: ...
    @staticmethod
    @overload
    def Solid_s(arg0 : TopoDS_Shape) -> TopoDS_Solid: 
        """
        Casts shape S to the more specialized return type, Solid. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Solid_s(S : TopoDS_Shape) -> TopoDS_Solid: ...
    @staticmethod
    @overload
    def Vertex_s(S : TopoDS_Shape) -> TopoDS_Vertex: 
        """
        Basic tool to access the data structure. Casts shape S to the more specialized return type, Vertex. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Vertex_s(arg0 : TopoDS_Shape) -> TopoDS_Vertex: ...
    @staticmethod
    @overload
    def Wire_s(S : TopoDS_Shape) -> TopoDS_Wire: 
        """
        Casts shape S to the more specialized return type, Wire. Exceptions Standard_TypeMismatch if S cannot be cast to this return type.

        None
        """
    @staticmethod
    @overload
    def Wire_s(arg0 : TopoDS_Shape) -> TopoDS_Wire: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_AlertAttribute(OCP.Message.Message_AttributeStream, OCP.Message.Message_Attribute, OCP.Standard.Standard_Transient):
    """
    Alert attribute object storing TopoDS shape in its field
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns custom name of alert if it is set
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> TopoDS_Shape: 
        """
        Returns contained shape
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
    @staticmethod
    def Send_s(theMessenger : OCP.Message.Message_Messenger,theShape : TopoDS_Shape) -> None: 
        """
        Push shape information into messenger
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the custom name of alert
        """
    def SetStream(self,theStream : Any) -> None: 
        """
        Sets stream value
        """
    def Stream(self) -> Any: 
        """
        Returns stream value
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theShape : TopoDS_Shape,theName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class TopoDS_AlertWithShape(OCP.Message.Message_Alert, OCP.Standard.Standard_Transient):
    """
    Alert object storing TopoDS shape in its field
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
    def GetMessageKey(self) -> str: 
        """
        Return a C string to be used as a key for generating text user messages describing this alert. The messages are generated with help of Message_Msg class, in Message_Report::Dump(). Base implementation returns dynamic type name of the instance.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetShape(self) -> TopoDS_Shape: 
        """
        Returns contained shape
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
    def Merge(self,theTarget : OCP.Message.Message_Alert) -> bool: 
        """
        Returns false.
        """
    def SetShape(self,theShape : TopoDS_Shape) -> None: 
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
    def __init__(self,theShape : TopoDS_Shape) -> None: ...
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
class TopoDS_Builder():
    """
    A Builder is used to create Topological Data Structures.It is the root of the Builder class hierarchy.
    """
    def Add(self,S : TopoDS_Shape,C : TopoDS_Shape) -> None: 
        """
        Add the Shape C in the Shape S. Exceptions - TopoDS_FrozenShape if S is not free and cannot be modified. - TopoDS__UnCompatibleShapes if S and C are not compatible.
        """
    def MakeCompSolid(self,C : TopoDS_CompSolid) -> None: 
        """
        Make an empty Composite Solid.

        Make an empty Composite Solid.
        """
    def MakeCompound(self,C : TopoDS_Compound) -> None: 
        """
        Make an empty Compound.

        Make an empty Compound.
        """
    def MakeShell(self,S : TopoDS_Shell) -> None: 
        """
        Make an empty Shell.

        Make an empty Shell.
        """
    def MakeSolid(self,S : TopoDS_Solid) -> None: 
        """
        Make a Solid covering the whole 3D space.

        Make a Solid covering the whole 3D space.
        """
    def MakeWire(self,W : TopoDS_Wire) -> None: 
        """
        Make an empty Wire.

        Make an empty Wire.
        """
    def Remove(self,S : TopoDS_Shape,C : TopoDS_Shape) -> None: 
        """
        Remove the Shape C from the Shape S. Exceptions TopoDS_FrozenShape if S is frozen and cannot be modified.
        """
    def __init__(self) -> None: ...
    pass
class TopoDS_Shape():
    """
    Describes a shape which - references an underlying shape with the potential to be given a location and an orientation - has a location for the underlying shape, giving its placement in the local coordinate system - has an orientation for the underlying shape, in terms of its geometry (as opposed to orientation in relation to other shapes). Note: A Shape is empty if it references an underlying shape which has an empty list of shapes.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Compound(TopoDS_Shape):
    """
    Describes a compound which - references an underlying compound with the potential to be given a location and an orientation - has a location for the underlying compound, giving its placement in the local coordinate system - has an orientation for the underlying compound, in terms of its geometry (as opposed to orientation in relation to other shapes). Casts shape S to the more specialized return type, Compound.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Edge(TopoDS_Shape):
    """
    Describes an edge which - references an underlying edge with the potential to be given a location and an orientation - has a location for the underlying edge, giving its placement in the local coordinate system - has an orientation for the underlying edge, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Face(TopoDS_Shape):
    """
    Describes a face which - references an underlying face with the potential to be given a location and an orientation - has a location for the underlying face, giving its placement in the local coordinate system - has an orientation for the underlying face, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_FrozenShape(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.TopoDS', '__weakref__': <attribute '__weakref__' of 'TopoDS_FrozenShape' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'TopoDS_FrozenShape' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class TopoDS_HShape(OCP.Standard.Standard_Transient):
    """
    Class to manipulate a Shape with handle.Class to manipulate a Shape with handle.Class to manipulate a Shape with handle.
    """
    def ChangeShape(self) -> TopoDS_Shape: 
        """
        Exchanges the TopoDS_Shape object defining this shape for another one referencing the same underlying shape Accesses the list of shapes within the underlying shape referenced by the TopoDS_Shape object. Returns a reference to a TopoDS_Shape based on this shape. The TopoDS_Shape can be modified.

        Exchanges the TopoDS_Shape object defining this shape for another one referencing the same underlying shape Accesses the list of shapes within the underlying shape referenced by the TopoDS_Shape object. Returns a reference to a TopoDS_Shape based on this shape. The TopoDS_Shape can be modified.
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
    @overload
    def Shape(self) -> TopoDS_Shape: 
        """
        Loads this shape with the shape aShape

        Loads this shape with the shape aShape

        Returns a reference to a constant TopoDS_Shape based on this shape.

        Returns a reference to a constant TopoDS_Shape based on this shape.
        """
    @overload
    def Shape(self,aShape : TopoDS_Shape) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,aShape : TopoDS_Shape) -> None: ...
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
class TopoDS_Iterator():
    """
    Iterates on the underlying shape underlying a given TopoDS_Shape object, providing access to its component sub-shapes. Each component shape is returned as a TopoDS_Shape with an orientation, and a compound of the original values and the relative values.
    """
    def Initialize(self,S : TopoDS_Shape,cumOri : bool=True,cumLoc : bool=True) -> None: 
        """
        Initializes this iterator with shape S. Note: - If cumOri is true, the function composes all sub-shapes with the orientation of S. - If cumLoc is true, the function multiplies all sub-shapes by the location of S, i.e. it applies to each sub-shape the transformation that is associated with S.
        """
    def More(self) -> bool: 
        """
        Returns true if there is another sub-shape in the shape which this iterator is scanning.
        """
    def Next(self) -> None: 
        """
        Moves on to the next sub-shape in the shape which this iterator is scanning. Exceptions Standard_NoMoreObject if there are no more sub-shapes in the shape.
        """
    def Value(self) -> TopoDS_Shape: 
        """
        Returns the current sub-shape in the shape which this iterator is scanning. Exceptions Standard_NoSuchObject if there is no current sub-shape.
        """
    @overload
    def __init__(self,S : TopoDS_Shape,cumOri : bool=True,cumLoc : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopoDS_LockedShape(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.TopoDS', '__weakref__': <attribute '__weakref__' of 'TopoDS_LockedShape' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'TopoDS_LockedShape' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class TopoDS_CompSolid(TopoDS_Shape):
    """
    Describes a composite solid which - references an underlying composite solid with the potential to be given a location and an orientation - has a location for the underlying composite solid, giving its placement in the local coordinate system - has an orientation for the underlying composite solid, in terms of its geometry (as opposed to orientation in relation to other shapes). Casts shape S to the more specialized return type, CompSolid.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Shell(TopoDS_Shape):
    """
    Describes a shell which - references an underlying shell with the potential to be given a location and an orientation - has a location for the underlying shell, giving its placement in the local coordinate system - has an orientation for the underlying shell, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Solid(TopoDS_Shape):
    """
    Describes a solid shape which - references an underlying solid shape with the potential to be given a location and an orientation - has a location for the underlying shape, giving its placement in the local coordinate system - has an orientation for the underlying shape, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_TShape(OCP.Standard.Standard_Transient):
    """
    A TShape is a topological structure describing a set of points in a 2D or 3D space.A TShape is a topological structure describing a set of points in a 2D or 3D space.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the type as a term of the ShapeEnum enum : VERTEX, EDGE, WIRE, FACE, ....
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class TopoDS_TCompound(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A TCompound is an all-purpose set of Shapes.A TCompound is an all-purpose set of Shapes.A TCompound is an all-purpose set of Shapes.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TCompound.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns COMPOUND.
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
class TopoDS_TEdge(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A topological part of a curve in 2D or 3D, the boundary is a set of oriented Vertices.A topological part of a curve in 2D or 3D, the boundary is a set of oriented Vertices.A topological part of a curve in 2D or 3D, the boundary is a set of oriented Vertices.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns EDGE.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class TopoDS_TFace(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A topological part of a surface or of the 2D space. The boundary is a set of wires and vertices.A topological part of a surface or of the 2D space. The boundary is a set of wires and vertices.A topological part of a surface or of the 2D space. The boundary is a set of wires and vertices.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TFace.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        returns FACE.
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
class TopoDS_TCompSolid(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A set of solids connected by their faces.A set of solids connected by their faces.A set of solids connected by their faces.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TCompSolid.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        returns COMPSOLID
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
class TopoDS_TShell(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A set of faces connected by their edges.A set of faces connected by their edges.A set of faces connected by their edges.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TShell.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns SHELL.
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
class TopoDS_TSolid(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A Topological part of 3D space, bounded by shells, edges and vertices.A Topological part of 3D space, bounded by shells, edges and vertices.A Topological part of 3D space, bounded by shells, edges and vertices.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TSolid.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        returns SOLID.
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
class TopoDS_TVertex(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A Vertex is a topological point in two or three dimensions.A Vertex is a topological point in two or three dimensions.A Vertex is a topological point in two or three dimensions.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns a copy of the TShape with no sub-shapes.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns VERTEX.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class TopoDS_TWire(TopoDS_TShape, OCP.Standard.Standard_Transient):
    """
    A set of edges connected by their vertices.A set of edges connected by their vertices.A set of edges connected by their vertices.
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self) -> bool: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self,theIsClosed : bool) -> None: ...
    @overload
    def Convex(self,theIsConvex : bool) -> None: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self) -> bool: ...
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
    def EmptyCopy(self) -> TopoDS_TShape: 
        """
        Returns an empty TWire.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self) -> bool: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
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
    def Locked(self) -> bool: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self,theIsLocked : bool) -> None: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns WIRE.
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
class TopoDS_UnCompatibleShapes(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.TopoDS', '__weakref__': <attribute '__weakref__' of 'TopoDS_UnCompatibleShapes' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'TopoDS_UnCompatibleShapes' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class TopoDS_Vertex(TopoDS_Shape):
    """
    Describes a vertex which - references an underlying vertex with the potential to be given a location and an orientation - has a location for the underlying vertex, giving its placement in the local coordinate system - has an orientation for the underlying vertex, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
class TopoDS_Wire(TopoDS_Shape):
    """
    Describes a wire which - references an underlying wire with the potential to be given a location and an orientation - has a location for the underlying wire, giving its placement in the local coordinate system - has an orientation for the underlying wire, in terms of its geometry (as opposed to orientation in relation to other shapes).
    """
    @overload
    def Checked(self) -> bool: 
        """
        Returns the checked flag.

        Sets the checked flag.
        """
    @overload
    def Checked(self,theIsChecked : bool) -> None: ...
    @overload
    def Closed(self,theIsClosed : bool) -> None: 
        """
        Returns the closedness flag.

        Sets the closedness flag.
        """
    @overload
    def Closed(self) -> bool: ...
    def Complement(self) -> None: 
        """
        Complements the orientation, using the Complement method from the TopAbs package.
        """
    def Complemented(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation complemented, using the Complement method from the TopAbs package.
        """
    def Compose(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the Shape Orientation by composition with theOrient, using the Compose method from the TopAbs package.
        """
    def Composed(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation composed with theOrient, using the Compose method from the TopAbs package.
        """
    @overload
    def Convex(self) -> bool: 
        """
        Returns the convexness flag.

        Sets the convexness flag.
        """
    @overload
    def Convex(self,theIsConvex : bool) -> None: ...
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EmptyCopied(self) -> TopoDS_Shape: 
        """
        Returns a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    def EmptyCopy(self) -> None: 
        """
        Replace <me> by a new Shape with the same Orientation and Location and a new TShape with the same geometry and no sub-shapes.
        """
    @overload
    def Free(self) -> bool: 
        """
        Returns the free flag.

        Sets the free flag.
        """
    @overload
    def Free(self,theIsFree : bool) -> None: ...
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Returns a hashed value denoting <me>. This value is in the range [1, theUpperBound]. It is computed from the TShape and the Location. The Orientation is not used.
        """
    @overload
    def Infinite(self) -> bool: 
        """
        Returns the infinity flag.

        Sets the infinity flag.
        """
    @overload
    def Infinite(self,theIsInfinite : bool) -> None: ...
    def IsEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are equal, i.e. if they share the same TShape with the same Locations and Orientations.
        """
    def IsNotEqual(self,theOther : TopoDS_Shape) -> bool: 
        """
        Negation of the IsEqual method.
        """
    def IsNull(self) -> bool: 
        """
        Returns true if this shape is null. In other words, it references no underlying shape with the potential to be given a location and an orientation.
        """
    def IsPartner(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are partners, i.e. if they share the same TShape. Locations and Orientations may differ.
        """
    def IsSame(self,theOther : TopoDS_Shape) -> bool: 
        """
        Returns True if two shapes are same, i.e. if they share the same TShape with the same Locations. Orientations may differ.
        """
    def Located(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the local coordinate system set to <Loc>.
        """
    @overload
    def Location(self) -> OCP.TopLoc.TopLoc_Location: 
        """
        Sets the shape local coordinate system.

        Returns the shape local coordinate system.
        """
    @overload
    def Location(self,theLoc : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: ...
    @overload
    def Locked(self,theIsLocked : bool) -> None: 
        """
        Returns the locked flag.

        Sets the locked flag.
        """
    @overload
    def Locked(self) -> bool: ...
    @overload
    def Modified(self) -> bool: 
        """
        Returns the modification flag.

        Sets the modification flag.
        """
    @overload
    def Modified(self,theIsModified : bool) -> None: ...
    def Move(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> None: 
        """
        Multiplies the Shape location by thePosition.
        """
    def Moved(self,thePosition : OCP.TopLoc.TopLoc_Location,theRaiseExc : bool=True) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with a location multiplied by thePosition.
        """
    def NbChildren(self) -> int: 
        """
        Returns the number of direct sub-shapes (children).
        """
    def Nullify(self) -> None: 
        """
        Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.
        """
    @overload
    def Orientable(self,theIsOrientable : bool) -> None: 
        """
        Returns the orientability flag.

        Sets the orientability flag.
        """
    @overload
    def Orientable(self) -> bool: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation.

        Sets the shape orientation.
        """
    @overload
    def Orientation(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def Oriented(self,theOrient : OCP.TopAbs.TopAbs_Orientation) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation set to <Or>.
        """
    def Reverse(self) -> None: 
        """
        Reverses the orientation, using the Reverse method from the TopAbs package.
        """
    def Reversed(self) -> TopoDS_Shape: 
        """
        Returns a shape similar to <me> with the orientation reversed, using the Reverse method from the TopAbs package.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the value of the TopAbs_ShapeEnum enumeration that corresponds to this shape, for example VERTEX, EDGE, and so on. Exceptions Standard_NullObject if this shape is null.
        """
    @overload
    def TShape(self,theTShape : TopoDS_TShape) -> None: 
        """
        None

        Returns a handle to the actual shape implementation.
        """
    @overload
    def TShape(self) -> TopoDS_TShape: ...
    def __init__(self) -> None: ...
    pass
def HashCode(theShape : TopoDS_Shape,theUpperBound : int) -> int:
    """
    Computes a hash code for the given shape, in the range [1, theUpperBound]
    """
def TopoDS_Mismatch(S : TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum) -> bool:
    """
    None
    """
