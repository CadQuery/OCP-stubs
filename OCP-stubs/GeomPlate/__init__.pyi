import OCP.GeomPlate
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.GeomLProp
import OCP.gp
import OCP.Plate
import OCP.Geom
import OCP.TColStd
import OCP.GeomAbs
import OCP.NCollection
import OCP.Adaptor3d
import OCP.AdvApp2Var
import OCP.Law
import OCP.Geom2d
import OCP.Standard
import OCP.TColGeom2d
import OCP.TColgp
import OCP.Adaptor2d
__all__  = [
"GeomPlate_Aij",
"GeomPlate_Array1OfHCurve",
"GeomPlate_Array1OfSequenceOfReal",
"GeomPlate_BuildAveragePlane",
"GeomPlate_BuildPlateSurface",
"GeomPlate_CurveConstraint",
"GeomPlate_HArray1OfHCurve",
"GeomPlate_HArray1OfSequenceOfReal",
"GeomPlate_SequenceOfCurveConstraint",
"GeomPlate_SequenceOfPointConstraint",
"GeomPlate_MakeApprox",
"GeomPlate_PlateG0Criterion",
"GeomPlate_PlateG1Criterion",
"GeomPlate_PointConstraint",
"GeomPlate_SequenceOfAij",
"GeomPlate_HSequenceOfCurveConstraint",
"GeomPlate_HSequenceOfPointConstraint",
"GeomPlate_Surface"
]
class GeomPlate_Aij():
    """
    A structure containing indexes of two normals and its cross product
    """
    @overload
    def __init__(self,anInd1 : int,anInd2 : int,aVec : OCP.gp.gp_Vec) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GeomPlate_Array1OfHCurve():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GeomPlate_Array1OfHCurve) -> GeomPlate_Array1OfHCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Variable value access
        """
    def First(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
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
    def Last(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
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
    def Move(self,theOther : GeomPlate_Array1OfHCurve) -> GeomPlate_Array1OfHCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : OCP.Adaptor3d.Adaptor3d_HCurve,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_Array1OfHCurve) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GeomPlate_Array1OfSequenceOfReal():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Variable value access
        """
    def First(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Returns first element
        """
    def Init(self,theValue : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
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
    def Last(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def Move(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TColStd.TColStd_SequenceOfReal,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GeomPlate_BuildAveragePlane():
    """
    This class computes an average inertial plane with an array of points. Computes the initial surface (average plane) in the cases when the initial surface is not given.
    """
    @staticmethod
    def HalfSpace_s(NewNormals : OCP.TColgp.TColgp_SequenceOfVec,Normals : OCP.TColgp.TColgp_SequenceOfVec,Bset : GeomPlate_SequenceOfAij,LinTol : float,AngTol : float) -> bool: 
        """
        None
        """
    def IsLine(self) -> bool: 
        """
        return OK if is a line.
        """
    def IsPlane(self) -> bool: 
        """
        return OK if is a plane.
        """
    def Line(self) -> OCP.Geom.Geom_Line: 
        """
        Return a Line when 2 eigenvalues are null.
        """
    def MinMaxBox(self) -> Tuple[float, float, float, float]: 
        """
        computes the minimal box to include all normal projection points of the initial array on the plane.
        """
    def Plane(self) -> OCP.Geom.Geom_Plane: 
        """
        Return the average Plane.
        """
    @overload
    def __init__(self,Pts : OCP.TColgp.TColgp_HArray1OfPnt,NbBoundPoints : int,Tol : float,POption : int,NOption : int) -> None: ...
    @overload
    def __init__(self,Normals : OCP.TColgp.TColgp_SequenceOfVec,Pts : OCP.TColgp.TColgp_HArray1OfPnt) -> None: ...
    pass
class GeomPlate_BuildPlateSurface():
    """
    This class provides an algorithm for constructing such a plate surface that it conforms to given curve and/or point constraints. The algorithm accepts or constructs an initial surface and looks for a deformation of it satisfying the constraints and minimizing energy input. A BuildPlateSurface object provides a framework for: - defining or setting constraints - implementing the construction algorithm - consulting the result.
    """
    @overload
    def Add(self,Cont : GeomPlate_PointConstraint) -> None: 
        """
        Adds the linear constraint cont.

        Adds the point constraint cont.
        """
    @overload
    def Add(self,Cont : GeomPlate_CurveConstraint) -> None: ...
    def CurveConstraint(self,order : int) -> GeomPlate_CurveConstraint: 
        """
        returns the CurveConstraints of order order
        """
    def Curves2d(self) -> OCP.TColGeom2d.TColGeom2d_HArray1OfCurve: 
        """
        Extracts the array of curves on the plate surface which correspond to the curve constraints set in Add.
        """
    def Disc2dContour(self,nbp : int,Seq2d : OCP.TColgp.TColgp_SequenceOfXY) -> None: 
        """
        None
        """
    def Disc3dContour(self,nbp : int,iordre : int,Seq3d : OCP.TColgp.TColgp_SequenceOfXYZ) -> None: 
        """
        None
        """
    @overload
    def G0Error(self) -> float: 
        """
        Returns the max distance betwen the result and the constraints

        Returns the max distance between the result and the constraint Index
        """
    @overload
    def G0Error(self,Index : int) -> float: ...
    @overload
    def G1Error(self,Index : int) -> float: 
        """
        Returns the max angle betwen the result and the constraints

        Returns the max angle between the result and the constraint Index
        """
    @overload
    def G1Error(self) -> float: ...
    @overload
    def G2Error(self) -> float: 
        """
        Returns the max difference of curvature betwen the result and the constraints

        Returns the max difference of curvature between the result and the constraint Index
        """
    @overload
    def G2Error(self,Index : int) -> float: ...
    def Init(self) -> None: 
        """
        Resets all constraints
        """
    def IsDone(self) -> bool: 
        """
        Tests whether computation of the plate has been completed.
        """
    def LoadInitSurface(self,Surf : OCP.Geom.Geom_Surface) -> None: 
        """
        Loads the initial Surface
        """
    def Order(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Returns the order of the curves in the array returned by Curves2d. Computation changes this order. Consequently, this method returns the order of the curves prior to computation.
        """
    def Perform(self,aProgress : OCP.Message.Message_ProgressIndicator=None) -> None: 
        """
        Calls the algorithm and computes the plate surface using the loaded constraints. If no initial surface is given, the algorithm automatically computes one. Exceptions Standard_RangeError if the value of the constraint is null or if plate is not done.
        """
    def PointConstraint(self,order : int) -> GeomPlate_PointConstraint: 
        """
        returns the PointConstraint of order order
        """
    def Sense(self) -> OCP.TColStd.TColStd_HArray1OfInteger: 
        """
        Allows you to ensure that the array of curves returned by Curves2d has the correct orientation. Returns the orientation of the curves in the the array returned by Curves2d. Computation changes the orientation of these curves. Consequently, this method returns the orientation prior to computation.
        """
    def SetNbBounds(self,NbBounds : int) -> None: 
        """
        None
        """
    def SurfInit(self) -> OCP.Geom.Geom_Surface: 
        """
        Returns the initial surface
        """
    def Surface(self) -> GeomPlate_Surface: 
        """
        Returns the result of the computation. This surface can then be used by GeomPlate_MakeApprox for converting the resulting surface into a BSpline.
        """
    @overload
    def __init__(self,NPoints : OCP.TColStd.TColStd_HArray1OfInteger,TabCurve : GeomPlate_HArray1OfHCurve,Tang : OCP.TColStd.TColStd_HArray1OfInteger,Degree : int,NbIter : int=3,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1,Anisotropie : bool=False) -> None: ...
    @overload
    def __init__(self,Degree : int=3,NbPtsOnCur : int=10,NbIter : int=3,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1,Anisotropie : bool=False) -> None: ...
    @overload
    def __init__(self,Surf : OCP.Geom.Geom_Surface,Degree : int=3,NbPtsOnCur : int=10,NbIter : int=3,Tol2d : float=1e-05,Tol3d : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1,Anisotropie : bool=False) -> None: ...
    pass
class GeomPlate_CurveConstraint(OCP.Standard.Standard_Transient):
    """
    Defines curves as constraints to be used to deform a surface.Defines curves as constraints to be used to deform a surface.Defines curves as constraints to be used to deform a surface.
    """
    def Curve2dOnSurf(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns a 2d curve associated the surface resulting of the constraints
        """
    def Curve3d(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        None
        """
    def D0(self,U : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec,V4 : OCP.gp.gp_Vec,V5 : OCP.gp.gp_Vec) -> None: 
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
    def FirstParameter(self) -> float: 
        """
        None
        """
    def G0Criterion(self,U : float) -> float: 
        """
        Returns the G0 criterion at the parametric point U on the curve. This is the greatest distance allowed between the constraint and the target surface at U.
        """
    def G1Criterion(self,U : float) -> float: 
        """
        Returns the G1 criterion at the parametric point U on the curve. This is the greatest angle allowed between the constraint and the target surface at U. Raises ConstructionError if the curve is not on a surface
        """
    def G2Criterion(self,U : float) -> float: 
        """
        Returns the G2 criterion at the parametric point U on the curve. This is the greatest difference in curvature allowed between the constraint and the target surface at U. Raises ConstructionError if the curve is not on a surface
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
    def LPropSurf(self,U : float) -> OCP.GeomLProp.GeomLProp_SLProps: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        None
        """
    def Length(self) -> float: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points on the curve used as a constraint. The default setting is 10. This parameter affects computation time, which increases by the cube of the number of points.
        """
    def Order(self) -> int: 
        """
        Returns the order of constraint, one of G0, G1 or G2.
        """
    def ProjectedCurve(self) -> OCP.Adaptor2d.Adaptor2d_HCurve2d: 
        """
        Returns the projected curve resulting from the normal projection of the curve on the initial surface
        """
    def SetCurve2dOnSurf(self,Curve2d : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        loads a 2d curve associated the surface resulting of the constraints
        """
    def SetG0Criterion(self,G0Crit : OCP.Law.Law_Function) -> None: 
        """
        Allows you to set the G0 criterion. This is the law defining the greatest distance allowed between the constraint and the target surface for each point of the constraint. If this criterion is not set, TolDist, the distance tolerance from the constructor, is used.
        """
    def SetG1Criterion(self,G1Crit : OCP.Law.Law_Function) -> None: 
        """
        Allows you to set the G1 criterion. This is the law defining the greatest angle allowed between the constraint and the target surface. If this criterion is not set, TolAng, the angular tolerance from the constructor, is used. Raises ConstructionError if the curve is not on a surface
        """
    def SetG2Criterion(self,G2Crit : OCP.Law.Law_Function) -> None: 
        """
        None
        """
    def SetNbPoints(self,NewNb : int) -> None: 
        """
        Allows you to set the number of points on the curve constraint. The default setting is 10. This parameter affects computation time, which increases by the cube of the number of points.
        """
    def SetOrder(self,Order : int) -> None: 
        """
        Allows you to set the order of continuity required for the constraints: G0, G1, and G2, controlled respectively by G0Criterion G1Criterion and G2Criterion.
        """
    def SetProjectedCurve(self,Curve2d : OCP.Adaptor2d.Adaptor2d_HCurve2d,TolU : float,TolV : float) -> None: 
        """
        loads a 2d curve resulting from the normal projection of the curve on the initial surface
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Boundary : OCP.Adaptor3d.Adaptor3d_HCurve,Order : int,NPt : int=10,TolDist : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1) -> None: ...
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
class GeomPlate_HArray1OfHCurve(GeomPlate_Array1OfHCurve, OCP.Standard.Standard_Transient):
    def Array1(self) -> GeomPlate_Array1OfHCurve: 
        """
        None
        """
    def Assign(self,theOther : GeomPlate_Array1OfHCurve) -> GeomPlate_Array1OfHCurve: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> GeomPlate_Array1OfHCurve: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
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
    def First(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
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
    def Init(self,theValue : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
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
    def Last(self) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
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
    def Move(self,theOther : GeomPlate_Array1OfHCurve) -> GeomPlate_Array1OfHCurve: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: 
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
    def Value(self,theIndex : int) -> OCP.Adaptor3d.Adaptor3d_HCurve: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.Adaptor3d.Adaptor3d_HCurve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_Array1OfHCurve) -> None: ...
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
class GeomPlate_HArray1OfSequenceOfReal(GeomPlate_Array1OfSequenceOfReal, OCP.Standard.Standard_Transient):
    def Array1(self) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        None
        """
    def Assign(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        None
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def First(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def Init(self,theValue : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
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
    def Last(self) -> OCP.TColStd.TColStd_SequenceOfReal: 
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
    def Move(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> GeomPlate_Array1OfSequenceOfReal: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : OCP.TColStd.TColStd_SequenceOfReal) -> None: 
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
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_SequenceOfReal: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_Array1OfSequenceOfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : OCP.TColStd.TColStd_SequenceOfReal) -> None: ...
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
class GeomPlate_SequenceOfCurveConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: ...
    def Assign(self,theOther : GeomPlate_SequenceOfCurveConstraint) -> GeomPlate_SequenceOfCurveConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomPlate_CurveConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomPlate_CurveConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> GeomPlate_CurveConstraint: 
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
    def First(self) -> GeomPlate_CurveConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> GeomPlate_CurveConstraint: 
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
    def Prepend(self,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> GeomPlate_CurveConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_SequenceOfCurveConstraint) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class GeomPlate_SequenceOfPointConstraint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : GeomPlate_PointConstraint) -> None: ...
    def Assign(self,theOther : GeomPlate_SequenceOfPointConstraint) -> GeomPlate_SequenceOfPointConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomPlate_PointConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomPlate_PointConstraint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> GeomPlate_PointConstraint: 
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
    def First(self) -> GeomPlate_PointConstraint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> GeomPlate_PointConstraint: 
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
    def Prepend(self,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : GeomPlate_PointConstraint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> GeomPlate_PointConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_SequenceOfPointConstraint) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class GeomPlate_MakeApprox():
    """
    Allows you to convert a GeomPlate surface into a BSpline.
    """
    def ApproxError(self) -> float: 
        """
        Returns the error in computation of the approximation surface. This is the distance between the entire target BSpline surface and the entire original surface generated by BuildPlateSurface and converted by GeomPlate_Surface.
        """
    def CriterionError(self) -> float: 
        """
        Returns the criterion error in computation of the approximation surface. This is estimated relative to the curve and point constraints only.
        """
    def Surface(self) -> OCP.Geom.Geom_BSplineSurface: 
        """
        Returns the BSpline surface extracted from the GeomPlate_MakeApprox object.
        """
    @overload
    def __init__(self,SurfPlate : GeomPlate_Surface,PlateCrit : OCP.AdvApp2Var.AdvApp2Var_Criterion,Tol3d : float,Nbmax : int,dgmax : int,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,EnlargeCoeff : float=1.1) -> None: ...
    @overload
    def __init__(self,SurfPlate : GeomPlate_Surface,Tol3d : float,Nbmax : int,dgmax : int,dmax : float,CritOrder : int=0,Continuity : OCP.GeomAbs.GeomAbs_Shape=GeomAbs_Shape.GeomAbs_C1,EnlargeCoeff : float=1.1) -> None: ...
    pass
class GeomPlate_PlateG0Criterion(OCP.AdvApp2Var.AdvApp2Var_Criterion):
    """
    this class contains a specific G0 criterion for GeomPlate_MakeApprox
    """
    def IsSatisfied(self,P : OCP.AdvApp2Var.AdvApp2Var_Patch) -> bool: 
        """
        None
        """
    def MaxValue(self) -> float: 
        """
        None
        """
    def Repartition(self) -> OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition: 
        """
        None
        """
    def Type(self) -> OCP.AdvApp2Var.AdvApp2Var_CriterionType: 
        """
        None
        """
    def Value(self,P : OCP.AdvApp2Var.AdvApp2Var_Patch,C : OCP.AdvApp2Var.AdvApp2Var_Context) -> None: 
        """
        None
        """
    def __init__(self,Data : OCP.TColgp.TColgp_SequenceOfXY,G0Data : OCP.TColgp.TColgp_SequenceOfXYZ,Maximum : float,Type : OCP.AdvApp2Var.AdvApp2Var_CriterionType=AdvApp2Var_CriterionType.AdvApp2Var_Absolute,Repart : OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition=AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular) -> None: ...
    pass
class GeomPlate_PlateG1Criterion(OCP.AdvApp2Var.AdvApp2Var_Criterion):
    """
    this class contains a specific G1 criterion for GeomPlate_MakeApprox
    """
    def IsSatisfied(self,P : OCP.AdvApp2Var.AdvApp2Var_Patch) -> bool: 
        """
        None
        """
    def MaxValue(self) -> float: 
        """
        None
        """
    def Repartition(self) -> OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition: 
        """
        None
        """
    def Type(self) -> OCP.AdvApp2Var.AdvApp2Var_CriterionType: 
        """
        None
        """
    def Value(self,P : OCP.AdvApp2Var.AdvApp2Var_Patch,C : OCP.AdvApp2Var.AdvApp2Var_Context) -> None: 
        """
        None
        """
    def __init__(self,Data : OCP.TColgp.TColgp_SequenceOfXY,G1Data : OCP.TColgp.TColgp_SequenceOfXYZ,Maximum : float,Type : OCP.AdvApp2Var.AdvApp2Var_CriterionType=AdvApp2Var_CriterionType.AdvApp2Var_Absolute,Repart : OCP.AdvApp2Var.AdvApp2Var_CriterionRepartition=AdvApp2Var_CriterionRepartition.AdvApp2Var_Regular) -> None: ...
    pass
class GeomPlate_PointConstraint(OCP.Standard.Standard_Transient):
    """
    Defines points as constraints to be used to deform a surface.Defines points as constraints to be used to deform a surface.Defines points as constraints to be used to deform a surface.
    """
    def D0(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def D1(self,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec) -> None: 
        """
        None
        """
    def D2(self,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec,V4 : OCP.gp.gp_Vec,V5 : OCP.gp.gp_Vec) -> None: 
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
    def G0Criterion(self) -> float: 
        """
        Returns the G0 criterion. This is the greatest distance allowed between the constraint and the target surface.
        """
    def G1Criterion(self) -> float: 
        """
        Returns the G1 criterion. This is the greatest angle allowed between the constraint and the target surface. Raises ConstructionError if the point is not on the surface.
        """
    def G2Criterion(self) -> float: 
        """
        Returns the G2 criterion. This is the greatest difference in curvature allowed between the constraint and the target surface. Raises ConstructionError if the point is not on the surface
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPnt2dOnSurf(self) -> bool: 
        """
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def LPropSurf(self) -> OCP.GeomLProp.GeomLProp_SLProps: 
        """
        None
        """
    def Order(self) -> int: 
        """
        Returns the order of constraint: G0, G1, and G2, controlled respectively by G0Criterion G1Criterion and G2Criterion.
        """
    def Pnt2dOnSurf(self) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def SetG0Criterion(self,TolDist : float) -> None: 
        """
        Allows you to set the G0 criterion. This is the law defining the greatest distance allowed between the constraint and the target surface. If this criterion is not set, {TolDist, the distance tolerance from the constructor, is used
        """
    def SetG1Criterion(self,TolAng : float) -> None: 
        """
        Allows you to set the G1 criterion. This is the law defining the greatest angle allowed between the constraint and the target surface. If this criterion is not set, TolAng, the angular tolerance from the constructor, is used. Raises ConstructionError if the point is not on the surface
        """
    def SetG2Criterion(self,TolCurv : float) -> None: 
        """
        Allows you to set the G2 criterion. This is the law defining the greatest difference in curvature allowed between the constraint and the target surface. If this criterion is not set, TolCurv, the curvature tolerance from the constructor, is used. Raises ConstructionError if the point is not on the surface
        """
    def SetOrder(self,Order : int) -> None: 
        """
        None
        """
    def SetPnt2dOnSurf(self,Pnt : OCP.gp.gp_Pnt2d) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,Pt : OCP.gp.gp_Pnt,Order : int,TolDist : float=0.0001) -> None: ...
    @overload
    def __init__(self,U : float,V : float,Surf : OCP.Geom.Geom_Surface,Order : int,TolDist : float=0.0001,TolAng : float=0.01,TolCurv : float=0.1) -> None: ...
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
class GeomPlate_SequenceOfAij(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : GeomPlate_SequenceOfAij) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : GeomPlate_Aij) -> None: ...
    def Assign(self,theOther : GeomPlate_SequenceOfAij) -> GeomPlate_SequenceOfAij: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomPlate_Aij: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomPlate_Aij: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> GeomPlate_Aij: 
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
    def First(self) -> GeomPlate_Aij: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomPlate_SequenceOfAij) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : GeomPlate_Aij) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomPlate_Aij) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomPlate_SequenceOfAij) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> GeomPlate_Aij: 
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
    def Prepend(self,theSeq : GeomPlate_SequenceOfAij) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : GeomPlate_Aij) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : GeomPlate_Aij) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomPlate_SequenceOfAij) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> GeomPlate_Aij: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : GeomPlate_SequenceOfAij) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class GeomPlate_HSequenceOfCurveConstraint(GeomPlate_SequenceOfCurveConstraint, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theSequence : GeomPlate_SequenceOfCurveConstraint) -> None: ...
    def Assign(self,theOther : GeomPlate_SequenceOfCurveConstraint) -> GeomPlate_SequenceOfCurveConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomPlate_CurveConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomPlate_CurveConstraint: 
        """
        Last item access
        """
    def ChangeSequence(self) -> GeomPlate_SequenceOfCurveConstraint: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> GeomPlate_CurveConstraint: 
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
    def First(self) -> GeomPlate_CurveConstraint: 
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
    def InsertAfter(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: ...
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> GeomPlate_CurveConstraint: 
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
    def Prepend(self,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: ...
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
    def Sequence(self) -> GeomPlate_SequenceOfCurveConstraint: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : GeomPlate_CurveConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomPlate_SequenceOfCurveConstraint) -> None: 
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
    def Value(self,theIndex : int) -> GeomPlate_CurveConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : GeomPlate_SequenceOfCurveConstraint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class GeomPlate_HSequenceOfPointConstraint(GeomPlate_SequenceOfPointConstraint, OCP.NCollection.NCollection_BaseSequence, OCP.Standard.Standard_Transient):
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSequence : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        None

        None
        """
    @overload
    def Append(self,theItem : GeomPlate_PointConstraint) -> None: ...
    def Assign(self,theOther : GeomPlate_SequenceOfPointConstraint) -> GeomPlate_SequenceOfPointConstraint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> GeomPlate_PointConstraint: 
        """
        First item access
        """
    def ChangeLast(self) -> GeomPlate_PointConstraint: 
        """
        Last item access
        """
    def ChangeSequence(self) -> GeomPlate_SequenceOfPointConstraint: 
        """
        None
        """
    def ChangeValue(self,theIndex : int) -> GeomPlate_PointConstraint: 
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
    def First(self) -> GeomPlate_PointConstraint: 
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
    def InsertAfter(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: ...
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> GeomPlate_PointConstraint: 
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
    def Prepend(self,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : GeomPlate_PointConstraint) -> None: ...
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
    def Sequence(self) -> GeomPlate_SequenceOfPointConstraint: 
        """
        None
        """
    def SetValue(self,theIndex : int,theItem : GeomPlate_PointConstraint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : GeomPlate_SequenceOfPointConstraint) -> None: 
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
    def Value(self,theIndex : int) -> GeomPlate_PointConstraint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : GeomPlate_SequenceOfPointConstraint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class GeomPlate_Surface(OCP.Geom.Geom_Surface, OCP.Geom.Geom_Geometry, OCP.Standard.Standard_Transient):
    """
    Describes the characteristics of plate surface objects returned by BuildPlateSurface::Surface. These can be used to verify the quality of the resulting surface before approximating it to a Geom_BSpline surface generated by MakeApprox. This proves necessary in cases where you want to use the resulting surface as the support for a shape. The algorithmically generated surface cannot fill this function as is, and as a result must be converted first.Describes the characteristics of plate surface objects returned by BuildPlateSurface::Surface. These can be used to verify the quality of the resulting surface before approximating it to a Geom_BSpline surface generated by MakeApprox. This proves necessary in cases where you want to use the resulting surface as the support for a shape. The algorithmically generated surface cannot fill this function as is, and as a result must be converted first.Describes the characteristics of plate surface objects returned by BuildPlateSurface::Surface. These can be used to verify the quality of the resulting surface before approximating it to a Geom_BSpline surface generated by MakeApprox. This proves necessary in cases where you want to use the resulting surface as the support for a shape. The algorithmically generated surface cannot fill this function as is, and as a result must be converted first.
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def CallSurfinit(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Constraints(self,Seq : OCP.TColgp.TColgp_SequenceOfXY) -> None: 
        """
        None
        """
    def Continuity(self) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Global Continuity of the surface in direction U and V : C0 : only geometric continuity, C1 : continuity of the first derivative all along the surface, C2 : continuity of the second derivative all along the surface, C3 : continuity of the third derivative all along the surface, G1 : tangency continuity all along the surface, G2 : curvature continuity all along the surface, CN : the order of continuity is infinite. Example : If the surface is C1 in the V parametric direction and C2 in the U parametric direction Shape = C1.
        """
    def Copy(self) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def D0(self,U : float,V : float,P : OCP.gp.gp_Pnt) -> None: 
        """
        Computes the point of parameter U,V on the surface.
        """
    def D1(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P and the first derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C1.
        """
    def D2(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first and the second derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def D3(self,U : float,V : float,P : OCP.gp.gp_Pnt,D1U : OCP.gp.gp_Vec,D1V : OCP.gp.gp_Vec,D2U : OCP.gp.gp_Vec,D2V : OCP.gp.gp_Vec,D2UV : OCP.gp.gp_Vec,D3U : OCP.gp.gp_Vec,D3V : OCP.gp.gp_Vec,D3UUV : OCP.gp.gp_Vec,D3UVV : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point P, the first,the second and the third derivatives in the directions U and V at this point. Raised if the continuity of the surface is not C2.
        """
    def DN(self,U : float,V : float,Nu : int,Nv : int) -> OCP.gp.gp_Vec: 
        """
        ---Purpose ; Computes the derivative of order Nu in the direction U and Nv in the direction V at the point P(U, V).
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
    def IsCNu(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the U parametric direction. Raised if N < 0.
        """
    def IsCNv(self,N : int) -> bool: 
        """
        Returns the order of continuity of the surface in the V parametric direction. Raised if N < 0.
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
    def IsUClosed(self) -> bool: 
        """
        Is the surface closed in the parametric direction U ? Returns True if for each parameter V the distance between the point P (UFirst, V) and P (ULast, V) is lower or equal to Resolution from gp. UFirst and ULast are the parametric bounds in the U direction.
        """
    def IsUPeriodic(self) -> bool: 
        """
        Is the parametrization of a surface periodic in the direction U ? It is possible only if the surface is closed in this parametric direction and if the following relation is satisfied : for each parameter V the distance between the point P (U, V) and the point P (U + T, V) is lower or equal to Resolution from package gp. T is the parametric period and must be a constant.
        """
    def IsVClosed(self) -> bool: 
        """
        Is the surface closed in the parametric direction V ? Returns True if for each parameter U the distance between the point P (U, VFirst) and P (U, VLast) is lower or equal to Resolution from gp. VFirst and VLast are the parametric bounds in the V direction.
        """
    def IsVPeriodic(self) -> bool: 
        """
        Is the parametrization of a surface periodic in the direction U ? It is possible only if the surface is closed in this parametric direction and if the following relation is satisfied : for each parameter V the distance between the point P (U, V) and the point P (U + T, V) is lower or equal to Resolution from package gp. T is the parametric period and must be a constant.
        """
    @overload
    def Mirror(self,A1 : OCP.gp.gp_Ax1) -> None: 
        """
        Performs the symmetrical transformation of a Geometry with respect to the point P which is the center of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to an axis placement which is the axis of the symmetry.

        Performs the symmetrical transformation of a Geometry with respect to a plane. The axis placement A2 locates the plane of the symmetry : (Location, XDirection, YDirection).
        """
    @overload
    def Mirror(self,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Mirror(self,A2 : OCP.gp.gp_Ax2) -> None: ...
    @overload
    def Mirrored(self,A2 : OCP.gp.gp_Ax2) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None

        None
        """
    @overload
    def Mirrored(self,A1 : OCP.gp.gp_Ax1) -> OCP.Geom.Geom_Geometry: ...
    @overload
    def Mirrored(self,P : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: ...
    def ParametricTransformation(self,T : OCP.gp.gp_Trsf) -> OCP.gp.gp_GTrsf2d: 
        """
        Returns a 2d transformation used to find the new parameters of a point on the transformed surface.
        """
    def RealBounds(self) -> Tuple[float, float, float, float]: 
        """
        None
        """
    def Rotate(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> None: 
        """
        Rotates a Geometry. A1 is the axis of the rotation. Ang is the angular value of the rotation in radians.
        """
    def Rotated(self,A1 : OCP.gp.gp_Ax1,Ang : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def Scale(self,P : OCP.gp.gp_Pnt,S : float) -> None: 
        """
        Scales a Geometry. S is the scaling value.
        """
    def Scaled(self,P : OCP.gp.gp_Pnt,S : float) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    def SetBounds(self,Umin : float,Umax : float,Vmin : float,Vmax : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,T : OCP.gp.gp_Trsf) -> None: 
        """
        Transformation of a geometric object. This tansformation can be a translation, a rotation, a symmetry, a scaling or a complex transformation obtained by combination of the previous elementaries transformations. (see class Transformation of the package Geom).
        """
    def TransformParameters(self,T : OCP.gp.gp_Trsf) -> Tuple[float, float]: 
        """
        Computes the parameters on the transformed surface for the transform of the point of parameters U,V on <me>.
        """
    def Transformed(self,T : OCP.gp.gp_Trsf) -> OCP.Geom.Geom_Geometry: 
        """
        None
        """
    @overload
    def Translate(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: 
        """
        Translates a Geometry. V is the vector of the tanslation.

        Translates a Geometry from the point P1 to the point P2.
        """
    @overload
    def Translate(self,V : OCP.gp.gp_Vec) -> None: ...
    @overload
    def Translated(self,V : OCP.gp.gp_Vec) -> OCP.Geom.Geom_Geometry: 
        """
        None

        None
        """
    @overload
    def Translated(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> OCP.Geom.Geom_Geometry: ...
    def UIso(self,U : float) -> OCP.Geom.Geom_Curve: 
        """
        Computes the U isoparametric curve.
        """
    def UPeriod(self) -> float: 
        """
        returns the Uperiod. raises if the surface is not uperiodic.
        """
    def UReverse(self) -> None: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def UReversed(self) -> OCP.Geom.Geom_Surface: 
        """
        Reverses the U direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def UReversedParameter(self,U : float) -> float: 
        """
        Return the parameter on the Ureversed surface for the point of parameter U on <me>.
        """
    def VIso(self,V : float) -> OCP.Geom.Geom_Curve: 
        """
        Computes the V isoparametric curve.
        """
    def VPeriod(self) -> float: 
        """
        returns the Vperiod. raises if the surface is not vperiodic.
        """
    def VReverse(self) -> None: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified.
        """
    def VReversed(self) -> OCP.Geom.Geom_Surface: 
        """
        Reverses the V direction of parametrization of <me>. The bounds of the surface are not modified. A copy of <me> is returned.
        """
    def VReversedParameter(self,V : float) -> float: 
        """
        Return the parameter on the Vreversed surface for the point of parameter V on <me>.
        """
    def Value(self,U : float,V : float) -> OCP.gp.gp_Pnt: 
        """
        Computes the point of parameter U on the surface.
        """
    def __init__(self,Surfinit : OCP.Geom.Geom_Surface,Surfinter : OCP.Plate.Plate_Plate) -> None: ...
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
