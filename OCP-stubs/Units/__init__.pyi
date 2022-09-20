import OCP.Units
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.NCollection
import OCP.Standard
import OCP.TColStd
__all__  = [
"Units",
"Units_Dimensions",
"Units_Explorer",
"Units_Lexicon",
"Units_Sentence",
"Units_Measurement",
"Units_NoSuchType",
"Units_NoSuchUnit",
"Units_QtsSequence",
"Units_QuantitiesSequence",
"Units_Quantity",
"Units_MathSentence",
"Units_Token",
"Units_Unit",
"Units_TksSequence",
"Units_ShiftedToken",
"Units_TokensSequence",
"Units_ShiftedUnit",
"Units_UnitSentence",
"Units_UnitsDictionary",
"Units_UnitsLexicon",
"Units_UtsSequence",
"Units_UnitsSystem",
"Units_UnitsSequence",
"__add__",
"__mul__",
"__rmul__",
"__sub__",
"__truediv__",
"pow"
]
class Units():
    """
    This package provides all the facilities to create and question a dictionary of units, and also to manipulate measurements which are real values with units.
    """
    @staticmethod
    def Convert_s(avalue : float,afirstunit : str,asecondunit : str) -> float: 
        """
        Converts <avalue> expressed in <afirstunit> into the <asecondunit>.
        """
    @staticmethod
    def DictionaryOfUnits_s(amode : bool=False) -> Units_UnitsDictionary: 
        """
        Returns a unique instance of the dictionary of units. If <amode> is True, then it forces the recomputation of the dictionary of units.
        """
    @staticmethod
    def Dimensions_s(aType : str) -> Units_Dimensions: 
        """
        return the dimension associated to the Type
        """
    @staticmethod
    def FirstQuantity_s(aunit : str) -> str: 
        """
        Returns the first quantity string founded from the unit <aUnit>.
        """
    @staticmethod
    @overload
    def FromSI_s(aData : float,aUnit : str) -> float: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def FromSI_s(aData : float,aUnit : str,aDim : Units_Dimensions) -> float: ...
    @staticmethod
    def LexiconFile_s(afile : str) -> None: 
        """
        Defines the location of the file containing the lexicon useful in manipulating composite units.
        """
    @staticmethod
    def LexiconFormula_s() -> Units_Lexicon: 
        """
        Return a unique instance of LexiconFormula.
        """
    @staticmethod
    def LexiconUnits_s(amode : bool=True) -> Units_Lexicon: 
        """
        Returns a unique instance of the Units_Lexicon. If <amode> is True, it forces the recomputation of the dictionary of units, and by consequence the completion of the Units_Lexicon.
        """
    @staticmethod
    def NullDimensions_s() -> Units_Dimensions: 
        """
        Returns always the same instance of Dimensions.
        """
    @staticmethod
    def Quantity_s(aquantity : str) -> Units_Quantity: 
        """
        Returns a unique quantity instance corresponding to <aquantity>.
        """
    @staticmethod
    @overload
    def ToSI_s(aData : float,aUnit : str) -> float: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def ToSI_s(aData : float,aUnit : str,aDim : Units_Dimensions) -> float: ...
    @staticmethod
    def UnitsFile_s(afile : str) -> None: 
        """
        Defines the location of the file containing all the information useful in creating the dictionary of all the units known to the system.
        """
    def __init__(self) -> None: ...
    pass
class Units_Dimensions(OCP.Standard.Standard_Transient):
    """
    This class includes all the methods to create and manipulate the dimensions of the physical quantities.This class includes all the methods to create and manipulate the dimensions of the physical quantities.This class includes all the methods to create and manipulate the dimensions of the physical quantities.
    """
    @staticmethod
    def AAmountOfSubstance_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def AElectricCurrent_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def ALength_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def ALess_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def ALuminousIntensity_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def AMass_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def APlaneAngle_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def ASolidAngle_s() -> Units_Dimensions: 
        """
        Returns the basic dimensions.
        """
    @staticmethod
    def AThermodynamicTemperature_s() -> Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def ATime_s() -> Units_Dimensions: 
        """
        None
        """
    def AmountOfSubstance(self) -> float: 
        """
        Returns the power of quantity of material (mole) stored in the dimensions.

        Returns the power of quantity of material (mole) stored in the dimensions.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Divide(self,adimensions : Units_Dimensions) -> Units_Dimensions: 
        """
        Creates and returns a new Dimensions object which is the result of the division of <me> by <adimensions>.
        """
    def Dump(self,ashift : int) -> None: 
        """
        Useful for degugging.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ElectricCurrent(self) -> float: 
        """
        Returns the power of electrical intensity (current) stored in the dimensions.

        Returns the power of electrical intensity (current) stored in the dimensions.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEqual(self,adimensions : Units_Dimensions) -> bool: 
        """
        Returns true if <me> and <adimensions> have the same dimensions, false otherwise.
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
    def IsNotEqual(self,adimensions : Units_Dimensions) -> bool: 
        """
        Returns false if <me> and <adimensions> have the same dimensions, true otherwise.
        """
    def Length(self) -> float: 
        """
        Returns the power of length stored in the dimensions.

        Returns the power of length stored in the dimensions.
        """
    def LuminousIntensity(self) -> float: 
        """
        Returns the power of light intensity stored in the dimensions.

        Returns the power of light intensity stored in the dimensions.
        """
    def Mass(self) -> float: 
        """
        Returns the power of mass stored in the dimensions.

        Returns the power of mass stored in the dimensions.
        """
    def Multiply(self,adimensions : Units_Dimensions) -> Units_Dimensions: 
        """
        Creates and returns a new Dimensions object which is the result of the multiplication of <me> and <adimensions>.
        """
    def PlaneAngle(self) -> float: 
        """
        Returns the power of plane angle stored in the dimensions.

        Returns the power of plane angle stored in the dimensions.
        """
    def Power(self,anexponent : float) -> Units_Dimensions: 
        """
        Creates and returns a new Dimensions object which is the result of the power of <me> and <anexponent>.
        """
    def Quantity(self) -> str: 
        """
        Returns the quantity string of the dimension
        """
    def SolidAngle(self) -> float: 
        """
        Returns the power of solid angle stored in the dimensions.

        Returns the power of solid angle stored in the dimensions.
        """
    def ThermodynamicTemperature(self) -> float: 
        """
        Returns the power of temperature stored in the dimensions.

        Returns the power of temperature stored in the dimensions.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Time(self) -> float: 
        """
        Returns the power of time stored in the dimensions.

        Returns the power of time stored in the dimensions.
        """
    def __init__(self,amass : float,alength : float,atime : float,anelectriccurrent : float,athermodynamictemperature : float,anamountofsubstance : float,aluminousintensity : float,aplaneangle : float,asolidangle : float) -> None: ...
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
class Units_Explorer():
    """
    This class provides all the services to explore UnitsSystem or UnitsDictionary.
    """
    @overload
    def Init(self,aunitsdictionary : Units_UnitsDictionary) -> None: 
        """
        Initializes the instance of the class with the UnitsSystem <aunitssystem>.

        Initializes the instance of the class with the UnitsDictionary <aunitsdictionary>.

        Initializes the instance of the class with the UnitsSystem <aunitssystem> and positioned at the quantity <aquantity>.

        Initializes the instance of the class with the UnitsDictionary <aunitsdictionary> and positioned at the quantity <aquantity>.
        """
    @overload
    def Init(self,aunitssystem : Units_UnitsSystem) -> None: ...
    @overload
    def Init(self,aunitssystem : Units_UnitsSystem,aquantity : str) -> None: ...
    @overload
    def Init(self,aunitsdictionary : Units_UnitsDictionary,aquantity : str) -> None: ...
    def IsActive(self) -> bool: 
        """
        If the units system to explore is a user system, returns True if the current unit is active, False otherwise.
        """
    def MoreQuantity(self) -> bool: 
        """
        Returns True if there is another Quantity to explore, False otherwise.
        """
    def MoreUnit(self) -> bool: 
        """
        Returns True if there is another Unit to explore, False otherwise.
        """
    def NextQuantity(self) -> None: 
        """
        Sets the next Quantity current.
        """
    def NextUnit(self) -> None: 
        """
        Sets the next Unit current.
        """
    def Quantity(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the current Quantity.
        """
    def Unit(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the current unit.
        """
    @overload
    def __init__(self,aunitsdictionary : Units_UnitsDictionary,aquantity : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aunitssystem : Units_UnitsSystem,aquantity : str) -> None: ...
    @overload
    def __init__(self,aunitsdictionary : Units_UnitsDictionary) -> None: ...
    @overload
    def __init__(self,aunitssystem : Units_UnitsSystem) -> None: ...
    pass
class Units_Lexicon(OCP.Standard.Standard_Transient):
    """
    This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.
    """
    def AddToken(self,aword : str,amean : str,avalue : float) -> None: 
        """
        Adds to the lexicon a new token with <aword>, <amean>, <avalue> as arguments. If there is already a token with the field <theword> equal to <aword>, the existing token is updated.
        """
    def Creates(self) -> None: 
        """
        Reads the file <afilename> to create a sequence of tokens stored in <thesequenceoftokens>.
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
        Useful for debugging.

        Useful for debugging.
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
    def Sequence(self) -> Units_TokensSequence: 
        """
        Returns the first item of the sequence of tokens.

        Returns the first item of the sequence of tokens.
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
class Units_Sentence():
    """
    This class describes all the methods to create and compute an expression contained in a string.
    """
    def Dump(self) -> None: 
        """
        Useful for debugging.

        Useful for debugging.
        """
    def Evaluate(self) -> Units_Token: 
        """
        Computes and returns in a token the result of the expression.
        """
    def IsDone(self) -> bool: 
        """
        Return True if number of created tokens > 0 (i.e creation of sentence is successful)

        Return True if number of created tokens > 0 (i.e creation of sentence is successful)
        """
    @overload
    def Sequence(self,asequenceoftokens : Units_TokensSequence) -> None: 
        """
        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.

        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.
        """
    @overload
    def Sequence(self) -> Units_TokensSequence: ...
    def SetConstants(self) -> None: 
        """
        For each constant encountered, sets the value.
        """
    def __init__(self,alexicon : Units_Lexicon,astring : str) -> None: ...
    pass
class Units_Measurement():
    """
    This class defines a measurement which is the association of a real value and a unit.
    """
    def Add(self,ameasurement : Units_Measurement) -> Units_Measurement: ...
    def Convert(self,aunit : str) -> None: ...
    @overload
    def Divide(self,avalue : float) -> Units_Measurement: 
        """
        Returns a measurement which is the division of <me> by <ameasurement>.

        Returns a measurement which is the division of <me> by the constant <avalue>.
        """
    @overload
    def Divide(self,ameasurement : Units_Measurement) -> Units_Measurement: ...
    def Dump(self) -> None: 
        """
        Useful for debugging.
        """
    def Fractional(self) -> Units_Measurement: 
        """
        Returns a Measurement object with the fractional value of the measurement contained in <me>.
        """
    def HasToken(self) -> bool: 
        """
        None
        """
    def Integer(self) -> Units_Measurement: 
        """
        Returns a Measurement object with the integer value of the measurement contained in <me>.
        """
    def Measurement(self) -> float: 
        """
        Returns the value of the measurement.
        """
    @overload
    def Multiply(self,ameasurement : Units_Measurement) -> Units_Measurement: 
        """
        Returns a measurement which is the multiplication of <me> and <ameasurement>.

        Returns a measurement which is the multiplication of <me> with the value <avalue>.
        """
    @overload
    def Multiply(self,avalue : float) -> Units_Measurement: ...
    def Power(self,anexponent : float) -> Units_Measurement: 
        """
        Returns a measurement which is <me> powered <anexponent>.
        """
    def Subtract(self,ameasurement : Units_Measurement) -> Units_Measurement: ...
    def Token(self) -> Units_Token: 
        """
        Returns the token contained in <me>.
        """
    def __add__(self,ameasurement : Units_Measurement) -> Units_Measurement: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,avalue : float,aunit : str) -> None: ...
    @overload
    def __init__(self,avalue : float,atoken : Units_Token) -> None: ...
    @overload
    def __mul__(self,avalue : float) -> Units_Measurement: 
        """
        None

        None
        """
    @overload
    def __mul__(self,ameasurement : Units_Measurement) -> Units_Measurement: ...
    @overload
    def __rmul__(self,avalue : float) -> Units_Measurement: 
        """
        None

        None
        """
    @overload
    def __rmul__(self,ameasurement : Units_Measurement) -> Units_Measurement: ...
    def __sub__(self,ameasurement : Units_Measurement) -> Units_Measurement: 
        """
        None
        """
    @overload
    def __truediv__(self,ameasurement : Units_Measurement) -> Units_Measurement: 
        """
        None

        None
        """
    @overload
    def __truediv__(self,avalue : float) -> Units_Measurement: ...
    pass
class Units_NoSuchType(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Units', '__weakref__': <attribute '__weakref__' of 'Units_NoSuchType' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Units_NoSuchType' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Units_NoSuchUnit(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Units', '__weakref__': <attribute '__weakref__' of 'Units_NoSuchUnit' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Units_NoSuchUnit' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Units_QtsSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Units_Quantity) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Units_QtsSequence) -> None: ...
    def Assign(self,theOther : Units_QtsSequence) -> Units_QtsSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Quantity: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Quantity: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Units_Quantity: 
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
    def First(self) -> Units_Quantity: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Quantity) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Quantity) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Units_Quantity: 
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
    def Prepend(self,theItem : Units_Quantity) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Units_QtsSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Units_Quantity) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Units_Quantity: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Units_QtsSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Units_QuantitiesSequence(Units_QtsSequence, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Units_Quantity) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : Units_QtsSequence) -> None: ...
    def Assign(self,theOther : Units_QtsSequence) -> Units_QtsSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Quantity: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Quantity: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Units_QtsSequence: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Units_Quantity: 
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
    def First(self) -> Units_Quantity: 
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
    def InsertAfter(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Quantity) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Quantity) -> None: ...
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
    def Last(self) -> Units_Quantity: 
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
    def Prepend(self,theItem : Units_Quantity) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Units_QtsSequence) -> None: ...
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
    def Sequence(self) -> Units_QtsSequence: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Units_Quantity) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_QtsSequence) -> None: 
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
    def Value(self,theIndex : int) -> Units_Quantity: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Units_QtsSequence) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class Units_Quantity(OCP.Standard.Standard_Transient):
    """
    This class stores in its field all the possible units of all the unit systems for a given physical quantity. Each unit's value is expressed in the S.I. unit system.This class stores in its field all the possible units of all the unit systems for a given physical quantity. Each unit's value is expressed in the S.I. unit system.This class stores in its field all the possible units of all the unit systems for a given physical quantity. Each unit's value is expressed in the S.I. unit system.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimensions(self) -> Units_Dimensions: 
        """
        Returns the physical dimensions of the quantity.

        Returns the physical dimensions of the quantity.
        """
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        Useful for debugging.
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
    def IsEqual(self,astring : str) -> bool: 
        """
        Returns True if the name of the Quantity <me> is equal to <astring>, False otherwise.
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
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns in a AsciiString from TCollection the name of the quantity.

        Returns in a AsciiString from TCollection the name of the quantity.
        """
    def Sequence(self) -> Units_UnitsSequence: 
        """
        Returns <theunitssequence>, which is the sequence of all the units stored for this physical quantity.

        Returns <theunitssequence>, which is the sequence of all the units stored for this physical quantity.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,aname : str,adimensions : Units_Dimensions,aunitssequence : Units_UnitsSequence) -> None: ...
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
class Units_MathSentence(Units_Sentence):
    """
    This class defines all the methods to create and compute an algebraic formula.
    """
    def Dump(self) -> None: 
        """
        Useful for debugging.

        Useful for debugging.
        """
    def Evaluate(self) -> Units_Token: 
        """
        Computes and returns in a token the result of the expression.
        """
    def IsDone(self) -> bool: 
        """
        Return True if number of created tokens > 0 (i.e creation of sentence is successful)

        Return True if number of created tokens > 0 (i.e creation of sentence is successful)
        """
    @overload
    def Sequence(self,asequenceoftokens : Units_TokensSequence) -> None: 
        """
        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.

        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.
        """
    @overload
    def Sequence(self) -> Units_TokensSequence: ...
    def SetConstants(self) -> None: 
        """
        For each constant encountered, sets the value.
        """
    def __init__(self,astring : str) -> None: ...
    pass
class Units_Token(OCP.Standard.Standard_Transient):
    """
    This class defines an elementary word contained in a Sentence object.This class defines an elementary word contained in a Sentence object.This class defines an elementary word contained in a Sentence object.
    """
    @overload
    def Add(self,atoken : Units_Token) -> Units_Token: 
        """
        None

        Returns a token which is the addition of <me> and another token <atoken>. The addition is possible if and only if the dimensions are the same.
        """
    @overload
    def Add(self,aninteger : int) -> Units_Token: ...
    def Creates(self) -> Units_Token: 
        """
        Creates and returns a token, which is a ShiftedToken.
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
    def Dimensions(self,adimensions : Units_Dimensions) -> None: 
        """
        Returns the dimensions of the token <thedimensions>.

        Sets the field <thedimensions> to <adimensions>.

        Returns the dimensions of the token <thedimensions>.
        """
    @overload
    def Dimensions(self) -> Units_Dimensions: ...
    def Divide(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the division of <me> by another token <atoken>.
        """
    def Divided(self,avalue : float) -> float: 
        """
        This virtual method is called by the Measurement methods, to compute the measurement during a conversion.
        """
    def Dump(self,ashift : int,alevel : int) -> None: 
        """
        Useful for debugging
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
    def IsEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns true if the field <theword> and the string <astring> are the same, false otherwise.

        Returns true if the field <theword> and the string <theword> contained in the token <atoken> are the same, false otherwise.
        """
    @overload
    def IsEqual(self,astring : str) -> bool: ...
    @overload
    def IsGreater(self,atoken : Units_Token) -> bool: 
        """
        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.
        """
    @overload
    def IsGreater(self,astring : str) -> bool: ...
    def IsGreaterOrEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns true if the string <astring> is strictly contained at the beginning of the field <theword> false otherwise.

        Returns true if the string <astring> is strictly contained at the beginning of the field <theword> false otherwise.
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
    def IsLessOrEqual(self,astring : str) -> bool: 
        """
        Returns true if the field <theword> is strictly contained at the beginning of the string <astring>, false otherwise.

        Returns true if the field <theword> is strictly contained at the beginning of the string <astring>, false otherwise.
        """
    @overload
    def IsNotEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns false if the field <theword> and the string <astring> are the same, true otherwise.

        Returns false if the field <theword> and the string <theword> contained in the token <atoken> are the same, true otherwise.

        Returns false if the field <theword> and the string <astring> are the same, true otherwise.

        Returns false if the field <theword> and the string <theword> contained in the token <atoken> are the same, true otherwise.
        """
    @overload
    def IsNotEqual(self,astring : str) -> bool: ...
    def Length(self) -> int: 
        """
        Returns the length of the word.
        """
    @overload
    def Mean(self,amean : str) -> None: 
        """
        Returns the significance of the word <theword>, which is in the field <themean>.

        Sets the field <themean> to <amean>.

        Returns the significance of the word <theword>, which is in the field <themean>.

        Sets the field <themean> to <amean>.
        """
    @overload
    def Mean(self) -> OCP.TCollection.TCollection_AsciiString: ...
    def Multiplied(self,avalue : float) -> float: 
        """
        This virtual method is called by the Measurement methods, to compute the measurement during a conversion.
        """
    def Multiply(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the product of <me> and another token <atoken>.
        """
    @overload
    def Power(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is <me> to the power of another token <atoken>. The computation is possible only if <atoken> is a dimensionless constant.

        Returns a token which is <me> to the power of <anexponent>.
        """
    @overload
    def Power(self,anexponent : float) -> Units_Token: ...
    def Subtract(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the subtraction of <me> and another token <atoken>. The subtraction is possible if and only if the dimensions are the same.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,amean : str) -> None: 
        """
        Updates the token <me> with the additional signification <amean> by concatenation of the two strings <themean> and <amean>. If the two significations are the same , an information message is written in the output device.
        """
    @overload
    def Value(self) -> float: 
        """
        Returns the value stored in the field <thevalue>.

        Sets the field <thevalue> to <avalue>.

        Returns the value stored in the field <thevalue>.

        Sets the field <thevalue> to <avalue>.
        """
    @overload
    def Value(self,avalue : float) -> None: ...
    @overload
    def Word(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the string <theword>

        Sets the field <theword> to <aword>.

        Returns the string <theword>

        Sets the field <theword> to <aword>.
        """
    @overload
    def Word(self,aword : str) -> None: ...
    @overload
    def __init__(self,aword : str,amean : str) -> None: ...
    @overload
    def __init__(self,aword : str) -> None: ...
    @overload
    def __init__(self,aword : str,amean : str,avalue : float) -> None: ...
    @overload
    def __init__(self,aword : str,amean : str,avalue : float,adimension : Units_Dimensions) -> None: ...
    @overload
    def __init__(self,atoken : Units_Token) -> None: ...
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
class Units_Unit(OCP.Standard.Standard_Transient):
    """
    This class defines an elementary word contained in a physical quantity.This class defines an elementary word contained in a physical quantity.This class defines an elementary word contained in a physical quantity.
    """
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
        Useful for debugging
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
    def IsEqual(self,astring : str) -> bool: 
        """
        Compares all the symbols linked within <me> with the name of <atoken>, and returns True if there is one symbol equal to the name, False otherwise.
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
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the unit <thename>

        Returns the name of the unit <thename>
        """
    @overload
    def Quantity(self,aquantity : Units_Quantity) -> None: 
        """
        Returns <thequantity> contained in <me>.

        Sets the physical Quantity <aquantity> to <me>.

        Returns <thequantity> contained in <me>.

        Sets the physical Quantity <aquantity> to <me>.
        """
    @overload
    def Quantity(self) -> Units_Quantity: ...
    def Symbol(self,asymbol : str) -> None: 
        """
        Adds a new symbol <asymbol> attached to <me>.
        """
    def SymbolsSequence(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the sequence of symbols <thesymbolssequence>

        Returns the sequence of symbols <thesymbolssequence>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Token(self) -> Units_Token: 
        """
        Starting with <me>, returns a new Token object.
        """
    @overload
    def Value(self) -> float: 
        """
        Returns the value in relation with the International System of Units.

        Sets the value <avalue> to <me>.

        Returns the value in relation with the International System of Units.

        Sets the value <avalue> to <me>.
        """
    @overload
    def Value(self,avalue : float) -> None: ...
    @overload
    def __init__(self,aname : str,asymbol : str) -> None: ...
    @overload
    def __init__(self,aname : str,asymbol : str,avalue : float,aquantity : Units_Quantity) -> None: ...
    @overload
    def __init__(self,aname : str) -> None: ...
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
class Units_TksSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Units_Token) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Units_TksSequence) -> None: ...
    def Assign(self,theOther : Units_TksSequence) -> Units_TksSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Token: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Token: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Units_Token: 
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
    def First(self) -> Units_Token: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Units_TksSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Token) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Token) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_TksSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Units_Token: 
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
    def Prepend(self,theItem : Units_Token) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Units_TksSequence) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Units_Token) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_TksSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Units_Token: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Units_TksSequence) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Units_ShiftedToken(Units_Token, OCP.Standard.Standard_Transient):
    """
    The ShiftedToken class inherits from Token and describes tokens which have a gap in addition of the multiplicative factor. This kind of token allows the description of linear functions which do not pass through the origin, of the form :The ShiftedToken class inherits from Token and describes tokens which have a gap in addition of the multiplicative factor. This kind of token allows the description of linear functions which do not pass through the origin, of the form :The ShiftedToken class inherits from Token and describes tokens which have a gap in addition of the multiplicative factor. This kind of token allows the description of linear functions which do not pass through the origin, of the form :
    """
    @overload
    def Add(self,atoken : Units_Token) -> Units_Token: 
        """
        None

        Returns a token which is the addition of <me> and another token <atoken>. The addition is possible if and only if the dimensions are the same.
        """
    @overload
    def Add(self,aninteger : int) -> Units_Token: ...
    def Creates(self) -> Units_Token: 
        """
        Creates and returns a token, which is a ShiftedToken.
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
    def Dimensions(self,adimensions : Units_Dimensions) -> None: 
        """
        Returns the dimensions of the token <thedimensions>.

        Sets the field <thedimensions> to <adimensions>.

        Returns the dimensions of the token <thedimensions>.
        """
    @overload
    def Dimensions(self) -> Units_Dimensions: ...
    def Divide(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the division of <me> by another token <atoken>.
        """
    def Divided(self,avalue : float) -> float: 
        """
        This virtual method is called by the Measurement methods, to compute the measurement during a conversion.
        """
    def Dump(self,ashift : int,alevel : int) -> None: 
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
    def IsEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns true if the field <theword> and the string <astring> are the same, false otherwise.

        Returns true if the field <theword> and the string <theword> contained in the token <atoken> are the same, false otherwise.
        """
    @overload
    def IsEqual(self,astring : str) -> bool: ...
    @overload
    def IsGreater(self,atoken : Units_Token) -> bool: 
        """
        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.

        Returns false if the field <theword> is strictly contained at the beginning of the string <astring>, true otherwise.
        """
    @overload
    def IsGreater(self,astring : str) -> bool: ...
    def IsGreaterOrEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns true if the string <astring> is strictly contained at the beginning of the field <theword> false otherwise.

        Returns true if the string <astring> is strictly contained at the beginning of the field <theword> false otherwise.
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
    def IsLessOrEqual(self,astring : str) -> bool: 
        """
        Returns true if the field <theword> is strictly contained at the beginning of the string <astring>, false otherwise.

        Returns true if the field <theword> is strictly contained at the beginning of the string <astring>, false otherwise.
        """
    @overload
    def IsNotEqual(self,atoken : Units_Token) -> bool: 
        """
        Returns false if the field <theword> and the string <astring> are the same, true otherwise.

        Returns false if the field <theword> and the string <theword> contained in the token <atoken> are the same, true otherwise.

        Returns false if the field <theword> and the string <astring> are the same, true otherwise.

        Returns false if the field <theword> and the string <theword> contained in the token <atoken> are the same, true otherwise.
        """
    @overload
    def IsNotEqual(self,astring : str) -> bool: ...
    def Length(self) -> int: 
        """
        Returns the length of the word.
        """
    @overload
    def Mean(self,amean : str) -> None: 
        """
        Returns the significance of the word <theword>, which is in the field <themean>.

        Sets the field <themean> to <amean>.

        Returns the significance of the word <theword>, which is in the field <themean>.

        Sets the field <themean> to <amean>.
        """
    @overload
    def Mean(self) -> OCP.TCollection.TCollection_AsciiString: ...
    def Move(self) -> float: 
        """
        Returns the gap <themove>
        """
    def Multiplied(self,avalue : float) -> float: 
        """
        This virtual method is called by the Measurement methods, to compute the measurement during a conversion.
        """
    def Multiply(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the product of <me> and another token <atoken>.
        """
    @overload
    def Power(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is <me> to the power of another token <atoken>. The computation is possible only if <atoken> is a dimensionless constant.

        Returns a token which is <me> to the power of <anexponent>.
        """
    @overload
    def Power(self,anexponent : float) -> Units_Token: ...
    def Subtract(self,atoken : Units_Token) -> Units_Token: 
        """
        Returns a token which is the subtraction of <me> and another token <atoken>. The subtraction is possible if and only if the dimensions are the same.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,amean : str) -> None: 
        """
        Updates the token <me> with the additional signification <amean> by concatenation of the two strings <themean> and <amean>. If the two significations are the same , an information message is written in the output device.
        """
    @overload
    def Value(self) -> float: 
        """
        Returns the value stored in the field <thevalue>.

        Sets the field <thevalue> to <avalue>.

        Returns the value stored in the field <thevalue>.

        Sets the field <thevalue> to <avalue>.
        """
    @overload
    def Value(self,avalue : float) -> None: ...
    @overload
    def Word(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the string <theword>

        Sets the field <theword> to <aword>.

        Returns the string <theword>

        Sets the field <theword> to <aword>.
        """
    @overload
    def Word(self,aword : str) -> None: ...
    def __init__(self,aword : str,amean : str,avalue : float,amove : float,adimensions : Units_Dimensions) -> None: ...
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
class Units_TokensSequence(Units_TksSequence, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : Units_TksSequence) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : Units_Token) -> None: ...
    def Assign(self,theOther : Units_TksSequence) -> Units_TksSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Token: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Token: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Units_TksSequence: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Units_Token: 
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
    def First(self) -> Units_Token: 
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
    def InsertAfter(self,theIndex : int,theSeq : Units_TksSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Token) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Token) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_TksSequence) -> None: ...
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
    def Last(self) -> Units_Token: 
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
    def Prepend(self,theItem : Units_Token) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Units_TksSequence) -> None: ...
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
    def Sequence(self) -> Units_TksSequence: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Units_Token) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_TksSequence) -> None: 
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
    def Value(self,theIndex : int) -> Units_Token: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Units_TksSequence) -> None: ...
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
class Units_ShiftedUnit(Units_Unit, OCP.Standard.Standard_Transient):
    """
    This class is useful to describe units with a shifted origin in relation to another unit. A well known example is the Celsius degrees in relation to Kelvin degrees. The shift of the Celsius origin is 273.15 Kelvin degrees.This class is useful to describe units with a shifted origin in relation to another unit. A well known example is the Celsius degrees in relation to Kelvin degrees. The shift of the Celsius origin is 273.15 Kelvin degrees.This class is useful to describe units with a shifted origin in relation to another unit. A well known example is the Celsius degrees in relation to Kelvin degrees. The shift of the Celsius origin is 273.15 Kelvin degrees.
    """
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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEqual(self,astring : str) -> bool: 
        """
        Compares all the symbols linked within <me> with the name of <atoken>, and returns True if there is one symbol equal to the name, False otherwise.
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
    @overload
    def Move(self,amove : float) -> None: 
        """
        Sets the field <themove> to <amove>

        Returns the shifted value <themove>.
        """
    @overload
    def Move(self) -> float: ...
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the unit <thename>

        Returns the name of the unit <thename>
        """
    @overload
    def Quantity(self,aquantity : Units_Quantity) -> None: 
        """
        Returns <thequantity> contained in <me>.

        Sets the physical Quantity <aquantity> to <me>.

        Returns <thequantity> contained in <me>.

        Sets the physical Quantity <aquantity> to <me>.
        """
    @overload
    def Quantity(self) -> Units_Quantity: ...
    def Symbol(self,asymbol : str) -> None: 
        """
        Adds a new symbol <asymbol> attached to <me>.
        """
    def SymbolsSequence(self) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the sequence of symbols <thesymbolssequence>

        Returns the sequence of symbols <thesymbolssequence>
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Token(self) -> Units_Token: 
        """
        This redefined method returns a ShiftedToken object.
        """
    @overload
    def Value(self) -> float: 
        """
        Returns the value in relation with the International System of Units.

        Sets the value <avalue> to <me>.

        Returns the value in relation with the International System of Units.

        Sets the value <avalue> to <me>.
        """
    @overload
    def Value(self,avalue : float) -> None: ...
    @overload
    def __init__(self,aname : str) -> None: ...
    @overload
    def __init__(self,aname : str,asymbol : str,avalue : float,amove : float,aquantity : Units_Quantity) -> None: ...
    @overload
    def __init__(self,aname : str,asymbol : str) -> None: ...
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
class Units_UnitSentence(Units_Sentence):
    """
    This class describes all the facilities to manipulate and compute units contained in a string expression.
    """
    def Analyse(self) -> None: 
        """
        Analyzes the sequence of tokens created by the constructor to find the true significance of each token.
        """
    def Dump(self) -> None: 
        """
        Useful for debugging.

        Useful for debugging.
        """
    def Evaluate(self) -> Units_Token: 
        """
        Computes and returns in a token the result of the expression.
        """
    def IsDone(self) -> bool: 
        """
        Return True if number of created tokens > 0 (i.e creation of sentence is successful)

        Return True if number of created tokens > 0 (i.e creation of sentence is successful)
        """
    @overload
    def Sequence(self,asequenceoftokens : Units_TokensSequence) -> None: 
        """
        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.

        Returns <thesequenceoftokens>.

        Sets the field <thesequenceoftokens> to <asequenceoftokens>.
        """
    @overload
    def Sequence(self) -> Units_TokensSequence: ...
    def SetConstants(self) -> None: 
        """
        For each constant encountered, sets the value.
        """
    def SetUnits(self,aquantitiessequence : Units_QuantitiesSequence) -> None: 
        """
        For each token which represents a unit, finds in the sequence of physical quantities all the characteristics of the unit found.
        """
    @overload
    def __init__(self,astring : str,aquantitiessequence : Units_QuantitiesSequence) -> None: ...
    @overload
    def __init__(self,astring : str) -> None: ...
    pass
class Units_UnitsDictionary(OCP.Standard.Standard_Transient):
    """
    This class creates a dictionary of all the units you want to know.This class creates a dictionary of all the units you want to know.This class creates a dictionary of all the units you want to know.
    """
    def ActiveUnit(self,aquantity : str) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns for <aquantity> the active unit.
        """
    def Creates(self) -> None: 
        """
        Returns a UnitsDictionary object which contains the sequence of all the units you want to consider, physical quantity by physical quantity.
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
    def Dump(self,alevel : int) -> None: 
        """
        Dumps only the sequence of quantities without the units if <alevel> is equal to zero, and for each quantity all the units stored if <alevel> is equal to one.

        Dumps for a designated physical dimensions <adimensions> all the previously stored units.

        Dumps only the sequence of quantities without the units if <alevel> is equal to zero, and for each quantity all the units stored if <alevel> is equal to one.

        Dumps for a designated physical dimensions <adimensions> all the previously stored units.
        """
    @overload
    def Dump(self,adimensions : Units_Dimensions) -> None: ...
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
    def Sequence(self) -> Units_QuantitiesSequence: 
        """
        Returns the head of the sequence of physical quantities.

        Returns the head of the sequence of physical quantities.
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
class Units_UnitsLexicon(Units_Lexicon, OCP.Standard.Standard_Transient):
    """
    This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.This class defines a lexicon useful to analyse and recognize the different key words included in a sentence. The lexicon is stored in a sequence of tokens.
    """
    def AddToken(self,aword : str,amean : str,avalue : float) -> None: 
        """
        Adds to the lexicon a new token with <aword>, <amean>, <avalue> as arguments. If there is already a token with the field <theword> equal to <aword>, the existing token is updated.
        """
    def Creates(self,amode : bool=True) -> None: 
        """
        Reads the files <afilename1> and <afilename2> to create a sequence of tokens stored in <thesequenceoftokens>.
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
        Useful for debugging.

        Useful for debugging.
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
    def Sequence(self) -> Units_TokensSequence: 
        """
        Returns the first item of the sequence of tokens.

        Returns the first item of the sequence of tokens.
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
class Units_UtsSequence(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Units_UtsSequence) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Units_Unit) -> None: ...
    def Assign(self,theOther : Units_UtsSequence) -> Units_UtsSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Unit: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Unit: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Units_Unit: 
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
    def First(self) -> Units_Unit: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Units_UtsSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Unit) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Unit) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_UtsSequence) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Units_Unit: 
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
    def Prepend(self,theSeq : Units_UtsSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Units_Unit) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Units_Unit) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_UtsSequence) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Units_Unit: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Units_UtsSequence) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Units_UnitsSystem(OCP.Standard.Standard_Transient):
    """
    This class allows the user to define his own system of units.This class allows the user to define his own system of units.This class allows the user to define his own system of units.
    """
    def Activate(self,aquantity : str,aunit : str) -> None: 
        """
        Specifies for <aquantity> the unit <aunit> used.
        """
    def Activates(self) -> None: 
        """
        Activates the first unit of all defined system quantities
        """
    def ActiveUnit(self,aquantity : str) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns for <aquantity> the active unit.
        """
    def ActiveUnitsSequence(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns a sequence of integer in correspondence with the sequence of quantities, which indicates, for each redefined quantity, the index into the sequence of units, of the active unit.
        """
    def ConvertSIValueToUserSystem(self,aquantity : str,avalue : float) -> float: 
        """
        Converts the real value <avalue> from the S.I. system of units to the user system of units. <aquantity> is the physical dimensions of the measurement.
        """
    def ConvertUserSystemValueToSI(self,aquantity : str,avalue : float) -> float: 
        """
        Converts the real value <avalue> from the user system of units to the S.I. system of units. <aquantity> is the physical dimensions of the measurement.
        """
    def ConvertValueToUserSystem(self,aquantity : str,avalue : float,aunit : str) -> float: 
        """
        Converts a real value <avalue> from the unit <aunit> belonging to the physical dimensions <aquantity> to the corresponding unit of the user system.
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
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if no units has been defined in the system.
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
    def QuantitiesSequence(self) -> Units_QuantitiesSequence: 
        """
        Returns the sequence of refined quantities.
        """
    def Remove(self,aquantity : str,aunit : str) -> None: 
        """
        Removes for <aquantity> the unit <aunit> used.
        """
    def Specify(self,aquantity : str,aunit : str) -> None: 
        """
        Specifies for <aquantity> the unit <aunit> used.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,aName : str,Verbose : bool=False) -> None: ...
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
class Units_UnitsSequence(Units_UtsSequence, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : Units_UtsSequence) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : Units_Unit) -> None: ...
    def Assign(self,theOther : Units_UtsSequence) -> Units_UtsSequence: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Units_Unit: 
        """
        First item access
        """
    def ChangeLast(self) -> Units_Unit: 
        """
        Last item access
        """
    def ChangeSequence(self) -> Units_UtsSequence: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> Units_Unit: 
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
    def First(self) -> Units_Unit: 
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
    def InsertAfter(self,theIndex : int,theSeq : Units_UtsSequence) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Units_Unit) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Units_Unit) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Units_UtsSequence) -> None: ...
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
    def Last(self) -> Units_Unit: 
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
    def Prepend(self,theSeq : Units_UtsSequence) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Units_Unit) -> None: ...
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
    def Sequence(self) -> Units_UtsSequence: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : Units_Unit) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Units_UtsSequence) -> None: 
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
    def Value(self,theIndex : int) -> Units_Unit: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Units_UtsSequence) -> None: ...
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
@overload
def __add__(arg0 : Units_Token,arg1 : int) -> Units_Token:
    """
    None

    None
    """
@overload
def __add__(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    pass
@overload
def __mul__(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    """
    None

    None
    """
@overload
def __mul__(arg0 : Units_Dimensions,arg1 : Units_Dimensions) -> Units_Dimensions:
    pass
@overload
def __rmul__(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    """
    None

    None
    """
@overload
def __rmul__(arg0 : Units_Dimensions,arg1 : Units_Dimensions) -> Units_Dimensions:
    pass
def __sub__(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    """
    None
    """
@overload
def __truediv__(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    """
    None

    None
    """
@overload
def __truediv__(arg0 : Units_Dimensions,arg1 : Units_Dimensions) -> Units_Dimensions:
    pass
@overload
def pow(arg0 : Units_Token,arg1 : Units_Token) -> Units_Token:
    """
    None

    None

    None
    """
@overload
def pow(arg0 : Units_Dimensions,arg1 : float) -> Units_Dimensions:
    pass
@overload
def pow(arg0 : Units_Token,arg1 : float) -> Units_Token:
    pass
