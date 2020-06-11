import OCP.RWStl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.OSD
import OCP.Standard
import OCP.gp
import OCP.Poly
import OCP.Message
__all__  = [
"RWStl",
"RWStl_Reader"
]
class RWStl():
    """
    This class provides methods to read and write triangulation from / to the STL files.
    """
    @staticmethod
    def ReadAscii_s(thePath : OCP.OSD.OSD_Path,theProgInd : OCP.Message.Message_ProgressIndicator=None) -> OCP.Poly.Poly_Triangulation: 
        """
        Read triangulation from an Ascii STL file In case of error, returns Null handle.
        """
    @staticmethod
    def ReadBinary_s(thePath : OCP.OSD.OSD_Path,theProgInd : OCP.Message.Message_ProgressIndicator=None) -> OCP.Poly.Poly_Triangulation: 
        """
        Read triangulation from a binary STL file In case of error, returns Null handle.
        """
    @staticmethod
    @overload
    def ReadFile_s(theFile : str,aProgInd : OCP.Message.Message_ProgressIndicator=None) -> OCP.Poly.Poly_Triangulation: 
        """
        Read specified STL file and returns its content as triangulation. In case of error, returns Null handle.

        Read specified STL file and returns its content as triangulation. In case of error, returns Null handle.
        """
    @staticmethod
    @overload
    def ReadFile_s(theFile : OCP.OSD.OSD_Path,aProgInd : OCP.Message.Message_ProgressIndicator=None) -> OCP.Poly.Poly_Triangulation: ...
    @staticmethod
    def WriteAscii_s(theMesh : OCP.Poly.Poly_Triangulation,thePath : OCP.OSD.OSD_Path,theProgInd : OCP.Message.Message_ProgressIndicator=None) -> bool: 
        """
        write the meshing in a file following the Ascii format of an STL file. Returns false if the cannot be opened;
        """
    @staticmethod
    def WriteBinary_s(theMesh : OCP.Poly.Poly_Triangulation,thePath : OCP.OSD.OSD_Path,theProgInd : OCP.Message.Message_ProgressIndicator=None) -> bool: 
        """
        Write triangulation to binary STL file. binary format of an STL file. Returns false if the cannot be opened;
        """
    def __init__(self) -> None: ...
    pass
class RWStl_Reader(OCP.Standard.Standard_Transient):
    """
    An abstract class implementing procedure to read STL file.
    """
    def AddNode(self,thePnt : OCP.gp.gp_XYZ) -> int: 
        """
        Callback function to be implemented in descendant. Should create new node with specified coordinates in the target model, and return its ID as integer.
        """
    def AddTriangle(self,theN1 : int,theN2 : int,theN3 : int) -> None: 
        """
        Callback function to be implemented in descendant. Should create new triangle built on specified nodes in the target model.
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
    def IsAscii(self,theStream : Any) -> bool: 
        """
        Guess whether the stream is an Ascii STL file, by analysis of the first bytes (~200). The function attempts to put back the read symbols to the stream which thus must support ungetc(). Returns true if the stream seems to contain Ascii STL.
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
    def Read(self,theFile : str,theProgress : OCP.Message.Message_ProgressIndicator) -> bool: 
        """
        Reads data from STL file (either binary or Ascii). This function supports reading multi-domain STL files formed by concatenation of several "plain" files. The mesh nodes are not merged between domains. Unicode paths can be given in UTF-8 encoding. Format is recognized automatically by analysis of the file header. Returns true if success, false on error or user break.
        """
    def ReadBinary(self,theStream : Any,theProgress : OCP.Message.Message_ProgressIndicator) -> bool: 
        """
        Reads STL data from binary stream. The stream must be opened in binary mode. Stops after reading the number of triangles recorded in the file header. Returns true if success, false on error or user break.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
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
