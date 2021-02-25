import OCP.FairCurve
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColStd
import io
import OCP.math
import OCP.gp
import OCP.TColgp
import OCP.Geom2d
__all__  = [
"FairCurve_AnalysisCode",
"FairCurve_Batten",
"FairCurve_BattenLaw",
"FairCurve_DistributionOfEnergy",
"FairCurve_DistributionOfJerk",
"FairCurve_DistributionOfSagging",
"FairCurve_DistributionOfTension",
"FairCurve_Energy",
"FairCurve_EnergyOfBatten",
"FairCurve_EnergyOfMVC",
"FairCurve_MinimalVariation",
"FairCurve_Newton",
"FairCurve_InfiniteSliding",
"FairCurve_NotConverged",
"FairCurve_NullHeight",
"FairCurve_OK"
]
class FairCurve_AnalysisCode():
    """
    To deal with different results in the computation of curvatures. - FairCurve_OK describes the case where computation is successfully completed - FairCurve_NotConverged describes the case where the algorithm does not converge. In this case, you can not be certain of the result quality and should resume computation if you want to make use of the curve. - FairCurve_InfiniteSliding describes the case where sliding is infinite, and, consequently, computation stops. The solution is to use an imposed sliding value. - FairCurve_NullHeight describes the case where no matter is left at one of the ends of the curve, and as a result, computation stops. The solution is to change (increase or reduce) the slope value by increasing or decreasing it.

    Members:

      FairCurve_OK

      FairCurve_NotConverged

      FairCurve_InfiniteSliding

      FairCurve_NullHeight
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
    FairCurve_InfiniteSliding: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_InfiniteSliding: 2>
    FairCurve_NotConverged: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_NotConverged: 1>
    FairCurve_NullHeight: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_NullHeight: 3>
    FairCurve_OK: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_OK: 0>
    __entries: dict # value = {'FairCurve_OK': (<FairCurve_AnalysisCode.FairCurve_OK: 0>, None), 'FairCurve_NotConverged': (<FairCurve_AnalysisCode.FairCurve_NotConverged: 1>, None), 'FairCurve_InfiniteSliding': (<FairCurve_AnalysisCode.FairCurve_InfiniteSliding: 2>, None), 'FairCurve_NullHeight': (<FairCurve_AnalysisCode.FairCurve_NullHeight: 3>, None)}
    __members__: dict # value = {'FairCurve_OK': <FairCurve_AnalysisCode.FairCurve_OK: 0>, 'FairCurve_NotConverged': <FairCurve_AnalysisCode.FairCurve_NotConverged: 1>, 'FairCurve_InfiniteSliding': <FairCurve_AnalysisCode.FairCurve_InfiniteSliding: 2>, 'FairCurve_NullHeight': <FairCurve_AnalysisCode.FairCurve_NullHeight: 3>}
    pass
class FairCurve_Batten():
    """
    Constructs curves with a constant or linearly increasing section to be used in the design of wooden or plastic battens. These curves are two-dimensional, and simulate physical splines or battens.
    """
    def Compute(self,Code : FairCurve_AnalysisCode,NbIterations : int=50,Tolerance : float=0.001) -> bool: 
        """
        Performs the algorithm, using the arguments Code, NbIterations and Tolerance and computes the curve with respect to the constraints. Code will have one of the following values: - OK - NotConverged - InfiniteSliding - NullHeight The parameters Tolerance and NbIterations control how precise the computation is, and how long it will take.
        """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns the computed curve a 2d BSpline.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object.
        """
    def GetAngle1(self) -> float: 
        """
        Returns the established first angle.

        Returns the established first angle.
        """
    def GetAngle2(self) -> float: 
        """
        Returns the established second angle.

        Returns the established second angle.
        """
    def GetConstraintOrder1(self) -> int: 
        """
        Returns the established first constraint order.

        Returns the established first constraint order.
        """
    def GetConstraintOrder2(self) -> int: 
        """
        Returns the established second constraint order.

        Returns the established second constraint order.
        """
    def GetFreeSliding(self) -> bool: 
        """
        Returns the initial free sliding value, false by default. Free sliding is generally more aesthetically pleasing than constrained sliding. However, the computation can fail with values such as angles greater than PI/2. This is because the resulting batten length is theoretically infinite.

        Returns the initial free sliding value, false by default. Free sliding is generally more aesthetically pleasing than constrained sliding. However, the computation can fail with values such as angles greater than PI/2. This is because the resulting batten length is theoretically infinite.
        """
    def GetHeight(self) -> float: 
        """
        Returns the thickness of the lathe.

        Returns the thickness of the lathe.
        """
    def GetP1(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the established location of the point P1.

        Returns the established location of the point P1.
        """
    def GetP2(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the established location of the point P2.

        Returns the established location of the point P2.
        """
    def GetSlidingFactor(self) -> float: 
        """
        Returns the initial sliding factor.

        Returns the initial sliding factor.
        """
    def GetSlope(self) -> float: 
        """
        Returns the established slope value.

        Returns the established slope value.
        """
    def SetAngle1(self,Angle1 : float) -> None: 
        """
        Allows you to change the angle Angle1 at the first point, P1. The default setting is 0.

        Allows you to change the angle Angle1 at the first point, P1. The default setting is 0.
        """
    def SetAngle2(self,Angle2 : float) -> None: 
        """
        Allows you to change the angle Angle2 at the second point, P2. The default setting is 0.

        Allows you to change the angle Angle2 at the second point, P2. The default setting is 0.
        """
    def SetConstraintOrder1(self,ConstraintOrder : int) -> None: 
        """
        Allows you to change the order of the constraint on the first point. ConstraintOrder has the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.

        Allows you to change the order of the constraint on the first point. ConstraintOrder has the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.
        """
    def SetConstraintOrder2(self,ConstraintOrder : int) -> None: 
        """
        Allows you to change the order of the constraint on the second point. ConstraintOrder is initialized with the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.

        Allows you to change the order of the constraint on the second point. ConstraintOrder is initialized with the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.
        """
    def SetFreeSliding(self,FreeSliding : bool) -> None: 
        """
        Freesliding is initialized with the default setting false. When Freesliding is set to true and, as a result, sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten.

        Freesliding is initialized with the default setting false. When Freesliding is set to true and, as a result, sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten.
        """
    def SetHeight(self,Height : float) -> None: 
        """
        Allows you to change the height of the deformation. Raises NegativeValue; -- if Height <= 0 if Height <= 0

        Allows you to change the height of the deformation. Raises NegativeValue; -- if Height <= 0 if Height <= 0
        """
    def SetP1(self,P1 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Allows you to change the location of the point, P1, and in doing so, modify the curve. Warning This method changes the angle as well as the point. Exceptions NullValue if the distance between P1 and P2 is less than or equal to the tolerance value for distance in Precision::Confusion: P1.IsEqual(P2, Precision::Confusion()). The function gp_Pnt2d::IsEqual tests to see if this is the case.
        """
    def SetP2(self,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Allows you to change the location of the point, P1, and in doing so, modify the curve. Warning This method changes the angle as well as the point. Exceptions NullValue if the distance between P1 and P2 is less than or equal to the tolerance value for distance in Precision::Confusion: P1.IsEqual(P2, Precision::Confusion()). The function gp_Pnt2d::IsEqual tests to see if this is the case.
        """
    def SetSlidingFactor(self,SlidingFactor : float) -> None: 
        """
        Allows you to change the ratio SlidingFactor. This compares the length of the batten and the reference length, which is, in turn, a function of the constraints. This modification has one of the following two effects: - if you increase the value, it inflates the batten - if you decrease the value, it flattens the batten. When sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten. When sliding is imposed, a value is required for the sliding factor. SlidingFactor is initialized with the default setting of 1.

        Allows you to change the ratio SlidingFactor. This compares the length of the batten and the reference length, which is, in turn, a function of the constraints. This modification has one of the following two effects: - if you increase the value, it inflates the batten - if you decrease the value, it flattens the batten. When sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten. When sliding is imposed, a value is required for the sliding factor. SlidingFactor is initialized with the default setting of 1.
        """
    def SetSlope(self,Slope : float) -> None: 
        """
        Allows you to set the slope value, Slope.

        Allows you to set the slope value, Slope.
        """
    def SlidingOfReference(self) -> float: 
        """
        Computes the real number value for length Sliding of Reference for new constraints. If you want to give a specific length to a batten curve, use the following syntax: b.SetSlidingFactor(L / b.SlidingOfReference()) where b is the name of the batten curve object.
        """
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Height : float,Slope : float=0.0) -> None: ...
    pass
class FairCurve_BattenLaw(OCP.math.math_Function):
    """
    This class compute the Heigth of an batten
    """
    def GetStateNumber(self) -> int: 
        """
        returns the state of the function corresponding to the latest call of any methods associated with the function. This function is called by each of the algorithms described later which defined the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def SetHeigth(self,Heigth : float) -> None: 
        """
        Change the value of Heigth at the middle point.

        Change the value of Heigth at the middle point.
        """
    def SetSliding(self,Sliding : float) -> None: 
        """
        Change the value of sliding

        Change the value of sliding
        """
    def SetSlope(self,Slope : float) -> None: 
        """
        Change the value of the geometric slope.

        Change the value of the geometric slope.
        """
    def Value(self,T : float,THeigth : float) -> bool: 
        """
        computes the value of the heigth for the parameter T on the neutral fibber

        computes the value of the heigth for the parameter T on the neutral fibber
        """
    def __init__(self,Heigth : float,Slope : float,Sliding : float) -> None: ...
    pass
class FairCurve_DistributionOfEnergy(OCP.math.math_FunctionSet):
    """
    Abstract class to use the Energy of an FairCurve
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def SetDerivativeOrder(self,DerivativeOrder : int) -> None: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        Computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    pass
class FairCurve_DistributionOfJerk(FairCurve_DistributionOfEnergy, OCP.math.math_FunctionSet):
    """
    Compute the "Jerk" distribution.
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def SetDerivativeOrder(self,DerivativeOrder : int) -> None: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,BSplOrder : int,FlatKnots : OCP.TColStd.TColStd_HArray1OfReal,Poles : OCP.TColgp.TColgp_HArray1OfPnt2d,DerivativeOrder : int,Law : FairCurve_BattenLaw,NbValAux : int=0) -> None: ...
    pass
class FairCurve_DistributionOfSagging(FairCurve_DistributionOfEnergy, OCP.math.math_FunctionSet):
    """
    Compute the Sagging Distribution
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def SetDerivativeOrder(self,DerivativeOrder : int) -> None: 
        """
        None
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,BSplOrder : int,FlatKnots : OCP.TColStd.TColStd_HArray1OfReal,Poles : OCP.TColgp.TColgp_HArray1OfPnt2d,DerivativeOrder : int,Law : FairCurve_BattenLaw,NbValAux : int=0) -> None: ...
    pass
class FairCurve_DistributionOfTension(FairCurve_DistributionOfEnergy, OCP.math.math_FunctionSet):
    """
    Compute the Tension Distribution
    """
    def GetStateNumber(self) -> int: 
        """
        Returns the state of the function corresponding to the latestcall of any methods associated with the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def NbEquations(self) -> int: 
        """
        returns the number of equations of the function.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the function.
        """
    def SetDerivativeOrder(self,DerivativeOrder : int) -> None: 
        """
        None
        """
    def SetLengthSliding(self,LengthSliding : float) -> None: 
        """
        change the length sliding

        change the length sliding
        """
    def Value(self,X : OCP.math.math_Vector,F : OCP.math.math_Vector) -> bool: 
        """
        computes the values <F> of the functions for the variable <X>. returns True if the computation was done successfully, False otherwise.
        """
    def __init__(self,BSplOrder : int,FlatKnots : OCP.TColStd.TColStd_HArray1OfReal,Poles : OCP.TColgp.TColgp_HArray1OfPnt2d,DerivativeOrder : int,LengthSliding : float,Law : FairCurve_BattenLaw,NbValAux : int=0,Uniform : bool=False) -> None: ...
    pass
class FairCurve_Energy(OCP.math.math_MultipleVarFunctionWithHessian, OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    necessary methodes to compute the energy of an FairCurve.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        computes the gradient <G> of the energys for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the energy.

        returns the number of variables of the energy.
        """
    def Poles(self) -> OCP.TColgp.TColgp_HArray1OfPnt2d: 
        """
        return the poles

        return the poles
        """
    def Value(self,X : OCP.math.math_Vector,E : float) -> bool: 
        """
        computes the values of the Energys E for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector,H : OCP.math.math_Matrix) -> bool: 
        """
        computes the Energy <E> and the gradient <G> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.

        computes the Energy <E>, the gradient <G> and the Hessian <H> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector) -> bool: ...
    def Variable(self,X : OCP.math.math_Vector) -> bool: 
        """
        compute the variables <X> wich correspond with the field <MyPoles>
        """
    pass
class FairCurve_EnergyOfBatten(FairCurve_Energy, OCP.math.math_MultipleVarFunctionWithHessian, OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    Energy Criterium to minimize in Batten.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        computes the gradient <G> of the energys for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def LengthSliding(self) -> float: 
        """
        return the lengthSliding = P1P2 + Sliding

        return the lengthSliding = P1P2 + Sliding
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the energy.

        returns the number of variables of the energy.
        """
    def Poles(self) -> OCP.TColgp.TColgp_HArray1OfPnt2d: 
        """
        return the poles

        return the poles
        """
    def Status(self) -> FairCurve_AnalysisCode: 
        """
        return the status

        return the status
        """
    def Value(self,X : OCP.math.math_Vector,E : float) -> bool: 
        """
        computes the values of the Energys E for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector,H : OCP.math.math_Matrix) -> bool: 
        """
        computes the Energy <E> and the gradient <G> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.

        computes the Energy <E>, the gradient <G> and the Hessian <H> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector) -> bool: ...
    def Variable(self,X : OCP.math.math_Vector) -> bool: 
        """
        compute the variables <X> wich correspond with the field <MyPoles>
        """
    def __init__(self,BSplOrder : int,FlatKnots : OCP.TColStd.TColStd_HArray1OfReal,Poles : OCP.TColgp.TColgp_HArray1OfPnt2d,ContrOrder1 : int,ContrOrder2 : int,Law : FairCurve_BattenLaw,LengthSliding : float,FreeSliding : bool=True,Angle1 : float=0.0,Angle2 : float=0.0) -> None: ...
    pass
class FairCurve_EnergyOfMVC(FairCurve_Energy, OCP.math.math_MultipleVarFunctionWithHessian, OCP.math.math_MultipleVarFunctionWithGradient, OCP.math.math_MultipleVarFunction):
    """
    Energy Criterium to minimize in MinimalVariationCurve.
    """
    def GetStateNumber(self) -> int: 
        """
        return the state of the function corresponding to the latestt call of any methods associated to the function. This function is called by each of the algorithms described later which define the function Integer Algorithm::StateNumber(). The algorithm has the responsibility to call this function when it has found a solution (i.e. a root or a minimum) and has to maintain the association between the solution found and this StateNumber. Byu default, this method returns 0 (which means for the algorithm: no state has been saved). It is the responsibility of the programmer to decide if he needs to save the current state of the function and to return an Integer that allows retrieval of the state.
        """
    def Gradient(self,X : OCP.math.math_Vector,G : OCP.math.math_Vector) -> bool: 
        """
        computes the gradient <G> of the energys for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    def LengthSliding(self) -> float: 
        """
        return the lengthSliding = P1P2 + Sliding

        return the lengthSliding = P1P2 + Sliding
        """
    def NbVariables(self) -> int: 
        """
        returns the number of variables of the energy.

        returns the number of variables of the energy.
        """
    def Poles(self) -> OCP.TColgp.TColgp_HArray1OfPnt2d: 
        """
        return the poles

        return the poles
        """
    def Status(self) -> FairCurve_AnalysisCode: 
        """
        return the status

        return the status
        """
    def Value(self,X : OCP.math.math_Vector,E : float) -> bool: 
        """
        computes the values of the Energys E for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector,H : OCP.math.math_Matrix) -> bool: 
        """
        computes the Energy <E> and the gradient <G> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.

        computes the Energy <E>, the gradient <G> and the Hessian <H> of the energy for the variable <X>. Returns True if the computation was done successfully, False otherwise.
        """
    @overload
    def Values(self,X : OCP.math.math_Vector,E : float,G : OCP.math.math_Vector) -> bool: ...
    def Variable(self,X : OCP.math.math_Vector) -> bool: 
        """
        compute the variables <X> wich correspond with the field <MyPoles>
        """
    def __init__(self,BSplOrder : int,FlatKnots : OCP.TColStd.TColStd_HArray1OfReal,Poles : OCP.TColgp.TColgp_HArray1OfPnt2d,ContrOrder1 : int,ContrOrder2 : int,Law : FairCurve_BattenLaw,PhysicalRatio : float,LengthSliding : float,FreeSliding : bool=True,Angle1 : float=0.0,Angle2 : float=0.0,Curvature1 : float=0.0,Curvature2 : float=0.0) -> None: ...
    pass
class FairCurve_MinimalVariation(FairCurve_Batten):
    """
    Computes a 2D curve using an algorithm which minimizes tension, sagging, and jerk energy. As in FairCurve_Batten, two reference points are used. Unlike that class, FairCurve_MinimalVariation requires curvature settings at the first and second reference points. These are defined by the rays of curvature desired at each point.
    """
    def Compute(self,ACode : FairCurve_AnalysisCode,NbIterations : int=50,Tolerance : float=0.001) -> bool: 
        """
        Computes the curve with respect to the constraints, NbIterations and Tolerance. The tolerance setting allows you to control the precision of computation, and the maximum number of iterations allows you to set a limit on computation time.
        """
    def Curve(self) -> OCP.Geom2d.Geom2d_BSplineCurve: 
        """
        Returns the computed curve a 2d BSpline.
        """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def GetAngle1(self) -> float: 
        """
        Returns the established first angle.

        Returns the established first angle.
        """
    def GetAngle2(self) -> float: 
        """
        Returns the established second angle.

        Returns the established second angle.
        """
    def GetConstraintOrder1(self) -> int: 
        """
        Returns the established first constraint order.

        Returns the established first constraint order.
        """
    def GetConstraintOrder2(self) -> int: 
        """
        Returns the established second constraint order.

        Returns the established second constraint order.
        """
    def GetCurvature1(self) -> float: 
        """
        Returns the first established curvature.

        Returns the first established curvature.
        """
    def GetCurvature2(self) -> float: 
        """
        Returns the second established curvature.

        Returns the second established curvature.
        """
    def GetFreeSliding(self) -> bool: 
        """
        Returns the initial free sliding value, false by default. Free sliding is generally more aesthetically pleasing than constrained sliding. However, the computation can fail with values such as angles greater than PI/2. This is because the resulting batten length is theoretically infinite.

        Returns the initial free sliding value, false by default. Free sliding is generally more aesthetically pleasing than constrained sliding. However, the computation can fail with values such as angles greater than PI/2. This is because the resulting batten length is theoretically infinite.
        """
    def GetHeight(self) -> float: 
        """
        Returns the thickness of the lathe.

        Returns the thickness of the lathe.
        """
    def GetP1(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the established location of the point P1.

        Returns the established location of the point P1.
        """
    def GetP2(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the established location of the point P2.

        Returns the established location of the point P2.
        """
    def GetPhysicalRatio(self) -> float: 
        """
        Returns the physical ratio, or kind of energy.

        Returns the physical ratio, or kind of energy.
        """
    def GetSlidingFactor(self) -> float: 
        """
        Returns the initial sliding factor.

        Returns the initial sliding factor.
        """
    def GetSlope(self) -> float: 
        """
        Returns the established slope value.

        Returns the established slope value.
        """
    def SetAngle1(self,Angle1 : float) -> None: 
        """
        Allows you to change the angle Angle1 at the first point, P1. The default setting is 0.

        Allows you to change the angle Angle1 at the first point, P1. The default setting is 0.
        """
    def SetAngle2(self,Angle2 : float) -> None: 
        """
        Allows you to change the angle Angle2 at the second point, P2. The default setting is 0.

        Allows you to change the angle Angle2 at the second point, P2. The default setting is 0.
        """
    def SetConstraintOrder1(self,ConstraintOrder : int) -> None: 
        """
        Allows you to change the order of the constraint on the first point. ConstraintOrder has the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.

        Allows you to change the order of the constraint on the first point. ConstraintOrder has the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.
        """
    def SetConstraintOrder2(self,ConstraintOrder : int) -> None: 
        """
        Allows you to change the order of the constraint on the second point. ConstraintOrder is initialized with the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.

        Allows you to change the order of the constraint on the second point. ConstraintOrder is initialized with the default setting of 1. The following settings are available: - 0-the curve must pass through a point - 1-the curve must pass through a point and have a given tangent - 2-the curve must pass through a point, have a given tangent and a given curvature. The third setting is only valid for FairCurve_MinimalVariation curves. These constraints, though geometric, represent the mechanical constraints due, for example, to the resistance of the material the actual physical batten is made of.
        """
    def SetCurvature1(self,Curvature : float) -> None: 
        """
        Allows you to set a new constraint on curvature at the first point.

        Allows you to set a new constraint on curvature at the first point.
        """
    def SetCurvature2(self,Curvature : float) -> None: 
        """
        Allows you to set a new constraint on curvature at the second point.

        Allows you to set a new constraint on curvature at the second point.
        """
    def SetFreeSliding(self,FreeSliding : bool) -> None: 
        """
        Freesliding is initialized with the default setting false. When Freesliding is set to true and, as a result, sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten.

        Freesliding is initialized with the default setting false. When Freesliding is set to true and, as a result, sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten.
        """
    def SetHeight(self,Height : float) -> None: 
        """
        Allows you to change the height of the deformation. Raises NegativeValue; -- if Height <= 0 if Height <= 0

        Allows you to change the height of the deformation. Raises NegativeValue; -- if Height <= 0 if Height <= 0
        """
    def SetP1(self,P1 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Allows you to change the location of the point, P1, and in doing so, modify the curve. Warning This method changes the angle as well as the point. Exceptions NullValue if the distance between P1 and P2 is less than or equal to the tolerance value for distance in Precision::Confusion: P1.IsEqual(P2, Precision::Confusion()). The function gp_Pnt2d::IsEqual tests to see if this is the case.
        """
    def SetP2(self,P2 : OCP.gp.gp_Pnt2d) -> None: 
        """
        Allows you to change the location of the point, P1, and in doing so, modify the curve. Warning This method changes the angle as well as the point. Exceptions NullValue if the distance between P1 and P2 is less than or equal to the tolerance value for distance in Precision::Confusion: P1.IsEqual(P2, Precision::Confusion()). The function gp_Pnt2d::IsEqual tests to see if this is the case.
        """
    def SetPhysicalRatio(self,Ratio : float) -> None: 
        """
        Allows you to set the physical ratio Ratio. The kinds of energy which you can specify include: 0 is only "Jerk" Energy 1 is only "Sagging" Energy like batten Warning: if Ratio is 1 it is impossible to impose curvature constraints. Raises DomainError if Ratio < 0 or Ratio > 1

        Allows you to set the physical ratio Ratio. The kinds of energy which you can specify include: 0 is only "Jerk" Energy 1 is only "Sagging" Energy like batten Warning: if Ratio is 1 it is impossible to impose curvature constraints. Raises DomainError if Ratio < 0 or Ratio > 1
        """
    def SetSlidingFactor(self,SlidingFactor : float) -> None: 
        """
        Allows you to change the ratio SlidingFactor. This compares the length of the batten and the reference length, which is, in turn, a function of the constraints. This modification has one of the following two effects: - if you increase the value, it inflates the batten - if you decrease the value, it flattens the batten. When sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten. When sliding is imposed, a value is required for the sliding factor. SlidingFactor is initialized with the default setting of 1.

        Allows you to change the ratio SlidingFactor. This compares the length of the batten and the reference length, which is, in turn, a function of the constraints. This modification has one of the following two effects: - if you increase the value, it inflates the batten - if you decrease the value, it flattens the batten. When sliding is free, the sliding factor is automatically computed to satisfy the equilibrium of the batten. When sliding is imposed, a value is required for the sliding factor. SlidingFactor is initialized with the default setting of 1.
        """
    def SetSlope(self,Slope : float) -> None: 
        """
        Allows you to set the slope value, Slope.

        Allows you to set the slope value, Slope.
        """
    def SlidingOfReference(self) -> float: 
        """
        Computes the real number value for length Sliding of Reference for new constraints. If you want to give a specific length to a batten curve, use the following syntax: b.SetSlidingFactor(L / b.SlidingOfReference()) where b is the name of the batten curve object.
        """
    def __init__(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Heigth : float,Slope : float=0.0,PhysicalRatio : float=0.0) -> None: ...
    pass
class FairCurve_Newton(OCP.math.math_NewtonMinimum):
    """
    Algorithme of Optimization used to make "FairCurve"
    """
    def Dump(self,o : io.BytesIO) -> None: 
        """
        Prints on the stream o information on the current state of the object. Is used to redefine the operator <<.
        """
    def GetStatus(self) -> OCP.math.math_Status: 
        """
        Returns the Status of computation. The exception NotDone is raised if an error has occured.

        Returns the Status of computation. The exception NotDone is raised if an error has occured.
        """
    @overload
    def Gradient(self,Grad : OCP.math.math_Vector) -> None: 
        """
        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        outputs the gradient vector at the minimum in Grad. Exception NotDone is raised if the minimum was not found. Exception DimensionError is raised if the range of Grad is not equal to the range of the StartingPoint.

        returns the gradient vector at the minimum. Exception NotDone is raised if an error has occured.the minimum was not found.

        returns the gradient vector at the minimum. Exception NotDone is raised if an error has occured.the minimum was not found.
        """
    @overload
    def Gradient(self) -> OCP.math.math_Vector: ...
    def IsConverged(self) -> bool: 
        """
        This method is called at the end of each iteration to check the convergence : || Xi+1 - Xi || < SpatialTolerance/100 Or || Xi+1 - Xi || < SpatialTolerance and |F(Xi+1) - F(Xi)| < CriteriumTolerance * |F(xi)| It can be redefined in a sub-class to implement a specific test.
        """
    def IsDone(self) -> bool: 
        """
        Tests if an error has occured.

        Tests if an error has occured.
        """
    @overload
    def Location(self,Loc : OCP.math.math_Vector) -> None: 
        """
        outputs the location vector of the minimum in Loc. Exception NotDone is raised if an error has occured. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        outputs the location vector of the minimum in Loc. Exception NotDone is raised if an error has occured. Exception DimensionError is raised if the range of Loc is not equal to the range of the StartingPoint.

        returns the location vector of the minimum. Exception NotDone is raised if an error has occured.

        returns the location vector of the minimum. Exception NotDone is raised if an error has occured.
        """
    @overload
    def Location(self) -> OCP.math.math_Vector: ...
    def Minimum(self) -> float: 
        """
        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.

        returns the value of the minimum. Exception NotDone is raised if the minimum was not found.
        """
    def NbIterations(self) -> int: 
        """
        returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if an error has occured.

        returns the number of iterations really done in the calculation of the minimum. The exception NotDone is raised if an error has occured.
        """
    def Perform(self,theFunction : OCP.math.math_MultipleVarFunctionWithHessian,theStartingPoint : OCP.math.math_Vector) -> None: 
        """
        Search the solution.
        """
    def SetBoundary(self,theLeftBorder : OCP.math.math_Vector,theRightBorder : OCP.math.math_Vector) -> None: 
        """
        Set boundaries.
        """
    def __init__(self,theFunction : OCP.math.math_MultipleVarFunctionWithHessian,theSpatialTolerance : float=1e-07,theCriteriumTolerance : float=1e-07,theNbIterations : int=40,theConvexity : float=1e-06,theWithSingularity : bool=True) -> None: ...
    pass
FairCurve_InfiniteSliding: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_InfiniteSliding: 2>
FairCurve_NotConverged: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_NotConverged: 1>
FairCurve_NullHeight: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_NullHeight: 3>
FairCurve_OK: OCP.FairCurve.FairCurve_AnalysisCode # value = <FairCurve_AnalysisCode.FairCurve_OK: 0>
