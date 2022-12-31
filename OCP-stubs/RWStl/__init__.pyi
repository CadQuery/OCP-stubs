import OCP.RWStl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopoDS
import OCP.TDocStd
import OCP.TCollection
import OCP.NCollection
import OCP.Poly
import OCP.OSD
import OCP.gp
import OCP.Message
import OCP.DE
import OCP.Standard
import OCP.XSControl
import OCP.TColStd
import io
__all__  = [
"RWStl",
"RWStl_ConfigurationNode",
"RWStl_Provider",
"RWStl_Reader"
]
class RWStl():
    """
    This class provides methods to read and write triangulation from / to the STL files.
    """
    @staticmethod
    def ReadAscii_s(thePath : OCP.OSD.OSD_Path,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Poly.Poly_Triangulation: 
        """
        Read triangulation from an Ascii STL file In case of error, returns Null handle.
        """
    @staticmethod
    def ReadBinary_s(thePath : OCP.OSD.OSD_Path,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Poly.Poly_Triangulation: 
        """
        Read triangulation from a binary STL file In case of error, returns Null handle.
        """
    @staticmethod
    @overload
    def ReadFile_s(theFile : str,theMergeAngle : float,theTriangList : Any,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Read specified STL file and returns its content as triangulation. In case of error, returns Null handle.

        Read specified STL file and returns its content as triangulation. In case of error, returns Null handle.

        Read specified STL file and returns its content as triangulation.

        Read specified STL file and fills triangulation list for multi-domain case.
        """
    @staticmethod
    @overload
    def ReadFile_s(theFile : str,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Poly.Poly_Triangulation: ...
    @staticmethod
    @overload
    def ReadFile_s(theFile : OCP.OSD.OSD_Path,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Poly.Poly_Triangulation: ...
    @staticmethod
    @overload
    def ReadFile_s(theFile : str,theMergeAngle : float,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> OCP.Poly.Poly_Triangulation: ...
    @staticmethod
    def WriteAscii_s(theMesh : OCP.Poly.Poly_Triangulation,thePath : OCP.OSD.OSD_Path,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        write the meshing in a file following the Ascii format of an STL file. Returns false if the cannot be opened;
        """
    @staticmethod
    def WriteBinary_s(theMesh : OCP.Poly.Poly_Triangulation,thePath : OCP.OSD.OSD_Path,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Write triangulation to binary STL file. binary format of an STL file. Returns false if the cannot be opened;
        """
    def __init__(self) -> None: ...
    pass
class RWStl_ConfigurationNode(OCP.DE.DE_ConfigurationNode, OCP.Standard.Standard_Transient):
    """
    The purpose of this class is to configure the transfer process for STL format Stores the necessary settings for RWStl_Provider. Configures and creates special provider to transfer STL files.
    """
    def BuildProvider(self) -> OCP.DE.DE_Provider: 
        """
        Creates new provider for the own format
        """
    def CheckContent(self,theBuffer : OCP.NCollection.NCollection_Buffer) -> bool: 
        """
        Checks the file content to verify a format
        """
    def CheckExtension(self,theExtension : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Checks the file extension to verify a format
        """
    def Copy(self) -> OCP.DE.DE_ConfigurationNode: 
        """
        Copies values of all fields
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
    def GetExtensions(self) -> OCP.TColStd.TColStd_ListOfAsciiString: 
        """
        Gets list of supported file extensions
        """
    def GetFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets CAD format name of associated provider
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVendor(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets provider's vendor name of associated provider
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEnabled(self) -> bool: 
        """
        Gets the provider loading status
        """
    def IsExportSupported(self) -> bool: 
        """
        Checks the export supporting
        """
    def IsImportSupported(self) -> bool: 
        """
        Checks the import supporting
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
    def Load(self,theResource : OCP.DE.DE_ConfigurationContext) -> bool: 
        """
        Updates values according the resource
        """
    def Save(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Writes configuration to the string
        """
    def SetEnabled(self,theIsLoaded : bool) -> None: 
        """
        Sets the provider loading status
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateLoad(self) -> bool: 
        """
        Update loading status. Checking for the license.
        """
    @overload
    def __init__(self,theNode : RWStl_ConfigurationNode) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class RWStl_Provider(OCP.DE.DE_Provider, OCP.Standard.Standard_Transient):
    """
    The class to transfer STL files. Reads and Writes any STL files into/from OCCT. Each operation needs configuration node.
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
    def GetFormat(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets CAD format name of associated provider
        """
    def GetNode(self) -> OCP.DE.DE_ConfigurationNode: 
        """
        Gets internal configuration node
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetVendor(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets provider's vendor name of associated provider
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
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration
        """
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def SetNode(self,theNode : OCP.DE.DE_ConfigurationNode) -> None: 
        """
        Sets internal configuration node
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def __init__(self,theNode : OCP.DE.DE_ConfigurationNode) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class RWStl_Reader(OCP.Standard.Standard_Transient):
    """
    An abstract class implementing procedure to read STL file.
    """
    def AddNode(self,thePnt : OCP.gp.gp_XYZ) -> int: 
        """
        Callback function to be implemented in descendant. Should create new node with specified coordinates in the target model, and return its ID as integer.
        """
    def AddSolid(self) -> None: 
        """
        Callback function to be implemented in descendant. Should create a new triangulation for a solid in multi-domain case.
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
    def IsAscii(self,theStream : io.BytesIO,isSeekgAvailable : bool) -> bool: 
        """
        Guess whether the stream is an Ascii STL file, by analysis of the first bytes (~200). If the stream does not support seekg() then the parameter isSeekgAvailable should be passed as 'false', in this case the function attempts to put back the read symbols to the stream which thus must support ungetc(). Returns true if the stream seems to contain Ascii STL.
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
    def MergeAngle(self) -> float: 
        """
        Return merge tolerance; M_PI/2 by default - all nodes are merged regardless angle between triangles.
        """
    def MergeTolerance(self) -> float: 
        """
        Return linear merge tolerance; 0.0 by default (only 3D points with exactly matching coordinates are merged).
        """
    def Read(self,theFile : str,theProgress : OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads data from STL file (either binary or Ascii). This function supports reading multi-domain STL files formed by concatenation of several "plain" files. The mesh nodes are not merged between domains. Unicode paths can be given in UTF-8 encoding. Format is recognized automatically by analysis of the file header. Returns true if success, false on error or user break.
        """
    def ReadBinary(self,theStream : io.BytesIO,theProgress : OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads STL data from binary stream. The stream must be opened in binary mode. Stops after reading the number of triangles recorded in the file header. Returns true if success, false on error or user break.
        """
    def SetMergeAngle(self,theAngleRad : float) -> None: 
        """
        Set merge angle in radians. Specify something like M_PI/4 (45 degrees) to avoid merge nodes between triangles at sharp corners.
        """
    def SetMergeTolerance(self,theTolerance : float) -> None: 
        """
        Set linear merge tolerance.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self) -> None: ...
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
