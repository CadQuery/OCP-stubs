import OCP.MAT
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Standard
__all__  = [
"MAT_Arc",
"MAT_BasicElt",
"MAT_Bisector",
"MAT_Edge",
"MAT_Graph",
"MAT_ListOfBisector",
"MAT_ListOfEdge",
"MAT_Node",
"MAT_SequenceOfArc",
"MAT_SequenceOfBasicElt",
"MAT_Side",
"MAT_TListNodeOfListOfBisector",
"MAT_TListNodeOfListOfEdge",
"MAT_Zone",
"MAT_Left",
"MAT_Right"
]
class MAT_Arc(OCP.Standard.Standard_Transient):
    """
    An Arc is associated to each Bisecting of the mat.An Arc is associated to each Bisecting of the mat.An Arc is associated to each Bisecting of the mat.
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
    def FirstElement(self) -> MAT_BasicElt: 
        """
        Returns one of the BasicElt equidistant from <me>.
        """
    def FirstNode(self) -> MAT_Node: 
        """
        Returns one Node extremity of <me>.
        """
    def GeomIndex(self) -> int: 
        """
        Returns the index associated of the geometric representation of <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasNeighbour(self,aNode : MAT_Node,aSide : MAT_Side) -> bool: 
        """
        Returnst True is there is an arc linked to the Node <aNode> located on the side <aSide> of <me>; if <aNode> is not on <me>
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self) -> int: 
        """
        Returns the index of <me> in Graph.theArcs.
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
    def Neighbour(self,aNode : MAT_Node,aSide : MAT_Side) -> MAT_Arc: 
        """
        Returns the first arc linked to the Node <aNode> located on the side <aSide> of <me>; if HasNeighbour() returns FALSE.
        """
    def SecondElement(self) -> MAT_BasicElt: 
        """
        Returns the other BasicElt equidistant from <me>.
        """
    def SecondNode(self) -> MAT_Node: 
        """
        Returns the other Node extremity of <me>.
        """
    def SetFirstArc(self,aSide : MAT_Side,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def SetFirstElement(self,aBasicElt : MAT_BasicElt) -> None: 
        """
        None
        """
    def SetFirstNode(self,aNode : MAT_Node) -> None: 
        """
        None
        """
    def SetGeomIndex(self,anInteger : int) -> None: 
        """
        None
        """
    def SetIndex(self,anInteger : int) -> None: 
        """
        None
        """
    def SetNeighbour(self,aSide : MAT_Side,aNode : MAT_Node,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def SetSecondArc(self,aSide : MAT_Side,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def SetSecondElement(self,aBasicElt : MAT_BasicElt) -> None: 
        """
        None
        """
    def SetSecondNode(self,aNode : MAT_Node) -> None: 
        """
        None
        """
    def TheOtherNode(self,aNode : MAT_Node) -> MAT_Node: 
        """
        an Arc has two Node, if <aNode> egal one Returns the other.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,ArcIndex : int,GeomIndex : int,FirstElement : MAT_BasicElt,SecondElement : MAT_BasicElt) -> None: ...
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
class MAT_BasicElt(OCP.Standard.Standard_Transient):
    """
    A BasicELt is associated to each elemtary constituant of the figure.A BasicELt is associated to each elemtary constituant of the figure.A BasicELt is associated to each elemtary constituant of the figure.
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
    def EndArc(self) -> MAT_Arc: 
        """
        Return <endArcLeft> or <endArcRight> corresponding to <aSide>.
        """
    def GeomIndex(self) -> int: 
        """
        Return the <GeomIndex> of <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self) -> int: 
        """
        Return the <index> of <me> in Graph.TheBasicElts.
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
    def SetEndArc(self,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def SetGeomIndex(self,anInteger : int) -> None: 
        """
        None
        """
    def SetIndex(self,anInteger : int) -> None: 
        """
        None
        """
    def SetStartArc(self,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def StartArc(self) -> MAT_Arc: 
        """
        Return <startArcLeft> or <startArcRight> corresponding to <aSide>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,anInteger : int) -> None: ...
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
class MAT_Bisector(OCP.Standard.Standard_Transient):
    def AddBisector(self,abisector : MAT_Bisector) -> None: 
        """
        None
        """
    @overload
    def BisectorNumber(self) -> int: 
        """
        None

        None
        """
    @overload
    def BisectorNumber(self,anumber : int) -> None: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def DistIssuePoint(self,areal : float) -> None: 
        """
        None

        None
        """
    @overload
    def DistIssuePoint(self) -> float: ...
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def EndPoint(self,apoint : int) -> None: 
        """
        None

        None
        """
    @overload
    def EndPoint(self) -> int: ...
    def FirstBisector(self) -> MAT_Bisector: 
        """
        None
        """
    @overload
    def FirstEdge(self,anedge : MAT_Edge) -> None: 
        """
        None

        None
        """
    @overload
    def FirstEdge(self) -> MAT_Edge: ...
    @overload
    def FirstParameter(self) -> float: 
        """
        None

        None
        """
    @overload
    def FirstParameter(self,aparameter : float) -> None: ...
    @overload
    def FirstVector(self,avector : int) -> None: 
        """
        None

        None
        """
    @overload
    def FirstVector(self) -> int: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IndexNumber(self,anumber : int) -> None: 
        """
        None

        None
        """
    @overload
    def IndexNumber(self) -> int: ...
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
    def IssuePoint(self,apoint : int) -> None: 
        """
        None

        None
        """
    @overload
    def IssuePoint(self) -> int: ...
    def LastBisector(self) -> MAT_Bisector: 
        """
        None
        """
    def List(self) -> MAT_ListOfBisector: 
        """
        None
        """
    @overload
    def SecondEdge(self) -> MAT_Edge: 
        """
        None

        None
        """
    @overload
    def SecondEdge(self,anedge : MAT_Edge) -> None: ...
    @overload
    def SecondParameter(self,aparameter : float) -> None: 
        """
        None

        None
        """
    @overload
    def SecondParameter(self) -> float: ...
    @overload
    def SecondVector(self,avector : int) -> None: 
        """
        None

        None
        """
    @overload
    def SecondVector(self) -> int: ...
    @overload
    def Sense(self,asense : float) -> None: 
        """
        None

        None
        """
    @overload
    def Sense(self) -> float: ...
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
class MAT_Edge(OCP.Standard.Standard_Transient):
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
        None

        None
        """
    @overload
    def Distance(self,adistance : float) -> None: ...
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def EdgeNumber(self) -> int: 
        """
        None

        None
        """
    @overload
    def EdgeNumber(self,anumber : int) -> None: ...
    @overload
    def FirstBisector(self,abisector : MAT_Bisector) -> None: 
        """
        None

        None
        """
    @overload
    def FirstBisector(self) -> MAT_Bisector: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def IntersectionPoint(self) -> int: 
        """
        None

        None
        """
    @overload
    def IntersectionPoint(self,apoint : int) -> None: ...
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
    def SecondBisector(self,abisector : MAT_Bisector) -> None: 
        """
        None

        None
        """
    @overload
    def SecondBisector(self) -> MAT_Bisector: ...
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
class MAT_Graph(OCP.Standard.Standard_Transient):
    """
    The Class Graph permits the exploration of the Bisector Locus.The Class Graph permits the exploration of the Bisector Locus.The Class Graph permits the exploration of the Bisector Locus.
    """
    def Arc(self,Index : int) -> MAT_Arc: 
        """
        Return the Arc of index <Index> in <theArcs>.
        """
    def BasicElt(self,Index : int) -> MAT_BasicElt: 
        """
        Return the BasicElt of index <Index> in <theBasicElts>.
        """
    def ChangeBasicElt(self,Index : int) -> MAT_BasicElt: 
        """
        None
        """
    def ChangeBasicElts(self,NewMap : Any) -> None: 
        """
        None
        """
    def CompactArcs(self) -> None: 
        """
        None
        """
    def CompactNodes(self) -> None: 
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
    def FusionOfBasicElts(self,IndexElt1 : int,IndexElt2 : int) -> Tuple[bool, int, int, bool, int, int]: 
        """
        Merge two BasicElts. The End of the BasicElt Elt1 of IndexElt1 becomes The End of the BasicElt Elt2 of IndexElt2. Elt2 is replaced in the arcs by Elt1, Elt2 is eliminated.
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
    def Node(self,Index : int) -> MAT_Node: 
        """
        Return the Node of index <Index> in <theNodes>.
        """
    def NumberOfArcs(self) -> int: 
        """
        Return the number of arcs of <me>.
        """
    def NumberOfBasicElts(self) -> int: 
        """
        Return the number of basic elements of <me>.
        """
    def NumberOfInfiniteNodes(self) -> int: 
        """
        Return the number of infinites nodes of <me>.
        """
    def NumberOfNodes(self) -> int: 
        """
        Return the number of nodes of <me>.
        """
    def Perform(self,SemiInfinite : bool,TheRoots : MAT_ListOfBisector,NbBasicElts : int,NbArcs : int) -> None: 
        """
        Construct <me> from the result of the method <CreateMat> of the class <MAT> from <MAT>.
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
class MAT_ListOfBisector(OCP.Standard.Standard_Transient):
    def BackAdd(self,anitem : MAT_Bisector) -> None: 
        """
        None
        """
    def Brackets(self,anindex : int) -> MAT_Bisector: 
        """
        None
        """
    @overload
    def Current(self,anitem : MAT_Bisector) -> None: 
        """
        None

        None
        """
    @overload
    def Current(self) -> MAT_Bisector: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def First(self) -> None: 
        """
        None
        """
    def FirstItem(self) -> MAT_Bisector: 
        """
        None
        """
    def FrontAdd(self,anitem : MAT_Bisector) -> None: 
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
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,aniten : MAT_Bisector) -> None: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
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
    def Last(self) -> None: 
        """
        None
        """
    def LastItem(self) -> MAT_Bisector: 
        """
        None
        """
    def LinkAfter(self,anitem : MAT_Bisector) -> None: 
        """
        None
        """
    def LinkBefore(self,anitem : MAT_Bisector) -> None: 
        """
        None
        """
    def Loop(self) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def NextItem(self) -> MAT_Bisector: 
        """
        None
        """
    def Number(self) -> int: 
        """
        None
        """
    def Permute(self) -> None: 
        """
        None
        """
    def Previous(self) -> None: 
        """
        None
        """
    def PreviousItem(self) -> MAT_Bisector: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unlink(self) -> None: 
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
class MAT_ListOfEdge(OCP.Standard.Standard_Transient):
    def BackAdd(self,anitem : MAT_Edge) -> None: 
        """
        None
        """
    def Brackets(self,anindex : int) -> MAT_Edge: 
        """
        None
        """
    @overload
    def Current(self,anitem : MAT_Edge) -> None: 
        """
        None

        None
        """
    @overload
    def Current(self) -> MAT_Edge: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def First(self) -> None: 
        """
        None
        """
    def FirstItem(self) -> MAT_Edge: 
        """
        None
        """
    def FrontAdd(self,anitem : MAT_Edge) -> None: 
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
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,aniten : MAT_Edge) -> None: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
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
    def Last(self) -> None: 
        """
        None
        """
    def LastItem(self) -> MAT_Edge: 
        """
        None
        """
    def LinkAfter(self,anitem : MAT_Edge) -> None: 
        """
        None
        """
    def LinkBefore(self,anitem : MAT_Edge) -> None: 
        """
        None
        """
    def Loop(self) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def NextItem(self) -> MAT_Edge: 
        """
        None
        """
    def Number(self) -> int: 
        """
        None
        """
    def Permute(self) -> None: 
        """
        None
        """
    def Previous(self) -> None: 
        """
        None
        """
    def PreviousItem(self) -> MAT_Edge: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unlink(self) -> None: 
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
class MAT_Node(OCP.Standard.Standard_Transient):
    """
    Node of Graph.Node of Graph.Node of Graph.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distance(self) -> float: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GeomIndex(self) -> int: 
        """
        Returns the index associated of the geometric representation of <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self) -> int: 
        """
        Returns the index associated of the node
        """
    def Infinite(self) -> bool: 
        """
        Returns True if the distance of <me> is Infinite
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
    def LinkedArcs(self,S : MAT_SequenceOfArc) -> None: 
        """
        Returns in <S> the Arcs linked to <me>.
        """
    def NearElts(self,S : MAT_SequenceOfBasicElt) -> None: 
        """
        Returns in <S> the BasicElts equidistant to <me>.
        """
    def OnBasicElt(self) -> bool: 
        """
        Returns True if <me> belongs to the figure.
        """
    def PendingNode(self) -> bool: 
        """
        Returns True if <me> is a pending Node. (ie : the number of Arc Linked = 1)
        """
    def SetIndex(self,anIndex : int) -> None: 
        """
        Set the index associated of the node
        """
    def SetLinkedArc(self,anArc : MAT_Arc) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,GeomIndex : int,LinkedArc : MAT_Arc,Distance : float) -> None: ...
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
class MAT_SequenceOfArc(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : MAT_Arc) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MAT_SequenceOfArc) -> None: ...
    def Assign(self,theOther : MAT_SequenceOfArc) -> MAT_SequenceOfArc: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> MAT_Arc: 
        """
        First item access
        """
    def ChangeLast(self) -> MAT_Arc: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> MAT_Arc: 
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
    def First(self) -> MAT_Arc: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : MAT_Arc) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MAT_SequenceOfArc) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MAT_SequenceOfArc) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : MAT_Arc) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> MAT_Arc: 
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
    def Prepend(self,theItem : MAT_Arc) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : MAT_SequenceOfArc) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : MAT_Arc) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MAT_SequenceOfArc) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> MAT_Arc: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : MAT_SequenceOfArc) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MAT_SequenceOfBasicElt(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : MAT_BasicElt) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : MAT_SequenceOfBasicElt) -> None: ...
    def Assign(self,theOther : MAT_SequenceOfBasicElt) -> MAT_SequenceOfBasicElt: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> MAT_BasicElt: 
        """
        First item access
        """
    def ChangeLast(self) -> MAT_BasicElt: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> MAT_BasicElt: 
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
    def First(self) -> MAT_BasicElt: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : MAT_SequenceOfBasicElt) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : MAT_BasicElt) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : MAT_BasicElt) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : MAT_SequenceOfBasicElt) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> MAT_BasicElt: 
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
    def Prepend(self,theItem : MAT_BasicElt) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : MAT_SequenceOfBasicElt) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : MAT_BasicElt) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : MAT_SequenceOfBasicElt) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> MAT_BasicElt: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : MAT_SequenceOfBasicElt) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class MAT_Side():
    """
    Definition on the Left and the Right on the Fig.

    Members:

      MAT_Left

      MAT_Right
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    MAT_Left: OCP.MAT.MAT_Side # value = MAT_Side.MAT_Left
    MAT_Right: OCP.MAT.MAT_Side # value = MAT_Side.MAT_Right
    __entries: dict # value = {'MAT_Left': (MAT_Side.MAT_Left, None), 'MAT_Right': (MAT_Side.MAT_Right, None)}
    __members__: dict # value = {'MAT_Left': MAT_Side.MAT_Left, 'MAT_Right': MAT_Side.MAT_Right}
    pass
class MAT_TListNodeOfListOfBisector(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dummy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetItem(self) -> MAT_Bisector: 
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
    def Next(self,atlistnode : MAT_TListNodeOfListOfBisector) -> None: 
        """
        None

        None
        """
    @overload
    def Next(self) -> MAT_TListNodeOfListOfBisector: ...
    @overload
    def Previous(self,atlistnode : MAT_TListNodeOfListOfBisector) -> None: 
        """
        None

        None
        """
    @overload
    def Previous(self) -> MAT_TListNodeOfListOfBisector: ...
    def SetItem(self,anitem : MAT_Bisector) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,anitem : MAT_Bisector) -> None: ...
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
class MAT_TListNodeOfListOfEdge(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dummy(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetItem(self) -> MAT_Edge: 
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
    def Next(self) -> MAT_TListNodeOfListOfEdge: 
        """
        None

        None
        """
    @overload
    def Next(self,atlistnode : MAT_TListNodeOfListOfEdge) -> None: ...
    @overload
    def Previous(self) -> MAT_TListNodeOfListOfEdge: 
        """
        None

        None
        """
    @overload
    def Previous(self,atlistnode : MAT_TListNodeOfListOfEdge) -> None: ...
    def SetItem(self,anitem : MAT_Edge) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,anitem : MAT_Edge) -> None: ...
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
class MAT_Zone(OCP.Standard.Standard_Transient):
    """
    Definition of Zone of Proximity of a BasicElt : ---------------------------------------------- A Zone of proximity is the set of the points which are more near from the BasicElt than any other.Definition of Zone of Proximity of a BasicElt : ---------------------------------------------- A Zone of proximity is the set of the points which are more near from the BasicElt than any other.Definition of Zone of Proximity of a BasicElt : ---------------------------------------------- A Zone of proximity is the set of the points which are more near from the BasicElt than any other.
    """
    def ArcOnFrontier(self,Index : int) -> MAT_Arc: 
        """
        Return the Arc number <Index> on the frontier. of <me>.
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
    def Limited(self) -> bool: 
        """
        Return TRUE if <me> is Limited.
        """
    def NoEmptyZone(self) -> bool: 
        """
        Return TRUE if <me> is not empty .
        """
    def NumberOfArcs(self) -> int: 
        """
        Return the number Of Arcs On the frontier of <me>.
        """
    def Perform(self,aBasicElt : MAT_BasicElt) -> None: 
        """
        Compute the frontier of the Zone of proximity.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,aBasicElt : MAT_BasicElt) -> None: ...
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
MAT_Left: OCP.MAT.MAT_Side # value = MAT_Side.MAT_Left
MAT_Right: OCP.MAT.MAT_Side # value = MAT_Side.MAT_Right
