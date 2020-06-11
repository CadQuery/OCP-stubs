import OCP.Poly
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Standard
import OCP.gp
import OCP.TColgp
import OCP.TColStd
import OCP.TShort
__all__  = [
"Poly_Array1OfTriangle",
"Poly_CoherentLink",
"Poly_CoherentNode",
"Poly_CoherentTriangle",
"Poly_CoherentTriangulation",
"Poly_Connect",
"Poly_HArray1OfTriangle",
"Poly_ListOfTriangulation",
"Poly_MakeLoops2D",
"Poly_MakeLoops3D",
"Poly_Polygon2D",
"Poly_Polygon3D",
"Poly_PolygonOnTriangulation",
"Poly_Triangle",
"Poly_Triangulation",
"HashCode",
"IsEqual"
]
class Poly_Array1OfTriangle():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Poly_Array1OfTriangle) -> Poly_Array1OfTriangle: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Poly_Triangle: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Poly_Triangle: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Poly_Triangle: 
        """
        Variable value access
        """
    def First(self) -> Poly_Triangle: 
        """
        Returns first element
        """
    def Init(self,theValue : Poly_Triangle) -> None: 
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
    def Last(self) -> Poly_Triangle: 
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
    def Move(self,theOther : Poly_Array1OfTriangle) -> Poly_Array1OfTriangle: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Poly_Triangle) -> None: 
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
    def Value(self,theIndex : int) -> Poly_Triangle: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self,theBegin : Poly_Triangle,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Poly_CoherentLink():
    """
    Link between two mesh nodes that is created by existing triangle(s). Keeps reference to the opposite node of each incident triangle. The referred node with index "0" is always on the left side of the link, the one with the index "1" is always on the right side. It is possible to find both incident triangles using the method Poly_CoherentTriangulation::FindTriangle(). Any Link can store an arbitrary pointer that is called Attribute.
    """
    def GetAttribute(self) -> capsule: 
        """
        Query the attribute of the Link.
        """
    def IsEmpty(self) -> bool: 
        """
        Query the status of the link - if it is an invalid one. An invalid link has Node members equal to -1.
        """
    def Node(self,ind : int) -> int: 
        """
        Return the node index in the current triangulation.
        """
    def Nullify(self) -> None: 
        """
        Invalidate this Link.
        """
    def OppositeNode(self,ind : int) -> int: 
        """
        Return the opposite node (belonging to the left or right incident triangle) index in the current triangulation.
        """
    def SetAttribute(self,theAtt : capsule) -> None: 
        """
        Set the attribute of the Link.
        """
    @overload
    def __init__(self,iNode0 : int,iNode1 : int) -> None: ...
    @overload
    def __init__(self,theTri : Poly_CoherentTriangle,iSide : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Poly_CoherentNode(OCP.gp.gp_XYZ):
    """
    Node of coherent triangulation. Contains: Coordinates of a 3D point defining the node location 2D point coordinates List of triangles that use this Node Integer index, normally the index of the node in the original triangulation
    """
    def Add(self,Other : OCP.gp.gp_XYZ) -> None: 
        """
        <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y() <me>.Z() = <me>.Z() + Other.Z()

        <me>.X() = <me>.X() + Other.X() <me>.Y() = <me>.Y() + Other.Y() <me>.Z() = <me>.Z() + Other.Z()
        """
    def AddTriangle(self,theTri : Poly_CoherentTriangle,theA : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Connect a triangle to this Node.
        """
    def Added(self,Other : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y() new.Z() = <me>.Z() + Other.Z()

        new.X() = <me>.X() + Other.X() new.Y() = <me>.Y() + Other.Y() new.Z() = <me>.Z() + Other.Z()
        """
    def ChangeCoord(self,theIndex : int) -> float: 
        """
        None

        None
        """
    def ChangeData(self) -> float: 
        """
        Returns a ptr to coordinates location. Is useful for algorithms, but DOES NOT PERFORM ANY CHECKS!
        """
    def Clear(self,arg1 : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Reset the Node to void.
        """
    @overload
    def Coord(self,i : int) -> float: 
        """
        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned

        returns the coordinate of range Index : Index = 1 => X is returned Index = 2 => Y is returned Index = 3 => Z is returned

        None

        None
        """
    @overload
    def Coord(self) -> Tuple[float, float, float]: ...
    @overload
    def Coord(self,Index : int) -> float: ...
    def Cross(self,Right : OCP.gp.gp_XYZ) -> None: 
        """
        <me>.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() <me>.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() <me>.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()

        <me>.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() <me>.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() <me>.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()
        """
    def CrossCross(self,Coord1 : OCP.gp.gp_XYZ,Coord2 : OCP.gp.gp_XYZ) -> None: 
        """
        Triple vector product Computes <me> = <me>.Cross(Coord1.Cross(Coord2))

        Triple vector product Computes <me> = <me>.Cross(Coord1.Cross(Coord2))
        """
    def CrossCrossed(self,Coord1 : OCP.gp.gp_XYZ,Coord2 : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        Triple vector product computes New = <me>.Cross(Coord1.Cross(Coord2))

        Triple vector product computes New = <me>.Cross(Coord1.Cross(Coord2))
        """
    def CrossMagnitude(self,Right : OCP.gp.gp_XYZ) -> float: 
        """
        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||

        Computes the magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||
        """
    def CrossSquareMagnitude(self,Right : OCP.gp.gp_XYZ) -> float: 
        """
        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2

        Computes the square magnitude of the cross product between <me> and Right. Returns || <me> ^ Right ||**2
        """
    def Crossed(self,Right : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        new.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() new.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() new.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()

        new.X() = <me>.Y() * Other.Z() - <me>.Z() * Other.Y() new.Y() = <me>.Z() * Other.X() - <me>.X() * Other.Z() new.Z() = <me>.X() * Other.Y() - <me>.Y() * Other.X()
        """
    def Divide(self,Scalar : float) -> None: 
        """
        divides <me> by a real.

        divides <me> by a real.
        """
    def Divided(self,Scalar : float) -> OCP.gp.gp_XYZ: 
        """
        divides <me> by a real.

        divides <me> by a real.
        """
    def Dot(self,Other : OCP.gp.gp_XYZ) -> float: 
        """
        computes the scalar product between <me> and Other

        computes the scalar product between <me> and Other
        """
    def DotCross(self,Coord1 : OCP.gp.gp_XYZ,Coord2 : OCP.gp.gp_XYZ) -> float: 
        """
        computes the triple scalar product

        computes the triple scalar product
        """
    def Dump(self,theStream : Any) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetData(self) -> float: 
        """
        Returns a const ptr to coordinates location. Is useful for algorithms, but DOES NOT PERFORM ANY CHECKS!
        """
    def GetIndex(self) -> int: 
        """
        Get the value of node Index.
        """
    def GetNormal(self) -> OCP.gp.gp_XYZ: 
        """
        Get the stored normal in the node.
        """
    def GetU(self) -> float: 
        """
        Get U coordinate of the Node.
        """
    def GetV(self) -> float: 
        """
        Get V coordinate of the Node.
        """
    def HasNormal(self) -> bool: 
        """
        Query if the Node contains a normal vector.
        """
    def IsEqual(self,Other : OCP.gp.gp_XYZ,Tolerance : float) -> bool: 
        """
        Returns True if he coordinates of this XYZ object are equal to the respective coordinates Other, within the specified tolerance Tolerance. I.e.: abs(<me>.X() - Other.X()) <= Tolerance and abs(<me>.Y() - Other.Y()) <= Tolerance and abs(<me>.Z() - Other.Z()) <= Tolerance.
        """
    def IsFreeNode(self) -> bool: 
        """
        Check if this is a free node, i.e., a node without a single incident triangle.
        """
    def Modulus(self) -> float: 
        """
        computes Sqrt (X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ object.

        computes Sqrt (X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ object.
        """
    @overload
    def Multiplied(self,Scalar : float) -> OCP.gp.gp_XYZ: 
        """
        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar; New.Z() = <me>.Z() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y(); new.Z() = <me>.Z() * Other.Z();

        New = Matrix * <me>

        New.X() = <me>.X() * Scalar; New.Y() = <me>.Y() * Scalar; New.Z() = <me>.Z() * Scalar;

        new.X() = <me>.X() * Other.X(); new.Y() = <me>.Y() * Other.Y(); new.Z() = <me>.Z() * Other.Z();

        New = Matrix * <me>
        """
    @overload
    def Multiplied(self,Other : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    @overload
    def Multiplied(self,Matrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: ...
    @overload
    def Multiply(self,Scalar : float) -> None: 
        """
        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar; <me>.Z() = <me>.Z() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y(); <me>.Z() = <me>.Z() * Other.Z();

        <me> = Matrix * <me>

        <me>.X() = <me>.X() * Scalar; <me>.Y() = <me>.Y() * Scalar; <me>.Z() = <me>.Z() * Scalar;

        <me>.X() = <me>.X() * Other.X(); <me>.Y() = <me>.Y() * Other.Y(); <me>.Z() = <me>.Z() * Other.Z();

        <me> = Matrix * <me>
        """
    @overload
    def Multiply(self,Other : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def Multiply(self,Matrix : OCP.gp.gp_Mat) -> None: ...
    def Normalize(self) -> None: 
        """
        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() <me>.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp

        <me>.X() = <me>.X()/ <me>.Modulus() <me>.Y() = <me>.Y()/ <me>.Modulus() <me>.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp
        """
    def Normalized(self) -> OCP.gp.gp_XYZ: 
        """
        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() New.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp

        New.X() = <me>.X()/ <me>.Modulus() New.Y() = <me>.Y()/ <me>.Modulus() New.Z() = <me>.Z()/ <me>.Modulus() Raised if <me>.Modulus() <= Resolution from gp
        """
    def RemoveTriangle(self,theTri : Poly_CoherentTriangle,theA : OCP.NCollection.NCollection_BaseAllocator) -> bool: 
        """
        Disconnect a triangle from this Node.
        """
    def Reverse(self) -> None: 
        """
        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y() <me>.Z() = -<me>.Z()

        <me>.X() = -<me>.X() <me>.Y() = -<me>.Y() <me>.Z() = -<me>.Z()
        """
    def Reversed(self) -> OCP.gp.gp_XYZ: 
        """
        New.X() = -<me>.X() New.Y() = -<me>.Y() New.Z() = -<me>.Z()

        New.X() = -<me>.X() New.Y() = -<me>.Y() New.Z() = -<me>.Z()
        """
    @overload
    def SetCoord(self,X : float,Y : float,Z : float) -> None: 
        """
        For this XYZ object, assigns the values X, Y and Z to its three coordinates

        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raises OutOfRange if Index != {1, 2, 3}.

        For this XYZ object, assigns the values X, Y and Z to its three coordinates

        modifies the coordinate of range Index Index = 1 => X is modified Index = 2 => Y is modified Index = 3 => Z is modified Raises OutOfRange if Index != {1, 2, 3}.
        """
    @overload
    def SetCoord(self,Index : int,Xi : float) -> None: ...
    @overload
    def SetCoord(self,i : int,X : float) -> None: ...
    def SetIndex(self,theIndex : int) -> None: 
        """
        Set the value of node Index.
        """
    @overload
    def SetLinearForm(self,XYZ1 : OCP.gp.gp_XYZ,XYZ2 : OCP.gp.gp_XYZ) -> None: 
        """
        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3 + XYZ4

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + XYZ2

        <me> is set to the following linear form : XYZ1 + XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + XYZ2

        <me> is set to the following linear form : XYZ1 + XYZ2

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + XYZ3

        <me> is set to the following linear form : A1 * XYZ1 + A2 * XYZ2 + A3 * XYZ3 + XYZ4
        """
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : OCP.gp.gp_XYZ,A2 : float,XYZ2 : OCP.gp.gp_XYZ,A3 : float,XYZ3 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : OCP.gp.gp_XYZ,A2 : float,XYZ2 : OCP.gp.gp_XYZ,XYZ3 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,Left : OCP.gp.gp_XYZ,Right : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : OCP.gp.gp_XYZ,A2 : float,XYZ2 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : OCP.gp.gp_XYZ,XYZ2 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : OCP.gp.gp_XYZ,R : float,Right : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,L : float,Left : OCP.gp.gp_XYZ,Right : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,A1 : float,XYZ1 : OCP.gp.gp_XYZ,A2 : float,XYZ2 : OCP.gp.gp_XYZ,A3 : float,XYZ3 : OCP.gp.gp_XYZ,XYZ4 : OCP.gp.gp_XYZ) -> None: ...
    def SetNormal(self,theVector : OCP.gp.gp_XYZ) -> None: 
        """
        Define the normal vector in the Node.
        """
    def SetUV(self,theU : float,theV : float) -> None: 
        """
        Set the UV coordinates of the Node.
        """
    def SetX(self,X : float) -> None: 
        """
        Assigns the given value to the X coordinate

        Assigns the given value to the X coordinate
        """
    def SetY(self,Y : float) -> None: 
        """
        Assigns the given value to the Y coordinate

        Assigns the given value to the Y coordinate
        """
    def SetZ(self,Z : float) -> None: 
        """
        Assigns the given value to the Z coordinate

        Assigns the given value to the Z coordinate
        """
    def SquareModulus(self) -> float: 
        """
        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.

        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.
        """
    def Subtract(self,Right : OCP.gp.gp_XYZ) -> None: 
        """
        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y() <me>.Z() = <me>.Z() - Other.Z()

        <me>.X() = <me>.X() - Other.X() <me>.Y() = <me>.Y() - Other.Y() <me>.Z() = <me>.Z() - Other.Z()
        """
    def Subtracted(self,Right : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y() new.Z() = <me>.Z() - Other.Z()

        new.X() = <me>.X() - Other.X() new.Y() = <me>.Y() - Other.Y() new.Z() = <me>.Z() - Other.Z()
        """
    def TriangleIterator(self) -> Any: 
        """
        Create an iterator of incident triangles.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate

        Returns the X coordinate
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate

        Returns the Y coordinate
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate

        Returns the Z coordinate
        """
    def __add__(self,Other : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def __iadd__(self,Other : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,Matrix : OCP.gp.gp_Mat) -> None: 
        """
        None

        None

        None
        """
    @overload
    def __imul__(self,Other : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __imul__(self,Scalar : float) -> None: ...
    @overload
    def __init__(self,thePnt : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __ipow__(self,Right : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def __isub__(self,Right : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def __itruediv__(self,Scalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,Other : OCP.gp.gp_XYZ) -> float: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,Matrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: ...
    @overload
    def __mul__(self,Scalar : float) -> OCP.gp.gp_XYZ: ...
    def __pow__(self,Right : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    @overload
    def __rmul__(self,Other : OCP.gp.gp_XYZ) -> float: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,Matrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: ...
    @overload
    def __rmul__(self,Scalar : float) -> OCP.gp.gp_XYZ: ...
    def __sub__(self,Right : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def __truediv__(self,Scalar : float) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    pass
class Poly_CoherentTriangle():
    """
    Data class used in Poly_CoherentTriangultion. Implements a triangle with references to its neighbours.
    """
    def FindConnection(self,arg1 : Poly_CoherentTriangle) -> int: 
        """
        Retuns the index of the connection with the given triangle, or -1 if not found.
        """
    def GetConnectedNode(self,iConn : int) -> int: 
        """
        Query the connected node on the given side. Returns -1 if there is no connection on the specified side.
        """
    def GetConnectedTri(self,iConn : int) -> Poly_CoherentTriangle: 
        """
        Query the connected triangle on the given side. Returns NULL if there is no connection on the specified side.
        """
    def GetLink(self,iLink : int) -> Poly_CoherentLink: 
        """
        Query the Link associate with the given side of the Triangle. May return NULL if there are no links in the triangulation.
        """
    def IsEmpty(self) -> bool: 
        """
        Query if this is a valid triangle.
        """
    def NConnections(self) -> int: 
        """
        Query the number of connected triangles.
        """
    def Node(self,ind : int) -> int: 
        """
        Query the node index in the position given by the parameter 'ind'
        """
    @overload
    def RemoveConnection(self,theTri : Poly_CoherentTriangle) -> bool: 
        """
        Remove the connection with the given index.

        Remove the connection with the given Triangle.
        """
    @overload
    def RemoveConnection(self,iConn : int) -> None: ...
    @overload
    def SetConnection(self,theTri : Poly_CoherentTriangle) -> bool: 
        """
        Create connection with another triangle theTri. This method creates both connections: in this triangle and in theTri. You do not need to call the same method on triangle theTr.

        Create connection with another triangle theTri. This method creates both connections: in this triangle and in theTri. This method is slower than the previous one, because it makes analysis what sides of both triangles are connected.
        """
    @overload
    def SetConnection(self,iConn : int,theTr : Poly_CoherentTriangle) -> bool: ...
    @overload
    def __init__(self,iNode0 : int,iNode1 : int,iNode2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Poly_CoherentTriangulation(OCP.Standard.Standard_Transient):
    """
    Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.
    """
    def AddLink(self,theTri : Poly_CoherentTriangle,theConn : int) -> Poly_CoherentLink: 
        """
        Add a single link to triangulation, based on a triangle and its side index. This method does not check for coincidence with already present links.
        """
    def AddTriangle(self,iNode0 : int,iNode1 : int,iNode2 : int) -> Poly_CoherentTriangle: 
        """
        Add a triangle to the triangulation.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Query the allocator of elements, this allocator can be used for other objects
        """
    def ChangeNode(self,i : int) -> Poly_CoherentNode: 
        """
        Get the node at the given index 'i'.
        """
    def ClearLinks(self) -> None: 
        """
        Clear all Links data from the Triangulation data.
        """
    def Clone(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> Poly_CoherentTriangulation: 
        """
        Create a copy of this Triangulation, using the given allocator.
        """
    def ComputeLinks(self) -> int: 
        """
        (Re)Calculate all links in this Triangulation.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Deflection(self) -> float: 
        """
        Query the Deflection parameter (default value 0. -- if never initialized)
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,arg1 : Any) -> None: 
        """
        Debugging output.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetFreeNodes(self,lstNodes : OCP.TColStd.TColStd_ListOfInteger) -> bool: 
        """
        Create a list of free nodes. These nodes may appear as a result of any custom mesh decimation or RemoveDegenerated() call. This analysis is necessary if you support additional data structures based on the triangulation (e.g., edges on the surface boundary).
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTriangulation(self) -> Poly_Triangulation: 
        """
        Create an instance of Poly_Triangulation from this object.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MaxNode(self) -> int: 
        """
        Query the index of the last node in the triangulation
        """
    def MaxTriangle(self) -> int: 
        """
        Query the index of the last triangle in the triangulation
        """
    def NLinks(self) -> int: 
        """
        Query the total number of active Links.
        """
    def NNodes(self) -> int: 
        """
        Query the total number of active nodes (i.e. nodes used by 1 or more triangles)
        """
    def NTriangles(self) -> int: 
        """
        Query the total number of active triangles (i.e. triangles that refer nodes, non-empty ones)
        """
    def Node(self,i : int) -> Poly_CoherentNode: 
        """
        Get the node at the given index 'i'.
        """
    def RemoveLink(self,theLink : Poly_CoherentLink) -> None: 
        """
        Removal of a single link from the triangulation.
        """
    def RemoveTriangle(self,theTr : Poly_CoherentTriangle) -> bool: 
        """
        Removal of a single triangle from the triangulation.
        """
    def ReplaceNodes(self,theTriangle : Poly_CoherentTriangle,iNode0 : int,iNode1 : int,iNode2 : int) -> bool: 
        """
        Replace nodes in the given triangle.
        """
    def SetDeflection(self,theDefl : float) -> None: 
        """
        Set the Deflection value as the parameter of the given triangulation.
        """
    def SetNode(self,thePnt : OCP.gp.gp_XYZ,iN : int=-1) -> int: 
        """
        Initialize a node
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangle(self,i : int) -> Poly_CoherentTriangle: 
        """
        Get the triangle at the given index 'i'.
        """
    @overload
    def __init__(self,theTriangulation : Poly_Triangulation,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
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
class Poly_Connect():
    """
    Provides an algorithm to explore, inside a triangulation, the adjacency data for a node or a triangle. Adjacency data for a node consists of triangles which contain the node. Adjacency data for a triangle consists of: - the 3 adjacent triangles which share an edge of the triangle, - and the 3 nodes which are the other nodes of these adjacent triangles. Example Inside a triangulation, a triangle T has nodes n1, n2 and n3. It has adjacent triangles AT1, AT2 and AT3 where: - AT1 shares the nodes n2 and n3, - AT2 shares the nodes n3 and n1, - AT3 shares the nodes n1 and n2. It has adjacent nodes an1, an2 and an3 where: - an1 is the third node of AT1, - an2 is the third node of AT2, - an3 is the third node of AT3. So triangle AT1 is composed of nodes n2, n3 and an1. There are two ways of using this algorithm. - From a given node you can look for one triangle that passes through the node, then look for the triangles adjacent to this triangle, then the adjacent nodes. You can thus explore the triangulation step by step (functions Triangle, Triangles and Nodes). - From a given node you can look for all the triangles that pass through the node (iteration method, using the functions Initialize, More, Next and Value). A Connect object can be seen as a tool which analyzes a triangulation and translates it into a series of triangles. By doing this, it provides an interface with other tools and applications working on basic triangles, and which do not work directly with a Poly_Triangulation.
    """
    def Initialize(self,N : int) -> None: 
        """
        Initializes an iterator to search for all the triangles containing the node referenced at index N in the nodes table, for the triangulation analyzed by this tool. The iterator is managed by the following functions: - More, which checks if there are still elements in the iterator - Next, which positions the iterator on the next element - Value, which returns the current element. The use of such an iterator provides direct access to the triangles around a particular node, i.e. it avoids iterating on all the component triangles of a triangulation. Example Poly_Connect C(Tr); for (C.Initialize(n1);C.More();C.Next()) { t = C.Value(); }
        """
    def Load(self,theTriangulation : Poly_Triangulation) -> None: 
        """
        Initialize the algorithm to explore the adjacency data of nodes or triangles for the triangulation theTriangulation.
        """
    def More(self) -> bool: 
        """
        Returns true if there is another element in the iterator defined with the function Initialize (i.e. if there is another triangle containing the given node).
        """
    def Next(self) -> None: 
        """
        Advances the iterator defined with the function Initialize to access the next triangle. Note: There is no action if the iterator is empty (i.e. if the function More returns false).-
        """
    def Nodes(self,T : int) -> Tuple[int, int, int]: 
        """
        Returns, in n1, n2 and n3, the indices of the 3 nodes adjacent to the triangle referenced at index T in the triangles table specific to the triangulation analyzed by this tool. Warning Null indices are returned when there are fewer than 3 adjacent nodes.
        """
    def Triangle(self,N : int) -> int: 
        """
        Returns the index of a triangle containing the node at index N in the nodes table specific to the triangulation analyzed by this tool
        """
    def Triangles(self,T : int) -> Tuple[int, int, int]: 
        """
        Returns in t1, t2 and t3, the indices of the 3 triangles adjacent to the triangle at index T in the triangles table specific to the triangulation analyzed by this tool. Warning Null indices are returned when there are fewer than 3 adjacent triangles.
        """
    def Triangulation(self) -> Poly_Triangulation: 
        """
        Returns the triangulation analyzed by this tool.
        """
    def Value(self) -> int: 
        """
        Returns the index of the current triangle to which the iterator, defined with the function Initialize, points. This is an index in the triangles table specific to the triangulation analyzed by this tool
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theTriangulation : Poly_Triangulation) -> None: ...
    pass
class Poly_HArray1OfTriangle(Poly_Array1OfTriangle, OCP.Standard.Standard_Transient):
    def Array1(self) -> Poly_Array1OfTriangle: 
        """
        None
        """
    def Assign(self,theOther : Poly_Array1OfTriangle) -> Poly_Array1OfTriangle: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Poly_Array1OfTriangle: 
        """
        None
        """
    def ChangeFirst(self) -> Poly_Triangle: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Poly_Triangle: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Poly_Triangle: 
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
    def First(self) -> Poly_Triangle: 
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
    def Init(self,theValue : Poly_Triangle) -> None: 
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> Poly_Triangle: 
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
    def Move(self,theOther : Poly_Array1OfTriangle) -> Poly_Array1OfTriangle: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Poly_Triangle) -> None: 
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
    def Value(self,theIndex : int) -> Poly_Triangle: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Poly_Triangle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class Poly_ListOfTriangulation(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : Poly_ListOfTriangulation) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : Poly_Triangulation) -> Poly_Triangulation: ...
    @overload
    def Append(self,theItem : Poly_Triangulation,theIter : Any) -> None: ...
    def Assign(self,theOther : Poly_ListOfTriangulation) -> Poly_ListOfTriangulation: 
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
    def First(self) -> Poly_Triangulation: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : Poly_Triangulation,theIter : Any) -> Poly_Triangulation: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : Poly_ListOfTriangulation,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theOther : Poly_ListOfTriangulation,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : Poly_Triangulation,theIter : Any) -> Poly_Triangulation: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> Poly_Triangulation: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : Poly_ListOfTriangulation) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : Poly_Triangulation) -> Poly_Triangulation: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Poly_ListOfTriangulation) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Poly_MakeLoops2D():
    """
    None
    """
    def __init__(self,theLeftWay : bool,theHelper : Any,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class Poly_MakeLoops3D():
    """
    None
    """
    def __init__(self,theHelper : Any,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class Poly_Polygon2D(OCP.Standard.Standard_Transient):
    """
    Provides a polygon in 2D space (for example, in the parametric space of a surface). It is generally an approximate representation of a curve. A Polygon2D is defined by a table of nodes. Each node is a 2D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes.Provides a polygon in 2D space (for example, in the parametric space of a surface). It is generally an approximate representation of a curve. A Polygon2D is defined by a table of nodes. Each node is a 2D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes.Provides a polygon in 2D space (for example, in the parametric space of a surface). It is generally an approximate representation of a curve. A Polygon2D is defined by a table of nodes. Each node is a 2D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self) -> float: 
        """
        Returns the deflection of this polygon. Deflection is used in cases where the polygon is an approximate representation of a curve. Deflection represents the maximum distance permitted between any point on the curve and the corresponding point on the polygon. By default the deflection value is equal to 0. An algorithm using this 2D polygon with a deflection value equal to 0 considers that it is working with a true polygon and not with an approximate representation of a curve. The Deflection function is used to modify the deflection value of this polygon. The deflection value can be used by any algorithm working with 2D polygons. For example: - An algorithm may use a unique deflection value for all its polygons. In this case it is not necessary to use the Deflection function. - Or an algorithm may want to attach a different deflection to each polygon. In this case, the Deflection function is used to set a value on each polygon, and later to fetch the value.

        Sets the deflection of this polygon to D
        """
    @overload
    def Deflection(self,D : float) -> None: ...
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes in this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle, the function NbNodes returns 4.

        Returns the number of nodes in this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle, the function NbNodes returns 4.
        """
    def Nodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of nodes for this polygon.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt2d) -> None: ...
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
class Poly_Polygon3D(OCP.Standard.Standard_Transient):
    """
    This class Provides a polygon in 3D space. It is generally an approximate representation of a curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.This class Provides a polygon in 3D space. It is generally an approximate representation of a curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.This class Provides a polygon in 3D space. It is generally an approximate representation of a curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.
    """
    def ChangeParameters(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns the table of the parameters associated with each node in this polygon. ChangeParameters function returnes the array as shared. Therefore if the table is selected by reference you can, by simply modifying it, directly modify the data structure of this polygon.
        """
    def Copy(self) -> Poly_Polygon3D: 
        """
        Creates a copy of current polygon
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self,D : float) -> None: 
        """
        Returns the deflection of this polygon

        Sets the deflection of this polygon to D. See more on deflection in Poly_Polygon2D
        """
    @overload
    def Deflection(self) -> float: ...
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
    def HasParameters(self) -> bool: 
        """
        Returns the table of the parameters associated with each node in this polygon. HasParameters function checks if parameters are associated with the nodes of this polygon.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes in this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle the function NbNodes returns 4.

        Returns the number of nodes in this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle the function NbNodes returns 4.
        """
    def Nodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of nodes for this polygon.
        """
    def Parameters(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns true if parameters are associated with the nodes in this polygon.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
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
class Poly_PolygonOnTriangulation(OCP.Standard.Standard_Transient):
    """
    This class provides a polygon in 3D space, based on the triangulation of a surface. It may be the approximate representation of a curve on the surface, or more generally the shape. A PolygonOnTriangulation is defined by a table of nodes. Each node is an index in the table of nodes specific to a triangulation, and represents a point on the surface. If the polygon is closed, the index of the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve on a surface, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.represents a 3d PolygonThis class provides a polygon in 3D space, based on the triangulation of a surface. It may be the approximate representation of a curve on the surface, or more generally the shape. A PolygonOnTriangulation is defined by a table of nodes. Each node is an index in the table of nodes specific to a triangulation, and represents a point on the surface. If the polygon is closed, the index of the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve on a surface, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.represents a 3d PolygonThis class provides a polygon in 3D space, based on the triangulation of a surface. It may be the approximate representation of a curve on the surface, or more generally the shape. A PolygonOnTriangulation is defined by a table of nodes. Each node is an index in the table of nodes specific to a triangulation, and represents a point on the surface. If the polygon is closed, the index of the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve on a surface, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.represents a 3d Polygon
    """
    def Copy(self) -> Poly_PolygonOnTriangulation: 
        """
        Creates a copy of current polygon
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self,D : float) -> None: 
        """
        Returns the deflection of this polygon

        Sets the deflection of this polygon to D. See more on deflection in Poly_Polygones2D.
        """
    @overload
    def Deflection(self) -> float: ...
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
    def HasParameters(self) -> bool: 
        """
        Returns true if parameters are associated with the nodes in this polygon.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes for this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle, the function NbNodes returns 4.

        Returns the number of nodes for this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle, the function NbNodes returns 4.
        """
    def Nodes(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Returns the table of nodes for this polygon. A node value is an index in the table of nodes specific to an existing triangulation of a shape.
        """
    def Parameters(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the table of the parameters associated with each node in this polygon. Warning Use the function HasParameters to check if parameters are associated with the nodes in this polygon.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Nodes : OCP.TColStd.TColStd_Array1OfInteger,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
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
class Poly_Triangle():
    """
    Describes a component triangle of a triangulation (Poly_Triangulation object). A Triangle is defined by a triplet of nodes. Each node is an index in the table of nodes specific to an existing triangulation of a shape, and represents a point on the surface.
    """
    def ChangeValue(self,Index : int) -> int: 
        """
        Get the node of given Index. Raises OutOfRange if Index is not in 1,2,3

        Get the node of given Index. Raises OutOfRange if Index is not in 1,2,3
        """
    def Get(self) -> Tuple[int, int, int]: 
        """
        Returns the node indices of this triangle in N1, N2 and N3.
        """
    @overload
    def Set(self,Index : int,Node : int) -> None: 
        """
        Sets the value of the three nodes of this triangle to N1, N2 and N3 respectively.

        Sets the value of the Indexth node of this triangle to Node. Raises OutOfRange if Index is not in 1,2,3

        Sets the value of the Indexth node of this triangle to Node. Raises OutOfRange if Index is not in 1,2,3
        """
    @overload
    def Set(self,N1 : int,N2 : int,N3 : int) -> None: ...
    def Value(self,Index : int) -> int: 
        """
        Get the node of given Index. Raises OutOfRange from Standard if Index is not in 1,2,3

        Get the node of given Index. Raises OutOfRange from Standard if Index is not in 1,2,3
        """
    @overload
    def __init__(self,N1 : int,N2 : int,N3 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Poly_Triangulation(OCP.Standard.Standard_Transient):
    """
    Provides a triangulation for a surface, a set of surfaces, or more generally a shape. A triangulation consists of an approximate representation of the actual shape, using a collection of points and triangles. The points are located on the surface. The edges of the triangles connect adjacent points with a straight line that approximates the true curve on the surface. A triangulation comprises: - A table of 3D nodes (3D points on the surface). - A table of triangles. Each triangle (Poly_Triangle object) comprises a triplet of indices in the table of 3D nodes specific to the triangulation. - A table of 2D nodes (2D points), parallel to the table of 3D nodes. This table is optional. If it exists, the coordinates of a 2D point are the (u, v) parameters of the corresponding 3D point on the surface approximated by the triangulation. - A deflection (optional), which maximizes the distance from a point on the surface to the corresponding point on its approximate triangulation. In many cases, algorithms do not need to work with the exact representation of a surface. A triangular representation induces simpler and more robust adjusting, faster performances, and the results are as good. This is a Transient class.Provides a triangulation for a surface, a set of surfaces, or more generally a shape. A triangulation consists of an approximate representation of the actual shape, using a collection of points and triangles. The points are located on the surface. The edges of the triangles connect adjacent points with a straight line that approximates the true curve on the surface. A triangulation comprises: - A table of 3D nodes (3D points on the surface). - A table of triangles. Each triangle (Poly_Triangle object) comprises a triplet of indices in the table of 3D nodes specific to the triangulation. - A table of 2D nodes (2D points), parallel to the table of 3D nodes. This table is optional. If it exists, the coordinates of a 2D point are the (u, v) parameters of the corresponding 3D point on the surface approximated by the triangulation. - A deflection (optional), which maximizes the distance from a point on the surface to the corresponding point on its approximate triangulation. In many cases, algorithms do not need to work with the exact representation of a surface. A triangular representation induces simpler and more robust adjusting, faster performances, and the results are as good. This is a Transient class.Provides a triangulation for a surface, a set of surfaces, or more generally a shape. A triangulation consists of an approximate representation of the actual shape, using a collection of points and triangles. The points are located on the surface. The edges of the triangles connect adjacent points with a straight line that approximates the true curve on the surface. A triangulation comprises: - A table of 3D nodes (3D points on the surface). - A table of triangles. Each triangle (Poly_Triangle object) comprises a triplet of indices in the table of 3D nodes specific to the triangulation. - A table of 2D nodes (2D points), parallel to the table of 3D nodes. This table is optional. If it exists, the coordinates of a 2D point are the (u, v) parameters of the corresponding 3D point on the surface approximated by the triangulation. - A deflection (optional), which maximizes the distance from a point on the surface to the corresponding point on its approximate triangulation. In many cases, algorithms do not need to work with the exact representation of a surface. A triangular representation induces simpler and more robust adjusting, faster performances, and the results are as good. This is a Transient class.
    """
    def ChangeNode(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Give access to the node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def ChangeNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of 3D nodes (3D points) for this triangulation. The returned array is shared. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def ChangeNormals(self) -> OCP.TShort.TShort_Array1OfShortReal: 
        """
        Gives access to the table of node normals.
        """
    def ChangeTriangle(self,theIndex : int) -> Poly_Triangle: 
        """
        Give access to the triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def ChangeTriangles(self) -> Poly_Array1OfTriangle: 
        """
        Returns the table of triangles for this triangulation. Function ChangeUVNodes shares the returned array. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def ChangeUVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Give access to the UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def ChangeUVNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of 2D nodes (2D points) associated with each 3D node of this triangulation. Function ChangeUVNodes shares the returned array. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def Copy(self) -> Poly_Triangulation: 
        """
        Creates full copy of current triangulation
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self) -> float: 
        """
        Returns the deflection of this triangulation.

        Sets the deflection of this triangulation to theDeflection. See more on deflection in Polygon2D
        """
    @overload
    def Deflection(self,theDeflection : float) -> None: ...
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
    def HasNormals(self) -> bool: 
        """
        Returns Standard_True if nodal normals are defined.
        """
    def HasUVNodes(self) -> bool: 
        """
        Returns Standard_True if 2D nodes are associated with 3D nodes for this triangulation.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes for this triangulation.
        """
    def NbTriangles(self) -> int: 
        """
        Returns the number of triangles for this triangulation.
        """
    def Node(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def Nodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of 3D nodes (3D points) for this triangulation.
        """
    def Normal(self,theIndex : int) -> OCP.gp.gp_Dir: 
        """
        Returns normal at the given index. Raises Standard_OutOfRange exception.
        """
    def Normals(self) -> OCP.TShort.TShort_Array1OfShortReal: 
        """
        Returns the table of node normals.
        """
    def RemoveUVNodes(self) -> None: 
        """
        Deallocates the UV nodes.
        """
    def SetNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: 
        """
        Changes normal at the given index. Raises Standard_OutOfRange exception.
        """
    def SetNormals(self,theNormals : OCP.TShort.TShort_HArray1OfShortReal) -> None: 
        """
        Sets the table of node normals. raises exception if length of theNormals != 3*NbNodes
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangle(self,theIndex : int) -> Poly_Triangle: 
        """
        Returns triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def Triangles(self) -> Poly_Array1OfTriangle: 
        """
        Returns the table of triangles for this triangulation.
        """
    def UVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def UVNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of 2D nodes (2D points) associated with each 3D node of this triangulation. The function HasUVNodes checks if 2D nodes are associated with the 3D nodes of this triangulation. Const reference on the 2d nodes values.
        """
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt,UVNodes : OCP.TColgp.TColgp_Array1OfPnt2d,Triangles : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self,theTriangulation : Poly_Triangulation) -> None: ...
    @overload
    def __init__(self,nbNodes : int,nbTriangles : int,UVNodes : bool) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt,Triangles : Poly_Array1OfTriangle) -> None: ...
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
def HashCode(theLink : Any,theUpperBound : int) -> int:
    """
    Computes a hash code for the given link, in the range [1, theUpperBound]
    """
def IsEqual(theKey1 : Any,theKey2 : Any) -> bool:
    """
    IsEqual method is needed for maps
    """
