import OCP.BRepGProp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.math
import OCP.BRepAdaptor
import OCP.TopLoc
import OCP.TopoDS
import OCP.Poly
import OCP.gp
import OCP.TopAbs
import OCP.TColgp
import OCP.GeomAbs
import OCP.GProp
import BRepGProp_MeshProps
import OCP.TColStd
__all__  = [
"BRepGProp",
"BRepGProp_Cinert",
"BRepGProp_Domain",
"BRepGProp_EdgeTool",
"BRepGProp_Face",
"BRepGProp_MeshCinert",
"BRepGProp_MeshProps",
"BRepGProp_Sinert",
"BRepGProp_TFunction",
"BRepGProp_UFunction",
"BRepGProp_Vinert",
"BRepGProp_VinertGK"
]
class BRepGProp():
    """
    Provides global functions to compute a shape's global properties for lines, surfaces or volumes, and bring them together with the global properties already computed for a geometric system. The global properties computed for a system are : - its mass, - its center of mass, - its matrix of inertia, - its moment about an axis, - its radius of gyration about an axis, - and its principal properties of inertia such as principal axis, principal moments, principal radius of gyration.
    """
    @staticmethod
    def LinearProperties_s(S : OCP.TopoDS.TopoDS_Shape,LProps : OCP.GProp.GProp_GProps,SkipShared : bool=False,UseTriangulation : bool=False) -> None: 
        """
        Computes the linear global properties of the shape S, i.e. the global properties induced by each edge of the shape S, and brings them together with the global properties still retained by the framework LProps. If the current system of LProps was empty, its global properties become equal to the linear global properties of S. For this computation no linear density is attached to the edges. So, for example, the added mass corresponds to the sum of the lengths of the edges of S. The density of the composed systems, i.e. that of each component of the current system of LProps, and that of S which is considered to be equal to 1, must be coherent. Note that this coherence cannot be checked. You are advised to use a separate framework for each density, and then to bring these frameworks together into a global one. The point relative to which the inertia of the system is computed is the reference point of the framework LProps. Note: if your programming ensures that the framework LProps retains only linear global properties (brought together for example, by the function LinearProperties) for objects the density of which is equal to 1 (or is not defined), the function Mass will return the total length of edges of the system analysed by LProps. Warning No check is performed to verify that the shape S retains truly linear properties. If S is simply a vertex, it is not considered to present any additional global properties. SkipShared is a special flag, which allows taking in calculation shared topological entities or not. For ex., if SkipShared = True, edges, shared by two or more faces, are taken into calculation only once. If we have cube with sizes 1, 1, 1, its linear properties = 12 for SkipEdges = true and 24 for SkipEdges = false. UseTriangulation is a special flag, which defines preferable source of geometry data. If UseTriangulation = Standard_False, exact geometry objects (curves) are used, otherwise polygons of triangulation are used first.
        """
    @staticmethod
    @overload
    def SurfaceProperties_s(S : OCP.TopoDS.TopoDS_Shape,SProps : OCP.GProp.GProp_GProps,Eps : float,SkipShared : bool=False) -> float: 
        """
        Computes the surface global properties of the shape S, i.e. the global properties induced by each face of the shape S, and brings them together with the global properties still retained by the framework SProps. If the current system of SProps was empty, its global properties become equal to the surface global properties of S. For this computation, no surface density is attached to the faces. Consequently, the added mass corresponds to the sum of the areas of the faces of S. The density of the component systems, i.e. that of each component of the current system of SProps, and that of S which is considered to be equal to 1, must be coherent. Note that this coherence cannot be checked. You are advised to use a framework for each different value of density, and then to bring these frameworks together into a global one. The point relative to which the inertia of the system is computed is the reference point of the framework SProps. Note : if your programming ensures that the framework SProps retains only surface global properties, brought together, for example, by the function SurfaceProperties, for objects the density of which is equal to 1 (or is not defined), the function Mass will return the total area of faces of the system analysed by SProps. Warning No check is performed to verify that the shape S retains truly surface properties. If S is simply a vertex, an edge or a wire, it is not considered to present any additional global properties. SkipShared is a special flag, which allows taking in calculation shared topological entities or not. For ex., if SkipShared = True, faces, shared by two or more shells, are taken into calculation only once. UseTriangulation is a special flag, which defines preferable source of geometry data. If UseTriangulation = Standard_False, exact geometry objects (surfaces) are used, otherwise face triangulations are used first.

        Updates <SProps> with the shape <S>, that contains its principal properties. The surface properties of all the faces in <S> are computed. Adaptive 2D Gauss integration is used. Parameter Eps sets maximal relative error of computed mass (area) for each face. Error is calculated as Abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values for two successive steps of adaptive integration. Method returns estimation of relative error reached for whole shape. WARNING: if Eps > 0.001 algorithm performs non-adaptive integration. SkipShared is a special flag, which allows taking in calculation shared topological entities or not For ex., if SkipShared = True, faces, shared by two or more shells, are taken into calculation only once.
        """
    @staticmethod
    @overload
    def SurfaceProperties_s(S : OCP.TopoDS.TopoDS_Shape,SProps : OCP.GProp.GProp_GProps,SkipShared : bool=False,UseTriangulation : bool=False) -> None: ...
    @staticmethod
    @overload
    def VolumePropertiesGK_s(S : OCP.TopoDS.TopoDS_Shape,VProps : OCP.GProp.GProp_GProps,Eps : float=0.001,OnlyClosed : bool=False,IsUseSpan : bool=False,CGFlag : bool=False,IFlag : bool=False,SkipShared : bool=False) -> float: 
        """
        Updates <VProps> with the shape <S>, that contains its principal properties. The volume properties of all the FORWARD and REVERSED faces in <S> are computed. If OnlyClosed is True then computed faces must belong to closed Shells. Adaptive 2D Gauss integration is used. Parameter IsUseSpan says if it is necessary to define spans on a face. This option has an effect only for BSpline faces. Parameter Eps sets maximal relative error of computed property for each face. Error is delivered by the adaptive Gauss-Kronrod method of integral computation that is used for properties computation. Method returns estimation of relative error reached for whole shape. Returns negative value if the computation is failed. SkipShared is a special flag, which allows taking in calculation shared topological entities or not. For ex., if SkipShared = True, the volumes formed by the equal (the same TShape, location and orientation) faces are taken into calculation only once.

        None
        """
    @staticmethod
    @overload
    def VolumePropertiesGK_s(S : OCP.TopoDS.TopoDS_Shape,VProps : OCP.GProp.GProp_GProps,thePln : OCP.gp.gp_Pln,Eps : float=0.001,OnlyClosed : bool=False,IsUseSpan : bool=False,CGFlag : bool=False,IFlag : bool=False,SkipShared : bool=False) -> float: ...
    @staticmethod
    @overload
    def VolumeProperties_s(S : OCP.TopoDS.TopoDS_Shape,VProps : OCP.GProp.GProp_GProps,OnlyClosed : bool=False,SkipShared : bool=False,UseTriangulation : bool=False) -> None: 
        """
        Computes the global volume properties of the solid S, and brings them together with the global properties still retained by the framework VProps. If the current system of VProps was empty, its global properties become equal to the global properties of S for volume. For this computation, no volume density is attached to the solid. Consequently, the added mass corresponds to the volume of S. The density of the component systems, i.e. that of each component of the current system of VProps, and that of S which is considered to be equal to 1, must be coherent to each other. Note that this coherence cannot be checked. You are advised to use a separate framework for each density, and then to bring these frameworks together into a global one. The point relative to which the inertia of the system is computed is the reference point of the framework VProps. Note: if your programming ensures that the framework VProps retains only global properties of volume (brought together for example, by the function VolumeProperties) for objects the density of which is equal to 1 (or is not defined), the function Mass will return the total volume of the solids of the system analysed by VProps. Warning The shape S must represent an object whose global volume properties can be computed. It may be a finite solid, or a series of finite solids all oriented in a coherent way. Nonetheless, S must be exempt of any free boundary. Note that these conditions of coherence are not checked by this algorithm, and results will be false if they are not respected. SkipShared a is special flag, which allows taking in calculation shared topological entities or not. For ex., if SkipShared = True, the volumes formed by the equal (the same TShape, location and orientation) faces are taken into calculation only once. UseTriangulation is a special flag, which defines preferable source of geometry data. If UseTriangulation = Standard_False, exact geometry objects (surfaces) are used, otherwise face triangulations are used first.

        Updates <VProps> with the shape <S>, that contains its principal properties. The volume properties of all the FORWARD and REVERSED faces in <S> are computed. If OnlyClosed is True then computed faces must belong to closed Shells. Adaptive 2D Gauss integration is used. Parameter Eps sets maximal relative error of computed mass (volume) for each face. Error is calculated as Abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values for two successive steps of adaptive integration. Method returns estimation of relative error reached for whole shape. WARNING: if Eps > 0.001 algorithm performs non-adaptive integration. SkipShared is a special flag, which allows taking in calculation shared topological entities or not. For ex., if SkipShared = True, the volumes formed by the equal (the same TShape, location and orientation) faces are taken into calculation only once.
        """
    @staticmethod
    @overload
    def VolumeProperties_s(S : OCP.TopoDS.TopoDS_Shape,VProps : OCP.GProp.GProp_GProps,Eps : float,OnlyClosed : bool=False,SkipShared : bool=False) -> float: ...
    def __init__(self) -> None: ...
    pass
class BRepGProp_Cinert(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of bounded curves in 3D space. The curve must have at least a continuity C1. It can be a curve as defined in the template CurveTool from package GProp. This template gives the minimum of methods required to evaluate the global properties of a curve 3D with the algorithms of GProp.
    """
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
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
    def Perform(self,C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> None: 
        """
        None
        """
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.BRepAdaptor.BRepAdaptor_Curve,CLocation : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepGProp_Domain():
    """
    Arc iterator. Returns only Forward and Reversed edges from the face in an undigested order.
    """
    @overload
    def Init(self) -> None: 
        """
        Initializes the domain with the face.

        Initializes the exploration with the face already set.

        Initializes the domain with the face.

        Initializes the exploration with the face already set.
        """
    @overload
    def Init(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def More(self) -> bool: 
        """
        Returns True if there is another arc of curve in the list.

        Returns True if there is another arc of curve in the list.
        """
    def Next(self) -> None: 
        """
        Sets the index of the arc iterator to the next arc of curve.
        """
    def Value(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        Returns the current edge.

        Returns the current edge.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepGProp_EdgeTool():
    """
    Provides the required methods to instantiate CGProps from GProp with a Curve from BRepAdaptor.
    """
    @staticmethod
    def D1_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float,P : OCP.gp.gp_Pnt,V1 : OCP.gp.gp_Vec) -> None: 
        """
        Returns the point of parameter U and the first derivative at this point.
        """
    @staticmethod
    def FirstParameter_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> float: 
        """
        Returns the parametric value of the start point of the curve. The curve is oriented from the start point to the end point.
        """
    @staticmethod
    def IntegrationOrder_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> int: 
        """
        Returns the number of Gauss points required to do the integration with a good accuracy using the Gauss method. For a polynomial curve of degree n the maxima of accuracy is obtained with an order of integration equal to 2*n-1.
        """
    @staticmethod
    def Intervals_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def LastParameter_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve) -> float: 
        """
        Returns the parametric value of the end point of the curve. The curve is oriented from the start point to the end point.
        """
    @staticmethod
    def NbIntervals_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(me) >= <S>
        """
    @staticmethod
    def Value_s(C : OCP.BRepAdaptor.BRepAdaptor_Curve,U : float) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of parameter U on the loaded curve.
        """
    def __init__(self) -> None: ...
    pass
class BRepGProp_Face():
    """
    None
    """
    def Bounds(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parametric bounds of the Face.
        """
    def D12d(self,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point of parameter U and the first derivative at this point of a boundary curve.

        Returns the point of parameter U and the first derivative at this point of a boundary curve.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the parametric value of the start point of the current arc of curve.

        Returns the parametric value of the start point of the current arc of curve.
        """
    def GetFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the TopoDS face.

        Returns the TopoDS face.
        """
    def GetTKnots(self,theTMin : float,theTMax : float,theTKnots : OCP.TColStd.TColStd_HArray1OfReal) -> Any: 
        """
        Returns an array of combination of T knots of the arc and V knots of the face. The first and last elements of the array will be theTMin and theTMax. The middle elements will be the Knots of the arc and the values of parameters of arc on which the value points have V coordinates close to V knots of face. All the parameter will be greater then theTMin and lower then theTMax in increasing order. If the face is not a BSpline, the array initialized with theTMin and theTMax only.
        """
    def GetUKnots(self,theUMin : float,theUMax : float,theUKnots : OCP.TColStd.TColStd_HArray1OfReal) -> Any: 
        """
        Returns an array of U knots of the face. The first and last elements of the array will be theUMin and theUMax. The middle elements will be the U Knots of the face greater then theUMin and lower then theUMax in increasing order. If the face is not a BSpline, the array initialized with theUMin and theUMax only.
        """
    def IntegrationOrder(self) -> int: 
        """
        Returns the number of points required to do the integration along the parameter of curve.
        """
    def LIntOrder(self,Eps : float) -> int: 
        """
        None
        """
    def LIntSubs(self) -> int: 
        """
        None
        """
    def LKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def LastParameter(self) -> float: 
        """
        Returns the parametric value of the end point of the current arc of curve.

        Returns the parametric value of the end point of the current arc of curve.
        """
    @overload
    def Load(self,IsFirstParam : bool,theIsoType : OCP.GeomAbs.GeomAbs_IsoType) -> None: 
        """
        None

        Loading the boundary arc. Returns FALSE if edge has no P-Curve.

        Loading the boundary arc. This arc is either a top, bottom, left or right bound of a UV rectangle in which the parameters of surface are defined. If IsFirstParam is equal to Standard_True, the face is initialized by either left of bottom bound. Otherwise it is initialized by the top or right one. If theIsoType is equal to GeomAbs_IsoU, the face is initialized with either left or right bound. Otherwise - with either top or bottom one.
        """
    @overload
    def Load(self,E : OCP.TopoDS.TopoDS_Edge) -> bool: ...
    @overload
    def Load(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    def NaturalRestriction(self) -> bool: 
        """
        Returns Standard_True if the face is not trimmed.

        Returns Standard_True if the face is not trimmed.
        """
    def Normal(self,U : float,V : float,P : OCP.gp.gp_Pnt,VNor : OCP.gp.gp_Vec) -> None: 
        """
        Computes the point of parameter U, V on the Face <S> and the normal to the face at this point.
        """
    def SIntOrder(self,Eps : float) -> int: 
        """
        None
        """
    def SUIntSubs(self) -> int: 
        """
        None
        """
    def SVIntSubs(self) -> int: 
        """
        None
        """
    def UIntegrationOrder(self) -> int: 
        """
        Returns the number of points required to do the integration in the U parametric direction with a good accuracy.
        """
    def UKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def VIntegrationOrder(self) -> int: 
        """
        None
        """
    def VKnots(self,Knots : OCP.TColStd.TColStd_Array1OfReal) -> None: 
        """
        None
        """
    def Value2d(self,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the value of the boundary curve of the face.

        Returns the value of the boundary curve of the face.
        """
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,IsUseSpan : bool=False) -> None: ...
    @overload
    def __init__(self,IsUseSpan : bool=False) -> None: ...
    pass
class BRepGProp_MeshCinert(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of of polylines represented by set of points. This class is used for computation of global properties of edge, which has no exact geometry (3d or 2d curve), but has any of allowed polygons.
    """
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
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
    def Perform(self,theNodes : OCP.TColgp.TColgp_Array1OfPnt) -> None: 
        """
        Computes the global properties of of polylines represented by set of points.
        """
    @staticmethod
    def PreparePolygon_s(theE : OCP.TopoDS.TopoDS_Edge,thePolyg : OCP.TColgp.TColgp_HArray1OfPnt) -> None: 
        """
        Prepare set of 3d points on base of any available edge polygons: 3D polygon, polygon on triangulation, 2d polygon on surface If edge has no polygons, array thePolyg is left unchanged
        """
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
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
    def __init__(self) -> None: ...
    pass
class BRepGProp_MeshProps(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of a surface mesh. The mesh can be interpreted as just a surface or as a piece of volume limited by this surface.
    """
    class BRepGProp_MeshObjType_e():
        """
        Describes types of geometric objects. - Vinert is 3D closed region of space delimited with Point and surface mesh; - Sinert is surface mesh in 3D space.

        Members:

          Vinert

          Sinert
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
        Sinert: OCP.BRepGProp.BRepGProp_MeshObjType_e # value = <BRepGProp_MeshObjType_e.Sinert: 1>
        Vinert: OCP.BRepGProp.BRepGProp_MeshObjType_e # value = <BRepGProp_MeshObjType_e.Vinert: 0>
        __entries: dict # value = {'Vinert': (<BRepGProp_MeshObjType_e.Vinert: 0>, None), 'Sinert': (<BRepGProp_MeshObjType_e.Sinert: 1>, None)}
        __members__: dict # value = {'Vinert': <BRepGProp_MeshObjType_e.Vinert: 0>, 'Sinert': <BRepGProp_MeshObjType_e.Sinert: 1>}
        pass
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    @staticmethod
    def CalculateProps_s(p1 : OCP.gp.gp_Pnt,p2 : OCP.gp.gp_Pnt,p3 : OCP.gp.gp_Pnt,Apex : OCP.gp.gp_Pnt,isVolume : bool,GProps : float,NbGaussPoints : int,GaussPnts : float) -> None: 
        """
        Computes the global properties of triangle {p1, p2, p3} relatively point Apex If isVolume = true, volume properties are calculated otherwise - surface ones
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def GetMeshObjType(self) -> BRepGProp_MeshProps.BRepGProp_MeshObjType_e: 
        """
        Get type of mesh object
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
    def Perform(self,theMesh : OCP.Poly.Poly_Triangulation,theLoc : OCP.TopLoc.TopLoc_Location,theOri : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Computes the global properties of a surface mesh of 3D space. Calculation of surface properties is performed by numerical integration over triangle surfaces using Gauss cubature formulas. Depending on the mesh object type used in constructor this method can calculate the surface or volume properties of the mesh.

        None
        """
    @overload
    def Perform(self,theMesh : OCP.Poly.Poly_Triangulation,theOri : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def SetLocation(self,theLocation : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the point relative which the calculation is to be done
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    def __init__(self,theType : BRepGProp_MeshProps.BRepGProp_MeshObjType_e) -> None: ...
    Sinert: OCP.BRepGProp.BRepGProp_MeshObjType_e # value = <BRepGProp_MeshObjType_e.Sinert: 1>
    Vinert: OCP.BRepGProp.BRepGProp_MeshObjType_e # value = <BRepGProp_MeshObjType_e.Vinert: 0>
    pass
class BRepGProp_Sinert(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of a face in 3D space. The face 's requirements to evaluate the global properties are defined in the template FaceTool from package GProp.
    """
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def GetEpsilon(self) -> float: 
        """
        If previously used method contained Eps parameter get actual relative error of the computation, else return 1.0.
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
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Perform(self,S : BRepGProp_Face) -> None: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,Eps : float) -> float: ...
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
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
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,SLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,SLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,SLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,SLocation : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepGProp_TFunction(OCP.math.math_Function):
    """
    This class represents the integrand function for the outer integral computation. The returned value represents the integral of UFunction. It depends on the value type and the flag IsByPoint.
    """
    def AbsolutError(self) -> float: 
        """
        Returns the absolut reached error of all values computation since the last call of GetStateNumber method.

        Returns the absolut reached error of all values computation since the last call of GetStateNumber method.
        """
    def ErrorReached(self) -> float: 
        """
        Returns the relative reached error of all values computation since the last call of GetStateNumber method.

        Returns the relative reached error of all values computation since the last call of GetStateNumber method.
        """
    def GetStateNumber(self) -> int: 
        """
        Redefined method. Remembers the error reached during computation of integral values since the object creation or the last call of GetStateNumber. It is invoked in each algorithm from the package math. Particularly in the algorithm math_KronrodSingleIntegration that is used to compute the integral of TFunction.
        """
    def Init(self) -> None: 
        """
        None
        """
    def SetNbKronrodPoints(self,theNbPoints : int) -> None: 
        """
        Setting the expected number of Kronrod points for the outer integral computation. This number is required for computation of a value of tolerance for inner integral computation. After GetStateNumber method call, this number is recomputed by the same law as in math_KronrodSingleIntegration, i.e. next number of points is equal to the current number plus a square root of the current number. If the law in math_KronrodSingleIntegration is changed, the modification algo should be modified accordingly.

        Setting the expected number of Kronrod points for the outer integral computation. This number is required for computation of a value of tolerance for inner integral computation. After GetStateNumber method call, this number is recomputed by the same law as in math_KronrodSingleIntegration, i.e. next number of points is equal to the current number plus a square root of the current number. If the law in math_KronrodSingleIntegration is changed, the modification algo should be modified accordingly.
        """
    @overload
    def SetTolerance(self,aTol : float) -> None: 
        """
        Setting the tolerance for inner integration

        Setting the tolerance for inner integration
        """
    @overload
    def SetTolerance(self,theTolerance : float) -> None: ...
    @overload
    def SetValueType(self,theType : OCP.GProp.GProp_ValueType) -> None: 
        """
        Setting the type of the value to be returned. This parameter is directly passed to the UFunction.

        Setting the type of the value to be returned. This parameter is directly passed to the UFunction.
        """
    @overload
    def SetValueType(self,aType : OCP.GProp.GProp_ValueType) -> None: ...
    def Value(self,X : float,F : float) -> bool: 
        """
        Returns a value of the function. The value represents an integral of UFunction. It is computed with the predefined tolerance using the adaptive Gauss-Kronrod method.
        """
    def __init__(self,theSurface : BRepGProp_Face,theVertex : OCP.gp.gp_Pnt,IsByPoint : bool,theCoeffs : float,theUMin : float,theTolerance : float) -> None: ...
    pass
class BRepGProp_UFunction(OCP.math.math_Function):
    """
    This class represents the integrand function for computation of an inner integral. The returned value depends on the value type and the flag IsByPoint.
    """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def SetVParam(self,theVParam : float) -> None: 
        """
        Setting the V parameter that is constant during the integral computation.

        Setting the V parameter that is constant during the integral computation.
        """
    def SetValueType(self,theType : OCP.GProp.GProp_ValueType) -> None: 
        """
        Setting the type of the value to be returned.

        Setting the type of the value to be returned.
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        Returns a value of the function.
        """
    def __init__(self,theSurface : BRepGProp_Face,theVertex : OCP.gp.gp_Pnt,IsByPoint : bool,theCoeffs : float) -> None: ...
    pass
class BRepGProp_Vinert(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of a geometric solid (3D closed region of space) delimited with : . a surface . a point and a surface . a plane and a surface
    """
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def GetEpsilon(self) -> float: 
        """
        If previously used methods containe Eps parameter gets actual relative error of the computation, else returns 1.0.
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
    def Perform(self,S : BRepGProp_Face,O : OCP.gp.gp_Pnt) -> None: 
        """
        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None

        None
        """
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def Perform(self,S : BRepGProp_Face,Pl : OCP.gp.gp_Pln,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,O : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,O : OCP.gp.gp_Pnt,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain) -> None: ...
    @overload
    def Perform(self,S : BRepGProp_Face,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,O : OCP.gp.gp_Pnt,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,D : BRepGProp_Domain,Pl : OCP.gp.gp_Pln,Eps : float) -> float: ...
    @overload
    def Perform(self,S : BRepGProp_Face,Pl : OCP.gp.gp_Pln) -> None: ...
    @overload
    def Perform(self,S : BRepGProp_Face) -> None: ...
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
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
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,O : OCP.gp.gp_Pnt,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,Pl : OCP.gp.gp_Pln,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,O : OCP.gp.gp_Pnt,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,Pl : OCP.gp.gp_Pln,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,O : OCP.gp.gp_Pnt,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,Pl : OCP.gp.gp_Pln,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,Pl : OCP.gp.gp_Pln,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,VLocation : OCP.gp.gp_Pnt,Eps : float) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,O : OCP.gp.gp_Pnt,VLocation : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,S : BRepGProp_Face,D : BRepGProp_Domain,VLocation : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepGProp_VinertGK(OCP.GProp.GProp_GProps):
    """
    Computes the global properties of a geometric solid (3D closed region of space) delimited with : - a point and a surface - a plane and a surface
    """
    def Add(self,Item : OCP.GProp.GProp_GProps,Density : float=1.0) -> None: 
        """
        Either - initializes the global properties retained by this framework from those retained by the framework Item, or - brings together the global properties still retained by this framework with those retained by the framework Item. The value Density, which is 1.0 by default, is used as the density of the system analysed by Item. Sometimes the density will have already been given at the time of construction of the framework Item. This may be the case for example, if Item is a GProp_PGProps framework built to compute the global properties of a set of points ; or another GProp_GProps object which already retains composite global properties. In these cases the real density was perhaps already taken into account at the time of construction of Item. Note that this is not checked: if the density of parts of the system is taken into account two or more times, results of the computation will be false. Notes : - The point relative to which the inertia of Item is computed (i.e. the reference point of Item) may be different from the reference point in this framework. Huygens' theorem is applied automatically to transfer inertia values to the reference point in this framework. - The function Add is used once per component of the system. After that, you use the interrogation functions available to access values computed for the system. - The system whose global properties are already brought together by this framework is referred to as the current system. However, the current system is not retained by this framework, which maintains only its global properties. Exceptions Standard_DomainError if Density is less than or equal to gp::Resolution().
        """
    def CentreOfMass(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.
        """
    def GetErrorReached(self) -> float: 
        """
        Returns the relative reached computation error.
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
    def Perform(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: 
        """
        Computes the global properties of a region of 3D space delimited with the naturally restricted surface and the point VLocation.

        Computes the global properties of a region of 3D space delimited with the naturally restricted surface and the point VLocation. The inertia is computed with respect to thePoint.

        Computes the global properties of a region of 3D space delimited with the surface bounded by the domain and the point VLocation.

        Computes the global properties of a region of 3D space delimited with the surface bounded by the domain and the point VLocation. The inertia is computed with respect to thePoint.

        Computes the global properties of a region of 3D space delimited with the naturally restricted surface and the plane.

        Computes the global properties of a region of 3D space delimited with the surface bounded by the domain and the plane.
        """
    @overload
    def Perform(self,theSurface : BRepGProp_Face,thePlane : OCP.gp.gp_Pln,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: ...
    @overload
    def Perform(self,theSurface : BRepGProp_Face,thePoint : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: ...
    @overload
    def Perform(self,theSurface : BRepGProp_Face,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: ...
    @overload
    def Perform(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,thePlane : OCP.gp.gp_Pln,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: ...
    @overload
    def Perform(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,thePoint : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> float: ...
    def PrincipalProperties(self) -> OCP.GProp.GProp_PrincipalProps: 
        """
        Computes the principal properties of inertia of the current system. There is always a set of axes for which the products of inertia of a geometric system are equal to 0; i.e. the matrix of inertia of the system is diagonal. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. This function computes the eigen values and the eigen vectors of the matrix of inertia of the system. Results are stored by using a presentation framework of principal properties of inertia (GProp_PrincipalProps object) which may be queried to access the value sought.
        """
    def RadiusOfGyration(self,A : OCP.gp.gp_Ax1) -> float: 
        """
        Returns the radius of gyration of the current system about the axis A.
        """
    def SetLocation(self,theLocation : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the vertex that delimit 3D closed region of space.
        """
    def StaticMoments(self) -> Tuple[float, float, float]: 
        """
        Returns Ix, Iy, Iz, the static moments of inertia of the current system; i.e. the moments of inertia about the three axes of the Cartesian coordinate system.
        """
    @overload
    def __init__(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,thePlane : OCP.gp.gp_Pln,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    @overload
    def __init__(self,theSurface : BRepGProp_Face,thePlane : OCP.gp.gp_Pln,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    @overload
    def __init__(self,theSurface : BRepGProp_Face,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    @overload
    def __init__(self,theSurface : BRepGProp_Face,thePoint : OCP.gp.gp_Pnt,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    @overload
    def __init__(self,theSurface : BRepGProp_Face,theDomain : BRepGProp_Domain,thePoint : OCP.gp.gp_Pnt,theLocation : OCP.gp.gp_Pnt,theTolerance : float=0.001,theCGFlag : bool=False,theIFlag : bool=False) -> None: ...
    pass
