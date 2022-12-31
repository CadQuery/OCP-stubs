import OCP.Bnd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.gp
import OCP.TColgp
import io
import OCP.TColStd
__all__  = [
"Bnd_Array1OfBox",
"Bnd_Array1OfBox2d",
"Bnd_Array1OfSphere",
"Bnd_B2d",
"Bnd_B2f",
"Bnd_B3d",
"Bnd_B3f",
"Bnd_BoundSortBox",
"Bnd_Box",
"Bnd_Box2d",
"Bnd_HArray1OfBox",
"Bnd_HArray1OfBox2d",
"Bnd_HArray1OfSphere",
"Bnd_OBB",
"Bnd_Range",
"Bnd_Sphere",
"Bnd_Tools"
]
class Bnd_Array1OfBox():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Bnd_Array1OfBox) -> Bnd_Array1OfBox: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Bnd_Box: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Box: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Box: 
        """
        Variable value access
        """
    def First(self) -> Bnd_Box: 
        """
        Returns first element
        """
    def Init(self,theValue : Bnd_Box) -> None: 
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
    def Last(self) -> Bnd_Box: 
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
    def Move(self,theOther : Bnd_Array1OfBox) -> Bnd_Array1OfBox: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Box) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Box: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Bnd_Box,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Bnd_Array1OfBox) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Bnd_Array1OfBox2d():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Bnd_Array1OfBox2d) -> Bnd_Array1OfBox2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Bnd_Box2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Box2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Box2d: 
        """
        Variable value access
        """
    def First(self) -> Bnd_Box2d: 
        """
        Returns first element
        """
    def Init(self,theValue : Bnd_Box2d) -> None: 
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
    def Last(self) -> Bnd_Box2d: 
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
    def Move(self,theOther : Bnd_Array1OfBox2d) -> Bnd_Array1OfBox2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Box2d) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Box2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Bnd_Array1OfBox2d) -> None: ...
    @overload
    def __init__(self,theBegin : Bnd_Box2d,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Bnd_Array1OfSphere():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Bnd_Array1OfSphere) -> Bnd_Array1OfSphere: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Bnd_Sphere: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Sphere: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Sphere: 
        """
        Variable value access
        """
    def First(self) -> Bnd_Sphere: 
        """
        Returns first element
        """
    def Init(self,theValue : Bnd_Sphere) -> None: 
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
    def Last(self) -> Bnd_Sphere: 
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
    def Move(self,theOther : Bnd_Array1OfSphere) -> Bnd_Array1OfSphere: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Sphere) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Sphere: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : Bnd_Array1OfSphere) -> None: ...
    @overload
    def __init__(self,theBegin : Bnd_Sphere,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Bnd_B2d():
    """
    None
    """
    @overload
    def Add(self,theBox : Bnd_B2d) -> None: 
        """
        Update the box by a point.

        Update the box by a point.

        Update the box by another box.
        """
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def Add(self,thePnt : OCP.gp.gp_XY) -> None: ...
    def Clear(self) -> None: 
        """
        Reset the box data.
        """
    def CornerMax(self) -> OCP.gp.gp_XY: 
        """
        Query a box corner: (Center + HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def CornerMin(self) -> OCP.gp.gp_XY: 
        """
        Query a box corner: (Center - HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def Enlarge(self,theDiff : float) -> None: 
        """
        Extend the Box by the absolute value of theDiff.
        """
    @overload
    def IsIn(self,theBox : Bnd_B2d,theTrsf : OCP.gp.gp_Trsf2d) -> bool: 
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns True if 'this' box is fully inside 'theBox'.

        Check that the box 'this' is inside the given box 'theBox' transformed by 'theTrsf'. Returns True if 'this' box is fully inside the transformed 'theBox'.
        """
    @overload
    def IsIn(self,theBox : Bnd_B2d) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B2d) -> bool: 
        """
        Check the given point for the inclusion in the Box. Returns True if the point is outside.

        Check a circle for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box oriented by the given transformation for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given Line for the intersection with the current box. Returns True if there is no intersection.

        Check the Segment defined by the couple of input points for the intersection with the current box. Returns True if there is no intersection.
        """
    @overload
    def IsOut(self,theCenter : OCP.gp.gp_XY,theRadius : float,isCircleHollow : bool=False) -> bool: ...
    @overload
    def IsOut(self,theP0 : OCP.gp.gp_XY,theP1 : OCP.gp.gp_XY) -> bool: ...
    @overload
    def IsOut(self,thePnt : OCP.gp.gp_XY) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B2d,theTrsf : OCP.gp.gp_Trsf2d) -> bool: ...
    @overload
    def IsOut(self,theLine : OCP.gp.gp_Ax2d) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Returns True if the box is void (non-initialized).
        """
    def Limit(self,theOtherBox : Bnd_B2d) -> bool: 
        """
        Limit the Box by the internals of theOtherBox. Returns True if the limitation takes place, otherwise False indicating that the boxes do not intersect.
        """
    def SetCenter(self,theCenter : OCP.gp.gp_XY) -> None: 
        """
        Set the Center coordinates
        """
    def SetHSize(self,theHSize : OCP.gp.gp_XY) -> None: 
        """
        Set the HSize (half-diagonal) coordinates. All components of theHSize must be non-negative.
        """
    def SquareExtent(self) -> float: 
        """
        Query the square diagonal. If the box is VOID (see method IsVoid()) then a very big real value is returned.
        """
    def Transformed(self,theTrsf : OCP.gp.gp_Trsf2d) -> Bnd_B2d: 
        """
        Transform the bounding box with the given transformation. The resulting box will be larger if theTrsf contains rotation.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCenter : OCP.gp.gp_XY,theHSize : OCP.gp.gp_XY) -> None: ...
    pass
class Bnd_B2f():
    """
    None
    """
    @overload
    def Add(self,theBox : Bnd_B2f) -> None: 
        """
        Update the box by a point.

        Update the box by a point.

        Update the box by another box.
        """
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt2d) -> None: ...
    @overload
    def Add(self,thePnt : OCP.gp.gp_XY) -> None: ...
    def Clear(self) -> None: 
        """
        Reset the box data.
        """
    def CornerMax(self) -> OCP.gp.gp_XY: 
        """
        Query a box corner: (Center + HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def CornerMin(self) -> OCP.gp.gp_XY: 
        """
        Query a box corner: (Center - HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def Enlarge(self,theDiff : float) -> None: 
        """
        Extend the Box by the absolute value of theDiff.
        """
    @overload
    def IsIn(self,theBox : Bnd_B2f,theTrsf : OCP.gp.gp_Trsf2d) -> bool: 
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns True if 'this' box is fully inside 'theBox'.

        Check that the box 'this' is inside the given box 'theBox' transformed by 'theTrsf'. Returns True if 'this' box is fully inside the transformed 'theBox'.
        """
    @overload
    def IsIn(self,theBox : Bnd_B2f) -> bool: ...
    @overload
    def IsOut(self,thePnt : OCP.gp.gp_XY) -> bool: 
        """
        Check the given point for the inclusion in the Box. Returns True if the point is outside.

        Check a circle for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box oriented by the given transformation for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given Line for the intersection with the current box. Returns True if there is no intersection.

        Check the Segment defined by the couple of input points for the intersection with the current box. Returns True if there is no intersection.
        """
    @overload
    def IsOut(self,theOtherBox : Bnd_B2f) -> bool: ...
    @overload
    def IsOut(self,theLine : OCP.gp.gp_Ax2d) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B2f,theTrsf : OCP.gp.gp_Trsf2d) -> bool: ...
    @overload
    def IsOut(self,theP0 : OCP.gp.gp_XY,theP1 : OCP.gp.gp_XY) -> bool: ...
    @overload
    def IsOut(self,theCenter : OCP.gp.gp_XY,theRadius : float,isCircleHollow : bool=False) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Returns True if the box is void (non-initialized).
        """
    def Limit(self,theOtherBox : Bnd_B2f) -> bool: 
        """
        Limit the Box by the internals of theOtherBox. Returns True if the limitation takes place, otherwise False indicating that the boxes do not intersect.
        """
    def SetCenter(self,theCenter : OCP.gp.gp_XY) -> None: 
        """
        Set the Center coordinates
        """
    def SetHSize(self,theHSize : OCP.gp.gp_XY) -> None: 
        """
        Set the HSize (half-diagonal) coordinates. All components of theHSize must be non-negative.
        """
    def SquareExtent(self) -> float: 
        """
        Query the square diagonal. If the box is VOID (see method IsVoid()) then a very big real value is returned.
        """
    def Transformed(self,theTrsf : OCP.gp.gp_Trsf2d) -> Bnd_B2f: 
        """
        Transform the bounding box with the given transformation. The resulting box will be larger if theTrsf contains rotation.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCenter : OCP.gp.gp_XY,theHSize : OCP.gp.gp_XY) -> None: ...
    pass
class Bnd_B3d():
    """
    None
    """
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Update the box by a point.

        Update the box by a point.

        Update the box by another box.
        """
    @overload
    def Add(self,thePnt : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def Add(self,theBox : Bnd_B3d) -> None: ...
    def Clear(self) -> None: 
        """
        Reset the box data.
        """
    def CornerMax(self) -> OCP.gp.gp_XYZ: 
        """
        Query the upper corner: (Center + HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def CornerMin(self) -> OCP.gp.gp_XYZ: 
        """
        Query the lower corner: (Center - HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def Enlarge(self,theDiff : float) -> None: 
        """
        Extend the Box by the absolute value of theDiff.
        """
    @overload
    def IsIn(self,theBox : Bnd_B3d) -> bool: 
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns True if 'this' box is fully inside 'theBox'.

        Check that the box 'this' is inside the given box 'theBox' transformed by 'theTrsf'. Returns True if 'this' box is fully inside the transformed 'theBox'.
        """
    @overload
    def IsIn(self,theBox : Bnd_B3d,theTrsf : OCP.gp.gp_Trsf) -> bool: ...
    @overload
    def IsOut(self,thePnt : OCP.gp.gp_XYZ) -> bool: 
        """
        Check the given point for the inclusion in the Box. Returns True if the point is outside.

        Check a sphere for the intersection with the current box. Returns True if there is no intersection between boxes. If the parameter 'IsSphereHollow' is True, then the intersection is not reported for a box that is completely inside the sphere (otherwise this method would report an intersection).

        Check the given box for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box oriented by the given transformation for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given Line for the intersection with the current box. Returns True if there is no intersection. isRay==True means intersection check with the positive half-line theOverthickness is the addition to the size of the current box (may be negative). If positive, it can be treated as the thickness of the line 'theLine' or the radius of the cylinder along 'theLine'

        Check the given Plane for the intersection with the current box. Returns True if there is no intersection.
        """
    @overload
    def IsOut(self,thePlane : OCP.gp.gp_Ax3) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B3d,theTrsf : OCP.gp.gp_Trsf) -> bool: ...
    @overload
    def IsOut(self,theCenter : OCP.gp.gp_XYZ,theRadius : float,isSphereHollow : bool=False) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B3d) -> bool: ...
    @overload
    def IsOut(self,theLine : OCP.gp.gp_Ax1,isRay : bool=False,theOverthickness : float=0.0) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Returns True if the box is void (non-initialized).
        """
    def Limit(self,theOtherBox : Bnd_B3d) -> bool: 
        """
        Limit the Box by the internals of theOtherBox. Returns True if the limitation takes place, otherwise False indicating that the boxes do not intersect.
        """
    def SetCenter(self,theCenter : OCP.gp.gp_XYZ) -> None: 
        """
        Set the Center coordinates
        """
    def SetHSize(self,theHSize : OCP.gp.gp_XYZ) -> None: 
        """
        Set the HSize (half-diagonal) coordinates. All components of theHSize must be non-negative.
        """
    def SquareExtent(self) -> float: 
        """
        Query the square diagonal. If the box is VOID (see method IsVoid()) then a very big real value is returned.
        """
    def Transformed(self,theTrsf : OCP.gp.gp_Trsf) -> Bnd_B3d: 
        """
        Transform the bounding box with the given transformation. The resulting box will be larger if theTrsf contains rotation.
        """
    @overload
    def __init__(self,theCenter : OCP.gp.gp_XYZ,theHSize : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bnd_B3f():
    """
    None
    """
    @overload
    def Add(self,theBox : Bnd_B3f) -> None: 
        """
        Update the box by a point.

        Update the box by a point.

        Update the box by another box.
        """
    @overload
    def Add(self,thePnt : OCP.gp.gp_XYZ) -> None: ...
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt) -> None: ...
    def Clear(self) -> None: 
        """
        Reset the box data.
        """
    def CornerMax(self) -> OCP.gp.gp_XYZ: 
        """
        Query the upper corner: (Center + HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def CornerMin(self) -> OCP.gp.gp_XYZ: 
        """
        Query the lower corner: (Center - HSize). You must make sure that the box is NOT VOID (see IsVoid()), otherwise the method returns irrelevant result.
        """
    def Enlarge(self,theDiff : float) -> None: 
        """
        Extend the Box by the absolute value of theDiff.
        """
    @overload
    def IsIn(self,theBox : Bnd_B3f) -> bool: 
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns True if 'this' box is fully inside 'theBox'.

        Check that the box 'this' is inside the given box 'theBox' transformed by 'theTrsf'. Returns True if 'this' box is fully inside the transformed 'theBox'.
        """
    @overload
    def IsIn(self,theBox : Bnd_B3f,theTrsf : OCP.gp.gp_Trsf) -> bool: ...
    @overload
    def IsOut(self,thePlane : OCP.gp.gp_Ax3) -> bool: 
        """
        Check the given point for the inclusion in the Box. Returns True if the point is outside.

        Check a sphere for the intersection with the current box. Returns True if there is no intersection between boxes. If the parameter 'IsSphereHollow' is True, then the intersection is not reported for a box that is completely inside the sphere (otherwise this method would report an intersection).

        Check the given box for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given box oriented by the given transformation for the intersection with the current box. Returns True if there is no intersection between boxes.

        Check the given Line for the intersection with the current box. Returns True if there is no intersection. isRay==True means intersection check with the positive half-line theOverthickness is the addition to the size of the current box (may be negative). If positive, it can be treated as the thickness of the line 'theLine' or the radius of the cylinder along 'theLine'

        Check the given Plane for the intersection with the current box. Returns True if there is no intersection.
        """
    @overload
    def IsOut(self,theOtherBox : Bnd_B3f) -> bool: ...
    @overload
    def IsOut(self,theCenter : OCP.gp.gp_XYZ,theRadius : float,isSphereHollow : bool=False) -> bool: ...
    @overload
    def IsOut(self,theLine : OCP.gp.gp_Ax1,isRay : bool=False,theOverthickness : float=0.0) -> bool: ...
    @overload
    def IsOut(self,thePnt : OCP.gp.gp_XYZ) -> bool: ...
    @overload
    def IsOut(self,theOtherBox : Bnd_B3f,theTrsf : OCP.gp.gp_Trsf) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Returns True if the box is void (non-initialized).
        """
    def Limit(self,theOtherBox : Bnd_B3f) -> bool: 
        """
        Limit the Box by the internals of theOtherBox. Returns True if the limitation takes place, otherwise False indicating that the boxes do not intersect.
        """
    def SetCenter(self,theCenter : OCP.gp.gp_XYZ) -> None: 
        """
        Set the Center coordinates
        """
    def SetHSize(self,theHSize : OCP.gp.gp_XYZ) -> None: 
        """
        Set the HSize (half-diagonal) coordinates. All components of theHSize must be non-negative.
        """
    def SquareExtent(self) -> float: 
        """
        Query the square diagonal. If the box is VOID (see method IsVoid()) then a very big real value is returned.
        """
    def Transformed(self,theTrsf : OCP.gp.gp_Trsf) -> Bnd_B3f: 
        """
        Transform the bounding box with the given transformation. The resulting box will be larger if theTrsf contains rotation.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theCenter : OCP.gp.gp_XYZ,theHSize : OCP.gp.gp_XYZ) -> None: ...
    pass
class Bnd_BoundSortBox():
    """
    A tool to compare a bounding box or a plane with a set of bounding boxes. It sorts the set of bounding boxes to give the list of boxes which intersect the element being compared. The boxes being sorted generally bound a set of shapes, while the box being compared bounds a shape to be compared. The resulting list of intersecting boxes therefore gives the list of items which potentially intersect the shape to be compared.
    """
    def Add(self,theBox : Bnd_Box,boxIndex : int) -> None: 
        """
        Adds the bounding box theBox at position boxIndex in the array of boxes to be sorted by this comparison algorithm. This function is used only in conjunction with the third syntax described in the synopsis of Initialize.
        """
    @overload
    def Compare(self,theBox : Bnd_Box) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Compares the bounding box theBox, with the set of bounding boxes to be sorted by this comparison algorithm, and returns the list of intersecting bounding boxes as a list of indexes on the array of bounding boxes used by this algorithm.

        Compares the plane P with the set of bounding boxes to be sorted by this comparison algorithm, and returns the list of intersecting bounding boxes as a list of indexes on the array of bounding boxes used by this algorithm.
        """
    @overload
    def Compare(self,P : OCP.gp.gp_Pln) -> OCP.TColStd.TColStd_ListOfInteger: ...
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    @overload
    def Initialize(self,CompleteBox : Bnd_Box,SetOfBox : Bnd_HArray1OfBox) -> None: 
        """
        Initializes this comparison algorithm with - the set of bounding boxes SetOfBox.

        Initializes this comparison algorithm with - the set of bounding boxes SetOfBox, where CompleteBox is given as the global bounding box of SetOfBox.

        Initializes this comparison algorithm, giving it only - the maximum number nbComponents of the bounding boxes to be managed. Use the Add function to define the array of bounding boxes to be sorted by this algorithm.
        """
    @overload
    def Initialize(self,CompleteBox : Bnd_Box,nbComponents : int) -> None: ...
    @overload
    def Initialize(self,SetOfBox : Bnd_HArray1OfBox) -> None: ...
    def __init__(self) -> None: ...
    pass
class Bnd_Box():
    """
    Describes a bounding box in 3D space. A bounding box is parallel to the axes of the coordinates system. If it is finite, it is defined by the three intervals: - [ Xmin,Xmax ], - [ Ymin,Ymax ], - [ Zmin,Zmax ]. A bounding box may be infinite (i.e. open) in one or more directions. It is said to be: - OpenXmin if it is infinite on the negative side of the "X Direction"; - OpenXmax if it is infinite on the positive side of the "X Direction"; - OpenYmin if it is infinite on the negative side of the "Y Direction"; - OpenYmax if it is infinite on the positive side of the "Y Direction"; - OpenZmin if it is infinite on the negative side of the "Z Direction"; - OpenZmax if it is infinite on the positive side of the "Z Direction"; - WholeSpace if it is infinite in all six directions. In this case, any point of the space is inside the box; - Void if it is empty. In this case, there is no point included in the box. A bounding box is defined by: - six bounds (Xmin, Xmax, Ymin, Ymax, Zmin and Zmax) which limit the bounding box if it is finite, - eight flags (OpenXmin, OpenXmax, OpenYmin, OpenYmax, OpenZmin, OpenZmax, WholeSpace and Void) which describe the bounding box if it is infinite or empty, and - a gap, which is included on both sides in any direction when consulting the finite bounds of the box.
    """
    @overload
    def Add(self,Other : Bnd_Box) -> None: 
        """
        Adds the box <Other> to <me>.

        Adds a Pnt to the box.

        Extends <me> from the Pnt <P> in the direction <D>.

        Extends the Box in the given Direction, i.e. adds an half-line. The box may become infinite in 1,2 or 3 directions.
        """
    @overload
    def Add(self,D : OCP.gp.gp_Dir) -> None: ...
    @overload
    def Add(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Add(self,P : OCP.gp.gp_Pnt,D : OCP.gp.gp_Dir) -> None: ...
    def CornerMax(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the upper corner of this bounding box. The gap is included. If this bounding box is infinite (i.e. "open"), returned values may be equal to +/- Precision::Infinite(). Standard_ConstructionError exception will be thrown if the box is void. if IsVoid()
        """
    def CornerMin(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the lower corner of this bounding box. The gap is included. If this bounding box is infinite (i.e. "open"), returned values may be equal to +/- Precision::Infinite(). Standard_ConstructionError exception will be thrown if the box is void. if IsVoid()
        """
    def Distance(self,Other : Bnd_Box) -> float: 
        """
        Computes the minimum distance between two boxes.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Enlarge(self,Tol : float) -> None: 
        """
        Enlarges the box with a tolerance value. (minvalues-Abs(<tol>) and maxvalues+Abs(<tol>)) This means that the minimum values of its X, Y and Z intervals of definition, when they are finite, are reduced by the absolute value of Tol, while the maximum values are increased by the same amount.
        """
    def FinitePart(self) -> Bnd_Box: 
        """
        Returns a finite part of an infinite bounding box (returns self if this is already finite box). This can be a Void box in case if its sides has been defined as infinite (Open) without adding any finite points. WARNING! This method relies on Open flags, the infinite points added using Add() method will be returned as is.
        """
    def Get(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the bounds of this bounding box. The gap is included. If this bounding box is infinite (i.e. "open"), returned values may be equal to +/- Precision::Infinite(). Standard_ConstructionError exception will be thrown if the box is void. if IsVoid()
        """
    def GetGap(self) -> float: 
        """
        Returns the gap of this bounding box.
        """
    def HasFinitePart(self) -> bool: 
        """
        Returns TRUE if this box has finite part.
        """
    def InitFromJson(self,theSStream : Any,theStreamPos : int) -> bool: 
        """
        Inits the content of me from the stream
        """
    def IsOpen(self) -> bool: 
        """
        Returns true if this bounding box has at least one open direction.
        """
    def IsOpenXmax(self) -> bool: 
        """
        Returns true if this bounding box is open in the Xmax direction.
        """
    def IsOpenXmin(self) -> bool: 
        """
        Returns true if this bounding box is open in the Xmin direction.
        """
    def IsOpenYmax(self) -> bool: 
        """
        Returns true if this bounding box is open in the Ymax direction.
        """
    def IsOpenYmin(self) -> bool: 
        """
        Returns true if this bounding box is open in the Ymix direction.
        """
    def IsOpenZmax(self) -> bool: 
        """
        Returns true if this bounding box is open in the Zmax direction.
        """
    def IsOpenZmin(self) -> bool: 
        """
        Returns true if this bounding box is open in the Zmin direction.
        """
    @overload
    def IsOut(self,Other : Bnd_Box) -> bool: 
        """
        Returns True if the Pnt is out the box.

        Returns False if the line intersects the box.

        Returns False if the plane intersects the box.

        Returns False if the <Box> intersects or is inside <me>.

        Returns False if the transformed <Box> intersects or is inside <me>.

        Returns False if the transformed <Box> intersects or is inside the transformed box <me>.

        Returns False if the flat band lying between two parallel lines represented by their reference points <P1>, <P2> and direction <D> intersects the box.
        """
    @overload
    def IsOut(self,Other : Bnd_Box,T : OCP.gp.gp_Trsf) -> bool: ...
    @overload
    def IsOut(self,P : OCP.gp.gp_Pln) -> bool: ...
    @overload
    def IsOut(self,L : OCP.gp.gp_Lin) -> bool: ...
    @overload
    def IsOut(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt,D : OCP.gp.gp_Dir) -> bool: ...
    @overload
    def IsOut(self,P : OCP.gp.gp_Pnt) -> bool: ...
    @overload
    def IsOut(self,T1 : OCP.gp.gp_Trsf,Other : Bnd_Box,T2 : OCP.gp.gp_Trsf) -> bool: ...
    def IsThin(self,tol : float) -> bool: 
        """
        Returns true if IsXThin, IsYThin and IsZThin are all true, i.e. if the box is thin in all three dimensions.
        """
    def IsVoid(self) -> bool: 
        """
        Returns true if this bounding box is empty (Void flag).
        """
    def IsWhole(self) -> bool: 
        """
        Returns true if this bounding box is infinite in all 6 directions (WholeSpace flag).
        """
    def IsXThin(self,tol : float) -> bool: 
        """
        true if xmax-xmin < tol.
        """
    def IsYThin(self,tol : float) -> bool: 
        """
        true if ymax-ymin < tol.
        """
    def IsZThin(self,tol : float) -> bool: 
        """
        true if zmax-zmin < tol.
        """
    def OpenXmax(self) -> None: 
        """
        The Box will be infinitely long in the Xmax direction.
        """
    def OpenXmin(self) -> None: 
        """
        The Box will be infinitely long in the Xmin direction.
        """
    def OpenYmax(self) -> None: 
        """
        The Box will be infinitely long in the Ymax direction.
        """
    def OpenYmin(self) -> None: 
        """
        The Box will be infinitely long in the Ymin direction.
        """
    def OpenZmax(self) -> None: 
        """
        The Box will be infinitely long in the Zmax direction.
        """
    def OpenZmin(self) -> None: 
        """
        The Box will be infinitely long in the Zmin direction.
        """
    @overload
    def Set(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Sets this bounding box so that it bounds - the point P. This involves first setting this bounding box to be void and then adding the point P.

        Sets this bounding box so that it bounds the half-line defined by point P and direction D, i.e. all points M defined by M=P+u*D, where u is greater than or equal to 0, are inside the bounding volume. This involves first setting this box to be void and then adding the half-line.
        """
    @overload
    def Set(self,P : OCP.gp.gp_Pnt,D : OCP.gp.gp_Dir) -> None: ...
    def SetGap(self,Tol : float) -> None: 
        """
        Set the gap of this bounding box to abs(Tol).
        """
    def SetVoid(self) -> None: 
        """
        Sets this bounding box so that it is empty. All points are outside a void box.
        """
    def SetWhole(self) -> None: 
        """
        Sets this bounding box so that it covers the whole of 3D space. It is infinitely long in all directions.
        """
    def SquareExtent(self) -> float: 
        """
        Computes the squared diagonal of me.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> Bnd_Box: 
        """
        Returns a bounding box which is the result of applying the transformation T to this bounding box. Warning Applying a geometric transformation (for example, a rotation) to a bounding box generally increases its dimensions. This is not optimal for algorithms which use it.
        """
    @overload
    def Update(self,aXmin : float,aYmin : float,aZmin : float,aXmax : float,aYmax : float,aZmax : float) -> None: 
        """
        Enlarges this bounding box, if required, so that it contains at least: - interval [ aXmin,aXmax ] in the "X Direction", - interval [ aYmin,aYmax ] in the "Y Direction", - interval [ aZmin,aZmax ] in the "Z Direction";

        Adds a point of coordinates (X,Y,Z) to this bounding box.
        """
    @overload
    def Update(self,X : float,Y : float,Z : float) -> None: ...
    @overload
    def __init__(self,theMin : OCP.gp.gp_Pnt,theMax : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bnd_Box2d():
    """
    Describes a bounding box in 2D space. A bounding box is parallel to the axes of the coordinates system. If it is finite, it is defined by the two intervals: - [ Xmin,Xmax ], and - [ Ymin,Ymax ]. A bounding box may be infinite (i.e. open) in one or more directions. It is said to be: - OpenXmin if it is infinite on the negative side of the "X Direction"; - OpenXmax if it is infinite on the positive side of the "X Direction"; - OpenYmin if it is infinite on the negative side of the "Y Direction"; - OpenYmax if it is infinite on the positive side of the "Y Direction"; - WholeSpace if it is infinite in all four directions. In this case, any point of the space is inside the box; - Void if it is empty. In this case, there is no point included in the box. A bounding box is defined by four bounds (Xmin, Xmax, Ymin and Ymax) which limit the bounding box if it is finite, six flags (OpenXmin, OpenXmax, OpenYmin, OpenYmax, WholeSpace and Void) which describe the bounding box if it is infinite or empty, and - a gap, which is included on both sides in any direction when consulting the finite bounds of the box.
    """
    @overload
    def Add(self,Other : Bnd_Box2d) -> None: 
        """
        Adds the 2d box <Other> to <me>.

        Adds the 2d point.

        Extends bounding box from thePnt in the direction theDir.

        Extends the Box in the given Direction, i.e. adds a half-line. The box may become infinite in 1 or 2 directions.
        """
    @overload
    def Add(self,D : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt2d,theDir : OCP.gp.gp_Dir2d) -> None: ...
    @overload
    def Add(self,thePnt : OCP.gp.gp_Pnt2d) -> None: ...
    def Dump(self) -> None: 
        """
        None
        """
    def Enlarge(self,theTol : float) -> None: 
        """
        Enlarges the box with a tolerance value. This means that the minimum values of its X and Y intervals of definition, when they are finite, are reduced by the absolute value of Tol, while the maximum values are increased by the same amount.
        """
    def Get(self) -> Tuple[float, float, float, float]: 
        """
        Returns the bounds of this 2D bounding box. The gap is included. If this bounding box is infinite (i.e. "open"), returned values may be equal to +/- Precision::Infinite(). if IsVoid()
        """
    def GetGap(self) -> float: 
        """
        Returns the gap of this 2D bounding box.
        """
    def IsOpenXmax(self) -> bool: 
        """
        Returns true if this bounding box is open in the Xmax direction.
        """
    def IsOpenXmin(self) -> bool: 
        """
        Returns true if this bounding box is open in the Xmin direction.
        """
    def IsOpenYmax(self) -> bool: 
        """
        Returns true if this bounding box is open in the Ymax direction.
        """
    def IsOpenYmin(self) -> bool: 
        """
        Returns true if this bounding box is open in the Ymin direction.
        """
    @overload
    def IsOut(self,Other : Bnd_Box2d) -> bool: 
        """
        Returns True if the 2d pnt <P> is out <me>.

        Returns True if the line doesn't intersect the box.

        Returns True if the segment doesn't intersect the box.

        Returns True if <Box2d> is out <me>.

        Returns True if transformed <Box2d> is out <me>.

        Compares a transformed bounding with a transformed bounding. The default implementation is to make a copy of <me> and <Other>, to transform them and to test.
        """
    @overload
    def IsOut(self,P : OCP.gp.gp_Pnt2d) -> bool: ...
    @overload
    def IsOut(self,theL : OCP.gp.gp_Lin2d) -> bool: ...
    @overload
    def IsOut(self,theP0 : OCP.gp.gp_Pnt2d,theP1 : OCP.gp.gp_Pnt2d) -> bool: ...
    @overload
    def IsOut(self,T1 : OCP.gp.gp_Trsf2d,Other : Bnd_Box2d,T2 : OCP.gp.gp_Trsf2d) -> bool: ...
    @overload
    def IsOut(self,theOther : Bnd_Box2d,theTrsf : OCP.gp.gp_Trsf2d) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Returns true if this 2D bounding box is empty (Void flag).
        """
    def IsWhole(self) -> bool: 
        """
        Returns true if this bounding box is infinite in all 4 directions (Whole Space flag).
        """
    def OpenXmax(self) -> None: 
        """
        The Box will be infinitely long in the Xmax direction.
        """
    def OpenXmin(self) -> None: 
        """
        The Box will be infinitely long in the Xmin direction.
        """
    def OpenYmax(self) -> None: 
        """
        The Box will be infinitely long in the Ymax direction.
        """
    def OpenYmin(self) -> None: 
        """
        The Box will be infinitely long in the Ymin direction.
        """
    @overload
    def Set(self,thePnt : OCP.gp.gp_Pnt2d,theDir : OCP.gp.gp_Dir2d) -> None: 
        """
        Sets this 2D bounding box so that it bounds the point P. This involves first setting this bounding box to be void and then adding the point PThe rectangle bounds the point <P>.

        Sets this 2D bounding box so that it bounds the half-line defined by point P and direction D, i.e. all points M defined by M=P+u*D, where u is greater than or equal to 0, are inside the bounding area. This involves first setting this 2D box to be void and then adding the half-line.
        """
    @overload
    def Set(self,thePnt : OCP.gp.gp_Pnt2d) -> None: ...
    def SetGap(self,Tol : float) -> None: 
        """
        Set the gap of this 2D bounding box to abs(Tol).
        """
    def SetVoid(self) -> None: 
        """
        Sets this 2D bounding box so that it is empty. All points are outside a void box.
        """
    def SetWhole(self) -> None: 
        """
        Sets this bounding box so that it covers the whole 2D space, i.e. it is infinite in all directions.
        """
    def SquareExtent(self) -> float: 
        """
        Computes the squared diagonal of me.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf2d) -> Bnd_Box2d: 
        """
        Returns a bounding box which is the result of applying the transformation T to this bounding box. Warning Applying a geometric transformation (for example, a rotation) to a bounding box generally increases its dimensions. This is not optimal for algorithms which use it.
        """
    @overload
    def Update(self,X : float,Y : float) -> None: 
        """
        Enlarges this 2D bounding box, if required, so that it contains at least: - interval [ aXmin,aXmax ] in the "X Direction", - interval [ aYmin,aYmax ] in the "Y Direction"

        Adds a point of coordinates (X,Y) to this bounding box.
        """
    @overload
    def Update(self,aXmin : float,aYmin : float,aXmax : float,aYmax : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class Bnd_HArray1OfBox(Bnd_Array1OfBox, OCP.Standard.Standard_Transient):
    def Array1(self) -> Bnd_Array1OfBox: 
        """
        None
        """
    def Assign(self,theOther : Bnd_Array1OfBox) -> Bnd_Array1OfBox: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Bnd_Array1OfBox: 
        """
        None
        """
    def ChangeFirst(self) -> Bnd_Box: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Box: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Box: 
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
    def First(self) -> Bnd_Box: 
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
    def Init(self,theValue : Bnd_Box) -> None: 
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
    def Last(self) -> Bnd_Box: 
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
    def Move(self,theOther : Bnd_Array1OfBox) -> Bnd_Array1OfBox: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Box) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Box: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Bnd_Box) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Bnd_Array1OfBox) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class Bnd_HArray1OfBox2d(Bnd_Array1OfBox2d, OCP.Standard.Standard_Transient):
    def Array1(self) -> Bnd_Array1OfBox2d: 
        """
        None
        """
    def Assign(self,theOther : Bnd_Array1OfBox2d) -> Bnd_Array1OfBox2d: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Bnd_Array1OfBox2d: 
        """
        None
        """
    def ChangeFirst(self) -> Bnd_Box2d: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Box2d: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Box2d: 
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
    def First(self) -> Bnd_Box2d: 
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
    def Init(self,theValue : Bnd_Box2d) -> None: 
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
    def Last(self) -> Bnd_Box2d: 
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
    def Move(self,theOther : Bnd_Array1OfBox2d) -> Bnd_Array1OfBox2d: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Box2d) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Box2d: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Bnd_Box2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Bnd_Array1OfBox2d) -> None: ...
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
class Bnd_HArray1OfSphere(Bnd_Array1OfSphere, OCP.Standard.Standard_Transient):
    def Array1(self) -> Bnd_Array1OfSphere: 
        """
        None
        """
    def Assign(self,theOther : Bnd_Array1OfSphere) -> Bnd_Array1OfSphere: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Bnd_Array1OfSphere: 
        """
        None
        """
    def ChangeFirst(self) -> Bnd_Sphere: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Bnd_Sphere: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Bnd_Sphere: 
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
    def First(self) -> Bnd_Sphere: 
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
    def Init(self,theValue : Bnd_Sphere) -> None: 
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
    def Last(self) -> Bnd_Sphere: 
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
    def Move(self,theOther : Bnd_Array1OfSphere) -> Bnd_Array1OfSphere: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Bnd_Sphere) -> None: 
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
    def Value(self,theIndex : int) -> Bnd_Sphere: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Bnd_Sphere) -> None: ...
    @overload
    def __init__(self,theOther : Bnd_Array1OfSphere) -> None: ...
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
class Bnd_OBB():
    """
    The class describes the Oriented Bounding Box (OBB), much tighter enclosing volume for the shape than the Axis Aligned Bounding Box (AABB). The OBB is defined by a center of the box, the axes and the halves of its three dimensions. The OBB can be used more effectively than AABB as a rejection mechanism for non-interfering objects.
    """
    @overload
    def Add(self,theP : OCP.gp.gp_Pnt) -> None: 
        """
        Rebuilds this in order to include all previous objects (which it was created from) and theOther.

        Rebuilds this in order to include all previous objects (which it was created from) and theP.
        """
    @overload
    def Add(self,theOther : Bnd_OBB) -> None: ...
    def Center(self) -> OCP.gp.gp_XYZ: 
        """
        Returns the center of OBB
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Enlarge(self,theGapAdd : float) -> None: 
        """
        Enlarges the box with the given value
        """
    def GetVertex(self,theP : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns the array of vertices in <this>. The local coordinate of the vertex depending on the index of the array are follow: Index == 0: (-XHSize(), -YHSize(), -ZHSize()) Index == 1: ( XHSize(), -YHSize(), -ZHSize()) Index == 2: (-XHSize(), YHSize(), -ZHSize()) Index == 3: ( XHSize(), YHSize(), -ZHSize()) Index == 4: (-XHSize(), -YHSize(), ZHSize()) Index == 5: ( XHSize(), -YHSize(), ZHSize()) Index == 6: (-XHSize(), YHSize(), ZHSize()) Index == 7: ( XHSize(), YHSize(), ZHSize()).
        """
    def IsAABox(self) -> bool: 
        """
        Returns TRUE if the box is axes aligned
        """
    def IsCompletelyInside(self,theOther : Bnd_OBB) -> bool: 
        """
        Check if the theOther is completely inside *this.
        """
    @overload
    def IsOut(self,theOther : Bnd_OBB) -> bool: 
        """
        Check if the box do not interfere the other box.

        Check if the point is inside of <this>.
        """
    @overload
    def IsOut(self,theP : OCP.gp.gp_Pnt) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Checks if the box is empty.
        """
    def Position(self) -> OCP.gp.gp_Ax3: 
        """
        Returns the local coordinates system of this oriented box. So that applying it to axis-aligned box ((-XHSize, -YHSize, -ZHSize), (XHSize, YHSize, ZHSize)) will produce this oriented box.
        """
    def ReBuild(self,theListOfPoints : OCP.TColgp.TColgp_Array1OfPnt,theListOfTolerances : OCP.TColStd.TColStd_Array1OfReal=None,theIsOptimal : bool=False) -> None: 
        """
        Creates new OBB covering every point in theListOfPoints. Tolerance of every such point is set by *theListOfTolerances array. If this array is not void (not null-pointer) then the resulted Bnd_OBB will be enlarged using tolerances of points lying on the box surface. <theIsOptimal> flag defines the mode in which the OBB will be built. Constructing Optimal box takes more time, but the resulting box is usually more tight. In case of construction of Optimal OBB more possible axes are checked.
        """
    def SetAABox(self,theFlag : bool) -> None: 
        """
        Sets the flag for axes aligned box
        """
    def SetCenter(self,theCenter : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the center of OBB
        """
    def SetVoid(self) -> None: 
        """
        Clears this box
        """
    def SetXComponent(self,theXDirection : OCP.gp.gp_Dir,theHXSize : float) -> None: 
        """
        Sets the X component of OBB - direction and size
        """
    def SetYComponent(self,theYDirection : OCP.gp.gp_Dir,theHYSize : float) -> None: 
        """
        Sets the Y component of OBB - direction and size
        """
    def SetZComponent(self,theZDirection : OCP.gp.gp_Dir,theHZSize : float) -> None: 
        """
        Sets the Z component of OBB - direction and size
        """
    def SquareExtent(self) -> float: 
        """
        Returns square diagonal of this box
        """
    def XDirection(self) -> OCP.gp.gp_XYZ: 
        """
        Returns the X Direction of OBB
        """
    def XHSize(self) -> float: 
        """
        Returns the X Dimension of OBB
        """
    def YDirection(self) -> OCP.gp.gp_XYZ: 
        """
        Returns the Y Direction of OBB
        """
    def YHSize(self) -> float: 
        """
        Returns the Y Dimension of OBB
        """
    def ZDirection(self) -> OCP.gp.gp_XYZ: 
        """
        Returns the Z Direction of OBB
        """
    def ZHSize(self) -> float: 
        """
        Returns the Z Dimension of OBB
        """
    @overload
    def __init__(self,theBox : Bnd_Box) -> None: ...
    @overload
    def __init__(self,theCenter : OCP.gp.gp_Pnt,theXDirection : OCP.gp.gp_Dir,theYDirection : OCP.gp.gp_Dir,theZDirection : OCP.gp.gp_Dir,theHXSize : float,theHYSize : float,theHZSize : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bnd_Range():
    """
    This class describes a range in 1D space restricted by two real values. A range can be void indicating there is no point included in the range.
    """
    @overload
    def Add(self,theRange : Bnd_Range) -> None: 
        """
        Extends <this> to include theParameter

        Extends this range to include both ranges.
        """
    @overload
    def Add(self,theParameter : float) -> None: ...
    def Common(self,theOther : Bnd_Range) -> None: 
        """
        Replaces <this> with common-part of <this> and theOther
        """
    def Delta(self) -> float: 
        """
        Returns range value (MAX-MIN). Returns negative value for VOID range.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def Enlarge(self,theDelta : float) -> None: 
        """
        Extends this to the given value (in both side)
        """
    def GetBounds(self,theFirstPar : float,theLastPar : float) -> bool: 
        """
        Obtain first and last boundary of <this>. If <this> is VOID the method returns false.
        """
    def GetIntermediatePoint(self,theLambda : float,theParameter : float) -> bool: 
        """
        Obtain theParameter satisfied to the equation (theParameter-MIN)/(MAX-MIN) == theLambda. * theLambda == 0 --> MIN boundary will be returned; * theLambda == 0.5 --> Middle point will be returned; * theLambda == 1 --> MAX boundary will be returned; * theLambda < 0 --> the value less than MIN will be returned; * theLambda > 1 --> the value greater than MAX will be returned. If <this> is VOID the method returns false.
        """
    def GetMax(self,thePar : float) -> bool: 
        """
        Obtain MAX boundary of <this>. If <this> is VOID the method returns false.
        """
    def GetMin(self,thePar : float) -> bool: 
        """
        Obtain MIN boundary of <this>. If <this> is VOID the method returns false.
        """
    def IsIntersected(self,theVal : float,thePeriod : float=0.0) -> int: 
        """
        Checks if <this> intersects values like theVal+k*thePeriod, where k is an integer number (k = 0, +/-1, +/-2, ...). Returns: 0 - if <this> does not intersect the theVal+k*thePeriod. 1 - if <this> intersects theVal+k*thePeriod. 2 - if myFirst or/and myLast are equal to theVal+k*thePeriod.
        """
    @overload
    def IsOut(self,theValue : float) -> bool: 
        """
        Returns True if the value is out of this range.

        Returns True if the given range is out of this range.
        """
    @overload
    def IsOut(self,theRange : Bnd_Range) -> bool: ...
    def IsVoid(self) -> bool: 
        """
        Is <this> initialized.
        """
    def SetVoid(self) -> None: 
        """
        Initializes <this> by default parameters. Makes <this> VOID.
        """
    def Shift(self,theVal : float) -> None: 
        """
        Shifts <*this> by theVal
        """
    def Shifted(self,theVal : float) -> Bnd_Range: 
        """
        Returns the copy of <*this> shifted by theVal
        """
    def Split(self,theVal : float,theList : Any,thePeriod : float=0.0) -> None: 
        """
        Splits <this> to several sub-ranges by theVal value (e.g. range [3, 15] will be split by theVal==5 to the two ranges: [3, 5] and [5, 15]). New ranges will be pushed to theList (theList must be initialized correctly before calling this method). If thePeriod != 0.0 then at least one boundary of new ranges (if <*this> intersects theVal+k*thePeriod) will be equal to theVal+thePeriod*k, where k is an integer number (k = 0, +/-1, +/-2, ...). (let thePeriod in above example be 4 ==> we will obtain four ranges: [3, 5], [5, 9], [9, 13] and [13, 15].
        """
    def TrimFrom(self,theValLower : float) -> None: 
        """
        Trims the First value in range by the given lower limit. Marks range as Void if the given Lower value is greater than range Max.
        """
    def TrimTo(self,theValUpper : float) -> None: 
        """
        Trim the Last value in range by the given Upper limit. Marks range as Void if the given Upper value is smaller than range Max.
        """
    def Union(self,theOther : Bnd_Range) -> bool: 
        """
        Joins *this and theOther to one interval. Replaces *this to the result. Returns false if the operation cannot be done (e.g. input arguments are empty or separated).
        """
    @overload
    def __init__(self,theMin : float,theMax : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bnd_Sphere():
    """
    This class represents a bounding sphere of a geometric entity (triangle, segment of line or whatever else).
    """
    def Add(self,theOther : Bnd_Sphere) -> None: 
        """
        None
        """
    def Center(self) -> OCP.gp.gp_XYZ: 
        """
        Returns center of sphere object

        Returns center of sphere object
        """
    def Distance(self,theNode : OCP.gp.gp_XYZ) -> float: 
        """
        None
        """
    def Distances(self,theXYZ : OCP.gp.gp_XYZ) -> Tuple[float, float]: 
        """
        Calculate and return minimal and maximal distance to sphere. NOTE: This function is tightly optimized; any modifications may affect performance!
        """
    @overload
    def IsOut(self,theOther : Bnd_Sphere) -> bool: 
        """
        None

        None
        """
    @overload
    def IsOut(self,thePnt : OCP.gp.gp_XYZ,theMaxDist : float) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Returns validity status, indicating that this sphere corresponds to a real entity

        Returns validity status, indicating that this sphere corresponds to a real entity
        """
    def Project(self,theNode : OCP.gp.gp_XYZ,theProjNode : OCP.gp.gp_XYZ,theDist : float,theInside : bool) -> bool: 
        """
        Projects a point on entity. Returns true if success
        """
    def Radius(self) -> float: 
        """
        Returns the radius value

        Returns the radius value
        """
    def SetValid(self,isValid : bool) -> None: 
        """
        None

        None
        """
    def SquareDistance(self,theNode : OCP.gp.gp_XYZ) -> float: 
        """
        None
        """
    def SquareDistances(self,theXYZ : OCP.gp.gp_XYZ) -> Tuple[float, float]: 
        """
        Calculate and return minimal and maximal distance to sphere. NOTE: This function is tightly optimized; any modifications may affect performance!
        """
    def SquareExtent(self) -> float: 
        """
        None
        """
    def U(self) -> int: 
        """
        Returns the U parameter on shape

        Returns the U parameter on shape
        """
    def V(self) -> int: 
        """
        Returns the V parameter on shape

        Returns the V parameter on shape
        """
    @overload
    def __init__(self,theCntr : OCP.gp.gp_XYZ,theRad : float,theU : int,theV : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Bnd_Tools():
    """
    Defines a set of static methods operating with bounding boxes
    """
    @staticmethod
    @overload
    def Bnd2BVH_s(theBox : Bnd_Box) -> Any: 
        """
        Converts the given Bnd_Box2d to BVH_Box

        Converts the given Bnd_Box to BVH_Box
        """
    @staticmethod
    @overload
    def Bnd2BVH_s(theBox : Bnd_Box2d) -> Any: ...
    def __init__(self) -> None: ...
    pass
