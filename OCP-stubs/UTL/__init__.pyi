import OCP.UTL
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.OSD
import OCP.Storage
import OCP.Standard
import OCP.TCollection
import OCP.Resource
__all__  = [
"UTL"
]
class UTL():
    """
    None
    """
    @staticmethod
    def AddToUserInfo_s(aData : OCP.Storage.Storage_Data,anInfo : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    @staticmethod
    def CString_s(anExtendedString : OCP.TCollection.TCollection_ExtendedString) -> str: 
        """
        None
        """
    @staticmethod
    def Disk_s(aPath : OCP.OSD.OSD_Path) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    @staticmethod
    def ExtendedString_s(anAsciiString : OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    @staticmethod
    @overload
    def Extension_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Extension_s(aPath : OCP.OSD.OSD_Path) -> OCP.TCollection.TCollection_ExtendedString: ...
    @staticmethod
    def FileIterator_s(aPath : OCP.OSD.OSD_Path,aMask : OCP.TCollection.TCollection_ExtendedString) -> OCP.OSD.OSD_FileIterator: 
        """
        None
        """
    @staticmethod
    def Find_s(aResourceManager : OCP.Resource.Resource_Manager,aResourceName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    @staticmethod
    def GUID_s(anXString : OCP.TCollection.TCollection_ExtendedString) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def IntegerValue_s(anExtendedString : OCP.TCollection.TCollection_ExtendedString) -> int: 
        """
        None
        """
    @staticmethod
    def IsReadOnly_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> bool: 
        """
        None
        """
    @staticmethod
    def LocalHost_s() -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    @staticmethod
    def Name_s(aPath : OCP.OSD.OSD_Path) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    @staticmethod
    def OpenFile_s(aFile : OCP.Storage.Storage_BaseDriver,aName : OCP.TCollection.TCollection_ExtendedString,aMode : OCP.Storage.Storage_OpenMode) -> OCP.Storage.Storage_Error: 
        """
        None
        """
    @staticmethod
    def Path_s(aFileName : OCP.TCollection.TCollection_ExtendedString) -> OCP.OSD.OSD_Path: 
        """
        None
        """
    @staticmethod
    def Trek_s(aPath : OCP.OSD.OSD_Path) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    @staticmethod
    def Value_s(aResourceManager : OCP.Resource.Resource_Manager,aResourceName : OCP.TCollection.TCollection_ExtendedString) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def __init__(self) -> None: ...
    @staticmethod
    def xgetenv_s(aCString : str) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    pass
