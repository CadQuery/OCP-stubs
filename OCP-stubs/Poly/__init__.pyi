import OCP.Poly
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.gp
import OCP.TColgp
import OCP.Bnd
import OCP.Standard
import OCP.TShort
import OCP.TColStd
import io
__all__  = [
"Poly_Array1OfTriangle",
"Poly_ArrayOfNodes",
"Poly_ArrayOfUVNodes",
"Poly_CoherentLink",
"Poly_CoherentNode",
"Poly_CoherentTriangle",
"Poly_CoherentTriangulation",
"Poly_Connect",
"Poly_HArray1OfTriangle",
"Poly_ListOfTriangulation",
"Poly_MakeLoops2D",
"Poly_MakeLoops3D",
"Poly_MergeNodesTool",
"Poly_Polygon2D",
"Poly_Polygon3D",
"Poly_PolygonOnTriangulation",
"Poly_Triangle",
"Poly_Triangulation",
"Poly_TriangulationParameters",
"HashCode",
"IsEqual",
"Poly_MeshPurpose_Active",
"Poly_MeshPurpose_AnyFallback",
"Poly_MeshPurpose_Calculation",
"Poly_MeshPurpose_Loaded",
"Poly_MeshPurpose_NONE",
"Poly_MeshPurpose_Presentation",
"Poly_MeshPurpose_USER"
]
class Poly_Array1OfTriangle():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
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
    def __init__(self,theBegin : Poly_Triangle,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Poly_ArrayOfNodes():
    """
    Defines an array of 3D nodes of single/double precision configurable at construction time.
    """
    def Assign(self,theOther : Poly_ArrayOfNodes) -> Poly_ArrayOfNodes: 
        """
        Copies data of theOther array to this. The arrays should have the same length, but may have different precision / number of components (data conversion will be applied in the latter case).
        """
    def IsDoublePrecision(self) -> bool: 
        """
        Returns TRUE if array defines nodes with double precision.
        """
    def Move(self,theOther : Poly_ArrayOfNodes) -> Poly_ArrayOfNodes: 
        """
        Move assignment.
        """
    def SetDoublePrecision(self,theIsDouble : bool) -> None: 
        """
        Sets if array should define nodes with double or single precision. Raises exception if array was already allocated.
        """
    def SetValue(self,theIndex : int,theValue : OCP.gp.gp_Pnt) -> None: 
        """
        A generalized setter for point.

        A generalized setter for point.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        A generalized accessor to point.

        A generalized accessor to point.
        """
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Pnt,theLength : int) -> None: ...
    @overload
    def __init__(self,theOther : Poly_ArrayOfNodes) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Vec3f,theLength : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLength : int) -> None: ...
    pass
class Poly_ArrayOfUVNodes():
    """
    Defines an array of 2D nodes of single/double precision configurable at construction time.
    """
    def Assign(self,theOther : Poly_ArrayOfUVNodes) -> Poly_ArrayOfUVNodes: 
        """
        Copies data of theOther array to this. The arrays should have the same length, but may have different precision / number of components (data conversion will be applied in the latter case).
        """
    def IsDoublePrecision(self) -> bool: 
        """
        Returns TRUE if array defines nodes with double precision.
        """
    def Move(self,theOther : Poly_ArrayOfUVNodes) -> Poly_ArrayOfUVNodes: 
        """
        Move assignment.
        """
    def SetDoublePrecision(self,theIsDouble : bool) -> None: 
        """
        Sets if array should define nodes with double or single precision. Raises exception if array was already allocated.
        """
    def SetValue(self,theIndex : int,theValue : OCP.gp.gp_Pnt2d) -> None: 
        """
        A generalized setter for point.

        A generalized setter for point.
        """
    def Value(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        A generalized accessor to point.

        A generalized accessor to point.
        """
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Pnt2d,theLength : int) -> None: ...
    @overload
    def __init__(self,theLength : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.gp.gp_Vec2f,theLength : int) -> None: ...
    @overload
    def __init__(self,theOther : Poly_ArrayOfUVNodes) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,iNode0 : int,iNode1 : int) -> None: ...
    @overload
    def __init__(self,theTri : Poly_CoherentTriangle,iSide : int) -> None: ...
    pass
class Poly_CoherentNode(OCP.gp.gp_XYZ):
    """
    Node of coherent triangulation. Contains: Coordinates of a 3D point defining the node location 2D point coordinates List of triangles that use this Node Integer index, normally the index of the node in the original triangulation
    """
    def Add(self,theOther : OCP.gp.gp_XYZ) -> None: ...
    def AddTriangle(self,theTri : Poly_CoherentTriangle,theA : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Connect a triangle to this Node.
        """
    def Added(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    def ChangeCoord(self,theIndex : int) -> float: 
        """
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
    def Coord(self) -> Tuple[float, float, float]: 
        """
        returns the coordinate of range theIndex : theIndex = 1 => X is returned theIndex = 2 => Y is returned theIndex = 3 => Z is returned

        None
        """
    @overload
    def Coord(self,theIndex : int) -> float: ...
    @overload
    def Cross(self,theRight : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def Cross(self,theOther : OCP.gp.gp_XYZ) -> None: ...
    def CrossCross(self,theCoord1 : OCP.gp.gp_XYZ,theCoord2 : OCP.gp.gp_XYZ) -> None: 
        """
        Triple vector product Computes <me> = <me>.Cross(theCoord1.Cross(theCoord2))

        Triple vector product Computes <me> = <me>.Cross(theCoord1.Cross(theCoord2))
        """
    def CrossCrossed(self,theCoord1 : OCP.gp.gp_XYZ,theCoord2 : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        Triple vector product computes New = <me>.Cross(theCoord1.Cross(theCoord2))
        """
    def CrossMagnitude(self,theRight : OCP.gp.gp_XYZ) -> float: 
        """
        Computes the magnitude of the cross product between <me> and theRight. Returns || <me> ^ theRight ||

        Computes the magnitude of the cross product between <me> and theRight. Returns || <me> ^ theRight ||
        """
    def CrossSquareMagnitude(self,theRight : OCP.gp.gp_XYZ) -> float: 
        """
        Computes the square magnitude of the cross product between <me> and theRight. Returns || <me> ^ theRight ||**2

        Computes the square magnitude of the cross product between <me> and theRight. Returns || <me> ^ theRight ||**2
        """
    def Crossed(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    def Divide(self,theScalar : float) -> None: 
        """
        divides <me> by a real.
        """
    def Divided(self,theScalar : float) -> OCP.gp.gp_XYZ: 
        """
        divides <me> by a real.
        """
    def Dot(self,theOther : OCP.gp.gp_XYZ) -> float: 
        """
        computes the scalar product between <me> and theOther
        """
    def DotCross(self,theCoord1 : OCP.gp.gp_XYZ,theCoord2 : OCP.gp.gp_XYZ) -> float: 
        """
        computes the triple scalar product

        computes the triple scalar product
        """
    def Dump(self,theStream : io.BytesIO) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
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
    def InitFromJson(self,theSStream : Any,theStreamPos : int) -> bool: 
        """
        Inits the content of me from the stream
        """
    def IsEqual(self,theOther : OCP.gp.gp_XYZ,theTolerance : float) -> bool: 
        """
        Returns True if he coordinates of this XYZ object are equal to the respective coordinates Other, within the specified tolerance theTolerance. I.e.: abs(<me>.X() - theOther.X()) <= theTolerance and abs(<me>.Y() - theOther.Y()) <= theTolerance and abs(<me>.Z() - theOther.Z()) <= theTolerance.
        """
    def IsFreeNode(self) -> bool: 
        """
        Check if this is a free node, i.e., a node without a single incident triangle.
        """
    def Modulus(self) -> float: 
        """
        computes Sqrt (X*X + Y*Y + Z*Z) where X, Y and Z are the three coordinates of this XYZ object.
        """
    @overload
    def Multiplied(self,theMatrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: 
        """
        New = theMatrix * <me>
        """
    @overload
    def Multiplied(self,theScalar : float) -> OCP.gp.gp_XYZ: ...
    @overload
    def Multiplied(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    @overload
    def Multiply(self,theScalar : float) -> None: 
        """
        <me> = theMatrix * <me>

        <me> = theMatrix * <me>
        """
    @overload
    def Multiply(self,theOther : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def Multiply(self,theMatrix : OCP.gp.gp_Mat) -> None: ...
    def Normalize(self) -> None: 
        """
        Raised if <me>.Modulus() <= Resolution from gp

        Raised if <me>.Modulus() <= Resolution from gp
        """
    def Normalized(self) -> OCP.gp.gp_XYZ: 
        """
        Raised if <me>.Modulus() <= Resolution from gp
        """
    def RemoveTriangle(self,theTri : Poly_CoherentTriangle,theA : OCP.NCollection.NCollection_BaseAllocator) -> bool: 
        """
        Disconnect a triangle from this Node.
        """
    def Reverse(self) -> None: ...
    def Reversed(self) -> OCP.gp.gp_XYZ: ...
    @overload
    def SetCoord(self,theIndex : int,theXi : float) -> None: 
        """
        For this XYZ object, assigns the values theX, theY and theZ to its three coordinates

        modifies the coordinate of range theIndex theIndex = 1 => X is modified theIndex = 2 => Y is modified theIndex = 3 => Z is modified Raises OutOfRange if theIndex != {1, 2, 3}.
        """
    @overload
    def SetCoord(self,theX : float,theY : float,theZ : float) -> None: ...
    def SetIndex(self,theIndex : int) -> None: 
        """
        Set the value of node Index.
        """
    @overload
    def SetLinearForm(self,theA1 : float,theXYZ1 : OCP.gp.gp_XYZ,theA2 : float,theXYZ2 : OCP.gp.gp_XYZ,theA3 : float,theXYZ3 : OCP.gp.gp_XYZ,theXYZ4 : OCP.gp.gp_XYZ) -> None: 
        """
        <me> is set to the following linear form :

        <me> is set to the following linear form :

        <me> is set to the following linear form :

        <me> is set to the following linear form :

        <me> is set to the following linear form :

        <me> is set to the following linear form :
        """
    @overload
    def SetLinearForm(self,theA1 : float,theXYZ1 : OCP.gp.gp_XYZ,theA2 : float,theXYZ2 : OCP.gp.gp_XYZ,theXYZ3 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,theA1 : float,theXYZ1 : OCP.gp.gp_XYZ,theA2 : float,theXYZ2 : OCP.gp.gp_XYZ,theA3 : float,theXYZ3 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,theXYZ1 : OCP.gp.gp_XYZ,theXYZ2 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,theA1 : float,theXYZ1 : OCP.gp.gp_XYZ,theXYZ2 : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def SetLinearForm(self,theA1 : float,theXYZ1 : OCP.gp.gp_XYZ,theA2 : float,theXYZ2 : OCP.gp.gp_XYZ) -> None: ...
    def SetNormal(self,theVector : OCP.gp.gp_XYZ) -> None: 
        """
        Define the normal vector in the Node.
        """
    def SetUV(self,theU : float,theV : float) -> None: 
        """
        Set the UV coordinates of the Node.
        """
    def SetX(self,theX : float) -> None: 
        """
        Assigns the given value to the X coordinate
        """
    def SetY(self,theY : float) -> None: 
        """
        Assigns the given value to the Y coordinate
        """
    def SetZ(self,theZ : float) -> None: 
        """
        Assigns the given value to the Z coordinate
        """
    def SquareModulus(self) -> float: 
        """
        Computes X*X + Y*Y + Z*Z where X, Y and Z are the three coordinates of this XYZ object.
        """
    def Subtract(self,theOther : OCP.gp.gp_XYZ) -> None: ...
    def Subtracted(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: ...
    def TriangleIterator(self) -> Any: 
        """
        Create an iterator of incident triangles.
        """
    def X(self) -> float: 
        """
        Returns the X coordinate
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate
        """
    def __add__(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def __iadd__(self,theOther : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    @overload
    def __imul__(self,theOther : OCP.gp.gp_XYZ) -> None: 
        """
        None

        None

        None
        """
    @overload
    def __imul__(self,theMatrix : OCP.gp.gp_Mat) -> None: ...
    @overload
    def __imul__(self,theScalar : float) -> None: ...
    @overload
    def __init__(self,thePnt : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __ipow__(self,theOther : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def __isub__(self,theOther : OCP.gp.gp_XYZ) -> None: 
        """
        None
        """
    def __itruediv__(self,theScalar : float) -> None: 
        """
        None
        """
    @overload
    def __mul__(self,theScalar : float) -> OCP.gp.gp_XYZ: 
        """
        None

        None

        None
        """
    @overload
    def __mul__(self,theOther : OCP.gp.gp_XYZ) -> float: ...
    @overload
    def __mul__(self,theMatrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: ...
    def __pow__(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    @overload
    def __rmul__(self,theScalar : float) -> OCP.gp.gp_XYZ: 
        """
        None

        None

        None
        """
    @overload
    def __rmul__(self,theMatrix : OCP.gp.gp_Mat) -> OCP.gp.gp_XYZ: ...
    @overload
    def __rmul__(self,theOther : OCP.gp.gp_XYZ) -> float: ...
    def __sub__(self,theOther : OCP.gp.gp_XYZ) -> OCP.gp.gp_XYZ: 
        """
        None
        """
    def __truediv__(self,theScalar : float) -> OCP.gp.gp_XYZ: 
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
        Returns the index of the connection with the given triangle, or -1 if not found.
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
    def RemoveConnection(self,iConn : int) -> None: 
        """
        Remove the connection with the given index.

        Remove the connection with the given Triangle.
        """
    @overload
    def RemoveConnection(self,theTri : Poly_CoherentTriangle) -> bool: ...
    @overload
    def SetConnection(self,iConn : int,theTr : Poly_CoherentTriangle) -> bool: 
        """
        Create connection with another triangle theTri. This method creates both connections: in this triangle and in theTri. You do not need to call the same method on triangle theTr.

        Create connection with another triangle theTri. This method creates both connections: in this triangle and in theTri. This method is slower than the previous one, because it makes analysis what sides of both triangles are connected.
        """
    @overload
    def SetConnection(self,theTri : Poly_CoherentTriangle) -> bool: ...
    @overload
    def __init__(self,iNode0 : int,iNode1 : int,iNode2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Poly_CoherentTriangulation(OCP.Standard.Standard_Transient):
    """
    Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.Triangulation structure that allows to: Store the connectivity of each triangle with up to 3 neighbouring ones and with the corresponding 3rd nodes on them, Store the connectivity of each node with all triangles that share this node Add nodes and triangles to the structure, Find all triangles sharing a single or a couple of nodes Remove triangles from structure Optionally create Links between pairs of nodes according to the current triangulation. Convert from/to Poly_Triangulation structure.
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
    def Dump(self,arg1 : io.BytesIO) -> None: 
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
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theTriangulation : Poly_Triangulation,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
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
    def __init__(self,theTriangulation : Poly_Triangulation) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
    def __init__(self,theLower : int,theUpper : int,theValue : Poly_Triangle) -> None: ...
    @overload
    def __init__(self,theOther : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
    def Append(self,theItem : Poly_Triangulation,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : Poly_Triangulation) -> Poly_Triangulation: ...
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
    def InsertAfter(self,theOther : Poly_ListOfTriangulation,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : Poly_Triangulation,theIter : Any) -> Poly_Triangulation: ...
    @overload
    def InsertBefore(self,theItem : Poly_Triangulation,theIter : Any) -> Poly_Triangulation: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : Poly_ListOfTriangulation,theIter : Any) -> None: ...
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
    def Prepend(self,theItem : Poly_Triangulation) -> Poly_Triangulation: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : Poly_ListOfTriangulation) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Poly_ListOfTriangulation) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class Poly_MergeNodesTool(OCP.Standard.Standard_Transient):
    """
    Auxiliary tool for merging triangulation nodes for visualization purposes. Tool tries to merge all nodes within input triangulation, but split the ones on sharp corners at specified angle.
    """
    def AddElement(self,theElemNodes : OCP.gp.gp_XYZ,theNbNodes : int) -> None: 
        """
        Add new triangle or quad.
        """
    def AddQuad(self,theElemNodes : OCP.gp.gp_XYZ) -> None: 
        """
        Add new quad.
        """
    def AddTriangle(self,theElemNodes : OCP.gp.gp_XYZ) -> None: 
        """
        Add new triangle.
        """
    def AddTriangulation(self,theTris : Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf=OCP.gp.gp_Trsf,theToReverse : bool=False) -> None: 
        """
        Add another triangulation to created one.
        """
    def ChangeElementNode(self,theIndex : int) -> OCP.gp.gp_XYZ: 
        """
        Change node coordinates of element to be pushed.
        """
    def ChangeOutput(self) -> Poly_Triangulation: 
        """
        Setup output triangulation for modifications. When set to NULL, the tool could be used as a merge map for filling in external mesh structure.
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
    def ElementNodeIndex(self,theIndex : int) -> int: 
        """
        Return current element node index defined by PushLastElement().
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
    def MergeAngle(self) -> float: 
        """
        Return merge angle in radians; 0.0 by default (normals with non-exact directions are not merged).
        """
    @staticmethod
    def MergeNodes_s(theTris : Poly_Triangulation,theTrsf : OCP.gp.gp_Trsf,theToReverse : bool,theSmoothAngle : float,theMergeTolerance : float=0.0,theToForce : bool=True) -> Poly_Triangulation: 
        """
        Merge nodes of existing mesh and return the new mesh.
        """
    def MergeTolerance(self) -> float: 
        """
        Return merge tolerance; 0.0 by default (only 3D points with exactly matching coordinates are merged).
        """
    def NbDegenerativeElems(self) -> int: 
        """
        Return number of discarded degenerate elements.
        """
    def NbElements(self) -> int: 
        """
        Return number of elements.
        """
    def NbMergedElems(self) -> int: 
        """
        Return number of merged equal elements.
        """
    def NbNodes(self) -> int: 
        """
        Return number of nodes.
        """
    def PushLastElement(self,theNbNodes : int) -> None: 
        """
        Add new triangle or quad with nodes specified by ChangeElementNode().
        """
    def PushLastQuad(self) -> None: 
        """
        Add new quad with nodes specified by ChangeElementNode().
        """
    def PushLastTriangle(self) -> None: 
        """
        Add new triangle with nodes specified by ChangeElementNode().
        """
    def Result(self) -> Poly_Triangulation: 
        """
        Prepare and return result triangulation (temporary data will be truncated to result size).
        """
    def SetDropDegenerative(self,theToDrop : bool) -> None: 
        """
        Set if degenerate elements should be discarded.
        """
    def SetMergeAngle(self,theAngleRad : float) -> None: 
        """
        Set merge angle.
        """
    def SetMergeElems(self,theToMerge : bool) -> None: 
        """
        Set if equal elements should be filtered.
        """
    def SetMergeOpposite(self,theToMerge : bool) -> None: 
        """
        Set if nodes with opposite normals should be merged.
        """
    def SetMergeTolerance(self,theTolerance : float) -> None: 
        """
        Set merge tolerance.
        """
    def SetUnitFactor(self,theUnitFactor : float) -> None: 
        """
        Setup unit factor.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDropDegenerative(self) -> bool: 
        """
        Return TRUE if degenerate elements should be discarded; TRUE by default.
        """
    def ToMergeElems(self) -> bool: 
        """
        Return TRUE if equal elements should be filtered; FALSE by default.
        """
    def ToMergeOpposite(self) -> bool: 
        """
        Return TRUE if nodes with opposite normals should be merged; FALSE by default.
        """
    def __init__(self,theSmoothAngle : float,theMergeTolerance : float=0.0,theNbFacets : int=-1) -> None: ...
    def computeTriNormal(self) -> OCP.gp.gp_Vec3f: 
        """
        Compute normal for the mesh element.
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
class Poly_Polygon2D(OCP.Standard.Standard_Transient):
    """
    Provides a polygon in 2D space (for example, in the parametric space of a surface). It is generally an approximate representation of a curve. A Polygon2D is defined by a table of nodes. Each node is a 2D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes.Provides a polygon in 2D space (for example, in the parametric space of a surface). It is generally an approximate representation of a curve. A Polygon2D is defined by a table of nodes. Each node is a 2D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes.
    """
    def ChangeNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of nodes for this polygon.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self) -> float: 
        """
        Returns the deflection of this polygon. Deflection is used in cases where the polygon is an approximate representation of a curve. Deflection represents the maximum distance permitted between any point on the curve and the corresponding point on the polygon. By default the deflection value is equal to 0. An algorithm using this 2D polygon with a deflection value equal to 0 considers that it is working with a true polygon and not with an approximate representation of a curve. The Deflection function is used to modify the deflection value of this polygon. The deflection value can be used by any algorithm working with 2D polygons. For example: - An algorithm may use a unique deflection value for all its polygons. In this case it is not necessary to use the Deflection function. - Or an algorithm may want to attach a different deflection to each polygon. In this case, the Deflection function is used to set a value on each polygon, and later to fetch the value.

        Sets the deflection of this polygon.
        """
    @overload
    def Deflection(self,theDefl : float) -> None: ...
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
    def NbNodes(self) -> int: 
        """
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
    @overload
    def __init__(self,theNbNodes : int) -> None: ...
    @overload
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
    This class Provides a polygon in 3D space. It is generally an approximate representation of a curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.This class Provides a polygon in 3D space. It is generally an approximate representation of a curve. A Polygon3D is defined by a table of nodes. Each node is a 3D point. If the polygon is closed, the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.
    """
    def ChangeNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of nodes for this polygon.
        """
    def ChangeParameters(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        Returns the table of the parameters associated with each node in this polygon. ChangeParameters function returns the array as shared. Therefore if the table is selected by reference you can, by simply modifying it, directly modify the data structure of this polygon.
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
    def Deflection(self) -> float: 
        """
        Returns the deflection of this polygon

        Sets the deflection of this polygon. See more on deflection in Poly_Polygon2D
        """
    @overload
    def Deflection(self,theDefl : float) -> None: ...
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
    def NbNodes(self) -> int: 
        """
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
    @overload
    def __init__(self,theNbNodes : int,theHasParams : bool) -> None: ...
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
    This class provides a polygon in 3D space, based on the triangulation of a surface. It may be the approximate representation of a curve on the surface, or more generally the shape. A PolygonOnTriangulation is defined by a table of nodes. Each node is an index in the table of nodes specific to a triangulation, and represents a point on the surface. If the polygon is closed, the index of the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve on a surface, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.represents a 3d PolygonThis class provides a polygon in 3D space, based on the triangulation of a surface. It may be the approximate representation of a curve on the surface, or more generally the shape. A PolygonOnTriangulation is defined by a table of nodes. Each node is an index in the table of nodes specific to a triangulation, and represents a point on the surface. If the polygon is closed, the index of the point of closure is repeated at the end of the table of nodes. If the polygon is an approximate representation of a curve on a surface, you can associate with each of its nodes the value of the parameter of the corresponding point on the curve.represents a 3d Polygon
    """
    def ChangeNodes(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        None
        """
    def ChangeParameters(self) -> OCP.TColStd.TColStd_Array1OfReal: 
        """
        None
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
    def Deflection(self,theDefl : float) -> None: 
        """
        Returns the deflection of this polygon

        Sets the deflection of this polygon. See more on deflection in Poly_Polygones2D.
        """
    @overload
    def Deflection(self) -> float: ...
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
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes for this polygon. Note: If the polygon is closed, the point of closure is repeated at the end of its table of nodes. Thus, on a closed triangle, the function NbNodes returns 4.
        """
    def Node(self,theIndex : int) -> int: 
        """
        Returns node at the given index.
        """
    def Nodes(self) -> OCP.TColStd.TColStd_Array1OfInteger: 
        """
        Returns the table of nodes for this polygon. A node value is an index in the table of nodes specific to an existing triangulation of a shape.
        """
    def Parameter(self,theIndex : int) -> float: 
        """
        Returns parameter at the given index.
        """
    def Parameters(self) -> OCP.TColStd.TColStd_HArray1OfReal: 
        """
        Returns the table of the parameters associated with each node in this polygon. Warning! Use the function HasParameters to check if parameters are associated with the nodes in this polygon.
        """
    def SetNode(self,theIndex : int,theNode : int) -> None: 
        """
        Sets node at the given index.
        """
    def SetParameter(self,theIndex : int,theValue : float) -> None: 
        """
        Sets parameter at the given index.
        """
    def SetParameters(self,theParameters : OCP.TColStd.TColStd_HArray1OfReal) -> None: 
        """
        Sets the table of the parameters associated with each node in this polygon. Raises exception if array size doesn't much number of polygon nodes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theNbNodes : int,theHasParams : bool) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColStd.TColStd_Array1OfInteger) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColStd.TColStd_Array1OfInteger,Parameters : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
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
    Describes a component triangle of a triangulation (Poly_Triangulation object). A Triangle is defined by a triplet of nodes within [1, Poly_Triangulation::NbNodes()] range. Each node is an index in the table of nodes specific to an existing triangulation of a shape, and represents a point on the surface.
    """
    def ChangeValue(self,theIndex : int) -> int: 
        """
        Get the node of given Index. Raises OutOfRange if Index is not in 1,2,3
        """
    def Get(self) -> Tuple[int, int, int]: 
        """
        Returns the node indices of this triangle.
        """
    @overload
    def Set(self,theIndex : int,theNode : int) -> None: 
        """
        Sets the value of the three nodes of this triangle.

        Sets the value of node with specified index of this triangle. Raises Standard_OutOfRange if index is not in 1,2,3
        """
    @overload
    def Set(self,theN1 : int,theN2 : int,theN3 : int) -> None: ...
    def Value(self,theIndex : int) -> int: 
        """
        Get the node of given Index. Raises OutOfRange from Standard if Index is not in 1,2,3
        """
    @overload
    def __init__(self,theN1 : int,theN2 : int,theN3 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Poly_Triangulation(OCP.Standard.Standard_Transient):
    """
    Provides a triangulation for a surface, a set of surfaces, or more generally a shape.Provides a triangulation for a surface, a set of surfaces, or more generally a shape.Provides a triangulation for a surface, a set of surfaces, or more generally a shape.
    """
    def AddNormals(self) -> None: 
        """
        If an array for normals is not allocated yet, do it now.
        """
    def AddUVNodes(self) -> None: 
        """
        If an array for UV coordinates is not allocated yet, do it now.
        """
    def CachedMinMax(self) -> OCP.Bnd.Bnd_Box: 
        """
        Returns cached min - max range of triangulation data, which is VOID by default (e.g, no cached information).
        """
    def ChangeTriangle(self,theIndex : int) -> Poly_Triangle: 
        """
        None
        """
    def ChangeTriangles(self) -> Poly_Array1OfTriangle: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears internal arrays of nodes and all attributes.
        """
    def ComputeNormals(self) -> None: 
        """
        Compute smooth normals by averaging triangle normals.
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
    def DetachedLoadDeferredData(self,theFileSystem : OCP.OSD.OSD_FileSystem=None) -> Poly_Triangulation: 
        """
        Loads triangulation data into new Poly_Triangulation object from some deferred storage using specified shared input file system.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCachedMinMax(self) -> bool: 
        """
        Returns TRUE if there is some cached min - max range of this triangulation.
        """
    def HasDeferredData(self) -> bool: 
        """
        Returns TRUE if there is some triangulation data that can be loaded using LoadDeferredData().
        """
    def HasGeometry(self) -> bool: 
        """
        Returns TRUE if triangulation has some geometry.
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
    def InternalNodes(self) -> Poly_ArrayOfNodes: 
        """
        Returns an internal array of nodes. Node()/SetNode() should be used instead in portable code.
        """
    def InternalNormals(self) -> Any: 
        """
        Return an internal array of normals. Normal()/SetNormal() should be used instead in portable code.
        """
    def InternalTriangles(self) -> Poly_Array1OfTriangle: 
        """
        Returns an internal array of triangles. Triangle()/SetTriangle() should be used instead in portable code.
        """
    def InternalUVNodes(self) -> Poly_ArrayOfUVNodes: 
        """
        Returns an internal array of UV nodes. UBNode()/SetUVNode() should be used instead in portable code.
        """
    def IsDoublePrecision(self) -> bool: 
        """
        Returns TRUE if node positions are defined with double precision; TRUE by default.
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
    def LoadDeferredData(self,theFileSystem : OCP.OSD.OSD_FileSystem=None) -> bool: 
        """
        Loads triangulation data into itself from some deferred storage using specified shared input file system.
        """
    def MapNodeArray(self) -> OCP.TColgp.TColgp_HArray1OfPnt: 
        """
        Returns the table of 3D points for read-only access or NULL if nodes array is undefined. Poly_Triangulation::Node() should be used instead when possible. Returned object should not be used after Poly_Triangulation destruction.
        """
    def MapNormalArray(self) -> OCP.TShort.TShort_HArray1OfShortReal: 
        """
        Returns the table of per-vertex normals for read-only access or NULL if normals array is undefined. Poly_Triangulation::Normal() should be used instead when possible. Returned object should not be used after Poly_Triangulation destruction.
        """
    def MapTriangleArray(self) -> Poly_HArray1OfTriangle: 
        """
        Returns the triangle array for read-only access or NULL if triangle array is undefined. Poly_Triangulation::Triangle() should be used instead when possible. Returned object should not be used after Poly_Triangulation destruction.
        """
    def MapUVNodeArray(self) -> OCP.TColgp.TColgp_HArray1OfPnt2d: 
        """
        Returns the table of 2D nodes for read-only access or NULL if UV nodes array is undefined. Poly_Triangulation::UVNode() should be used instead when possible. Returned object should not be used after Poly_Triangulation destruction.
        """
    def MeshPurpose(self) -> int: 
        """
        Returns mesh purpose bits.
        """
    def MinMax(self,theBox : OCP.Bnd.Bnd_Box,theTrsf : OCP.gp.gp_Trsf,theIsAccurate : bool=False) -> bool: 
        """
        Extends the passed box with bounding box of this triangulation. Uses cached min - max range when available and: - input transformation theTrsf has no rotation part; - theIsAccurate is set to FALSE; - no triangulation data available (e.g. it is deferred and not loaded).
        """
    def NbDeferredNodes(self) -> int: 
        """
        Returns number of deferred nodes that can be loaded using LoadDeferredData(). Note: this is estimated values, which might be different from actually loaded values. Always check triangulation size of actually loaded data in code to avoid out-of-range issues.
        """
    def NbDeferredTriangles(self) -> int: 
        """
        Returns number of deferred triangles that can be loaded using LoadDeferredData(). Note: this is estimated values, which might be different from actually loaded values Always check triangulation size of actually loaded data in code to avoid out-of-range issues.
        """
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
        Returns a node at the given index.
        """
    @overload
    def Normal(self,theIndex : int,theVec3 : OCP.gp.gp_Vec3f) -> None: 
        """
        Returns normal at the given index.

        Returns normal at the given index.
        """
    @overload
    def Normal(self,theIndex : int) -> OCP.gp.gp_Dir: ...
    @overload
    def Parameters(self,theParams : Poly_TriangulationParameters) -> None: 
        """
        Updates initial set of parameters used to generate this triangulation.

        Returns initial set of parameters used to generate this triangulation.
        """
    @overload
    def Parameters(self) -> Poly_TriangulationParameters: ...
    def RemoveNormals(self) -> None: 
        """
        Deallocates the normals array.
        """
    def RemoveUVNodes(self) -> None: 
        """
        Deallocates the UV nodes array.
        """
    def ResizeNodes(self,theNbNodes : int,theToCopyOld : bool) -> None: 
        """
        Method resizing internal arrays of nodes (synchronously for all attributes).
        """
    def ResizeTriangles(self,theNbTriangles : int,theToCopyOld : bool) -> None: 
        """
        Method resizing an internal array of triangles.
        """
    def SetCachedMinMax(self,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Sets a cached min - max range of this triangulation. The bounding box should exactly match actual range of triangulation data without a gap or transformation, or otherwise undefined behavior will be observed. Passing a VOID range invalidates the cache.
        """
    def SetDoublePrecision(self,theIsDouble : bool) -> None: 
        """
        Set if node positions should be defined with double or single precision for 3D and UV nodes. Raises exception if data was already allocated.
        """
    def SetMeshPurpose(self,thePurpose : int) -> None: 
        """
        Sets mesh purpose bits.
        """
    def SetNode(self,theIndex : int,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets a node coordinates.
        """
    @overload
    def SetNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: 
        """
        Changes normal at the given index.

        Changes normal at the given index.
        """
    @overload
    def SetNormal(self,theIndex : int,theNormal : OCP.gp.gp_Vec3f) -> None: ...
    def SetNormals(self,theNormals : OCP.TShort.TShort_HArray1OfShortReal) -> None: 
        """
        None
        """
    def SetTriangle(self,theIndex : int,theTriangle : Poly_Triangle) -> None: 
        """
        Sets a triangle.
        """
    def SetUVNode(self,theIndex : int,thePnt : OCP.gp.gp_Pnt2d) -> None: 
        """
        Sets an UV-node coordinates.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangle(self,theIndex : int) -> Poly_Triangle: 
        """
        Returns triangle at the given index.
        """
    def Triangles(self) -> Poly_Array1OfTriangle: 
        """
        None
        """
    def UVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns UV-node at the given index.
        """
    def UnloadDeferredData(self) -> bool: 
        """
        Releases triangulation data if it has connected deferred storage.
        """
    def UpdateCachedMinMax(self) -> None: 
        """
        Updates cached min - max range of this triangulation with bounding box of nodal data.
        """
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt,UVNodes : OCP.TColgp.TColgp_Array1OfPnt2d,Triangles : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self,Nodes : OCP.TColgp.TColgp_Array1OfPnt,Triangles : Poly_Array1OfTriangle) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbNodes : int,theNbTriangles : int,theHasUVNodes : bool,theHasNormals : bool=False) -> None: ...
    @overload
    def __init__(self,theTriangulation : Poly_Triangulation) -> None: ...
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
class Poly_TriangulationParameters(OCP.Standard.Standard_Transient):
    """
    Represents initial set of parameters triangulation is built for.Represents initial set of parameters triangulation is built for.
    """
    def Angle(self) -> float: 
        """
        Returns angular deflection or -1 if undefined.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Deflection(self) -> float: 
        """
        Returns linear deflection or -1 if undefined.
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
    def HasAngle(self) -> bool: 
        """
        Returns true if angular deflection is defined.
        """
    def HasDeflection(self) -> bool: 
        """
        Returns true if linear deflection is defined.
        """
    def HasMinSize(self) -> bool: 
        """
        Returns true if minimum size is defined.
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
    def MinSize(self) -> float: 
        """
        Returns minimum size or -1 if undefined.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theDeflection : float=-1.0,theAngle : float=-1.0,theMinSize : float=-1.0) -> None: ...
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
Poly_MeshPurpose_Active = 4
Poly_MeshPurpose_AnyFallback = 16
Poly_MeshPurpose_Calculation = 1
Poly_MeshPurpose_Loaded = 8
Poly_MeshPurpose_NONE = 0
Poly_MeshPurpose_Presentation = 2
Poly_MeshPurpose_USER = 32
