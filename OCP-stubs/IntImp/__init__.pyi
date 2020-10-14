import OCP.IntImp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"IntImp_ConstIsoparametric",
"ChoixRef",
"IntImp_ComputeTangence",
"IntImp_UIsoparametricOnCaro1",
"IntImp_UIsoparametricOnCaro2",
"IntImp_VIsoparametricOnCaro1",
"IntImp_VIsoparametricOnCaro2"
]
class IntImp_ConstIsoparametric():
    """
    None

    Members:

      IntImp_UIsoparametricOnCaro1

      IntImp_VIsoparametricOnCaro1

      IntImp_UIsoparametricOnCaro2

      IntImp_VIsoparametricOnCaro2
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
    IntImp_UIsoparametricOnCaro1: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro1
    IntImp_UIsoparametricOnCaro2: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro2
    IntImp_VIsoparametricOnCaro1: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro1
    IntImp_VIsoparametricOnCaro2: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro2
    __entries: dict # value = {'IntImp_UIsoparametricOnCaro1': (IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro1, None), 'IntImp_VIsoparametricOnCaro1': (IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro1, None), 'IntImp_UIsoparametricOnCaro2': (IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro2, None), 'IntImp_VIsoparametricOnCaro2': (IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro2, None)}
    __members__: dict # value = {'IntImp_UIsoparametricOnCaro1': IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro1, 'IntImp_VIsoparametricOnCaro1': IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro1, 'IntImp_UIsoparametricOnCaro2': IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro2, 'IntImp_VIsoparametricOnCaro2': IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro2}
    pass
def ChoixRef(theIndex : int) -> IntImp_ConstIsoparametric:
    """
    None
    """
def IntImp_ComputeTangence(DPuv : OCP.gp.gp_Vec,EpsUV : float,Tgduv : float,TabIso : IntImp_ConstIsoparametric) -> bool:
    """
    None
    """
IntImp_UIsoparametricOnCaro1: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro1
IntImp_UIsoparametricOnCaro2: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_UIsoparametricOnCaro2
IntImp_VIsoparametricOnCaro1: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro1
IntImp_VIsoparametricOnCaro2: OCP.IntImp.IntImp_ConstIsoparametric # value = IntImp_ConstIsoparametric.IntImp_VIsoparametricOnCaro2
