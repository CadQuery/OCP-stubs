import OCP.StlAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopoDS
__all__  = [
"StlAPI",
"StlAPI_Reader",
"StlAPI_Writer"
]
class StlAPI():
    """
    Offers the API for STL data manipulation.
    """
    @staticmethod
    def Read_s(theShape : OCP.TopoDS.TopoDS_Shape,aFile : str) -> bool: 
        """
        None
        """
    @staticmethod
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theAsciiMode : bool=True) -> bool: 
        """
        Convert and write shape to STL format. File is written in binary if aAsciiMode is False otherwise it is written in Ascii (by default).
        """
    def __init__(self) -> None: ...
    pass
class StlAPI_Reader():
    """
    Reading from stereolithography format.
    """
    def Read(self,theShape : OCP.TopoDS.TopoDS_Shape,theFileName : str) -> bool: 
        """
        Reads STL file to the TopoDS_Shape (each triangle is converted to the face).
        """
    def __init__(self) -> None: ...
    pass
class StlAPI_Writer():
    """
    This class creates and writes STL files from Open CASCADE shapes. An STL file can be written to an existing STL file or to a new one.
    """
    def Write(self,theShape : OCP.TopoDS.TopoDS_Shape,theFileName : str) -> bool: 
        """
        Converts a given shape to STL format and writes it to file with a given filename.
        """
    def __init__(self) -> None: ...
    @property
    def ASCIIMode(self) -> bool:
        """
        Returns the address to the flag defining the mode for writing the file. This address may be used to either read or change the flag. If the mode returns True (default value) the generated file is an ASCII file. If the mode returns False, the generated file is a binary file.

        :type: bool
        """
    @ASCIIMode.setter
    def ASCIIMode(self, arg1: bool) -> None:
        """
        Returns the address to the flag defining the mode for writing the file. This address may be used to either read or change the flag. If the mode returns True (default value) the generated file is an ASCII file. If the mode returns False, the generated file is a binary file.
        """
    pass
