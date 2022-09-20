import OCP.GProp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
import OCP.TColgp
import OCP.TColStd
__all__  = [
"GProp",
"GProp_GProps",
"GProp_EquaType",
"GProp_CelGProps",
"GProp_PEquation",
"GProp_PGProps",
"GProp_PrincipalProps",
"GProp_SelGProps",
"GProp_UndefinedAxis",
"GProp_ValueType",
"GProp_VelGProps",
"GProp_CenterMassX",
"GProp_CenterMassY",
"GProp_CenterMassZ",
"GProp_InertiaXX",
"GProp_InertiaXY",
"GProp_InertiaXZ",
"GProp_InertiaYY",
"GProp_InertiaYZ",
"GProp_InertiaZZ",
"GProp_Line",
"GProp_Mass",
"GProp_None",
"GProp_Plane",
"GProp_Point",
"GProp_Space",
"GProp_Unknown"
]
class GProp():
    """
    This package defines algorithms to compute the global properties of a set of points, a curve, a surface, a solid (non infinite region of space delimited with geometric entities), a compound geometric system (heterogeneous composition of the previous entities).
    """
    @staticmethod
    def HOperator_s(G : OCP.gp.gp_Pnt,Q : OCP.gp.gp_Pnt,Mass : float,Operator : OCP.gp.gp_Mat) -> None: 
        """
        methods of package Computes the matrix Operator, referred to as the "Huyghens Operator" of a geometric system at the point Q of the space, using the following data : - Mass, i.e. the mass of the system, - G, the center of mass of the system. The "Huyghens Operator" is used to compute Inertia/Q, the matrix of inertia of the system at the point Q using Huyghens' theorem : Inertia/Q = Inertia/G + HOperator (Q, G, Mass) where Inertia/G is the matrix of inertia of the system relative to its center of mass as returned by the function MatrixOfInertia on any GProp_GProps object.
        """
    def __init__(self) -> None: ...
    pass
class GProp_GProps():
    """
    Implements a general mechanism to compute the global properties of a "compound geometric system" in 3d space by composition of the global properties of "elementary geometric entities" such as (curve, surface, solid, set of points). It is possible to compose the properties of several "compound geometric systems" too.
    """
    def Add(self,Item : GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def Mass(self) -> float: 
        """
        Returns the mass of the current system. If no density is attached to the components of the current system the returned value corresponds to : - the total length of the edges of the current system if this framework retains only linear properties, as is the case for example, when using only the LinearProperties function to combine properties of lines from shapes, or - the total area of the faces of the current system if this framework retains only surface properties, as is the case for example, when using only the SurfaceProperties function to combine properties of surfaces from shapes, or - the total volume of the solids of the current system if this framework retains only volume properties, as is the case for example, when using only the VolumeProperties function to combine properties of volumes from solids. Warning A length, an area, or a volume is computed in the current data unit system. The mass of a single object is obtained by multiplying its length, its area or its volume by the given density. You must be consistent with respect to the units used.
        """
    def MatrixOfInertia(self) -> OCP.gp.gp_Mat: 
        """
        returns the matrix of inertia. It is a symmetrical matrix. The coefficients of the matrix are the quadratic moments of inertia.
        """
    def MomentOfInertia(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        computes the moment of inertia of the material system about the axis A.
        """
    def PrincipalProperties(self) -> GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,SystemLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GProp_EquaType():
    """
    None

    Members:

      GProp_Plane

      GProp_Line

      GProp_Point

      GProp_Space

      GProp_None
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
    GProp_Line: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Line: 1>
    GProp_None: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_None: 4>
    GProp_Plane: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Plane: 0>
    GProp_Point: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Point: 2>
    GProp_Space: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Space: 3>
    __entries: dict # value = {'GProp_Plane': (<GProp_EquaType.GProp_Plane: 0>, None), 'GProp_Line': (<GProp_EquaType.GProp_Line: 1>, None), 'GProp_Point': (<GProp_EquaType.GProp_Point: 2>, None), 'GProp_Space': (<GProp_EquaType.GProp_Space: 3>, None), 'GProp_None': (<GProp_EquaType.GProp_None: 4>, None)}
    __members__: dict # value = {'GProp_Plane': <GProp_EquaType.GProp_Plane: 0>, 'GProp_Line': <GProp_EquaType.GProp_Line: 1>, 'GProp_Point': <GProp_EquaType.GProp_Point: 2>, 'GProp_Space': <GProp_EquaType.GProp_Space: 3>, 'GProp_None': <GProp_EquaType.GProp_None: 4>}
    pass
class GProp_CelGProps(GProp_GProps):
    """
    Computes the global properties of bounded curves in 3D space. It can be an elementary curve from package gp such as Lin, Circ, Elips, Parab .
    """
    def Add(self,Item : GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def Mass(self) -> float: 
        """
        Returns the mass of the current system. If no density is attached to the components of the current system the returned value corresponds to : - the total length of the edges of the current system if this framework retains only linear properties, as is the case for example, when using only the LinearProperties function to combine properties of lines from shapes, or - the total area of the faces of the current system if this framework retains only surface properties, as is the case for example, when using only the SurfaceProperties function to combine properties of surfaces from shapes, or - the total volume of the solids of the current system if this framework retains only volume properties, as is the case for example, when using only the VolumeProperties function to combine properties of volumes from solids. Warning A length, an area, or a volume is computed in the current data unit system. The mass of a single object is obtained by multiplying its length, its area or its volume by the given density. You must be consistent with respect to the units used.
        """
    def MatrixOfInertia(self) -> OCP.gp.gp_Mat: 
        """
        returns the matrix of inertia. It is a symmetrical matrix. The coefficients of the matrix are the quadratic moments of inertia.
        """
    def MomentOfInertia(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        computes the moment of inertia of the material system about the axis A.
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Circ,U1 : float,U2 : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,C : OCP.gp.gp_Lin,U1 : float,U2 : float) -> None: ...
    def PrincipalProperties(self) -> GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def SetLocation(self,CLocation : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,C : OCP.gp.gp_Lin,U1 : float,U2 : float,CLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,U1 : float,U2 : float,CLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,CLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GProp_PEquation():
    """
    A framework to analyze a collection - or cloud - of points and to verify if they are coincident, collinear or coplanar within a given precision. If so, it also computes the mean point, the mean line or the mean plane of the points. If not, it computes the minimal box which includes all the points.
    """
    def Box(self,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec,V2 : OCP.gp.gp_Vec,V3 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the definition of the smallest box which contains all the points analyzed by this framework if, according to the given precision value, the points are considered to be neither coincident, nor collinear and nor coplanar. This box is centered on the barycenter P of the collection of points. Its sides are parallel to the three vectors V1, V2 and V3, the length of which is the length of the box in the corresponding direction. Note: Vectors V1, V2 and V3 are parallel to the three axes of principal inertia of the system composed of the collection of points where each point is of equal mass. Exceptions Standard_NoSuchObject if, according to the given precision, the points analyzed by this framework are considered to be coincident, collinear or coplanar.
        """
    def IsLinear(self) -> bool: 
        """
        Returns true if, according to the given tolerance, the points analyzed by this framework are colinear. Use the function Line to access the computed result.
        """
    def IsPlanar(self) -> bool: 
        """
        Returns true if, according to the given tolerance, the points analyzed by this framework are coplanar. Use the function Plane to access the computed result.
        """
    def IsPoint(self) -> bool: 
        """
        Returns true if, according to the given tolerance, the points analyzed by this framework are coincident. Use the function Point to access the computed result.
        """
    def IsSpace(self) -> bool: 
        """
        Returns true if, according to the given tolerance value, the points analyzed by this framework are neither coincident, nor collinear, nor coplanar. Use the function Box to query the smallest box that includes the collection of points.
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        Returns the mean line passing near all the points analyzed by this framework if, according to the given precision value, the points are considered to be collinear. Exceptions Standard_NoSuchObject if, according to the given precision, the points analyzed by this framework are considered to be: - coincident, or - not collinear.
        """
    def Plane(self) -> OCP.gp.gp_Pln: 
        """
        Returns the mean plane passing near all the points analyzed by this framework if, according to the given precision, the points are considered to be coplanar. Exceptions Standard_NoSuchObject if, according to the given precision value, the points analyzed by this framework are considered to be: - coincident, or - collinear, or - not coplanar.
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the mean point of all the points analyzed by this framework if, according to the given precision, the points are considered to be coincident. Exceptions Standard_NoSuchObject if, according to the given precision, the points analyzed by this framework are not considered to be coincident.
        """
    def __init__(self,Pnts : OCP.TColgp.TColgp_Array1OfPnt,Tol : float) -> None: ...
    pass
class GProp_PGProps(GProp_GProps):
    """
    A framework for computing the global properties of a set of points. A point mass is attached to each point. The global mass of the system is the sum of each individual mass. By default, the point mass is equal to 1 and the mass of a system composed of N points is equal to N. Warning A framework of this sort provides functions to handle sets of points easily. But, like any GProp_GProps object, by using the Add function, it can theoretically bring together the computed global properties and those of a system more complex than a set of points . The mass of each point and the density of each component of the composed system must be coherent. Note that this coherence cannot be checked. Nonetheless, you are advised to restrict your use of a GProp_PGProps object to a set of points and to create a GProp_GProps object in order to bring together global properties of different systems.
    """
    def Add(self,Item : GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    @overload
    def AddPoint(self,P : OCP.gp.gp_Pnt) -> None: 
        """
        Brings together the global properties already retained by this framework with those induced by the point Pnt. Pnt may be the first point of the current system. A point mass is attached to the point Pnt, it is either equal to 1. or to Density.

        Adds a new point P with its density in the system of points Exceptions Standard_DomainError if the mass value Density is less than gp::Resolution().
        """
    @overload
    def AddPoint(self,P : OCP.gp.gp_Pnt,Density : float) -> None: ...
    @staticmethod
    @overload
    def Barycentre_s(Pnts : OCP.TColgp.TColgp_Array2OfPnt,Density : OCP.TColStd.TColStd_Array2OfReal,G : OCP.gp.gp_Pnt) -> Tuple[float]: 
        """
        Computes the barycentre of a set of points. The density of the points is defaulted to 1.

        Computes the barycentre of a set of points. The density of the points is defaulted to 1.

        Computes the barycentre of a set of points. A density is associated with each point.

        Computes the barycentre of a set of points. A density is associated with each point.
        """
    @staticmethod
    @overload
    def Barycentre_s(Pnts : OCP.TColgp.TColgp_Array1OfPnt,Density : OCP.TColStd.TColStd_Array1OfReal,G : OCP.gp.gp_Pnt) -> Tuple[float]: ...
    @staticmethod
    @overload
    def Barycentre_s(Pnts : OCP.TColgp.TColgp_Array1OfPnt) -> OCP.gp.gp_Pnt: ...
    @staticmethod
    @overload
    def Barycentre_s(Pnts : OCP.TColgp.TColgp_Array2OfPnt) -> OCP.gp.gp_Pnt: ...
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def Mass(self) -> float: 
        """
        Returns the mass of the current system. If no density is attached to the components of the current system the returned value corresponds to : - the total length of the edges of the current system if this framework retains only linear properties, as is the case for example, when using only the LinearProperties function to combine properties of lines from shapes, or - the total area of the faces of the current system if this framework retains only surface properties, as is the case for example, when using only the SurfaceProperties function to combine properties of surfaces from shapes, or - the total volume of the solids of the current system if this framework retains only volume properties, as is the case for example, when using only the VolumeProperties function to combine properties of volumes from solids. Warning A length, an area, or a volume is computed in the current data unit system. The mass of a single object is obtained by multiplying its length, its area or its volume by the given density. You must be consistent with respect to the units used.
        """
    def MatrixOfInertia(self) -> OCP.gp.gp_Mat: 
        """
        returns the matrix of inertia. It is a symmetrical matrix. The coefficients of the matrix are the quadratic moments of inertia.
        """
    def MomentOfInertia(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        computes the moment of inertia of the material system about the axis A.
        """
    def PrincipalProperties(self) -> GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,Pnts : OCP.TColgp.TColgp_Array2OfPnt) -> None: ...
    @overload
    def __init__(self,Pnts : OCP.TColgp.TColgp_Array1OfPnt) -> None: ...
    @overload
    def __init__(self,Pnts : OCP.TColgp.TColgp_Array1OfPnt,Density : OCP.TColStd.TColStd_Array1OfReal) -> None: ...
    @overload
    def __init__(self,Pnts : OCP.TColgp.TColgp_Array2OfPnt,Density : OCP.TColStd.TColStd_Array2OfReal) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GProp_PrincipalProps():
    """
    A framework to present the principal properties of inertia of a system of which global properties are computed by a GProp_GProps object. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This sort of presentation object is created, filled and returned by the function PrincipalProperties for any GProp_GProps object, and can be queried to access the result. Note: The system whose principal properties of inertia are returned by this framework is referred to as the current system. The current system, however, is retained neither by this presentation framework nor by the GProp_GProps object which activates it.
    """
    def FirstAxisOfInertia(self) -> OCP.gp.gp_Vec: 
        """
        returns the first axis of inertia.
        """
    @overload
    def HasSymmetryAxis(self,aTol : float) -> bool: 
        """
        returns true if the geometric system has an axis of symmetry. For comparing moments relative tolerance 1.e-10 is used. Usually it is enough for objects, restricted by faces with analitycal geometry.

        returns true if the geometric system has an axis of symmetry. aTol is relative tolerance for checking equality of moments If aTol == 0, relative tolerance is ~ 1.e-16 (Epsilon(I))
        """
    @overload
    def HasSymmetryAxis(self) -> bool: ...
    @overload
    def HasSymmetryPoint(self) -> bool: 
        """
        returns true if the geometric system has a point of symmetry. For comparing moments relative tolerance 1.e-10 is used. Usually it is enough for objects, restricted by faces with analitycal geometry.

        returns true if the geometric system has a point of symmetry. aTol is relative tolerance for checking equality of moments If aTol == 0, relative tolerance is ~ 1.e-16 (Epsilon(I))
        """
    @overload
    def HasSymmetryPoint(self,aTol : float) -> bool: ...
    def Moments(self) -> Tuple[float, float, float]: 
        """
        Ixx, Iyy and Izz return the principal moments of inertia in the current system. Notes : - If the current system has an axis of symmetry, two of the three values Ixx, Iyy and Izz are equal. They indicate which eigen vectors define an infinity of axes of principal inertia. - If the current system has a center of symmetry, Ixx, Iyy and Izz are equal.
        """
    def RadiusOfGyration(self) -> Tuple[float, float, float]: 
        """
        Returns the principal radii of gyration Rxx, Ryy and Rzz are the radii of gyration of the current system about its three principal axes of inertia. Note that: - If the current system has an axis of symmetry, two of the three values Rxx, Ryy and Rzz are equal. - If the current system has a center of symmetry, Rxx, Ryy and Rzz are equal.
        """
    def SecondAxisOfInertia(self) -> OCP.gp.gp_Vec: 
        """
        returns the second axis of inertia.
        """
    def ThirdAxisOfInertia(self) -> OCP.gp.gp_Vec: 
        """
        returns the third axis of inertia. This and the above functions return the first, second or third eigen vector of the matrix of inertia of the current system. The first, second and third principal axis of inertia pass through the center of mass of the current system. They are respectively parallel to these three eigen vectors. Note that: - If the current system has an axis of symmetry, any axis is an axis of principal inertia if it passes through the center of mass of the system, and runs parallel to a linear combination of the two eigen vectors of the matrix of inertia, corresponding to the two eigen values which are equal. If the current system has a center of symmetry, any axis passing through the center of mass of the system is an axis of principal inertia. Use the functions HasSymmetryAxis and HasSymmetryPoint to check these particular cases, where the returned eigen vectors define an infinity of principal axis of inertia. - The Moments function can be used to know which of the three eigen vectors corresponds to the two eigen values which are equal.
        """
    def __init__(self) -> None: ...
    pass
class GProp_SelGProps(GProp_GProps):
    """
    Computes the global properties of a bounded elementary surface in 3d (surface of the gp package)
    """
    def Add(self,Item : GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def Mass(self) -> float: 
        """
        Returns the mass of the current system. If no density is attached to the components of the current system the returned value corresponds to : - the total length of the edges of the current system if this framework retains only linear properties, as is the case for example, when using only the LinearProperties function to combine properties of lines from shapes, or - the total area of the faces of the current system if this framework retains only surface properties, as is the case for example, when using only the SurfaceProperties function to combine properties of surfaces from shapes, or - the total volume of the solids of the current system if this framework retains only volume properties, as is the case for example, when using only the VolumeProperties function to combine properties of volumes from solids. Warning A length, an area, or a volume is computed in the current data unit system. The mass of a single object is obtained by multiplying its length, its area or its volume by the given density. You must be consistent with respect to the units used.
        """
    def MatrixOfInertia(self) -> OCP.gp.gp_Mat: 
        """
        returns the matrix of inertia. It is a symmetrical matrix. The coefficients of the matrix are the quadratic moments of inertia.
        """
    def MomentOfInertia(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        computes the moment of inertia of the material system about the axis A.
        """
    @overload
    def Perform(self,S : OCP.gp.gp_Sphere,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Perform(self,S : OCP.gp.gp_Cone,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Torus,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Cylinder,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float) -> None: ...
    def PrincipalProperties(self) -> GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def SetLocation(self,SLocation : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,S : OCP.gp.gp_Cylinder,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float,SLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Torus,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float,SLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float,SLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Cone,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float,SLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class GProp_UndefinedAxis(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.GProp', '__weakref__': <attribute '__weakref__' of 'GProp_UndefinedAxis' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'GProp_UndefinedAxis' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class GProp_ValueType():
    """
    Algorithmes :

    Members:

      GProp_Mass

      GProp_CenterMassX

      GProp_CenterMassY

      GProp_CenterMassZ

      GProp_InertiaXX

      GProp_InertiaYY

      GProp_InertiaZZ

      GProp_InertiaXY

      GProp_InertiaXZ

      GProp_InertiaYZ

      GProp_Unknown
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
    GProp_CenterMassX: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassX: 1>
    GProp_CenterMassY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassY: 2>
    GProp_CenterMassZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassZ: 3>
    GProp_InertiaXX: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXX: 4>
    GProp_InertiaXY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXY: 7>
    GProp_InertiaXZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXZ: 8>
    GProp_InertiaYY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaYY: 5>
    GProp_InertiaYZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaYZ: 9>
    GProp_InertiaZZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaZZ: 6>
    GProp_Mass: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_Mass: 0>
    GProp_Unknown: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_Unknown: 10>
    __entries: dict # value = {'GProp_Mass': (<GProp_ValueType.GProp_Mass: 0>, None), 'GProp_CenterMassX': (<GProp_ValueType.GProp_CenterMassX: 1>, None), 'GProp_CenterMassY': (<GProp_ValueType.GProp_CenterMassY: 2>, None), 'GProp_CenterMassZ': (<GProp_ValueType.GProp_CenterMassZ: 3>, None), 'GProp_InertiaXX': (<GProp_ValueType.GProp_InertiaXX: 4>, None), 'GProp_InertiaYY': (<GProp_ValueType.GProp_InertiaYY: 5>, None), 'GProp_InertiaZZ': (<GProp_ValueType.GProp_InertiaZZ: 6>, None), 'GProp_InertiaXY': (<GProp_ValueType.GProp_InertiaXY: 7>, None), 'GProp_InertiaXZ': (<GProp_ValueType.GProp_InertiaXZ: 8>, None), 'GProp_InertiaYZ': (<GProp_ValueType.GProp_InertiaYZ: 9>, None), 'GProp_Unknown': (<GProp_ValueType.GProp_Unknown: 10>, None)}
    __members__: dict # value = {'GProp_Mass': <GProp_ValueType.GProp_Mass: 0>, 'GProp_CenterMassX': <GProp_ValueType.GProp_CenterMassX: 1>, 'GProp_CenterMassY': <GProp_ValueType.GProp_CenterMassY: 2>, 'GProp_CenterMassZ': <GProp_ValueType.GProp_CenterMassZ: 3>, 'GProp_InertiaXX': <GProp_ValueType.GProp_InertiaXX: 4>, 'GProp_InertiaYY': <GProp_ValueType.GProp_InertiaYY: 5>, 'GProp_InertiaZZ': <GProp_ValueType.GProp_InertiaZZ: 6>, 'GProp_InertiaXY': <GProp_ValueType.GProp_InertiaXY: 7>, 'GProp_InertiaXZ': <GProp_ValueType.GProp_InertiaXZ: 8>, 'GProp_InertiaYZ': <GProp_ValueType.GProp_InertiaYZ: 9>, 'GProp_Unknown': <GProp_ValueType.GProp_Unknown: 10>}
    pass
class GProp_VelGProps(GProp_GProps):
    """
    Computes the global properties and the volume of a geometric solid (3D closed region of space) The solid can be elementary(definition in the gp package)
    """
    def Add(self,Item : GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def Mass(self) -> float: 
        """
        Returns the mass of the current system. If no density is attached to the components of the current system the returned value corresponds to : - the total length of the edges of the current system if this framework retains only linear properties, as is the case for example, when using only the LinearProperties function to combine properties of lines from shapes, or - the total area of the faces of the current system if this framework retains only surface properties, as is the case for example, when using only the SurfaceProperties function to combine properties of surfaces from shapes, or - the total volume of the solids of the current system if this framework retains only volume properties, as is the case for example, when using only the VolumeProperties function to combine properties of volumes from solids. Warning A length, an area, or a volume is computed in the current data unit system. The mass of a single object is obtained by multiplying its length, its area or its volume by the given density. You must be consistent with respect to the units used.
        """
    def MatrixOfInertia(self) -> OCP.gp.gp_Mat: 
        """
        returns the matrix of inertia. It is a symmetrical matrix. The coefficients of the matrix are the quadratic moments of inertia.
        """
    def MomentOfInertia(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        computes the moment of inertia of the material system about the axis A.
        """
    @overload
    def Perform(self,S : OCP.gp.gp_Torus,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Perform(self,S : OCP.gp.gp_Cylinder,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Sphere,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float) -> None: ...
    @overload
    def Perform(self,S : OCP.gp.gp_Cone,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float) -> None: ...
    def PrincipalProperties(self) -> GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def SetLocation(self,VLocation : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,S : OCP.gp.gp_Torus,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Sphere,Teta1 : float,Teta2 : float,Alpha1 : float,Alpha2 : float,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Cylinder,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : OCP.gp.gp_Cone,Alpha1 : float,Alpha2 : float,Z1 : float,Z2 : float,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
GProp_CenterMassX: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassX: 1>
GProp_CenterMassY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassY: 2>
GProp_CenterMassZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_CenterMassZ: 3>
GProp_InertiaXX: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXX: 4>
GProp_InertiaXY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXY: 7>
GProp_InertiaXZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaXZ: 8>
GProp_InertiaYY: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaYY: 5>
GProp_InertiaYZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaYZ: 9>
GProp_InertiaZZ: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_InertiaZZ: 6>
GProp_Line: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Line: 1>
GProp_Mass: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_Mass: 0>
GProp_None: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_None: 4>
GProp_Plane: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Plane: 0>
GProp_Point: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Point: 2>
GProp_Space: OCP.GProp.GProp_EquaType # value = <GProp_EquaType.GProp_Space: 3>
GProp_Unknown: OCP.GProp.GProp_ValueType # value = <GProp_ValueType.GProp_Unknown: 10>
