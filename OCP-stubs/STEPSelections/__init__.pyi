import OCP.STEPSelections
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.StepRepr
import OCP.StepBasic
import OCP.NCollection
import OCP.Transfer
import io
import OCP.Standard
import OCP.StepShape
import OCP.IFSelect
import OCP.Interface
import OCP.XSControl
import OCP.TCollection
__all__  = [
"STEPSelections_AssemblyComponent",
"STEPSelections_AssemblyExplorer",
"STEPSelections_AssemblyLink",
"STEPSelections_Counter",
"STEPSelections_SequenceOfAssemblyLink",
"STEPSelections_SelectAssembly",
"STEPSelections_SelectDerived",
"STEPSelections_SelectFaces",
"STEPSelections_SelectForTransfer",
"STEPSelections_SelectGSCurves",
"STEPSelections_SelectInstances",
"STEPSelections_SequenceOfAssemblyComponent",
"STEPSelections_HSequenceOfAssemblyLink"
]
class STEPSelections_AssemblyComponent(OCP.Standard.Standard_Transient):
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
    def GetList(self) -> STEPSelections_HSequenceOfAssemblyLink: 
        """
        None

        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSDR(self) -> OCP.StepShape.StepShape_ShapeDefinitionRepresentation: 
        """
        None

        None
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
    def SetList(self,list : STEPSelections_HSequenceOfAssemblyLink) -> None: 
        """
        None

        None
        """
    def SetSDR(self,sdr : OCP.StepShape.StepShape_ShapeDefinitionRepresentation) -> None: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,sdr : OCP.StepShape.StepShape_ShapeDefinitionRepresentation,list : STEPSelections_HSequenceOfAssemblyLink) -> None: ...
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
class STEPSelections_AssemblyExplorer():
    """
    None
    """
    def Dump(self,os : io.BytesIO) -> None: 
        """
        None
        """
    def FillListWithGraph(self,cmp : STEPSelections_AssemblyComponent) -> None: 
        """
        None
        """
    def FindItemWithNAUO(self,nauo : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def FindSDRWithProduct(self,product : OCP.StepBasic.StepBasic_ProductDefinition) -> OCP.StepShape.StepShape_ShapeDefinitionRepresentation: 
        """
        None
        """
    def Init(self,G : OCP.Interface.Interface_Graph) -> None: 
        """
        None
        """
    def NbAssemblies(self) -> int: 
        """
        Returns the number of root assemblies;

        Returns the number of root assemblies;
        """
    @overload
    def Root(self,rank : int=1) -> STEPSelections_AssemblyComponent: 
        """
        Returns root of assenbly by its rank;

        Returns root of assenbly by its rank;
        """
    @overload
    def Root(self,rank : int) -> STEPSelections_AssemblyComponent: ...
    def __init__(self,G : OCP.Interface.Interface_Graph) -> None: ...
    pass
class STEPSelections_AssemblyLink(OCP.Standard.Standard_Transient):
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
    def GetComponent(self) -> STEPSelections_AssemblyComponent: 
        """
        None

        None
        """
    def GetItem(self) -> OCP.Standard.Standard_Transient: 
        """
        None

        None
        """
    def GetNAUO(self) -> OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence: 
        """
        None

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
    def SetComponent(self,part : STEPSelections_AssemblyComponent) -> None: 
        """
        None

        None
        """
    def SetItem(self,item : OCP.Standard.Standard_Transient) -> None: 
        """
        None

        None
        """
    def SetNAUO(self,nauo : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence) -> None: 
        """
        None

        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,nauo : OCP.StepRepr.StepRepr_NextAssemblyUsageOccurrence,item : OCP.Standard.Standard_Transient,part : STEPSelections_AssemblyComponent) -> None: ...
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
class STEPSelections_Counter():
    """
    None
    """
    def Clear(self) -> None: 
        """
        None
        """
    def Count(self,graph : OCP.Interface.Interface_Graph,start : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def NbInstancesOfEdges(self) -> int: 
        """
        None

        None
        """
    def NbInstancesOfFaces(self) -> int: 
        """
        None

        None
        """
    def NbInstancesOfShells(self) -> int: 
        """
        None

        None
        """
    def NbInstancesOfSolids(self) -> int: 
        """
        None

        None
        """
    def NbInstancesOfWires(self) -> int: 
        """
        None

        None
        """
    def NbSourceEdges(self) -> int: 
        """
        None

        None
        """
    def NbSourceFaces(self) -> int: 
        """
        None

        None
        """
    def NbSourceShells(self) -> int: 
        """
        None

        None
        """
    def NbSourceSolids(self) -> int: 
        """
        None

        None
        """
    def NbSourceWires(self) -> int: 
        """
        None

        None
        """
    def __init__(self) -> None: ...
    pass
class STEPSelections_SequenceOfAssemblyLink(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : STEPSelections_AssemblyLink) -> None: ...
    def Assign(self,theOther : STEPSelections_SequenceOfAssemblyLink) -> STEPSelections_SequenceOfAssemblyLink: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> STEPSelections_AssemblyLink: 
        """
        First item access
        """
    def ChangeLast(self) -> STEPSelections_AssemblyLink: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> STEPSelections_AssemblyLink: 
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
    def First(self) -> STEPSelections_AssemblyLink: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> STEPSelections_AssemblyLink: 
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
    def Prepend(self,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> STEPSelections_AssemblyLink: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class STEPSelections_SelectAssembly(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def Explore(self,level : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        Explores an entity, to take its faces Works recursively
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Assembly structures"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus specific criterium returned by ExploreLabel (see below)
        """
    def Level(self) -> int: 
        """
        Returns the required exploring level
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Explore on each input entity : it can be rejected, taken for output, or to explore. If the maximum level has not yet been attained, or if no max level is specified, entities to be explored are themselves used as if they were input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class STEPSelections_SelectDerived():
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel,text : OCP.TCollection.TCollection_AsciiString,exact : bool) -> bool: 
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
class STEPSelections_SelectFaces(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection returns "STEP faces"This selection returns "STEP faces"This selection returns "STEP faces"
    """
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def Explore(self,level : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        Explores an entity, to take its faces Works recursively
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Faces"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus specific criterium returned by ExploreLabel (see below)
        """
    def Level(self) -> int: 
        """
        Returns the required exploring level
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Explore on each input entity : it can be rejected, taken for output, or to explore. If the maximum level has not yet been attained, or if no max level is specified, entities to be explored are themselves used as if they were input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class STEPSelections_SelectForTransfer(OCP.XSControl.XSControl_SelectForTransfer, OCP.IFSelect.IFSelect_SelectExtract, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    def Actor(self) -> OCP.Transfer.Transfer_ActorOfTransientProcess: 
        """
        Returns the Actor used as precised one. Returns a Null Handle for a creation from a TransferReader without any further setting
        """
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def ExtractLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Recognized for Transfer [(current actor)]"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
        """
    def IsDirect(self) -> bool: 
        """
        Returns True if Sort criterium is Direct, False if Reverse
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "Picked" or "Removed", plus the specific criterium returned by ExtractLabel (see below)
        """
    def Reader(self) -> OCP.XSControl.XSControl_TransferReader: 
        """
        Returns the Reader (if created with a Reader) Returns a Null Handle if not created with a Reader
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        None
        """
    def SetActor(self,act : OCP.Transfer.Transfer_ActorOfTransientProcess) -> None: 
        """
        Sets a precise actor to sort entities This definition oversedes the creation with a TransferReader
        """
    def SetDirect(self,direct : bool) -> None: 
        """
        Sets Sort criterium sense to a new value (True : Direct , False : Reverse)
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def SetReader(self,TR : OCP.XSControl.XSControl_TransferReader) -> None: 
        """
        Sets a TransferReader to sort entities : it brings the Actor, which may change, while the TransferReader does not
        """
    def Sort(self,rank : int,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        Returns True for an Entity which is recognized by the Actor, either the precised one, or the one defined by TransferReader
        """
    def SortInGraph(self,rank : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph) -> bool: 
        """
        Works as Sort but works on the Graph Default directly calls Sort, but it can be redefined If SortInGraph is redefined, Sort should be defined even if not called (to avoid deferred methods in a final class)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
        """
    @overload
    def __init__(self,TR : OCP.XSControl.XSControl_TransferReader) -> None: ...
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
class STEPSelections_SelectGSCurves(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    """
    This selection returns "curves in the geometric_set (except composite curves)"This selection returns "curves in the geometric_set (except composite curves)"This selection returns "curves in the geometric_set (except composite curves)"
    """
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def Explore(self,level : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        None
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Curves"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus specific criterium returned by ExploreLabel (see below)
        """
    def Level(self) -> int: 
        """
        Returns the required exploring level
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities. Works by calling the method Explore on each input entity : it can be rejected, taken for output, or to explore. If the maximum level has not yet been attained, or if no max level is specified, entities to be explored are themselves used as if they were input
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class STEPSelections_SelectInstances(OCP.IFSelect.IFSelect_SelectExplore, OCP.IFSelect.IFSelect_SelectDeduct, OCP.IFSelect.IFSelect_Selection, OCP.Standard.Standard_Transient):
    def Alternate(self) -> OCP.IFSelect.IFSelect_SelectPointed: 
        """
        Returns the Alternate Definition It is returned modifiable, hence an already defined SelectPointed can be used But if it was not yet defined, it is created the first time
        """
    def CompleteResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities involved by a Selection, i.e. UniqueResult plus the shared entities (directly or not)
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
    def Explore(self,level : int,ent : OCP.Standard.Standard_Transient,G : OCP.Interface.Interface_Graph,explored : OCP.Interface.Interface_EntityIterator) -> bool: 
        """
        None
        """
    def ExploreLabel(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text defining the criterium : "Instances"
        """
    def FillIterator(self,iter : OCP.IFSelect.IFSelect_SelectionIterator) -> None: 
        """
        Puts in an Iterator the Selections from which "me" depends This list contains one Selection : the InputSelection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlternate(self) -> bool: 
        """
        Tells if an Alternate List has been set, i.e. : the Alternate Definition is present and set
        """
    def HasInput(self) -> bool: 
        """
        Returns True if the Input Selection is defined, False else
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.IFSelect.IFSelect_Selection: 
        """
        Returns the Input Selection
        """
    def InputResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the Result determined by Input Selection, as Unique if Input Selection is not defined, returns an empty list.
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
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a text saying "(Recursive)" or "(Level nn)" plus specific criterium returned by ExploreLabel (see below)
        """
    def Level(self) -> int: 
        """
        Returns the required exploring level
        """
    def RootResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        None
        """
    def SetInput(self,sel : OCP.IFSelect.IFSelect_Selection) -> None: 
        """
        Defines or Changes the Input Selection
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UniqueResult(self,G : OCP.Interface.Interface_Graph) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of selected entities, each of them being unique. Default definition works from RootResult. According HasUniqueResult, UniqueResult returns directly RootResult, or build a Unique Result from it with a Graph.
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
class STEPSelections_SequenceOfAssemblyComponent(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : STEPSelections_AssemblyComponent) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : STEPSelections_SequenceOfAssemblyComponent) -> None: ...
    def Assign(self,theOther : STEPSelections_SequenceOfAssemblyComponent) -> STEPSelections_SequenceOfAssemblyComponent: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> STEPSelections_AssemblyComponent: 
        """
        First item access
        """
    def ChangeLast(self) -> STEPSelections_AssemblyComponent: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> STEPSelections_AssemblyComponent: 
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
    def First(self) -> STEPSelections_AssemblyComponent: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : STEPSelections_AssemblyComponent) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyComponent) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : STEPSelections_AssemblyComponent) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyComponent) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> STEPSelections_AssemblyComponent: 
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
    def Prepend(self,theItem : STEPSelections_AssemblyComponent) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : STEPSelections_SequenceOfAssemblyComponent) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : STEPSelections_AssemblyComponent) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyComponent) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> STEPSelections_AssemblyComponent: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : STEPSelections_SequenceOfAssemblyComponent) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class STEPSelections_HSequenceOfAssemblyLink(STEPSelections_SequenceOfAssemblyLink, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    def Assign(self,theOther : STEPSelections_SequenceOfAssemblyLink) -> STEPSelections_SequenceOfAssemblyLink: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> STEPSelections_AssemblyLink: 
        """
        First item access
        """
    def ChangeLast(self) -> STEPSelections_AssemblyLink: 
        """
        Last item access
        """
    def ChangeSequence(self) -> STEPSelections_SequenceOfAssemblyLink: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> STEPSelections_AssemblyLink: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
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
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> STEPSelections_AssemblyLink: 
        """
        First item access
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
    def InsertAfter(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
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
    def Last(self) -> STEPSelections_AssemblyLink: 
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
    def Prepend(self,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def Sequence(self) -> STEPSelections_SequenceOfAssemblyLink: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : STEPSelections_AssemblyLink) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : STEPSelections_SequenceOfAssemblyLink) -> None: 
        """
        Split in two sequences
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> STEPSelections_AssemblyLink: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : STEPSelections_SequenceOfAssemblyLink) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
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
