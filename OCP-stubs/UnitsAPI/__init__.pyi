import OCP.UnitsAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Units
__all__  = [
"UnitsAPI",
"UnitsAPI_SystemUnits",
"UnitsAPI_DEFAULT",
"UnitsAPI_MDTV",
"UnitsAPI_SI"
]
class UnitsAPI():
    """
    The UnitsAPI global functions are used to convert a value from any unit into another unit. Principles Conversion is executed among three unit systems: - the SI System - the user's Local System - the user's Current System. The SI System is the standard international unit system. It is indicated by SI in the synopses of the UnitsAPI functions. The MDTV System corresponds to the SI international standard but the length unit and all its derivatives use millimeters instead of the meters. Both systems are proposed by Open CASCADE; the SI System is the standard option. By selecting one of these two systems, the user defines his Local System through the SetLocalSystem function. The Local System is indicated by LS in the synopses of the UnitsAPI functions. The user's Local System units can be modified in the working environment. The user defines his Current System by modifying its units through the SetCurrentUnit function. The Current System is indicated by Current in the synopses of the UnitsAPI functions.
    """
    @staticmethod
    def AnyFromLS_s(aData : float,aUnit : str) -> float: 
        """
        Converts the local system units value to the local unit value. Example: AnyFromLS(25.4,"in.") returns 1. if the LocalSystem is MDTV. Note: aUnit is also used to identify the type of physical quantity to convert.
        """
    @staticmethod
    def AnyFromSI_s(aData : float,aUnit : str) -> float: 
        """
        Converts the SI system units value to the local unit value. Example: AnyFromSI(0.0254,"in.") returns 0.001 Note: aUnit is also used to identify the type of physical quantity to convert.
        """
    @staticmethod
    def AnyToAny_s(aData : float,aUnit1 : str,aUnit2 : str) -> float: 
        """
        Converts the local unit value to another local unit value. Example: AnyToAny(0.0254,"in.","millimeter") returns 1. ;
        """
    @staticmethod
    @overload
    def AnyToLS_s(aData : float,aUnit : str,aDim : OCP.Units.Units_Dimensions) -> float: 
        """
        Converts the local unit value to the local system units value. Example: AnyToLS(1.,"in.") returns 25.4 if the LocalSystem is MDTV.

        Converts the local unit value to the local system units value. and gives the associated dimension of the unit
        """
    @staticmethod
    @overload
    def AnyToLS_s(aData : float,aUnit : str) -> float: ...
    @staticmethod
    @overload
    def AnyToSI_s(aData : float,aUnit : str) -> float: 
        """
        Converts the local unit value to the SI system units value. Example: AnyToSI(1.,"in.") returns 0.0254

        Converts the local unit value to the SI system units value. and gives the associated dimension of the unit
        """
    @staticmethod
    @overload
    def AnyToSI_s(aData : float,aUnit : str,aDim : OCP.Units.Units_Dimensions) -> float: ...
    @staticmethod
    def Check_s(aQuantity : str,aUnit : str) -> bool: 
        """
        Checks the coherence between the quantity <aQuantity> and the unit <aUnits> in the current system and returns FALSE when it's WRONG.
        """
    @staticmethod
    def CurrentFromAny_s(aData : float,aQuantity : str,aUnit : str) -> float: 
        """
        Converts the aData value expressed in the unit aUnit, into the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function.
        """
    @staticmethod
    def CurrentFromLS_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the local system units value to the current unit value. Example: CurrentFromLS(1000.,"LENGTH") returns 1. if current length unit is meter and LocalSystem is MDTV.
        """
    @staticmethod
    def CurrentFromSI_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the SI system units value to the current unit value. Example: CurrentFromSI(0.001,"LENGTH") returns 1 if current length unit is millimeter.
        """
    @staticmethod
    def CurrentToAny_s(aData : float,aQuantity : str,aUnit : str) -> float: 
        """
        Converts the aData value expressed in the current unit for the working environment, as defined for the physical quantity aQuantity by the last call to the SetCurrentUnit function, into the unit aUnit.
        """
    @staticmethod
    def CurrentToLS_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the current unit value to the local system units value. Example: CurrentToLS(1.,"LENGTH") returns 1000. if the current length unit is meter and LocalSystem is MDTV.
        """
    @staticmethod
    def CurrentToSI_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the current unit value to the SI system units value. Example: CurrentToSI(1.,"LENGTH") returns 0.001 if current length unit is millimeter.
        """
    @staticmethod
    def CurrentUnit_s(aQuantity : str) -> str: 
        """
        Returns the current unit dimension <aUnit> from the unit quantity <aQuantity>.
        """
    @staticmethod
    def DimensionAmountOfSubstance_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionElectricCurrent_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionLength_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionLess_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionLuminousIntensity_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionMass_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionPlaneAngle_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionSolidAngle_s() -> OCP.Units.Units_Dimensions: 
        """
        Returns the basic dimensions.
        """
    @staticmethod
    def DimensionThermodynamicTemperature_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def DimensionTime_s() -> OCP.Units.Units_Dimensions: 
        """
        None
        """
    @staticmethod
    def Dimensions_s(aQuantity : str) -> OCP.Units.Units_Dimensions: 
        """
        return the dimension associated to the quantity
        """
    @staticmethod
    def LSToSI_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the local system units value to the SI system unit value. Example: LSToSI(1.,"LENGTH") returns 0.001 if the local system length unit is millimeter.
        """
    @staticmethod
    def LocalSystem_s() -> UnitsAPI_SystemUnits: 
        """
        Returns the current local system units.
        """
    @staticmethod
    def Reload_s() -> None: 
        """
        None
        """
    @staticmethod
    def SIToLS_s(aData : float,aQuantity : str) -> float: 
        """
        Converts the SI system unit value to the local system units value. Example: SIToLS(1.,"LENGTH") returns 1000. if the local system length unit is millimeter.
        """
    @staticmethod
    def Save_s() -> None: 
        """
        saves the units in the file .CurrentUnits of the directory pointed by the CSF_CurrentUnitsUserDefaults environment variable.
        """
    @staticmethod
    def SetCurrentUnit_s(aQuantity : str,aUnit : str) -> None: 
        """
        Sets the current unit dimension <aUnit> to the unit quantity <aQuantity>. Example: SetCurrentUnit("LENGTH","millimeter")
        """
    @staticmethod
    def SetLocalSystem_s(aSystemUnit : UnitsAPI_SystemUnits=UnitsAPI_SystemUnits.UnitsAPI_SI) -> None: 
        """
        Sets the local system units. Example: SetLocalSystem(UnitsAPI_MDTV)
        """
    def __init__(self) -> None: ...
    pass
class UnitsAPI_SystemUnits():
    """
    Identifies unit systems which may be defined as a basis system in the user's session: - UnitsAPI_DEFAULT : default system (this is the SI system) - UnitsAPI_SI : the SI unit system - UnitsAPI_MDTV : the MDTV unit system; it is equivalent to the SI unit system but the length unit and all its derivatives use millimeters instead of meters. Use the function SetLocalSystem to set up one of these unit systems as working environment.

    Members:

      UnitsAPI_DEFAULT

      UnitsAPI_SI

      UnitsAPI_MDTV
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
    UnitsAPI_DEFAULT: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_DEFAULT: 0>
    UnitsAPI_MDTV: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_MDTV: 2>
    UnitsAPI_SI: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_SI: 1>
    __entries: dict # value = {'UnitsAPI_DEFAULT': (<UnitsAPI_SystemUnits.UnitsAPI_DEFAULT: 0>, None), 'UnitsAPI_SI': (<UnitsAPI_SystemUnits.UnitsAPI_SI: 1>, None), 'UnitsAPI_MDTV': (<UnitsAPI_SystemUnits.UnitsAPI_MDTV: 2>, None)}
    __members__: dict # value = {'UnitsAPI_DEFAULT': <UnitsAPI_SystemUnits.UnitsAPI_DEFAULT: 0>, 'UnitsAPI_SI': <UnitsAPI_SystemUnits.UnitsAPI_SI: 1>, 'UnitsAPI_MDTV': <UnitsAPI_SystemUnits.UnitsAPI_MDTV: 2>}
    pass
UnitsAPI_DEFAULT: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_DEFAULT: 0>
UnitsAPI_MDTV: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_MDTV: 2>
UnitsAPI_SI: OCP.UnitsAPI.UnitsAPI_SystemUnits # value = <UnitsAPI_SystemUnits.UnitsAPI_SI: 1>
