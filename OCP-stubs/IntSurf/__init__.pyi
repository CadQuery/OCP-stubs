import OCP.IntSurf
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Adaptor3d
import OCP.GeomAbs
import OCP.NCollection
import OCP.gp
import OCP.Standard
__all__  = [
"IntSurf",
"IntSurf_Couple",
"IntSurf_InteriorPoint",
"IntSurf_InteriorPointTool",
"IntSurf_LineOn2S",
"IntSurf_ListOfPntOn2S",
"IntSurf_PathPoint",
"IntSurf_PathPointTool",
"IntSurf_PntOn2S",
"IntSurf_Quadric",
"IntSurf_QuadricTool",
"IntSurf_SequenceOfCouple",
"IntSurf_SequenceOfInteriorPoint",
"IntSurf_SequenceOfPathPoint",
"IntSurf_SequenceOfPntOn2S",
"IntSurf_Situation",
"IntSurf_Transition",
"IntSurf_TypeTrans",
"IntSurf_In",
"IntSurf_Inside",
"IntSurf_Out",
"IntSurf_Outside",
"IntSurf_Touch",
"IntSurf_Undecided",
"IntSurf_Unknown"
]
class IntSurf():
    """
    This package provides resources for all the packages concerning the intersection between surfaces.
    """
    @staticmethod
    def MakeTransition_s(TgFirst : OCP.gp.gp_Vec,TgSecond : OCP.gp.gp_Vec,Normal : OCP.gp.gp_Dir,TFirst : IntSurf_Transition,TSecond : IntSurf_Transition) -> None: 
        """
        Computes the transition of the intersection point between the two lines. TgFirst is the tangent vector of the first line. TgSecond is the tangent vector of the second line. Normal is the direction used to orientate the cross product TgFirst^TgSecond. TFirst is the transition of the point on the first line. TSecond is the transition of the point on the second line.
        """
    @staticmethod
    def SetPeriod_s(theFirstSurf : OCP.Adaptor3d.Adaptor3d_Surface,theSecondSurf : OCP.Adaptor3d.Adaptor3d_Surface,theArrOfPeriod : float) -> None: 
        """
        Fills theArrOfPeriod array by the period values of theFirstSurf and theSecondSurf. [0] = U-period of theFirstSurf, [1] = V-period of theFirstSurf, [2] = U-period of theSecondSurf, [3] = V-period of theSecondSurf.
        """
    def __init__(self) -> None: ...
    pass
class IntSurf_Couple():
    """
    creation d 'un couple de 2 entiers
    """
    def First(self) -> int: 
        """
        returns the first element

        returns the first element
        """
    def Second(self) -> int: 
        """
        returns the Second element

        returns the Second element
        """
    @overload
    def __init__(self,Index1 : int,Index2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntSurf_InteriorPoint():
    """
    Definition of a point solution of the intersection between an implicit an a parametrised surface. These points are passing points on the intersection lines, or starting points for the closed lines on the parametrised surface.
    """
    def Direction(self) -> OCP.gp.gp_Vec: 
        """
        Returns the tangent at the intersection in 3d space associated to the interior point.

        Returns the tangent at the intersection in 3d space associated to the interior point.
        """
    def Direction2d(self) -> OCP.gp.gp_Vec2d: 
        """
        Returns the tangent at the intersection in the parametric space of the parametric surface.

        Returns the tangent at the intersection in the parametric space of the parametric surface.
        """
    def Parameters(self) -> Tuple[float, float]: 
        """
        Returns the parameters of the interior point on the parametric surface.

        Returns the parameters of the interior point on the parametric surface.
        """
    def SetValue(self,P : OCP.gp.gp_Pnt,U : float,V : float,Direc : OCP.gp.gp_Vec,Direc2d : OCP.gp.gp_Vec2d) -> None: 
        """
        None
        """
    def UParameter(self) -> float: 
        """
        Returns the first parameter of the interior point on the parametric surface.

        Returns the first parameter of the interior point on the parametric surface.
        """
    def VParameter(self) -> float: 
        """
        Returns the second parameter of the interior point on the parametric surface.

        Returns the second parameter of the interior point on the parametric surface.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d coordinates of the interior point.

        Returns the 3d coordinates of the interior point.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,U : float,V : float,Direc : OCP.gp.gp_Vec,Direc2d : OCP.gp.gp_Vec2d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntSurf_InteriorPointTool():
    """
    This class provides a tool on the "interior point" that can be used to instantiates the Walking algorithms (see package IntWalk).
    """
    @staticmethod
    def Direction2d_s(PStart : IntSurf_InteriorPoint) -> OCP.gp.gp_Dir2d: 
        """
        returns the tangent at the intersectin in the parametric space of the parametrized surface.This tangent is associated to the value2d
        """
    @staticmethod
    def Direction3d_s(PStart : IntSurf_InteriorPoint) -> OCP.gp.gp_Vec: 
        """
        returns the tangent at the intersectin in 3d space associated to <P>
        """
    @staticmethod
    def Value2d_s(PStart : IntSurf_InteriorPoint) -> Tuple[float, float]: 
        """
        Returns the <U,V> parameters which are associated with <P> it's the parameters which start the marching algorithm
        """
    @staticmethod
    def Value3d_s(PStart : IntSurf_InteriorPoint) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d coordinates of the starting point.
        """
    def __init__(self) -> None: ...
    pass
class IntSurf_LineOn2S(OCP.Standard.Standard_Transient):
    def Add(self,P : IntSurf_PntOn2S) -> None: 
        """
        Adds a point in the line.
        """
    def Clear(self) -> None: 
        """
        None

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
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertBefore(self,I : int,P : IntSurf_PntOn2S) -> None: 
        """
        None
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
    def IsOutBox(self,theP : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns TRUE if theP is out of the box built from 3D-points.
        """
    def IsOutSurf1Box(self,theP : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns TRUE if theP is out of the box built from the points on 1st surface
        """
    def IsOutSurf2Box(self,theP : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns TRUE if theP is out of the box built from the points on 2nd surface
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points in the line.

        Returns the number of points in the line.
        """
    def RemovePoint(self,I : int) -> None: 
        """
        None
        """
    def Reverse(self) -> None: 
        """
        Reverses the order of points of the line.

        Reverses the order of points of the line.
        """
    def SetPoint(self,Index : int,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the 3D point of the Index-th PntOn2S

        Sets the 3D point of the Index-th PntOn2S
        """
    def SetUV(self,Index : int,OnFirst : bool,U : float,V : float) -> None: 
        """
        Sets the parametric coordinates on one of the surfaces of the point of range Index in the line.
        """
    def Split(self,Index : int) -> IntSurf_LineOn2S: 
        """
        Keeps in <me> the points 1 to Index-1, and returns the items Index to the end.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Value(self,Index : int) -> IntSurf_PntOn2S: 
        """
        Returns the point of range Index in the line.

        Replaces the point of range Index in the line.

        Returns the point of range Index in the line.

        Replaces the point of range Index in the line.
        """
    @overload
    def Value(self,Index : int,P : IntSurf_PntOn2S) -> None: ...
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
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
class IntSurf_ListOfPntOn2S(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntSurf_PntOn2S,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : IntSurf_PntOn2S) -> IntSurf_PntOn2S: ...
    @overload
    def Append(self,theOther : IntSurf_ListOfPntOn2S) -> None: ...
    def Assign(self,theOther : IntSurf_ListOfPntOn2S) -> IntSurf_ListOfPntOn2S: 
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
    def First(self) -> IntSurf_PntOn2S: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IntSurf_ListOfPntOn2S,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : IntSurf_PntOn2S,theIter : Any) -> IntSurf_PntOn2S: ...
    @overload
    def InsertBefore(self,theOther : IntSurf_ListOfPntOn2S,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : IntSurf_PntOn2S,theIter : Any) -> IntSurf_PntOn2S: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IntSurf_PntOn2S: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : IntSurf_PntOn2S) -> IntSurf_PntOn2S: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : IntSurf_ListOfPntOn2S) -> None: ...
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
    def __init__(self,theOther : IntSurf_ListOfPntOn2S) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class IntSurf_PathPoint():
    """
    None
    """
    def AddUV(self,U : float,V : float) -> None: 
        """
        None

        None
        """
    def Direction2d(self) -> OCP.gp.gp_Dir2d: 
        """
        None

        None
        """
    def Direction3d(self) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    def IsPassingPnt(self) -> bool: 
        """
        None

        None
        """
    def IsTangent(self) -> bool: 
        """
        None

        None
        """
    def Multiplicity(self) -> int: 
        """
        None

        None
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None

        None
        """
    def SetDirections(self,V : OCP.gp.gp_Vec,D : OCP.gp.gp_Dir2d) -> None: 
        """
        None

        None
        """
    def SetPassing(self,Pass : bool) -> None: 
        """
        None

        None
        """
    def SetTangency(self,Tang : bool) -> None: 
        """
        None

        None
        """
    def SetValue(self,P : OCP.gp.gp_Pnt,U : float,V : float) -> None: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def Value2d(self) -> Tuple[float, float]: 
        """
        None

        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,U : float,V : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntSurf_PathPointTool():
    """
    None
    """
    @staticmethod
    def Direction2d_s(PStart : IntSurf_PathPoint) -> OCP.gp.gp_Dir2d: 
        """
        returns the tangent at the intersection in the parametric space of the parametrized surface.This tangent is associated to the value2d la tangente a un sens signifiant (indique le sens de chemin ement) an exception is raised if IsTangent is true.
        """
    @staticmethod
    def Direction3d_s(PStart : IntSurf_PathPoint) -> OCP.gp.gp_Vec: 
        """
        returns the tangent at the intersection in 3d space associated to <P> an exception is raised if IsTangent is true.
        """
    @staticmethod
    def IsPassingPnt_s(PStart : IntSurf_PathPoint) -> bool: 
        """
        Returns True if the point is a point on a non-oriented arc, which means that the intersection line does not stop at such a point but just go through such a point. IsPassingPnt is True when IsOnArc is True
        """
    @staticmethod
    def IsTangent_s(PStart : IntSurf_PathPoint) -> bool: 
        """
        Returns True if the surfaces are tangent at this point. IsTangent can be True when IsOnArc is True if IsPassingPnt is True and IsTangent is True,this point is a stopped point.
        """
    @staticmethod
    def Multiplicity_s(PStart : IntSurf_PathPoint) -> int: 
        """
        Returns the multiplicity of the point i-e the number of auxillar parameters associated to the point which the principal parameters are given by Value2d
        """
    @staticmethod
    def Parameters_s(PStart : IntSurf_PathPoint,Mult : int) -> Tuple[float, float]: 
        """
        Parametric coordinates associated to the multiplicity. An exception is raised if Mult<=0 or Mult>multiplicity.
        """
    @staticmethod
    def Value2d_s(PStart : IntSurf_PathPoint) -> Tuple[float, float]: 
        """
        Returns the <U, V> parameters which are associated with <P> it's the parameters which start the marching algorithm
        """
    @staticmethod
    def Value3d_s(PStart : IntSurf_PathPoint) -> OCP.gp.gp_Pnt: 
        """
        Returns the 3d coordinates of the starting point.
        """
    def __init__(self) -> None: ...
    pass
class IntSurf_PntOn2S():
    """
    This class defines the geometric information for an intersection point between 2 surfaces : The coordinates ( Pnt from gp ), and two parametric coordinates.
    """
    def IsSame(self,theOtherPoint : IntSurf_PntOn2S,theTol3D : float=0.0,theTol2D : float=-1.0) -> bool: 
        """
        Returns TRUE if 2D- and 3D-coordinates of theOterPoint are equal to corresponding coordinates of me (with given tolerance). If theTol2D < 0.0 we will compare 3D-points only.
        """
    def Parameters(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parameters of the point on both surfaces.

        Returns the parameters of the point on both surfaces.
        """
    def ParametersOnS1(self) -> Tuple[float, float]: 
        """
        Returns the parameters of the point on the first surface.

        Returns the parameters of the point on the first surface.
        """
    def ParametersOnS2(self) -> Tuple[float, float]: 
        """
        Returns the parameters of the point on the second surface.

        Returns the parameters of the point on the second surface.
        """
    def ParametersOnSurface(self,OnFirst : bool) -> Tuple[float, float]: 
        """
        Returns the parameters of the point in the parametric space of one of the surface.
        """
    @overload
    def SetValue(self,Pt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the value of the point in 3d space.

        Sets the values of the point in 3d space, and in the parametric space of one of the surface.

        Sets the values of the point in 3d space, and in the parametric space of each surface.

        Set the values of the point in the parametric space of one of the surface.

        Set the values of the point in the parametric space of one of the surface.

        Sets the value of the point in 3d space.

        Sets the values of the point in 3d space, and in the parametric space of each surface.

        Set the values of the point in the parametric space of one of the surface.
        """
    @overload
    def SetValue(self,Pt : OCP.gp.gp_Pnt,OnFirst : bool,U : float,V : float) -> None: ...
    @overload
    def SetValue(self,U1 : float,V1 : float,U2 : float,V2 : float) -> None: ...
    @overload
    def SetValue(self,Pt : OCP.gp.gp_Pnt,U1 : float,V1 : float,U2 : float,V2 : float) -> None: ...
    @overload
    def SetValue(self,OnFirst : bool,U : float,V : float) -> None: ...
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point in 3d space.

        Returns the point in 3d space.
        """
    def ValueOnSurface(self,OnFirst : bool) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the point in 2d space of one of the surfaces.
        """
    def __init__(self) -> None: ...
    pass
class IntSurf_Quadric():
    """
    None
    """
    def Cone(self) -> OCP.gp.gp_Cone: 
        """
        None

        None
        """
    def Cylinder(self) -> OCP.gp.gp_Cylinder: 
        """
        None

        None
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def Distance(self,P : OCP.gp.gp_Pnt) -> float: 
        """
        None
        """
    def Gradient(self,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Vec: 
        """
        None
        """
    @overload
    def Normale(self,U : float,V : float) -> OCP.gp.gp_Vec: 
        """
        None

        None
        """
    @overload
    def Normale(self,P : OCP.gp.gp_Pnt) -> OCP.gp.gp_Vec: ...
    def Parameters(self,P : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        None
        """
    def Plane(self) -> OCP.gp.gp_Pln: 
        """
        None

        None
        """
    @overload
    def SetValue(self,T : OCP.gp.gp_Torus) -> None: 
        """
        None

        None

        None

        None

        None
        """
    @overload
    def SetValue(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def SetValue(self,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def SetValue(self,C : OCP.gp.gp_Cylinder) -> None: ...
    @overload
    def SetValue(self,P : OCP.gp.gp_Pln) -> None: ...
    def Sphere(self) -> OCP.gp.gp_Sphere: 
        """
        None

        None
        """
    def Torus(self) -> OCP.gp.gp_Torus: 
        """
        None

        None
        """
    def TypeQuadric(self) -> OCP.GeomAbs.GeomAbs_SurfaceType: 
        """
        None

        None
        """
    def ValAndGrad(self,P : OCP.gp.gp_Pnt,Grad : OCP.gp.gp_Vec) -> Tuple[float]: 
        """
        None
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def __init__(self,T : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder) -> None: ...
    pass
class IntSurf_QuadricTool():
    """
    This class provides a tool on a quadric that can be used to instantiates the Walking algorithms (see package IntWalk) with a Quadric from IntSurf as implicit surface.
    """
    @staticmethod
    def Gradient_s(Quad : IntSurf_Quadric,X : float,Y : float,Z : float,V : OCP.gp.gp_Vec) -> None: 
        """
        Returns the gradient of the function.
        """
    @staticmethod
    def Tolerance_s(Quad : IntSurf_Quadric) -> float: 
        """
        returns the tolerance of the zero of the implicit function
        """
    @staticmethod
    def ValueAndGradient_s(Quad : IntSurf_Quadric,X : float,Y : float,Z : float,Grad : OCP.gp.gp_Vec) -> Tuple[float]: 
        """
        Returns the value and the gradient.
        """
    @staticmethod
    def Value_s(Quad : IntSurf_Quadric,X : float,Y : float,Z : float) -> float: 
        """
        Returns the value of the function.
        """
    def __init__(self) -> None: ...
    pass
class IntSurf_SequenceOfCouple(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntSurf_Couple) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntSurf_SequenceOfCouple) -> None: ...
    def Assign(self,theOther : IntSurf_SequenceOfCouple) -> IntSurf_SequenceOfCouple: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntSurf_Couple: 
        """
        First item access
        """
    def ChangeLast(self) -> IntSurf_Couple: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntSurf_Couple: 
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
    def First(self) -> IntSurf_Couple: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntSurf_SequenceOfCouple) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntSurf_Couple) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntSurf_SequenceOfCouple) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntSurf_Couple) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntSurf_Couple: 
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
    def Prepend(self,theItem : IntSurf_Couple) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntSurf_SequenceOfCouple) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntSurf_Couple) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntSurf_SequenceOfCouple) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntSurf_Couple: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntSurf_SequenceOfCouple) -> None: ...
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
class IntSurf_SequenceOfInteriorPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntSurf_SequenceOfInteriorPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntSurf_InteriorPoint) -> None: ...
    def Assign(self,theOther : IntSurf_SequenceOfInteriorPoint) -> IntSurf_SequenceOfInteriorPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntSurf_InteriorPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> IntSurf_InteriorPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntSurf_InteriorPoint: 
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
    def First(self) -> IntSurf_InteriorPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntSurf_SequenceOfInteriorPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntSurf_InteriorPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntSurf_SequenceOfInteriorPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntSurf_InteriorPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntSurf_InteriorPoint: 
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
    def Prepend(self,theSeq : IntSurf_SequenceOfInteriorPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntSurf_InteriorPoint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntSurf_InteriorPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntSurf_SequenceOfInteriorPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntSurf_InteriorPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntSurf_SequenceOfInteriorPoint) -> None: ...
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
class IntSurf_SequenceOfPathPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntSurf_PathPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntSurf_SequenceOfPathPoint) -> None: ...
    def Assign(self,theOther : IntSurf_SequenceOfPathPoint) -> IntSurf_SequenceOfPathPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntSurf_PathPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> IntSurf_PathPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntSurf_PathPoint: 
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
    def First(self) -> IntSurf_PathPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntSurf_SequenceOfPathPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntSurf_PathPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntSurf_SequenceOfPathPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntSurf_PathPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntSurf_PathPoint: 
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
    def Prepend(self,theSeq : IntSurf_SequenceOfPathPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntSurf_PathPoint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntSurf_PathPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntSurf_SequenceOfPathPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntSurf_PathPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntSurf_SequenceOfPathPoint) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntSurf_SequenceOfPntOn2S(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntSurf_PntOn2S) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntSurf_SequenceOfPntOn2S) -> None: ...
    def Assign(self,theOther : IntSurf_SequenceOfPntOn2S) -> IntSurf_SequenceOfPntOn2S: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntSurf_PntOn2S: 
        """
        First item access
        """
    def ChangeLast(self) -> IntSurf_PntOn2S: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntSurf_PntOn2S: 
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
    def First(self) -> IntSurf_PntOn2S: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntSurf_SequenceOfPntOn2S) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntSurf_PntOn2S) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntSurf_PntOn2S) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntSurf_SequenceOfPntOn2S) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntSurf_PntOn2S: 
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
    def Prepend(self,theItem : IntSurf_PntOn2S) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntSurf_SequenceOfPntOn2S) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntSurf_PntOn2S) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntSurf_SequenceOfPntOn2S) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntSurf_PntOn2S: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntSurf_SequenceOfPntOn2S) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntSurf_Situation():
    """
    None

    Members:

      IntSurf_Inside

      IntSurf_Outside

      IntSurf_Unknown
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    IntSurf_Inside: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Inside: 0>
    IntSurf_Outside: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Outside: 1>
    IntSurf_Unknown: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Unknown: 2>
    __entries: dict # value = {'IntSurf_Inside': (<IntSurf_Situation.IntSurf_Inside: 0>, None), 'IntSurf_Outside': (<IntSurf_Situation.IntSurf_Outside: 1>, None), 'IntSurf_Unknown': (<IntSurf_Situation.IntSurf_Unknown: 2>, None)}
    __members__: dict # value = {'IntSurf_Inside': <IntSurf_Situation.IntSurf_Inside: 0>, 'IntSurf_Outside': <IntSurf_Situation.IntSurf_Outside: 1>, 'IntSurf_Unknown': <IntSurf_Situation.IntSurf_Unknown: 2>}
    pass
class IntSurf_Transition():
    """
    Definition of the transition at the intersection between an intersection line and a restriction curve on a surface.
    """
    def IsOpposite(self) -> bool: 
        """
        returns a significant value if TransitionType returns TOUCH. In this case, the function returns true when the 2 curves locally define two different parts of the space. If TransitionType returns IN or OUT or UNDECIDED, an exception is raised.

        returns a significant value if TransitionType returns TOUCH. In this case, the function returns true when the 2 curves locally define two different parts of the space. If TransitionType returns IN or OUT or UNDECIDED, an exception is raised.
        """
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the point is tangent to the arc given by Value. An exception is raised if TransitionType returns UNDECIDED.

        Returns TRUE if the point is tangent to the arc given by Value. An exception is raised if TransitionType returns UNDECIDED.
        """
    @overload
    def SetValue(self) -> None: 
        """
        Set the values of an IN or OUT transition.

        Set the values of a TOUCH transition.

        Set the values of an UNDECIDED transition.

        Set the values of an IN or OUT transition.

        Set the values of a TOUCH transition.

        Set the values of an UNDECIDED transition.
        """
    @overload
    def SetValue(self,Tangent : bool,Type : IntSurf_TypeTrans) -> None: ...
    @overload
    def SetValue(self,Tangent : bool,Situ : IntSurf_Situation,Oppos : bool) -> None: ...
    def Situation(self) -> IntSurf_Situation: 
        """
        Returns a significant value if TransitionType returns TOUCH. In this case, the function returns : INSIDE when the intersection line remains inside the Arc, OUTSIDE when it remains outside the Arc, UNKNOWN when the calsulus cannot give results. If TransitionType returns IN, or OUT, or UNDECIDED, a exception is raised.

        Returns a significant value if TransitionType returns TOUCH. In this case, the function returns : INSIDE when the intersection line remains inside the Arc, OUTSIDE when it remains outside the Arc, UNKNOWN when the calsulus cannot give results. If TransitionType returns IN, or OUT, or UNDECIDED, a exception is raised.
        """
    def TransitionType(self) -> IntSurf_TypeTrans: 
        """
        Returns the type of Transition (in/out/touch/undecided) for the arc given by value. This the transition of the intersection line compared to the Arc of restriction, i-e when the function returns INSIDE for example, it means that the intersection line goes inside the part of plane limited by the arc of restriction.

        Returns the type of Transition (in/out/touch/undecided) for the arc given by value. This the transition of the intersection line compared to the Arc of restriction, i-e when the function returns INSIDE for example, it means that the intersection line goes inside the part of plane limited by the arc of restriction.
        """
    @overload
    def __init__(self,Tangent : bool,Situ : IntSurf_Situation,Oppos : bool) -> None: ...
    @overload
    def __init__(self,Tangent : bool,Type : IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntSurf_TypeTrans():
    """
    None

    Members:

      IntSurf_In

      IntSurf_Out

      IntSurf_Touch

      IntSurf_Undecided
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    IntSurf_In: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_In: 0>
    IntSurf_Out: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Out: 1>
    IntSurf_Touch: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Touch: 2>
    IntSurf_Undecided: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Undecided: 3>
    __entries: dict # value = {'IntSurf_In': (<IntSurf_TypeTrans.IntSurf_In: 0>, None), 'IntSurf_Out': (<IntSurf_TypeTrans.IntSurf_Out: 1>, None), 'IntSurf_Touch': (<IntSurf_TypeTrans.IntSurf_Touch: 2>, None), 'IntSurf_Undecided': (<IntSurf_TypeTrans.IntSurf_Undecided: 3>, None)}
    __members__: dict # value = {'IntSurf_In': <IntSurf_TypeTrans.IntSurf_In: 0>, 'IntSurf_Out': <IntSurf_TypeTrans.IntSurf_Out: 1>, 'IntSurf_Touch': <IntSurf_TypeTrans.IntSurf_Touch: 2>, 'IntSurf_Undecided': <IntSurf_TypeTrans.IntSurf_Undecided: 3>}
    pass
IntSurf_In: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_In: 0>
IntSurf_Inside: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Inside: 0>
IntSurf_Out: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Out: 1>
IntSurf_Outside: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Outside: 1>
IntSurf_Touch: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Touch: 2>
IntSurf_Undecided: OCP.IntSurf.IntSurf_TypeTrans # value = <IntSurf_TypeTrans.IntSurf_Undecided: 3>
IntSurf_Unknown: OCP.IntSurf.IntSurf_Situation # value = <IntSurf_Situation.IntSurf_Unknown: 2>
