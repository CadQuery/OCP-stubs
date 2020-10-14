import OCP.IntAna
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TColStd
import OCP.gp
__all__  = [
"IntAna_Curve",
"IntAna_Int3Pln",
"IntAna_IntConicQuad",
"IntAna_IntLinTorus",
"IntAna_IntQuadQuad",
"IntAna_ListOfCurve",
"IntAna_QuadQuadGeo",
"IntAna_Quadric",
"IntAna_ResultType",
"IntAna_Circle",
"IntAna_Ellipse",
"IntAna_Empty",
"IntAna_Hyperbola",
"IntAna_Line",
"IntAna_NoGeometricSolution",
"IntAna_Parabola",
"IntAna_Point",
"IntAna_PointAndCircle",
"IntAna_Same"
]
class IntAna_Curve():
    """
    Definition of a parametric Curve which is the result of the intersection between two quadrics.
    """
    def D1u(self,Theta : float,P : OCP.gp.gp_Pnt,V : OCP.gp.gp_Vec) -> bool: 
        """
        Returns the point and the first derivative at parameter Theta on the curve.
        """
    def Domain(self) -> Tuple[float, float]: 
        """
        Returns the paramatric domain of the curve.
        """
    def FindParameter(self,P : OCP.gp.gp_Pnt,theParams : OCP.TColStd.TColStd_ListOfReal) -> None: 
        """
        Tries to find the parameter of the point P on the curve. If the method returns False, the "projection" is impossible. If the method returns True at least one parameter has been found. theParams is always sorted in ascending order.
        """
    def IsConstant(self) -> bool: 
        """
        Returns TRUE if the function is constant.
        """
    def IsFirstOpen(self) -> bool: 
        """
        Returns TRUE if the domain is open at the beginning.
        """
    def IsLastOpen(self) -> bool: 
        """
        Returns TRUE if the domain is open at the end.
        """
    def IsOpen(self) -> bool: 
        """
        Returns TRUE if the curve is not infinite at the last parameter or at the first parameter of the domain.
        """
    def SetConeQuadValues(self,Cone : OCP.gp.gp_Cone,Qxx : float,Qyy : float,Qzz : float,Qxy : float,Qxz : float,Qyz : float,Qx : float,Qy : float,Qz : float,Q1 : float,Tol : float,DomInf : float,DomSup : float,TwoZForATheta : bool,ZIsPositive : bool) -> None: 
        """
        Sets the parameters used to compute Points and Derivative on the curve.
        """
    def SetCylinderQuadValues(self,Cylinder : OCP.gp.gp_Cylinder,Qxx : float,Qyy : float,Qzz : float,Qxy : float,Qxz : float,Qyz : float,Qx : float,Qy : float,Qz : float,Q1 : float,Tol : float,DomInf : float,DomSup : float,TwoZForATheta : bool,ZIsPositive : bool) -> None: 
        """
        Sets the parameters used to compute Points and Derivative on the curve.
        """
    def SetDomain(self,theFirst : float,theLast : float) -> None: 
        """
        Trims this curve
        """
    def SetIsFirstOpen(self,Flag : bool) -> None: 
        """
        If flag is True, the Curve is not defined at the first parameter of its domain.
        """
    def SetIsLastOpen(self,Flag : bool) -> None: 
        """
        If flag is True, the Curve is not defined at the first parameter of its domain.
        """
    def Value(self,Theta : float) -> OCP.gp.gp_Pnt: 
        """
        Returns the point at parameter Theta on the curve.
        """
    def __init__(self) -> None: ...
    pass
class IntAna_Int3Pln():
    """
    Intersection between 3 planes. The algorithm searches for an intersection point. If two of the planes are parallel or identical, IsEmpty returns TRUE.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the computation was successful.

        Returns True if the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection POINT. If 2 planes are identical or parallel, IsEmpty will return TRUE.

        Returns TRUE if there is no intersection POINT. If 2 planes are identical or parallel, IsEmpty will return TRUE.
        """
    def Perform(self,P1 : OCP.gp.gp_Pln,P2 : OCP.gp.gp_Pln,P3 : OCP.gp.gp_Pln) -> None: 
        """
        Determination of the intersection point between 3 planes.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the intersection point.

        Returns the intersection point.
        """
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pln,P2 : OCP.gp.gp_Pln,P3 : OCP.gp.gp_Pln) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntAna_IntConicQuad():
    """
    This class provides the analytic intersection between a conic defined as an element of gp (Lin,Circ,Elips, Parab,Hypr) and a quadric as defined in the class Quadric from IntAna. The intersection between a conic and a plane is treated as a special case.
    """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the creation completed.

        Returns TRUE if the creation completed.
        """
    def IsInQuadric(self) -> bool: 
        """
        Returns TRUE if the conic is in the quadric.

        Returns TRUE if the conic is in the quadric.
        """
    def IsParallel(self) -> bool: 
        """
        Returns TRUE if the line is in a quadric which is parallel to the quadric.

        Returns TRUE if the line is in a quadric which is parallel to the quadric.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of intersection point.

        Returns the number of intersection point.
        """
    @overload
    def ParamOnConic(self,i : int) -> float: 
        """
        Returns the parameter on the line of the intersection point of range N.

        Returns the parameter on the line of the intersection point of range N.
        """
    @overload
    def ParamOnConic(self,N : int) -> float: ...
    @overload
    def Perform(self,H : OCP.gp.gp_Hypr,Q : IntAna_Quadric) -> None: 
        """
        Intersects a line and a quadric.

        Intersects a circle and a quadric.

        Intersects an ellipse and a quadric.

        Intersects a parabola and a quadric.

        Intersects an hyperbola and a quadric.

        Intersects a line and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to check the distance between line and plane on the distance <Len> from the origin of the line.

        Intersects a circle and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to determine if a distance is null.

        Intersects an ellipse and a plane. Tolang is used to determine if the angle between two vectors is null. Tol is used to determine if a distance is null.

        Intersects a parabola and a plane. Tolang is used to determine if the angle between two vectors is null.

        Intersects an hyperbola and a plane. Tolang is used to determine if the angle between two vectors is null.
        """
    @overload
    def Perform(self,E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pln,Tolang : float,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Parab,Q : IntAna_Quadric) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pln,Tolang : float,Tol : float) -> None: ...
    @overload
    def Perform(self,E : OCP.gp.gp_Elips,Q : IntAna_Quadric) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,Q : IntAna_Quadric) -> None: ...
    @overload
    def Perform(self,H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pln,Tolang : float) -> None: ...
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,Q : IntAna_Quadric) -> None: ...
    @overload
    def Perform(self,Pb : OCP.gp.gp_Parab,P : OCP.gp.gp_Pln,Tolang : float) -> None: ...
    @overload
    def Perform(self,L : OCP.gp.gp_Lin,P : OCP.gp.gp_Pln,Tolang : float,Tol : float=0.0,Len : float=0.0) -> None: ...
    @overload
    def Point(self,i : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of range N.

        Returns the point of range N.
        """
    @overload
    def Point(self,N : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,P : OCP.gp.gp_Pln,Tolang : float,Tol : float) -> None: ...
    @overload
    def __init__(self,Pb : OCP.gp.gp_Parab,P : OCP.gp.gp_Pln,Tolang : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,Q : IntAna_Quadric) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,Q : IntAna_Quadric) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips,Q : IntAna_Quadric) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr,Q : IntAna_Quadric) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr,P : OCP.gp.gp_Pln,Tolang : float) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,P : OCP.gp.gp_Pln,Tolang : float,Tol : float=0.0,Len : float=0.0) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab,Q : IntAna_Quadric) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips,P : OCP.gp.gp_Pln,Tolang : float,Tol : float) -> None: ...
    pass
class IntAna_IntLinTorus():
    """
    Intersection between a line and a torus.
    """
    def IsDone(self) -> bool: 
        """
        Returns True if the computation was successful.

        Returns True if the computation was successful.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of intersection points.

        Returns the number of intersection points.
        """
    def ParamOnLine(self,Index : int) -> float: 
        """
        Returns the parameter on the line of the intersection point of range Index.

        Returns the parameter on the line of the intersection point of range Index.
        """
    def ParamOnTorus(self,Index : int) -> Tuple[float, float]: 
        """
        Returns the parameters on the torus of the intersection point of range Index.

        Returns the parameters on the torus of the intersection point of range Index.
        """
    def Perform(self,L : OCP.gp.gp_Lin,T : OCP.gp.gp_Torus) -> None: 
        """
        Intersects a line and a torus.
        """
    def Value(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the intersection point of range Index.

        Returns the intersection point of range Index.
        """
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,T : OCP.gp.gp_Torus) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntAna_IntQuadQuad():
    """
    This class provides the analytic intersection between a cylinder or a cone from gp and another quadric, as defined in the class Quadric from IntAna. This algorithm is used when the geometric intersection (class QuadQuadGeo from IntAna) returns no geometric solution. The result of the intersection may be - Curves as defined in the class Curve from IntAna - Points (Pnt from gp)
    """
    def Curve(self,N : int) -> IntAna_Curve: 
        """
        Returns the curve of range N.
        """
    def HasNextCurve(self,I : int) -> bool: 
        """
        Returns True if the Curve I shares its last bound with another curve.
        """
    def HasPreviousCurve(self,I : int) -> bool: 
        """
        Returns True if the Curve I shares its first bound with another curve.
        """
    def IdenticalElements(self) -> bool: 
        """
        Returns TRUE if the cylinder, the cone or the sphere is identical to the quadric.

        Returns TRUE if the cylinder, the cone or the sphere is identical to the quadric.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the computation was successful.

        Returns True if the computation was successful.
        """
    def NbCurve(self) -> int: 
        """
        Returns the number of curves solution.

        Returns the number of curves solution.
        """
    def NbPnt(self) -> int: 
        """
        Returns the number of contact point.

        Returns the number of contact point.
        """
    def NextCurve(self,I : int,theOpposite : bool) -> int: 
        """
        If HasNextCurve(I) returns True, this function returns the Index J of the curve which has a common bound with the curve I. If theOpposite == True , then the last parameter of the curve I, and the last parameter of the curve J give the same point. Else the last parameter of the curve I and the first parameter of the curve J are the same point.
        """
    def Parameters(self,N : int) -> Tuple[float, float]: 
        """
        Returns the paramaters on the "explicit quadric" (i.e the cylinder or the cone, the first argument given to the constructor) of the point of range N.
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Cylinder,Q : IntAna_Quadric,Tol : float) -> None: 
        """
        Intersects a cylinder and a quadric . Tol est a definir plus precisemment.

        Intersects a cone and a quadric. Tol est a definir plus precisemment.
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Cone,Q : IntAna_Quadric,Tol : float) -> None: ...
    def Point(self,N : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of range N.
        """
    def PreviousCurve(self,I : int,theOpposite : bool) -> int: 
        """
        if HasPreviousCurve(I) returns True, this function returns the Index J of the curve which has a common bound with the curve I. If theOpposite == True , then the first parameter of the curve I, and the first parameter of the curve J give the same point. Else the first parameter of the curve I and the last parameter of the curve J are the same point.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Cone,Q : IntAna_Quadric,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Cylinder,Q : IntAna_Quadric,Tol : float) -> None: ...
    pass
class IntAna_ListOfCurve(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntAna_Curve) -> IntAna_Curve: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : IntAna_Curve,theIter : Any) -> None: ...
    @overload
    def Append(self,theOther : IntAna_ListOfCurve) -> None: ...
    def Assign(self,theOther : IntAna_ListOfCurve) -> IntAna_ListOfCurve: 
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
    def First(self) -> IntAna_Curve: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : IntAna_ListOfCurve,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : IntAna_Curve,theIter : Any) -> IntAna_Curve: ...
    @overload
    def InsertBefore(self,theOther : IntAna_ListOfCurve,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : IntAna_Curve,theIter : Any) -> IntAna_Curve: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> IntAna_Curve: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : IntAna_ListOfCurve) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : IntAna_Curve) -> IntAna_Curve: ...
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
    def __init__(self,theOther : IntAna_ListOfCurve) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class IntAna_QuadQuadGeo():
    """
    Geometric intersections between two natural quadrics (Sphere , Cylinder , Cone , Pln from gp). The possible intersections are : - 1 point - 1 or 2 line(s) - 1 Point and 1 Line - 1 circle - 1 ellipse - 1 parabola - 1 or 2 hyperbola(s). - Empty : there is no intersection between the two quadrics. - Same : the quadrics are identical - NoGeometricSolution : there may be an intersection, but it is necessary to use an analytic algorithm to determine it. See class IntQuadQuad from IntAna.
    """
    def Circle(self,Num : int) -> OCP.gp.gp_Circ: 
        """
        Returns the circle solution of range Num.
        """
    def Ellipse(self,Num : int) -> OCP.gp.gp_Elips: 
        """
        Returns the ellipse solution of range Num.
        """
    def HasCommonGen(self) -> bool: 
        """
        None
        """
    def Hyperbola(self,Num : int) -> OCP.gp.gp_Hypr: 
        """
        Returns the hyperbola solution of range Num.
        """
    def IsDone(self) -> bool: 
        """
        Returns Standard_True if the computation was successful.

        Returns Standard_True if the computation was successful.
        """
    def Line(self,Num : int) -> OCP.gp.gp_Lin: 
        """
        Returns the line solution of range Num.
        """
    def NbSolutions(self) -> int: 
        """
        Returns the number of interesections. The possible intersections are : - 1 point - 1 or 2 line(s) - 1 Point and 1 Line - 1 circle - 1 ellipse - 1 parabola - 1 or 2 hyperbola(s).

        Returns the number of interesections. The possible intersections are : - 1 point - 1 or 2 line(s) - 1 Point and 1 Line - 1 circle - 1 ellipse - 1 parabola - 1 or 2 hyperbola(s).
        """
    def PChar(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Parabola(self,Num : int) -> OCP.gp.gp_Parab: 
        """
        Returns the parabola solution of range Num.
        """
    @overload
    def Perform(self,P : OCP.gp.gp_Pln,C : OCP.gp.gp_Cone,Tolang : float,Tol : float) -> None: 
        """
        Intersects two planes. TolAng is the angular tolerance used to determine if the planes are parallel. Tol is the tolerance used to determine if the planes are identical (only when they are parallel).

        Intersects a plane and a cylinder. TolAng is the angular tolerance used to determine if the axis of the cylinder is parallel to the plane. Tol is the tolerance used to determine if the result is a circle or an ellipse. If the maximum distance between the ellipse solution and the circle centered at the ellipse center is less than Tol, the result will be the circle. H is the height of the cylinder <Cyl>. It is used to check whether the plane and cylinder are parallel.

        Intersects a plane and a sphere.

        Intersects a plane and a cone. TolAng is the angular tolerance used to determine if the axis of the cone is parallel or perpendicular to the plane, and if the generating line of the cone is parallel to the plane. Tol is the tolerance used to determine if the apex of the cone is in the plane.

        Intersects two cylinders

        Intersects a cylinder and a sphere.

        Intersects a cylinder and a cone.

        Intersects a two spheres.

        Intersects a sphere and a cone.

        Intersects two cones.

        Intersects plane and torus.

        Intersects cylinder and torus.

        Intersects cone and torus.

        Intersects sphere and torus.

        Intersects two toruses.
        """
    @overload
    def Perform(self,P1 : OCP.gp.gp_Pln,P2 : OCP.gp.gp_Pln,TolAng : float,Tol : float) -> None: ...
    @overload
    def Perform(self,Sph1 : OCP.gp.gp_Sphere,Sph2 : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    @overload
    def Perform(self,Con : OCP.gp.gp_Cone,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def Perform(self,Tor1 : OCP.gp.gp_Torus,Tor2 : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pln,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def Perform(self,Con1 : OCP.gp.gp_Cone,Con2 : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def Perform(self,Sph : OCP.gp.gp_Sphere,Con : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def Perform(self,P : OCP.gp.gp_Pln,C : OCP.gp.gp_Cylinder,Tolang : float,Tol : float,H : float=0.0) -> None: ...
    @overload
    def Perform(self,Sph : OCP.gp.gp_Sphere,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def Perform(self,Cyl : OCP.gp.gp_Cylinder,Con : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def Perform(self,Cyl : OCP.gp.gp_Cylinder,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def Perform(self,Cyl1 : OCP.gp.gp_Cylinder,Cyl2 : OCP.gp.gp_Cylinder,Tol : float) -> None: ...
    @overload
    def Perform(self,Pln : OCP.gp.gp_Pln,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def Perform(self,Cyl : OCP.gp.gp_Cylinder,Sph : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    def Point(self,Num : int) -> OCP.gp.gp_Pnt: 
        """
        Returns the point solution of range Num.
        """
    def TypeInter(self) -> IntAna_ResultType: 
        """
        Returns the type of intersection.

        Returns the type of intersection.
        """
    @overload
    def __init__(self,Sph1 : OCP.gp.gp_Sphere,Sph2 : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    @overload
    def __init__(self,Con1 : OCP.gp.gp_Cone,Con2 : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def __init__(self,Con : OCP.gp.gp_Cone,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self,Tor1 : OCP.gp.gp_Torus,Tor2 : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,C : OCP.gp.gp_Cylinder,Tolang : float,Tol : float,H : float=0.0) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,C : OCP.gp.gp_Cone,Tolang : float,Tol : float) -> None: ...
    @overload
    def __init__(self,Sph : OCP.gp.gp_Sphere,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Sph : OCP.gp.gp_Sphere,Con : OCP.gp.gp_Cone,Tol : float) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Sph : OCP.gp.gp_Sphere,Tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pln,S : OCP.gp.gp_Sphere) -> None: ...
    @overload
    def __init__(self,Cyl1 : OCP.gp.gp_Cylinder,Cyl2 : OCP.gp.gp_Cylinder,Tol : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pln,P2 : OCP.gp.gp_Pln,TolAng : float,Tol : float) -> None: ...
    @overload
    def __init__(self,Pln : OCP.gp.gp_Pln,Tor : OCP.gp.gp_Torus,Tol : float) -> None: ...
    @overload
    def __init__(self,Cyl : OCP.gp.gp_Cylinder,Con : OCP.gp.gp_Cone,Tol : float) -> None: ...
    pass
class IntAna_Quadric():
    """
    This class provides a description of Quadrics by their Coefficients in natural coordinate system.
    """
    def Coefficients(self) -> Tuple[float, float, float, float, float, float, float, float, float, float]: 
        """
        Returns the coefficients of the polynomial equation which define the quadric: xCXX x**2 + xCYY y**2 + xCZZ z**2 + 2 ( xCXY x y + xCXZ x z + xCYZ y z ) + 2 ( xCX x + xCY y + xCZ z ) + xCCte
        """
    def __init__(self) -> None: ...
    pass
class IntAna_ResultType():
    """
    None

    Members:

      IntAna_Point

      IntAna_Line

      IntAna_Circle

      IntAna_PointAndCircle

      IntAna_Ellipse

      IntAna_Parabola

      IntAna_Hyperbola

      IntAna_Empty

      IntAna_Same

      IntAna_NoGeometricSolution
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    IntAna_Circle: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Circle
    IntAna_Ellipse: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Ellipse
    IntAna_Empty: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Empty
    IntAna_Hyperbola: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Hyperbola
    IntAna_Line: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Line
    IntAna_NoGeometricSolution: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_NoGeometricSolution
    IntAna_Parabola: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Parabola
    IntAna_Point: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Point
    IntAna_PointAndCircle: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_PointAndCircle
    IntAna_Same: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Same
    __entries: dict # value = {'IntAna_Point': (IntAna_ResultType.IntAna_Point, None), 'IntAna_Line': (IntAna_ResultType.IntAna_Line, None), 'IntAna_Circle': (IntAna_ResultType.IntAna_Circle, None), 'IntAna_PointAndCircle': (IntAna_ResultType.IntAna_PointAndCircle, None), 'IntAna_Ellipse': (IntAna_ResultType.IntAna_Ellipse, None), 'IntAna_Parabola': (IntAna_ResultType.IntAna_Parabola, None), 'IntAna_Hyperbola': (IntAna_ResultType.IntAna_Hyperbola, None), 'IntAna_Empty': (IntAna_ResultType.IntAna_Empty, None), 'IntAna_Same': (IntAna_ResultType.IntAna_Same, None), 'IntAna_NoGeometricSolution': (IntAna_ResultType.IntAna_NoGeometricSolution, None)}
    __members__: dict # value = {'IntAna_Point': IntAna_ResultType.IntAna_Point, 'IntAna_Line': IntAna_ResultType.IntAna_Line, 'IntAna_Circle': IntAna_ResultType.IntAna_Circle, 'IntAna_PointAndCircle': IntAna_ResultType.IntAna_PointAndCircle, 'IntAna_Ellipse': IntAna_ResultType.IntAna_Ellipse, 'IntAna_Parabola': IntAna_ResultType.IntAna_Parabola, 'IntAna_Hyperbola': IntAna_ResultType.IntAna_Hyperbola, 'IntAna_Empty': IntAna_ResultType.IntAna_Empty, 'IntAna_Same': IntAna_ResultType.IntAna_Same, 'IntAna_NoGeometricSolution': IntAna_ResultType.IntAna_NoGeometricSolution}
    pass
IntAna_Circle: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Circle
IntAna_Ellipse: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Ellipse
IntAna_Empty: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Empty
IntAna_Hyperbola: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Hyperbola
IntAna_Line: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Line
IntAna_NoGeometricSolution: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_NoGeometricSolution
IntAna_Parabola: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Parabola
IntAna_Point: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Point
IntAna_PointAndCircle: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_PointAndCircle
IntAna_Same: OCP.IntAna.IntAna_ResultType # value = IntAna_ResultType.IntAna_Same
