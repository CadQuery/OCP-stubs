import OCP.DE
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Resource
import OCP.TopoDS
import OCP.TDocStd
import OCP.TCollection
import OCP.NCollection
import OCP.Standard
import OCP.XSControl
import OCP.TColStd
__all__  = [
"DE_ConfigurationContext",
"DE_ConfigurationNode",
"DE_Provider",
"DE_Wrapper"
]
class DE_ConfigurationContext(OCP.Standard.Standard_Transient):
    """
    Provides convenient interface to resource file Allows loading of the resource file and getting attributes' values starting from some scope, for example if scope is defined as "ToV4" and requested parameter is "exec.op", value of "ToV4.exec.op" parameter from the resource file will be returned
    """
    def BooleanVal(self,theParam : OCP.TCollection.TCollection_AsciiString,theDefValue : bool,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
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
    def GetBoolean(self,theParam : OCP.TCollection.TCollection_AsciiString,theValue : bool,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
        """
    def GetInteger(self,theParam : OCP.TCollection.TCollection_AsciiString,theValue : int,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
        """
    def GetInternalMap(self) -> OCP.Resource.Resource_DataMapOfAsciiStringAsciiString: 
        """
        Gets internal resource map
        """
    def GetReal(self,theParam : OCP.TCollection.TCollection_AsciiString,theValue : float,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetString(self,theParam : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TCollection.TCollection_AsciiString,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
        """
    def GetStringSeq(self,theParam : OCP.TCollection.TCollection_AsciiString,theValue : OCP.TColStd.TColStd_ListOfAsciiString,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Gets value of parameter as being of specific type
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IntegerVal(self,theParam : OCP.TCollection.TCollection_AsciiString,theDefValue : int,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Gets value of parameter as being of specific type
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
    def IsParamSet(self,theParam : OCP.TCollection.TCollection_AsciiString,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Checks for existing the parameter name
        """
    def Load(self,theConfiguration : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Import the custom configuration Save all parameters with their values.
        """
    def LoadFile(self,theFile : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Import the resource file. Save all parameters with their values.
        """
    def LoadStr(self,theResource : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Import the resource string. Save all parameters with their values.
        """
    def RealVal(self,theParam : OCP.TCollection.TCollection_AsciiString,theDefValue : float,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> float: 
        """
        Gets value of parameter as being of specific type
        """
    def StringVal(self,theParam : OCP.TCollection.TCollection_AsciiString,theDefValue : OCP.TCollection.TCollection_AsciiString,theScope : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Gets value of parameter as being of specific type
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
class DE_ConfigurationNode(OCP.Standard.Standard_Transient):
    """
    Base class to work with CAD transfer properties. Stores the necessary settings for a single Provider type. Configures and creates special provider to transfer CAD files.
    """
    def BuildProvider(self) -> DE_Provider: 
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
    def Copy(self) -> DE_ConfigurationNode: 
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
    @overload
    def Load(self,theResourcePath : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Updates values according the resource file

        Updates values according the resource
        """
    @overload
    def Load(self,theResource : DE_ConfigurationContext) -> bool: ...
    @overload
    def Save(self,theResourcePath : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Writes configuration to the resource file

        Writes configuration to the string
        """
    @overload
    def Save(self) -> OCP.TCollection.TCollection_AsciiString: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theConfigurationNode : DE_ConfigurationNode) -> None: ...
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
class DE_Provider(OCP.Standard.Standard_Transient):
    """
    Base class to make transfer process. Reads or Writes specialized CAD files into/from OCCT. Each operation needs the Configuration Node.
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
    def GetNode(self) -> DE_ConfigurationNode: 
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
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration
        """
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def SetNode(self,theNode : DE_ConfigurationNode) -> None: 
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
    def __init__(self,theNode : DE_ConfigurationNode) -> None: ...
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
class DE_Wrapper(OCP.Standard.Standard_Transient):
    """
    The main class for working with CAD file exchange. Loads and Saves special CAD transfer property. Consolidates all supported Formats and Vendors. Automatically recognizes CAD format and uses the preferred existed Vendor. Note: If Vendor's format is not binded, the configuration loading doesn't affect on its property.
    """
    def Bind(self,theNode : DE_ConfigurationNode) -> bool: 
        """
        Creates new node copy and adds to the map
        """
    @overload
    def ChangePriority(self,theVendorPriority : OCP.TColStd.TColStd_ListOfAsciiString,theToDisable : bool=False) -> None: 
        """
        Changes provider priority to one format if it exists

        Changes provider priority to all loaded nodes
        """
    @overload
    def ChangePriority(self,theFormat : OCP.TCollection.TCollection_AsciiString,theVendorPriority : OCP.TColStd.TColStd_ListOfAsciiString,theToDisable : bool=False) -> None: ...
    def Copy(self) -> DE_Wrapper: 
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
    def Find(self,theFormat : OCP.TCollection.TCollection_AsciiString,theVendor : OCP.TCollection.TCollection_AsciiString,theNode : DE_ConfigurationNode) -> bool: 
        """
        Finds a node associated with input format and vendor
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def GlobalWrapper_s() -> DE_Wrapper: 
        """
        Gets global configuration singleton
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
    def Load(self,theResource : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theIsRecursive : bool=True) -> bool: 
        """
        Updates values according the resource file

        Updates values according the resource
        """
    @overload
    def Load(self,theResource : DE_ConfigurationContext,theIsRecursive : bool=True) -> bool: ...
    def Nodes(self) -> Any: 
        """
        Gets format map, contains vendor map with nodes
        """
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration

        Reads a CAD file, according internal configuration
        """
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Read(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Save(self,theResourcePath : OCP.TCollection.TCollection_AsciiString,theIsRecursive : bool=True,theFormats : OCP.TColStd.TColStd_ListOfAsciiString=OCP.TColStd.TColStd_ListOfAsciiString,theVendors : OCP.TColStd.TColStd_ListOfAsciiString=OCP.TColStd.TColStd_ListOfAsciiString) -> bool: 
        """
        Writes configuration to the resource file

        Writes configuration to the string
        """
    @overload
    def Save(self,theIsRecursive : bool=True,theFormats : OCP.TColStd.TColStd_ListOfAsciiString=OCP.TColStd.TColStd_ListOfAsciiString,theVendors : OCP.TColStd.TColStd_ListOfAsciiString=OCP.TColStd.TColStd_ListOfAsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration

        Writes a CAD file, according internal configuration
        """
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theDocument : OCP.TDocStd.TDocStd_Document,theWS : OCP.XSControl.XSControl_WorkSession,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def Write(self,thePath : OCP.TCollection.TCollection_AsciiString,theShape : OCP.TopoDS.TopoDS_Shape,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @overload
    def __init__(self,theWrapper : DE_Wrapper) -> None: ...
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
