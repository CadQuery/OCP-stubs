import OCP.TCollection
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import io
__all__  = [
"TCollection",
"TCollection_AsciiString",
"TCollection_BaseSequence",
"TCollection_BasicMap",
"TCollection_BasicMapIterator",
"TCollection_ExtendedString",
"TCollection_HAsciiString",
"TCollection_HExtendedString",
"TCollection_MapNode",
"TCollection_SeqNode",
"TCollection_Side",
"HashCode",
"IsEqual",
"TCollection_Left",
"TCollection_Right"
]
class TCollection():
    """
    The package <TCollection> provides the services for the transient basic data structures.
    """
    @staticmethod
    def NextPrimeForMap_s(I : int) -> int: 
        """
        Returns a prime number greater than <I> suitable to dimension a Map. When <I> becomes great there is a limit on the result (today the limit is around 1 000 000). This is not a limit of the number of items but a limit in the number of buckets. i.e. there will be more collisions in the map.
        """
    def __init__(self) -> None: ...
    pass
class TCollection_AsciiString():
    """
    Class defines a variable-length sequence of 8-bit characters. Despite class name (kept for historical reasons), it is intended to store UTF-8 string, not just ASCII characters. However, multi-byte nature of UTF-8 is not considered by the following methods: - Method ::Length() return the number of bytes, not the number of Unicode symbols. - Methods taking/returning symbol index work with 8-bit code units, not true Unicode symbols, including ::Remove(), ::SetValue(), ::Value(), ::Search(), ::Trunc() and others. If application needs to process multi-byte Unicode symbols explicitly, NCollection_Utf8Iter class can be used for iterating through Unicode string (UTF-32 code unit will be returned for each position).
    """
    @overload
    def AssignCat(self,other : str) -> None: 
        """
        Appends <other> to me. This is an unary operator.

        Appends <other> to me. This is an unary operator.

        Appends <other> to me. This is an unary operator.

        Appends <other> to me. This is an unary operator. ex: aString += "Dummy" To catenate more than one CString, you must put a AsciiString before. Example: aString += "Hello " + "Dolly" IS NOT VALID ! But astring += anotherString + "Hello " + "Dolly" is valid.

        Appends <other> to me. This is an unary operator. Example: aString += anotherString
        """
    @overload
    def AssignCat(self,other : float) -> None: ...
    @overload
    def AssignCat(self,other : TCollection_AsciiString) -> None: ...
    @overload
    def AssignCat(self,other : int) -> None: ...
    def Capitalize(self) -> None: 
        """
        Converts the first character into its corresponding upper-case character and the other characters into lowercase Example: before me = "hellO " after me = "Hello "
        """
    @overload
    def Cat(self,other : float) -> TCollection_AsciiString: 
        """
        Appends <other> to me. Syntax: aString = aString + "Dummy" Example: aString contains "I say " aString = aString + "Hello " + "Dolly" gives "I say Hello Dolly" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + 15; Example: aString contains "I say " gives "I say 15" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + 15.15; Example: aString contains "I say " gives "I say 15.15" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + "Dummy" Example: aString contains "I say " aString = aString + "Hello " + "Dolly" gives "I say Hello Dolly" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Example: aString = aString + anotherString

        Appends <other> to me. Example: aString = aString + anotherString

        Appends <other> to me. Syntax: aString = aString + "Dummy" Example: aString contains "I say " aString = aString + "Hello " + "Dolly" gives "I say Hello Dolly" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + "Dummy" Example: aString contains "I say " aString = aString + "Hello " + "Dolly" gives "I say Hello Dolly" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + 15; Example: aString contains "I say " gives "I say 15" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Appends <other> to me. Syntax: aString = aString + 15.15; Example: aString contains "I say " gives "I say 15.15" To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.
        """
    @overload
    def Cat(self,other : int) -> TCollection_AsciiString: ...
    @overload
    def Cat(self,other : TCollection_AsciiString) -> TCollection_AsciiString: ...
    @overload
    def Cat(self,other : str) -> TCollection_AsciiString: ...
    def Center(self,Width : int,Filler : str) -> None: 
        """
        Modifies this ASCII string so that its length becomes equal to Width and the new characters are equal to Filler. New characters are added both at the beginning and at the end of this string. If Width is less than the length of this ASCII string, nothing happens. Example TCollection_AsciiString myAlphabet("abcdef"); myAlphabet.Center(9,' '); assert ( myAlphabet == " abcdef " );
        """
    def ChangeAll(self,aChar : str,NewChar : str,CaseSensitive : bool=True) -> None: 
        """
        Substitutes all the characters equal to aChar by NewChar in the AsciiString <me>. The substitution can be case sensitive. If you don't use default case sensitive, no matter wether aChar is uppercase or not. Example: me = "Histake" -> ChangeAll('H','M',Standard_True) gives me = "Mistake"
        """
    def Clear(self) -> None: 
        """
        Removes all characters contained in <me>. This produces an empty AsciiString.
        """
    @overload
    def Copy(self,fromwhere : TCollection_AsciiString) -> None: 
        """
        Copy <fromwhere> to <me>. Used as operator = Example: aString = anotherCString;

        Copy <fromwhere> to <me>. Used as operator = Example: aString = anotherString;
        """
    @overload
    def Copy(self,fromwhere : str) -> None: ...
    def EndsWith(self,theEndString : TCollection_AsciiString) -> bool: 
        """
        Determines whether the end of this string instance matches the specified string.
        """
    def FirstLocationInSet(self,Set : TCollection_AsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        Returns the index of the first character of <me> that is present in <Set>. The search begins to the index FromIndex and ends to the the index ToIndex. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7 after me = "aabAcAa" returns 1
        """
    def FirstLocationNotInSet(self,Set : TCollection_AsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        Returns the index of the first character of <me> that is not present in the set <Set>. The search begins to the index FromIndex and ends to the the index ToIndex in <me>. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7 after me = "aabAcAa" returns 3
        """
    @staticmethod
    def HashCode_s(theAsciiString : TCollection_AsciiString,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given ASCII string, in the range [1, theUpperBound]. Returns the same integer value as the hash function for TCollection_ExtendedString
        """
    @overload
    def Insert(self,where : int,what : TCollection_AsciiString) -> None: 
        """
        Inserts a Character at position <where>. Example: aString contains "hy not ?" aString.Insert(1,'W'); gives "Why not ?" aString contains "Wh" aString.Insert(3,'y'); gives "Why" aString contains "Way" aString.Insert(2,'h'); gives "Why"

        Inserts a CString at position <where>. Example: aString contains "O more" aString.Insert(2,"nce"); gives "Once more"

        Inserts a AsciiString at position <where>.
        """
    @overload
    def Insert(self,where : int,what : str) -> None: ...
    def InsertAfter(self,Index : int,other : TCollection_AsciiString) -> None: 
        """
        Pushing a string after a specific index in the string <me>. Raises an exception if Index is out of bounds. - less than 0 (InsertAfter), or less than 1 (InsertBefore), or - greater than the number of characters in this ASCII string. Example: before me = "cde" , Index = 0 , other = "ab" after me = "abcde" , other = "ab"
        """
    def InsertBefore(self,Index : int,other : TCollection_AsciiString) -> None: 
        """
        Pushing a string before a specific index in the string <me>. Raises an exception if Index is out of bounds. - less than 0 (InsertAfter), or less than 1 (InsertBefore), or - greater than the number of characters in this ASCII string. Example: before me = "cde" , Index = 1 , other = "ab" after me = "abcde" , other = "ab"
        """
    def IntegerValue(self) -> int: 
        """
        Converts a AsciiString containing a numeric expression to an Integer. Example: "215" returns 215.
        """
    def IsAscii(self) -> bool: 
        """
        Returns True if the AsciiString contains only ASCII characters between ' ' and '~'. This means no control character and no extended ASCII code.
        """
    @overload
    def IsDifferent(self,other : str) -> bool: 
        """
        Returns true if there are differences between the characters in this ASCII string and ASCII string other. Note that this method is an alias of operator !=

        Returns true if there are differences between the characters in this ASCII string and ASCII string other. Note that this method is an alias of operator !=
        """
    @overload
    def IsDifferent(self,other : TCollection_AsciiString) -> bool: ...
    def IsEmpty(self) -> bool: 
        """
        Returns True if the string <me> contains zero character.
        """
    @overload
    def IsEqual(self,other : str) -> bool: 
        """
        Returns true if the characters in this ASCII string are identical to the characters in ASCII string other. Note that this method is an alias of operator ==.

        Returns true if the characters in this ASCII string are identical to the characters in ASCII string other. Note that this method is an alias of operator ==.
        """
    @overload
    def IsEqual(self,other : TCollection_AsciiString) -> bool: ...
    @staticmethod
    @overload
    def IsEqual_s(string1 : TCollection_AsciiString,string2 : str) -> bool: 
        """
        Returns True when the two strings are the same. (Just for HashCode for AsciiString)

        Returns True when the two strings are the same. (Just for HashCode for AsciiString)
        """
    @staticmethod
    @overload
    def IsEqual_s(string1 : TCollection_AsciiString,string2 : TCollection_AsciiString) -> bool: ...
    @overload
    def IsGreater(self,other : TCollection_AsciiString) -> bool: 
        """
        Returns TRUE if <me> is 'ASCII' greater than <other>.

        Returns TRUE if <me> is 'ASCII' greater than <other>.
        """
    @overload
    def IsGreater(self,other : str) -> bool: ...
    def IsIntegerValue(self) -> bool: 
        """
        Returns True if the AsciiString contains an integer value. Note: an integer value is considered to be a real value as well.
        """
    @overload
    def IsLess(self,other : str) -> bool: 
        """
        Returns TRUE if <me> is 'ASCII' less than <other>.

        Returns TRUE if <me> is 'ASCII' less than <other>.
        """
    @overload
    def IsLess(self,other : TCollection_AsciiString) -> bool: ...
    def IsRealValue(self) -> bool: 
        """
        Returns True if the AsciiString contains a real value. Note: an integer value is considered to be a real value as well.
        """
    @staticmethod
    def IsSameString_s(theString1 : TCollection_AsciiString,theString2 : TCollection_AsciiString,theIsCaseSensitive : bool) -> bool: 
        """
        Returns True if the strings contain same characters.
        """
    def LeftAdjust(self) -> None: 
        """
        Removes all space characters in the begining of the string.
        """
    def LeftJustify(self,Width : int,Filler : str) -> None: 
        """
        left justify Length becomes equal to Width and the new characters are equal to Filler. If Width < Length nothing happens. Raises an exception if Width is less than zero. Example: before me = "abcdef" , Width = 9 , Filler = ' ' after me = "abcdef "
        """
    def Length(self) -> int: 
        """
        Returns number of characters in <me>. This is the same functionality as 'strlen' in C. Example TCollection_AsciiString myAlphabet("abcdef"); assert ( myAlphabet.Length() == 6 ); - 1 is the position of the first character in this string. - The length of this string gives the position of its last character. - Positions less than or equal to zero, or greater than the length of this string are invalid in functions which identify a character of this string by its position.

        Returns number of characters in <me>. This is the same functionality as 'strlen' in C. Example TCollection_AsciiString myAlphabet("abcdef"); assert ( myAlphabet.Length() == 6 ); - 1 is the position of the first character in this string. - The length of this string gives the position of its last character. - Positions less than or equal to zero, or greater than the length of this string are invalid in functions which identify a character of this string by its position.
        """
    @overload
    def Location(self,other : TCollection_AsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        Returns an index in the string <me> of the first occurence of the string S in the string <me> from the starting index FromIndex to the ending index ToIndex returns zero if failure Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAaAa", S = "Aa", FromIndex = 1, ToIndex = 7 after me = "aabAaAa" returns 4

        Returns the index of the nth occurence of the character C in the string <me> from the starting index FromIndex to the ending index ToIndex. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAa", N = 3, C = 'a', FromIndex = 1, ToIndex = 5 after me = "aabAa" returns 5
        """
    @overload
    def Location(self,N : int,C : str,FromIndex : int,ToIndex : int) -> int: ...
    def LowerCase(self) -> None: 
        """
        Converts <me> to its lower-case equivalent. Example TCollection_AsciiString myString("Hello Dolly"); myString.UpperCase(); assert ( myString == "HELLO DOLLY" ); myString.LowerCase(); assert ( myString == "hello dolly" );
        """
    def Prepend(self,other : TCollection_AsciiString) -> None: 
        """
        Inserts the string other at the beginning of this ASCII string. Example TCollection_AsciiString myAlphabet("cde"); TCollection_AsciiString myBegin("ab"); myAlphabet.Prepend(myBegin); assert ( myAlphabet == "abcde" );
        """
    def Print(self,astream : io.BytesIO) -> None: 
        """
        Displays <me> on a stream.
        """
    def Read(self,astream : io.BytesIO) -> None: 
        """
        Read <me> from a stream.
        """
    def RealValue(self) -> float: 
        """
        Converts an AsciiString containing a numeric expression. to a Real. Example: ex: "215" returns 215.0. ex: "3.14159267" returns 3.14159267.
        """
    def Remove(self,where : int,ahowmany : int=1) -> None: 
        """
        Erases <ahowmany> characters from position <where>, <where> included. Example: aString contains "Hello" aString.Remove(2,2) erases 2 characters from position 2 This gives "Hlo".
        """
    @overload
    def RemoveAll(self,what : str) -> None: 
        """
        Remove all the occurences of the character C in the string. Example: before me = "HellLLo", C = 'L' , CaseSensitive = True after me = "Hello"

        Removes every <what> characters from <me>.
        """
    @overload
    def RemoveAll(self,C : str,CaseSensitive : bool) -> None: ...
    def RightAdjust(self) -> None: 
        """
        Removes all space characters at the end of the string.
        """
    def RightJustify(self,Width : int,Filler : str) -> None: 
        """
        Right justify. Length becomes equal to Width and the new characters are equal to Filler. if Width < Length nothing happens. Raises an exception if Width is less than zero. Example: before me = "abcdef" , Width = 9 , Filler = ' ' after me = " abcdef"
        """
    @overload
    def Search(self,what : TCollection_AsciiString) -> int: 
        """
        Searches a CString in <me> from the beginning and returns position of first item <what> matching. it returns -1 if not found. Example: aString contains "Sample single test" aString.Search("le") returns 5

        Searches an AsciiString in <me> from the beginning and returns position of first item <what> matching. It returns -1 if not found.
        """
    @overload
    def Search(self,what : str) -> int: ...
    @overload
    def SearchFromEnd(self,what : TCollection_AsciiString) -> int: 
        """
        Searches a CString in a AsciiString from the end and returns position of first item <what> matching. It returns -1 if not found. Example: aString contains "Sample single test" aString.SearchFromEnd("le") returns 12

        Searches a AsciiString in another AsciiString from the end and returns position of first item <what> matching. It returns -1 if not found.
        """
    @overload
    def SearchFromEnd(self,what : str) -> int: ...
    @overload
    def SetValue(self,where : int,what : TCollection_AsciiString) -> None: 
        """
        Replaces one character in the AsciiString at position <where>. If <where> is less than zero or greater than the length of <me> an exception is raised. Example: aString contains "Garbake" astring.Replace(6,'g') gives <me> = "Garbage"

        Replaces a part of <me> by a CString. If <where> is less than zero or greater than the length of <me> an exception is raised. Example: aString contains "abcde" aString.SetValue(4,"1234567") gives <me> = "abc1234567"

        Replaces a part of <me> by another AsciiString.
        """
    @overload
    def SetValue(self,where : int,what : str) -> None: ...
    def Split(self,where : int) -> TCollection_AsciiString: 
        """
        Splits a AsciiString into two sub-strings. Example: aString contains "abcdefg" aString.Split(3) gives <me> = "abc" and returns "defg"
        """
    def StartsWith(self,theStartString : TCollection_AsciiString) -> bool: 
        """
        Determines whether the beginning of this string instance matches the specified string.
        """
    def SubString(self,FromIndex : int,ToIndex : int) -> TCollection_AsciiString: 
        """
        Creation of a sub-string of the string <me>. The sub-string starts to the index Fromindex and ends to the index ToIndex. Raises an exception if ToIndex or FromIndex is out of bounds Example: before me = "abcdefg", ToIndex=3, FromIndex=6 after me = "abcdefg" returns "cdef"

        Creation of a sub-string of the string <me>. The sub-string starts to the index Fromindex and ends to the index ToIndex. Raises an exception if ToIndex or FromIndex is out of bounds Example: before me = "abcdefg", ToIndex=3, FromIndex=6 after me = "abcdefg" returns "cdef"
        """
    def Swap(self,theOther : TCollection_AsciiString) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToCString(self) -> str: 
        """
        Returns pointer to AsciiString (char *). This is useful for some casual manipulations. Warning: Because this "char *" is 'const', you can't modify its contents.

        Returns pointer to AsciiString (char *). This is useful for some casual manipulations. Warning: Because this "char *" is 'const', you can't modify its contents.
        """
    def Token(self,separators : str=' \t',whichone : int=1) -> TCollection_AsciiString: 
        """
        Extracts <whichone> token from <me>. By default, the <separators> is set to space and tabulation. By default, the token extracted is the first one (whichone = 1). <separators> contains all separators you need. If no token indexed by <whichone> is found, it returns empty AsciiString. Example: aString contains "This is a message" aString.Token() returns "This" aString.Token(" ",4) returns "message" aString.Token(" ",2) returns "is" aString.Token(" ",9) returns "" Other separators than space character and tabulation are allowed : aString contains "1234; test:message , value" aString.Token("; :,",4) returns "value" aString.Token("; :,",2) returns "test"
        """
    def Trunc(self,ahowmany : int) -> None: 
        """
        Truncates <me> to <ahowmany> characters. Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel"
        """
    def UpperCase(self) -> None: 
        """
        Converts <me> to its upper-case equivalent.
        """
    def UsefullLength(self) -> int: 
        """
        Length of the string ignoring all spaces (' ') and the control character at the end.
        """
    def Value(self,where : int) -> str: 
        """
        Returns character at position <where> in <me>. If <where> is less than zero or greater than the lenght of <me>, an exception is raised. Example: aString contains "Hello" aString.Value(2) returns 'e'
        """
    @overload
    def __add__(self,other : str) -> TCollection_AsciiString: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def __add__(self,other : float) -> TCollection_AsciiString: ...
    @overload
    def __add__(self,other : TCollection_AsciiString) -> TCollection_AsciiString: ...
    @overload
    def __add__(self,other : int) -> TCollection_AsciiString: ...
    @overload
    def __iadd__(self,other : str) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def __iadd__(self,other : TCollection_AsciiString) -> None: ...
    @overload
    def __iadd__(self,other : float) -> None: ...
    @overload
    def __iadd__(self,other : int) -> None: ...
    @overload
    def __init__(self,aChar : str) -> None: ...
    @overload
    def __init__(self,astring : TCollection_ExtendedString,replaceNonAscii : str='\x00') -> None: ...
    @overload
    def __init__(self,message : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theStringUtf : str) -> None: ...
    @overload
    def __init__(self,astring : TCollection_AsciiString,message : str) -> None: ...
    @overload
    def __init__(self,value : float) -> None: ...
    @overload
    def __init__(self,value : int) -> None: ...
    @overload
    def __init__(self,message : str,aLen : int) -> None: ...
    @overload
    def __init__(self,astring : TCollection_AsciiString,message : TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,length : int,filler : str) -> None: ...
    @overload
    def __init__(self,astring : TCollection_AsciiString) -> None: ...
    pass
class TCollection_BaseSequence():
    """
    Definition of a base class for all instanciations of sequence.
    """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Swaps elements which are located at positions <I> and <J> in <me>. Raises an exception if I or J is out of bound. Example: before me = (A B C), I = 1, J = 3 after me = (C B A)
        """
    def IsEmpty(self) -> bool: 
        """
        returns True if the sequence <me> contains no elements.

        returns True if the sequence <me> contains no elements.
        """
    def Length(self) -> int: 
        """
        Returns the number of element(s) in the sequence. Returns zero if the sequence is empty.

        Returns the number of element(s) in the sequence. Returns zero if the sequence is empty.
        """
    def Reverse(self) -> None: 
        """
        Reverses the order of items on <me>. Example: before me = (A B C) after me = (C B A)
        """
    pass
class TCollection_BasicMap():
    """
    Root class of all the maps, provides utilitites for managing the buckets. Maps are dynamically extended data structures where data is quickly accessed with a key. General properties of maps - Map items may be (complex) non-unitary data; they may be difficult to manage with an array. Moreover, the map allows a data structure to be indexed by complex data. - The size of a map is dynamically extended. So a map may be first dimensioned for a little number of items. Maps avoid the use of large and quasi-empty arrays. - The access to a map item is much faster than the one to a sequence, a list, a queue or a stack item. - The access time to a map item may be compared with the one to an array item. First of all, it depends on the size of the map. It also depends on the quality of a user redefinable function (the hashing function) to find quickly where the item is. - The exploration of a map may be of better performance than the exploration of an array because the size of the map is adapted to the number of inserted items. These properties explain why maps are commonly used as internal data structures for algorithms. Definitions - A map is a data structure for which data is addressed by keys. - Once inserted in the map, a map item is referenced as an entry of the map. - Each entry of the map is addressed by a key. Two different keys address two different entries of the map. - The position of an entry in the map is called a bucket. - A map is dimensioned by its number of buckets, i.e. the maximum number of entries in the map. The performance of a map is conditioned by the number of buckets. - The hashing function transforms a key into a bucket index. The number of values that can be computed by the hashing function is equal to the number of buckets of the map. - Both the hashing function and the equality test between two keys are provided by a hasher object. - A map may be explored by a map iterator. This exploration provides only inserted entries in the map (i.e. non empty buckets). Collections' generic maps The Collections component provides numerous generic derived maps. - These maps include automatic management of the number of buckets: they are automatically resized when the number of keys exceeds the number of buckets. If you have a fair idea of the number of items in your map, you can save on automatic resizing by specifying a number of buckets at the time of construction, or by using a resizing function. This may be considered for crucial optimization issues. - Keys, items and hashers are parameters of these generic derived maps. - TCollection_MapHasher class describes the functions required by any hasher which is to be used with a map instantiated from the Collections component. - An iterator class is automatically instantiated at the time of instantiation of a map provided by the Collections component if this map is to be explored with an iterator. Note that some provided generic maps are not to be explored with an iterator but with indexes (indexed maps).
    """
    def Extent(self) -> int: 
        """
        Returns the number of keys already stored in <me>.

        Returns the number of keys already stored in <me>.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True when the map contains no keys. This is exactly Extent() == 0.

        Returns True when the map contains no keys. This is exactly Extent() == 0.
        """
    def NbBuckets(self) -> int: 
        """
        Returns the number of buckets in <me>.

        Returns the number of buckets in <me>.
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Prints on <S> usefull statistics about the map <me>. It can be used to test the quality of the hashcoding.
        """
    pass
class TCollection_BasicMapIterator():
    """
    This class provides basic services for the iterators on Maps. The iterators are inherited from this one.
    """
    def More(self) -> bool: 
        """
        Returns true if there is a current entry for this iterator in the map. Use the function Next to set this iterator to the position of the next entry, if it exists.

        Returns true if there is a current entry for this iterator in the map. Use the function Next to set this iterator to the position of the next entry, if it exists.
        """
    def Next(self) -> None: 
        """
        Sets this iterator to the position of the next entry of the map. Nothing is changed if there is no more entry to explore in the map: this iterator is always positioned on the last entry of the map but the function More returns false.
        """
    def Reset(self) -> None: 
        """
        Resets the iterator to the first node.
        """
    pass
class TCollection_ExtendedString():
    """
    A variable-length sequence of "extended" (UNICODE) characters (16-bit character type). It provides editing operations with built-in memory management to make ExtendedString objects easier to use than ordinary extended character arrays. ExtendedString objects follow "value semantics", that is, they are the actual strings, not handles to strings, and are copied through assignment. You may use HExtendedString objects to get handles to strings.
    """
    @overload
    def AssignCat(self,other : TCollection_ExtendedString) -> None: 
        """
        Appends the other extended string to this extended string. Note that this method is an alias of operator +=. Example: aString += anotherString

        Appends the utf16 char to this extended string.
        """
    @overload
    def AssignCat(self,theChar : str) -> None: ...
    def Cat(self,other : TCollection_ExtendedString) -> TCollection_ExtendedString: 
        """
        Appends <other> to me.
        """
    def ChangeAll(self,aChar : str,NewChar : str) -> None: 
        """
        Substitutes all the characters equal to aChar by NewChar in the ExtendedString <me>. The substitution can be case sensitive. If you don't use default case sensitive, no matter wether aChar is uppercase or not.
        """
    def Clear(self) -> None: 
        """
        Removes all characters contained in <me>. This produces an empty ExtendedString.
        """
    def Copy(self,fromwhere : TCollection_ExtendedString) -> None: 
        """
        Copy <fromwhere> to <me>. Used as operator =
        """
    def EndsWith(self,theEndString : TCollection_ExtendedString) -> bool: 
        """
        Determines whether the end of this string instance matches the specified string.
        """
    @staticmethod
    def HashCode_s(theString : TCollection_ExtendedString,theUpperBound : int) -> int: 
        """
        Returns a hashed value for the extended string within the range 1 .. theUpper. Note: if string is ASCII, the computed value is the same as the value computed with the HashCode function on a TCollection_AsciiString string composed with equivalent ASCII characters.
        """
    @overload
    def Insert(self,where : int,what : TCollection_ExtendedString) -> None: 
        """
        Insert a Character at position <where>.

        Insert a ExtendedString at position <where>.
        """
    @overload
    def Insert(self,where : int,what : str) -> None: ...
    def IsAscii(self) -> bool: 
        """
        Returns True if the ExtendedString contains only "Ascii Range" characters .
        """
    @overload
    def IsDifferent(self,other : TCollection_ExtendedString) -> bool: 
        """
        Returns true if there are differences between the characters in this extended string and the other extended string. Note that this method is an alias of operator !=.

        Returns true if there are differences between the characters in this extended string and the other extended string. Note that this method is an alias of operator !=.
        """
    @overload
    def IsDifferent(self,other : str) -> bool: ...
    def IsEmpty(self) -> bool: 
        """
        Returns True if this string contains no characters.
        """
    @overload
    def IsEqual(self,other : str) -> bool: 
        """
        Returns true if the characters in this extended string are identical to the characters in the other extended string. Note that this method is an alias of operator ==

        Returns true if the characters in this extended string are identical to the characters in the other extended string. Note that this method is an alias of operator ==
        """
    @overload
    def IsEqual(self,other : TCollection_ExtendedString) -> bool: ...
    @staticmethod
    def IsEqual_s(theString1 : TCollection_ExtendedString,theString2 : TCollection_ExtendedString) -> bool: 
        """
        Returns true if the characters in this extended string are identical to the characters in the other extended string. Note that this method is an alias of operator ==.
        """
    @overload
    def IsGreater(self,other : TCollection_ExtendedString) -> bool: 
        """
        Returns TRUE if <me> is greater than <other>.

        Returns TRUE if <me> is greater than <other>.
        """
    @overload
    def IsGreater(self,other : str) -> bool: ...
    @overload
    def IsLess(self,other : TCollection_ExtendedString) -> bool: 
        """
        Returns TRUE if <me> is less than <other>.

        Returns TRUE if <me> is less than <other>.
        """
    @overload
    def IsLess(self,other : str) -> bool: ...
    def Length(self) -> int: 
        """
        Returns the number of 16-bit code units (might be greater than number of Unicode symbols if string contains surrogate pairs).
        """
    def LengthOfCString(self) -> int: 
        """
        Returns expected CString length in UTF8 coding. It can be used for memory calculation before converting to CString containing symbols in UTF8 coding.
        """
    def Print(self,astream : io.BytesIO) -> None: 
        """
        Displays <me> .
        """
    def Remove(self,where : int,ahowmany : int=1) -> None: 
        """
        Erases <ahowmany> characters from position <where>,<where> included.
        """
    def RemoveAll(self,what : str) -> None: 
        """
        Removes every <what> characters from <me>.
        """
    def Search(self,what : TCollection_ExtendedString) -> int: 
        """
        Searches a ExtendedString in <me> from the beginning and returns position of first item <what> matching. it returns -1 if not found.
        """
    def SearchFromEnd(self,what : TCollection_ExtendedString) -> int: 
        """
        Searches a ExtendedString in another ExtendedString from the end and returns position of first item <what> matching. it returns -1 if not found.
        """
    @overload
    def SetValue(self,where : int,what : TCollection_ExtendedString) -> None: 
        """
        Replaces one character in the ExtendedString at position <where>. If <where> is less than zero or greater than the length of <me> an exception is raised.

        Replaces a part of <me> by another ExtendedString see above.
        """
    @overload
    def SetValue(self,where : int,what : str) -> None: ...
    def Split(self,where : int) -> TCollection_ExtendedString: 
        """
        Splits this extended string into two sub-strings at position where. - The second sub-string (from position where + 1 of this string to the end) is returned in a new extended string. - this extended string is modified: its last characters are removed, it becomes equal to the first sub-string (from the first character to position where). Example: aString contains "abcdefg" aString.Split(3) gives <me> = "abc" and returns "defg"
        """
    def StartsWith(self,theStartString : TCollection_ExtendedString) -> bool: 
        """
        Determines whether the beginning of this string instance matches the specified string.
        """
    def Swap(self,theOther : TCollection_ExtendedString) -> None: 
        """
        Exchange the data of two strings (without reallocating memory).
        """
    def ToExtString(self) -> str: 
        """
        Returns pointer to ExtString
        """
    def Token(self,separators : str,whichone : int=1) -> TCollection_ExtendedString: 
        """
        Extracts <whichone> token from <me>. By default, the <separators> is set to space and tabulation. By default, the token extracted is the first one (whichone = 1). <separators> contains all separators you need. If no token indexed by <whichone> is found, it returns an empty AsciiString. Example: aString contains "This is a message" aString.Token() returns "This" aString.Token(" ",4) returns "message" aString.Token(" ",2) returns "is" aString.Token(" ",9) returns "" Other separators than space character and tabulation are allowed : aString contains "1234; test:message , value" aString.Token("; :,",4) returns "value" aString.Token("; :,",2) returns "test"
        """
    def Trunc(self,ahowmany : int) -> None: 
        """
        Truncates <me> to <ahowmany> characters. Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel" Exceptions Standard_OutOfRange if ahowmany is greater than the length of this string.
        """
    def Value(self,where : int) -> str: 
        """
        Returns character at position <where> in <me>. If <where> is less than zero or greater than the lenght of <me>, an exception is raised. Example: aString contains "Hello" aString.Value(2) returns 'e' Exceptions Standard_OutOfRange if where lies outside the bounds of this extended string.
        """
    def __add__(self,other : TCollection_ExtendedString) -> TCollection_ExtendedString: 
        """
        None
        """
    def __iadd__(self,other : TCollection_ExtendedString) -> None: 
        """
        None
        """
    @overload
    def __init__(self,value : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,value : int) -> None: ...
    @overload
    def __init__(self,astring : str,isMultiByte : bool=False) -> None: ...
    @overload
    def __init__(self,astring : str) -> None: ...
    @overload
    def __init__(self,length : int,filler : str) -> None: ...
    @overload
    def __init__(self,astring : TCollection_ExtendedString) -> None: ...
    @overload
    def __init__(self,aChar : str) -> None: ...
    @overload
    def __init__(self,astring : TCollection_AsciiString,isMultiByte : bool=True) -> None: ...
    @overload
    def __init__(self,theStringUtf : str) -> None: ...
    pass
class TCollection_HAsciiString(OCP.Standard.Standard_Transient):
    """
    A variable-length sequence of ASCII characters (normal 8-bit character type). It provides editing operations with built-in memory management to make HAsciiString objects easier to use than ordinary character arrays. HAsciiString objects are handles to strings. - HAsciiString strings may be shared by several objects. - You may use an AsciiString object to get the actual string. Note: HAsciiString objects use an AsciiString string as a field.A variable-length sequence of ASCII characters (normal 8-bit character type). It provides editing operations with built-in memory management to make HAsciiString objects easier to use than ordinary character arrays. HAsciiString objects are handles to strings. - HAsciiString strings may be shared by several objects. - You may use an AsciiString object to get the actual string. Note: HAsciiString objects use an AsciiString string as a field.A variable-length sequence of ASCII characters (normal 8-bit character type). It provides editing operations with built-in memory management to make HAsciiString objects easier to use than ordinary character arrays. HAsciiString objects are handles to strings. - HAsciiString strings may be shared by several objects. - You may use an AsciiString object to get the actual string. Note: HAsciiString objects use an AsciiString string as a field.
    """
    @overload
    def AssignCat(self,other : TCollection_HAsciiString) -> None: 
        """
        Appends <other> to me.

        Appends <other> to me. Example: aString = aString + anotherString

        Appends <other> to me.

        Appends <other> to me. Example: aString = aString + anotherString
        """
    @overload
    def AssignCat(self,other : str) -> None: ...
    def Capitalize(self) -> None: 
        """
        Converts the first character into its corresponding upper-case character and the other characters into lowercase. Example: before me = "hellO " after me = "Hello "
        """
    @overload
    def Cat(self,other : str) -> TCollection_HAsciiString: 
        """
        Creates a new string by concatenation of this ASCII string and the other ASCII string. Example: aString = aString + anotherString aString = aString + "Dummy" aString contains "I say " aString = aString + "Hello " + "Dolly" gives "I say Hello Dolly" Warning: To catenate more than one CString, you must put a String before. So the following example is WRONG ! aString = "Hello " + "Dolly" THIS IS NOT ALLOWED This rule is applicable to AssignCat (operator +=) too.

        Creates a new string by concatenation of this ASCII string and the other ASCII string. Example: aString = aString + anotherString
        """
    @overload
    def Cat(self,other : TCollection_HAsciiString) -> TCollection_HAsciiString: ...
    def Center(self,Width : int,Filler : str) -> None: 
        """
        Modifies this ASCII string so that its length becomes equal to Width and the new characters are equal to Filler. New characters are added both at the beginning and at the end of this string. If Width is less than the length of this ASCII string, nothing happens. Example Handle(TCollection_HAsciiString) myAlphabet = new TCollection_HAsciiString ("abcdef"); myAlphabet->Center(9,' '); assert ( !strcmp( myAlphabet->ToCString(), " abcdef ") );
        """
    def ChangeAll(self,aChar : str,NewChar : str,CaseSensitive : bool=True) -> None: 
        """
        Replaces all characters equal to aChar by NewChar in this ASCII string. The substitution is case sensitive if CaseSensitive is true (default value). If you do not use the default case sensitive option, it does not matter whether aChar is upper-case or not. Example Handle(TCollection_HAsciiString) myMistake = new TCollection_HAsciiString ("Hather"); myMistake->ChangeAll('H','F'); assert ( !strcmp( myMistake->ToCString(), "Father") );
        """
    def Clear(self) -> None: 
        """
        Removes all characters contained in <me>. This produces an empty HAsciiString.
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
    def FirstLocationInSet(self,Set : TCollection_HAsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        Returns the index of the first character of <me> that is present in <Set>. The search begins to the index FromIndex and ends to the the index ToIndex. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range Example: before me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7 after me = "aabAcAa" returns 1
        """
    def FirstLocationNotInSet(self,Set : TCollection_HAsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        Returns the index of the first character of <me> that is not present in the set <Set>. The search begins to the index FromIndex and ends to the the index ToIndex in <me>. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7 after me = "aabAcAa" returns 3
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
    def Insert(self,where : int,what : str) -> None: 
        """
        Insert a Character at position <where>. Example: aString contains "hy not ?" aString.Insert(1,'W'); gives "Why not ?" aString contains "Wh" aString.Insert(3,'y'); gives "Why" aString contains "Way" aString.Insert(2,'h'); gives "Why"

        Insert a HAsciiString at position <where>.

        Insert a HAsciiString at position <where>.
        """
    @overload
    def Insert(self,where : int,what : TCollection_HAsciiString) -> None: ...
    def InsertAfter(self,Index : int,other : TCollection_HAsciiString) -> None: 
        """
        Inserts the other ASCII string a after a specific index in the string <me> Example: before me = "cde" , Index = 0 , other = "ab" after me = "abcde" , other = "ab"
        """
    def InsertBefore(self,Index : int,other : TCollection_HAsciiString) -> None: 
        """
        Inserts the other ASCII string a before a specific index in the string <me> Raises an exception if Index is out of bounds Example: before me = "cde" , Index = 1 , other = "ab" after me = "abcde" , other = "ab"
        """
    def IntegerValue(self) -> int: 
        """
        Converts a HAsciiString containing a numeric expression to an Integer. Example: "215" returns 215.
        """
    def IsAscii(self) -> bool: 
        """
        Returns True if the string contains only ASCII characters between ' ' and '~'. This means no control character and no extended ASCII code.
        """
    def IsDifferent(self,S : TCollection_HAsciiString) -> bool: 
        """
        Returns True if the string S not contains same characters than the string <me>.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if the string <me> contains zero character
        """
    def IsGreater(self,other : TCollection_HAsciiString) -> bool: 
        """
        Returns TRUE if <me> is 'ASCII' greater than <other>.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsIntegerValue(self) -> bool: 
        """
        Returns True if the string contains an integer value.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsLess(self,other : TCollection_HAsciiString) -> bool: 
        """
        Returns TRUE if <me> is 'ASCII' less than <other>.
        """
    def IsRealValue(self) -> bool: 
        """
        Returns True if the string contains a real value.
        """
    def IsSameState(self,other : TCollection_HAsciiString) -> bool: 
        """
        None
        """
    @overload
    def IsSameString(self,S : TCollection_HAsciiString,CaseSensitive : bool) -> bool: 
        """
        Returns True if the string S contains same characters than the string <me>.

        Returns True if the string S contains same characters than the string <me>.
        """
    @overload
    def IsSameString(self,S : TCollection_HAsciiString) -> bool: ...
    def LeftAdjust(self) -> None: 
        """
        Removes all space characters in the begining of the string
        """
    def LeftJustify(self,Width : int,Filler : str) -> None: 
        """
        Left justify. Length becomes equal to Width and the new characters are equal to Filler if Width < Length nothing happens Raises an exception if Width is less than zero Example: before me = "abcdef" , Width = 9 , Filler = ' ' after me = "abcdef "
        """
    def Length(self) -> int: 
        """
        Returns number of characters in <me>. This is the same functionality as 'strlen' in C.

        Returns number of characters in <me>. This is the same functionality as 'strlen' in C.
        """
    @overload
    def Location(self,other : TCollection_HAsciiString,FromIndex : int,ToIndex : int) -> int: 
        """
        returns an index in the string <me> of the first occurence of the string S in the string <me> from the starting index FromIndex to the ending index ToIndex returns zero if failure Raises an exception if FromIndex or ToIndex is out of range. Example: before me = "aabAaAa", S = "Aa", FromIndex = 1, ToIndex = 7 after me = "aabAaAa" returns 4

        Returns the index of the nth occurence of the character C in the string <me> from the starting index FromIndex to the ending index ToIndex. Returns zero if failure. Raises an exception if FromIndex or ToIndex is out of range Example: before me = "aabAa", N = 3, C = 'a', FromIndex = 1, ToIndex = 5 after me = "aabAa" returns 5
        """
    @overload
    def Location(self,N : int,C : str,FromIndex : int,ToIndex : int) -> int: ...
    def LowerCase(self) -> None: 
        """
        Converts <me> to its lower-case equivalent.
        """
    def Prepend(self,other : TCollection_HAsciiString) -> None: 
        """
        Inserts the other string at the begining of the string <me> Example: before me = "cde" , S = "ab" after me = "abcde" , S = "ab"
        """
    def Print(self,astream : io.BytesIO) -> None: 
        """
        Prints this string on the stream <astream>.
        """
    def RealValue(self) -> float: 
        """
        Converts a string containing a numeric expression to a Real. Example: "215" returns 215.0. "3.14159267" returns 3.14159267.
        """
    def Remove(self,where : int,ahowmany : int=1) -> None: 
        """
        Erases <ahowmany> characters from position <where>, <where> included. Example: aString contains "Hello" aString.Erase(2,2) erases 2 characters from position 1 This gives "Hlo".
        """
    @overload
    def RemoveAll(self,C : str,CaseSensitive : bool) -> None: 
        """
        Remove all the occurences of the character C in the string Example: before me = "HellLLo", C = 'L' , CaseSensitive = True after me = "Hello"

        Removes every <what> characters from <me>
        """
    @overload
    def RemoveAll(self,what : str) -> None: ...
    def RightAdjust(self) -> None: 
        """
        Removes all space characters at the end of the string.
        """
    def RightJustify(self,Width : int,Filler : str) -> None: 
        """
        Right justify. Length becomes equal to Width and the new characters are equal to Filler if Width < Length nothing happens Raises an exception if Width is less than zero Example: before me = "abcdef" , Width = 9 , Filler = ' ' after me = " abcdef"
        """
    @overload
    def Search(self,what : str) -> int: 
        """
        Searches a CString in <me> from the beginning and returns position of first item <what> matching. It returns -1 if not found. Example: aString contains "Sample single test" aString.Search("le") returns 5

        Searches a String in <me> from the beginning and returns position of first item <what> matching. it returns -1 if not found.
        """
    @overload
    def Search(self,what : TCollection_HAsciiString) -> int: ...
    @overload
    def SearchFromEnd(self,what : str) -> int: 
        """
        Searches a CString in a String from the end and returns position of first item <what> matching. It returns -1 if not found. Example: aString contains "Sample single test" aString.SearchFromEnd("le") returns 12

        Searches a HAsciiString in another HAsciiString from the end and returns position of first item <what> matching. It returns -1 if not found.
        """
    @overload
    def SearchFromEnd(self,what : TCollection_HAsciiString) -> int: ...
    @overload
    def SetValue(self,where : int,what : str) -> None: 
        """
        Replaces one character in the string at position <where>. If <where> is less than zero or greater than the length of <me> an exception is raised. Example: aString contains "Garbake" astring.Replace(6,'g') gives <me> = "Garbage"

        Replaces a part of <me> in the string at position <where>. If <where> is less than zero or greater than the length of <me> an exception is raised. Example: aString contains "Garbake" astring.Replace(6,'g') gives <me> = "Garbage"

        Replaces a part of <me> by another string.
        """
    @overload
    def SetValue(self,where : int,what : TCollection_HAsciiString) -> None: ...
    def Split(self,where : int) -> TCollection_HAsciiString: 
        """
        Splits a HAsciiString into two sub-strings. Example: aString contains "abcdefg" aString.Split(3) gives <me> = "abc" and returns "defg"
        """
    def String(self) -> TCollection_AsciiString: 
        """
        Returns the field myString.

        Returns the field myString.
        """
    def SubString(self,FromIndex : int,ToIndex : int) -> TCollection_HAsciiString: 
        """
        Creation of a sub-string of the string <me>. The sub-string starts to the index Fromindex and ends to the index ToIndex. Raises an exception if ToIndex or FromIndex is out of bounds Example: before me = "abcdefg", ToIndex=3, FromIndex=6 after me = "abcdefg" returns "cdef"
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCString(self) -> str: 
        """
        Returns pointer to string (char *) This is useful for some casual manipulations Because this "char *" is 'const', you can't modify its contents.

        Returns pointer to string (char *) This is useful for some casual manipulations Because this "char *" is 'const', you can't modify its contents.
        """
    def Token(self,separators : str=' \t',whichone : int=1) -> TCollection_HAsciiString: 
        """
        Extracts <whichone> token from <me>. By default, the <separators> is set to space and tabulation. By default, the token extracted is the first one (whichone = 1). <separators> contains all separators you need. If no token indexed by <whichone> is found, it returns an empty String. Example: aString contains "This is a message" aString.Token() returns "This" aString.Token(" ",4) returns "message" aString.Token(" ",2) returns "is" aString.Token(" ",9) returns "" Other separators than space character and tabulation are allowed aString contains "1234; test:message , value" aString.Token("; :,",4) returns "value" aString.Token("; :,",2) returns "test"
        """
    def Trunc(self,ahowmany : int) -> None: 
        """
        Truncates <me> to <ahowmany> characters. Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel"
        """
    def UpperCase(self) -> None: 
        """
        Converts <me> to its upper-case equivalent.
        """
    def UsefullLength(self) -> int: 
        """
        Length of the string ignoring all spaces (' ') and the control character at the end.
        """
    def Value(self,where : int) -> str: 
        """
        Returns character at position <where> in <me>. If <where> is less than zero or greater than the lenght of <me>, an exception is raised. Example: aString contains "Hello" aString.Value(2) returns 'e'
        """
    @overload
    def __init__(self,aChar : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,value : int) -> None: ...
    @overload
    def __init__(self,message : str) -> None: ...
    @overload
    def __init__(self,aString : TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,aString : TCollection_HAsciiString) -> None: ...
    @overload
    def __init__(self,aString : TCollection_HExtendedString,replaceNonAscii : str) -> None: ...
    @overload
    def __init__(self,length : int,filler : str) -> None: ...
    @overload
    def __init__(self,value : float) -> None: ...
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
class TCollection_HExtendedString(OCP.Standard.Standard_Transient):
    """
    A variable-length sequence of "extended" (UNICODE) characters (16-bit character type). It provides editing operations with built-in memory management to make ExtendedString objects easier to use than ordinary extended character arrays. HExtendedString objects are handles to strings. - HExtendedString strings may be shared by several objects. - You may use an ExtendedString object to get the actual string. Note: HExtendedString objects use an ExtendedString string as a field.A variable-length sequence of "extended" (UNICODE) characters (16-bit character type). It provides editing operations with built-in memory management to make ExtendedString objects easier to use than ordinary extended character arrays. HExtendedString objects are handles to strings. - HExtendedString strings may be shared by several objects. - You may use an ExtendedString object to get the actual string. Note: HExtendedString objects use an ExtendedString string as a field.A variable-length sequence of "extended" (UNICODE) characters (16-bit character type). It provides editing operations with built-in memory management to make ExtendedString objects easier to use than ordinary extended character arrays. HExtendedString objects are handles to strings. - HExtendedString strings may be shared by several objects. - You may use an ExtendedString object to get the actual string. Note: HExtendedString objects use an ExtendedString string as a field.
    """
    def AssignCat(self,other : TCollection_HExtendedString) -> None: 
        """
        Appends <other> to me.
        """
    def Cat(self,other : TCollection_HExtendedString) -> TCollection_HExtendedString: 
        """
        Returns a string appending <other> to me.
        """
    def ChangeAll(self,aChar : str,NewChar : str) -> None: 
        """
        Substitutes all the characters equal to aChar by NewChar in the string <me>.
        """
    def Clear(self) -> None: 
        """
        Removes all characters contained in <me>. This produces an empty ExtendedString.
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
    def Insert(self,where : int,what : TCollection_HExtendedString) -> None: 
        """
        Insert a ExtCharacter at position <where>. Example: aString contains "hy not ?" aString.Insert(1,'W'); gives "Why not ?" aString contains "Wh" aString.Insert(3,'y'); gives "Why" aString contains "Way" aString.Insert(2,'h'); gives "Why"

        Insert a HExtendedString at position <where>.
        """
    @overload
    def Insert(self,where : int,what : str) -> None: ...
    def IsAscii(self) -> bool: 
        """
        Returns True if the string contains only "Ascii Range" characters
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if the string <me> contains zero character
        """
    def IsGreater(self,other : TCollection_HExtendedString) -> bool: 
        """
        Returns TRUE if <me> is greater than <other>.
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
    def IsLess(self,other : TCollection_HExtendedString) -> bool: 
        """
        Returns TRUE if <me> is less than <other>.
        """
    def IsSameState(self,other : TCollection_HExtendedString) -> bool: 
        """
        None
        """
    def Length(self) -> int: 
        """
        Returns number of characters in <me>. This is the same functionality as 'strlen' in C.
        """
    def Print(self,astream : io.BytesIO) -> None: 
        """
        Displays <me> .
        """
    def Remove(self,where : int,ahowmany : int=1) -> None: 
        """
        Erases <ahowmany> characters from position <where>, <where> included. Example: aString contains "Hello" aString.Erase(2,2) erases 2 characters from position 1 This gives "Hlo".
        """
    def RemoveAll(self,what : str) -> None: 
        """
        Removes every <what> characters from <me>.
        """
    def Search(self,what : TCollection_HExtendedString) -> int: 
        """
        Searches a String in <me> from the beginning and returns position of first item <what> matching. It returns -1 if not found.
        """
    def SearchFromEnd(self,what : TCollection_HExtendedString) -> int: 
        """
        Searches a ExtendedString in another ExtendedString from the end and returns position of first item <what> matching. It returns -1 if not found.
        """
    @overload
    def SetValue(self,where : int,what : TCollection_HExtendedString) -> None: 
        """
        Replaces one character in the string at position <where>. If <where> is less than zero or greater than the length of <me> an exception is raised. Example: aString contains "Garbake" astring.Replace(6,'g') gives <me> = "Garbage"

        Replaces a part of <me> by another string.
        """
    @overload
    def SetValue(self,where : int,what : str) -> None: ...
    def Split(self,where : int) -> TCollection_HExtendedString: 
        """
        Splits a ExtendedString into two sub-strings. Example: aString contains "abcdefg" aString.Split(3) gives <me> = "abc" and returns "defg"
        """
    def String(self) -> TCollection_ExtendedString: 
        """
        Returns the field myString
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToExtString(self) -> str: 
        """
        Returns pointer to ExtString
        """
    def Token(self,separators : str,whichone : int=1) -> TCollection_HExtendedString: 
        """
        Extracts <whichone> token from <me>. By default, the <separators> is set to space and tabulation. By default, the token extracted is the first one (whichone = 1). <separators> contains all separators you need. If no token indexed by <whichone> is found, it returns an empty String. Example: aString contains "This is a message" aString.Token() returns "This" aString.Token(" ",4) returns "message" aString.Token(" ",2) returns "is" aString.Token(" ",9) returns "" Other separators than space character and tabulation are allowed aString contains "1234; test:message , value" aString.Token("; :,",4) returns "value" aString.Token("; :,",2) returns "test"
        """
    def Trunc(self,ahowmany : int) -> None: 
        """
        Truncates <me> to <ahowmany> characters. Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel"
        """
    def Value(self,where : int) -> str: 
        """
        Returns ExtCharacter at position <where> in <me>. If <where> is less than zero or greater than the length of <me>, an exception is raised. Example: aString contains "Hello" aString.Value(2) returns 'e'
        """
    @overload
    def __init__(self,aString : TCollection_HAsciiString) -> None: ...
    @overload
    def __init__(self,length : int,filler : str) -> None: ...
    @overload
    def __init__(self,aString : TCollection_HExtendedString) -> None: ...
    @overload
    def __init__(self,aChar : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,aString : TCollection_ExtendedString) -> None: ...
    @overload
    def __init__(self,message : str) -> None: ...
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
class TCollection_MapNode(OCP.Standard.Standard_Transient):
    """
    Basic class root of all the Maps.Basic class root of all the Maps.Basic class root of all the Maps.
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
    def Next(self) -> TCollection_MapNode: 
        """
        None

        None
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
class TCollection_SeqNode(OCP.Standard.Standard_Transient):
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
    def Next(self) -> TCollection_SeqNode: 
        """
        None

        None
        """
    def Previous(self) -> TCollection_SeqNode: 
        """
        None

        None
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
class TCollection_Side():
    """
    None

    Members:

      TCollection_Left

      TCollection_Right
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    TCollection_Left: OCP.TCollection.TCollection_Side # value = <TCollection_Side.TCollection_Left: 0>
    TCollection_Right: OCP.TCollection.TCollection_Side # value = <TCollection_Side.TCollection_Right: 1>
    __entries: dict # value = {'TCollection_Left': (<TCollection_Side.TCollection_Left: 0>, None), 'TCollection_Right': (<TCollection_Side.TCollection_Right: 1>, None)}
    __members__: dict # value = {'TCollection_Left': <TCollection_Side.TCollection_Left: 0>, 'TCollection_Right': <TCollection_Side.TCollection_Right: 1>}
    pass
@overload
def HashCode(theExtendedString : TCollection_ExtendedString,theUpperBound : int) -> int:
    """
    Computes a hash code for the given ASCII string, in the range [1, theUpperBound]

    Computes a hash code for the given extended string, in the range [1, theUpperBound]
    """
@overload
def HashCode(theAsciiString : TCollection_AsciiString,theUpperBound : int) -> int:
    pass
def IsEqual(string1 : TCollection_AsciiString,string2 : TCollection_AsciiString) -> bool:
    """
    None
    """
TCollection_Left: OCP.TCollection.TCollection_Side # value = <TCollection_Side.TCollection_Left: 0>
TCollection_Right: OCP.TCollection.TCollection_Side # value = <TCollection_Side.TCollection_Right: 1>
