import OCP.TopOpeBRepDS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.TCollection
import OCP.TColStd
import io
import OCP.NCollection
import OCP.gp
import OCP.Geom
import OCP.TopOpeBRepTool
import OCP.TopoDS
import OCP.Geom2d
import OCP.Standard
import OCP.TopAbs
__all__  = [
"TopOpeBRepDS",
"TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference",
"TopOpeBRepDS_Association",
"TopOpeBRepDS_BuildTool",
"TopOpeBRepDS_Check",
"TopOpeBRepDS_CheckStatus",
"TopOpeBRepDS_Config",
"TopOpeBRepDS_Curve",
"TopOpeBRepDS_GeometryData",
"TopOpeBRepDS_CurveExplorer",
"TopOpeBRepDS_InterferenceIterator",
"TopOpeBRepDS_Interference",
"TopOpeBRepDS_DataMapOfCheckStatus",
"TopOpeBRepDS_DataMapOfIntegerListOfInterference",
"TopOpeBRepDS_DataMapOfInterferenceListOfInterference",
"TopOpeBRepDS_DataMapOfInterferenceShape",
"TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State",
"TopOpeBRepDS_DataMapOfShapeState",
"TopOpeBRepDS_DataStructure",
"TopOpeBRepDS_DoubleMapOfIntegerShape",
"TopOpeBRepDS_Dumper",
"TopOpeBRepDS_EIR",
"TopOpeBRepDS_Edge3dInterferenceTool",
"TopOpeBRepDS_EdgeInterferenceTool",
"TopOpeBRepDS_ShapeShapeInterference",
"TopOpeBRepDS_Explorer",
"TopOpeBRepDS_FIR",
"TopOpeBRepDS_FaceEdgeInterference",
"TopOpeBRepDS_FaceInterferenceTool",
"TopOpeBRepDS_Filter",
"TopOpeBRepDS_GapFiller",
"TopOpeBRepDS_GapTool",
"TopOpeBRepDS_CurveData",
"TopOpeBRepDS_HArray1OfDataMapOfIntegerListOfInterference",
"TopOpeBRepDS_HDataStructure",
"TopOpeBRepDS_IndexedDataMapOfShapeWithState",
"TopOpeBRepDS_IndexedDataMapOfVertexPoint",
"TopOpeBRepDS_CurvePointInterference",
"TopOpeBRepDS_CurveIterator",
"TopOpeBRepDS_InterferenceTool",
"TopOpeBRepDS_Kind",
"TopOpeBRepDS_ListOfInterference",
"TopOpeBRepDS_ListOfShapeOn1State",
"TopOpeBRepDS_MapOfCurve",
"TopOpeBRepDS_MapOfIntegerShapeData",
"TopOpeBRepDS_MapOfPoint",
"TopOpeBRepDS_MapOfShapeData",
"TopOpeBRepDS_MapOfSurface",
"TopOpeBRepDS_Marker",
"TopOpeBRepDS_Point",
"TopOpeBRepDS_PointData",
"TopOpeBRepDS_PointExplorer",
"TopOpeBRepDS_PointIterator",
"TopOpeBRepDS_Reducer",
"TopOpeBRepDS_ShapeData",
"TopOpeBRepDS_EdgeVertexInterference",
"TopOpeBRepDS_ShapeWithState",
"TopOpeBRepDS_SolidSurfaceInterference",
"TopOpeBRepDS_Surface",
"TopOpeBRepDS_SurfaceCurveInterference",
"TopOpeBRepDS_SurfaceData",
"TopOpeBRepDS_SurfaceExplorer",
"TopOpeBRepDS_SurfaceIterator",
"TopOpeBRepDS_TKI",
"TopOpeBRepDS_TOOL",
"TopOpeBRepDS_Transition",
"FDSCNX_Dump",
"FDSCNX_DumpIndex",
"FDSCNX_EdgeConnexitySameShape",
"FDSCNX_EdgeConnexityShapeIndex",
"FDSCNX_FaceEdgeConnexFaces",
"FDSCNX_HasConnexFace",
"FDSCNX_Prepare",
"FDSSDM_contains",
"FDSSDM_copylist",
"FDSSDM_makes1s2",
"FDSSDM_prepare",
"FDSSDM_s1s2",
"FDSSDM_sordor",
"FDS_Config3d",
"FDS_EdgeIsConnexToSameDomainFaces",
"FDS_HasSameDomain2d",
"FDS_HasSameDomain3d",
"FDS_Idata",
"FDS_LOIinfsup",
"FDS_Parameter",
"FDS_SIisGIofIofSBAofTofI",
"FDS_SetT",
"FDS_Tdata",
"FDS_aresamdom",
"FDS_assign",
"FDS_copy",
"FDS_data",
"FDS_getupperlower",
"FDS_hasUNK",
"FDS_parbefaft",
"FDS_repvg",
"FDS_repvg2",
"FDS_stateEwithF2d",
"FUN_ds_FEIGb1TO0",
"FUN_ds_FillSDMFaces",
"FUN_ds_GetTr",
"FUN_ds_ONesd",
"FUN_ds_PURGEforE9",
"FUN_ds_PointToVertex",
"FUN_ds_addSEsdm1d",
"FUN_ds_complete1dForSESDM",
"FUN_ds_completeforE7",
"FUN_ds_completeforSE1",
"FUN_ds_completeforSE2",
"FUN_ds_completeforSE3",
"FUN_ds_completeforSE4",
"FUN_ds_completeforSE5",
"FUN_ds_completeforSE6",
"FUN_ds_completeforSE8",
"FUN_ds_completeforSE9",
"FUN_ds_getVsdm",
"FUN_ds_getoov",
"FUN_ds_hasFEI",
"FUN_ds_hasI2d",
"FUN_ds_mkTonFsdm",
"FUN_ds_oriEinF",
"FUN_ds_redu2d1d",
"FUN_ds_redusamsha",
"FUN_ds_samRk",
"FUN_ds_sdm",
"FUN_ds_shareG",
"FUN_hasStateShape",
"FUN_interfhassupport",
"FUN_reducedoublons",
"FUN_select1dI",
"FUN_select2dI",
"FUN_select3dinterference",
"FUN_selectGIinterference",
"FUN_selectGKinterference",
"FUN_selectITRASHAinterference",
"FUN_selectSIinterference",
"FUN_selectSKinterference",
"FUN_selectTRAINTinterference",
"FUN_selectTRAORIinterference",
"FUN_selectTRASHAinterference",
"FUN_selectTRAUNKinterference",
"FUN_selectpure2dI",
"FUN_transitionEQUAL",
"FUN_transitionINDEXEQUAL",
"FUN_transitionSHAPEEQUAL",
"FUN_transitionSTATEEQUAL",
"FUN_unkeepUNKNOWN",
"MakeCPVInterference",
"MakeEPVInterference",
"TopOpeBRepDS_COMPOUND",
"TopOpeBRepDS_COMPSOLID",
"TopOpeBRepDS_CURVE",
"TopOpeBRepDS_DIFFORIENTED",
"TopOpeBRepDS_EDGE",
"TopOpeBRepDS_FACE",
"TopOpeBRepDS_NOK",
"TopOpeBRepDS_OK",
"TopOpeBRepDS_POINT",
"TopOpeBRepDS_SAMEORIENTED",
"TopOpeBRepDS_SHELL",
"TopOpeBRepDS_SOLID",
"TopOpeBRepDS_SURFACE",
"TopOpeBRepDS_UNKNOWN",
"TopOpeBRepDS_UNSHGEOMETRY",
"TopOpeBRepDS_VERTEX",
"TopOpeBRepDS_WIRE"
]
class TopOpeBRepDS():
    """
    This package provides services used by the TopOpeBRepBuild package performing topological operations on the BRep data structure.
    """
    @staticmethod
    def IsGeometry_s(K : TopOpeBRepDS_Kind) -> bool: 
        """
        None
        """
    @staticmethod
    def IsTopology_s(K : TopOpeBRepDS_Kind) -> bool: 
        """
        None
        """
    @staticmethod
    def KindToShape_s(K : TopOpeBRepDS_Kind) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    @staticmethod
    @overload
    def Print_s(S : OCP.TopAbs.TopAbs_State,OS : io.BytesIO) -> io.BytesIO: 
        """
        None

        None

        None

        None

        None
        """
    @staticmethod
    @overload
    def Print_s(K : TopOpeBRepDS_Kind,S : io.BytesIO) -> io.BytesIO: ...
    @staticmethod
    @overload
    def Print_s(C : TopOpeBRepDS_Config,S : io.BytesIO) -> io.BytesIO: ...
    @staticmethod
    @overload
    def Print_s(K : TopOpeBRepDS_Kind,I : int,S : io.BytesIO,B : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,A : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> io.BytesIO: ...
    @staticmethod
    @overload
    def Print_s(T : OCP.TopAbs.TopAbs_ShapeEnum,I : int,S : io.BytesIO) -> io.BytesIO: ...
    @staticmethod
    @overload
    def SPrint_s(T : OCP.TopAbs.TopAbs_ShapeEnum,I : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        IN OU ON UN

        <K>

        None

        (<T>,<I>)

        None

        None
        """
    @staticmethod
    @overload
    def SPrint_s(K : TopOpeBRepDS_Kind,I : int,B : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,A : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    @overload
    def SPrint_s(O : OCP.TopAbs.TopAbs_Orientation) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    @overload
    def SPrint_s(C : TopOpeBRepDS_Config) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    @overload
    def SPrint_s(T : OCP.TopAbs.TopAbs_ShapeEnum) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    @overload
    def SPrint_s(S : OCP.TopAbs.TopAbs_State) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    @overload
    def SPrint_s(K : TopOpeBRepDS_Kind) -> OCP.TCollection.TCollection_AsciiString: ...
    @staticmethod
    def ShapeToKind_s(S : OCP.TopAbs.TopAbs_ShapeEnum) -> TopOpeBRepDS_Kind: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Variable value access
        """
    def First(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns first element
        """
    def Init(self,theValue : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : TopOpeBRepDS_DataMapOfIntegerListOfInterference,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_Association(OCP.Standard.Standard_Transient):
    def AreAssociated(self,I : TopOpeBRepDS_Interference,K : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    @overload
    def Associate(self,I : TopOpeBRepDS_Interference,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None

        None
        """
    @overload
    def Associate(self,I : TopOpeBRepDS_Interference,K : TopOpeBRepDS_Interference) -> None: ...
    def Associated(self,I : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
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
    def HasAssociation(self,I : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
class TopOpeBRepDS_BuildTool():
    """
    Provides a Tool to build topologies. Used to instantiate the Builder algorithm.
    """
    @overload
    def AddEdgeVertex(self,Ein : OCP.TopoDS.TopoDS_Shape,Eou : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def AddEdgeVertex(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def AddFaceWire(self,F : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddShellFace(self,Sh : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddSolidShell(self,S : OCP.TopoDS.TopoDS_Shape,Sh : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddWireEdge(self,W : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def ApproxCurves(self,C : TopOpeBRepDS_Curve,E : OCP.TopoDS.TopoDS_Edge,HDS : TopOpeBRepDS_HDataStructure) -> Tuple[int]: 
        """
        None
        """
    def Approximation(self) -> bool: 
        """
        None
        """
    def ChangeGeomTool(self) -> OCP.TopOpeBRepTool.TopOpeBRepTool_GeomTool: 
        """
        None
        """
    def Closed(self,S : OCP.TopoDS.TopoDS_Shape,B : bool) -> None: 
        """
        None
        """
    def ComputePCurves(self,C : TopOpeBRepDS_Curve,E : OCP.TopoDS.TopoDS_Edge,newC : TopOpeBRepDS_Curve,CompPC1 : bool,CompPC2 : bool,CompC3D : bool) -> None: 
        """
        None
        """
    def CopyEdge(self,Ein : OCP.TopoDS.TopoDS_Shape,Eou : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Make an edge <Eou> with the curve of the edge <Ein>
        """
    def CopyFace(self,Fin : OCP.TopoDS.TopoDS_Shape,Fou : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Make a face <Fou> with the surface of the face <Fin>
        """
    def Curve3D(self,E : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve,Tol : float) -> None: 
        """
        Sets the curve <C> for the edge <E>
        """
    def GetGeomTool(self) -> OCP.TopOpeBRepTool.TopOpeBRepTool_GeomTool: 
        """
        None
        """
    def GetOrientedEdgeVertices(self,E : OCP.TopoDS.TopoDS_Edge,Vmin : OCP.TopoDS.TopoDS_Vertex,Vmax : OCP.TopoDS.TopoDS_Vertex) -> Tuple[float, float]: 
        """
        None
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Shape,C : TopOpeBRepDS_Curve,DS : TopOpeBRepDS_DataStructure) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Shape,C : TopOpeBRepDS_Curve) -> None: ...
    @overload
    def MakeEdge(self,E : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve,Tol : float) -> None: ...
    def MakeFace(self,F : OCP.TopoDS.TopoDS_Shape,S : TopOpeBRepDS_Surface) -> None: 
        """
        None
        """
    def MakeShell(self,Sh : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeSolid(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def MakeVertex(self,V : OCP.TopoDS.TopoDS_Shape,P : TopOpeBRepDS_Point) -> None: 
        """
        None
        """
    def MakeWire(self,W : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    @overload
    def Orientation(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Orientation(self,S : OCP.TopoDS.TopoDS_Shape,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def OverWrite(self) -> bool: 
        """
        None

        None
        """
    @overload
    def OverWrite(self,O : bool) -> None: ...
    @overload
    def PCurve(self,F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        Sets the pcurve <C> for the edge <E> on the face <F>. If OverWrite is True the old pcurve if there is one is overwritten, else the two pcurves are set.

        None
        """
    @overload
    def PCurve(self,F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,CDS : TopOpeBRepDS_Curve,C : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Parameter(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape,P : float) -> None: 
        """
        Sets the parameter <P> for the vertex <V> on the edge <E>.

        Compute the parameter of the vertex <V>, supported by the edge <E>, on the curve <C>.
        """
    @overload
    def Parameter(self,C : TopOpeBRepDS_Curve,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def PutPCurves(self,newC : TopOpeBRepDS_Curve,E : OCP.TopoDS.TopoDS_Edge,CompPC1 : bool,CompPC2 : bool) -> None: 
        """
        None
        """
    def Range(self,E : OCP.TopoDS.TopoDS_Shape,first : float,last : float) -> None: 
        """
        Sets the range of edge <E>.
        """
    def RecomputeCurves(self,C : TopOpeBRepDS_Curve,oldE : OCP.TopoDS.TopoDS_Edge,E : OCP.TopoDS.TopoDS_Edge,HDS : TopOpeBRepDS_HDataStructure) -> Tuple[int]: 
        """
        None
        """
    @overload
    def Translate(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Translate(self,T : bool) -> None: ...
    def UpdateEdge(self,Ein : OCP.TopoDS.TopoDS_Shape,Eou : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets the range of edge <Eou> from <Ein> only when <Ein> has a closed geometry.
        """
    def UpdateEdgeCurveTol(self,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,E : OCP.TopoDS.TopoDS_Edge,C3Dnew : OCP.Geom.Geom_Curve,tol3d : float,tol2d1 : float,tol2d2 : float) -> Tuple[float, float, float]: 
        """
        None
        """
    @overload
    def UpdateSurface(self,E : OCP.TopoDS.TopoDS_Shape,oldF : OCP.TopoDS.TopoDS_Shape,newF : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None
        """
    @overload
    def UpdateSurface(self,F : OCP.TopoDS.TopoDS_Shape,SU : OCP.Geom.Geom_Surface) -> None: ...
    @overload
    def __init__(self,GT : OCP.TopOpeBRepTool.TopOpeBRepTool_GeomTool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,OutCurveType : OCP.TopOpeBRepTool.TopOpeBRepTool_OutCurveType) -> None: ...
    pass
class TopOpeBRepDS_Check(OCP.Standard.Standard_Transient):
    """
    a tool verifing integrity and structure of DSa tool verifing integrity and structure of DSa tool verifing integrity and structure of DS
    """
    def ChangeHDS(self) -> TopOpeBRepDS_HDataStructure: 
        """
        None
        """
    def CheckDS(self,i : int,K : TopOpeBRepDS_Kind) -> bool: 
        """
        Verifie que le ieme element de la DS existe, et pour un K de type topologique, verifie qu'il est du bon type (VERTEX, EDGE, WIRE, FACE, SHELL ou SOLID)
        """
    def CheckShapes(self,LS : OCP.TopTools.TopTools_ListOfShape) -> bool: 
        """
        Verifie que les Shapes existent bien dans la DS Utile pour les Shapes SameDomain si la liste est vide, renvoie vrai
        """
    def ChkIntg(self) -> bool: 
        """
        Check integrition of DS
        """
    def ChkIntgInterf(self,LI : TopOpeBRepDS_ListOfInterference) -> bool: 
        """
        Check integrition of interferences (les supports et les geometries de LI)
        """
    def ChkIntgSamDom(self) -> bool: 
        """
        Check integrition des champs SameDomain de la DS
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
    def HDS(self) -> TopOpeBRepDS_HDataStructure: 
        """
        None
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
    def OneVertexOnPnt(self) -> bool: 
        """
        Verifie que les Vertex non SameDomain sont bien nonSameDomain, que les vertex sameDomain sont bien SameDomain, que les Points sont non confondus ni entre eux, ni avec des Vertex.
        """
    def Print(self,stat : TopOpeBRepDS_CheckStatus,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints the name of CheckStatus <stat> as a String
        """
    def PrintIntg(self,S : io.BytesIO) -> io.BytesIO: 
        """
        None
        """
    @overload
    def PrintShape(self,SE : OCP.TopAbs.TopAbs_ShapeEnum,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints the name of CheckStatus <stat> as a String

        Prints the name of CheckStatus <stat> as a String
        """
    @overload
    def PrintShape(self,index : int,S : io.BytesIO) -> io.BytesIO: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
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
class TopOpeBRepDS_CheckStatus():
    """
    None

    Members:

      TopOpeBRepDS_OK

      TopOpeBRepDS_NOK
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    TopOpeBRepDS_NOK: OCP.TopOpeBRepDS.TopOpeBRepDS_CheckStatus # value = <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_NOK: 1>
    TopOpeBRepDS_OK: OCP.TopOpeBRepDS.TopOpeBRepDS_CheckStatus # value = <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_OK: 0>
    __entries: dict # value = {'TopOpeBRepDS_OK': (<TopOpeBRepDS_CheckStatus.TopOpeBRepDS_OK: 0>, None), 'TopOpeBRepDS_NOK': (<TopOpeBRepDS_CheckStatus.TopOpeBRepDS_NOK: 1>, None)}
    __members__: dict # value = {'TopOpeBRepDS_OK': <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_OK: 0>, 'TopOpeBRepDS_NOK': <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_NOK: 1>}
    pass
class TopOpeBRepDS_Config():
    """
    None

    Members:

      TopOpeBRepDS_UNSHGEOMETRY

      TopOpeBRepDS_SAMEORIENTED

      TopOpeBRepDS_DIFFORIENTED
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    TopOpeBRepDS_DIFFORIENTED: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_DIFFORIENTED: 2>
    TopOpeBRepDS_SAMEORIENTED: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_SAMEORIENTED: 1>
    TopOpeBRepDS_UNSHGEOMETRY: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_UNSHGEOMETRY: 0>
    __entries: dict # value = {'TopOpeBRepDS_UNSHGEOMETRY': (<TopOpeBRepDS_Config.TopOpeBRepDS_UNSHGEOMETRY: 0>, None), 'TopOpeBRepDS_SAMEORIENTED': (<TopOpeBRepDS_Config.TopOpeBRepDS_SAMEORIENTED: 1>, None), 'TopOpeBRepDS_DIFFORIENTED': (<TopOpeBRepDS_Config.TopOpeBRepDS_DIFFORIENTED: 2>, None)}
    __members__: dict # value = {'TopOpeBRepDS_UNSHGEOMETRY': <TopOpeBRepDS_Config.TopOpeBRepDS_UNSHGEOMETRY: 0>, 'TopOpeBRepDS_SAMEORIENTED': <TopOpeBRepDS_Config.TopOpeBRepDS_SAMEORIENTED: 1>, 'TopOpeBRepDS_DIFFORIENTED': <TopOpeBRepDS_Config.TopOpeBRepDS_DIFFORIENTED: 2>}
    pass
class TopOpeBRepDS_Curve():
    """
    A Geom curve and a tolerance.
    """
    def ChangeCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def ChangeDSIndex(self,I : int) -> None: 
        """
        None
        """
    def ChangeIsWalk(self,B : bool) -> None: 
        """
        None
        """
    def ChangeKeep(self,B : bool) -> None: 
        """
        None
        """
    def ChangeMother(self,I : int) -> None: 
        """
        None
        """
    def ChangeShape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def ChangeShape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Curve(self,C3D : OCP.Geom.Geom_Curve,Tol : float) -> None: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> OCP.Geom.Geom_Curve: ...
    @overload
    def Curve1(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def Curve1(self,PC1 : OCP.Geom2d.Geom2d_Curve) -> None: ...
    @overload
    def Curve2(self,PC2 : OCP.Geom2d.Geom2d_Curve) -> None: 
        """
        None

        None
        """
    @overload
    def Curve2(self) -> OCP.Geom2d.Geom2d_Curve: ...
    def DSIndex(self) -> int: 
        """
        None
        """
    def DefineCurve(self,P : OCP.Geom.Geom_Curve,T : float,IsWalk : bool) -> None: 
        """
        None
        """
    def GetSCI(self,I1 : TopOpeBRepDS_Interference,I2 : TopOpeBRepDS_Interference) -> Any: 
        """
        None
        """
    def GetSCI1(self) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    def GetSCI2(self) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    def GetShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def IsWalk(self) -> bool: 
        """
        None
        """
    def Keep(self) -> bool: 
        """
        None
        """
    def Mother(self) -> int: 
        """
        None
        """
    def Range(self,First : float,Last : float) -> bool: 
        """
        None
        """
    def SetRange(self,First : float,Last : float) -> None: 
        """
        None
        """
    def SetSCI(self,I1 : TopOpeBRepDS_Interference,I2 : TopOpeBRepDS_Interference) -> None: 
        """
        define the interferences face/curve.
        """
    def SetShapes(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Shape1(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Shape2(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    @overload
    def Tolerance(self) -> float: 
        """
        Update the tolerance

        None
        """
    @overload
    def Tolerance(self,tol : float) -> None: ...
    @overload
    def __init__(self,P : OCP.Geom.Geom_Curve,T : float,IsWalk : bool=False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_GeometryData():
    """
    mother-class of SurfaceData, CurveData, PointData
    """
    def AddInterference(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Assign(self,Other : TopOpeBRepDS_GeometryData) -> None: 
        """
        None
        """
    def ChangeInterferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Interferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def __init__(self,Other : TopOpeBRepDS_GeometryData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_CurveExplorer():
    """
    None
    """
    @overload
    def Curve(self,I : int) -> TopOpeBRepDS_Curve: 
        """
        None

        None
        """
    @overload
    def Curve(self) -> TopOpeBRepDS_Curve: ...
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: 
        """
        None
        """
    def IsCurve(self,I : int) -> bool: 
        """
        None
        """
    def IsCurveKeep(self,I : int) -> bool: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def NbCurve(self) -> int: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    @overload
    def __init__(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_InterferenceIterator():
    """
    Iterate on interferences of a list, matching conditions on interferences. Nota : inheritance of ListIteratorOfListOfInterference from TopOpeBRepDS has not been done because of the impossibility of naming the classical More, Next methods which are declared as static in TCollection_ListIteratorOfList ... . ListIteratorOfList has benn placed as a field of InterferenceIterator.
    """
    def ChangeIterator(self) -> Any: 
        """
        None
        """
    def Geometry(self,G : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry <G>
        """
    def GeometryKind(self,GK : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry Kind <ST>
        """
    def Init(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        re-initialize interference iteration process on the list of interference <L>. Conditions are not modified.
        """
    def Match(self) -> None: 
        """
        reach for an interference matching the conditions (if defined).
        """
    def MatchInterference(self,I : TopOpeBRepDS_Interference) -> bool: 
        """
        Returns True if the Interference <I> matches the conditions (if defined). If no conditions defined, returns True.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Interference in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Interference.
        """
    def Support(self,S : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support <S>
        """
    def SupportKind(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support Kind <ST>
        """
    def Value(self) -> TopOpeBRepDS_Interference: 
        """
        Returns the current Interference, matching the conditions (if defined).
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,L : TopOpeBRepDS_ListOfInterference) -> None: ...
    pass
class TopOpeBRepDS_Interference(OCP.Standard.Standard_Transient):
    """
    An interference is the description of the attachment of a new geometry on a geometry. For example an intersection point on an Edge or on a Curve.An interference is the description of the attachment of a new geometry on a geometry. For example an intersection point on an Edge or on a Curve.An interference is the description of the attachment of a new geometry on a geometry. For example an intersection point on an Edge or on a Curve.
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
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
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    @overload
    def __init__(self,Transition : TopOpeBRepDS_Transition,SupportType : TopOpeBRepDS_Kind,Support : int,GeometryType : TopOpeBRepDS_Kind,Geometry : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,I : TopOpeBRepDS_Interference) -> None: ...
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
class TopOpeBRepDS_DataMapOfCheckStatus(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfCheckStatus) -> TopOpeBRepDS_DataMapOfCheckStatus: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_CheckStatus) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_CheckStatus) -> TopOpeBRepDS_CheckStatus: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_CheckStatus: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_CheckStatus: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfCheckStatus) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_CheckStatus: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_CheckStatus) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_CheckStatus: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfCheckStatus) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataMapOfIntegerListOfInterference(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_ListOfInterference) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_ListOfInterference) -> TopOpeBRepDS_ListOfInterference: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_ListOfInterference) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataMapOfInterferenceListOfInterference(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfInterferenceListOfInterference) -> TopOpeBRepDS_DataMapOfInterferenceListOfInterference: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : TopOpeBRepDS_Interference,theItem : TopOpeBRepDS_ListOfInterference) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : TopOpeBRepDS_Interference,theItem : TopOpeBRepDS_ListOfInterference) -> TopOpeBRepDS_ListOfInterference: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfInterferenceListOfInterference) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : TopOpeBRepDS_Interference,theValue : TopOpeBRepDS_ListOfInterference) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: ...
    def IsBound(self,theKey : TopOpeBRepDS_Interference) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : TopOpeBRepDS_Interference) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfInterferenceListOfInterference) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataMapOfInterferenceShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfInterferenceShape) -> TopOpeBRepDS_DataMapOfInterferenceShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : TopOpeBRepDS_Interference,theItem : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : TopOpeBRepDS_Interference,theItem : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : TopOpeBRepDS_Interference) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : TopOpeBRepDS_Interference) -> OCP.TopoDS.TopoDS_Shape: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfInterferenceShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : TopOpeBRepDS_Interference,theValue : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : TopOpeBRepDS_Interference) -> OCP.TopoDS.TopoDS_Shape: ...
    def IsBound(self,theKey : TopOpeBRepDS_Interference) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : TopOpeBRepDS_Interference) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : TopOpeBRepDS_Interference) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfInterferenceShape) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ListOfShapeOn1State) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ListOfShapeOn1State) -> TopOpeBRepDS_ListOfShapeOn1State: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ListOfShapeOn1State: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ListOfShapeOn1State: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ListOfShapeOn1State: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepDS_ListOfShapeOn1State) -> bool: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ListOfShapeOn1State: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataMapOfShapeState(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_DataMapOfShapeState) -> TopOpeBRepDS_DataMapOfShapeState: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : OCP.TopAbs.TopAbs_State) -> OCP.TopAbs.TopAbs_State: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DataMapOfShapeState) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : OCP.TopAbs.TopAbs_State) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: ...
    def IsBound(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> OCP.TopAbs.TopAbs_State: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DataMapOfShapeState) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_DataStructure():
    """
    The DataStructure stores :
    """
    def AddCurve(self,S : TopOpeBRepDS_Curve) -> int: 
        """
        Insert a new curve. Returns the index.
        """
    def AddPoint(self,PDS : TopOpeBRepDS_Point) -> int: 
        """
        Insert a new point. Returns the index.
        """
    def AddPointSS(self,PDS : TopOpeBRepDS_Point,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Insert a new point. Returns the index.
        """
    def AddSectionEdge(self,E : OCP.TopoDS.TopoDS_Edge) -> int: 
        """
        None
        """
    @overload
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape,I : int) -> int: 
        """
        Insert a shape S. Returns the index.

        Insert a shape S which ancestor is I = 1 or 2. Returns the index.
        """
    @overload
    def AddShape(self,S : OCP.TopoDS.TopoDS_Shape) -> int: ...
    def AddShapeInterference(self,S : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def AddShapeSameDomain(self,S : OCP.TopoDS.TopoDS_Shape,SSD : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def AddSurface(self,S : TopOpeBRepDS_Surface) -> int: 
        """
        Insert a new surface. Returns the index.
        """
    @overload
    def AncestorRank(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        None

        None

        None

        None
        """
    @overload
    def AncestorRank(self,I : int) -> int: ...
    @overload
    def AncestorRank(self,I : int,Ianc : int) -> None: ...
    @overload
    def AncestorRank(self,S : OCP.TopoDS.TopoDS_Shape,Ianc : int) -> None: ...
    def ChangeCurve(self,I : int) -> TopOpeBRepDS_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def ChangeCurveInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def ChangeKeepCurve(self,C : TopOpeBRepDS_Curve,FindKeep : bool) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeKeepCurve(self,I : int,FindKeep : bool) -> None: ...
    @overload
    def ChangeKeepPoint(self,P : TopOpeBRepDS_Point,FindKeep : bool) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeKeepPoint(self,I : int,FindKeep : bool) -> None: ...
    @overload
    def ChangeKeepShape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeKeepShape(self,I : int,FindKeep : bool) -> None: ...
    @overload
    def ChangeKeepSurface(self,I : int,FindKeep : bool) -> None: 
        """
        None

        None
        """
    @overload
    def ChangeKeepSurface(self,S : TopOpeBRepDS_Surface,FindKeep : bool) -> None: ...
    def ChangeMapOfRejectedShapesObj(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None
        """
    def ChangeMapOfRejectedShapesTool(self) -> OCP.TopTools.TopTools_IndexedMapOfShape: 
        """
        None
        """
    def ChangeMapOfShapeWithState(self,aShape : OCP.TopoDS.TopoDS_Shape,aFlag : bool) -> TopOpeBRepDS_IndexedDataMapOfShapeWithState: 
        """
        None
        """
    def ChangeMapOfShapeWithStateObj(self) -> TopOpeBRepDS_IndexedDataMapOfShapeWithState: 
        """
        None
        """
    def ChangeMapOfShapeWithStateTool(self) -> TopOpeBRepDS_IndexedDataMapOfShapeWithState: 
        """
        None
        """
    def ChangeNbCurves(self,N : int) -> None: 
        """
        None
        """
    def ChangePoint(self,I : int) -> TopOpeBRepDS_Point: 
        """
        Returns the point of index <I>.
        """
    def ChangePointInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def ChangeShapeInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None

        None
        """
    @overload
    def ChangeShapeInterferences(self,S : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ListOfInterference: ...
    @overload
    def ChangeShapeSameDomain(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    @overload
    def ChangeShapeSameDomain(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: ...
    def ChangeShapes(self) -> TopOpeBRepDS_MapOfShapeData: 
        """
        None
        """
    def ChangeSurface(self,I : int) -> TopOpeBRepDS_Surface: 
        """
        Returns the surface of index <I>.
        """
    def ChangeSurfaceInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Curve(self,I : int) -> TopOpeBRepDS_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def CurveInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def FillShapesSameDomain(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,c1 : TopOpeBRepDS_Config,c2 : TopOpeBRepDS_Config,refFirst : bool=True) -> None: 
        """
        None

        None
        """
    @overload
    def FillShapesSameDomain(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,refFirst : bool=True) -> None: ...
    def GetShapeWithState(self,aShape : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: 
        """
        None
        """
    def HasGeometry(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <S> has new geometries, i.e : True si : HasShape(S) True S a une liste d'interferences non vide. S = SOLID, FACE, EDGE : true/false S = SHELL, WIRE, VERTEX : false.
        """
    def HasNewSurface(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def HasShape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> bool: 
        """
        Returns True if <S> est dans myShapes
        """
    def Init(self) -> None: 
        """
        reset the data structure
        """
    def InitSectionEdges(self) -> None: 
        """
        None
        """
    def IsSectionEdge(self,E : OCP.TopoDS.TopoDS_Edge,FindKeep : bool=True) -> bool: 
        """
        None
        """
    @overload
    def Isfafa(self) -> bool: 
        """
        None

        None
        """
    @overload
    def Isfafa(self,isfafa : bool) -> None: ...
    @overload
    def KeepCurve(self,I : int) -> bool: 
        """
        None

        None
        """
    @overload
    def KeepCurve(self,C : TopOpeBRepDS_Curve) -> bool: ...
    @overload
    def KeepPoint(self,P : TopOpeBRepDS_Point) -> bool: 
        """
        None

        None
        """
    @overload
    def KeepPoint(self,I : int) -> bool: ...
    @overload
    def KeepShape(self,I : int,FindKeep : bool=True) -> bool: 
        """
        None

        None
        """
    @overload
    def KeepShape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> bool: ...
    @overload
    def KeepSurface(self,S : TopOpeBRepDS_Surface) -> bool: 
        """
        None

        None
        """
    @overload
    def KeepSurface(self,I : int) -> bool: ...
    def NbCurves(self) -> int: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbSectionEdges(self) -> int: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        None
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    def Point(self,I : int) -> TopOpeBRepDS_Point: 
        """
        Returns the point of index <I>.
        """
    def PointInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def RemoveCurve(self,I : int) -> None: 
        """
        None
        """
    def RemovePoint(self,I : int) -> None: 
        """
        None
        """
    def RemoveShapeInterference(self,S : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def RemoveShapeSameDomain(self,S : OCP.TopoDS.TopoDS_Shape,SSD : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def RemoveSurface(self,I : int) -> None: 
        """
        None
        """
    @overload
    def SameDomainInd(self,I : int,Ind : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def SameDomainInd(self,S : OCP.TopoDS.TopoDS_Shape,Ind : int) -> None: ...
    @overload
    def SameDomainInd(self,S : OCP.TopoDS.TopoDS_Shape) -> int: ...
    @overload
    def SameDomainInd(self,I : int) -> int: ...
    @overload
    def SameDomainOri(self,I : int,Ori : TopOpeBRepDS_Config) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def SameDomainOri(self,S : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Config: ...
    @overload
    def SameDomainOri(self,I : int) -> TopOpeBRepDS_Config: ...
    @overload
    def SameDomainOri(self,S : OCP.TopoDS.TopoDS_Shape,Ori : TopOpeBRepDS_Config) -> None: ...
    @overload
    def SameDomainRef(self,I : int,Ref : int) -> None: 
        """
        None

        None

        None

        None
        """
    @overload
    def SameDomainRef(self,I : int) -> int: ...
    @overload
    def SameDomainRef(self,S : OCP.TopoDS.TopoDS_Shape) -> int: ...
    @overload
    def SameDomainRef(self,S : OCP.TopoDS.TopoDS_Shape,Ref : int) -> None: ...
    @overload
    def SectionEdge(self,E : OCP.TopoDS.TopoDS_Edge,FindKeep : bool=True) -> int: 
        """
        None

        None
        """
    @overload
    def SectionEdge(self,I : int,FindKeep : bool=True) -> OCP.TopoDS.TopoDS_Edge: ...
    def SetNewSurface(self,F : OCP.TopoDS.TopoDS_Shape,S : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    @overload
    def Shape(self,I : int,FindKeep : bool=True) -> OCP.TopoDS.TopoDS_Shape: 
        """
        returns the shape of index I stored in the map myShapes, accessing a list of interference.

        returns the index of shape <S> stored in the map myShapes, accessing a list of interference. returns 0 if <S> is not in the map.
        """
    @overload
    def Shape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> int: ...
    @overload
    def ShapeInterferences(self,I : int,FindKeep : bool=True) -> TopOpeBRepDS_ListOfInterference: 
        """
        None

        None
        """
    @overload
    def ShapeInterferences(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> TopOpeBRepDS_ListOfInterference: ...
    @overload
    def ShapeSameDomain(self,I : int) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None

        None
        """
    @overload
    def ShapeSameDomain(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: ...
    def Surface(self,I : int) -> TopOpeBRepDS_Surface: 
        """
        Returns the surface of index <I>.
        """
    def SurfaceInterferences(self,I : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def UnfillShapesSameDomain(self,S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_DoubleMapOfIntegerShape(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DoubleMap is used to bind pairs (Key1,Key2) and retrieve them in linear time.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def AreBound(self,theKey1 : int,theKey2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        * AreBound
        """
    def Assign(self,theOther : TopOpeBRepDS_DoubleMapOfIntegerShape) -> TopOpeBRepDS_DoubleMapOfIntegerShape: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey1 : int,theKey2 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Bind
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_DoubleMapOfIntegerShape) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find1(self,theKey1 : int,theKey2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Find the Key1 and return Key2 value. Raises an exception if Key1 was not bound.

        Find the Key1 and return Key2 value (by copying its value).
        """
    @overload
    def Find1(self,theKey1 : int) -> OCP.TopoDS.TopoDS_Shape: ...
    @overload
    def Find2(self,theKey2 : OCP.TopoDS.TopoDS_Shape,theKey1 : int) -> bool: 
        """
        Find the Key2 and return Key1 value. Raises an exception if Key2 was not bound.

        Find the Key2 and return Key1 value (by copying its value).
        """
    @overload
    def Find2(self,theKey2 : OCP.TopoDS.TopoDS_Shape) -> int: ...
    def IsBound1(self,theKey1 : int) -> bool: 
        """
        IsBound1
        """
    def IsBound2(self,theKey2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        IsBound2
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek1(self,theKey1 : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Find the Key1 and return pointer to Key2 or NULL if Key1 is not bound.
        """
    def Seek2(self,theKey2 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Find the Key2 and return pointer to Key1 or NULL if not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind1(self,theKey1 : int) -> bool: 
        """
        UnBind1
        """
    def UnBind2(self,theKey2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        UnBind2
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_DoubleMapOfIntegerShape) -> None: ...
    pass
class TopOpeBRepDS_Dumper():
    """
    None
    """
    @overload
    def SDumpRefOri(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SDumpRefOri(self,K : TopOpeBRepDS_Kind,I : int) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def SPrintShape(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SPrintShape(self,I : int) -> OCP.TCollection.TCollection_AsciiString: ...
    @overload
    def SPrintShapeRefOri(self,S : OCP.TopoDS.TopoDS_Shape,B : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None

        None
        """
    @overload
    def SPrintShapeRefOri(self,L : OCP.TopTools.TopTools_ListOfShape,B : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OCP.TCollection.TCollection_AsciiString: ...
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
    pass
class TopOpeBRepDS_EIR():
    """
    EdgeInterferenceReducer
    """
    @overload
    def ProcessEdgeInterferences(self) -> None: 
        """
        None

        None
        """
    @overload
    def ProcessEdgeInterferences(self,I : int) -> None: ...
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
    pass
class TopOpeBRepDS_Edge3dInterferenceTool():
    """
    a tool computing edge / face complex transition, Interferences of edge reference are given by I = (T on face, G = point or vertex, S = edge)
    """
    def Add(self,Eref : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Init(self,Eref : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def InitPointVertex(self,IsVertex : int,VonOO : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None
        """
    def Transition(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_EdgeInterferenceTool():
    """
    a tool computing complex transition on Edge.
    """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Shape,P : TopOpeBRepDS_Point,I : TopOpeBRepDS_Interference) -> None: 
        """
        None

        None
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Shape,V : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: ...
    def Init(self,E : OCP.TopoDS.TopoDS_Shape,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Transition(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_ShapeShapeInterference(TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    InterferenceInterferenceInterference
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
        """
    def Config(self) -> TopOpeBRepDS_Config: 
        """
        None
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
    def GBound(self) -> bool: 
        """
        None
        """
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def SetGBound(self,b : bool) -> None: 
        """
        None
        """
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    def __init__(self,T : TopOpeBRepDS_Transition,ST : TopOpeBRepDS_Kind,S : int,GT : TopOpeBRepDS_Kind,G : int,GBound : bool,C : TopOpeBRepDS_Config) -> None: ...
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
class TopOpeBRepDS_Explorer():
    """
    None
    """
    def Current(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        None
        """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,HDS : TopOpeBRepDS_HDataStructure,T : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE,findkeep : bool=True) -> None: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Type(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    def Vertex(self) -> OCP.TopoDS.TopoDS_Vertex: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure,T : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE,findkeep : bool=True) -> None: ...
    pass
class TopOpeBRepDS_FIR():
    """
    FaceInterferenceReducer
    """
    @overload
    def ProcessFaceInterferences(self,I : int,M : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: 
        """
        None

        None
        """
    @overload
    def ProcessFaceInterferences(self,M : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: ...
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
    pass
class TopOpeBRepDS_FaceEdgeInterference(TopOpeBRepDS_ShapeShapeInterference, TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    ShapeShapeInterferenceShapeShapeInterferenceShapeShapeInterference
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
        """
    def Config(self) -> TopOpeBRepDS_Config: 
        """
        None
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
    def GBound(self) -> bool: 
        """
        None
        """
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def SetGBound(self,b : bool) -> None: 
        """
        None
        """
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    def __init__(self,T : TopOpeBRepDS_Transition,S : int,G : int,GIsBound : bool,C : TopOpeBRepDS_Config) -> None: ...
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
class TopOpeBRepDS_FaceInterferenceTool():
    """
    a tool computing complex transition on Face.
    """
    @overload
    def Add(self,FI : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,Eisnew : bool,I : TopOpeBRepDS_Interference) -> None: 
        """
        Eisnew = true if E is a new edge built on edge I->Geometry() false if E is shape <=> I->Geometry()

        None
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Shape,C : TopOpeBRepDS_Curve,I : TopOpeBRepDS_Interference) -> None: ...
    def GetEdgePntPar(self,P : OCP.gp.gp_Pnt) -> Tuple[float]: 
        """
        None
        """
    def Init(self,FI : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,Eisnew : bool,I : TopOpeBRepDS_Interference) -> None: 
        """
        Eisnew = true if E is a new edge built on edge I->Geometry() false if E is shape <=> I->Geometry()
        """
    def IsEdgePntParDef(self) -> bool: 
        """
        None
        """
    def SetEdgePntPar(self,P : OCP.gp.gp_Pnt,par : float) -> None: 
        """
        None
        """
    def Transition(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    pass
class TopOpeBRepDS_Filter():
    """
    None
    """
    @overload
    def ProcessCurveInterferences(self) -> None: 
        """
        None

        None
        """
    @overload
    def ProcessCurveInterferences(self,I : int) -> None: ...
    @overload
    def ProcessEdgeInterferences(self,I : int) -> None: 
        """
        None

        None
        """
    @overload
    def ProcessEdgeInterferences(self) -> None: ...
    @overload
    def ProcessFaceInterferences(self,MEsp : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: 
        """
        None

        None
        """
    @overload
    def ProcessFaceInterferences(self,I : int,MEsp : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: ...
    def ProcessInterferences(self) -> None: 
        """
        None
        """
    pass
class TopOpeBRepDS_GapFiller():
    """
    None
    """
    def AddPointsOnConnexShape(self,F : OCP.TopoDS.TopoDS_Shape,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        Methodes pour reduire la liste des Points qui peuvent correspondre a une Point donne.
        """
    def AddPointsOnShape(self,S : OCP.TopoDS.TopoDS_Shape,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def BuildNewGeometries(self) -> None: 
        """
        None
        """
    def CheckConnexity(self,LI : TopOpeBRepDS_ListOfInterference) -> bool: 
        """
        Enchaine les sections via les points d'Interferences deja associe; Renvoit dans <L> les points extremites des Lignes. Methodes pour construire la liste des Points qui peuvent correspondre a une Point donne.
        """
    def FilterByEdge(self,E : OCP.TopoDS.TopoDS_Edge,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def FilterByFace(self,F : OCP.TopoDS.TopoDS_Face,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def FilterByIncidentDistance(self,F : OCP.TopoDS.TopoDS_Face,I : TopOpeBRepDS_Interference,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def FindAssociatedPoints(self,I : TopOpeBRepDS_Interference,LI : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        Recherche parmi l'ensemble des points d'Interference la Liste <LI> des points qui correspondent au point d'indice <Index>
        """
    def IsOnEdge(self,I : TopOpeBRepDS_Interference,E : OCP.TopoDS.TopoDS_Edge) -> bool: 
        """
        Return TRUE si I ou une de ses representaions a pour support <E>. Methodes de reconstructions des geometries des point et des courbes de section
        """
    def IsOnFace(self,I : TopOpeBRepDS_Interference,F : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        Return TRUE si I a ete obtenu par une intersection avec <F>.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def ReBuildGeom(self,I1 : TopOpeBRepDS_Interference,Done : OCP.TColStd.TColStd_MapOfInteger) -> None: 
        """
        None
        """
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
    pass
class TopOpeBRepDS_GapTool(OCP.Standard.Standard_Transient):
    def ChangeSameInterferences(self,I : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Curve(self,I : TopOpeBRepDS_Interference,C : TopOpeBRepDS_Curve) -> bool: 
        """
        None
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
    def EdgeSupport(self,I : TopOpeBRepDS_Interference,E : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def FacesSupport(self,I : TopOpeBRepDS_Interference,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Return les faces qui ont genere la section origine de I
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,HDS : TopOpeBRepDS_HDataStructure) -> None: 
        """
        None
        """
    def Interferences(self,IndexPoint : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
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
    def ParameterOnEdge(self,I : TopOpeBRepDS_Interference,E : OCP.TopoDS.TopoDS_Shape,U : float) -> bool: 
        """
        None
        """
    def SameInterferences(self,I : TopOpeBRepDS_Interference) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def SetParameterOnEdge(self,I : TopOpeBRepDS_Interference,E : OCP.TopoDS.TopoDS_Shape,U : float) -> None: 
        """
        None
        """
    def SetPoint(self,I : TopOpeBRepDS_Interference,IndexPoint : int) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
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
class TopOpeBRepDS_CurveData(TopOpeBRepDS_GeometryData):
    """
    None
    """
    def AddInterference(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Assign(self,Other : TopOpeBRepDS_GeometryData) -> None: 
        """
        None
        """
    def ChangeInterferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Interferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def __init__(self,C : TopOpeBRepDS_Curve) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_HArray1OfDataMapOfIntegerListOfInterference(TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference, OCP.Standard.Standard_Transient):
    def Array1(self) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        None
        """
    def Assign(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        None
        """
    def ChangeFirst(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns first element
        """
    def ChangeLast(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Variable value access
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
    def First(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
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
    def Last(self) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> TopOpeBRepDS_DataMapOfIntegerListOfInterference: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : TopOpeBRepDS_DataMapOfIntegerListOfInterference) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_Array1OfDataMapOfIntegerListOfInterference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class TopOpeBRepDS_HDataStructure(OCP.Standard.Standard_Transient):
    @overload
    def AddAncestors(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        Update the data structure with shapes of type T1 containing a subshape of type T2 which is stored in the DS. Used by the previous one.
        """
    @overload
    def AddAncestors(self,S : OCP.TopoDS.TopoDS_Shape,T1 : OCP.TopAbs.TopAbs_ShapeEnum,T2 : OCP.TopAbs.TopAbs_ShapeEnum) -> None: ...
    def ChangeCurve(self,I : int) -> TopOpeBRepDS_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def ChangeDS(self) -> TopOpeBRepDS_DataStructure: 
        """
        None
        """
    def ChkIntg(self) -> None: 
        """
        Check the integrity of the DS
        """
    @overload
    def ClearStoreInterferences(self,LI : TopOpeBRepDS_ListOfInterference,IS : int,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None
        """
    @overload
    def ClearStoreInterferences(self,LI : TopOpeBRepDS_ListOfInterference,S : OCP.TopoDS.TopoDS_Shape,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    def Curve(self,I : int) -> TopOpeBRepDS_Curve: 
        """
        Returns the Curve of index <I>.
        """
    def CurvePoints(self,I : int) -> TopOpeBRepDS_PointIterator: 
        """
        Returns an iterator on the points on the curve <I>.
        """
    def DS(self) -> TopOpeBRepDS_DataStructure: 
        """
        None
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
    def EdgePoints(self,E : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_PointIterator: 
        """
        Returns an iterator on the points attached to the edge <E>.
        """
    def EdgesSameParameter(self) -> bool: 
        """
        returns True if all the edges stored as shapes in the DS are SameParameter, otherwise False.
        """
    @overload
    def FaceCurves(self,F : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_CurveIterator: 
        """
        Returns an iterator on the curves attached to the face <F>.

        Returns an iterator on the curves attached to the face <I>.
        """
    @overload
    def FaceCurves(self,I : int) -> TopOpeBRepDS_CurveIterator: ...
    def GetGeometry(self,IT : Any,PDS : TopOpeBRepDS_Point,G : int,K : TopOpeBRepDS_Kind) -> bool: 
        """
        Get the geometry of a DS point <PDS>. Search for it with ScanInterfList (previous method). if found, set <G,K> to the geometry,kind of the interference found. returns the value of ScanInterfList().
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasGeometry(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns True if <S> has new geometries.
        """
    def HasSameDomain(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> bool: 
        """
        Returns True if <S> share a geometrical domain with some other shapes.
        """
    def HasShape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> bool: 
        """
        Returns True if <S> has new geometries (SOLID,FACE,EDGE) or if <S> (SHELL,WIRE) has sub-shape (FACE,EDGE) with new geometries
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
    def MakeCurve(self,C1 : TopOpeBRepDS_Curve,C2 : TopOpeBRepDS_Curve) -> int: 
        """
        None
        """
    def MinMaxOnParameter(self,L : TopOpeBRepDS_ListOfInterference) -> Tuple[float, float]: 
        """
        None
        """
    def NbCurves(self) -> int: 
        """
        None
        """
    def NbGeometry(self,K : TopOpeBRepDS_Kind) -> int: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        None
        """
    def NbShapes(self) -> int: 
        """
        None
        """
    def NbSurfaces(self) -> int: 
        """
        None
        """
    @overload
    def NbTopology(self,K : TopOpeBRepDS_Kind) -> int: 
        """
        None

        None
        """
    @overload
    def NbTopology(self) -> int: ...
    def Point(self,I : int) -> TopOpeBRepDS_Point: 
        """
        Returns the point of index <I>.
        """
    def RemoveCurve(self,iC : int) -> None: 
        """
        None
        """
    def SameDomain(self,S : OCP.TopoDS.TopoDS_Shape) -> Any: 
        """
        Returns an iterator on the SameDomain shapes attached to the shape <S>.
        """
    def SameDomainOrientation(self,S : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Config: 
        """
        Returns orientation of shape <S> compared with its reference shape
        """
    def SameDomainReference(self,S : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Returns orientation of shape <S> compared with its reference shape
        """
    def ScanInterfList(self,IT : Any,PDS : TopOpeBRepDS_Point) -> bool: 
        """
        Search, among a list of interferences accessed by the iterator <IT>, a geometry <G> whose 3D point is identical to the 3D point of the TheDSPoint <PDS>. returns True if such an interference has been found, False else. if True, iterator It points (by the Value() method) on the first interference accessing an identical 3D point.
        """
    @overload
    def Shape(self,I : int,FindKeep : bool=True) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the shape of index <I> in the DS

        Returns the index of shape <S> in the DS returns 0 if <S> is not in the DS
        """
    @overload
    def Shape(self,S : OCP.TopoDS.TopoDS_Shape,FindKeep : bool=True) -> int: ...
    @overload
    def SolidSurfaces(self,S : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_SurfaceIterator: 
        """
        Returns an iterator on the surfaces attached to the solid <S>.

        Returns an iterator on the surfaces attached to the solid <I>.
        """
    @overload
    def SolidSurfaces(self,I : int) -> TopOpeBRepDS_SurfaceIterator: ...
    @overload
    def SortOnParameter(self,L1 : TopOpeBRepDS_ListOfInterference,L2 : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None

        None
        """
    @overload
    def SortOnParameter(self,L : TopOpeBRepDS_ListOfInterference) -> None: ...
    @overload
    def StoreInterference(self,I : TopOpeBRepDS_Interference,LI : TopOpeBRepDS_ListOfInterference,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Add interference <I> to list <LI>.

        Add interference <I> to list of interference of shape <S>.

        Add interference <I> to list of interference of shape <IS>.
        """
    @overload
    def StoreInterference(self,I : TopOpeBRepDS_Interference,IS : int,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def StoreInterference(self,I : TopOpeBRepDS_Interference,S : OCP.TopoDS.TopoDS_Shape,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def StoreInterferences(self,LI : TopOpeBRepDS_ListOfInterference,IS : int,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None

        None
        """
    @overload
    def StoreInterferences(self,LI : TopOpeBRepDS_ListOfInterference,S : OCP.TopoDS.TopoDS_Shape,str : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
    def Surface(self,I : int) -> TopOpeBRepDS_Surface: 
        """
        Returns the surface of index <I>.
        """
    def SurfaceCurves(self,I : int) -> TopOpeBRepDS_CurveIterator: 
        """
        Returns an iterator on the curves on the surface <I>.
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
class TopOpeBRepDS_IndexedDataMapOfShapeWithState(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ShapeWithState) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_IndexedDataMapOfShapeWithState) -> TopOpeBRepDS_IndexedDataMapOfShapeWithState: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopOpeBRepDS_ShapeWithState: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepDS_IndexedDataMapOfShapeWithState) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopOpeBRepDS_ShapeWithState: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepDS_ShapeWithState) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeWithState: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ShapeWithState) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_IndexedDataMapOfShapeWithState) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_IndexedDataMapOfVertexPoint(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_Point) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_IndexedDataMapOfVertexPoint) -> TopOpeBRepDS_IndexedDataMapOfVertexPoint: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopOpeBRepDS_Point: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Point: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Point: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepDS_IndexedDataMapOfVertexPoint) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopOpeBRepDS_Point: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Point: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepDS_Point) -> bool: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_Point: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_Point) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_IndexedDataMapOfVertexPoint) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_CurvePointInterference(TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    An interference with a parameter.An interference with a parameter.An interference with a parameter.
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
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
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def Parameter(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter(self) -> float: ...
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    def __init__(self,T : TopOpeBRepDS_Transition,ST : TopOpeBRepDS_Kind,S : int,GT : TopOpeBRepDS_Kind,G : int,P : float) -> None: ...
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
class TopOpeBRepDS_CurveIterator(TopOpeBRepDS_InterferenceIterator):
    """
    None
    """
    def ChangeIterator(self) -> Any: 
        """
        None
        """
    def Current(self) -> int: 
        """
        Index of the curve in the data structure.
        """
    def Geometry(self,G : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry <G>
        """
    def GeometryKind(self,GK : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry Kind <ST>
        """
    def Init(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        re-initialize interference iteration process on the list of interference <L>. Conditions are not modified.
        """
    def Match(self) -> None: 
        """
        reach for an interference matching the conditions (if defined).
        """
    def MatchInterference(self,I : TopOpeBRepDS_Interference) -> bool: 
        """
        Returns True if the Interference <I> has a GeometryType() TopOpeBRepDS_CURVE returns False else.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Interference in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Interference.
        """
    def Orientation(self,S : OCP.TopAbs.TopAbs_State) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None
        """
    def Support(self,S : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support <S>
        """
    def SupportKind(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support Kind <ST>
        """
    def Value(self) -> TopOpeBRepDS_Interference: 
        """
        Returns the current Interference, matching the conditions (if defined).
        """
    def __init__(self,L : TopOpeBRepDS_ListOfInterference) -> None: ...
    pass
class TopOpeBRepDS_InterferenceTool():
    """
    None
    """
    @staticmethod
    def DuplicateCurvePointInterference_s(I : TopOpeBRepDS_Interference) -> TopOpeBRepDS_Interference: 
        """
        duplicate I in a new interference with Complement() transition.
        """
    @staticmethod
    def MakeCurveInterference_s(T : TopOpeBRepDS_Transition,SK : TopOpeBRepDS_Kind,SI : int,GK : TopOpeBRepDS_Kind,GI : int,P : float) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    def MakeEdgeInterference_s(T : TopOpeBRepDS_Transition,SK : TopOpeBRepDS_Kind,SI : int,GK : TopOpeBRepDS_Kind,GI : int,P : float) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    def MakeEdgeVertexInterference_s(Transition : TopOpeBRepDS_Transition,EdgeI : int,VertexI : int,VertexIsBound : bool,Config : TopOpeBRepDS_Config,param : float) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    def MakeFaceCurveInterference_s(Transition : TopOpeBRepDS_Transition,FaceI : int,CurveI : int,PC : OCP.Geom2d.Geom2d_Curve) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    def MakeFaceEdgeInterference_s(Transition : TopOpeBRepDS_Transition,FaceI : int,EdgeI : int,EdgeIsBound : bool,Config : TopOpeBRepDS_Config) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    def MakeSolidSurfaceInterference_s(Transition : TopOpeBRepDS_Transition,SolidI : int,SurfaceI : int) -> TopOpeBRepDS_Interference: 
        """
        None
        """
    @staticmethod
    @overload
    def Parameter_s(CPI : TopOpeBRepDS_Interference) -> float: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def Parameter_s(CPI : TopOpeBRepDS_Interference,Par : float) -> None: ...
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_Kind():
    """
    different types of objects in DataStructure

    Members:

      TopOpeBRepDS_POINT

      TopOpeBRepDS_CURVE

      TopOpeBRepDS_SURFACE

      TopOpeBRepDS_VERTEX

      TopOpeBRepDS_EDGE

      TopOpeBRepDS_WIRE

      TopOpeBRepDS_FACE

      TopOpeBRepDS_SHELL

      TopOpeBRepDS_SOLID

      TopOpeBRepDS_COMPSOLID

      TopOpeBRepDS_COMPOUND

      TopOpeBRepDS_UNKNOWN
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
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
    TopOpeBRepDS_COMPOUND: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPOUND: 10>
    TopOpeBRepDS_COMPSOLID: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPSOLID: 9>
    TopOpeBRepDS_CURVE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_CURVE: 1>
    TopOpeBRepDS_EDGE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_EDGE: 4>
    TopOpeBRepDS_FACE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_FACE: 6>
    TopOpeBRepDS_POINT: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_POINT: 0>
    TopOpeBRepDS_SHELL: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SHELL: 7>
    TopOpeBRepDS_SOLID: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SOLID: 8>
    TopOpeBRepDS_SURFACE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SURFACE: 2>
    TopOpeBRepDS_UNKNOWN: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_UNKNOWN: 11>
    TopOpeBRepDS_VERTEX: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_VERTEX: 3>
    TopOpeBRepDS_WIRE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_WIRE: 5>
    __entries: dict # value = {'TopOpeBRepDS_POINT': (<TopOpeBRepDS_Kind.TopOpeBRepDS_POINT: 0>, None), 'TopOpeBRepDS_CURVE': (<TopOpeBRepDS_Kind.TopOpeBRepDS_CURVE: 1>, None), 'TopOpeBRepDS_SURFACE': (<TopOpeBRepDS_Kind.TopOpeBRepDS_SURFACE: 2>, None), 'TopOpeBRepDS_VERTEX': (<TopOpeBRepDS_Kind.TopOpeBRepDS_VERTEX: 3>, None), 'TopOpeBRepDS_EDGE': (<TopOpeBRepDS_Kind.TopOpeBRepDS_EDGE: 4>, None), 'TopOpeBRepDS_WIRE': (<TopOpeBRepDS_Kind.TopOpeBRepDS_WIRE: 5>, None), 'TopOpeBRepDS_FACE': (<TopOpeBRepDS_Kind.TopOpeBRepDS_FACE: 6>, None), 'TopOpeBRepDS_SHELL': (<TopOpeBRepDS_Kind.TopOpeBRepDS_SHELL: 7>, None), 'TopOpeBRepDS_SOLID': (<TopOpeBRepDS_Kind.TopOpeBRepDS_SOLID: 8>, None), 'TopOpeBRepDS_COMPSOLID': (<TopOpeBRepDS_Kind.TopOpeBRepDS_COMPSOLID: 9>, None), 'TopOpeBRepDS_COMPOUND': (<TopOpeBRepDS_Kind.TopOpeBRepDS_COMPOUND: 10>, None), 'TopOpeBRepDS_UNKNOWN': (<TopOpeBRepDS_Kind.TopOpeBRepDS_UNKNOWN: 11>, None)}
    __members__: dict # value = {'TopOpeBRepDS_POINT': <TopOpeBRepDS_Kind.TopOpeBRepDS_POINT: 0>, 'TopOpeBRepDS_CURVE': <TopOpeBRepDS_Kind.TopOpeBRepDS_CURVE: 1>, 'TopOpeBRepDS_SURFACE': <TopOpeBRepDS_Kind.TopOpeBRepDS_SURFACE: 2>, 'TopOpeBRepDS_VERTEX': <TopOpeBRepDS_Kind.TopOpeBRepDS_VERTEX: 3>, 'TopOpeBRepDS_EDGE': <TopOpeBRepDS_Kind.TopOpeBRepDS_EDGE: 4>, 'TopOpeBRepDS_WIRE': <TopOpeBRepDS_Kind.TopOpeBRepDS_WIRE: 5>, 'TopOpeBRepDS_FACE': <TopOpeBRepDS_Kind.TopOpeBRepDS_FACE: 6>, 'TopOpeBRepDS_SHELL': <TopOpeBRepDS_Kind.TopOpeBRepDS_SHELL: 7>, 'TopOpeBRepDS_SOLID': <TopOpeBRepDS_Kind.TopOpeBRepDS_SOLID: 8>, 'TopOpeBRepDS_COMPSOLID': <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPSOLID: 9>, 'TopOpeBRepDS_COMPOUND': <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPOUND: 10>, 'TopOpeBRepDS_UNKNOWN': <TopOpeBRepDS_Kind.TopOpeBRepDS_UNKNOWN: 11>}
    pass
class TopOpeBRepDS_ListOfInterference(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopOpeBRepDS_Interference,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : TopOpeBRepDS_ListOfInterference) -> None: ...
    @overload
    def Append(self,theItem : TopOpeBRepDS_Interference) -> TopOpeBRepDS_Interference: ...
    def Assign(self,theOther : TopOpeBRepDS_ListOfInterference) -> TopOpeBRepDS_ListOfInterference: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> TopOpeBRepDS_Interference: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopOpeBRepDS_Interference,theIter : Any) -> TopOpeBRepDS_Interference: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopOpeBRepDS_ListOfInterference,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : TopOpeBRepDS_Interference,theIter : Any) -> TopOpeBRepDS_Interference: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopOpeBRepDS_ListOfInterference,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopOpeBRepDS_Interference: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : TopOpeBRepDS_Interference) -> TopOpeBRepDS_Interference: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : TopOpeBRepDS_ListOfInterference) -> None: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_ListOfInterference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_ListOfShapeOn1State():
    """
    represent a list of shape
    """
    def ChangeListOnState(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def IsSplit(self) -> bool: 
        """
        None
        """
    def ListOnState(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def Split(self,B : bool=True) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_MapOfCurve(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_MapOfCurve) -> TopOpeBRepDS_MapOfCurve: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_CurveData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_CurveData) -> TopOpeBRepDS_CurveData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_CurveData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_CurveData: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_MapOfCurve) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_CurveData: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_CurveData) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_CurveData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_MapOfCurve) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_MapOfIntegerShapeData(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_MapOfIntegerShapeData) -> TopOpeBRepDS_MapOfIntegerShapeData: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_ShapeData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_ShapeData) -> TopOpeBRepDS_ShapeData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_ShapeData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_ShapeData: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_MapOfIntegerShapeData) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_ShapeData: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_ShapeData) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_ShapeData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_MapOfIntegerShapeData) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_MapOfPoint(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_MapOfPoint) -> TopOpeBRepDS_MapOfPoint: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_PointData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_PointData) -> TopOpeBRepDS_PointData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_PointData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_PointData: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_MapOfPoint) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_PointData: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_PointData) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_PointData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theOther : TopOpeBRepDS_MapOfPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_MapOfShapeData(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ShapeData) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_MapOfShapeData) -> TopOpeBRepDS_MapOfShapeData: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> TopOpeBRepDS_ShapeData: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeData: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeData: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : TopOpeBRepDS_MapOfShapeData) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> TopOpeBRepDS_ShapeData: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : TopOpeBRepDS_ShapeData) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeData: ...
    def FindIndex(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> TopOpeBRepDS_ShapeData: 
        """
        Seek returns pointer to Item by Key. Returns NULL if Key was not found.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : TopOpeBRepDS_ShapeData) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_MapOfShapeData) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_MapOfSurface(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : TopOpeBRepDS_MapOfSurface) -> TopOpeBRepDS_MapOfSurface: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : TopOpeBRepDS_SurfaceData) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : TopOpeBRepDS_SurfaceData) -> TopOpeBRepDS_SurfaceData: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> TopOpeBRepDS_SurfaceData: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> TopOpeBRepDS_SurfaceData: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : TopOpeBRepDS_MapOfSurface) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : TopOpeBRepDS_SurfaceData) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> TopOpeBRepDS_SurfaceData: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> TopOpeBRepDS_SurfaceData: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopOpeBRepDS_MapOfSurface) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class TopOpeBRepDS_Marker(OCP.Standard.Standard_Transient):
    def Allocate(self,n : int) -> None: 
        """
        None
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
    def GetI(self,i : int) -> bool: 
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
    def Reset(self) -> None: 
        """
        None
        """
    @overload
    def Set(self,i : int,b : bool) -> None: 
        """
        None

        None
        """
    @overload
    def Set(self,b : bool,n : int,a : capsule) -> None: ...
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
class TopOpeBRepDS_Point():
    """
    A Geom point and a tolerance.
    """
    def ChangeKeep(self,B : bool) -> None: 
        """
        None
        """
    def ChangePoint(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def IsEqual(self,other : TopOpeBRepDS_Point) -> bool: 
        """
        None
        """
    def Keep(self) -> bool: 
        """
        None
        """
    def Point(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    @overload
    def Tolerance(self,Tol : float) -> None: 
        """
        None

        None
        """
    @overload
    def Tolerance(self) -> float: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,T : float) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class TopOpeBRepDS_PointData(TopOpeBRepDS_GeometryData):
    """
    None
    """
    def AddInterference(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Assign(self,Other : TopOpeBRepDS_GeometryData) -> None: 
        """
        None
        """
    def ChangeInterferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def GetShapes(self) -> Tuple[int, int]: 
        """
        None
        """
    def Interferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def SetShapes(self,I1 : int,I2 : int) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : TopOpeBRepDS_Point) -> None: ...
    @overload
    def __init__(self,P : TopOpeBRepDS_Point,I1 : int,I2 : int) -> None: ...
    pass
class TopOpeBRepDS_PointExplorer():
    """
    None
    """
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: 
        """
        None
        """
    def IsPoint(self,I : int) -> bool: 
        """
        None
        """
    def IsPointKeep(self,I : int) -> bool: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def NbPoint(self) -> int: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    @overload
    def Point(self,I : int) -> TopOpeBRepDS_Point: 
        """
        None

        None
        """
    @overload
    def Point(self) -> TopOpeBRepDS_Point: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: ...
    pass
class TopOpeBRepDS_PointIterator(TopOpeBRepDS_InterferenceIterator):
    """
    None
    """
    def ChangeIterator(self) -> Any: 
        """
        None
        """
    def Current(self) -> int: 
        """
        Index of the point in the data structure.
        """
    def DiffOriented(self) -> bool: 
        """
        None
        """
    def Geometry(self,G : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry <G>
        """
    def GeometryKind(self,GK : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry Kind <ST>
        """
    def Init(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        re-initialize interference iteration process on the list of interference <L>. Conditions are not modified.
        """
    def IsPoint(self) -> bool: 
        """
        None
        """
    def IsVertex(self) -> bool: 
        """
        None
        """
    def Match(self) -> None: 
        """
        reach for an interference matching the conditions (if defined).
        """
    def MatchInterference(self,I : TopOpeBRepDS_Interference) -> bool: 
        """
        Returns True if the Interference <I> has a GeometryType() TopOpeBRepDS_POINT or TopOpeBRepDS_VERTEX returns False else.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Interference in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Interference.
        """
    def Orientation(self,S : OCP.TopAbs.TopAbs_State) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Parameter(self) -> float: 
        """
        None
        """
    def SameOriented(self) -> bool: 
        """
        None
        """
    def Support(self) -> int: 
        """
        None
        """
    def SupportKind(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support Kind <ST>
        """
    def Value(self) -> TopOpeBRepDS_Interference: 
        """
        Returns the current Interference, matching the conditions (if defined).
        """
    def __init__(self,L : TopOpeBRepDS_ListOfInterference) -> None: ...
    pass
class TopOpeBRepDS_Reducer():
    """
    reduce interferences of a data structure (HDS) used in topological operations.
    """
    def ProcessEdgeInterferences(self) -> None: 
        """
        None
        """
    def ProcessFaceInterferences(self,M : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None: 
        """
        None
        """
    def __init__(self,HDS : TopOpeBRepDS_HDataStructure) -> None: ...
    pass
class TopOpeBRepDS_ShapeData():
    """
    None
    """
    def ChangeInterferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def ChangeKeep(self,B : bool) -> None: 
        """
        None
        """
    def Interferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Keep(self) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_EdgeVertexInterference(TopOpeBRepDS_ShapeShapeInterference, TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    An interference with a parameter (ShapeShapeInterference).An interference with a parameter (ShapeShapeInterference).An interference with a parameter (ShapeShapeInterference).
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
        """
    def Config(self) -> TopOpeBRepDS_Config: 
        """
        None
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
    def GBound(self) -> bool: 
        """
        None
        """
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def Parameter(self,P : float) -> None: 
        """
        None

        None
        """
    @overload
    def Parameter(self) -> float: ...
    def SetGBound(self,b : bool) -> None: 
        """
        None
        """
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    @overload
    def __init__(self,T : TopOpeBRepDS_Transition,ST : TopOpeBRepDS_Kind,S : int,G : int,GIsBound : bool,C : TopOpeBRepDS_Config,P : float) -> None: ...
    @overload
    def __init__(self,T : TopOpeBRepDS_Transition,S : int,G : int,GIsBound : bool,C : TopOpeBRepDS_Config,P : float) -> None: ...
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
class TopOpeBRepDS_ShapeWithState():
    """
    None
    """
    def AddPart(self,aShape : OCP.TopoDS.TopoDS_Shape,aState : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def AddParts(self,aListOfShape : OCP.TopTools.TopTools_ListOfShape,aState : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def IsSplitted(self) -> bool: 
        """
        None
        """
    def Part(self,aState : OCP.TopAbs.TopAbs_State) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        None
        """
    def SetIsSplitted(self,anIsSplitted : bool) -> None: 
        """
        None
        """
    def SetState(self,aState : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_SolidSurfaceInterference(TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    InterferenceInterferenceInterference
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
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
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    def __init__(self,Transition : TopOpeBRepDS_Transition,SupportType : TopOpeBRepDS_Kind,Support : int,GeometryType : TopOpeBRepDS_Kind,Geometry : int) -> None: ...
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
class TopOpeBRepDS_Surface():
    """
    A Geom surface and a tolerance.
    """
    def Assign(self,Other : TopOpeBRepDS_Surface) -> None: 
        """
        None
        """
    def ChangeKeep(self,theToKeep : bool) -> None: 
        """
        None
        """
    def Keep(self) -> bool: 
        """
        None
        """
    def Surface(self) -> OCP.Geom.Geom_Surface: 
        """
        None
        """
    @overload
    def Tolerance(self,theTol : float) -> None: 
        """
        None

        Update the tolerance
        """
    @overload
    def Tolerance(self) -> float: ...
    @overload
    def __init__(self,Other : TopOpeBRepDS_Surface) -> None: ...
    @overload
    def __init__(self,P : OCP.Geom.Geom_Surface,T : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_SurfaceCurveInterference(TopOpeBRepDS_Interference, OCP.Standard.Standard_Transient):
    """
    an interference with a 2d curvean interference with a 2d curvean interference with a 2d curve
    """
    def ChangeTransition(self) -> TopOpeBRepDS_Transition: 
        """
        None
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
    def GKGSKS(self,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind) -> Tuple[int, int]: 
        """
        return GeometryType + Geometry + SupportType + Support
        """
    @overload
    def Geometry(self) -> int: 
        """
        None

        None
        """
    @overload
    def Geometry(self,G : int) -> None: ...
    @overload
    def GeometryType(self) -> TopOpeBRepDS_Kind: 
        """
        None

        None
        """
    @overload
    def GeometryType(self,GT : TopOpeBRepDS_Kind) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasSameGeometry(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
        """
    def HasSameSupport(self,Other : TopOpeBRepDS_Interference) -> bool: 
        """
        None
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
    def PCurve(self) -> OCP.Geom2d.Geom2d_Curve: 
        """
        None

        None
        """
    @overload
    def PCurve(self,PC : OCP.Geom2d.Geom2d_Curve) -> None: ...
    def SetGeometry(self,GI : int) -> None: 
        """
        None
        """
    @overload
    def Support(self,S : int) -> None: 
        """
        None

        None
        """
    @overload
    def Support(self) -> int: ...
    @overload
    def SupportType(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        None

        None
        """
    @overload
    def SupportType(self) -> TopOpeBRepDS_Kind: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Transition(self,T : TopOpeBRepDS_Transition) -> None: 
        """
        None

        None
        """
    @overload
    def Transition(self) -> TopOpeBRepDS_Transition: ...
    @overload
    def __init__(self,I : TopOpeBRepDS_Interference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Transition : TopOpeBRepDS_Transition,SupportType : TopOpeBRepDS_Kind,Support : int,GeometryType : TopOpeBRepDS_Kind,Geometry : int,PC : OCP.Geom2d.Geom2d_Curve) -> None: ...
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
class TopOpeBRepDS_SurfaceData(TopOpeBRepDS_GeometryData):
    """
    None
    """
    def AddInterference(self,I : TopOpeBRepDS_Interference) -> None: 
        """
        None
        """
    def Assign(self,Other : TopOpeBRepDS_GeometryData) -> None: 
        """
        None
        """
    def ChangeInterferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Interferences(self) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    @overload
    def __init__(self,S : TopOpeBRepDS_Surface) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_SurfaceExplorer():
    """
    None
    """
    def Index(self) -> int: 
        """
        None
        """
    def Init(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: 
        """
        None
        """
    def IsSurface(self,I : int) -> bool: 
        """
        None
        """
    def IsSurfaceKeep(self,I : int) -> bool: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def NbSurface(self) -> int: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    @overload
    def Surface(self,I : int) -> TopOpeBRepDS_Surface: 
        """
        None

        None
        """
    @overload
    def Surface(self) -> TopOpeBRepDS_Surface: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,DS : TopOpeBRepDS_DataStructure,FindOnlyKeep : bool=True) -> None: ...
    pass
class TopOpeBRepDS_SurfaceIterator(TopOpeBRepDS_InterferenceIterator):
    """
    None
    """
    def ChangeIterator(self) -> Any: 
        """
        None
        """
    def Current(self) -> int: 
        """
        Index of the surface in the data structure.
        """
    def Geometry(self,G : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry <G>
        """
    def GeometryKind(self,GK : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Geometry Kind <ST>
        """
    def Init(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        re-initialize interference iteration process on the list of interference <L>. Conditions are not modified.
        """
    def Match(self) -> None: 
        """
        reach for an interference matching the conditions (if defined).
        """
    def MatchInterference(self,I : TopOpeBRepDS_Interference) -> bool: 
        """
        Returns True if the Interference <I> matches the conditions (if defined). If no conditions defined, returns True.
        """
    def More(self) -> bool: 
        """
        Returns True if there is a current Interference in the iteration.
        """
    def Next(self) -> None: 
        """
        Move to the next Interference.
        """
    def Orientation(self,S : OCP.TopAbs.TopAbs_State) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None
        """
    def Support(self,S : int) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support <S>
        """
    def SupportKind(self,ST : TopOpeBRepDS_Kind) -> None: 
        """
        define a condition on interference iteration process. Interference must match the Support Kind <ST>
        """
    def Value(self) -> TopOpeBRepDS_Interference: 
        """
        Returns the current Interference, matching the conditions (if defined).
        """
    def __init__(self,L : TopOpeBRepDS_ListOfInterference) -> None: ...
    pass
class TopOpeBRepDS_TKI():
    """
    None
    """
    @overload
    def Add(self,K : TopOpeBRepDS_Kind,G : int) -> None: 
        """
        None

        None
        """
    @overload
    def Add(self,K : TopOpeBRepDS_Kind,G : int,HI : TopOpeBRepDS_Interference) -> None: ...
    def ChangeInterferences(self,K : TopOpeBRepDS_Kind,G : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def ChangeValue(self,K : TopOpeBRepDS_Kind,G : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def DumpTKIIterator(self,s1 : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,s2 : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def FillOnGeometry(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def FillOnSupport(self,L : TopOpeBRepDS_ListOfInterference) -> None: 
        """
        None
        """
    def HasInterferences(self,K : TopOpeBRepDS_Kind,G : int) -> bool: 
        """
        None
        """
    def Init(self) -> None: 
        """
        None
        """
    def Interferences(self,K : TopOpeBRepDS_Kind,G : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def IsBound(self,K : TopOpeBRepDS_Kind,G : int) -> bool: 
        """
        None
        """
    def More(self) -> bool: 
        """
        None
        """
    def Next(self) -> None: 
        """
        None
        """
    def Value(self,K : TopOpeBRepDS_Kind,G : int) -> TopOpeBRepDS_ListOfInterference: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_TOOL():
    """
    None
    """
    @staticmethod
    def EShareG_s(HDS : TopOpeBRepDS_HDataStructure,E : OCP.TopoDS.TopoDS_Edge,lEsd : OCP.TopTools.TopTools_ListOfShape) -> int: 
        """
        None
        """
    @staticmethod
    def GetConfig_s(HDS : TopOpeBRepDS_HDataStructure,MEspON : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State,ie : int,iesd : int,conf : int) -> bool: 
        """
        None
        """
    @staticmethod
    def GetEsd_s(HDS : TopOpeBRepDS_HDataStructure,S : OCP.TopoDS.TopoDS_Shape,ie : int,iesd : int) -> bool: 
        """
        None
        """
    @staticmethod
    def ShareG_s(HDS : TopOpeBRepDS_HDataStructure,is1 : int,is2 : int) -> bool: 
        """
        None
        """
    @staticmethod
    def ShareSplitON_s(HDS : TopOpeBRepDS_HDataStructure,MspON : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State,i1 : int,i2 : int,spON : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TopOpeBRepDS_Transition():
    """
    None
    """
    @overload
    def After(self) -> OCP.TopAbs.TopAbs_State: 
        """
        None

        None
        """
    @overload
    def After(self,S : OCP.TopAbs.TopAbs_State,ShapeAfter : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...
    @overload
    def Before(self,S : OCP.TopAbs.TopAbs_State,ShapeBefore : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE) -> None: 
        """
        None

        None
        """
    @overload
    def Before(self) -> OCP.TopAbs.TopAbs_State: ...
    def Complement(self) -> TopOpeBRepDS_Transition: 
        """
        None
        """
    @overload
    def Index(self,I : int) -> None: 
        """
        None

        None
        """
    @overload
    def Index(self) -> int: ...
    @overload
    def IndexAfter(self) -> int: 
        """
        None

        None
        """
    @overload
    def IndexAfter(self,I : int) -> None: ...
    @overload
    def IndexBefore(self) -> int: 
        """
        None

        None
        """
    @overload
    def IndexBefore(self,I : int) -> None: ...
    def IsUnknown(self) -> bool: 
        """
        returns True if both states are UNKNOWN
        """
    def ONAfter(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    def ONBefore(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None
        """
    def Orientation(self,S : OCP.TopAbs.TopAbs_State,T : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        returns the orientation corresponding to state <S>
        """
    @overload
    def Set(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None

        set the transition corresponding to orientation <O>
        """
    @overload
    def Set(self,StateBefore : OCP.TopAbs.TopAbs_State,StateAfter : OCP.TopAbs.TopAbs_State,ShapeBefore : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE,ShapeAfter : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...
    @overload
    def ShapeAfter(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        None

        None
        """
    @overload
    def ShapeAfter(self,SE : OCP.TopAbs.TopAbs_ShapeEnum) -> None: ...
    @overload
    def ShapeBefore(self,SE : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        None

        None
        """
    @overload
    def ShapeBefore(self) -> OCP.TopAbs.TopAbs_ShapeEnum: ...
    def StateAfter(self,S : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    def StateBefore(self,S : OCP.TopAbs.TopAbs_State) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def __init__(self,StateBefore : OCP.TopAbs.TopAbs_State,StateAfter : OCP.TopAbs.TopAbs_State,ShapeBefore : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE,ShapeAfter : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_FACE) -> None: ...
    pass
@overload
def FDSCNX_Dump(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None

    None
    """
@overload
def FDSCNX_Dump(HDS : TopOpeBRepDS_HDataStructure,I : int) -> None:
    pass
def FDSCNX_DumpIndex(HDS : TopOpeBRepDS_HDataStructure,I : int) -> None:
    """
    None
    """
def FDSCNX_EdgeConnexitySameShape(E : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure) -> OCP.TopTools.TopTools_ListOfShape:
    """
    None
    """
def FDSCNX_EdgeConnexityShapeIndex(E : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure,SI : int) -> OCP.TopTools.TopTools_ListOfShape:
    """
    None
    """
def FDSCNX_FaceEdgeConnexFaces(F : OCP.TopoDS.TopoDS_Shape,E : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure,LF : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
def FDSCNX_HasConnexFace(S : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure) -> bool:
    """
    None
    """
def FDSCNX_Prepare(S1 : OCP.TopoDS.TopoDS_Shape,S2 : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FDSSDM_contains(S : OCP.TopoDS.TopoDS_Shape,L : OCP.TopTools.TopTools_ListOfShape) -> bool:
    """
    None
    """
@overload
def FDSSDM_copylist(Lin : OCP.TopTools.TopTools_ListOfShape,Lou : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None

    None
    """
@overload
def FDSSDM_copylist(Lin : OCP.TopTools.TopTools_ListOfShape,I1 : int,I2 : int,Lou : OCP.TopTools.TopTools_ListOfShape) -> None:
    pass
def FDSSDM_makes1s2(S : OCP.TopoDS.TopoDS_Shape,L1 : OCP.TopTools.TopTools_ListOfShape,L2 : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
def FDSSDM_prepare(arg0 : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FDSSDM_s1s2(S : OCP.TopoDS.TopoDS_Shape,LS1 : OCP.TopTools.TopTools_ListOfShape,LS2 : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
def FDSSDM_sordor(S : OCP.TopoDS.TopoDS_Shape,LSO : OCP.TopTools.TopTools_ListOfShape,LDO : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
def FDS_Config3d(E1 : OCP.TopoDS.TopoDS_Shape,E2 : OCP.TopoDS.TopoDS_Shape,c : TopOpeBRepDS_Config) -> bool:
    """
    None
    """
def FDS_EdgeIsConnexToSameDomainFaces(E : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure) -> bool:
    """
    None
    """
def FDS_HasSameDomain2d(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Shape,PLSD : OCP.TopTools.TopTools_ListOfShape=None) -> bool:
    """
    None
    """
def FDS_HasSameDomain3d(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Shape,PLSD : OCP.TopTools.TopTools_ListOfShape=None) -> bool:
    """
    None
    """
def FDS_Idata(I : TopOpeBRepDS_Interference,SB : OCP.TopAbs.TopAbs_ShapeEnum,IB : int,SA : OCP.TopAbs.TopAbs_ShapeEnum,IA : int,GT1 : TopOpeBRepDS_Kind,G1 : int,ST1 : TopOpeBRepDS_Kind,S1 : int) -> None:
    """
    None
    """
def FDS_LOIinfsup(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Edge,pE : float,KDS : TopOpeBRepDS_Kind,GDS : int,LOI : TopOpeBRepDS_ListOfInterference,pbef : float,paft : float,isonboundper : bool) -> bool:
    """
    None
    """
@overload
def FDS_Parameter(I : TopOpeBRepDS_Interference) -> float:
    """
    None

    None
    """
@overload
def FDS_Parameter(I : TopOpeBRepDS_Interference,par : float) -> bool:
    pass
def FDS_SIisGIofIofSBAofTofI(BDS : TopOpeBRepDS_DataStructure,SI : int,I : TopOpeBRepDS_Interference) -> bool:
    """
    None
    """
def FDS_SetT(T : TopOpeBRepDS_Transition,T0 : TopOpeBRepDS_Transition) -> None:
    """
    None
    """
def FDS_Tdata(I : TopOpeBRepDS_Interference,SB : OCP.TopAbs.TopAbs_ShapeEnum,IB : int,SA : OCP.TopAbs.TopAbs_ShapeEnum,IA : int) -> None:
    """
    None
    """
@overload
def FDS_aresamdom(BDS : TopOpeBRepDS_DataStructure,ES : OCP.TopoDS.TopoDS_Shape,F1 : OCP.TopoDS.TopoDS_Shape,F2 : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None

    None
    """
@overload
def FDS_aresamdom(BDS : TopOpeBRepDS_DataStructure,SI : int,isb1 : int,isb2 : int) -> bool:
    pass
@overload
def FDS_assign(LI : OCP.TopTools.TopTools_ListOfShape,LII : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None

    None
    """
@overload
def FDS_assign(LI : TopOpeBRepDS_ListOfInterference,LII : TopOpeBRepDS_ListOfInterference) -> None:
    pass
@overload
def FDS_copy(LI : OCP.TopTools.TopTools_ListOfShape,LII : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None

    None
    """
@overload
def FDS_copy(LI : TopOpeBRepDS_ListOfInterference,LII : TopOpeBRepDS_ListOfInterference) -> None:
    pass
@overload
def FDS_data(it : Any,I : TopOpeBRepDS_Interference,GT1 : TopOpeBRepDS_Kind,G1 : int,ST1 : TopOpeBRepDS_Kind,S1 : int) -> bool:
    """
    None

    None
    """
@overload
def FDS_data(I : TopOpeBRepDS_Interference,GT1 : TopOpeBRepDS_Kind,G1 : int,ST1 : TopOpeBRepDS_Kind,S1 : int) -> None:
    pass
def FDS_getupperlower(HDS : TopOpeBRepDS_HDataStructure,edgeIndex : int,paredge : float,p1 : float,p2 : float) -> None:
    """
    None
    """
def FDS_hasUNK(T : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FDS_parbefaft(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Edge,pE : float,pbef : float,paft : float,isonboundper : bool,p1 : float,p2 : float) -> bool:
    """
    None
    """
def FDS_repvg(BDS : TopOpeBRepDS_DataStructure,EIX : int,GT : TopOpeBRepDS_Kind,LI : TopOpeBRepDS_ListOfInterference,reducedLI : TopOpeBRepDS_ListOfInterference) -> None:
    """
    None
    """
def FDS_repvg2(BDS : TopOpeBRepDS_DataStructure,EIX : int,GT : TopOpeBRepDS_Kind,LI : TopOpeBRepDS_ListOfInterference,reducedLI : TopOpeBRepDS_ListOfInterference) -> None:
    """
    None
    """
def FDS_stateEwithF2d(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Edge,pE : float,KDS : TopOpeBRepDS_Kind,GDS : int,F1 : OCP.TopoDS.TopoDS_Face,TrmemeS : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_ds_FEIGb1TO0(HDS : TopOpeBRepDS_HDataStructure,MEspON : TopOpeBRepDS_DataMapOfShapeListOfShapeOn1State) -> None:
    """
    None
    """
def FUN_ds_FillSDMFaces(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_GetTr(BDS : TopOpeBRepDS_DataStructure,ISE : int,G : int,LIG : TopOpeBRepDS_ListOfInterference,stb : OCP.TopAbs.TopAbs_State,isb : int,bdim : int,sta : OCP.TopAbs.TopAbs_State,isa : int,adim : int) -> bool:
    """
    None
    """
def FUN_ds_ONesd(BDS : TopOpeBRepDS_DataStructure,IE : int,EspON : OCP.TopoDS.TopoDS_Shape,IEsd : int) -> bool:
    """
    None
    """
def FUN_ds_PURGEforE9(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_PointToVertex(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_addSEsdm1d(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_complete1dForSESDM(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforE7(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE1(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE2(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE3(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE4(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE5(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE6(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE8(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_completeforSE9(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_getVsdm(BDS : TopOpeBRepDS_DataStructure,iV : int,iVsdm : int) -> bool:
    """
    None
    """
@overload
def FUN_ds_getoov(v : OCP.TopoDS.TopoDS_Shape,BDS : TopOpeBRepDS_DataStructure,oov : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None

    None
    """
@overload
def FUN_ds_getoov(v : OCP.TopoDS.TopoDS_Shape,HDS : TopOpeBRepDS_HDataStructure,oov : OCP.TopoDS.TopoDS_Shape) -> bool:
    pass
def FUN_ds_hasFEI(pDS2d : TopOpeBRepDS_DataStructure,F : OCP.TopoDS.TopoDS_Shape,GI : int,ITRA : int) -> bool:
    """
    None
    """
def FUN_ds_hasI2d(EIX : int,LI : TopOpeBRepDS_ListOfInterference,LI2d : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_ds_mkTonFsdm(HDS : TopOpeBRepDS_HDataStructure,iF1 : int,iF2 : int,iE2 : int,iEG : int,paronEG : float,Esp : OCP.TopoDS.TopoDS_Edge,pardef : bool,T : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_ds_oriEinF(BDS : TopOpeBRepDS_DataStructure,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Shape,O : OCP.TopAbs.TopAbs_Orientation) -> int:
    """
    None
    """
def FUN_ds_redu2d1d(BDS : TopOpeBRepDS_DataStructure,ISE : int,I2d : TopOpeBRepDS_Interference,l1d : TopOpeBRepDS_ListOfInterference,newT2d : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_ds_redusamsha(HDS : TopOpeBRepDS_HDataStructure) -> None:
    """
    None
    """
def FUN_ds_samRk(BDS : TopOpeBRepDS_DataStructure,Rk : int,LI : OCP.TopTools.TopTools_ListOfShape,LIsrk : OCP.TopTools.TopTools_ListOfShape) -> None:
    """
    None
    """
def FUN_ds_sdm(BDS : TopOpeBRepDS_DataStructure,s1 : OCP.TopoDS.TopoDS_Shape,s2 : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
def FUN_ds_shareG(HDS : TopOpeBRepDS_HDataStructure,iF1 : int,iF2 : int,iE2 : int,Esp : OCP.TopoDS.TopoDS_Edge,shareG : bool) -> bool:
    """
    None
    """
def FUN_hasStateShape(T : TopOpeBRepDS_Transition,state : OCP.TopAbs.TopAbs_State,shape : OCP.TopAbs.TopAbs_ShapeEnum) -> bool:
    """
    None
    """
def FUN_interfhassupport(DS : TopOpeBRepDS_DataStructure,I : TopOpeBRepDS_Interference,S : OCP.TopoDS.TopoDS_Shape) -> bool:
    """
    None
    """
def FUN_reducedoublons(LI : TopOpeBRepDS_ListOfInterference,BDS : TopOpeBRepDS_DataStructure,SIX : int) -> None:
    """
    None
    """
def FUN_select1dI(SIX : int,BDS : TopOpeBRepDS_DataStructure,LI : TopOpeBRepDS_ListOfInterference,l1dI : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_select2dI(SIX : int,BDS : TopOpeBRepDS_DataStructure,TRASHAk : OCP.TopAbs.TopAbs_ShapeEnum,lI : TopOpeBRepDS_ListOfInterference,l2dI : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_select3dinterference(SIX : int,BDS : TopOpeBRepDS_DataStructure,lF : TopOpeBRepDS_ListOfInterference,l3dF : TopOpeBRepDS_ListOfInterference,lFE : TopOpeBRepDS_ListOfInterference,lFEresi : TopOpeBRepDS_ListOfInterference,l3dFE : TopOpeBRepDS_ListOfInterference,l3dFEresi : TopOpeBRepDS_ListOfInterference,l2dFE : TopOpeBRepDS_ListOfInterference) -> None:
    """
    None
    """
def FUN_selectGIinterference(L1 : TopOpeBRepDS_ListOfInterference,GI : int,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectGKinterference(L1 : TopOpeBRepDS_ListOfInterference,GK : TopOpeBRepDS_Kind,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectITRASHAinterference(L1 : TopOpeBRepDS_ListOfInterference,Index : int,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectSIinterference(L1 : TopOpeBRepDS_ListOfInterference,SI : int,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectSKinterference(L1 : TopOpeBRepDS_ListOfInterference,SK : TopOpeBRepDS_Kind,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectTRAINTinterference(li : TopOpeBRepDS_ListOfInterference,liINTERNAL : TopOpeBRepDS_ListOfInterference) -> bool:
    """
    None
    """
def FUN_selectTRAORIinterference(L1 : TopOpeBRepDS_ListOfInterference,O : OCP.TopAbs.TopAbs_Orientation,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectTRASHAinterference(L1 : TopOpeBRepDS_ListOfInterference,sha : OCP.TopAbs.TopAbs_ShapeEnum,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectTRAUNKinterference(L1 : TopOpeBRepDS_ListOfInterference,L2 : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_selectpure2dI(lF : TopOpeBRepDS_ListOfInterference,lFE : TopOpeBRepDS_ListOfInterference,l2dFE : TopOpeBRepDS_ListOfInterference) -> int:
    """
    None
    """
def FUN_transitionEQUAL(arg0 : TopOpeBRepDS_Transition,arg1 : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_transitionINDEXEQUAL(arg0 : TopOpeBRepDS_Transition,arg1 : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_transitionSHAPEEQUAL(arg0 : TopOpeBRepDS_Transition,arg1 : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_transitionSTATEEQUAL(arg0 : TopOpeBRepDS_Transition,arg1 : TopOpeBRepDS_Transition) -> bool:
    """
    None
    """
def FUN_unkeepUNKNOWN(LI : TopOpeBRepDS_ListOfInterference,BDS : TopOpeBRepDS_DataStructure,SIX : int) -> None:
    """
    None
    """
def MakeCPVInterference(T : TopOpeBRepDS_Transition,S : int,G : int,P : float,GK : TopOpeBRepDS_Kind) -> TopOpeBRepDS_Interference:
    """
    None
    """
@overload
def MakeEPVInterference(T : TopOpeBRepDS_Transition,S : int,G : int,P : float,GK : TopOpeBRepDS_Kind,B : bool) -> TopOpeBRepDS_Interference:
    """
    None

    None
    """
@overload
def MakeEPVInterference(T : TopOpeBRepDS_Transition,S : int,G : int,P : float,GK : TopOpeBRepDS_Kind,SK : TopOpeBRepDS_Kind,B : bool) -> TopOpeBRepDS_Interference:
    pass
TopOpeBRepDS_COMPOUND: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPOUND: 10>
TopOpeBRepDS_COMPSOLID: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_COMPSOLID: 9>
TopOpeBRepDS_CURVE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_CURVE: 1>
TopOpeBRepDS_DIFFORIENTED: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_DIFFORIENTED: 2>
TopOpeBRepDS_EDGE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_EDGE: 4>
TopOpeBRepDS_FACE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_FACE: 6>
TopOpeBRepDS_NOK: OCP.TopOpeBRepDS.TopOpeBRepDS_CheckStatus # value = <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_NOK: 1>
TopOpeBRepDS_OK: OCP.TopOpeBRepDS.TopOpeBRepDS_CheckStatus # value = <TopOpeBRepDS_CheckStatus.TopOpeBRepDS_OK: 0>
TopOpeBRepDS_POINT: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_POINT: 0>
TopOpeBRepDS_SAMEORIENTED: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_SAMEORIENTED: 1>
TopOpeBRepDS_SHELL: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SHELL: 7>
TopOpeBRepDS_SOLID: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SOLID: 8>
TopOpeBRepDS_SURFACE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_SURFACE: 2>
TopOpeBRepDS_UNKNOWN: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_UNKNOWN: 11>
TopOpeBRepDS_UNSHGEOMETRY: OCP.TopOpeBRepDS.TopOpeBRepDS_Config # value = <TopOpeBRepDS_Config.TopOpeBRepDS_UNSHGEOMETRY: 0>
TopOpeBRepDS_VERTEX: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_VERTEX: 3>
TopOpeBRepDS_WIRE: OCP.TopOpeBRepDS.TopOpeBRepDS_Kind # value = <TopOpeBRepDS_Kind.TopOpeBRepDS_WIRE: 5>
