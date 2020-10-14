import OCP.ExprIntrp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TCollection
import OCP.Expr
import OCP.Standard
__all__  = [
"ExprIntrp",
"ExprIntrp_Analysis",
"ExprIntrp_Generator",
"ExprIntrp_GenFct",
"ExprIntrp_GenRel",
"ExprIntrp_GenExp",
"ExprIntrp_SequenceOfNamedExpression",
"ExprIntrp_SequenceOfNamedFunction",
"ExprIntrp_StackOfGeneralExpression",
"ExprIntrp_StackOfGeneralFunction",
"ExprIntrp_StackOfGeneralRelation",
"ExprIntrp_SyntaxError",
"ExprIntrp_GetDegree",
"ExprIntrp_GetResult"
]
class ExprIntrp():
    """
    Describes an interpreter for GeneralExpressions, GeneralFunctions, and GeneralRelations defined in package Expr.
    """
    def __init__(self) -> None: ...
    pass
class ExprIntrp_Analysis():
    """
    None
    """
    def GetFunction(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedFunction: 
        """
        None
        """
    def GetNamed(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedExpression: 
        """
        None
        """
    def IsExpStackEmpty(self) -> bool: 
        """
        None
        """
    def IsRelStackEmpty(self) -> bool: 
        """
        None
        """
    def Pop(self) -> OCP.Expr.Expr_GeneralExpression: 
        """
        None
        """
    def PopFunction(self) -> OCP.Expr.Expr_GeneralFunction: 
        """
        None
        """
    def PopName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def PopRelation(self) -> OCP.Expr.Expr_GeneralRelation: 
        """
        None
        """
    def PopValue(self) -> int: 
        """
        None
        """
    def Push(self,exp : OCP.Expr.Expr_GeneralExpression) -> None: 
        """
        None
        """
    def PushFunction(self,func : OCP.Expr.Expr_GeneralFunction) -> None: 
        """
        None
        """
    def PushName(self,name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def PushRelation(self,rel : OCP.Expr.Expr_GeneralRelation) -> None: 
        """
        None
        """
    def PushValue(self,degree : int) -> None: 
        """
        None
        """
    def ResetAll(self) -> None: 
        """
        None
        """
    def SetMaster(self,agen : ExprIntrp_Generator) -> None: 
        """
        None
        """
    @overload
    def Use(self,named : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        None

        None
        """
    @overload
    def Use(self,func : OCP.Expr.Expr_NamedFunction) -> None: ...
    def __init__(self) -> None: ...
    pass
class ExprIntrp_Generator(OCP.Standard.Standard_Transient):
    """
    Implements general services for interpretation of expressions.Implements general services for interpretation of expressions.Implements general services for interpretation of expressions.
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
    def GetFunction(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedFunction: 
        """
        Returns NamedFunction with name <name> already interpreted if it exists. Returns a null handle if not.
        """
    def GetFunctions(self) -> ExprIntrp_SequenceOfNamedFunction: 
        """
        None
        """
    @overload
    def GetNamed(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedExpression: 
        """
        Returns NamedExpression with name <name> already interpreted if it exists. Returns a null handle if not.

        None
        """
    @overload
    def GetNamed(self) -> ExprIntrp_SequenceOfNamedExpression: ...
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Use(self,named : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        None

        None
        """
    @overload
    def Use(self,func : OCP.Expr.Expr_NamedFunction) -> None: ...
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
class ExprIntrp_GenFct(ExprIntrp_Generator, OCP.Standard.Standard_Transient):
    """
    Implements an interpreter for defining functions. All its functionnalities can be found in class GenExp.Implements an interpreter for defining functions. All its functionnalities can be found in class GenExp.Implements an interpreter for defining functions. All its functionnalities can be found in class GenExp.
    """
    @staticmethod
    def Create_s() -> ExprIntrp_GenFct: 
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
    def GetFunction(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedFunction: 
        """
        Returns NamedFunction with name <name> already interpreted if it exists. Returns a null handle if not.
        """
    def GetFunctions(self) -> ExprIntrp_SequenceOfNamedFunction: 
        """
        None
        """
    @overload
    def GetNamed(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedExpression: 
        """
        Returns NamedExpression with name <name> already interpreted if it exists. Returns a null handle if not.

        None
        """
    @overload
    def GetNamed(self) -> ExprIntrp_SequenceOfNamedExpression: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
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
    def Process(self,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Use(self,named : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        None

        None
        """
    @overload
    def Use(self,func : OCP.Expr.Expr_NamedFunction) -> None: ...
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
class ExprIntrp_GenRel(ExprIntrp_Generator, OCP.Standard.Standard_Transient):
    """
    Implements an interpreter for equations or system of equations made of expressions of package Expr.Implements an interpreter for equations or system of equations made of expressions of package Expr.Implements an interpreter for equations or system of equations made of expressions of package Expr.
    """
    @staticmethod
    def Create_s() -> ExprIntrp_GenRel: 
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
    def GetFunction(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedFunction: 
        """
        Returns NamedFunction with name <name> already interpreted if it exists. Returns a null handle if not.
        """
    def GetFunctions(self) -> ExprIntrp_SequenceOfNamedFunction: 
        """
        None
        """
    @overload
    def GetNamed(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedExpression: 
        """
        Returns NamedExpression with name <name> already interpreted if it exists. Returns a null handle if not.

        None
        """
    @overload
    def GetNamed(self) -> ExprIntrp_SequenceOfNamedExpression: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Returns false if any syntax error has occurred during process.
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
    def Process(self,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Processes given string.
        """
    def Relation(self) -> OCP.Expr.Expr_GeneralRelation: 
        """
        Returns relation generated. Raises an exception if IsDone answers false.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Use(self,named : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        None

        None
        """
    @overload
    def Use(self,func : OCP.Expr.Expr_NamedFunction) -> None: ...
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
class ExprIntrp_GenExp(ExprIntrp_Generator, OCP.Standard.Standard_Transient):
    """
    This class permits, from a string, to create any kind of expression of package Expr by using built-in functions such as Sin,Cos, etc, and by creating variables.This class permits, from a string, to create any kind of expression of package Expr by using built-in functions such as Sin,Cos, etc, and by creating variables.This class permits, from a string, to create any kind of expression of package Expr by using built-in functions such as Sin,Cos, etc, and by creating variables.
    """
    @staticmethod
    def Create_s() -> ExprIntrp_GenExp: 
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
    def Expression(self) -> OCP.Expr.Expr_GeneralExpression: 
        """
        Returns expression generated. Raises an exception if IsDone answers false.
        """
    def GetFunction(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedFunction: 
        """
        Returns NamedFunction with name <name> already interpreted if it exists. Returns a null handle if not.
        """
    def GetFunctions(self) -> ExprIntrp_SequenceOfNamedFunction: 
        """
        None
        """
    @overload
    def GetNamed(self,name : OCP.TCollection.TCollection_AsciiString) -> OCP.Expr.Expr_NamedExpression: 
        """
        Returns NamedExpression with name <name> already interpreted if it exists. Returns a null handle if not.

        None
        """
    @overload
    def GetNamed(self) -> ExprIntrp_SequenceOfNamedExpression: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Returns false if any syntax error has occurred during process.
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
    def Process(self,str : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Processes given string.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Use(self,named : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        None

        None
        """
    @overload
    def Use(self,func : OCP.Expr.Expr_NamedFunction) -> None: ...
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
class ExprIntrp_SequenceOfNamedExpression(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : ExprIntrp_SequenceOfNamedExpression) -> None: ...
    def Assign(self,theOther : ExprIntrp_SequenceOfNamedExpression) -> ExprIntrp_SequenceOfNamedExpression: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Expr.Expr_NamedExpression: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Expr.Expr_NamedExpression: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Expr.Expr_NamedExpression: 
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
    def First(self) -> OCP.Expr.Expr_NamedExpression: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedExpression) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedExpression) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Expr.Expr_NamedExpression: 
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
    def Prepend(self,theSeq : ExprIntrp_SequenceOfNamedExpression) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Expr.Expr_NamedExpression) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Expr.Expr_NamedExpression) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedExpression) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Expr.Expr_NamedExpression: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ExprIntrp_SequenceOfNamedExpression) -> None: ...
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
class ExprIntrp_SequenceOfNamedFunction(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : OCP.Expr.Expr_NamedFunction) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : ExprIntrp_SequenceOfNamedFunction) -> None: ...
    def Assign(self,theOther : ExprIntrp_SequenceOfNamedFunction) -> ExprIntrp_SequenceOfNamedFunction: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OCP.Expr.Expr_NamedFunction: 
        """
        First item access
        """
    def ChangeLast(self) -> OCP.Expr.Expr_NamedFunction: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OCP.Expr.Expr_NamedFunction: 
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
    def First(self) -> OCP.Expr.Expr_NamedFunction: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedFunction) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OCP.Expr.Expr_NamedFunction) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : OCP.Expr.Expr_NamedFunction) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedFunction) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.Expr.Expr_NamedFunction: 
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
    def Prepend(self,theSeq : ExprIntrp_SequenceOfNamedFunction) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OCP.Expr.Expr_NamedFunction) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : OCP.Expr.Expr_NamedFunction) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : ExprIntrp_SequenceOfNamedFunction) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.Expr.Expr_NamedFunction: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : ExprIntrp_SequenceOfNamedFunction) -> None: ...
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
class ExprIntrp_StackOfGeneralExpression(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : ExprIntrp_StackOfGeneralExpression) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralExpression) -> OCP.Expr.Expr_GeneralExpression: ...
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralExpression,theIter : Any) -> None: ...
    def Assign(self,theOther : ExprIntrp_StackOfGeneralExpression) -> ExprIntrp_StackOfGeneralExpression: 
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
    def First(self) -> OCP.Expr.Expr_GeneralExpression: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : OCP.Expr.Expr_GeneralExpression,theIter : Any) -> OCP.Expr.Expr_GeneralExpression: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : ExprIntrp_StackOfGeneralExpression,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : OCP.Expr.Expr_GeneralExpression,theIter : Any) -> OCP.Expr.Expr_GeneralExpression: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : ExprIntrp_StackOfGeneralExpression,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Expr.Expr_GeneralExpression: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : ExprIntrp_StackOfGeneralExpression) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OCP.Expr.Expr_GeneralExpression) -> OCP.Expr.Expr_GeneralExpression: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : ExprIntrp_StackOfGeneralExpression) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ExprIntrp_StackOfGeneralFunction(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : ExprIntrp_StackOfGeneralFunction) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralFunction,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralFunction) -> OCP.Expr.Expr_GeneralFunction: ...
    def Assign(self,theOther : ExprIntrp_StackOfGeneralFunction) -> ExprIntrp_StackOfGeneralFunction: 
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
    def First(self) -> OCP.Expr.Expr_GeneralFunction: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : ExprIntrp_StackOfGeneralFunction,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.Expr.Expr_GeneralFunction,theIter : Any) -> OCP.Expr.Expr_GeneralFunction: ...
    @overload
    def InsertBefore(self,theItem : OCP.Expr.Expr_GeneralFunction,theIter : Any) -> OCP.Expr.Expr_GeneralFunction: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : ExprIntrp_StackOfGeneralFunction,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Expr.Expr_GeneralFunction: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.Expr.Expr_GeneralFunction) -> OCP.Expr.Expr_GeneralFunction: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : ExprIntrp_StackOfGeneralFunction) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : ExprIntrp_StackOfGeneralFunction) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ExprIntrp_StackOfGeneralRelation(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : ExprIntrp_StackOfGeneralRelation) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralRelation) -> OCP.Expr.Expr_GeneralRelation: ...
    @overload
    def Append(self,theItem : OCP.Expr.Expr_GeneralRelation,theIter : Any) -> None: ...
    def Assign(self,theOther : ExprIntrp_StackOfGeneralRelation) -> ExprIntrp_StackOfGeneralRelation: 
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
    def First(self) -> OCP.Expr.Expr_GeneralRelation: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : ExprIntrp_StackOfGeneralRelation,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OCP.Expr.Expr_GeneralRelation,theIter : Any) -> OCP.Expr.Expr_GeneralRelation: ...
    @overload
    def InsertBefore(self,theOther : ExprIntrp_StackOfGeneralRelation,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OCP.Expr.Expr_GeneralRelation,theIter : Any) -> OCP.Expr.Expr_GeneralRelation: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OCP.Expr.Expr_GeneralRelation: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : OCP.Expr.Expr_GeneralRelation) -> OCP.Expr.Expr_GeneralRelation: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : ExprIntrp_StackOfGeneralRelation) -> None: ...
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
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : ExprIntrp_StackOfGeneralRelation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class ExprIntrp_SyntaxError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.ExprIntrp', '__weakref__': <attribute '__weakref__' of 'ExprIntrp_SyntaxError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'ExprIntrp_SyntaxError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
def ExprIntrp_GetDegree() -> int:
    """
    None
    """
def ExprIntrp_GetResult() -> OCP.TCollection.TCollection_AsciiString:
    """
    None
    """
