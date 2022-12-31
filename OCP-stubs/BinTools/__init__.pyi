import OCP.BinTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Geom
import OCP.TopLoc
import OCP.TopoDS
import OCP.gp
import OCP.TopAbs
import OCP.Geom2d
import io
__all__  = [
"BinTools",
"BinTools_Curve2dSet",
"BinTools_CurveSet",
"BinTools_FormatVersion",
"BinTools_IStream",
"BinTools_LocationSet",
"BinTools_OStream",
"BinTools_ObjectType",
"BinTools_ShapeSetBase",
"BinTools_ShapeSet",
"BinTools_ShapeReader",
"BinTools_ShapeWriter",
"BinTools_SurfaceSet",
"HashCode",
"BinTools_FormatVersion_CURRENT",
"BinTools_FormatVersion_LOWER",
"BinTools_FormatVersion_UPPER",
"BinTools_FormatVersion_VERSION_1",
"BinTools_FormatVersion_VERSION_2",
"BinTools_FormatVersion_VERSION_3",
"BinTools_FormatVersion_VERSION_4",
"BinTools_ObjectType_Curve",
"BinTools_ObjectType_Curve2d",
"BinTools_ObjectType_EmptyCurve",
"BinTools_ObjectType_EmptyCurve2d",
"BinTools_ObjectType_EmptyLocation",
"BinTools_ObjectType_EmptyPolygon3d",
"BinTools_ObjectType_EmptyPolygonOnTriangulation",
"BinTools_ObjectType_EmptyShape",
"BinTools_ObjectType_EmptySurface",
"BinTools_ObjectType_EmptyTriangulation",
"BinTools_ObjectType_EndShape",
"BinTools_ObjectType_Location",
"BinTools_ObjectType_LocationEnd",
"BinTools_ObjectType_Polygon3d",
"BinTools_ObjectType_PolygonOnTriangulation",
"BinTools_ObjectType_Reference16",
"BinTools_ObjectType_Reference32",
"BinTools_ObjectType_Reference64",
"BinTools_ObjectType_Reference8",
"BinTools_ObjectType_SimpleLocation",
"BinTools_ObjectType_Surface",
"BinTools_ObjectType_Triangulation",
"BinTools_ObjectType_Unknown"
]
class BinTools():
    """
    Tool to keep shapes in binary format
    """
    @staticmethod
    def GetBool_s(IS : io.BytesIO,theValue : bool) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def GetExtChar_s(IS : io.BytesIO,theValue : str) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def GetInteger_s(IS : io.BytesIO,theValue : int) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def GetReal_s(IS : io.BytesIO,theValue : float) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def GetShortReal_s(IS : io.BytesIO,theValue : float) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def PutBool_s(OS : io.BytesIO,theValue : bool) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def PutExtChar_s(OS : io.BytesIO,theValue : str) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def PutInteger_s(OS : io.BytesIO,theValue : int) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def PutReal_s(OS : io.BytesIO,theValue : float) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    def PutShortReal_s(OS : io.BytesIO,theValue : float) -> io.BytesIO: 
        """
        None
        """
    @staticmethod
    @overload
    def Read_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Reads a shape from <theStream> and returns it in <theShape>.

        Reads a shape from <theFile> and returns it in <theShape>.
        """
    @staticmethod
    @overload
    def Read_s(theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the shape to the stream in binary format BinTools_FormatVersion_CURRENT. This alias writes shape with triangulation data.

        Writes the shape to the stream in binary format of specified version.

        Writes the shape to the file in binary format BinTools_FormatVersion_CURRENT.

        Writes the shape to the file in binary format of specified version.
        """
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO,theWithTriangles : bool,theWithNormals : bool,theVersion : BinTools_FormatVersion,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theWithTriangles : bool,theWithNormals : bool,theVersion : BinTools_FormatVersion,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    def __init__(self) -> None: ...
    pass
class BinTools_Curve2dSet():
    """
    Stores a set of Curves from Geom2d in binary format
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
    def Index(self,C : OCP.Geom2d.Geom2d_Curve) -> int: 
        """
        Returns the index of <L>.
        """
    def Read(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadCurve2d_s(IS : io.BytesIO,C : OCP.Geom2d.Geom2d_Curve) -> io.BytesIO: 
        """
        Reads the curve from the stream. The curve is assumed to have been written with the Write method.
        """
    def Write(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    @staticmethod
    def WriteCurve2d_s(C : OCP.Geom2d.Geom2d_Curve,OS : BinTools_OStream) -> None: 
        """
        Dumps the curve on the binary stream, that can be read back.
        """
    def __init__(self) -> None: ...
    pass
class BinTools_CurveSet():
    """
    Stores a set of Curves from Geom in binary format.
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
    def Index(self,C : OCP.Geom.Geom_Curve) -> int: 
        """
        Returns the index of <L>.
        """
    def Read(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadCurve_s(IS : io.BytesIO,C : OCP.Geom.Geom_Curve) -> io.BytesIO: 
        """
        Reads the curve from the stream. The curve is assumed to have been written with the Write method
        """
    def Write(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    @staticmethod
    def WriteCurve_s(C : OCP.Geom.Geom_Curve,OS : BinTools_OStream) -> None: 
        """
        Dumps the curve on the stream in binary format that can be read back.
        """
    def __init__(self) -> None: ...
    pass
class BinTools_FormatVersion():
    """
    Defined BinTools format version

    Members:

      BinTools_FormatVersion_VERSION_1

      BinTools_FormatVersion_VERSION_2

      BinTools_FormatVersion_VERSION_3

      BinTools_FormatVersion_VERSION_4

      BinTools_FormatVersion_CURRENT
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
    BinTools_FormatVersion_CURRENT: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>
    BinTools_FormatVersion_VERSION_1: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1: 1>
    BinTools_FormatVersion_VERSION_2: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2: 2>
    BinTools_FormatVersion_VERSION_3: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3: 3>
    BinTools_FormatVersion_VERSION_4: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>
    __entries: dict # value = {'BinTools_FormatVersion_VERSION_1': (<BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1: 1>, None), 'BinTools_FormatVersion_VERSION_2': (<BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2: 2>, None), 'BinTools_FormatVersion_VERSION_3': (<BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3: 3>, None), 'BinTools_FormatVersion_VERSION_4': (<BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>, None), 'BinTools_FormatVersion_CURRENT': (<BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>, None)}
    __members__: dict # value = {'BinTools_FormatVersion_VERSION_1': <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1: 1>, 'BinTools_FormatVersion_VERSION_2': <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2: 2>, 'BinTools_FormatVersion_VERSION_3': <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3: 3>, 'BinTools_FormatVersion_VERSION_4': <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>, 'BinTools_FormatVersion_CURRENT': <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>}
    pass
class BinTools_IStream():
    """
    Substitution of IStream for shape reader for fast management of position in the file (get and go) and operation on all reading types.
    """
    def GoTo(self,thePosition : int) -> None: 
        """
        Moves the current stream position to the given one.
        """
    def IsReference(self) -> bool: 
        """
        Returns true if the last restored type is one of a reference
        """
    def LastType(self) -> BinTools_ObjectType: 
        """
        Returns the last read type.
        """
    def Position(self) -> int: 
        """
        Returns the current position in the stream.
        """
    def ReadBool(self) -> bool: 
        """
        Reads boolean value from the stream (stored as one byte).
        """
    @overload
    def ReadBools(self) -> Tuple[bool, bool, bool, bool, bool, bool, bool]: 
        """
        Reads 3 boolean values from one byte

        Reads 7 boolean values from one byte
        """
    @overload
    def ReadBools(self) -> Tuple[bool, bool, bool]: ...
    def ReadByte(self) -> int: 
        """
        Reads byte value from the stream.
        """
    def ReadInteger(self) -> int: 
        """
        Reads integer value from the stream.
        """
    def ReadPnt(self) -> OCP.gp.gp_Pnt: 
        """
        Reads point coordinates value from the stream.
        """
    def ReadReal(self) -> float: 
        """
        Reads real value from the stream.
        """
    def ReadReference(self) -> int: 
        """
        Reads a reference IStream using the last restored type.
        """
    def ReadShortReal(self) -> float: 
        """
        Reads short real value from the stream.
        """
    def ReadType(self) -> BinTools_ObjectType: 
        """
        Reads and returns the type.
        """
    def ShapeOrientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the shape orientation by the last retrieved type.
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Returns the shape type by the last retrieved type.
        """
    def Stream(self) -> io.BytesIO: 
        """
        Returns the original IStream.
        """
    def UpdatePosition(self) -> None: 
        """
        Makes up to date the myPosition because myStream was used outside and position is changed.
        """
    def __init__(self,theStream : io.BytesIO) -> None: ...
    pass
class BinTools_LocationSet():
    """
    The class LocationSet stores a set of location in a relocatable state.
    """
    def Add(self,L : OCP.TopLoc.TopLoc_Location) -> int: 
        """
        Incorporate a new Location in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Index(self,L : OCP.TopLoc.TopLoc_Location) -> int: 
        """
        Returns the index of <L>.
        """
    def Location(self,I : int) -> OCP.TopLoc.TopLoc_Location: 
        """
        Returns the location of index <I>.
        """
    def NbLocations(self) -> int: 
        """
        Returns number of locations.
        """
    def Read(self,IS : io.BytesIO) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    def Write(self,OS : io.BytesIO) -> None: 
        """
        Writes the content of me on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class BinTools_OStream():
    """
    Substitution of OStream for shape writer for fast management of position in the file and operation on all writing types.
    """
    def Position(self) -> int: 
        """
        Returns the current position of the stream
        """
    @overload
    def PutBools(self,theValue1 : bool,theValue2 : bool,theValue3 : bool,theValue4 : bool,theValue5 : bool,theValue6 : bool,theValue7 : bool) -> None: 
        """
        Writes 3 booleans as one byte to the stream.

        Writes 7 booleans as one byte to the stream.
        """
    @overload
    def PutBools(self,theValue1 : bool,theValue2 : bool,theValue3 : bool) -> None: ...
    def WriteReference(self,thePosition : int) -> None: 
        """
        Writes the reference to the given position (an offset between the current and the given one).
        """
    def WriteShape(self,theType : OCP.TopAbs.TopAbs_ShapeEnum,theOrientation : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Writes an identifier of shape type and orientation into the stream.
        """
    def __init__(self,theStream : io.BytesIO) -> None: ...
    pass
class BinTools_ObjectType():
    """
    Enumeration defining objects identifiers in the shape read/write format.

    Members:

      BinTools_ObjectType_Unknown

      BinTools_ObjectType_Reference8

      BinTools_ObjectType_Reference16

      BinTools_ObjectType_Reference32

      BinTools_ObjectType_Reference64

      BinTools_ObjectType_Location

      BinTools_ObjectType_SimpleLocation

      BinTools_ObjectType_EmptyLocation

      BinTools_ObjectType_LocationEnd

      BinTools_ObjectType_Curve

      BinTools_ObjectType_EmptyCurve

      BinTools_ObjectType_Curve2d

      BinTools_ObjectType_EmptyCurve2d

      BinTools_ObjectType_Surface

      BinTools_ObjectType_EmptySurface

      BinTools_ObjectType_Polygon3d

      BinTools_ObjectType_EmptyPolygon3d

      BinTools_ObjectType_PolygonOnTriangulation

      BinTools_ObjectType_EmptyPolygonOnTriangulation

      BinTools_ObjectType_Triangulation

      BinTools_ObjectType_EmptyTriangulation

      BinTools_ObjectType_EmptyShape

      BinTools_ObjectType_EndShape
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
    BinTools_ObjectType_Curve: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Curve: 9>
    BinTools_ObjectType_Curve2d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Curve2d: 11>
    BinTools_ObjectType_EmptyCurve: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve: 10>
    BinTools_ObjectType_EmptyCurve2d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d: 12>
    BinTools_ObjectType_EmptyLocation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyLocation: 7>
    BinTools_ObjectType_EmptyPolygon3d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d: 16>
    BinTools_ObjectType_EmptyPolygonOnTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation: 18>
    BinTools_ObjectType_EmptyShape: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyShape: 198>
    BinTools_ObjectType_EmptySurface: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptySurface: 14>
    BinTools_ObjectType_EmptyTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation: 20>
    BinTools_ObjectType_EndShape: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EndShape: 199>
    BinTools_ObjectType_Location: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Location: 5>
    BinTools_ObjectType_LocationEnd: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_LocationEnd: 8>
    BinTools_ObjectType_Polygon3d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Polygon3d: 15>
    BinTools_ObjectType_PolygonOnTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation: 17>
    BinTools_ObjectType_Reference16: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference16: 2>
    BinTools_ObjectType_Reference32: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference32: 3>
    BinTools_ObjectType_Reference64: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference64: 4>
    BinTools_ObjectType_Reference8: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference8: 1>
    BinTools_ObjectType_SimpleLocation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_SimpleLocation: 6>
    BinTools_ObjectType_Surface: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Surface: 13>
    BinTools_ObjectType_Triangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Triangulation: 19>
    BinTools_ObjectType_Unknown: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Unknown: 0>
    __entries: dict # value = {'BinTools_ObjectType_Unknown': (<BinTools_ObjectType.BinTools_ObjectType_Unknown: 0>, None), 'BinTools_ObjectType_Reference8': (<BinTools_ObjectType.BinTools_ObjectType_Reference8: 1>, None), 'BinTools_ObjectType_Reference16': (<BinTools_ObjectType.BinTools_ObjectType_Reference16: 2>, None), 'BinTools_ObjectType_Reference32': (<BinTools_ObjectType.BinTools_ObjectType_Reference32: 3>, None), 'BinTools_ObjectType_Reference64': (<BinTools_ObjectType.BinTools_ObjectType_Reference64: 4>, None), 'BinTools_ObjectType_Location': (<BinTools_ObjectType.BinTools_ObjectType_Location: 5>, None), 'BinTools_ObjectType_SimpleLocation': (<BinTools_ObjectType.BinTools_ObjectType_SimpleLocation: 6>, None), 'BinTools_ObjectType_EmptyLocation': (<BinTools_ObjectType.BinTools_ObjectType_EmptyLocation: 7>, None), 'BinTools_ObjectType_LocationEnd': (<BinTools_ObjectType.BinTools_ObjectType_LocationEnd: 8>, None), 'BinTools_ObjectType_Curve': (<BinTools_ObjectType.BinTools_ObjectType_Curve: 9>, None), 'BinTools_ObjectType_EmptyCurve': (<BinTools_ObjectType.BinTools_ObjectType_EmptyCurve: 10>, None), 'BinTools_ObjectType_Curve2d': (<BinTools_ObjectType.BinTools_ObjectType_Curve2d: 11>, None), 'BinTools_ObjectType_EmptyCurve2d': (<BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d: 12>, None), 'BinTools_ObjectType_Surface': (<BinTools_ObjectType.BinTools_ObjectType_Surface: 13>, None), 'BinTools_ObjectType_EmptySurface': (<BinTools_ObjectType.BinTools_ObjectType_EmptySurface: 14>, None), 'BinTools_ObjectType_Polygon3d': (<BinTools_ObjectType.BinTools_ObjectType_Polygon3d: 15>, None), 'BinTools_ObjectType_EmptyPolygon3d': (<BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d: 16>, None), 'BinTools_ObjectType_PolygonOnTriangulation': (<BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation: 17>, None), 'BinTools_ObjectType_EmptyPolygonOnTriangulation': (<BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation: 18>, None), 'BinTools_ObjectType_Triangulation': (<BinTools_ObjectType.BinTools_ObjectType_Triangulation: 19>, None), 'BinTools_ObjectType_EmptyTriangulation': (<BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation: 20>, None), 'BinTools_ObjectType_EmptyShape': (<BinTools_ObjectType.BinTools_ObjectType_EmptyShape: 198>, None), 'BinTools_ObjectType_EndShape': (<BinTools_ObjectType.BinTools_ObjectType_EndShape: 199>, None)}
    __members__: dict # value = {'BinTools_ObjectType_Unknown': <BinTools_ObjectType.BinTools_ObjectType_Unknown: 0>, 'BinTools_ObjectType_Reference8': <BinTools_ObjectType.BinTools_ObjectType_Reference8: 1>, 'BinTools_ObjectType_Reference16': <BinTools_ObjectType.BinTools_ObjectType_Reference16: 2>, 'BinTools_ObjectType_Reference32': <BinTools_ObjectType.BinTools_ObjectType_Reference32: 3>, 'BinTools_ObjectType_Reference64': <BinTools_ObjectType.BinTools_ObjectType_Reference64: 4>, 'BinTools_ObjectType_Location': <BinTools_ObjectType.BinTools_ObjectType_Location: 5>, 'BinTools_ObjectType_SimpleLocation': <BinTools_ObjectType.BinTools_ObjectType_SimpleLocation: 6>, 'BinTools_ObjectType_EmptyLocation': <BinTools_ObjectType.BinTools_ObjectType_EmptyLocation: 7>, 'BinTools_ObjectType_LocationEnd': <BinTools_ObjectType.BinTools_ObjectType_LocationEnd: 8>, 'BinTools_ObjectType_Curve': <BinTools_ObjectType.BinTools_ObjectType_Curve: 9>, 'BinTools_ObjectType_EmptyCurve': <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve: 10>, 'BinTools_ObjectType_Curve2d': <BinTools_ObjectType.BinTools_ObjectType_Curve2d: 11>, 'BinTools_ObjectType_EmptyCurve2d': <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d: 12>, 'BinTools_ObjectType_Surface': <BinTools_ObjectType.BinTools_ObjectType_Surface: 13>, 'BinTools_ObjectType_EmptySurface': <BinTools_ObjectType.BinTools_ObjectType_EmptySurface: 14>, 'BinTools_ObjectType_Polygon3d': <BinTools_ObjectType.BinTools_ObjectType_Polygon3d: 15>, 'BinTools_ObjectType_EmptyPolygon3d': <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d: 16>, 'BinTools_ObjectType_PolygonOnTriangulation': <BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation: 17>, 'BinTools_ObjectType_EmptyPolygonOnTriangulation': <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation: 18>, 'BinTools_ObjectType_Triangulation': <BinTools_ObjectType.BinTools_ObjectType_Triangulation: 19>, 'BinTools_ObjectType_EmptyTriangulation': <BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation: 20>, 'BinTools_ObjectType_EmptyShape': <BinTools_ObjectType.BinTools_ObjectType_EmptyShape: 198>, 'BinTools_ObjectType_EndShape': <BinTools_ObjectType.BinTools_ObjectType_EndShape: 199>}
    pass
class BinTools_ShapeSetBase():
    """
    A base class for all readers/writers of TopoDS_Shape into/from stream.
    """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def FormatNb(self) -> int: 
        """
        Returns the BinTools_FormatVersion.
        """
    def IsWithNormals(self) -> bool: 
        """
        Return true if shape should be stored triangulation with normals.
        """
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
        """
    @overload
    def Read(self,arg1 : io.BytesIO,arg2 : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the binary stream <IS>. me is first cleared.

        An empty virtual method for redefinition in shape-reader.
        """
    @overload
    def Read(self,arg1 : io.BytesIO,arg2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        Sets the BinTools_FormatVersion.
        """
    def SetWithNormals(self,theWithNormals : bool) -> None: 
        """
        Define if shape will be stored triangulation with normals. Ignored (always written) if face defines only triangulation (no surface).
        """
    def SetWithTriangles(self,theWithTriangles : bool) -> None: 
        """
        Define if shape will be stored with triangles. Ignored (always written) if face defines only triangulation (no surface).
        """
    @overload
    def Write(self,arg1 : io.BytesIO,arg2 : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in binary format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,arg1 : OCP.TopoDS.TopoDS_Shape,arg2 : io.BytesIO) -> None: ...
    def __init__(self) -> None: ...
    pass
class BinTools_ShapeSet(BinTools_ShapeSetBase):
    """
    Writes topology in OStream in binary format
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Stores <S> and its sub-shape. Returns the index of <S>. The method AddGeometry is called on each sub-shape.
        """
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores the shape <S>.
        """
    def AddShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Inserts the shape <S2> in the shape <S1>.
        """
    def ChangeLocations(self) -> BinTools_LocationSet: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def FormatNb(self) -> int: 
        """
        Returns the BinTools_FormatVersion.
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the index of <S>.
        """
    def IsWithNormals(self) -> bool: 
        """
        Return true if shape should be stored triangulation with normals.
        """
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
        """
    def Locations(self) -> BinTools_LocationSet: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        Returns number of shapes read from file.
        """
    @overload
    def Read(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the binary stream <IS>. me is first cleared.

        An empty virtual method for redefinition in shape-reader.
        """
    @overload
    def Read(self,arg1 : io.BytesIO,arg2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def ReadFlagsAndSubs(self,S : OCP.TopoDS.TopoDS_Shape,T : OCP.TopAbs.TopAbs_ShapeEnum,IS : io.BytesIO,NbShapes : int) -> None: 
        """
        Reads from <IS> a shape flags and sub-shapes and modifies S.
        """
    def ReadGeometry(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the geometry of me from the stream <IS>.
        """
    def ReadPolygon3D(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the 3d polygons of me from the stream <IS>.
        """
    def ReadPolygonOnTriangulation(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the polygons on triangulation of me from the stream <IS>.
        """
    def ReadShape(self,T : OCP.TopAbs.TopAbs_ShapeEnum,IS : io.BytesIO,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Reads a shape of type <T> from the stream <IS> and returns it in <S>.
        """
    def ReadSubs(self,S : OCP.TopoDS.TopoDS_Shape,IS : io.BytesIO,NbShapes : int) -> None: 
        """
        Reads from <IS> a shape and returns it in S. <NbShapes> is the number of tshapes in the set.
        """
    def ReadTriangulation(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the triangulation of me from the stream <IS>.
        """
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        Sets the BinTools_FormatVersion.
        """
    def SetWithNormals(self,theWithNormals : bool) -> None: 
        """
        Define if shape will be stored triangulation with normals. Ignored (always written) if face defines only triangulation (no surface).
        """
    def SetWithTriangles(self,theWithTriangles : bool) -> None: 
        """
        Define if shape will be stored with triangles. Ignored (always written) if face defines only triangulation (no surface).
        """
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the sub-shape of index <I>.
        """
    @overload
    def Write(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the content of me on the stream <OS> in binary format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def WriteGeometry(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the geometry of me on the stream <OS> in a binary format that can be read back by Read.
        """
    def WritePolygon3D(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the 3d polygons on the stream <OS> in a format that can be read back by Read.
        """
    def WritePolygonOnTriangulation(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the polygons on triangulation on the stream <OS> in a format that can be read back by Read.
        """
    def WriteShape(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the shape <S> on the stream <OS> in a binary format that can be read back by Read.
        """
    def WriteTriangulation(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the triangulation on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self) -> None: ...
    pass
class BinTools_ShapeReader(BinTools_ShapeSetBase):
    """
    Reads topology from IStream in binary format without grouping of objects by types and using relative positions in a file as references.
    """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def FormatNb(self) -> int: 
        """
        Returns the BinTools_FormatVersion.
        """
    def IsWithNormals(self) -> bool: 
        """
        Return true if shape should be stored triangulation with normals.
        """
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
        """
    def Read(self,theStream : io.BytesIO,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Reads the shape from stream using previously restored shapes and objects by references.
        """
    def ReadLocation(self,theStream : BinTools_IStream) -> OCP.TopLoc.TopLoc_Location: 
        """
        Reads location from the stream.
        """
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        Sets the BinTools_FormatVersion.
        """
    def SetWithNormals(self,theWithNormals : bool) -> None: 
        """
        Define if shape will be stored triangulation with normals. Ignored (always written) if face defines only triangulation (no surface).
        """
    def SetWithTriangles(self,theWithTriangles : bool) -> None: 
        """
        Define if shape will be stored with triangles. Ignored (always written) if face defines only triangulation (no surface).
        """
    @overload
    def Write(self,arg1 : io.BytesIO,arg2 : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in binary format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,arg1 : OCP.TopoDS.TopoDS_Shape,arg2 : io.BytesIO) -> None: ...
    def __init__(self) -> None: ...
    pass
class BinTools_ShapeWriter(BinTools_ShapeSetBase):
    """
    Writes topology in OStream in binary format without grouping of objects by types and using relative positions in a file as references.
    """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def FormatNb(self) -> int: 
        """
        Returns the BinTools_FormatVersion.
        """
    def IsWithNormals(self) -> bool: 
        """
        Return true if shape should be stored triangulation with normals.
        """
    def IsWithTriangles(self) -> bool: 
        """
        Return true if shape should be stored with triangles.
        """
    @overload
    def Read(self,arg1 : io.BytesIO,arg2 : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the binary stream <IS>. me is first cleared.

        An empty virtual method for redefinition in shape-reader.
        """
    @overload
    def Read(self,arg1 : io.BytesIO,arg2 : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        Sets the BinTools_FormatVersion.
        """
    def SetWithNormals(self,theWithNormals : bool) -> None: 
        """
        Define if shape will be stored triangulation with normals. Ignored (always written) if face defines only triangulation (no surface).
        """
    def SetWithTriangles(self,theWithTriangles : bool) -> None: 
        """
        Define if shape will be stored with triangles. Ignored (always written) if face defines only triangulation (no surface).
        """
    def Write(self,theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO) -> None: 
        """
        Writes the shape to stream using previously stored shapes and objects to refer them.
        """
    def WriteLocation(self,theStream : BinTools_OStream,theLocation : OCP.TopLoc.TopLoc_Location) -> None: 
        """
        Writes location to the stream (all the needed sub-information or reference if it is already used).
        """
    def __init__(self) -> None: ...
    pass
class BinTools_SurfaceSet():
    """
    Stores a set of Surfaces from Geom in binary format.
    """
    def Add(self,S : OCP.Geom.Geom_Surface) -> int: 
        """
        Incorporate a new Surface in the set and returns its index.
        """
    def Clear(self) -> None: 
        """
        Clears the content of the set.
        """
    def Index(self,S : OCP.Geom.Geom_Surface) -> int: 
        """
        Returns the index of <L>.
        """
    def Read(self,IS : io.BytesIO,therange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the content of me from the stream <IS>. me is first cleared.
        """
    @staticmethod
    def ReadSurface_s(IS : io.BytesIO,S : OCP.Geom.Geom_Surface) -> io.BytesIO: 
        """
        Reads the surface from the stream. The surface is assumed to have been written with the Write method.
        """
    def Surface(self,I : int) -> OCP.Geom.Geom_Surface: 
        """
        Returns the Surface of index <I>.
        """
    def Write(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in binary format that can be read back by Read.
        """
    @staticmethod
    def WriteSurface_s(S : OCP.Geom.Geom_Surface,OS : BinTools_OStream) -> None: 
        """
        Dumps the surface on the stream in binary format that can be read back.
        """
    def __init__(self) -> None: ...
    pass
def HashCode(theValue : int,theUpperBound : int) -> int:
    """
    Computes a hash code for the given value of the uint64_t type, in range [1, theUpperBound]
    """
BinTools_FormatVersion_CURRENT: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>
BinTools_FormatVersion_LOWER = 1
BinTools_FormatVersion_UPPER = 4
BinTools_FormatVersion_VERSION_1: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_1: 1>
BinTools_FormatVersion_VERSION_2: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_2: 2>
BinTools_FormatVersion_VERSION_3: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_3: 3>
BinTools_FormatVersion_VERSION_4: OCP.BinTools.BinTools_FormatVersion # value = <BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4: 4>
BinTools_ObjectType_Curve: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Curve: 9>
BinTools_ObjectType_Curve2d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Curve2d: 11>
BinTools_ObjectType_EmptyCurve: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve: 10>
BinTools_ObjectType_EmptyCurve2d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyCurve2d: 12>
BinTools_ObjectType_EmptyLocation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyLocation: 7>
BinTools_ObjectType_EmptyPolygon3d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygon3d: 16>
BinTools_ObjectType_EmptyPolygonOnTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyPolygonOnTriangulation: 18>
BinTools_ObjectType_EmptyShape: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyShape: 198>
BinTools_ObjectType_EmptySurface: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptySurface: 14>
BinTools_ObjectType_EmptyTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EmptyTriangulation: 20>
BinTools_ObjectType_EndShape: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_EndShape: 199>
BinTools_ObjectType_Location: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Location: 5>
BinTools_ObjectType_LocationEnd: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_LocationEnd: 8>
BinTools_ObjectType_Polygon3d: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Polygon3d: 15>
BinTools_ObjectType_PolygonOnTriangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_PolygonOnTriangulation: 17>
BinTools_ObjectType_Reference16: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference16: 2>
BinTools_ObjectType_Reference32: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference32: 3>
BinTools_ObjectType_Reference64: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference64: 4>
BinTools_ObjectType_Reference8: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Reference8: 1>
BinTools_ObjectType_SimpleLocation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_SimpleLocation: 6>
BinTools_ObjectType_Surface: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Surface: 13>
BinTools_ObjectType_Triangulation: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Triangulation: 19>
BinTools_ObjectType_Unknown: OCP.BinTools.BinTools_ObjectType # value = <BinTools_ObjectType.BinTools_ObjectType_Unknown: 0>
