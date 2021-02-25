import OCP.Expr
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import OCP.TCollection
import io
import OCP.NCollection
import OCP.Standard
__all__  = [
"Expr",
"Expr_GeneralExpression",
"Expr_UnaryExpression",
"Expr_ArcSine",
"Expr_ArcTangent",
"Expr_ArgCosh",
"Expr_ArgSinh",
"Expr_ArgTanh",
"Expr_Array1OfGeneralExpression",
"Expr_Array1OfNamedUnknown",
"Expr_Array1OfSingleRelation",
"Expr_BinaryExpression",
"Expr_BinaryFunction",
"Expr_Cosh",
"Expr_Cosine",
"Expr_Difference",
"Expr_GeneralRelation",
"Expr_Division",
"Expr_SingleRelation",
"Expr_Exponential",
"Expr_Exponentiate",
"Expr_ExprFailure",
"Expr_GeneralFunction",
"Expr_Absolute",
"Expr_FunctionDerivative",
"Expr_Different",
"Expr_GreaterThan",
"Expr_GreaterThanOrEqual",
"Expr_InvalidAssignment",
"Expr_InvalidFunction",
"Expr_InvalidOperand",
"Expr_LessThan",
"Expr_LessThanOrEqual",
"Expr_LogOf10",
"Expr_LogOfe",
"Expr_MapOfNamedUnknown",
"Expr_NamedExpression",
"Expr_NamedConstant",
"Expr_NamedFunction",
"Expr_NamedUnknown",
"Expr_NotAssigned",
"Expr_NotEvaluable",
"Expr_NumericValue",
"Expr_PolyExpression",
"Expr_PolyFunction",
"Expr_Product",
"Expr_RUIterator",
"Expr_RelationIterator",
"Expr_SequenceOfGeneralExpression",
"Expr_SequenceOfGeneralRelation",
"Expr_Sign",
"Expr_Sine",
"Expr_Equal",
"Expr_Sinh",
"Expr_Square",
"Expr_SquareRoot",
"Expr_Sum",
"Expr_SystemRelation",
"Expr_Tangent",
"Expr_Tanh",
"Expr_ArcCosine",
"Expr_UnaryFunction",
"Expr_UnaryMinus",
"Expr_UnknownIterator",
"__add__",
"__mul__",
"__rmul__",
"__sub__",
"__truediv__"
]
class Expr():
    """
    This package describes the data structure of any expression, relation or function used in mathematics. It also describes the assignment of variables. Standard mathematical functions are implemented such as trigonometrics, hyperbolics, and log functions.
    """
    @staticmethod
    def CopyShare_s(exp : Expr_GeneralExpression) -> Expr_GeneralExpression: 
        """
        None
        """
    @staticmethod
    @overload
    def NbOfFreeVariables_s(exp : Expr_GeneralExpression) -> int: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def NbOfFreeVariables_s(exp : Expr_GeneralRelation) -> int: ...
    @staticmethod
    def Sign_s(val : float) -> float: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Expr_GeneralExpression(OCP.Standard.Standard_Transient):
    """
    Defines the general purposes of any expression.Defines the general purposes of any expression.Defines the general purposes of any expression.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Tests if <me> contains NamedUnknowns.
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. Warning: This method does not include any simplification before testing. It could also be very slow; to be used carefully.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear on every NamedUnknown it contains.
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with copies of <with> in <me>. Copies of <with> are made with the Copy() method. Raises InvalidOperand if <with> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
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
class Expr_UnaryExpression(Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. Warning: This method does not include any simplification before testing. It could also be very slow; to be used carefully.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear on every NamedUnknown it contains.
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
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
class Expr_ArcSine(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_ArcTangent(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_ArgCosh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_ArgSinh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_ArgTanh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Array1OfGeneralExpression():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Expr_Array1OfGeneralExpression) -> Expr_Array1OfGeneralExpression: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Expr_GeneralExpression: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Expr_GeneralExpression: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Expr_GeneralExpression: 
        """
        Variable value access
        """
    def First(self) -> Expr_GeneralExpression: 
        """
        Returns first element
        """
    def Init(self,theValue : Expr_GeneralExpression) -> None: 
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
    def Last(self) -> Expr_GeneralExpression: 
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
    def Move(self,theOther : Expr_Array1OfGeneralExpression) -> Expr_Array1OfGeneralExpression: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Expr_GeneralExpression) -> None: 
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
    def Value(self,theIndex : int) -> Expr_GeneralExpression: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Expr_GeneralExpression,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Expr_Array1OfGeneralExpression) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Expr_Array1OfNamedUnknown():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Expr_Array1OfNamedUnknown) -> Expr_Array1OfNamedUnknown: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Expr_NamedUnknown: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Expr_NamedUnknown: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Expr_NamedUnknown: 
        """
        Variable value access
        """
    def First(self) -> Expr_NamedUnknown: 
        """
        Returns first element
        """
    def Init(self,theValue : Expr_NamedUnknown) -> None: 
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
    def Last(self) -> Expr_NamedUnknown: 
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
    def Move(self,theOther : Expr_Array1OfNamedUnknown) -> Expr_Array1OfNamedUnknown: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Expr_NamedUnknown) -> None: 
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
    def Value(self,theIndex : int) -> Expr_NamedUnknown: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Expr_Array1OfNamedUnknown) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Expr_NamedUnknown,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Expr_Array1OfSingleRelation():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Expr_Array1OfSingleRelation) -> Expr_Array1OfSingleRelation: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Expr_SingleRelation: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Expr_SingleRelation: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Expr_SingleRelation: 
        """
        Variable value access
        """
    def First(self) -> Expr_SingleRelation: 
        """
        Returns first element
        """
    def Init(self,theValue : Expr_SingleRelation) -> None: 
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
    def Last(self) -> Expr_SingleRelation: 
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
    def Move(self,theOther : Expr_Array1OfSingleRelation) -> Expr_Array1OfSingleRelation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Expr_SingleRelation) -> None: 
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
    def Value(self,theIndex : int) -> Expr_SingleRelation: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Expr_Array1OfSingleRelation) -> None: ...
    @overload
    def __init__(self,theBegin : Expr_SingleRelation,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Expr_BinaryExpression(Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Defines all binary expressions. The order of the two operands is significant.Defines all binary expressions. The order of the two operands is significant.Defines all binary expressions. The order of the two operands is significant.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contain NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def FirstOperand(self) -> Expr_GeneralExpression: 
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
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. Warning: This method does not include any simplification before testing. It could also be very slow; to be used carefully.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear on every NamedUnknown it contains.
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>. Raises InvalidOperand if <with> contains <me>.
        """
    def SecondOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def SetFirstOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets first operand of <me> Raises InvalidOperand if exp = me
        """
    def SetSecondOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets second operand of <me> Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
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
class Expr_BinaryFunction(Expr_BinaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Defines the use of a binary function in an expression with given arguments.Defines the use of a binary function in an expression with given arguments.Defines the use of a binary function in an expression with given arguments.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contain NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def FirstOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def Function(self) -> Expr_GeneralFunction: 
        """
        Returns the function defining <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>. Raises InvalidOperand if <with> contains <me>.
        """
    def SecondOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def SetFirstOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets first operand of <me> Raises InvalidOperand if exp = me
        """
    def SetSecondOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets second operand of <me> Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,func : Expr_GeneralFunction,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_Cosh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Cosine(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Difference(Expr_BinaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contain NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def FirstOperand(self) -> Expr_GeneralExpression: 
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
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raises OutOfRange if <N> <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>. Raises InvalidOperand if <with> contains <me>.
        """
    def SecondOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def SetFirstOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets first operand of <me> Raises InvalidOperand if exp = me
        """
    def SetSecondOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets second operand of <me> Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_GeneralRelation(OCP.Standard.Standard_Transient):
    """
    Defines the general purposes of any relation between expressions.Defines the general purposes of any relation between expressions.Defines the general purposes of any relation between expressions.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> contains <var>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        Returns the current status of the relation
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me>.
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if <index> is out of range.
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
class Expr_Division(Expr_BinaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contain NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def FirstOperand(self) -> Expr_GeneralExpression: 
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
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>. Raises InvalidOperand if <with> contains <me>.
        """
    def SecondOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def SetFirstOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets first operand of <me> Raises InvalidOperand if exp = me
        """
    def SetSecondOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets second operand of <me> Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_SingleRelation(Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        Returns the current status of the relation
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
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
class Expr_Exponential(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Exponentiate(Expr_BinaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contain NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def FirstOperand(self) -> Expr_GeneralExpression: 
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
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>. Raises InvalidOperand if <with> contains <me>.
        """
    def SecondOperand(self) -> Expr_GeneralExpression: 
        """
        None

        None
        """
    def SetFirstOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets first operand of <me> Raises InvalidOperand if exp = me
        """
    def SetSecondOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets second operand of <me> Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_ExprFailure(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_ExprFailure' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_ExprFailure' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_GeneralFunction(OCP.Standard.Standard_Transient):
    """
    Defines the general purposes of any function.Defines the general purposes of any function.Defines the general purposes of any function.
    """
    def Copy(self) -> Expr_GeneralFunction: 
        """
        Returns a copy of <me> with the same form.
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
    def Derivative(self,var : Expr_NamedUnknown) -> Expr_GeneralFunction: 
        """
        Returns Derivative of <me> for variable <var>.

        Returns Derivative of <me> for variable <var> with degree <deg>.
        """
    @overload
    def Derivative(self,var : Expr_NamedUnknown,deg : int) -> Expr_GeneralFunction: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Computes the value of <me> with the given variables. Raises NotEvaluable if <vars> does not match all variables of <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStringName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,func : Expr_GeneralFunction) -> bool: 
        """
        Tests if <me> and <func> are similar functions (same name and same used expression).
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
    def IsLinearOnVariable(self,index : int) -> bool: 
        """
        Tests if <me> is linear on variable on range <index>
        """
    def NbOfVariables(self) -> int: 
        """
        Returns the number of variables of <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Variable(self,index : int) -> Expr_NamedUnknown: 
        """
        Returns the variable denoted by <index> in <me>. Raises OutOfRange if index > NbOfVariables.
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
class Expr_Absolute(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_FunctionDerivative(Expr_GeneralFunction, OCP.Standard.Standard_Transient):
    def Copy(self) -> Expr_GeneralFunction: 
        """
        Returns a copy of <me> with the same form.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Degree(self) -> int: 
        """
        Returns the degree of derivation of <me>.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DerivVariable(self) -> Expr_NamedUnknown: 
        """
        Returns the derivation variable of <me>.
        """
    @overload
    def Derivative(self,var : Expr_NamedUnknown) -> Expr_GeneralFunction: 
        """
        Returns Derivative of <me> for variable <var>.

        Returns Derivative of <me> for variable <var> with degree <deg>.
        """
    @overload
    def Derivative(self,var : Expr_NamedUnknown,deg : int) -> Expr_GeneralFunction: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,values : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Computes the value of <me> with the given variables. Raises DimensionMismatch if Length(vars) is different from Length(values).
        """
    def Expression(self) -> Expr_GeneralExpression: 
        """
        None
        """
    def Function(self) -> Expr_GeneralFunction: 
        """
        Returns the function of which <me> is the derivative.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStringName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,func : Expr_GeneralFunction) -> bool: 
        """
        Tests if <me> and <func> are similar functions (same name and same used expression).
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
    def IsLinearOnVariable(self,index : int) -> bool: 
        """
        Tests if <me> is linear on variable on range <index>
        """
    def NbOfVariables(self) -> int: 
        """
        Returns the number of variables of <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateExpression(self) -> None: 
        """
        None
        """
    def Variable(self,index : int) -> Expr_NamedUnknown: 
        """
        Returns the variable denoted by <index> in <me>. Raises OutOfRange if <index> greater than NbOfVariables of <me>.
        """
    def __init__(self,func : Expr_GeneralFunction,withX : Expr_NamedUnknown,deg : int) -> None: ...
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
class Expr_Different(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_GreaterThan(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_GreaterThanOrEqual(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_InvalidAssignment(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_InvalidAssignment' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_InvalidAssignment' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_InvalidFunction(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_InvalidFunction' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_InvalidFunction' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_InvalidOperand(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_InvalidOperand' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_InvalidOperand' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_LessThan(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_LessThanOrEqual(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_LogOf10(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_LogOfe(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_MapOfNamedUnknown(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : Expr_NamedUnknown) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Expr_MapOfNamedUnknown) -> Expr_MapOfNamedUnknown: 
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
    def Contains(self,theKey1 : Expr_NamedUnknown) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Expr_MapOfNamedUnknown) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : Expr_NamedUnknown) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> Expr_NamedUnknown: 
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
    def RemoveKey(self,theKey1 : Expr_NamedUnknown) -> bool: 
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
    def Substitute(self,theIndex : int,theKey1 : Expr_NamedUnknown) -> None: 
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
    def __init__(self,theOther : Expr_MapOfNamedUnknown) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Expr_NamedExpression(Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Describe an expression used by its name (as constants or variables). A single reference is made to a NamedExpression in every Expression (i.e. a NamedExpression is shared).Describe an expression used by its name (as constants or variables). A single reference is made to a NamedExpression in every Expression (i.e. a NamedExpression is shared).Describe an expression used by its name (as constants or variables). A single reference is made to a NamedExpression in every Expression (i.e. a NamedExpression is shared).
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Tests if <me> contains NamedUnknowns.
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear on every NamedUnknown it contains.
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method redefines to a True value the GeneralExpression method.
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with copies of <with> in <me>. Copies of <with> are made with the Copy() method. Raises InvalidOperand if <with> contains <me>.
        """
    def SetName(self,name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
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
class Expr_NamedConstant(Expr_NamedExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Describes any numeric constant known by a special name (as PI, e,...).Describes any numeric constant known by a special name (as PI, e,...).Describes any numeric constant known by a special name (as PI, e,...).
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Tests if <me> contains NamedUnknown. (returns always False)
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetValue(self) -> float: 
        """
        None

        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method redefines to a True value the GeneralExpression method.
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raises OutOfRange if <N> <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> (always returns zero)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>
        """
    def SetName(self,name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        returns the <I>-th sub-expression of <me> raises OutOfRange
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,name : OCP.TCollection.TCollection_AsciiString,value : float) -> None: ...
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
class Expr_NamedFunction(Expr_GeneralFunction, OCP.Standard.Standard_Transient):
    def Copy(self) -> Expr_GeneralFunction: 
        """
        Returns a copy of <me> with the same form.
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
    def Derivative(self,var : Expr_NamedUnknown) -> Expr_GeneralFunction: 
        """
        Returns Derivative of <me> for variable <var>.

        Returns Derivative of <me> for variable <var> with degree <deg>.
        """
    @overload
    def Derivative(self,var : Expr_NamedUnknown,deg : int) -> Expr_GeneralFunction: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,values : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Computes the value of <me> with the given variables. Raises DimensionMismatch if Length(vars) is different from Length(values).
        """
    def Expression(self) -> Expr_GeneralExpression: 
        """
        Returns equivalent expression of <me>.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name assigned to <me>
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStringName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,func : Expr_GeneralFunction) -> bool: 
        """
        Tests if <me> and <func> are similar functions (same name and same used expression).
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
    def IsLinearOnVariable(self,index : int) -> bool: 
        """
        Tests if <me> is linear on variable on range <index>
        """
    def NbOfVariables(self) -> int: 
        """
        Returns the number of variables of <me>.
        """
    def SetExpression(self,exp : Expr_GeneralExpression) -> None: 
        """
        Modifies expression of <me>. Warning: Beware of derivatives. See FunctionDerivative
        """
    def SetName(self,newname : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets the name <newname> to <me>.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Variable(self,index : int) -> Expr_NamedUnknown: 
        """
        Returns the variable denoted by <index> in <me>. Raises OutOfRange if <index> is greater than NbOfVariables of <me>, or less than or equal to zero.
        """
    def __init__(self,name : OCP.TCollection.TCollection_AsciiString,exp : Expr_GeneralExpression,vars : Expr_Array1OfNamedUnknown) -> None: ...
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
class Expr_NamedUnknown(Expr_NamedExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    This class describes any variable of an expression. Assignment is treated directly in this class.This class describes any variable of an expression. Assignment is treated directly in this class.This class describes any variable of an expression. Assignment is treated directly in this class.
    """
    def Assign(self,exp : Expr_GeneralExpression) -> None: 
        """
        Assigns <me> to <exp> expression. Raises exception if <exp> refers to <me>.
        """
    def AssignedExpression(self) -> Expr_GeneralExpression: 
        """
        If exists, returns the assigned expression. An exception is raised if the expression does not exist.
        """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Tests if <me> contains NamedUnknown.
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def Deassign(self) -> None: 
        """
        Supresses the assigned expression

        Supresses the assigned expression
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetName(self) -> OCP.TCollection.TCollection_AsciiString: 
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
    def IsAssigned(self) -> bool: 
        """
        Tests if an expression is assigned to <me>.

        Tests if an expression is assigned to <me>.
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method redefines to a True value the GeneralExpression method.
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetName(self,name : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,name : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Expr_NotAssigned(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_NotAssigned' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_NotAssigned' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_NotEvaluable(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Expr', '__weakref__': <attribute '__weakref__' of 'Expr_NotEvaluable' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Expr_NotEvaluable' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Expr_NumericValue(Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    This class describes any reel value defined in an expression.This class describes any reel value defined in an expression.This class describes any reel value defined in an expression.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Tests if <me> contains NamedUnknown.
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetValue(self) -> float: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raises OutOfRange if <N> <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>
        """
    def SetValue(self,val : float) -> None: 
        """
        None
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me> raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,val : float) -> None: ...
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
class Expr_PolyExpression(Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. Warning: This method does not include any simplification before testing. It could also be very slow; to be used carefully.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear on every NamedUnknown it contains.
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbOperands(self) -> int: 
        """
        returns the number of operands contained in <me>
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 2)
        """
    def Operand(self,index : int) -> Expr_GeneralExpression: 
        """
        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range

        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression,index : int) -> None: 
        """
        Sets the <index>-th operand used in <me>. An exception is raised if <index> is out of range Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the sub-expression denoted by <I> in <me> Raises OutOfRange if <I> > NbSubExpressions(me)
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
class Expr_PolyFunction(Expr_PolyExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Defines the use of an n-ary function in an expression with given arguments.Defines the use of an n-ary function in an expression with given arguments.Defines the use of an n-ary function in an expression with given arguments.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def Function(self) -> Expr_GeneralFunction: 
        """
        Returns the function defining <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbOperands(self) -> int: 
        """
        returns the number of operands contained in <me>
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 2)
        """
    def Operand(self,index : int) -> Expr_GeneralExpression: 
        """
        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range

        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression,index : int) -> None: 
        """
        Sets the <index>-th operand used in <me>. An exception is raised if <index> is out of range Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the sub-expression denoted by <I> in <me> Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,func : Expr_GeneralFunction,exps : Expr_Array1OfGeneralExpression) -> None: ...
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
class Expr_Product(Expr_PolyExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbOperands(self) -> int: 
        """
        returns the number of operands contained in <me>
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 2)
        """
    def Operand(self,index : int) -> Expr_GeneralExpression: 
        """
        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range

        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression,index : int) -> None: 
        """
        Sets the <index>-th operand used in <me>. An exception is raised if <index> is out of range Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the sub-expression denoted by <I> in <me> Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
    @overload
    def __init__(self,exps : Expr_SequenceOfGeneralExpression) -> None: ...
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
class Expr_RUIterator():
    """
    Iterates on NamedUnknowns in a GeneralRelation.
    """
    def More(self) -> bool: 
        """
        Returns False if on other unknown remains.
        """
    def Next(self) -> None: 
        """
        None
        """
    def Value(self) -> Expr_NamedUnknown: 
        """
        Returns current NamedUnknown. Raises exception if no more unknowns remain.
        """
    def __init__(self,rel : Expr_GeneralRelation) -> None: ...
    pass
class Expr_RelationIterator():
    """
    Iterates on every basic relation contained in a GeneralRelation.
    """
    def More(self) -> bool: 
        """
        Returns False if no other relation remains.
        """
    def Next(self) -> None: 
        """
        None
        """
    def Value(self) -> Expr_SingleRelation: 
        """
        Returns current basic relation. Exception is raised if no more relation remains.
        """
    def __init__(self,rel : Expr_GeneralRelation) -> None: ...
    pass
class Expr_SequenceOfGeneralExpression(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Expr_SequenceOfGeneralExpression) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Expr_GeneralExpression) -> None: ...
    def Assign(self,theOther : Expr_SequenceOfGeneralExpression) -> Expr_SequenceOfGeneralExpression: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Expr_GeneralExpression: 
        """
        First item access
        """
    def ChangeLast(self) -> Expr_GeneralExpression: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Expr_GeneralExpression: 
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
    def First(self) -> Expr_GeneralExpression: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Expr_SequenceOfGeneralExpression) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Expr_GeneralExpression) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Expr_GeneralExpression) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Expr_SequenceOfGeneralExpression) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Expr_GeneralExpression: 
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
    def Prepend(self,theItem : Expr_GeneralExpression) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Expr_SequenceOfGeneralExpression) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Expr_GeneralExpression) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Expr_SequenceOfGeneralExpression) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Expr_GeneralExpression: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Expr_SequenceOfGeneralExpression) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Expr_SequenceOfGeneralRelation(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Expr_GeneralRelation) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Expr_SequenceOfGeneralRelation) -> None: ...
    def Assign(self,theOther : Expr_SequenceOfGeneralRelation) -> Expr_SequenceOfGeneralRelation: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Expr_GeneralRelation: 
        """
        First item access
        """
    def ChangeLast(self) -> Expr_GeneralRelation: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Expr_GeneralRelation: 
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
    def First(self) -> Expr_GeneralRelation: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Expr_SequenceOfGeneralRelation) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Expr_GeneralRelation) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Expr_GeneralRelation) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Expr_SequenceOfGeneralRelation) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Expr_GeneralRelation: 
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
    def Prepend(self,theSeq : Expr_SequenceOfGeneralRelation) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Expr_GeneralRelation) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Expr_GeneralRelation) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Expr_SequenceOfGeneralRelation) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Expr_GeneralRelation: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Expr_SequenceOfGeneralRelation) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Expr_Sign(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Sine(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Equal(Expr_SingleRelation, Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def FirstMember(self) -> Expr_GeneralExpression: 
        """
        Returns the first member of the relation
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me> (Always 1).
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def SecondMember(self) -> Expr_GeneralExpression: 
        """
        Returns the second member of the relation
        """
    def SetFirstMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the first member of the relation
        """
    def SetSecondMember(self,exp : Expr_GeneralExpression) -> None: 
        """
        Defines the second member of the relation
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        returns a GeneralRelation after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by an associated expressions and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if index is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
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
class Expr_Sinh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Square(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_SquareRoot(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Sum(Expr_PolyExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raises OutOfRange if <N> <= 0
        """
    def NbOperands(self) -> int: 
        """
        returns the number of operands contained in <me>
        """
    def NbSubExpressions(self) -> int: 
        """
        returns the number of sub-expressions contained in <me> ( >= 2)
        """
    def Operand(self,index : int) -> Expr_GeneralExpression: 
        """
        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range

        Returns the <index>-th operand used in <me>. An exception is raised if index is out of range
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression,index : int) -> None: 
        """
        Sets the <index>-th operand used in <me>. An exception is raised if <index> is out of range Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the sub-expression denoted by <I> in <me> Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,exp1 : Expr_GeneralExpression,exp2 : Expr_GeneralExpression) -> None: ...
    @overload
    def __init__(self,exps : Expr_SequenceOfGeneralExpression) -> None: ...
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
class Expr_SystemRelation(Expr_GeneralRelation, OCP.Standard.Standard_Transient):
    def Add(self,relation : Expr_GeneralRelation) -> None: 
        """
        Appends <relation> in the list of components of <me>.
        """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> contains <exp>.
        """
    def Copy(self) -> Expr_GeneralRelation: 
        """
        Returns a copy of <me> having the same unknowns and functions.
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
    def IsLinear(self) -> bool: 
        """
        Tests if <me> is linear between its NamedUnknowns.
        """
    def IsSatisfied(self) -> bool: 
        """
        None
        """
    def NbOfSingleRelations(self) -> int: 
        """
        Returns the number of SingleRelations contained in <me>.
        """
    def NbOfSubRelations(self) -> int: 
        """
        Returns the number of relations contained in <me>.
        """
    def Remove(self,relation : Expr_GeneralRelation) -> None: 
        """
        None
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me>.
        """
    def Simplified(self) -> Expr_GeneralRelation: 
        """
        Returns a GeneralRelation after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def Simplify(self) -> None: 
        """
        Replaces NamedUnknowns by associated expressions, and computes values in <me>.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubRelation(self,index : int) -> Expr_GeneralRelation: 
        """
        Returns the relation denoted by <index> in <me>. An exception is raised if <index> is out of range.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,relation : Expr_GeneralRelation) -> None: ...
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
class Expr_Tangent(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_Tanh(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_ArcCosine(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_UnaryFunction(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    """
    Defines the use of an unary function in an expression with a given argument.Defines the use of an unary function in an expression with a given argument.Defines the use of an unary function in an expression with a given argument.
    """
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        returns the derivative on <X> unknown of <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def Function(self) -> Expr_GeneralFunction: 
        """
        Returns the function defining <me>.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raise OutOfRange if N <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,func : Expr_GeneralFunction,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_UnaryMinus(Expr_UnaryExpression, Expr_GeneralExpression, OCP.Standard.Standard_Transient):
    def Contains(self,exp : Expr_GeneralExpression) -> bool: 
        """
        Tests if <exp> is contained in <me>.
        """
    def ContainsUnknowns(self) -> bool: 
        """
        Does <me> contains NamedUnknown ?
        """
    def Copy(self) -> Expr_GeneralExpression: 
        """
        Returns a copy of <me> having the same unknowns and functions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Derivative(self,X : Expr_NamedUnknown) -> Expr_GeneralExpression: 
        """
        Returns the derivative on <X> unknown of <me>
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Evaluate(self,vars : Expr_Array1OfNamedUnknown,vals : OCP.TColStd.TColStd_Array1OfReal) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def EvaluateNumeric(self) -> float: 
        """
        Returns the value of <me> (as a Real) by replacement of <vars> by <vals>. Raises NotEvaluable if <me> contains NamedUnknown not in <vars> or NumericError if result cannot be computed.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsIdentical(self,Other : Expr_GeneralExpression) -> bool: 
        """
        Tests if <me> and <Other> define the same expression. This method does not include any simplification before testing.
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
    def IsLinear(self) -> bool: 
        """
        None
        """
    def IsShareable(self) -> bool: 
        """
        Tests if <me> can be shared by one or more expressions or must be copied. This method returns False as a default value. To be redefined ( especially for NamedUnknown).
        """
    def NDerivative(self,X : Expr_NamedUnknown,N : int) -> Expr_GeneralExpression: 
        """
        Returns the <N>-th derivative on <X> unknown of <me>. Raises OutOfRange if <N> <= 0
        """
    def NbSubExpressions(self) -> int: 
        """
        Returns the number of sub-expressions contained in <me> ( >= 0)
        """
    def Operand(self) -> Expr_GeneralExpression: 
        """
        Returns the operand used

        Returns the operand used
        """
    def Replace(self,var : Expr_NamedUnknown,with_ : Expr_GeneralExpression) -> None: 
        """
        Replaces all occurences of <var> with <with> in <me> Raises InvalidOperand if <with> contains <me>.
        """
    def SetOperand(self,exp : Expr_GeneralExpression) -> None: 
        """
        Sets the operand used Raises InvalidOperand if <exp> contains <me>.
        """
    def ShallowSimplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after a simplification of the arguments of <me>.
        """
    def Simplified(self) -> Expr_GeneralExpression: 
        """
        Returns a GeneralExpression after replacement of NamedUnknowns by an associated expression, and after values computation.
        """
    def String(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        returns a string representing <me> in a readable way.
        """
    def SubExpression(self,I : int) -> Expr_GeneralExpression: 
        """
        Returns the <I>-th sub-expression of <me>. Raises OutOfRange if <I> > NbSubExpressions(me)
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
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
class Expr_UnknownIterator():
    """
    Describes an iterator on NamedUnknowns contained in any GeneralExpression.
    """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Value(self) -> Expr_NamedUnknown: 
        """
        None
        """
    def __init__(self,exp : Expr_GeneralExpression) -> None: ...
    pass
@overload
def __add__(x : Expr_GeneralExpression,y : Expr_GeneralExpression) -> Expr_Sum:
    """
    None

    None

    None
    """
@overload
def __add__(x : float,y : Expr_GeneralExpression) -> Expr_Sum:
    pass
@overload
def __add__(x : Expr_GeneralExpression,y : float) -> Expr_Sum:
    pass
@overload
def __mul__(x : Expr_GeneralExpression,y : Expr_GeneralExpression) -> Expr_Product:
    """
    None

    None

    None
    """
@overload
def __mul__(x : Expr_GeneralExpression,y : float) -> Expr_Product:
    pass
@overload
def __mul__(x : float,y : Expr_GeneralExpression) -> Expr_Product:
    pass
@overload
def __rmul__(x : Expr_GeneralExpression,y : Expr_GeneralExpression) -> Expr_Product:
    """
    None

    None

    None
    """
@overload
def __rmul__(x : float,y : Expr_GeneralExpression) -> Expr_Product:
    pass
@overload
def __rmul__(x : Expr_GeneralExpression,y : float) -> Expr_Product:
    pass
@overload
def __sub__(x : Expr_GeneralExpression) -> Expr_UnaryMinus:
    """
    None

    None

    None

    None
    """
@overload
def __sub__(x : float,y : Expr_GeneralExpression) -> Expr_Difference:
    pass
@overload
def __sub__(x : Expr_GeneralExpression,y : float) -> Expr_Difference:
    pass
@overload
def __sub__(x : Expr_GeneralExpression,y : Expr_GeneralExpression) -> Expr_Difference:
    pass
@overload
def __truediv__(x : Expr_GeneralExpression,y : Expr_GeneralExpression) -> Expr_Division:
    """
    None

    None

    None
    """
@overload
def __truediv__(x : float,y : Expr_GeneralExpression) -> Expr_Division:
    pass
@overload
def __truediv__(x : Expr_GeneralExpression,y : float) -> Expr_Division:
    pass
