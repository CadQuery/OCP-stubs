import OCP.IntPatch
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import IntPatch_WLine
import OCP.Intf
import OCP.Adaptor3d
import IntPatch_ImpImpIntersection
import OCP.IntAna
import OCP.Geom2d
import OCP.Standard
import OCP.TColStd
import OCP.IntSurf
import OCP.math
import OCP.NCollection
import OCP.gp
import OCP.Bnd
import OCP.GeomAbs
import OCP.Adaptor2d
__all__  = [
"IntPatch_Line",
"IntPatch_ALineToWLine",
"IntPatch_ArcFunction",
"IntPatch_CSFunction",
"IntPatch_CurvIntSurf",
"IntPatch_GLine",
"IntPatch_HCurve2dTool",
"IntPatch_HInterTool",
"IntPatch_IType",
"IntPatch_ImpImpIntersection",
"IntPatch_ImpPrmIntersection",
"IntPatch_InterferencePolyhedron",
"IntPatch_Intersection",
"IntPatch_ALine",
"IntPatch_LineConstructor",
"IntPatch_Point",
"IntPatch_PointLine",
"IntPatch_Polygo",
"IntPatch_PolyLine",
"IntPatch_PolyArc",
"IntPatch_Polyhedron",
"IntPatch_PolyhedronTool",
"IntPatch_PrmPrmIntersection",
"IntPatch_PrmPrmIntersection_T3Bits",
"IntPatch_RLine",
"IntPatch_RstInt",
"IntPatch_SequenceOfIWLineOfTheIWalking",
"IntPatch_SequenceOfLine",
"IntPatch_SequenceOfPathPointOfTheSOnBounds",
"IntPatch_SequenceOfPoint",
"IntPatch_SequenceOfSegmentOfTheSOnBounds",
"IntPatch_SpecPntType",
"IntPatch_SpecialPoints",
"IntPatch_TheIWLineOfTheIWalking",
"IntPatch_TheIWalking",
"IntPatch_ThePathPointOfTheSOnBounds",
"IntPatch_TheSOnBounds",
"IntPatch_TheSearchInside",
"IntPatch_TheSegmentOfTheSOnBounds",
"IntPatch_TheSurfFunction",
"IntPatch_WLine",
"IntPatch_WLineTool",
"IntPatch_Analytic",
"IntPatch_Circle",
"IntPatch_Ellipse",
"IntPatch_Hyperbola",
"IntPatch_Lin",
"IntPatch_Parabola",
"IntPatch_Restriction",
"IntPatch_SPntNone",
"IntPatch_SPntPole",
"IntPatch_SPntPoleSeamU",
"IntPatch_SPntSeamU",
"IntPatch_SPntSeamUV",
"IntPatch_SPntSeamV",
"IntPatch_Walking"
]
class IntPatch_Line(OCP.Standard.Standard_Transient):
    """
    Definition of an intersection line between two surfaces. A line may be either geometric : line, circle, ellipse, parabola, hyperbola, as defined in the class GLine, or analytic, as defined in the class ALine, or defined by a set of points (coming from a walking algorithm) as defined in the class WLine.Definition of an intersection line between two surfaces. A line may be either geometric : line, circle, ellipse, parabola, hyperbola, as defined in the class GLine, or analytic, as defined in the class ALine, or defined by a set of points (coming from a walking algorithm) as defined in the class WLine.Definition of an intersection line between two surfaces. A line may be either geometric : line, circle, ellipse, parabola, hyperbola, as defined in the class GLine, or analytic, as defined in the class ALine, or defined by a set of points (coming from a walking algorithm) as defined in the class WLine.
    """
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
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
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
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
class IntPatch_ALineToWLine():
    """
    None
    """
    @overload
    def MakeWLine(self,aline : IntPatch_ALine,theLines : IntPatch_SequenceOfLine) -> None: 
        """
        Converts aline to the set of Walking-lines and adds them in theLines.

        Converts aline (limited by paraminf and paramsup) to the set of Walking-lines and adds them in theLines.
        """
    @overload
    def MakeWLine(self,aline : IntPatch_ALine,paraminf : float,paramsup : float,theLines : IntPatch_SequenceOfLine) -> None: ...
    def SetTol3D(self,aT : float) -> None: 
        """
        None
        """
    def SetTolOpenDomain(self,aT : float) -> None: 
        """
        None
        """
    def SetTolTransition(self,aT : float) -> None: 
        """
        None
        """
    def Tol3D(self) -> float: 
        """
        None
        """
    def TolOpenDomain(self) -> float: 
        """
        None
        """
    def TolTransition(self) -> float: 
        """
        None
        """
    def __init__(self,theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theNbPoints : int=200) -> None: ...
    pass
class IntPatch_ArcFunction(OCP.math.math_FunctionWithDerivative, OCP.math.math_Function):
    """
    None
    """
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None

        None
        """
    def Derivative(self,X : float,D : float) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        None
        """
    def LastComputedPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the point, which has been computed while the last calling Value() method

        Returns the point, which has been computed while the last calling Value() method
        """
    def NbSamples(self) -> int: 
        """
        None
        """
    def Quadric(self) -> OCP.IntSurf.IntSurf_Quadric: 
        """
        None

        None
        """
    @overload
    def Set(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def Set(self,S : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    def SetQuadric(self,Q : OCP.IntSurf.IntSurf_Quadric) -> None: 
        """
        None

        None
        """
    def Surface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None

        None
        """
    def Valpoint(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        None

        None
        """
    def Value(self,X : float,F : float) -> bool: 
        """
        None
        """
    def Values(self,X : float,F : float,D : float) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_CSFunction(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    this function is associated to the intersection between a curve on surface and a surface .
    """
    def AuxillarCurve(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def AuxillarSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,C : OCP.Adaptor2d.Adaptor2d_Curve2d,S2 : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class IntPatch_CurvIntSurf():
    """
    None
    """
    def Function(self) -> IntPatch_CSFunction: 
        """
        return the math function which is used to compute the intersection
        """
    def IsDone(self) -> bool: 
        """
        Returns TRUE if the creation completed without failure.
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def ParameterOnCurve(self) -> float: 
        """
        None
        """
    def ParameterOnSurface(self) -> Tuple[float, float]: 
        """
        None
        """
    def Perform(self,U : float,V : float,W : float,Rsnld : OCP.math.math_FunctionSetRoot,u0 : float,v0 : float,u1 : float,v1 : float,w0 : float,w1 : float) -> None: 
        """
        compute the solution it's possible to write to optimize: IntImp_IntCS inter(S1,C1,Toltangency) math_FunctionSetRoot rsnld(Inter.function()) while ...{ u=... v=... w=... inter.Perform(u,v,w,rsnld) } or IntImp_IntCS inter(Toltangency) inter.SetSurface(S); math_FunctionSetRoot rsnld(Inter.function()) while ...{ C=... inter.SetCurve(C); u=... v=... w=... inter.Perform(u,v,w,rsnld) }
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        returns the intersection point The exception NotDone is raised if IsDone is false. The exception DomainError is raised if IsEmpty is true.
        """
    @overload
    def __init__(self,F : IntPatch_CSFunction,TolTangency : float) -> None: ...
    @overload
    def __init__(self,U : float,V : float,W : float,F : IntPatch_CSFunction,TolTangency : float,MarginCoef : float=0.0) -> None: ...
    pass
class IntPatch_GLine(IntPatch_Line, OCP.Standard.Standard_Transient):
    """
    Implementation of an intersection line represented by a conic.Implementation of an intersection line represented by a conic.Implementation of an intersection line represented by a conic.
    """
    def AddVertex(self,Pnt : IntPatch_Point) -> None: 
        """
        To add a vertex in the list.
        """
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """
    def Circle(self) -> OCP.gp.gp_Circ: 
        """
        Returns the Circ from gp corresponding to the intersection when ArcType returns IntPatch_Circle.

        Returns the Circ from gp corresponding to the intersection when ArcType returns IntPatch_Circle.
        """
    def ComputeVertexParameters(self,Tol : float) -> None: 
        """
        Set the parameters of all the vertex on the line. if a vertex is already in the line, its parameter is modified else a new point in the line is inserted.
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
    def Ellipse(self) -> OCP.gp.gp_Elips: 
        """
        Returns the Elips from gp corresponding to the intersection when ArcType returns IntPatch_Ellipse.

        Returns the Elips from gp corresponding to the intersection when ArcType returns IntPatch_Ellipse.
        """
    def FirstPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.

        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the line has a known First point. This point is given by the method FirstPoint().

        Returns True if the line has a known First point. This point is given by the method FirstPoint().
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the line has a known Last point. This point is given by the method LastPoint().

        Returns True if the line has a known Last point. This point is given by the method LastPoint().
        """
    def Hyperbola(self) -> OCP.gp.gp_Hypr: 
        """
        Returns the Hypr from gp corresponding to the intersection when ArcType returns IntPatch_Hyperbola.

        Returns the Hypr from gp corresponding to the intersection when ArcType returns IntPatch_Hyperbola.
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
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    def LastPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.

        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.
        """
    def Line(self) -> OCP.gp.gp_Lin: 
        """
        Returns the Lin from gp corresponding to the intersection when ArcType returns IntPatch_Line.

        Returns the Lin from gp corresponding to the intersection when ArcType returns IntPatch_Line.
        """
    def NbVertex(self) -> int: 
        """
        None

        None
        """
    def Parabola(self) -> OCP.gp.gp_Parab: 
        """
        Returns the Parab from gp corresponding to the intersection when ArcType returns IntPatch_Parabola.

        Returns the Parab from gp corresponding to the intersection when ArcType returns IntPatch_Parabola.
        """
    def Replace(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        To replace the element of range Index in the list of points.
        """
    def SetFirstPoint(self,IndFirst : int) -> None: 
        """
        None

        None
        """
    def SetLastPoint(self,IndLast : int) -> None: 
        """
        None

        None
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
        """
    def Vertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    @overload
    def __init__(self,E : OCP.gp.gp_Elips,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips,Tang : bool) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
    @overload
    def __init__(self,E : OCP.gp.gp_Elips,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,L : OCP.gp.gp_Lin,Tang : bool) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
    @overload
    def __init__(self,C : OCP.gp.gp_Circ,Tang : bool) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab,Tang : bool) -> None: ...
    @overload
    def __init__(self,H : OCP.gp.gp_Hypr,Tang : bool) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Parab,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
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
class IntPatch_HCurve2dTool():
    """
    None
    """
    @staticmethod
    def BSpline_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        None
        """
    @staticmethod
    def Bezier_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.Geom2d.Geom2d_BezierCurve: 
        """
        None
        """
    @staticmethod
    def Circle_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Circ2d: 
        """
        None
        """
    @staticmethod
    def Continuity_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    @staticmethod
    def D0_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d) -> None: 
        """
        Computes the point of parameter U on the curve.
        """
    @staticmethod
    def D1_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V : OCP.gp.gp_Vec2d) -> None: 
        """
        Computes the point of parameter U on the curve with its first derivative. Raised if the continuity of the current interval is not C1.
        """
    @staticmethod
    def D2_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first and second derivatives V1 and V2. Raised if the continuity of the current interval is not C2.
        """
    @staticmethod
    def D3_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,P : OCP.gp.gp_Pnt2d,V1 : OCP.gp.gp_Vec2d,V2 : OCP.gp.gp_Vec2d,V3 : OCP.gp.gp_Vec2d) -> None: 
        """
        Returns the point P of parameter U, the first, the second and the third derivative. Raised if the continuity of the current interval is not C3.
        """
    @staticmethod
    def DN_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float,N : int) -> OCP.gp.gp_Vec2d: 
        """
        The returned vector gives the value of the derivative for the order of derivation N. Raised if the continuity of the current interval is not CN. Raised if N < 1.
        """
    @staticmethod
    def Ellipse_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Elips2d: 
        """
        None
        """
    @staticmethod
    def FirstParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def GetType_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.GeomAbs.GeomAbs_CurveType: 
        """
        Returns the type of the curve in the current interval : Line, Circle, Ellipse, Hyperbola, Parabola, BezierCurve, BSplineCurve, OtherCurve.
        """
    @staticmethod
    def Hyperbola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Hypr2d: 
        """
        None
        """
    @staticmethod
    def Intervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,T : OCP.TColStd.TColStd_Array1OfReal,S : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Stores in <T> the parameters bounding the intervals of continuity <S>.
        """
    @staticmethod
    def IsClosed_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def IsPeriodic_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        None
        """
    @staticmethod
    def LastParameter_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Line_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Lin2d: 
        """
        None
        """
    @staticmethod
    def NbIntervals_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,S : OCP.GeomAbs.GeomAbs_Shape) -> int: 
        """
        Returns the number of intervals for continuity <S>. May be one if Continuity(myclass) >= <S>
        """
    @staticmethod
    def NbSamples_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U0 : float,U1 : float) -> int: 
        """
        None
        """
    @staticmethod
    def Parabola_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> OCP.gp.gp_Parab2d: 
        """
        None
        """
    @staticmethod
    def Period_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        None
        """
    @staticmethod
    def Resolution_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,R3d : float) -> float: 
        """
        Returns the parametric resolution corresponding to the real space resolution <R3d>.
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,U : float) -> OCP.gp.gp_Pnt2d: 
        """
        Computes the point of parameter U on the curve.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_HInterTool():
    """
    Tool for the intersection between 2 surfaces. Regroupe pour l instant les methodes hors Adaptor3d...
    """
    @staticmethod
    def Bounds_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> Tuple[float, float]: 
        """
        Returns the parametric limits on the arc C. These limits must be finite : they are either the real limits of the arc, for a finite arc, or a bounding box for an infinite arc.
        """
    @staticmethod
    def HasBeenSeen_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        Returns True if all the intersection point and edges are known on the Arc. The intersection point are given as vertices. The intersection edges are given as intervals between two vertices.
        """
    @staticmethod
    def HasFirstPoint_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int,IndFirst : int) -> bool: 
        """
        Returns True when the segment of range Index is not open at the left side. In that case, IndFirst is the range in the list intersection points (see NbPoints) of the one which defines the left bound of the segment. Otherwise, the method has to return False, and IndFirst has no meaning.
        """
    @staticmethod
    def HasLastPoint_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int,IndLast : int) -> bool: 
        """
        Returns True when the segment of range Index is not open at the right side. In that case, IndLast is the range in the list intersection points (see NbPoints) of the one which defines the right bound of the segment. Otherwise, the method has to return False, and IndLast has no meaning.
        """
    @staticmethod
    def IsAllSolution_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> bool: 
        """
        Returns True when the whole restriction is solution of the intersection problem.
        """
    @staticmethod
    def IsVertex_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int) -> bool: 
        """
        Returns True if the intersection point of range Index corresponds with a vertex on the arc A.
        """
    @staticmethod
    def NbPoints_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        Returns the number of intersection points on the arc A.
        """
    def NbSamplePoints(self,S : OCP.Adaptor3d.Adaptor3d_Surface) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamplesOnArc_s(A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        returns the number of points which is used to make a sample on the arc. this number is a function of the Surface and the CurveOnSurface complexity.
        """
    @staticmethod
    def NbSamplesU_s(S : OCP.Adaptor3d.Adaptor3d_Surface,u1 : float,u2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def NbSamplesV_s(S : OCP.Adaptor3d.Adaptor3d_Surface,v1 : float,v2 : float) -> int: 
        """
        None
        """
    @staticmethod
    def NbSegments_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> int: 
        """
        returns the number of part of A solution of the of intersection problem.
        """
    @staticmethod
    def Parameter_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        Returns the parameter of the vertex V on the arc A.
        """
    @staticmethod
    def Project_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,P : OCP.gp.gp_Pnt2d,Paramproj : float,Ptproj : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Projects the point P on the arc C. If the methods returns Standard_True, the projection is successful, and Paramproj is the parameter on the arc of the projected point, Ptproj is the projected Point. If the method returns Standard_False, Param proj and Ptproj are not significant.
        """
    def SamplePoint(self,S : OCP.Adaptor3d.Adaptor3d_Surface,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    @staticmethod
    def SingularOnUMax_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnUMin_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnVMax_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def SingularOnVMin_s(S : OCP.Adaptor3d.Adaptor3d_Surface) -> bool: 
        """
        None
        """
    @staticmethod
    def Tolerance_s(V : OCP.Adaptor3d.Adaptor3d_HVertex,C : OCP.Adaptor2d.Adaptor2d_Curve2d) -> float: 
        """
        Returns the parametric tolerance used to consider that the vertex and another point meet, i-e if Abs(parameter(Vertex) - parameter(OtherPnt))<= Tolerance, the points are "merged".
        """
    @staticmethod
    def Value_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int,Pt : OCP.gp.gp_Pnt) -> Tuple[float, float]: 
        """
        Returns the value (Pt), the tolerance (Tol), and the parameter (U) on the arc A , of the intersection point of range Index.
        """
    @staticmethod
    def Vertex_s(C : OCP.Adaptor2d.Adaptor2d_Curve2d,Index : int,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: 
        """
        When IsVertex returns True, this method returns the vertex on the arc A.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_IType():
    """
    None

    Members:

      IntPatch_Lin

      IntPatch_Circle

      IntPatch_Ellipse

      IntPatch_Parabola

      IntPatch_Hyperbola

      IntPatch_Analytic

      IntPatch_Walking

      IntPatch_Restriction
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
    IntPatch_Analytic: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Analytic: 5>
    IntPatch_Circle: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Circle: 1>
    IntPatch_Ellipse: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Ellipse: 2>
    IntPatch_Hyperbola: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Hyperbola: 4>
    IntPatch_Lin: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Lin: 0>
    IntPatch_Parabola: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Parabola: 3>
    IntPatch_Restriction: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Restriction: 7>
    IntPatch_Walking: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Walking: 6>
    __entries: dict # value = {'IntPatch_Lin': (<IntPatch_IType.IntPatch_Lin: 0>, None), 'IntPatch_Circle': (<IntPatch_IType.IntPatch_Circle: 1>, None), 'IntPatch_Ellipse': (<IntPatch_IType.IntPatch_Ellipse: 2>, None), 'IntPatch_Parabola': (<IntPatch_IType.IntPatch_Parabola: 3>, None), 'IntPatch_Hyperbola': (<IntPatch_IType.IntPatch_Hyperbola: 4>, None), 'IntPatch_Analytic': (<IntPatch_IType.IntPatch_Analytic: 5>, None), 'IntPatch_Walking': (<IntPatch_IType.IntPatch_Walking: 6>, None), 'IntPatch_Restriction': (<IntPatch_IType.IntPatch_Restriction: 7>, None)}
    __members__: dict # value = {'IntPatch_Lin': <IntPatch_IType.IntPatch_Lin: 0>, 'IntPatch_Circle': <IntPatch_IType.IntPatch_Circle: 1>, 'IntPatch_Ellipse': <IntPatch_IType.IntPatch_Ellipse: 2>, 'IntPatch_Parabola': <IntPatch_IType.IntPatch_Parabola: 3>, 'IntPatch_Hyperbola': <IntPatch_IType.IntPatch_Hyperbola: 4>, 'IntPatch_Analytic': <IntPatch_IType.IntPatch_Analytic: 5>, 'IntPatch_Walking': <IntPatch_IType.IntPatch_Walking: 6>, 'IntPatch_Restriction': <IntPatch_IType.IntPatch_Restriction: 7>}
    pass
class IntPatch_ImpImpIntersection():
    """
    Implementation of the intersection between two quadric patches : Plane, Cone, Cylinder or Sphere.
    """
    class IntStatus_e():
        """
        None

        Members:

          IntStatus_OK

          IntStatus_InfiniteSectionCurve

          IntStatus_Fail
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
        IntStatus_Fail: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_Fail: 2>
        IntStatus_InfiniteSectionCurve: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_InfiniteSectionCurve: 1>
        IntStatus_OK: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_OK: 0>
        __entries: dict # value = {'IntStatus_OK': (<IntStatus_e.IntStatus_OK: 0>, None), 'IntStatus_InfiniteSectionCurve': (<IntStatus_e.IntStatus_InfiniteSectionCurve: 1>, None), 'IntStatus_Fail': (<IntStatus_e.IntStatus_Fail: 2>, None)}
        __members__: dict # value = {'IntStatus_OK': <IntStatus_e.IntStatus_OK: 0>, 'IntStatus_InfiniteSectionCurve': <IntStatus_e.IntStatus_InfiniteSectionCurve: 1>, 'IntStatus_Fail': <IntStatus_e.IntStatus_Fail: 2>}
        pass
    def GetStatus(self) -> IntPatch_ImpImpIntersection.IntStatus_e: 
        """
        Returns status

        Returns status
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the calculus was successful.

        Returns True if the calculus was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if the is no intersection.

        Returns true if the is no intersection.
        """
    def Line(self,Index : int) -> IntPatch_Line: 
        """
        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.

        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.
        """
    def NbLines(self) -> int: 
        """
        Returns the number of intersection lines.

        Returns the number of intersection lines.
        """
    def NbPnts(self) -> int: 
        """
        Returns the number of "single" points.

        Returns the number of "single" points.
        """
    def OppositeFaces(self) -> bool: 
        """
        Returns True when the TangentFaces returns True and the normal vectors evaluated at a point on the first and the second surface are opposite. The exception DomainError is raised if TangentFaces returns False.

        Returns True when the TangentFaces returns True and the normal vectors evaluated at a point on the first and the second surface are opposite. The exception DomainError is raised if TangentFaces returns False.
        """
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,theIsReqToKeepRLine : bool=False) -> None: 
        """
        Flag theIsReqToKeepRLine has been entered only for compatibility with TopOpeBRep package. It shall be deleted after deleting TopOpeBRep. When intersection result returns IntPatch_RLine and another IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE) will always keep both lines even if they are coincided.
        """
    def Point(self,Index : int) -> IntPatch_Point: 
        """
        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.

        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.
        """
    def TangentFaces(self) -> bool: 
        """
        Returns True if the two patches are considered as entirely tangent, i.e every restriction arc of one patch is inside the geometric base of the other patch.

        Returns True if the two patches are considered as entirely tangent, i.e every restriction arc of one patch is inside the geometric base of the other patch.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,theIsReqToKeepRLine : bool=False) -> None: ...
    IntStatus_Fail: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_Fail: 2>
    IntStatus_InfiniteSectionCurve: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_InfiniteSectionCurve: 1>
    IntStatus_OK: OCP.IntPatch.IntStatus_e # value = <IntStatus_e.IntStatus_OK: 0>
    pass
class IntPatch_ImpPrmIntersection():
    """
    Implementation of the intersection between a natural quadric patch : Plane, Cone, Cylinder or Sphere and a bi-parametrised surface.
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the calculus was successful.

        Returns true if the calculus was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if the is no intersection.

        Returns true if the is no intersection.
        """
    def Line(self,Index : int) -> IntPatch_Line: 
        """
        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.

        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.
        """
    def NbLines(self) -> int: 
        """
        Returns the number of intersection lines.

        Returns the number of intersection lines.
        """
    def NbPnts(self) -> int: 
        """
        Returns the number of "single" points.

        Returns the number of "single" points.
        """
    def Perform(self,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,Fleche : float,Pas : float) -> None: 
        """
        None
        """
    def Point(self,Index : int) -> IntPatch_Point: 
        """
        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.

        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.
        """
    def SetStartPoint(self,U : float,V : float) -> None: 
        """
        to search for solution from the given point
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Surf1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Surf2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,Fleche : float,Pas : float) -> None: ...
    pass
class IntPatch_InterferencePolyhedron(OCP.Intf.Intf_Interference):
    """
    Computes the interference between two polyhedra or the self interference of a polyhedron. Points of intersection, polylines of intersection and zones of tangence.
    """
    def Contains(self,ThePnt : OCP.Intf.Intf_SectionPoint) -> bool: 
        """
        Tests if the polylines of intersection or the zones of tangence contain the point of intersection <ThePnt>.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def GetTolerance(self) -> float: 
        """
        Gives the tolerance used for the calculation.

        Gives the tolerance used for the calculation.
        """
    @overload
    def Insert(self,TheZone : OCP.Intf.Intf_TangentZone) -> bool: 
        """
        Inserts a new zone of tangence in the current list of tangent zones of the interference and returns True when done.

        Insert a new segment of intersection in the current list of polylines of intersection of the interference.
        """
    @overload
    def Insert(self,pdeb : OCP.Intf.Intf_SectionPoint,pfin : OCP.Intf.Intf_SectionPoint) -> None: ...
    def LineValue(self,Index : int) -> OCP.Intf.Intf_SectionLine: 
        """
        Gives the polyline of intersection at address <Index> in the interference.

        Gives the polyline of intersection at address <Index> in the interference.
        """
    def NbSectionLines(self) -> int: 
        """
        Gives the number of polylines of intersection in the interference.

        Gives the number of polylines of intersection in the interference.
        """
    def NbSectionPoints(self) -> int: 
        """
        Gives the number of points of intersection in the interference.

        Gives the number of points of intersection in the interference.
        """
    def NbTangentZones(self) -> int: 
        """
        Gives the number of zones of tangence in the interference.

        Gives the number of zones of tangence in the interference.
        """
    @overload
    def Perform(self,Obje1 : IntPatch_Polyhedron,Obje2 : IntPatch_Polyhedron) -> None: 
        """
        Computes the interference between the two Polyhedra.

        Computes the self interference of a Polyhedron.
        """
    @overload
    def Perform(self,Obje : IntPatch_Polyhedron) -> None: ...
    def PntValue(self,Index : int) -> OCP.Intf.Intf_SectionPoint: 
        """
        Gives the point of intersection of address Index in the interference.

        Gives the point of intersection of address Index in the interference.
        """
    def ZoneValue(self,Index : int) -> OCP.Intf.Intf_TangentZone: 
        """
        Gives the zone of tangence at address Index in the interference.

        Gives the zone of tangence at address Index in the interference.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Obje : IntPatch_Polyhedron) -> None: ...
    @overload
    def __init__(self,Obje1 : IntPatch_Polyhedron,Obje2 : IntPatch_Polyhedron) -> None: ...
    pass
class IntPatch_Intersection():
    """
    This class provides a generic algorithm to intersect 2 surfaces.
    """
    @staticmethod
    def CheckSingularPoints_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theD1 : OCP.Adaptor3d.Adaptor3d_TopolTool,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theDist : float) -> bool: 
        """
        Checks if surface theS1 has degenerated boundary (dS/du or dS/dv = 0) and calculates minimal distance between corresponding singular points and surface theS2 If singular point exists the method returns "true" and stores minimal distance in theDist.
        """
    @staticmethod
    def DefineUVMaxStep_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theD1 : OCP.Adaptor3d.Adaptor3d_TopolTool,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theD2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> float: 
        """
        Calculates recommended value for myUVMaxStep depending on surfaces and their domains
        """
    def Dump(self,Mode : int,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> None: 
        """
        Dump of each result line. Mode for more accurate dumps.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the calculus was successful.

        Returns True if the calculus was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if the is no intersection.

        Returns true if the is no intersection.
        """
    def Line(self,Index : int) -> IntPatch_Line: 
        """
        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.

        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.
        """
    def NbLines(self) -> int: 
        """
        Returns the number of intersection lines.

        Returns the number of intersection lines.
        """
    def NbPnts(self) -> int: 
        """
        Returns the number of "single" points.

        Returns the number of "single" points.
        """
    def OppositeFaces(self) -> bool: 
        """
        Returns True when the TangentFaces returns True and the normal vectors evaluated at a point on the first and the second surface are opposite. The exception DomainError is raised if TangentFaces returns False.

        Returns True when the TangentFaces returns True and the normal vectors evaluated at a point on the first and the second surface are opposite. The exception DomainError is raised if TangentFaces returns False.
        """
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,U1 : float,V1 : float,U2 : float,V2 : float,TolArc : float,TolTang : float) -> None: 
        """
        Flag theIsReqToKeepRLine has been entered only for compatibility with TopOpeBRep package. It shall be deleted after deleting TopOpeBRep. When intersection result returns IntPatch_RLine and another IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE) will always keep both lines even if they are coincided. Flag theIsReqToPostWLProc has been entered only for compatibility with TopOpeBRep package. It shall be deleted after deleting TopOpeBRep. If theIsReqToPostWLProc == FALSE, then we will work with Walking-line obtained after intersection algorithm directly (without any post-processing).

        If isGeomInt == Standard_False, then method Param-Param intersection will be used. Flag theIsReqToKeepRLine has been entered only for compatibility with TopOpeBRep package. It shall be deleted after deleting TopOpeBRep. When intersection result returns IntPatch_RLine and another IntPatch_Line (not restriction) we (in case of theIsReqToKeepRLine==TRUE) will always keep both lines even if they are coincided. Flag theIsReqToPostWLProc has been entered only for compatibility with TopOpeBRep package. It shall be deleted after deleting TopOpeBRep. If theIsReqToPostWLProc == FALSE, then we will work with Walking-line obtained after intersection algorithm directly (without any post-processing).

        Perform with start point

        Uses for finding self-intersected surfaces.
        """
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float) -> None: ...
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,isGeomInt : bool=True,theIsReqToKeepRLine : bool=False,theIsReqToPostWLProc : bool=True) -> None: ...
    @overload
    def Perform(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float,LOfPnts : OCP.IntSurf.IntSurf_ListOfPntOn2S,isGeomInt : bool=True,theIsReqToKeepRLine : bool=False,theIsReqToPostWLProc : bool=True) -> None: ...
    def Point(self,Index : int) -> IntPatch_Point: 
        """
        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.

        Returns the point of range Index. An exception is raised if Index<=0 or Index>NbPnt.
        """
    @staticmethod
    def PrepareSurfaces_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theD1 : OCP.Adaptor3d.Adaptor3d_TopolTool,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theD2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Tol : float,theSeqHS1 : Any,theSeqHS2 : Any) -> None: 
        """
        Prepares surfaces for intersection
        """
    def SequenceOfLine(self) -> IntPatch_SequenceOfLine: 
        """
        None
        """
    def SetTolerances(self,TolArc : float,TolTang : float,UVMaxStep : float,Fleche : float) -> None: 
        """
        Set the tolerances used by the algorithms: --- Implicit - Parametric --- Parametric - Parametric --- Implicit - Implicit
        """
    def TangentFaces(self) -> bool: 
        """
        Returns True if the two patches are considered as entirely tangent, i-e every restriction arc of one patch is inside the geometric base of the other patch.

        Returns True if the two patches are considered as entirely tangent, i-e every restriction arc of one patch is inside the geometric base of the other patch.
        """
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolArc : float,TolTang : float) -> None: ...
    pass
class IntPatch_ALine(IntPatch_Line, OCP.Standard.Standard_Transient):
    """
    Implementation of an intersection line described by a parametrized curve.Implementation of an intersection line described by a parametrized curve.Implementation of an intersection line described by a parametrized curve.
    """
    def AddVertex(self,Pnt : IntPatch_Point) -> None: 
        """
        To add a vertex in the list.
        """
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """
    def ChangeVertex(self,theIndex : int) -> IntPatch_Point: 
        """
        Allows modifying the vertex with index theIndex on the line.
        """
    def ComputeVertexParameters(self,Tol : float) -> None: 
        """
        Set the parameters of all the vertex on the line. if a vertex is already in the line, its parameter is modified else a new point in the line is inserted.
        """
    def Curve(self) -> OCP.IntAna.IntAna_Curve: 
        """
        None
        """
    def D1(self,U : float,P : OCP.gp.gp_Pnt,Du : OCP.gp.gp_Vec) -> bool: 
        """
        Returns Standard_True when the derivative at parameter U is defined on the analytic intersection line. In that case, Du is the derivative. Returns Standard_False when it is not possible to evaluate the derivative. In both cases, P is the point at parameter U on the intersection.

        Returns Standard_True when the derivative at parameter U is defined on the analytic intersection line. In that case, Du is the derivative. Returns Standard_False when it is not possible to evaluate the derivative. In both cases, P is the point at parameter U on the intersection.
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
    @overload
    def FindParameter(self,P : OCP.gp.gp_Pnt,theParams : OCP.TColStd.TColStd_ListOfReal) -> None: 
        """
        Tries to find the parameters of the point P on the curve. If the method returns False, the "projection" is impossible. If the method returns True at least one parameter has been found. theParams is always sorted in ascending order.

        Tries to find the parameters of the point P on the curve. If the method returns False, the "projection" is impossible. If the method returns True at least one parameter has been found. theParams is always sorted in ascending order.
        """
    @overload
    def FindParameter(self,theP : OCP.gp.gp_Pnt,theParams : OCP.TColStd.TColStd_ListOfReal) -> None: ...
    def FirstParameter(self,IsIncluded : bool) -> float: 
        """
        Returns the first parameter on the intersection line. If IsIncluded returns True, Value and D1 methods can be call with a parameter equal to FirstParameter. Otherwise, the parameter must be greater than FirstParameter.

        Returns the first parameter on the intersection line. If IsIncluded returns True, Value and D1 methods can be call with a parameter equal to FirstParameter. Otherwise, the parameter must be greater than FirstParameter.
        """
    def FirstPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.

        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the line has a known First point. This point is given by the method FirstPoint().

        Returns True if the line has a known First point. This point is given by the method FirstPoint().
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the line has a known Last point. This point is given by the method LastPoint().

        Returns True if the line has a known Last point. This point is given by the method LastPoint().
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
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    def LastParameter(self,IsIncluded : bool) -> float: 
        """
        Returns the last parameter on the intersection line. If IsIncluded returns True, Value and D1 methods can be call with a parameter equal to LastParameter. Otherwise, the parameter must be less than LastParameter.

        Returns the last parameter on the intersection line. If IsIncluded returns True, Value and D1 methods can be call with a parameter equal to LastParameter. Otherwise, the parameter must be less than LastParameter.
        """
    def LastPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.

        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.
        """
    def NbVertex(self) -> int: 
        """
        None

        None
        """
    def Replace(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        Replaces the element of range Index in the list of points.

        Replaces the element of range Index in the list of points.
        """
    def SetFirstPoint(self,IndFirst : int) -> None: 
        """
        None

        None
        """
    def SetLastPoint(self,IndLast : int) -> None: 
        """
        None

        None
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
        """
    def Value(self,U : float) -> OCP.gp.gp_Pnt: 
        """
        Returns the point of parameter U on the analytic intersection line.

        Returns the point of parameter U on the analytic intersection line.
        """
    def Vertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    @overload
    def __init__(self,C : OCP.IntAna.IntAna_Curve,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,C : OCP.IntAna.IntAna_Curve,Tang : bool) -> None: ...
    @overload
    def __init__(self,C : OCP.IntAna.IntAna_Curve,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
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
class IntPatch_LineConstructor():
    """
    The intersections algorithms compute the intersection on two surfaces and return the intersections lines as IntPatch_Line.
    """
    def Line(self,index : int) -> IntPatch_Line: 
        """
        None
        """
    def NbLines(self) -> int: 
        """
        None
        """
    def Perform(self,SL : IntPatch_SequenceOfLine,L : IntPatch_Line,S1 : OCP.Adaptor3d.Adaptor3d_Surface,D1 : OCP.Adaptor3d.Adaptor3d_TopolTool,S2 : OCP.Adaptor3d.Adaptor3d_Surface,D2 : OCP.Adaptor3d.Adaptor3d_TopolTool,Tol : float) -> None: 
        """
        None
        """
    def __init__(self,mode : int) -> None: ...
    pass
class IntPatch_Point():
    """
    Definition of an intersection point between two surfaces. Such a point is contains geometrical information (see the Value method) and logical information.
    """
    def ArcOnS1(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the arc of restriction containing the vertex. The exception DomainError is raised if IsOnDomS1 returns False.

        Returns the arc of restriction containing the vertex. The exception DomainError is raised if IsOnDomS1 returns False.
        """
    def ArcOnS2(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the arc of restriction containing the vertex. The exception DomainError is raised if IsOnDomS2 returns False.

        Returns the arc of restriction containing the vertex. The exception DomainError is raised if IsOnDomS2 returns False.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def IsMultiple(self) -> bool: 
        """
        Returns True if the point belongs to several intersection lines.

        Returns True if the point belongs to several intersection lines.
        """
    def IsOnDomS1(self) -> bool: 
        """
        Returns TRUE if the point is on a boundary of the domain of the first patch.

        Returns TRUE if the point is on a boundary of the domain of the first patch.
        """
    def IsOnDomS2(self) -> bool: 
        """
        Returns TRUE if the point is on a boundary of the domain of the second patch.

        Returns TRUE if the point is on a boundary of the domain of the second patch.
        """
    def IsTangencyPoint(self) -> bool: 
        """
        Returns True if the Point is a tangency point between the surfaces. If the Point is on one of the domain (IsOnDomS1 returns True or IsOnDomS2 returns True), an exception is raised.

        Returns True if the Point is a tangency point between the surfaces. If the Point is on one of the domain (IsOnDomS1 returns True or IsOnDomS2 returns True), an exception is raised.
        """
    def IsVertexOnS1(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.

        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.
        """
    def IsVertexOnS2(self) -> bool: 
        """
        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.

        Returns TRUE if the point is a vertex on the initial restriction facet of the first surface.
        """
    def ParameterOnArc1(self) -> float: 
        """
        Returns the parameter of the point on the arc returned by the method ArcOnS2. The exception DomainError is raised if IsOnDomS1 returns False.

        Returns the parameter of the point on the arc returned by the method ArcOnS2. The exception DomainError is raised if IsOnDomS1 returns False.
        """
    def ParameterOnArc2(self) -> float: 
        """
        Returns the parameter of the point on the arc returned by the method ArcOnS2. The exception DomainError is raised if IsOnDomS2 returns False.

        Returns the parameter of the point on the arc returned by the method ArcOnS2. The exception DomainError is raised if IsOnDomS2 returns False.
        """
    def ParameterOnLine(self) -> float: 
        """
        This method returns the parameter of the point on the intersection line. If the points does not belong to an intersection line, the value returned does not have any sens.

        This method returns the parameter of the point on the intersection line. If the points does not belong to an intersection line, the value returned does not have any sens.
        """
    def Parameters(self) -> Tuple[float, float, float, float]: 
        """
        Returns the parameters on the first and on the second surface of the point.

        Returns the parameters on the first and on the second surface of the point.
        """
    def ParametersOnS1(self) -> Tuple[float, float]: 
        """
        Returns the parameters on the first surface of the point.

        Returns the parameters on the first surface of the point.
        """
    def ParametersOnS2(self) -> Tuple[float, float]: 
        """
        Returns the parameters on the second surface of the point.

        Returns the parameters on the second surface of the point.
        """
    def PntOn2S(self) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the PntOn2S (geometric Point and the parameters)

        Returns the PntOn2S (geometric Point and the parameters)
        """
    def ReverseTransition(self) -> None: 
        """
        None
        """
    def SetArc(self,OnFirst : bool,A : OCP.Adaptor2d.Adaptor2d_Curve2d,Param : float,TLine : OCP.IntSurf.IntSurf_Transition,TArc : OCP.IntSurf.IntSurf_Transition) -> None: 
        """
        Sets the values of a point which is on one of the domain, when both surfaces are implicit ones. If OnFirst is True, the point is on the domain of the first patch, otherwise the point is on the domain of the second surface.
        """
    def SetMultiple(self,IsMult : bool) -> None: ...
    def SetParameter(self,Para : float) -> None: 
        """
        Set the value of the parameter on the intersection line.

        Set the value of the parameter on the intersection line.
        """
    def SetParameters(self,U1 : float,V1 : float,U2 : float,V2 : float) -> None: 
        """
        Sets the values of the parameters of the point on each surface.

        Sets the values of the parameters of the point on each surface.
        """
    def SetTolerance(self,Tol : float) -> None: 
        """
        None

        None
        """
    @overload
    def SetValue(self,Pt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the values of a point which is on no domain, when both surfaces are implicit ones. If Tangent is True, the point is a point of tangency between the surfaces.

        None

        Sets the value of <pt> member

        None

        Sets the value of <pt> member
        """
    @overload
    def SetValue(self,thePOn2S : OCP.IntSurf.IntSurf_PntOn2S) -> None: ...
    @overload
    def SetValue(self,Pt : OCP.gp.gp_Pnt,Tol : float,Tangent : bool) -> None: ...
    def SetVertex(self,OnFirst : bool,V : OCP.Adaptor3d.Adaptor3d_HVertex) -> None: 
        """
        Sets the values of a point which is a vertex on the initial facet of restriction of one of the surface. If OnFirst is True, the point is on the domain of the first patch, otherwise the point is on the domain of the second surface.
        """
    def Tolerance(self) -> float: 
        """
        This method returns the fuzziness on the point.

        This method returns the fuzziness on the point.
        """
    def TransitionLineArc1(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the intersection line with the arc on S1. The exception DomainError is raised if IsOnDomS1 returns False.

        Returns the transition of the point on the intersection line with the arc on S1. The exception DomainError is raised if IsOnDomS1 returns False.
        """
    def TransitionLineArc2(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition of the point on the intersection line with the arc on S2. The exception DomainError is raised if IsOnDomS2 returns False.

        Returns the transition of the point on the intersection line with the arc on S2. The exception DomainError is raised if IsOnDomS2 returns False.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition between the intersection line returned by the method Line and the arc on S1 returned by ArcOnS1(). The exception DomainError is raised if IsOnDomS1 returns False.

        Returns the transition between the intersection line returned by the method Line and the arc on S1 returned by ArcOnS1(). The exception DomainError is raised if IsOnDomS1 returns False.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_Transition: 
        """
        Returns the transition between the intersection line returned by the method Line and the arc on S2 returned by ArcOnS2. The exception DomainError is raised if IsOnDomS2 returns False.

        Returns the transition between the intersection line returned by the method Line and the arc on S2 returned by ArcOnS2. The exception DomainError is raised if IsOnDomS2 returns False.
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the intersection point (geometric information).

        Returns the intersection point (geometric information).
        """
    def VertexOnS1(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        Returns the information about the point when it is on the domain of the first patch, i-e when the function IsVertexOnS1 returns True. Otherwise, an exception is raised.

        Returns the information about the point when it is on the domain of the first patch, i-e when the function IsVertexOnS1 returns True. Otherwise, an exception is raised.
        """
    def VertexOnS2(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        Returns the information about the point when it is on the domain of the second patch, i-e when the function IsVertexOnS2 returns True. Otherwise, an exception is raised.

        Returns the information about the point when it is on the domain of the second patch, i-e when the function IsVertexOnS2 returns True. Otherwise, an exception is raised.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_PointLine(IntPatch_Line, OCP.Standard.Standard_Transient):
    """
    Definition of an intersection line between two surfaces. A line defined by a set of points (e.g. coming from a walking algorithm) as defined in the class WLine or RLine (Restriction line).Definition of an intersection line between two surfaces. A line defined by a set of points (e.g. coming from a walking algorithm) as defined in the class WLine or RLine (Restriction line).
    """
    def AddVertex(self,Pnt : IntPatch_Point,theIsPrepend : bool=False) -> None: 
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new vertex will be added before the first element of vertices sequence. Otherwise, to the end of the sequence
        """
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """
    def ChangeVertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.
        """
    def ClearVertexes(self) -> None: 
        """
        Removes vertices from the line
        """
    @staticmethod
    def CurvatureRadiusOfIntersLine_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theUVPoint : OCP.IntSurf.IntSurf_PntOn2S) -> float: 
        """
        Returns the radius of curvature of the intersection line in given point. Returns negative value if computation is not possible.
        """
    def Curve(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        Returns set of intersection points
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
    def IsOutBox(self,P : OCP.gp.gp_Pnt) -> bool: 
        """
        Returns TRUE if P is out of the box built from 3D-points.
        """
    def IsOutSurf1Box(self,P1 : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns TRUE if P1 is out of the box built from the points on 1st surface
        """
    def IsOutSurf2Box(self,P2 : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Returns TRUE if P2 is out of the box built from the points on 2nd surface
        """
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    def NbPnts(self) -> int: 
        """
        Returns the number of intersection points.
        """
    def NbVertex(self) -> int: 
        """
        Returns number of vertices (IntPatch_Point) of the line
        """
    def Point(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the intersection point of range Index.
        """
    def RemoveVertex(self,theIndex : int) -> None: 
        """
        Removes single vertex from the line
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
        """
    def Vertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.
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
class IntPatch_Polygo(OCP.Intf.Intf_Polygon2d):
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box2d: 
        """
        Returns the bounding box of the polygon.

        Returns the bounding box of the polygon.
        """
    def Closed(self) -> bool: 
        """
        Returns True if the polyline is closed.
        """
    def DeflectionOverEstimation(self) -> float: 
        """
        Returns the tolerance of the polygon.

        Returns the tolerance of the polygon.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def Error(self) -> float: 
        """
        None

        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of Segments in the polyline.

        Returns the number of Segments in the polyline.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def Segment(self,theIndex : int,theBegin : OCP.gp.gp_Pnt2d,theEnd : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points of the segment <Index> in the Polygon.

        Returns the points of the segment <Index> in the Polygon.
        """
    pass
class IntPatch_PolyLine(IntPatch_Polygo, OCP.Intf.Intf_Polygon2d):
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box2d: 
        """
        Returns the bounding box of the polygon.

        Returns the bounding box of the polygon.
        """
    def Closed(self) -> bool: 
        """
        Returns True if the polyline is closed.
        """
    def DeflectionOverEstimation(self) -> float: 
        """
        Returns the tolerance of the polygon.

        Returns the tolerance of the polygon.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def Error(self) -> float: 
        """
        None

        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of Segments in the polyline.

        Returns the number of Segments in the polyline.
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def ResetError(self) -> None: 
        """
        None
        """
    def Segment(self,theIndex : int,theBegin : OCP.gp.gp_Pnt2d,theEnd : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points of the segment <Index> in the Polygon.

        Returns the points of the segment <Index> in the Polygon.
        """
    def SetRLine(self,OnFirst : bool,Line : IntPatch_RLine) -> None: 
        """
        None
        """
    def SetWLine(self,OnFirst : bool,Line : IntPatch_WLine) -> None: 
        """
        None
        """
    @overload
    def __init__(self,InitDefle : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntPatch_PolyArc(IntPatch_Polygo, OCP.Intf.Intf_Polygon2d):
    """
    None
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box2d: 
        """
        Returns the bounding box of the polygon.

        Returns the bounding box of the polygon.
        """
    def Closed(self) -> bool: 
        """
        None
        """
    def DeflectionOverEstimation(self) -> float: 
        """
        Returns the tolerance of the polygon.

        Returns the tolerance of the polygon.
        """
    def Dump(self) -> None: 
        """
        None
        """
    def Error(self) -> float: 
        """
        None

        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of Segments in the polyline.

        Returns the number of Segments in the polyline.
        """
    def Parameter(self,Index : int) -> float: 
        """
        None
        """
    def Point(self,Index : int) -> OCP.gp.gp_Pnt2d: 
        """
        None
        """
    def Segment(self,theIndex : int,theBegin : OCP.gp.gp_Pnt2d,theEnd : OCP.gp.gp_Pnt2d) -> None: 
        """
        Returns the points of the segment <Index> in the Polygon.

        Returns the points of the segment <Index> in the Polygon.
        """
    def SetOffset(self,OffsetX : float,OffsetY : float) -> None: 
        """
        None
        """
    def __init__(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d,NbSample : int,Pfirst : float,Plast : float,BoxOtherPolygon : OCP.Bnd.Bnd_Box2d) -> None: ...
    pass
class IntPatch_Polyhedron():
    """
    This class provides a linear approximation of the PSurface. preview a constructor on a zone of a surface
    """
    def Bounding(self) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the MaTriangle.
        """
    def ComponentsBounding(self) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def Contain(self,Triang : int,ThePnt : OCP.gp.gp_Pnt) -> bool: 
        """
        Give the plane equation of the triangle of address Triang.
        """
    def DeflectionOnTriangle(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,Index : int) -> float: 
        """
        None
        """
    @overload
    def DeflectionOverEstimation(self) -> float: 
        """
        None

        None
        """
    @overload
    def DeflectionOverEstimation(self,flec : float) -> None: ...
    def Destroy(self) -> None: 
        """
        None
        """
    def Dump(self) -> None: 
        """
        None
        """
    def FillBounding(self) -> None: 
        """
        Compute the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    def NbPoints(self) -> int: 
        """
        Give the number of point in the double array of triangles ((nbdu+1)*(nbdv+1)).
        """
    def NbTriangles(self) -> int: 
        """
        Give the number of triangles in this double array of triangles (nbdu*nbdv*2).
        """
    def Parameters(self,Index : int) -> Tuple[float, float]: 
        """
        None
        """
    def PlaneEquation(self,Triang : int,NormalVector : OCP.gp.gp_XYZ) -> Tuple[float]: 
        """
        Give the plane equation of the triangle of address Triang.
        """
    @overload
    def Point(self,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Set the value of a field of the double array of points.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.

        Give the point of index i in the MaTriangle.
        """
    @overload
    def Point(self,Index : int,P : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def Point(self,thePnt : OCP.gp.gp_Pnt,lig : int,col : int,U : float,V : float) -> None: ...
    @overload
    def Point(self,Index : int,U : float,V : float) -> OCP.gp.gp_Pnt: ...
    def Size(self) -> Tuple[int, int]: 
        """
        Get the size of the MaTriangle.
        """
    def TriConnex(self,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Give the address Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    def Triangle(self,Index : int) -> Tuple[int, int, int]: 
        """
        Give the 3 points of the triangle of address Index in the double array of triangles.
        """
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface,nbdU : int,nbdV : int) -> None: ...
    @overload
    def __init__(self,Surface : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    pass
class IntPatch_PolyhedronTool():
    """
    Describe the signature of a polyhedral surface with only triangular facets and the necessary information to compute the interferences.
    """
    @staticmethod
    def Bounding_s(thePolyh : IntPatch_Polyhedron) -> OCP.Bnd.Bnd_Box: 
        """
        Give the bounding box of the Polyhedron.
        """
    @staticmethod
    def ComponentsBounding_s(thePolyh : IntPatch_Polyhedron) -> OCP.Bnd.Bnd_HArray1OfBox: 
        """
        Give the array of boxes. The box <n> corresponding to the triangle <n>.
        """
    @staticmethod
    def DeflectionOverEstimation_s(thePolyh : IntPatch_Polyhedron) -> float: 
        """
        Give the tolerance of the polygon.
        """
    @staticmethod
    def NbTriangles_s(thePolyh : IntPatch_Polyhedron) -> int: 
        """
        Give the number of triangles in this polyhedral surface.
        """
    @staticmethod
    def Point_s(thePolyh : IntPatch_Polyhedron,Index : int) -> OCP.gp.gp_Pnt: 
        """
        Give the point of index i in the polyhedral surface.
        """
    @staticmethod
    def TriConnex_s(thePolyh : IntPatch_Polyhedron,Triang : int,Pivot : int,Pedge : int,TriCon : int,OtherP : int) -> int: 
        """
        Gives the address Tricon of the triangle connexe to the triangle of address Triang by the edge Pivot Pedge and the third point of this connexe triangle. When we are on a free edge TriCon==0 but the function return the value of the triangle in the other side of Pivot on the free edge. Used to turn around a vertex.
        """
    @staticmethod
    def Triangle_s(thePolyh : IntPatch_Polyhedron,Index : int) -> Tuple[int, int, int]: 
        """
        Give the indices of the 3 points of the triangle of address Index in the Polyhedron.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_PrmPrmIntersection():
    """
    Implementation of the Intersection between two bi-parametrised surfaces.
    """
    @overload
    def CodeReject(self,x0 : float,y0 : float,z0 : float,x1 : float,y1 : float,z1 : float,x : float,y : float,z : float) -> int: 
        """
        None

        None
        """
    @overload
    def CodeReject(self,x1 : float,y1 : float,z1 : float,x2 : float,y2 : float,z2 : float,x3 : float,y3 : float,z3 : float) -> int: ...
    def DansGrille(self,t : int) -> int: 
        """
        None

        None
        """
    def GrilleInteger(self,ix : int,iy : int,iz : int) -> int: 
        """
        None

        None
        """
    @overload
    def IntegerGrille(self,t : int) -> Tuple[int, int, int]: 
        """
        None

        None
        """
    @overload
    def IntegerGrille(self,tt : int) -> Tuple[int, int, int]: ...
    def IsDone(self) -> bool: 
        """
        Returns true if the calculus was successful.

        Returns true if the calculus was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if the is no intersection.

        Returns true if the is no intersection.
        """
    @overload
    def Line(self,n : int) -> IntPatch_Line: 
        """
        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.

        Returns the line of range Index. An exception is raised if Index<=0 or Index>NbLine.
        """
    @overload
    def Line(self,Index : int) -> IntPatch_Line: ...
    def NbLines(self) -> int: 
        """
        Returns the number of intersection lines.

        Returns the number of intersection lines.
        """
    def NbPointsGrille(self) -> int: 
        """
        None

        None
        """
    def NewLine(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,IndexLine : int,LowPoint : int,HighPoint : int,NbPoints : int) -> IntPatch_Line: 
        """
        Computes about <NbPoints> Intersection Points on the Line <IndexLine> between the Points of Index <LowPoint> and <HighPoint>.
        """
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,U1 : float,V1 : float,U2 : float,V2 : float,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: 
        """
        Performs the intersection between <Caro1> and <Caro2>. Associated Polyhedrons <Polyhedron1> and <Polyhedron2> are given.

        None

        Performs the intersection between <Caro1> and <Caro2>. The method computes the polyhedron on each surface.

        Performs the intersection between <Caro1> and <Caro2>. The method computes the polyhedron on each surface.

        Performs the intersection between <Caro1> and <Caro2>. The method computes the polyhedron on each surface.

        Performs the intersection between <Caro1> and <Caro2>. The method computes the polyhedron on each surface.

        Performs the intersection between <Caro1> and <Caro2>.

        Performs the intersection between <Caro1> and <Caro2>.
        """
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron1 : IntPatch_Polyhedron,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron2 : IntPatch_Polyhedron,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron1 : IntPatch_Polyhedron,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron1 : IntPatch_Polyhedron,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Polyhedron2 : IntPatch_Polyhedron,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float,ListOfPnts : OCP.IntSurf.IntSurf_ListOfPntOn2S) -> None: ...
    @overload
    def Perform(self,Caro1 : OCP.Adaptor3d.Adaptor3d_Surface,Domain1 : OCP.Adaptor3d.Adaptor3d_TopolTool,Caro2 : OCP.Adaptor3d.Adaptor3d_Surface,Domain2 : OCP.Adaptor3d.Adaptor3d_TopolTool,TolTangency : float,Epsilon : float,Deflection : float,Increment : float,ClearFlag : bool=True) -> None: ...
    def PointDepart(self,LineOn2S : OCP.IntSurf.IntSurf_LineOn2S,S1 : OCP.Adaptor3d.Adaptor3d_Surface,SU1 : int,SV1 : int,S2 : OCP.Adaptor3d.Adaptor3d_Surface,SU2 : int,SV2 : int) -> Any: 
        """
        None
        """
    def Remplit(self,a : int,b : int,c : int,Map : IntPatch_PrmPrmIntersection_T3Bits) -> None: 
        """
        None
        """
    def RemplitLin(self,x1 : int,y1 : int,z1 : int,x2 : int,y2 : int,z2 : int,Map : IntPatch_PrmPrmIntersection_T3Bits) -> None: 
        """
        None
        """
    def RemplitTri(self,x1 : int,y1 : int,z1 : int,x2 : int,y2 : int,z2 : int,x3 : int,y3 : int,z3 : int,Map : IntPatch_PrmPrmIntersection_T3Bits) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_PrmPrmIntersection_T3Bits():
    """
    None
    """
    def Add(self,t : int) -> None: 
        """
        None
        """
    def And(self,Oth : IntPatch_PrmPrmIntersection_T3Bits,indiceprecedent : int) -> int: 
        """
        None
        """
    def Raz(self,t : int) -> None: 
        """
        None
        """
    def ResetAnd(self) -> None: 
        """
        None
        """
    def Val(self,t : int) -> int: 
        """
        None
        """
    def __init__(self,size : int) -> None: ...
    pass
class IntPatch_RLine(IntPatch_PointLine, IntPatch_Line, OCP.Standard.Standard_Transient):
    """
    Implementation of an intersection line described by a restriction line on one of the surfaces.Implementation of an intersection line described by a restriction line on one of the surfaces.Implementation of an intersection line described by a restriction line on one of the surfaces.
    """
    def Add(self,L : OCP.IntSurf.IntSurf_LineOn2S) -> None: 
        """
        None

        None
        """
    @overload
    def AddVertex(self,thePnt : IntPatch_Point,theIsPrepend : bool) -> None: 
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new vertex will be added before the first element of vertices sequence. Otherwise, to the end of the sequence

        Adds a vertex in the list. If theIsPrepend == TRUE the new vertex will be added before the first element of vertices sequence. Otherwise, to the end of the sequence
        """
    @overload
    def AddVertex(self,Pnt : IntPatch_Point,theIsPrepend : bool=False) -> None: ...
    def ArcOnS1(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the concerned arc.

        Returns the concerned arc.
        """
    def ArcOnS2(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the concerned arc.

        Returns the concerned arc.
        """
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """
    def ChangeVertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    def ClearVertexes(self) -> None: 
        """
        Removes vertices from the line (i.e. cleans svtx member)
        """
    def ComputeVertexParameters(self,Tol : float) -> None: 
        """
        Set the parameters of all the vertex on the line. if a vertex is already in the line, its parameter is modified else a new point in the line is inserted.
        """
    @staticmethod
    def CurvatureRadiusOfIntersLine_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theUVPoint : OCP.IntSurf.IntSurf_PntOn2S) -> float: 
        """
        Returns the radius of curvature of the intersection line in given point. Returns negative value if computation is not possible.
        """
    def Curve(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        Returns set of intersection points

        Returns set of intersection points
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,theMode : int) -> None: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FirstPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.

        Returns the IntPoint corresponding to the FirstPoint. An exception is raised when HasFirstPoint returns False.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the line has a known First point. This point is given by the method FirstPoint().

        Returns True if the line has a known First point. This point is given by the method FirstPoint().
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the line has a known Last point. This point is given by the method LastPoint().

        Returns True if the line has a known Last point. This point is given by the method LastPoint().
        """
    def HasPolygon(self) -> bool: 
        """
        None

        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsArcOnS1(self) -> bool: 
        """
        Returns True if the intersection is on the domain of the first patch. Returns False if the intersection is on the domain of the second patch.

        Returns True if the intersection is on the domain of the first patch. Returns False if the intersection is on the domain of the second patch.
        """
    def IsArcOnS2(self) -> bool: 
        """
        Returns True if the intersection is on the domain of the first patch. Returns False if the intersection is on the domain of the second patch.

        Returns True if the intersection is on the domain of the first patch. Returns False if the intersection is on the domain of the second patch.
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
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    def LastPoint(self) -> IntPatch_Point: 
        """
        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.

        Returns the IntPoint corresponding to the LastPoint. An exception is raised when HasLastPoint returns False.
        """
    def NbPnts(self) -> int: 
        """
        Returns the number of intersection points.

        Returns the number of intersection points.
        """
    def NbVertex(self) -> int: 
        """
        Returns number of vertices (IntPatch_Point) of the line

        Returns number of vertices (IntPatch_Point) of the line
        """
    def ParamOnS1(self) -> Tuple[float, float]: 
        """
        None
        """
    def ParamOnS2(self) -> Tuple[float, float]: 
        """
        None
        """
    def Point(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the intersection point of range Index.

        Returns the intersection point of range Index.
        """
    def RemoveVertex(self,theIndex : int) -> None: 
        """
        Removes single vertex from the line

        Removes single vertex from the line
        """
    def Replace(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        Replaces the element of range Index in the list of points.

        Replaces the element of range Index in the list of points.
        """
    def SetArcOnS1(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None
        """
    def SetArcOnS2(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None
        """
    def SetCurve(self,theNewCurve : OCP.IntSurf.IntSurf_LineOn2S) -> None: 
        """
        None
        """
    def SetFirstPoint(self,IndFirst : int) -> None: 
        """
        None

        None
        """
    def SetLastPoint(self,IndLast : int) -> None: 
        """
        None

        None
        """
    def SetPoint(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        Set the Point of index <Index> in the LineOn2S
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
        """
    def Vertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    @overload
    def __init__(self,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
    @overload
    def __init__(self,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,Tang : bool) -> None: ...
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
class IntPatch_RstInt():
    """
    trouver les points d intersection entre la ligne de cheminement et les arcs de restriction
    """
    @staticmethod
    def PutVertexOnLine_s(L : IntPatch_Line,Surf : OCP.Adaptor3d.Adaptor3d_Surface,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,OtherSurf : OCP.Adaptor3d.Adaptor3d_Surface,OnFirst : bool,Tol : float) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_SequenceOfIWLineOfTheIWalking(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntPatch_TheIWLineOfTheIWalking) -> None: ...
    def Assign(self,theOther : IntPatch_SequenceOfIWLineOfTheIWalking) -> IntPatch_SequenceOfIWLineOfTheIWalking: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPatch_TheIWLineOfTheIWalking: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPatch_TheIWLineOfTheIWalking: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPatch_TheIWLineOfTheIWalking: 
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
    def First(self) -> IntPatch_TheIWLineOfTheIWalking: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPatch_TheIWLineOfTheIWalking) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPatch_TheIWLineOfTheIWalking) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPatch_TheIWLineOfTheIWalking: 
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
    def Prepend(self,theSeq : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntPatch_TheIWLineOfTheIWalking) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPatch_TheIWLineOfTheIWalking) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPatch_TheIWLineOfTheIWalking: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntPatch_SequenceOfIWLineOfTheIWalking) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntPatch_SequenceOfLine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntPatch_Line) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntPatch_SequenceOfLine) -> None: ...
    def Assign(self,theOther : IntPatch_SequenceOfLine) -> IntPatch_SequenceOfLine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPatch_Line: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPatch_Line: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPatch_Line: 
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
    def First(self) -> IntPatch_Line: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPatch_Line) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPatch_SequenceOfLine) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPatch_SequenceOfLine) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPatch_Line) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPatch_Line: 
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
    def Prepend(self,theItem : IntPatch_Line) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntPatch_SequenceOfLine) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPatch_Line) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPatch_SequenceOfLine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPatch_Line: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntPatch_SequenceOfLine) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntPatch_SequenceOfPathPointOfTheSOnBounds(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntPatch_ThePathPointOfTheSOnBounds) -> None: ...
    def Assign(self,theOther : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> IntPatch_SequenceOfPathPointOfTheSOnBounds: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPatch_ThePathPointOfTheSOnBounds: 
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
    def First(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPatch_ThePathPointOfTheSOnBounds) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPatch_ThePathPointOfTheSOnBounds) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
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
    def Prepend(self,theSeq : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntPatch_ThePathPointOfTheSOnBounds) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPatch_ThePathPointOfTheSOnBounds) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntPatch_SequenceOfPathPointOfTheSOnBounds) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntPatch_SequenceOfPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntPatch_SequenceOfPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntPatch_Point) -> None: ...
    def Assign(self,theOther : IntPatch_SequenceOfPoint) -> IntPatch_SequenceOfPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPatch_Point: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPatch_Point: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPatch_Point: 
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
    def First(self) -> IntPatch_Point: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPatch_Point) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPatch_SequenceOfPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPatch_SequenceOfPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPatch_Point) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPatch_Point: 
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
    def Prepend(self,theSeq : IntPatch_SequenceOfPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntPatch_Point) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPatch_Point) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPatch_SequenceOfPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPatch_Point: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : IntPatch_SequenceOfPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntPatch_SequenceOfSegmentOfTheSOnBounds(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntPatch_TheSegmentOfTheSOnBounds) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: ...
    def Assign(self,theOther : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> IntPatch_SequenceOfSegmentOfTheSOnBounds: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntPatch_TheSegmentOfTheSOnBounds: 
        """
        First item access
        """
    def ChangeLast(self) -> IntPatch_TheSegmentOfTheSOnBounds: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntPatch_TheSegmentOfTheSOnBounds: 
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
    def First(self) -> IntPatch_TheSegmentOfTheSOnBounds: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntPatch_TheSegmentOfTheSOnBounds) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntPatch_TheSegmentOfTheSOnBounds) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntPatch_TheSegmentOfTheSOnBounds: 
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
    def Prepend(self,theSeq : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntPatch_TheSegmentOfTheSOnBounds) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntPatch_TheSegmentOfTheSOnBounds) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntPatch_TheSegmentOfTheSOnBounds: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntPatch_SequenceOfSegmentOfTheSOnBounds) -> None: ...
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
class IntPatch_SpecPntType():
    """
    This enum describe the different kinds of special (singular) points of Surface-Surface intersection algorithm. Such as pole of sphere, apex of cone, point on U- or V-seam etc.

    Members:

      IntPatch_SPntNone

      IntPatch_SPntSeamU

      IntPatch_SPntSeamV

      IntPatch_SPntSeamUV

      IntPatch_SPntPoleSeamU

      IntPatch_SPntPole
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
    IntPatch_SPntNone: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntNone: 0>
    IntPatch_SPntPole: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntPole: 5>
    IntPatch_SPntPoleSeamU: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntPoleSeamU: 4>
    IntPatch_SPntSeamU: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamU: 1>
    IntPatch_SPntSeamUV: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamUV: 3>
    IntPatch_SPntSeamV: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamV: 2>
    __entries: dict # value = {'IntPatch_SPntNone': (<IntPatch_SpecPntType.IntPatch_SPntNone: 0>, None), 'IntPatch_SPntSeamU': (<IntPatch_SpecPntType.IntPatch_SPntSeamU: 1>, None), 'IntPatch_SPntSeamV': (<IntPatch_SpecPntType.IntPatch_SPntSeamV: 2>, None), 'IntPatch_SPntSeamUV': (<IntPatch_SpecPntType.IntPatch_SPntSeamUV: 3>, None), 'IntPatch_SPntPoleSeamU': (<IntPatch_SpecPntType.IntPatch_SPntPoleSeamU: 4>, None), 'IntPatch_SPntPole': (<IntPatch_SpecPntType.IntPatch_SPntPole: 5>, None)}
    __members__: dict # value = {'IntPatch_SPntNone': <IntPatch_SpecPntType.IntPatch_SPntNone: 0>, 'IntPatch_SPntSeamU': <IntPatch_SpecPntType.IntPatch_SPntSeamU: 1>, 'IntPatch_SPntSeamV': <IntPatch_SpecPntType.IntPatch_SPntSeamV: 2>, 'IntPatch_SPntSeamUV': <IntPatch_SpecPntType.IntPatch_SPntSeamUV: 3>, 'IntPatch_SPntPoleSeamU': <IntPatch_SpecPntType.IntPatch_SPntPoleSeamU: 4>, 'IntPatch_SPntPole': <IntPatch_SpecPntType.IntPatch_SPntPole: 5>}
    pass
class IntPatch_SpecialPoints():
    """
    None
    """
    @staticmethod
    def AddCrossUVIsoPoint_s(theQSurf : OCP.Adaptor3d.Adaptor3d_Surface,thePSurf : OCP.Adaptor3d.Adaptor3d_Surface,theRefPt : OCP.IntSurf.IntSurf_PntOn2S,theTol3d : float,theAddedPoint : OCP.IntSurf.IntSurf_PntOn2S,theIsReversed : bool=False) -> bool: 
        """
        Adds the point defined as intersection of two isolines (U = 0 and V = 0) on theQSurf in theLine. theRefPt is used to correct adjusting parameters. If theIsReversed is TRUE then theQSurf correspond to the second (otherwise, the first) surface while forming intersection point IntSurf_PntOn2S.
        """
    @staticmethod
    def AddPointOnUorVIso_s(theQSurf : OCP.Adaptor3d.Adaptor3d_Surface,thePSurf : OCP.Adaptor3d.Adaptor3d_Surface,theRefPt : OCP.IntSurf.IntSurf_PntOn2S,theIsU : bool,theIsoParameter : float,theToler : OCP.math.math_Vector,theInitPoint : OCP.math.math_Vector,theInfBound : OCP.math.math_Vector,theSupBound : OCP.math.math_Vector,theAddedPoint : OCP.IntSurf.IntSurf_PntOn2S,theIsReversed : bool=False) -> bool: 
        """
        Adds the point lain strictly in the isoline U = 0 or V = 0 of theQSurf, in theLine. theRefPt is used to correct adjusting parameters. If theIsReversed is TRUE then theQSurf corresponds to the second (otherwise, the first) surface while forming intersection point IntSurf_PntOn2S. All math_Vector-objects must be filled as follows: [1] - U-parameter of thePSurf; [2] - V-parameter of thePSurf; [3] - U- (if V-isoline is considered) or V-parameter (if U-isoline is considered) of theQSurf.
        """
    @staticmethod
    def AddSingularPole_s(theQSurf : OCP.Adaptor3d.Adaptor3d_Surface,thePSurf : OCP.Adaptor3d.Adaptor3d_Surface,thePtIso : OCP.IntSurf.IntSurf_PntOn2S,theVertex : IntPatch_Point,theAddedPoint : OCP.IntSurf.IntSurf_PntOn2S,theIsReversed : bool=False,theIsReqRefCheck : bool=False) -> bool: 
        """
        Computes the pole of sphere to add it in the intersection line. Stores the result in theAddedPoint variable (does not add in the line). At that, cone and sphere (with singularity) must be set in theQSurf parameter. By default (if theIsReversed == FALSE), theQSurf is the first surface of the Walking line. If it is not, theIsReversed parameter must be set to TRUE. theIsReqRefCheck is TRUE if and only if 3D-point of theRefPt must be pole or apex for check (e.g. if it is vertex). thePtIso is the reference point for obtaining isoline where must be placed the Apex/Pole.
        """
    @staticmethod
    def AdjustPointAndVertex_s(theRefPoint : OCP.IntSurf.IntSurf_PntOn2S,theArrPeriods : float,theNewPoint : OCP.IntSurf.IntSurf_PntOn2S,theVertex : IntPatch_Point=None) -> None: 
        """
        Sets theNewPoint parameters in 2D-space the closest to theRefPoint with help of adding/subtracting corresponding periods. theArrPeriods must be filled as follows: {<U-period of 1st surface>, <V-period of 1st surface>, <U-period of 2nd surface>, <V-period of 2nd surface>}. If theVertex != 0 then its parameters will be filled as corresponding parameters of theNewPoint.
        """
    @staticmethod
    def ContinueAfterSpecialPoint_s(theQSurf : OCP.Adaptor3d.Adaptor3d_Surface,thePSurf : OCP.Adaptor3d.Adaptor3d_Surface,theRefPt : OCP.IntSurf.IntSurf_PntOn2S,theSPType : IntPatch_SpecPntType,theTol2D : float,theNewPoint : OCP.IntSurf.IntSurf_PntOn2S,theIsReversed : bool=False) -> bool: 
        """
        Special point has already been added in the line. Now, we need in correct prolongation of the line or in start new line. This function returns new point.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_TheIWLineOfTheIWalking(OCP.Standard.Standard_Transient):
    def AddIndexPassing(self,Index : int) -> None: 
        """
        associer a l 'indice du point sur la ligne l'indice du point passant dans l'iterateur de depart
        """
    def AddPoint(self,P : OCP.IntSurf.IntSurf_PntOn2S) -> None: 
        """
        Add a point in the line.
        """
    @overload
    def AddStatusFirst(self,Closed : bool,HasLast : bool,Index : int,P : OCP.IntSurf.IntSurf_PathPoint) -> None: 
        """
        None

        None
        """
    @overload
    def AddStatusFirst(self,Closed : bool,HasFirst : bool) -> None: ...
    def AddStatusFirstLast(self,Closed : bool,HasFirst : bool,HasLast : bool) -> None: 
        """
        None
        """
    @overload
    def AddStatusLast(self,HasLast : bool,Index : int,P : OCP.IntSurf.IntSurf_PathPoint) -> None: 
        """
        None

        None
        """
    @overload
    def AddStatusLast(self,HasLast : bool) -> None: ...
    def Cut(self,Index : int) -> None: 
        """
        Cut the line at the point of rank Index.
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
    def FirstPoint(self) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the first point of the line when it is a marching point. An exception is raised if HasFirstPoint returns False.
        """
    def FirstPointIndex(self) -> int: 
        """
        Returns the Index of first point of the line when it is a marching point.This index is the index in the PointStartIterator. An exception is raised if HasFirstPoint returns False.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the first point of the line is a marching point . when is HasFirstPoint==False ,the line begins on the natural bound of the surface.the line can be too long
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the end point of the line is a marching point (Point from IntWS). when is HasFirstPoint==False ,the line ends on the natural bound of the surface.the line can be too long.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the line is closed.
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
    def IsTangentAtBegining(self) -> bool: 
        """
        None
        """
    def IsTangentAtEnd(self) -> bool: 
        """
        None
        """
    def LastPoint(self) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the last point of the line when it is a marching point. An exception is raised if HasLastPoint returns False.
        """
    def LastPointIndex(self) -> int: 
        """
        Returns the index of last point of the line when it is a marching point.This index is the index in the PointStartIterator. An exception is raised if HasLastPoint returns False.
        """
    def Line(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        Returns the LineOn2S contained in the walking line.
        """
    def NbPassingPoint(self) -> int: 
        """
        returns the number of points belonging to Pnts1 which are passing point.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points of the line (including first point and end point : see HasLastPoint and HasFirstPoint).
        """
    def PassingPoint(self,Index : int) -> Tuple[int, int]: 
        """
        returns the index of the point belonging to the line which is associated to the passing point belonging to Pnts1 an exception is raised if Index > NbPassingPoint()
        """
    def Reverse(self) -> None: 
        """
        reverse the points in the line. Hasfirst, HasLast are kept.
        """
    def SetTangencyAtBegining(self,IsTangent : bool) -> None: 
        """
        None
        """
    def SetTangencyAtEnd(self,IsTangent : bool) -> None: 
        """
        None
        """
    def SetTangentVector(self,V : OCP.gp.gp_Vec,Index : int) -> None: 
        """
        None
        """
    def TangentVector(self,Index : int) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the point of range Index. If index <= 0 or Index > NbPoints, an exception is raised.
        """
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
class IntPatch_TheIWalking():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        Returns true if the calculus was successful.
        """
    def NbLines(self) -> int: 
        """
        Returns the number of resulting polylines. An exception is raised if IsDone returns False.
        """
    def NbSinglePnts(self) -> int: 
        """
        Returns the number of points belonging to Pnts on which no line starts or ends. An exception is raised if IsDone returns False.
        """
    @overload
    def Perform(self,Pnts1 : OCP.IntSurf.IntSurf_SequenceOfPathPoint,Pnts2 : OCP.IntSurf.IntSurf_SequenceOfInteriorPoint,Func : IntPatch_TheSurfFunction,S : OCP.Adaptor3d.Adaptor3d_Surface,Reversed : bool=False) -> None: 
        """
        Searches a set of polylines starting on a point of Pnts1 or Pnts2. Each point on a resulting polyline verifies F(u,v)=0

        Searches a set of polylines starting on a point of Pnts1. Each point on a resulting polyline verifies F(u,v)=0
        """
    @overload
    def Perform(self,Pnts1 : OCP.IntSurf.IntSurf_SequenceOfPathPoint,Func : IntPatch_TheSurfFunction,S : OCP.Adaptor3d.Adaptor3d_Surface,Reversed : bool=False) -> None: ...
    def SetTolerance(self,Epsilon : float,Deflection : float,Step : float) -> None: 
        """
        Deflection is the maximum deflection admitted between two consecutive points on a resulting polyline. Step is the maximum increment admitted between two consecutive points (in 2d space). Epsilon is the tolerance beyond which 2 points are confused
        """
    def SinglePnt(self,Index : int) -> OCP.IntSurf.IntSurf_PathPoint: 
        """
        Returns the point of range Index . An exception is raised if IsDone returns False. An exception is raised if Index<=0 or Index > NbSinglePnts.
        """
    def Value(self,Index : int) -> IntPatch_TheIWLineOfTheIWalking: 
        """
        Returns the polyline of range Index. An exception is raised if IsDone is False. An exception is raised if Index<=0 or Index>NbLines.
        """
    def __init__(self,Epsilon : float,Deflection : float,Step : float,theToFillHoles : bool=False) -> None: ...
    pass
class IntPatch_ThePathPointOfTheSOnBounds():
    """
    None
    """
    def Arc(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def IsNew(self) -> bool: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,Tol : float,V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_Curve2d,Parameter : float) -> None: 
        """
        None

        None
        """
    @overload
    def SetValue(self,P : OCP.gp.gp_Pnt,Tol : float,A : OCP.Adaptor2d.Adaptor2d_Curve2d,Parameter : float) -> None: ...
    def Tolerance(self) -> float: 
        """
        None
        """
    def Value(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Vertex(self) -> OCP.Adaptor3d.Adaptor3d_HVertex: 
        """
        None
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Tol : float,A : OCP.Adaptor2d.Adaptor2d_Curve2d,Parameter : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,Tol : float,V : OCP.Adaptor3d.Adaptor3d_HVertex,A : OCP.Adaptor2d.Adaptor2d_Curve2d,Parameter : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntPatch_TheSOnBounds():
    """
    None
    """
    def AllArcSolution(self) -> bool: 
        """
        Returns true if all arc of the Arcs are solution (inside the surface). An exception is raised if IsDone returns False.
        """
    def IsDone(self) -> bool: 
        """
        Returns True if the calculus was successful.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of resulting points. An exception is raised if IsDone returns False (NotDone).
        """
    def NbSegments(self) -> int: 
        """
        Returns the number of the resulting segments. An exception is raised if IsDone returns False (NotDone).
        """
    def Perform(self,F : IntPatch_ArcFunction,Domain : OCP.Adaptor3d.Adaptor3d_TopolTool,TolBoundary : float,TolTangency : float,RecheckOnRegularity : bool=False) -> None: 
        """
        Algorithm to find the points and parts of curves of Domain (domain of of restriction of a surface) which verify F = 0. TolBoundary defines if a curve is on Q. TolTangency defines if a point is on Q.
        """
    def Point(self,Index : int) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        Returns the resulting point of range Index. The exception NotDone is raised if IsDone() returns False. The exception OutOfRange is raised if Index <= 0 or Index > NbPoints.
        """
    def Segment(self,Index : int) -> IntPatch_TheSegmentOfTheSOnBounds: 
        """
        Returns the resulting segment of range Index. The exception NotDone is raised if IsDone() returns False. The exception OutOfRange is raised if Index <= 0 or Index > NbPoints.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_TheSearchInside():
    """
    None
    """
    def IsDone(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points. The exception NotDone if raised if IsDone returns False.
        """
    @overload
    def Perform(self,F : IntPatch_TheSurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_Surface,UStart : float,VStart : float) -> None: 
        """
        None

        None
        """
    @overload
    def Perform(self,F : IntPatch_TheSurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_Surface,T : OCP.Adaptor3d.Adaptor3d_TopolTool,Epsilon : float) -> None: ...
    def Value(self,Index : int) -> OCP.IntSurf.IntSurf_InteriorPoint: 
        """
        Returns the point of range Index. The exception NotDone if raised if IsDone returns False. The exception OutOfRange if raised if Index <= 0 or Index > NbPoints.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : IntPatch_TheSurfFunction,Surf : OCP.Adaptor3d.Adaptor3d_Surface,T : OCP.Adaptor3d.Adaptor3d_TopolTool,Epsilon : float) -> None: ...
    pass
class IntPatch_TheSegmentOfTheSOnBounds():
    """
    None
    """
    def Curve(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        Returns the geometric curve on the surface 's domain which is solution.
        """
    def FirstPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        Returns the first point.
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if there is a vertex (ThePathPoint) defining the lowest valid parameter on the arc.
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if there is a vertex (ThePathPoint) defining the greatest valid parameter on the arc.
        """
    def LastPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds: 
        """
        Returns the last point.
        """
    def SetLimitPoint(self,V : IntPatch_ThePathPointOfTheSOnBounds,First : bool) -> None: 
        """
        Defines the first point or the last point, depending on the value of the boolean First.
        """
    def SetValue(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        Defines the concerned arc.
        """
    def __init__(self) -> None: ...
    pass
class IntPatch_TheSurfFunction(OCP.math.math_FunctionSetWithDerivatives, OCP.math.math_FunctionSet):
    """
    None
    """
    def Derivatives(self,X : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    def Direction2d(self) -> OCP.gp.gp_Dir2d: 
        """
        None
        """
    def Direction3d(self) -> OCP.gp.gp_Vec: 
        """
        None
        """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def ISurface(self) -> OCP.IntSurf.IntSurf_Quadric: 
        """
        None
        """
    def IsTangent(self) -> bool: 
        """
        None
        """
    def NbEquations(self) -> int: 
        """
        None
        """
    def NbVariables(self) -> int: 
        """
        None
        """
    def PSurface(self) -> OCP.Adaptor3d.Adaptor3d_Surface: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def Root(self) -> float: 
        """
        None
        """
    @overload
    def Set(self,Tolerance : float) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,PS : OCP.Adaptor3d.Adaptor3d_Surface) -> None: ...
    def SetImplicitSurface(self,IS : OCP.IntSurf.IntSurf_Quadric) -> None: 
        """
        None
        """
    def Tolerance(self) -> float: 
        """
        Returns the value Tol so that if Abs(Func.Root())<Tol the function is considered null.
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        None
        """
    def Values(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector,D : OCP.math.math_Matrix) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,IS : OCP.IntSurf.IntSurf_Quadric) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,PS : OCP.Adaptor3d.Adaptor3d_Surface,IS : OCP.IntSurf.IntSurf_Quadric) -> None: ...
    pass
class IntPatch_WLine(IntPatch_PointLine, IntPatch_Line, OCP.Standard.Standard_Transient):
    """
    Definition of set of points as a result of the intersection between 2 parametrised patches.Definition of set of points as a result of the intersection between 2 parametrised patches.Definition of set of points as a result of the intersection between 2 parametrised patches.
    """
    class IntPatch_WLType_e():
        """
        Enumeration of ways of WLine creation.

        Members:

          IntPatch_WLUnknown

          IntPatch_WLImpImp

          IntPatch_WLImpPrm

          IntPatch_WLPrmPrm
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
        IntPatch_WLImpImp: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLImpImp: 1>
        IntPatch_WLImpPrm: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLImpPrm: 2>
        IntPatch_WLPrmPrm: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLPrmPrm: 3>
        IntPatch_WLUnknown: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLUnknown: 0>
        __entries: dict # value = {'IntPatch_WLUnknown': (<IntPatch_WLType_e.IntPatch_WLUnknown: 0>, None), 'IntPatch_WLImpImp': (<IntPatch_WLType_e.IntPatch_WLImpImp: 1>, None), 'IntPatch_WLImpPrm': (<IntPatch_WLType_e.IntPatch_WLImpPrm: 2>, None), 'IntPatch_WLPrmPrm': (<IntPatch_WLType_e.IntPatch_WLPrmPrm: 3>, None)}
        __members__: dict # value = {'IntPatch_WLUnknown': <IntPatch_WLType_e.IntPatch_WLUnknown: 0>, 'IntPatch_WLImpImp': <IntPatch_WLType_e.IntPatch_WLImpImp: 1>, 'IntPatch_WLImpPrm': <IntPatch_WLType_e.IntPatch_WLImpPrm: 2>, 'IntPatch_WLPrmPrm': <IntPatch_WLType_e.IntPatch_WLPrmPrm: 3>}
        pass
    @overload
    def AddVertex(self,Pnt : IntPatch_Point,theIsPrepend : bool=False) -> None: 
        """
        Adds a vertex in the list. If theIsPrepend == TRUE the new vertex will be added before the first element of vertices sequence. Otherwise, to the end of the sequence

        Adds a vertex in the list. If theIsPrepend == TRUE the new vertex will be added before the first element of vertices sequence. Otherwise, to the end of the sequence
        """
    @overload
    def AddVertex(self,thePnt : IntPatch_Point,theIsPrepend : bool) -> None: ...
    def ArcType(self) -> IntPatch_IType: 
        """
        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)

        Returns the type of geometry 3d (Line, Circle, Parabola, Hyperbola, Ellipse, Analytic, Walking, Restriction)
        """
    def ChangeVertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    def ClearVertexes(self) -> None: 
        """
        Removes vertices from the line (i.e. cleans svtx member)

        Removes vertices from the line (i.e. cleans svtx member)
        """
    def ComputeVertexParameters(self,Tol : float) -> None: 
        """
        Set the parameters of all the vertex on the line. if a vertex is already in the line, its parameter is modified else a new point in the line is inserted.
        """
    @staticmethod
    def CurvatureRadiusOfIntersLine_s(theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theUVPoint : OCP.IntSurf.IntSurf_PntOn2S) -> float: 
        """
        Returns the radius of curvature of the intersection line in given point. Returns negative value if computation is not possible.
        """
    def Curve(self) -> OCP.IntSurf.IntSurf_LineOn2S: 
        """
        Returns set of intersection points
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self,theMode : int) -> None: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnablePurging(self,theIsEnabled : bool) -> None: 
        """
        Allows or forbids purging of existing WLine
        """
    @overload
    def FirstPoint(self,Indfirst : int) -> IntPatch_Point: 
        """
        Returns the Point corresponding to the FirstPoint. Indfirst is the index of the first in the list of vertices.

        Returns the Point corresponding to the FirstPoint. Indfirst is the index of the first in the list of vertices.

        Returns the Point corresponding to the FirstPoint.

        Returns the Point corresponding to the FirstPoint.
        """
    @overload
    def FirstPoint(self) -> IntPatch_Point: ...
    def GetArcOnS1(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def GetArcOnS2(self) -> OCP.Adaptor2d.Adaptor2d_Curve2d: 
        """
        None
        """
    def GetCreatingWay(self) -> IntPatch_WLine.IntPatch_WLType_e: 
        """
        Returns the way of <*this> creation.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasArcOnS1(self) -> bool: 
        """
        None
        """
    def HasArcOnS2(self) -> bool: 
        """
        None
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the line has a known First point. This point is given by the method FirstPoint().

        Returns True if the line has a known First point. This point is given by the method FirstPoint().
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the line has a known Last point. This point is given by the method LastPoint().

        Returns True if the line has a known Last point. This point is given by the method LastPoint().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InsertVertexBefore(self,theIndex : int,thePnt : IntPatch_Point) -> None: 
        """
        None

        None
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
    def IsPurgingAllowed(self) -> bool: 
        """
        Returns TRUE if purging is allowed or forbidden for existing WLine
        """
    def IsTangent(self) -> bool: 
        """
        Returns TRUE if the intersection is a line of tangency between the 2 patches.

        Returns TRUE if the intersection is a line of tangency between the 2 patches.
        """
    def IsUIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the first patch.

        Returns TRUE if the intersection is a U isoparametric curve on the first patch.
        """
    def IsUIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a U isoparametric curve on the second patch.

        Returns TRUE if the intersection is a U isoparametric curve on the second patch.
        """
    def IsVIsoOnS1(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the first patch.

        Returns TRUE if the intersection is a V isoparametric curve on the first patch.
        """
    def IsVIsoOnS2(self) -> bool: 
        """
        Returns TRUE if the intersection is a V isoparametric curve on the second patch.

        Returns TRUE if the intersection is a V isoparametric curve on the second patch.
        """
    @overload
    def LastPoint(self,Indlast : int) -> IntPatch_Point: 
        """
        Returns the Point corresponding to the LastPoint. Indlast is the index of the last in the list of vertices.

        Returns the Point corresponding to the LastPoint. Indlast is the index of the last in the list of vertices.

        Returns the Point corresponding to the LastPoint.

        Returns the Point corresponding to the LastPoint.
        """
    @overload
    def LastPoint(self) -> IntPatch_Point: ...
    def NbPnts(self) -> int: 
        """
        Returns the number of intersection points.

        Returns the number of intersection points.
        """
    def NbVertex(self) -> int: 
        """
        Returns number of vertices (IntPatch_Point) of the line

        Returns number of vertices (IntPatch_Point) of the line
        """
    def Point(self,Index : int) -> OCP.IntSurf.IntSurf_PntOn2S: 
        """
        Returns the intersection point of range Index.

        Returns the intersection point of range Index.
        """
    def RemoveVertex(self,theIndex : int) -> None: 
        """
        Removes single vertex from the line

        Removes single vertex from the line
        """
    def Replace(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        Replaces the element of range Index in the list of points. The exception OutOfRange is raised when Index <= 0 or Index > NbVertex.

        Replaces the element of range Index in the list of points. The exception OutOfRange is raised when Index <= 0 or Index > NbVertex.
        """
    def SetArcOnS1(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None
        """
    def SetArcOnS2(self,A : OCP.Adaptor2d.Adaptor2d_Curve2d) -> None: 
        """
        None
        """
    def SetCreatingWayInfo(self,theAlgo : IntPatch_WLine.IntPatch_WLType_e) -> None: 
        """
        Sets the info about the way of <*this> creation.
        """
    def SetFirstPoint(self,IndFirst : int) -> None: 
        """
        None

        None
        """
    def SetLastPoint(self,IndLast : int) -> None: 
        """
        None

        None
        """
    def SetPeriod(self,pu1 : float,pv1 : float,pu2 : float,pv2 : float) -> None: 
        """
        None
        """
    def SetPoint(self,Index : int,Pnt : IntPatch_Point) -> None: 
        """
        Set the Point of index <Index> in the LineOn2S
        """
    def SetValue(self,Uiso1 : bool,Viso1 : bool,Uiso2 : bool,Viso2 : bool) -> None: 
        """
        To set the values returned by IsUIsoS1,.... The default values are False.

        To set the values returned by IsUIsoS1,.... The default values are False.
        """
    def SituationS1(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the first patch compared to the second one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def SituationS2(self) -> OCP.IntSurf.IntSurf_Situation: 
        """
        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.

        Returns the situation (INSIDE/OUTSIDE/UNKNOWN) of the second patch compared to the first one, when TransitionOnS1 or TransitionOnS2 returns TOUCH. Otherwise, an exception is raised.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransitionOnS1(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.

        Returns the type of the transition of the line for the first surface. The transition is "constant" along the line. The transition is IN if the line is oriented in such a way that the system of vector (N1,N2,T) is right-handed, where N1 is the normal to the first surface at a point P, N2 is the normal to the second surface at a point P, T is the tangent to the intersection line at P. If the system of vector is left-handed, the transition is OUT. When N1 and N2 are colinear all along the intersection line, the transition will be - TOUCH, if it is possible to use the 2nd derivatives to determine the position of one surafce compared to the other (see Situation) - UNDECIDED otherwise.
        """
    def TransitionOnS2(self) -> OCP.IntSurf.IntSurf_TypeTrans: 
        """
        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.

        Returns the type of the transition of the line for the second surface. The transition is "constant" along the line.
        """
    def U1Period(self) -> float: 
        """
        None
        """
    def U2Period(self) -> float: 
        """
        None
        """
    def V1Period(self) -> float: 
        """
        None
        """
    def V2Period(self) -> float: 
        """
        None
        """
    def Vertex(self,Index : int) -> IntPatch_Point: 
        """
        Returns the vertex of range Index on the line.

        Returns the vertex of range Index on the line.
        """
    @overload
    def __init__(self,Line : OCP.IntSurf.IntSurf_LineOn2S,Tang : bool) -> None: ...
    @overload
    def __init__(self,Line : OCP.IntSurf.IntSurf_LineOn2S,Tang : bool,Trans1 : OCP.IntSurf.IntSurf_TypeTrans,Trans2 : OCP.IntSurf.IntSurf_TypeTrans) -> None: ...
    @overload
    def __init__(self,Line : OCP.IntSurf.IntSurf_LineOn2S,Tang : bool,Situ1 : OCP.IntSurf.IntSurf_Situation,Situ2 : OCP.IntSurf.IntSurf_Situation) -> None: ...
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
    IntPatch_WLImpImp: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLImpImp: 1>
    IntPatch_WLImpPrm: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLImpPrm: 2>
    IntPatch_WLPrmPrm: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLPrmPrm: 3>
    IntPatch_WLUnknown: OCP.IntPatch.IntPatch_WLType_e # value = <IntPatch_WLType_e.IntPatch_WLUnknown: 0>
    pass
class IntPatch_WLineTool():
    """
    IntPatch_WLineTool provides set of static methods related to walking lines.
    """
    @staticmethod
    def ComputePurgedWLine_s(theWLine : IntPatch_WLine,theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theDom1 : OCP.Adaptor3d.Adaptor3d_TopolTool,theDom2 : OCP.Adaptor3d.Adaptor3d_TopolTool) -> IntPatch_WLine: 
        """
        I Removes equal points (leave one of equal points) from theWLine and recompute vertex parameters.
        """
    @staticmethod
    def ExtendTwoWLines_s(theSlin : IntPatch_SequenceOfLine,theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theToler3D : float,theArrPeriods : float,theBoxS1 : OCP.Bnd.Bnd_Box2d,theBoxS2 : OCP.Bnd.Bnd_Box2d,theListOfCriticalPoints : Any) -> None: 
        """
        Extends every line from theSlin (if it is possible) to be started/finished in strictly determined point (in the place of joint of two lines). As result, some gaps between two lines will vanish. The Walking lines are supposed (algorithm will do nothing for not-Walking line) to be computed as a result of intersection. Both theS1 and theS2 must be quadrics. Other cases are not supported. theArrPeriods must be filled as follows (every value must not be negative; if the surface is not periodic the period must be equal to 0.0 strictly): {<U-period of 1st surface>, <V-period of 1st surface>, <U-period of 2nd surface>, <V-period of 2nd surface>}. theListOfCriticalPoints must contain 3D-points where joining is disabled.
        """
    @staticmethod
    def JoinWLines_s(theSlin : IntPatch_SequenceOfLine,theSPnt : IntPatch_SequenceOfPoint,theS1 : OCP.Adaptor3d.Adaptor3d_Surface,theS2 : OCP.Adaptor3d.Adaptor3d_Surface,theTol3D : float) -> None: 
        """
        Joins all WLines from theSlin to one if it is possible and records the result into theSlin again. Lines will be kept to be split if: a) they are separated (has no common points); b) resulted line (after joining) go through seam-edges or surface boundaries.
        """
    def __init__(self) -> None: ...
    pass
IntPatch_Analytic: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Analytic: 5>
IntPatch_Circle: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Circle: 1>
IntPatch_Ellipse: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Ellipse: 2>
IntPatch_Hyperbola: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Hyperbola: 4>
IntPatch_Lin: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Lin: 0>
IntPatch_Parabola: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Parabola: 3>
IntPatch_Restriction: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Restriction: 7>
IntPatch_SPntNone: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntNone: 0>
IntPatch_SPntPole: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntPole: 5>
IntPatch_SPntPoleSeamU: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntPoleSeamU: 4>
IntPatch_SPntSeamU: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamU: 1>
IntPatch_SPntSeamUV: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamUV: 3>
IntPatch_SPntSeamV: OCP.IntPatch.IntPatch_SpecPntType # value = <IntPatch_SpecPntType.IntPatch_SPntSeamV: 2>
IntPatch_Walking: OCP.IntPatch.IntPatch_IType # value = <IntPatch_IType.IntPatch_Walking: 6>
