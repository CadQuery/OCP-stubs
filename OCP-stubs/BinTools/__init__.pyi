import OCP.BinTools
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import OCP.Geom
import OCP.TopoDS
import OCP.TopLoc
import OCP.Geom2d
import OCP.TopAbs
__all__  = [
"BinTools",
"BinTools_Curve2dSet",
"BinTools_CurveSet",
"BinTools_LocationSet",
"BinTools_ShapeSet",
"BinTools_SurfaceSet"
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
    def Read_s(theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads a shape from <theStream> and returns it in <theShape>.

        Reads a shape from <theFile> and returns it in <theShape>.
        """
    @staticmethod
    @overload
    def Read_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: ...
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theFile : str,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> bool: 
        """
        Writes <theShape> on <theStream> in binary format.

        Writes <theShape> in <theFile>.
        """
    @staticmethod
    @overload
    def Write_s(theShape : OCP.TopoDS.TopoDS_Shape,theStream : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
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
    def WriteCurve2d_s(C : OCP.Geom2d.Geom2d_Curve,OS : io.BytesIO) -> None: 
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
    def WriteCurve_s(C : OCP.Geom.Geom_Curve,OS : io.BytesIO) -> None: 
        """
        Dumps the curve on the stream in binary format that can be read back.
        """
    def __init__(self) -> None: ...
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
class BinTools_ShapeSet():
    """
    Writes topology in OStream in binary format
    """
    def Add(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Stores <S> and its sub-shape. Returns the index of <S>. The method AddGeometry is called on each sub-shape.
        """
    def AddGeometry(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Stores the goemetry of <S>.
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
        two formats available for the moment: First: does not write CurveOnSurface UV Points into the file on reading calls Check() method. Second: stores CurveOnSurface UV Points. On reading format is recognized from Version string.
        """
    def Index(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns the index of <S>.
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

        Reads from <IS> a shape and returns it in S. <NbShapes> is the number of tshapes in the set.
        """
    @overload
    def Read(self,S : OCP.TopoDS.TopoDS_Shape,IS : io.BytesIO,NbShapes : int) -> None: ...
    @overload
    def ReadGeometry(self,T : OCP.TopAbs.TopAbs_ShapeEnum,IS : io.BytesIO,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Reads the geometry of me from the stream <IS>.

        Reads the geometry of a shape of type <T> from the stream <IS> and returns it in <S>.
        """
    @overload
    def ReadGeometry(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def ReadPolygon3D(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the 3d polygons of me from the stream <IS>.
        """
    def ReadPolygonOnTriangulation(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the polygons on triangulation of me from the stream <IS>.
        """
    def ReadTriangulation(self,IS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Reads the triangulation of me from the stream <IS>.
        """
    def SetFormatNb(self,theFormatNb : int) -> None: 
        """
        None
        """
    def SetWithTriangles(self,isWithTriangles : bool) -> None: 
        """
        Define if shape will be stored with triangles. Ignored (always written) if face defines only triangulation (no surface).
        """
    def Shape(self,I : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the sub-shape of index <I>.
        """
    @overload
    def Write(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the content of me on the stream <OS> in binary format that can be read back by Read.

        Writes on <OS> the shape <S>. Writes the orientation, the index of the TShape and the index of the Location.
        """
    @overload
    def Write(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: ...
    @overload
    def WriteGeometry(self,S : OCP.TopoDS.TopoDS_Shape,OS : io.BytesIO) -> None: 
        """
        Writes the geometry of me on the stream <OS> in a binary format that can be read back by Read.

        Writes the geometry of <S> on the stream <OS> in a binary format that can be read back by Read.
        """
    @overload
    def WriteGeometry(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: ...
    def WritePolygon3D(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the 3d polygons on the stream <OS> in a format that can be read back by Read.
        """
    def WritePolygonOnTriangulation(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the polygons on triangulation on the stream <OS> in a format that can be read back by Read.
        """
    def WriteTriangulation(self,OS : io.BytesIO,theRange : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange) -> None: 
        """
        Writes the triangulation on the stream <OS> in a format that can be read back by Read.
        """
    def __init__(self,isWithTriangles : bool=False) -> None: ...
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
    def WriteSurface_s(S : OCP.Geom.Geom_Surface,OS : io.BytesIO) -> None: 
        """
        Dumps the surface on the stream in binary format that can be read back.
        """
    def __init__(self) -> None: ...
    pass
