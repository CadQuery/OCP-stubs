import OCP.GeomTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Message
import OCP.Geom2d
import OCP.Standard
import OCP.Geom
__all__  = [
"GeomTools",
"GeomTools_Curve2dSet",
"GeomTools_CurveSet",
"GeomTools_SurfaceSet",
"GeomTools_UndefinedTypeHandler"
]
class GeomTools():
    """
    The GeomTools package provides utilities for Geometry.
    """
    @staticmethod
    @overload
    def Dump_s(S : OCP.Geom.Geom_Surface,OS : Any) -> None: 
        """
        A set of Curves from Geom2d. Dumps the surface on the stream.

        Dumps the Curve on the stream.

        Dumps the Curve on the stream.
        """
    @staticmethod
    @overload
    def Dump_s(C : OCP.Geom.Geom_Curve,OS : Any) -> None: ...
    @staticmethod
    @overload
    def Dump_s(C : OCP.Geom2d.Geom2d_Curve,OS : Any) -> None: ...
    @staticmethod
    def GetReal_s(IS : Any) -> Tuple[float]: 
        """
        Reads the Standard_Real value from the stream. Zero is read in case of error
        """
    @staticmethod
    def GetUndefinedTypeHandler_s() -> GeomTools_UndefinedTypeHandler: 
        """
        None
        """
    @staticmethod
    @overload
    def Read_s(S : OCP.Geom.Geom_Surface,IS : Any) -> None: 
        """
        Reads the surface from the stream.

        Reads the Curve from the stream.

        Reads the Curve from the stream.
        """
    @staticmethod
    @overload
    def Read_s(C : OCP.Geom2d.Geom2d_Curve,IS : Any) -> None: ...
    @staticmethod
    @overload
    def Read_s(C : OCP.Geom.Geom_Curve,IS : Any) -> None: ...
    @staticmethod
    def SetUndefinedTypeHandler_s(aHandler : GeomTools_UndefinedTypeHandler) -> None: 
        """
        None
        """
    @staticmethod
    @overload
    def Write_s(S : OCP.Geom.Geom_Surface,OS : Any) -> None: 
        """
        Writes the surface on the stream.

        Writes the Curve on the stream.

        Writes the Curve on the stream.
        """
    @staticmethod
    @overload
    def Write_s(C : OCP.Geom.Geom_Curve,OS : Any) -> None: ...
    @staticmethod
    @overload
    def Write_s(C : OCP.Geom2d.Geom2d_Curve,OS : Any) -> None: ...
    def __init__(self) -> None: ...
    pass
class GeomTools_Curve2dSet():
    """
    Stores a set of Curves from Geom2d.
    """
    def Add(self,C : OCP.Geom2d.Geom2d_Curve) -> int: 
        """
        Incorporate a new Curve in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Curve2d(self,I : int) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def Dump(self,OS : Any) -> None: 
        """
        Dumps the content of me on the stream <OS>.
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        None
        """
    def Index(self,C : OCP.Geom2d.Geom2d_Curve) -> int: 
        """
        Returns the index of <L>.
        """
    @staticmethod
    def PrintCurve2d_s(C : OCP.Geom2d.Geom2d_Curve,OS : Any,compact : bool=False) -> None: 
        """
        Dumps the curve on the stream, if compact is True use the compact format that can be read back.
        """
    def Read(self,IS : Any) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadCurve2d_s(IS : Any) -> OCP.Geom2d.Geom2d_Curve: 
        """
        Reads the curve from the stream. The curve is assumed to have been written with the Print method (compact = True).
        """
    def SetProgress(self,PR : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        None
        """
    def Write(self,OS : Any) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class GeomTools_CurveSet():
    """
    Stores a set of Curves from Geom.
    """
    def Add(self,C : OCP.Geom.Geom_Curve) -> int: 
        """
        Incorporate a new Curve in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Curve(self,I : int) -> OCP.Geom.Geom_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def Dump(self,OS : Any) -> None: 
        """
        Dumps the content of me on the stream <OS>.
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        None
        """
    def Index(self,C : OCP.Geom.Geom_Curve) -> int: 
        """
        Returns the index of <L>.
        """
    @staticmethod
    def PrintCurve_s(C : OCP.Geom.Geom_Curve,OS : Any,compact : bool=False) -> None: 
        """
        Dumps the curve on the stream, if compact is True use the compact format that can be read back.
        """
    def Read(self,IS : Any) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadCurve_s(IS : Any) -> OCP.Geom.Geom_Curve: 
        """
        Reads the curve from the stream. The curve is assumed to have been written with the Print method (compact = True).
        """
    def SetProgress(self,PR : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        None
        """
    def Write(self,OS : Any) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class GeomTools_SurfaceSet():
    """
    Stores a set of Surfaces from Geom.
    """
    def Add(self,S : OCP.Geom.Geom_Surface) -> int: 
        """
        Incorporate a new Surface in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Dump(self,OS : Any) -> None: 
        """
        Dumps the content of me on the stream <OS>.
        """
    def GetProgress(self) -> OCP.Message.Message_ProgressIndicator: 
        """
        None
        """
    def Index(self,S : OCP.Geom.Geom_Surface) -> int: 
        """
        Returns the index of <L>.
        """
    @staticmethod
    def PrintSurface_s(S : OCP.Geom.Geom_Surface,OS : Any,compact : bool=False) -> None: 
        """
        Dumps the surface on the stream, if compact is True use the compact format that can be read back.
        """
    def Read(self,IS : Any) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadSurface_s(IS : Any) -> OCP.Geom.Geom_Surface: 
        """
        Reads the surface from the stream. The surface is assumed to have been written with the Print method (compact = True).
        """
    def SetProgress(self,PR : OCP.Message.Message_ProgressIndicator) -> None: 
        """
        None
        """
    def Surface(self,I : int) -> OCP.Geom.Geom_Surface: 
        """
        Returns the Surface of index <I>.
        """
    def Write(self,OS : Any) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class GeomTools_UndefinedTypeHandler(OCP.Standard.Standard_Transient):
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
    def PrintCurve(self,C : OCP.Geom.Geom_Curve,OS : Any,compact : bool=False) -> None: 
        """
        None
        """
    def PrintCurve2d(self,C : OCP.Geom2d.Geom2d_Curve,OS : Any,compact : bool=False) -> None: 
        """
        None
        """
    def PrintSurface(self,S : OCP.Geom.Geom_Surface,OS : Any,compact : bool=False) -> None: 
        """
        None
        """
    def ReadCurve(self,ctype : int,IS : Any,C : OCP.Geom.Geom_Curve) -> Any: 
        """
        None
        """
    def ReadCurve2d(self,ctype : int,IS : Any,C : OCP.Geom2d.Geom2d_Curve) -> Any: 
        """
        None
        """
    def ReadSurface(self,ctype : int,IS : Any,S : OCP.Geom.Geom_Surface) -> Any: 
        """
        None
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
