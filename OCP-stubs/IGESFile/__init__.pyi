import OCP.IGESFile
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IGESData
__all__  = [
"IGESFile_Read",
"IGESFile_ReadFNES"
]
@overload
def IGESFile_Read(nomfic : str,amodel : OCP.IGESData.IGESData_IGESModel,protocol : OCP.IGESData.IGESData_Protocol) -> int:
    """
    None

    None
    """
@overload
def IGESFile_Read(nomfic : str,amodel : OCP.IGESData.IGESData_IGESModel,protocol : OCP.IGESData.IGESData_Protocol,reco : OCP.IGESData.IGESData_FileRecognizer,modefnes : bool=False) -> int:
    pass
def IGESFile_ReadFNES(nomfic : str,amodel : OCP.IGESData.IGESData_IGESModel,protocol : OCP.IGESData.IGESData_Protocol) -> int:
    """
    None
    """
