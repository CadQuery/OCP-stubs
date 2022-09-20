import OCP.BOPDS
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.IntTools
import OCP.TopTools
import OCP.NCollection
import OCP.Bnd
import io
import OCP.gp
import OCP.Standard
import OCP.TopAbs
import OCP.TopoDS
import OCP.TColStd
__all__  = [
"BOPDS_CommonBlock",
"BOPDS_CoupleOfPaveBlocks",
"BOPDS_Curve",
"BOPDS_DS",
"BOPDS_DataMapOfIntegerListOfPaveBlock",
"BOPDS_DataMapOfPaveBlockListOfInteger",
"BOPDS_DataMapOfPaveBlockListOfPaveBlock",
"BOPDS_DataMapOfShapeCoupleOfPaveBlocks",
"BOPDS_FaceInfo",
"BOPDS_IndexRange",
"BOPDS_IndexedDataMapOfPaveBlockListOfInteger",
"BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock",
"BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks",
"BOPDS_IndexedMapOfPaveBlock",
"BOPDS_Interf",
"BOPDS_InterfEE",
"BOPDS_InterfEF",
"BOPDS_InterfEZ",
"BOPDS_InterfFF",
"BOPDS_InterfFZ",
"BOPDS_InterfVE",
"BOPDS_InterfVF",
"BOPDS_InterfVV",
"BOPDS_InterfVZ",
"BOPDS_InterfZZ",
"BOPDS_ListOfPave",
"BOPDS_ListOfPaveBlock",
"BOPDS_MapOfCommonBlock",
"BOPDS_MapOfPair",
"BOPDS_MapOfPave",
"BOPDS_MapOfPaveBlock",
"BOPDS_Pair",
"BOPDS_PairMapHasher",
"BOPDS_Pave",
"BOPDS_PaveBlock",
"BOPDS_PaveMapHasher",
"BOPDS_Point",
"BOPDS_ShapeInfo",
"BOPDS_SubIterator",
"BOPDS_Tools",
"BOPDS_VectorOfCurve",
"BOPDS_VectorOfFaceInfo",
"BOPDS_VectorOfIndexRange",
"BOPDS_VectorOfInterfEE",
"BOPDS_VectorOfInterfEF",
"BOPDS_VectorOfInterfEZ",
"BOPDS_VectorOfInterfFF",
"BOPDS_VectorOfInterfFZ",
"BOPDS_VectorOfInterfVE",
"BOPDS_VectorOfInterfVF",
"BOPDS_VectorOfInterfVV",
"BOPDS_VectorOfInterfVZ",
"BOPDS_VectorOfInterfZZ",
"BOPDS_VectorOfListOfPaveBlock",
"BOPDS_VectorOfPair",
"BOPDS_VectorOfPave",
"BOPDS_VectorOfPoint",
"BOPDS_VectorOfShapeInfo",
"BOPDS_VectorOfVectorOfPair"
]
class BOPDS_CommonBlock(OCP.Standard.Standard_Transient):
    """
    The class BOPDS_CommonBlock is to store the information about pave blocks that have geometrical coincidence (in terms of a tolerance) with: a) other pave block(s); b) face(s). First pave block in the common block (real pave block) is always a pave block with the minimal index of the original edge.The class BOPDS_CommonBlock is to store the information about pave blocks that have geometrical coincidence (in terms of a tolerance) with: a) other pave block(s); b) face(s). First pave block in the common block (real pave block) is always a pave block with the minimal index of the original edge.The class BOPDS_CommonBlock is to store the information about pave blocks that have geometrical coincidence (in terms of a tolerance) with: a) other pave block(s); b) face(s). First pave block in the common block (real pave block) is always a pave block with the minimal index of the original edge.
    """
    def AddFace(self,aF : int) -> None: 
        """
        Modifier Adds the index of the face <aF> to the list of indices of faces of the common block
        """
    def AddPaveBlock(self,aPB : BOPDS_PaveBlock) -> None: 
        """
        Modifier Adds the pave block <aPB> to the list of pave blocks of the common block
        """
    def AppendFaces(self,aLF : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Modifier Appends the list of indices of faces <aLF> to the list of indices of faces of the common block (the input list is emptied)
        """
    @overload
    def Contains(self,thePB : BOPDS_PaveBlock) -> bool: 
        """
        Query Returns true if the common block contains a pave block that is equal to <thePB>

        Query Returns true if the common block contains the face with index equal to <theF>
        """
    @overload
    def Contains(self,theF : int) -> bool: ...
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> int: 
        """
        Selector Returns the index of the edge of all pave blocks of the common block
        """
    def Faces(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Selector Returns the list of indices of faces of the common block
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsPaveBlockOnEdge(self,theIndex : int) -> bool: 
        """
        Query Returns true if the common block contains a pave block that belongs to the edge with index <theIx>
        """
    def IsPaveBlockOnFace(self,theIndex : int) -> bool: 
        """
        Query Returns true if the common block contains a pave block that belongs to the face with index <theIx>
        """
    def PaveBlock1(self) -> BOPDS_PaveBlock: 
        """
        Selector Returns the first pave block of the common block
        """
    def PaveBlockOnEdge(self,theIndex : int) -> BOPDS_PaveBlock: 
        """
        Selector Returns the pave block that belongs to the edge with index <theIx>
        """
    def PaveBlocks(self) -> BOPDS_ListOfPaveBlock: 
        """
        Selector Returns the list of pave blocks of the common block
        """
    def SetEdge(self,theEdge : int) -> None: 
        """
        Modifier Assign the index <theEdge> as the edge index to all pave blocks of the common block
        """
    def SetFaces(self,aLF : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Modifier Sets the list of indices of faces <aLF> of the common block
        """
    def SetPaveBlocks(self,aLPB : BOPDS_ListOfPaveBlock) -> None: 
        """
        Modifier Sets the list of pave blocks for the common block
        """
    def SetRealPaveBlock(self,thePB : BOPDS_PaveBlock) -> None: 
        """
        Moves the pave blocks in the list to make the given pave block to be the first. It will be representative for the whole group.
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        Sets the tolerance for the common block
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tolerance(self) -> float: 
        """
        Return the tolerance of common block
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
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
class BOPDS_CoupleOfPaveBlocks():
    """
    The Class BOPDS_CoupleOfPaveBlocks is to store the information about two pave blocks and some satellite information
    """
    def Index(self) -> int: 
        """
        Returns the index
        """
    def IndexInterf(self) -> int: 
        """
        Returns the index of an interference
        """
    def PaveBlock1(self) -> BOPDS_PaveBlock: 
        """
        Returns the first pave block
        """
    def PaveBlock2(self) -> BOPDS_PaveBlock: 
        """
        Returns the second pave block
        """
    def PaveBlocks(self,thePB1 : BOPDS_PaveBlock,thePB2 : BOPDS_PaveBlock) -> Any: 
        """
        Returns pave blocks
        """
    def SetIndex(self,theIndex : int) -> None: 
        """
        Sets an index
        """
    def SetIndexInterf(self,theIndex : int) -> None: 
        """
        Sets an index of an interference
        """
    def SetPaveBlock1(self,thePB : BOPDS_PaveBlock) -> None: 
        """
        Sets the first pave block
        """
    def SetPaveBlock2(self,thePB : BOPDS_PaveBlock) -> None: 
        """
        Sets the second pave block
        """
    def SetPaveBlocks(self,thePB1 : BOPDS_PaveBlock,thePB2 : BOPDS_PaveBlock) -> None: 
        """
        Sets pave blocks
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        Sets the tolerance associated with this couple
        """
    def Tolerance(self) -> float: 
        """
        Returns the tolerance associated with this couple
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePB1 : BOPDS_PaveBlock,thePB2 : BOPDS_PaveBlock) -> None: ...
    pass
class BOPDS_Curve():
    """
    The class BOPDS_Curve is to store the information about intersection curve
    """
    def Box(self) -> OCP.Bnd.Bnd_Box: 
        """
        Selector Returns the bounding box of the curve

        Selector Returns the bounding box of the curve
        """
    def ChangeBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Selector/Modifier Returns the bounding box of the curve

        Selector/Modifier Returns the bounding box of the curve
        """
    def ChangePaveBlock1(self) -> BOPDS_PaveBlock: 
        """
        Selector/Modifier Returns initial pave block of the curve

        Selector/Modifier Returns initial pave block of the curve
        """
    def ChangePaveBlocks(self) -> BOPDS_ListOfPaveBlock: 
        """
        Selector/Modifier Returns the list of pave blocks of the curve

        Selector/Modifier Returns the list of pave blocks of the curve
        """
    def ChangeTechnoVertices(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Selector/Modifier Returns list of indices of technologic vertices of the curve

        Selector/Modifier Returns list of indices of technologic vertices of the curve
        """
    def Curve(self) -> OCP.IntTools.IntTools_Curve: 
        """
        Selector Returns the curve

        Selector Returns the curve
        """
    def HasEdge(self) -> bool: 
        """
        Query Returns true if at least one pave block of the curve has edge

        Query Returns true if at least one pave block of the curve has edge
        """
    def InitPaveBlock1(self) -> None: 
        """
        Creates initial pave block of the curve

        Creates initial pave block of the curve
        """
    def PaveBlocks(self) -> BOPDS_ListOfPaveBlock: 
        """
        Selector Returns the list of pave blocks of the curve

        Selector Returns the list of pave blocks of the curve
        """
    def SetBox(self,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Modifier Sets the bounding box <theBox> of the curve

        Modifier Sets the bounding box <theBox> of the curve
        """
    @overload
    def SetCurve(self,theC : OCP.IntTools.IntTools_Curve) -> None: 
        """
        Modifier Sets the curve <theC>

        Modifier Sets the curve <theC>
        """
    @overload
    def SetCurve(self,theCurve : OCP.IntTools.IntTools_Curve) -> None: ...
    def SetPaveBlocks(self,theLPB : BOPDS_ListOfPaveBlock) -> None: 
        """
        None

        None
        """
    def SetTolerance(self,theTol : float) -> None: 
        """
        Sets the tolerance for the curve.
        """
    def TangentialTolerance(self) -> float: 
        """
        Returns the tangential tolerance of the curve
        """
    def TechnoVertices(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Selector Returns list of indices of technologic vertices of the curve

        Selector Returns list of indices of technologic vertices of the curve
        """
    def Tolerance(self) -> float: 
        """
        Returns the tolerance of the curve
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_DS():
    """
    The class BOPDS_DS provides the control of data structure for the algorithms in the Boolean Component such as General Fuse, Boolean operations, Section, Maker Volume, Splitter and Cells Builder.
    """
    def AddInterf(self,theI1 : int,theI2 : int) -> bool: 
        """
        Modifier Adds the information about an interference between shapes with indices theI1, theI2 to the summary table of interferences

        Modifier Adds the information about an interference between shapes with indices theI1, theI2 to the summary table of interferences
        """
    def AddShapeSD(self,theIndex : int,theIndexSD : int) -> None: 
        """
        Modifier Adds the information about same domain shapes with indices theIndex, theIndexSD
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Selector
        """
    def AloneVertices(self,theF : int,theLI : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Selector Returns the indices of alone vertices for the face with index theIndex
        """
    @overload
    def Append(self,theS : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Modifier Appends the information about the shape [theSI] to the data structure Returns the index of theSI in the data structure

        Modifier Appends the default information about the shape [theS] to the data structure Returns the index of theS in the data structure
        """
    @overload
    def Append(self,theSI : BOPDS_ShapeInfo) -> int: ...
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Selector Returns the arguments of an operation
        """
    def BuildBndBoxSolid(self,theIndex : int,theBox : OCP.Bnd.Bnd_Box,theCheckInverted : bool=True) -> None: 
        """
        Computes bounding box <theBox> for the solid with DS-index <theIndex>. The flag <theCheckInverted> enables/disables the check of the solid for inverted status. By default the solids will be checked.
        """
    def ChangeFaceInfo(self,theIndex : int) -> BOPDS_FaceInfo: 
        """
        Selector/Modifier Returns the state of face with index theIndex
        """
    def ChangePaveBlocks(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        Selector/Modifier Returns the pave blocks for the shape with index theIndex
        """
    def ChangePaveBlocksPool(self) -> BOPDS_VectorOfListOfPaveBlock: 
        """
        Selector/Modifier Returns the information about pave blocks on source edges
        """
    def ChangeShapeInfo(self,theIndex : int) -> BOPDS_ShapeInfo: 
        """
        Selector/Modifier Returns the information about the shape with index theIndex
        """
    def Clear(self) -> None: 
        """
        Clears the contents
        """
    def CommonBlock(self,thePB : BOPDS_PaveBlock) -> BOPDS_CommonBlock: 
        """
        Selector Returns the common block
        """
    def Dump(self) -> None: 
        """
        None
        """
    def FaceInfo(self,theIndex : int) -> BOPDS_FaceInfo: 
        """
        Selector Returns the state of face with index theIndex
        """
    def FaceInfoIn(self,theIndex : int,theMPB : BOPDS_IndexedMapOfPaveBlock,theMVP : OCP.TColStd.TColStd_MapOfInteger) -> None: 
        """
        Selector Returns the state In [theMPB,theMVP] of face with index theIndex
        """
    def FaceInfoOn(self,theIndex : int,theMPB : BOPDS_IndexedMapOfPaveBlock,theMVP : OCP.TColStd.TColStd_MapOfInteger) -> None: 
        """
        Selector Returns the state On [theMPB,theMVP] of face with index theIndex
        """
    def FaceInfoPool(self) -> BOPDS_VectorOfFaceInfo: 
        """
        Selector Returns the information about state of faces
        """
    def HasFaceInfo(self,theIndex : int) -> bool: 
        """
        Query Returns true if the shape with index theIndex has the information about state of face
        """
    @overload
    def HasInterf(self,theI1 : int,theI2 : int) -> bool: 
        """
        Query Returns true if the shape with index theI is interferred

        Query Returns true if the shapes with indices theI1, theI2 are interferred

        Query Returns true if the shape with index theI is interferred

        Query Returns true if the shapes with indices theI1, theI2 are interferred
        """
    @overload
    def HasInterf(self,theI : int) -> bool: ...
    def HasInterfShapeSubShapes(self,theI1 : int,theI2 : int,theFlag : bool=True) -> bool: 
        """
        Query Returns true if the shape with index theI1 is interfered with any sub-shape of the shape with index theI2 (theFlag=true) all sub-shapes of the shape with index theI2 (theFlag=false)
        """
    def HasInterfSubShapes(self,theI1 : int,theI2 : int) -> bool: 
        """
        Query Returns true if the shapes with indices theI1, theI2 have interferred sub-shapes
        """
    def HasPaveBlocks(self,theIndex : int) -> bool: 
        """
        Query Returns true if the shape with index theIndex has the information about pave blocks
        """
    def HasShapeSD(self,theIndex : int,theIndexSD : int) -> bool: 
        """
        Query Returns true if the shape with index theIndex has the same domain shape. In this case theIndexSD will contain the index of same domain shape found
        """
    def Index(self,theS : OCP.TopoDS.TopoDS_Shape) -> int: 
        """
        Selector Returns the index of the shape theS
        """
    def Init(self,theFuzz : float=1e-07) -> None: 
        """
        Initializes the data structure for the arguments
        """
    def InitPaveBlocksForVertex(self,theNV : int) -> None: 
        """
        None
        """
    def InterfEE(self) -> BOPDS_VectorOfInterfEE: 
        """
        Selector/Modifier Returns the collection of interferences Edge/Edge

        Selector/Modifier Returns the collection of interferences Edge/Edge
        """
    def InterfEF(self) -> BOPDS_VectorOfInterfEF: 
        """
        Selector/Modifier Returns the collection of interferences Edge/Face

        Selector/Modifier Returns the collection of interferences Edge/Face
        """
    def InterfEZ(self) -> BOPDS_VectorOfInterfEZ: 
        """
        Selector/Modifier Returns the collection of interferences Edge/Solid

        Selector/Modifier Returns the collection of interferences Edge/Solid
        """
    def InterfFF(self) -> BOPDS_VectorOfInterfFF: 
        """
        Selector/Modifier Returns the collection of interferences Face/Face

        Selector/Modifier Returns the collection of interferences Face/Face
        """
    def InterfFZ(self) -> BOPDS_VectorOfInterfFZ: 
        """
        Selector/Modifier Returns the collection of interferences Face/Solid

        Selector/Modifier Returns the collection of interferences Face/Solid
        """
    def InterfVE(self) -> BOPDS_VectorOfInterfVE: 
        """
        Selector/Modifier Returns the collection of interferences Vertex/Edge

        Selector/Modifier Returns the collection of interferences Vertex/Edge
        """
    def InterfVF(self) -> BOPDS_VectorOfInterfVF: 
        """
        Selector/Modifier Returns the collection of interferences Vertex/Face

        Selector/Modifier Returns the collection of interferences Vertex/Face
        """
    def InterfVV(self) -> BOPDS_VectorOfInterfVV: 
        """
        Selector/Modifier Returns the collection of interferences Vertex/Vertex

        Selector/Modifier Returns the collection of interferences Vertex/Vertex
        """
    def InterfVZ(self) -> BOPDS_VectorOfInterfVZ: 
        """
        Selector/Modifier Returns the collection of interferences Vertex/Solid

        Selector/Modifier Returns the collection of interferences Vertex/Solid
        """
    def InterfZZ(self) -> BOPDS_VectorOfInterfZZ: 
        """
        Selector/Modifier Returns the collection of interferences Solid/Solid

        Selector/Modifier Returns the collection of interferences Solid/Solid
        """
    def Interferences(self) -> BOPDS_MapOfPair: 
        """
        Selector Returns the table of interferences

        Selector Returns the table of interferences
        """
    def IsCommonBlock(self,thePB : BOPDS_PaveBlock) -> bool: 
        """
        Query Returns true if the pave block is common block
        """
    def IsCommonBlockOnEdge(self,thePB : BOPDS_PaveBlock) -> bool: 
        """
        Query Returns true if common block contains more then one pave block
        """
    def IsNewShape(self,theIndex : int) -> bool: 
        """
        Returns true if the shape of index "i" is not the source shape/sub-shape
        """
    def IsSubShape(self,theI1 : int,theI2 : int) -> bool: 
        """
        None
        """
    def IsValidShrunkData(self,thePB : BOPDS_PaveBlock) -> bool: 
        """
        Checks if the existing shrunk data of the pave block is still valid. The shrunk data may become invalid if e.g. the vertices of the pave block have been replaced with the new one with bigger tolerances, or the tolerances of the existing vertices have been increased.
        """
    @staticmethod
    def NbInterfTypes_s() -> int: 
        """
        Returns the number of types of the interferences
        """
    def NbRanges(self) -> int: 
        """
        Selector Returns the number of index ranges
        """
    def NbShapes(self) -> int: 
        """
        Selector Returns the total number of shapes stored
        """
    def NbSourceShapes(self) -> int: 
        """
        Selector Returns the total number of source shapes stored
        """
    def PaveBlocks(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        Selector Returns the pave blocks for the shape with index theIndex
        """
    def PaveBlocksPool(self) -> BOPDS_VectorOfListOfPaveBlock: 
        """
        Selector Returns the information about pave blocks on source edges
        """
    def Paves(self,theIndex : int,theLP : BOPDS_ListOfPave) -> None: 
        """
        Fills theLP with sorted paves of the shape with index theIndex
        """
    def Range(self,theIndex : int) -> BOPDS_IndexRange: 
        """
        Selector Returns the index range "i"
        """
    def Rank(self,theIndex : int) -> int: 
        """
        Selector Returns the rank of the shape of index "i"
        """
    def RealPaveBlock(self,thePB : BOPDS_PaveBlock) -> BOPDS_PaveBlock: 
        """
        Selector Returns the real first pave block
        """
    def RefineFaceInfoIn(self) -> None: 
        """
        Removes any pave block from list of having IN state if it has also the state ON.
        """
    def RefineFaceInfoOn(self) -> None: 
        """
        Refine the state On for the all faces having state information
        """
    def ReleasePaveBlocks(self) -> None: 
        """
        Clears information about PaveBlocks for the untouched edges
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Modifier Sets the arguments [theLS] of an operation
        """
    def SetCommonBlock(self,thePB : BOPDS_PaveBlock,theCB : BOPDS_CommonBlock) -> None: 
        """
        Modifier Sets the common block <theCB>
        """
    def Shape(self,theIndex : int) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Selector Returns the shape with index theIndex
        """
    def ShapeInfo(self,theIndex : int) -> BOPDS_ShapeInfo: 
        """
        Selector Returns the information about the shape with index theIndex
        """
    def ShapesSD(self) -> OCP.TColStd.TColStd_DataMapOfIntegerInteger: 
        """
        Selector Returns the collection same domain shapes
        """
    def SharedEdges(self,theF1 : int,theF2 : int,theLI : OCP.TColStd.TColStd_ListOfInteger,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Returns the indices of edges that are shared for the faces with indices theF1, theF2
        """
    def UpdateCommonBlock(self,theCB : BOPDS_CommonBlock,theFuzz : float) -> None: 
        """
        Update the common block theCB
        """
    def UpdateCommonBlockWithSDVertices(self,theCB : BOPDS_CommonBlock) -> None: 
        """
        Update the pave block of the common block for all shapes in data structure
        """
    @overload
    def UpdateFaceInfoIn(self,theIndex : int) -> None: 
        """
        Update the state In of face with index theIndex

        Update the state IN for all faces in the given map
        """
    @overload
    def UpdateFaceInfoIn(self,theFaces : OCP.TColStd.TColStd_MapOfInteger) -> None: ...
    @overload
    def UpdateFaceInfoOn(self,theIndex : int) -> None: 
        """
        Update the state On of face with index theIndex

        Update the state ON for all faces in the given map
        """
    @overload
    def UpdateFaceInfoOn(self,theFaces : OCP.TColStd.TColStd_MapOfInteger) -> None: ...
    def UpdatePaveBlock(self,thePB : BOPDS_PaveBlock) -> None: 
        """
        Update the pave block thePB
        """
    def UpdatePaveBlockWithSDVertices(self,thePB : BOPDS_PaveBlock) -> None: 
        """
        Update the pave block for all shapes in data structure
        """
    def UpdatePaveBlocks(self) -> None: 
        """
        Update the pave blocks for the all shapes in data structure
        """
    def UpdatePaveBlocksWithSDVertices(self) -> None: 
        """
        Update the pave blocks for all shapes in data structure
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_DataMapOfIntegerListOfPaveBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_DataMapOfIntegerListOfPaveBlock) -> BOPDS_DataMapOfIntegerListOfPaveBlock: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : BOPDS_ListOfPaveBlock) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : BOPDS_ListOfPaveBlock) -> BOPDS_ListOfPaveBlock: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> BOPDS_ListOfPaveBlock: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> BOPDS_ListOfPaveBlock: 
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
    def Exchange(self,theOther : BOPDS_DataMapOfIntegerListOfPaveBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : BOPDS_ListOfPaveBlock) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> BOPDS_ListOfPaveBlock: ...
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
    def Seek(self,theKey : int) -> BOPDS_ListOfPaveBlock: 
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
    def __init__(self,theOther : BOPDS_DataMapOfIntegerListOfPaveBlock) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_DataMapOfPaveBlockListOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_DataMapOfPaveBlockListOfInteger) -> BOPDS_DataMapOfPaveBlockListOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : BOPDS_PaveBlock,theItem : OCP.TColStd.TColStd_ListOfInteger) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : BOPDS_PaveBlock,theItem : OCP.TColStd.TColStd_ListOfInteger) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
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
    def Exchange(self,theOther : BOPDS_DataMapOfPaveBlockListOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : BOPDS_PaveBlock,theValue : OCP.TColStd.TColStd_ListOfInteger) -> bool: ...
    def IsBound(self,theKey : BOPDS_PaveBlock) -> bool: 
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
    def Seek(self,theKey : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
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
    def UnBind(self,theKey : BOPDS_PaveBlock) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_DataMapOfPaveBlockListOfInteger) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_DataMapOfPaveBlockListOfPaveBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_DataMapOfPaveBlockListOfPaveBlock) -> BOPDS_DataMapOfPaveBlockListOfPaveBlock: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : BOPDS_PaveBlock,theItem : BOPDS_ListOfPaveBlock) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : BOPDS_PaveBlock,theItem : BOPDS_ListOfPaveBlock) -> BOPDS_ListOfPaveBlock: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
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
    def Exchange(self,theOther : BOPDS_DataMapOfPaveBlockListOfPaveBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : BOPDS_PaveBlock,theValue : BOPDS_ListOfPaveBlock) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: ...
    def IsBound(self,theKey : BOPDS_PaveBlock) -> bool: 
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
    def Seek(self,theKey : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
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
    def UnBind(self,theKey : BOPDS_PaveBlock) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_DataMapOfPaveBlockListOfPaveBlock) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_DataMapOfShapeCoupleOfPaveBlocks(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_DataMapOfShapeCoupleOfPaveBlocks) -> BOPDS_DataMapOfShapeCoupleOfPaveBlocks: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BOPDS_CoupleOfPaveBlocks) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : OCP.TopoDS.TopoDS_Shape,theItem : BOPDS_CoupleOfPaveBlocks) -> BOPDS_CoupleOfPaveBlocks: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
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
    def Exchange(self,theOther : BOPDS_DataMapOfShapeCoupleOfPaveBlocks) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape,theValue : BOPDS_CoupleOfPaveBlocks) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: ...
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
    def Seek(self,theKey : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
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
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_DataMapOfShapeCoupleOfPaveBlocks) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_FaceInfo():
    """
    The class BOPDS_FaceInfo is to store handy information about state of face
    """
    def ChangePaveBlocksIn(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Selector/Modifier Returns the pave blocks of the face that have state In

        Selector/Modifier Returns the pave blocks of the face that have state In
        """
    def ChangePaveBlocksOn(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Selector/Modifier Returns the pave blocks of the face that have state On

        Selector/Modifier Returns the pave blocks of the face that have state On
        """
    def ChangePaveBlocksSc(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        None

        None
        """
    def ChangeVerticesIn(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector/Modifier Returns the list of indices for vertices of the face that have state In

        Selector/Modifier Returns the list of indices for vertices of the face that have state In
        """
    def ChangeVerticesOn(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector/Modifier Returns the list of indices for vertices of the face that have state On

        Selector/Modifier Returns the list of indices for vertices of the face that have state On
        """
    def ChangeVerticesSc(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector/Modifier Returns the list of indices for section vertices of the face

        Selector/Modifier Returns the list of indices for section vertices of the face
        """
    def Clear(self) -> None: 
        """
        Clears the contents

        Clears the contents
        """
    def Index(self) -> int: 
        """
        Selector Returns the index of the face

        Selector Returns the index of the face
        """
    def PaveBlocksIn(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Selector Returns the pave blocks of the face that have state In

        Selector Returns the pave blocks of the face that have state In
        """
    def PaveBlocksOn(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Selector Returns the pave blocks of the face that have state On

        Selector Returns the pave blocks of the face that have state On
        """
    def PaveBlocksSc(self) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Selector Returns the pave blocks of the face that are pave blocks of section edges

        Selector Returns the pave blocks of the face that are pave blocks of section edges
        """
    def SetIndex(self,theI : int) -> None: 
        """
        Modifier Sets the index of the face <theI>

        Modifier Sets the index of the face <theI>
        """
    def VerticesIn(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector Returns the list of indices for vertices of the face that have state In

        Selector Returns the list of indices for vertices of the face that have state In
        """
    def VerticesOn(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector Returns the list of indices for vertices of the face that have state On

        Selector Returns the list of indices for vertices of the face that have state On
        """
    def VerticesSc(self) -> OCP.TColStd.TColStd_MapOfInteger: 
        """
        Selector Returns the list of indices for section vertices of the face

        Selector Returns the list of indices for section vertices of the face
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_IndexRange():
    """
    The class BOPDS_IndexRange is to store the information about range of two indices
    """
    @overload
    def Contains(self,theIndex : int) -> bool: 
        """
        Query Returns true if the range contains <theIndex>

        Query Returns true if the range contains <theIndex>
        """
    @overload
    def Contains(self,aIndex : int) -> bool: ...
    def Dump(self) -> None: 
        """
        None
        """
    def First(self) -> int: 
        """
        Selector Returns the first index of the range

        Selector Returns the first index of the range
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Selector Returns the first index of the range <theI1> Returns the second index of the range <theI2>

        Selector Returns the first index of the range <theI1> Returns the second index of the range <theI2>
        """
    def Last(self) -> int: 
        """
        Selector Returns the second index of the range

        Selector Returns the second index of the range
        """
    @overload
    def SetFirst(self,theI1 : int) -> None: 
        """
        Modifier Sets the first index <theI1> of the range

        Modifier Sets the first index <theI1> of the range
        """
    @overload
    def SetFirst(self,aFirst : int) -> None: ...
    def SetIndices(self,theI1 : int,theI2 : int) -> None: 
        """
        Modifier Sets the first index of the range <theI1> Sets the second index of the range <theI2>

        Modifier Sets the first index of the range <theI1> Sets the second index of the range <theI2>
        """
    @overload
    def SetLast(self,aLast : int) -> None: 
        """
        Modifier Sets the second index <theI2> of the range

        Modifier Sets the second index <theI2> of the range
        """
    @overload
    def SetLast(self,theI2 : int) -> None: ...
    def __init__(self) -> None: ...
    pass
class BOPDS_IndexedDataMapOfPaveBlockListOfInteger(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : BOPDS_PaveBlock,theItem : OCP.TColStd.TColStd_ListOfInteger) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfInteger) -> BOPDS_IndexedDataMapOfPaveBlockListOfInteger: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL if Key was not found.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : BOPDS_PaveBlock) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfInteger) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : BOPDS_PaveBlock,theValue : OCP.TColStd.TColStd_ListOfInteger) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: ...
    def FindIndex(self,theKey1 : BOPDS_PaveBlock) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> BOPDS_PaveBlock: 
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
    def RemoveKey(self,theKey1 : BOPDS_PaveBlock) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : BOPDS_PaveBlock) -> OCP.TColStd.TColStd_ListOfInteger: 
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
    def Substitute(self,theIndex : int,theKey1 : BOPDS_PaveBlock,theItem : OCP.TColStd.TColStd_ListOfInteger) -> None: 
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
    def __init__(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfInteger) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : BOPDS_PaveBlock,theItem : BOPDS_ListOfPaveBlock) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock) -> BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
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
    def Contains(self,theKey1 : BOPDS_PaveBlock) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : BOPDS_PaveBlock,theValue : BOPDS_ListOfPaveBlock) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: ...
    def FindIndex(self,theKey1 : BOPDS_PaveBlock) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> BOPDS_PaveBlock: 
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
    def RemoveKey(self,theKey1 : BOPDS_PaveBlock) -> None: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Seek(self,theKey1 : BOPDS_PaveBlock) -> BOPDS_ListOfPaveBlock: 
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
    def Substitute(self,theIndex : int,theKey1 : BOPDS_PaveBlock,theItem : BOPDS_ListOfPaveBlock) -> None: 
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
    def __init__(self,theOther : BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1.. Extent. An Item is stored with each key.
    """
    def Add(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : BOPDS_CoupleOfPaveBlocks) -> int: 
        """
        Returns the Index of already bound Key or appends new Key with specified Item value.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks) -> BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def ChangeFromIndex(self,theIndex : int) -> BOPDS_CoupleOfPaveBlocks: 
        """
        ChangeFromIndex
        """
    def ChangeFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
        """
        ChangeFromKey
        """
    def ChangeSeek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
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
    def Exchange(self,theOther : BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindFromIndex(self,theIndex : int) -> BOPDS_CoupleOfPaveBlocks: 
        """
        FindFromIndex
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape,theValue : BOPDS_CoupleOfPaveBlocks) -> bool: 
        """
        FindFromKey

        Find value for key with copying.
        """
    @overload
    def FindFromKey(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: ...
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
    def Seek(self,theKey1 : OCP.TopoDS.TopoDS_Shape) -> BOPDS_CoupleOfPaveBlocks: 
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
    def Substitute(self,theIndex : int,theKey1 : OCP.TopoDS.TopoDS_Shape,theItem : BOPDS_CoupleOfPaveBlocks) -> None: 
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
    def __init__(self,theOther : BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_IndexedMapOfPaveBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : BOPDS_PaveBlock) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_IndexedMapOfPaveBlock) -> BOPDS_IndexedMapOfPaveBlock: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Contains(self,theKey1 : BOPDS_PaveBlock) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : BOPDS_IndexedMapOfPaveBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : BOPDS_PaveBlock) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> BOPDS_PaveBlock: 
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
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : BOPDS_PaveBlock) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : BOPDS_PaveBlock) -> None: 
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
    def __init__(self,theOther : BOPDS_IndexedMapOfPaveBlock) -> None: ...
    pass
class BOPDS_Interf():
    """
    The class BOPDS_Interf stores the information about the interference between two shapes. The class BOPDS_Interf is root class
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    pass
class BOPDS_InterfEE(BOPDS_Interf):
    """
    The class BOPDS_InterfEE stores the information about the interference of the type edge/edge.
    """
    def CommonPart(self) -> OCP.IntTools.IntTools_CommonPrt: 
        """
        Selector Returns the info of common part
        """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetCommonPart(self,theCP : OCP.IntTools.IntTools_CommonPrt) -> None: 
        """
        Modifier Sets the info of common part
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_InterfEF(BOPDS_Interf):
    """
    The class BOPDS_InterfEF stores the information about the interference of the type edge/face.
    """
    def CommonPart(self) -> OCP.IntTools.IntTools_CommonPrt: 
        """
        Selector Returns the info of common part
        """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetCommonPart(self,theCP : OCP.IntTools.IntTools_CommonPrt) -> None: 
        """
        Modifier Sets the info of common part
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfEZ(BOPDS_Interf):
    """
    The class BOPDS_InterfEZ stores the information about the interference of the type edge/solid.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfFF(BOPDS_Interf):
    """
    None
    """
    def ChangeCurves(self) -> BOPDS_VectorOfCurve: 
        """
        Selector/Modifier Returns the intersection curves
        """
    def ChangePoints(self) -> BOPDS_VectorOfPoint: 
        """
        Selector/Modifier Returns the intersection points
        """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    def Curves(self) -> BOPDS_VectorOfCurve: 
        """
        Selector Returns the intersection curves
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def Init(self,theNbCurves : int,theNbPoints : int) -> None: 
        """
        Initializer
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def Points(self) -> BOPDS_VectorOfPoint: 
        """
        Selector Returns the intersection points
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    def SetTangentFaces(self,theFlag : bool) -> None: 
        """
        Modifier Sets the flag of whether the faces are tangent
        """
    def TangentFaces(self) -> bool: 
        """
        Selector Returns the flag whether the faces are tangent
        """
    def __init__(self) -> None: ...
    pass
class BOPDS_InterfFZ(BOPDS_Interf):
    """
    The class BOPDS_InterfFZ stores the information about the interference of the type face/solid.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfVE(BOPDS_Interf):
    """
    The class BOPDS_InterfVE stores the information about the interference of the type vertex/edge.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def Parameter(self) -> float: 
        """
        Selector Returrns the value of parameter of the point of the vertex on the curve of the edge
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    def SetParameter(self,theT : float) -> None: 
        """
        Modifier Sets the value of parameter of the point of the vertex on the curve of the edge
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfVF(BOPDS_Interf):
    """
    The class BOPDS_InterfVF stores the information about the interference of the type vertex/face
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    def SetUV(self,theU : float,theV : float) -> None: 
        """
        Modifier Sets the value of parameters of the point of the vertex on the surface of of the face
        """
    def UV(self) -> Tuple[float, float]: 
        """
        Selector Returns the value of parameters of the point of the vertex on the surface of of the face
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_InterfVV(BOPDS_Interf):
    """
    The class BOPDS_InterfVV stores the information about the interference of the type vertex/vertex.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfVZ(BOPDS_Interf):
    """
    The class BOPDS_InterfVZ stores the information about the interference of the type vertex/solid.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_InterfZZ(BOPDS_Interf):
    """
    The class BOPDS_InterfZZ stores the information about the interference of the type solid/solid.
    """
    def Contains(self,theIndex : int) -> bool: 
        """
        Returns true if the interference contains given index
        """
    @overload
    def HasIndexNew(self) -> bool: 
        """
        Returns true if the interference has index of new shape that is equal to the given index

        Returns true if the interference has index of new shape the index
        """
    @overload
    def HasIndexNew(self,theIndex : int) -> bool: ...
    def Index1(self) -> int: 
        """
        Returns the index of the first interferred shape
        """
    def Index2(self) -> int: 
        """
        Returns the index of the second interferred shape
        """
    def IndexNew(self) -> int: 
        """
        Returns the index of new shape
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Returns the indices of interferred shapes
        """
    def OppositeIndex(self,theI : int) -> int: 
        """
        Returns the index of that are opposite to the given index
        """
    def SetIndex1(self,theIndex : int) -> None: 
        """
        Sets the index of the first interferred shape
        """
    def SetIndex2(self,theIndex : int) -> None: 
        """
        Sets the index of the second interferred shape
        """
    def SetIndexNew(self,theIndex : int) -> None: 
        """
        Sets the index of new shape
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices of interferred shapes
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_ListOfPave(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : BOPDS_Pave) -> BOPDS_Pave: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theOther : BOPDS_ListOfPave) -> None: ...
    @overload
    def Append(self,theItem : BOPDS_Pave,theIter : Any) -> None: ...
    def Assign(self,theOther : BOPDS_ListOfPave) -> BOPDS_ListOfPave: 
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
    def First(self) -> BOPDS_Pave: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : BOPDS_ListOfPave,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : BOPDS_Pave,theIter : Any) -> BOPDS_Pave: ...
    @overload
    def InsertBefore(self,theOther : BOPDS_ListOfPave,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : BOPDS_Pave,theIter : Any) -> BOPDS_Pave: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPDS_Pave: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theItem : BOPDS_Pave) -> BOPDS_Pave: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theOther : BOPDS_ListOfPave) -> None: ...
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_ListOfPave) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_ListOfPaveBlock(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : BOPDS_ListOfPaveBlock) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : BOPDS_PaveBlock,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : BOPDS_PaveBlock) -> BOPDS_PaveBlock: ...
    def Assign(self,theOther : BOPDS_ListOfPaveBlock) -> BOPDS_ListOfPaveBlock: 
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
    def First(self) -> BOPDS_PaveBlock: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : BOPDS_PaveBlock,theIter : Any) -> BOPDS_PaveBlock: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : BOPDS_ListOfPaveBlock,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : BOPDS_PaveBlock,theIter : Any) -> BOPDS_PaveBlock: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : BOPDS_ListOfPaveBlock,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> BOPDS_PaveBlock: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : BOPDS_ListOfPaveBlock) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : BOPDS_PaveBlock) -> BOPDS_PaveBlock: ...
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
    def __init__(self,theOther : BOPDS_ListOfPaveBlock) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_MapOfCommonBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : BOPDS_CommonBlock) -> bool: 
        """
        Add
        """
    def Added(self,K : BOPDS_CommonBlock) -> BOPDS_CommonBlock: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_MapOfCommonBlock) -> BOPDS_MapOfCommonBlock: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : BOPDS_CommonBlock) -> bool: ...
    def Differ(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : BOPDS_MapOfCommonBlock,theRight : BOPDS_MapOfCommonBlock) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : BOPDS_MapOfCommonBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : BOPDS_MapOfCommonBlock,theRight : BOPDS_MapOfCommonBlock) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : BOPDS_CommonBlock) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : BOPDS_MapOfCommonBlock,theRight : BOPDS_MapOfCommonBlock) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : BOPDS_MapOfCommonBlock,theRight : BOPDS_MapOfCommonBlock) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : BOPDS_MapOfCommonBlock) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_MapOfCommonBlock) -> None: ...
    pass
class BOPDS_MapOfPair(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : BOPDS_Pair) -> bool: 
        """
        Add
        """
    def Added(self,K : BOPDS_Pair) -> BOPDS_Pair: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_MapOfPair) -> BOPDS_MapOfPair: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,K : BOPDS_Pair) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,theOther : BOPDS_MapOfPair) -> bool: ...
    def Differ(self,theOther : BOPDS_MapOfPair) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : BOPDS_MapOfPair,theRight : BOPDS_MapOfPair) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : BOPDS_MapOfPair) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : BOPDS_MapOfPair) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : BOPDS_MapOfPair) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : BOPDS_MapOfPair,theRight : BOPDS_MapOfPair) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : BOPDS_MapOfPair) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : BOPDS_Pair) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : BOPDS_MapOfPair) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : BOPDS_MapOfPair,theRight : BOPDS_MapOfPair) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : BOPDS_MapOfPair,theRight : BOPDS_MapOfPair) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : BOPDS_MapOfPair) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_MapOfPair) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class BOPDS_MapOfPave(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : BOPDS_Pave) -> bool: 
        """
        Add
        """
    def Added(self,K : BOPDS_Pave) -> BOPDS_Pave: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_MapOfPave) -> BOPDS_MapOfPave: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    @overload
    def Contains(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : BOPDS_Pave) -> bool: ...
    def Differ(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : BOPDS_MapOfPave,theRight : BOPDS_MapOfPave) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : BOPDS_MapOfPave) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : BOPDS_MapOfPave) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : BOPDS_MapOfPave,theRight : BOPDS_MapOfPave) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : BOPDS_Pave) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : BOPDS_MapOfPave,theRight : BOPDS_MapOfPave) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : BOPDS_MapOfPave,theRight : BOPDS_MapOfPave) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : BOPDS_MapOfPave) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_MapOfPave) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    pass
class BOPDS_MapOfPaveBlock(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: Single hashed Map. This Map is used to store and retrieve keys in linear time.
    """
    def Add(self,K : BOPDS_PaveBlock) -> bool: 
        """
        Add
        """
    def Added(self,K : BOPDS_PaveBlock) -> BOPDS_PaveBlock: 
        """
        Added: add a new key if not yet in the map, and return reference to either newly added or previously existing object
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : BOPDS_MapOfPaveBlock) -> BOPDS_MapOfPaveBlock: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def Contains(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Contains

        Returns true if this map contains ALL keys of another map.
        """
    @overload
    def Contains(self,K : BOPDS_PaveBlock) -> bool: ...
    def Differ(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Apply to this Map the symmetric difference (aka exclusive disjunction, boolean XOR) operation with another (given) Map. The result contains the values that are contained only in this or the operand map, but not in both. This algorithm is similar to method Difference(). Returns True if contents of this map is changed.
        """
    def Difference(self,theLeft : BOPDS_MapOfPaveBlock,theRight : BOPDS_MapOfPaveBlock) -> None: 
        """
        Sets this Map to be the result of symmetric difference (aka exclusive disjunction, boolean XOR) operation between two given Maps. The new Map contains the values that are contained only in the first or the second operand maps but not in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be used as one of operands.
        """
    def Exchange(self,theOther : BOPDS_MapOfPaveBlock) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def HasIntersection(self,theMap : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Returns true if this and theMap have common elements.
        """
    def Intersect(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Apply to this Map the intersection operation (aka multiplication, common, boolean AND) with another (given) Map. The result contains only the values that are contained in both this and the given maps. This algorithm is similar to method Intersection(). Returns True if contents of this map is changed.
        """
    def Intersection(self,theLeft : BOPDS_MapOfPaveBlock,theRight : BOPDS_MapOfPaveBlock) -> None: 
        """
        Sets this Map to be the result of intersection (aka multiplication, common, boolean AND) operation between two given Maps. The new Map contains only the values that are contained in both map operands. All previous content of this Map is cleared. This same map (result of the boolean operation) can also be used as one of operands.
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def IsEqual(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Returns true if two maps contains exactly the same keys
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Remove(self,K : BOPDS_PaveBlock) -> bool: 
        """
        Remove
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def Subtract(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Apply to this Map the subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation with another (given) Map. The result contains only the values that were previously contained in this map and not contained in this map. This algorithm is similar to method Subtract() with two operands. Returns True if contents of this map is changed.
        """
    def Subtraction(self,theLeft : BOPDS_MapOfPaveBlock,theRight : BOPDS_MapOfPaveBlock) -> None: 
        """
        Sets this Map to be the result of subtraction (aka set-theoretic difference, relative complement, exclude, cut, boolean NOT) operation between two given Maps. The new Map contains only the values that are contained in the first map operands and not contained in the second one. All previous content of this Map is cleared.
        """
    def Union(self,theLeft : BOPDS_MapOfPaveBlock,theRight : BOPDS_MapOfPaveBlock) -> None: 
        """
        Sets this Map to be the result of union (aka addition, fuse, merge, boolean OR) operation between two given Maps The new Map contains the values that are contained either in the first map or in the second map or in both. All previous content of this Map is cleared. This map (result of the boolean operation) can also be passed as one of operands.
        """
    def Unite(self,theOther : BOPDS_MapOfPaveBlock) -> bool: 
        """
        Apply to this Map the boolean operation union (aka addition, fuse, merge, boolean OR) with another (given) Map. The result contains the values that were previously contained in this map or contained in the given (operand) map. This algorithm is similar to method Union(). Returns True if contents of this map is changed.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_MapOfPaveBlock) -> None: ...
    pass
class BOPDS_Pair():
    """
    The class is to provide the pair of indices of interfering shapes.
    """
    def HashCode(self,theUpperBound : int) -> int: 
        """
        Computes a hash code for this pair, in the range [1, theUpperBound]
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Gets the indices
        """
    def IsEqual(self,theOther : BOPDS_Pair) -> bool: 
        """
        Returns true if the Pair is equal to <the theOther>
        """
    def SetIndices(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Sets the indices
        """
    @overload
    def __init__(self,theIndex1 : int,theIndex2 : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_PairMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(thePair : BOPDS_Pair,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given pair, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(thePair1 : BOPDS_Pair,thePair2 : BOPDS_Pair) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BOPDS_Pave():
    """
    The class BOPDS_Pave is to store information about vertex on an edge
    """
    def Contents(self) -> Tuple[int, float]: 
        """
        Selector Returns the index of vertex <theIndex> Returns the parameter of vertex <theParameter>

        Selector Returns the index of vertex <theIndex> Returns the parameter of vertex <theParameter>
        """
    def Dump(self) -> None: 
        """
        None
        """
    def Index(self) -> int: 
        """
        Selector Returns the index of vertex

        Selector Returns the index of vertex
        """
    def IsEqual(self,theOther : BOPDS_Pave) -> bool: 
        """
        Query Returns true if thr parameter od this is equal to the parameter of <theOther>

        Query Returns true if thr parameter od this is equal to the parameter of <theOther>
        """
    def IsLess(self,theOther : BOPDS_Pave) -> bool: 
        """
        Query Returns true if thr parameter od this is less than the parameter of <theOther>

        Query Returns true if thr parameter od this is less than the parameter of <theOther>
        """
    def Parameter(self) -> float: 
        """
        Selector Returns the parameter of vertex

        Selector Returns the parameter of vertex
        """
    def SetIndex(self,theIndex : int) -> None: 
        """
        Modifier Sets the index of vertex <theIndex>

        Modifier Sets the index of vertex <theIndex>
        """
    def SetParameter(self,theParameter : float) -> None: 
        """
        Modifier Sets the parameter of vertex <theParameter>

        Modifier Sets the parameter of vertex <theParameter>
        """
    def __init__(self) -> None: ...
    pass
class BOPDS_PaveBlock(OCP.Standard.Standard_Transient):
    """
    The class BOPDS_PaveBlock is to store the information about pave block on an edge. Two adjacent paves on edge make up pave block.The class BOPDS_PaveBlock is to store the information about pave block on an edge. Two adjacent paves on edge make up pave block.The class BOPDS_PaveBlock is to store the information about pave block on an edge. Two adjacent paves on edge make up pave block.
    """
    def AppendExtPave(self,thePave : BOPDS_Pave) -> None: 
        """
        Modifier Appends extra paves <thePave>
        """
    def AppendExtPave1(self,thePave : BOPDS_Pave) -> None: 
        """
        Modifier Appends extra pave <thePave>
        """
    def ChangeExtPaves(self) -> BOPDS_ListOfPave: 
        """
        Selector / Modifier Returns the extra paves
        """
    def ContainsParameter(self,thePrm : float,theTol : float,theInd : int) -> bool: 
        """
        Query Returns true if the extra paves contain the pave with given value of the parameter <thePrm> <theTol> - the value of the tolerance to compare <theInd> - index of the found pave
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dump(self) -> None: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> int: 
        """
        Selector Returns the index of edge of pave block
        """
    def ExtPaves(self) -> BOPDS_ListOfPave: 
        """
        Selector Returns the extra paves
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def HasEdge(self) -> bool: 
        """
        Query Returns true if the pave block has edge

        Query Returns true if the pave block has edge Returns the index of edge <theEdge>
        """
    @overload
    def HasEdge(self,theEdge : int) -> bool: ...
    def HasSameBounds(self,theOther : BOPDS_PaveBlock) -> bool: 
        """
        Query Returns true if the pave block has pave indices that equal to the pave indices of the pave block <theOther>
        """
    def HasShrunkData(self) -> bool: 
        """
        Query Returns true if the pave block contains the shrunk data
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Tuple[int, int]: 
        """
        Selector Returns the pave indices <theIndex1,theIndex2> of the pave block
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
    def IsKind(self,theTypeName : str) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    def IsSplitEdge(self) -> bool: 
        """
        Query Returns true if the edge is equal to the original edge of the pave block
        """
    def IsSplittable(self) -> bool: 
        """
        Query Returns FALSE if the pave block has a too short shrunk range and cannot be split, otherwise returns TRUE
        """
    def IsToUpdate(self) -> bool: 
        """
        Query Returns true if the pave block contains extra paves
        """
    def OriginalEdge(self) -> int: 
        """
        Selector Returns the index of original edge of pave block
        """
    def Pave1(self) -> BOPDS_Pave: 
        """
        Selector Returns the first pave
        """
    def Pave2(self) -> BOPDS_Pave: 
        """
        Selector Returns the second pave
        """
    def Range(self) -> Tuple[float, float]: 
        """
        Selector Returns the parametric range <theT1,theT2> of the pave block
        """
    def RemoveExtPave(self,theVertNum : int) -> None: 
        """
        Modifier Removes a pave with the given vertex number from extra paves
        """
    def SetEdge(self,theEdge : int) -> None: 
        """
        Modifier Sets the index of edge of pave block <theEdge>
        """
    def SetOriginalEdge(self,theEdge : int) -> None: 
        """
        Modifier Sets the index of original edge of the pave block <theEdge>
        """
    def SetPave1(self,thePave : BOPDS_Pave) -> None: 
        """
        Modifier Sets the first pave <thePave>
        """
    def SetPave2(self,thePave : BOPDS_Pave) -> None: 
        """
        Modifier Sets the second pave <thePave>
        """
    def SetShrunkData(self,theTS1 : float,theTS2 : float,theBox : OCP.Bnd.Bnd_Box,theIsSplittable : bool) -> None: 
        """
        Modifier Sets the shrunk data for the pave block <theTS1>, <theTS2> - shrunk range <theBox> - the bounding box <theIsSplittable> - defines whether the edge can be split
        """
    def ShrunkData(self,theBox : OCP.Bnd.Bnd_Box) -> Tuple[float, float, bool]: 
        """
        Selector Returns the shrunk data for the pave block <theTS1>, <theTS2> - shrunk range <theBox> - the bounding box <theIsSplittable> - defines whether the edge can be split
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,theLPB : BOPDS_ListOfPaveBlock,theFlag : bool=True) -> None: 
        """
        Modifier Updates the pave block. The extra paves are used to create new pave blocks <theLPB>. <theFlag> - if true, the first pave and the second pave are used to produce new pave blocks.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
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
class BOPDS_PaveMapHasher():
    """
    None
    """
    @staticmethod
    def HashCode_s(thePave : BOPDS_Pave,theUpperBound : int) -> int: 
        """
        Computes a hash code for the given pave, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(aPave1 : BOPDS_Pave,aPave2 : BOPDS_Pave) -> bool: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BOPDS_Point():
    """
    The class BOPDS_Point is to store the information about intersection point
    """
    def Index(self) -> int: 
        """
        Selector Returns index of the vertex

        Selector Returns index of the vertex
        """
    def Pnt(self) -> OCP.gp.gp_Pnt: 
        """
        Selector Returns 3D point

        Selector Returns 3D point
        """
    def Pnt2D1(self) -> OCP.gp.gp_Pnt2d: 
        """
        Selector Returns 2D point on the first face <thePnt>

        Selector Returns 2D point on the first face <thePnt>
        """
    def Pnt2D2(self) -> OCP.gp.gp_Pnt2d: 
        """
        Selector Returns 2D point on the second face <thePnt>

        Selector Returns 2D point on the second face <thePnt>
        """
    def SetIndex(self,theIndex : int) -> None: 
        """
        Modifier Sets the index of the vertex <theIndex>

        Modifier Sets the index of the vertex <theIndex>
        """
    def SetPnt(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Modifier Sets 3D point <thePnt>

        Modifier Sets 3D point <thePnt>
        """
    def SetPnt2D1(self,thePnt : OCP.gp.gp_Pnt2d) -> None: 
        """
        Modifier Sets 2D point on the first face <thePnt>

        Modifier Sets 2D point on the first face <thePnt>
        """
    def SetPnt2D2(self,thePnt : OCP.gp.gp_Pnt2d) -> None: 
        """
        Modifier Sets 2D point on the second face <thePnt>

        Modifier Sets 2D point on the second face <thePnt>
        """
    def __init__(self) -> None: ...
    pass
class BOPDS_ShapeInfo():
    """
    The class BOPDS_ShapeInfo is to store handy information about shape
    """
    def Box(self) -> OCP.Bnd.Bnd_Box: 
        """
        Selector Returns the boundung box of the shape

        Selector Returns the boundung box of the shape
        """
    def ChangeBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Selector/Modifier Returns the boundung box of the shape

        Selector/Modifier Returns the boundung box of the shape
        """
    def ChangeSubShapes(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Selector/ Modifier Returns the list of indices of sub-shapes

        Selector/ Modifier Returns the list of indices of sub-shapes
        """
    def Dump(self) -> None: 
        """
        None
        """
    def Flag(self) -> int: 
        """
        Returns the flag

        Returns the flag
        """
    def HasBRep(self) -> bool: 
        """
        Query Returns true if the shape has boundary representation

        Query Returns true if the shape has boundary representation
        """
    @overload
    def HasFlag(self) -> bool: 
        """
        Query Returns true if there is flag.

        Query Returns true if there is flag. Returns the flag theFlag

        Query Returns true if there is flag.

        Query Returns true if there is flag. Returns the flag theFlag
        """
    @overload
    def HasFlag(self,theFlag : int) -> bool: ...
    def HasReference(self) -> bool: 
        """
        None

        None
        """
    def HasSubShape(self,theI : int) -> bool: 
        """
        Query Returns true if the shape has sub-shape with index theI

        Query Returns true if the shape has sub-shape with index theI
        """
    def IsInterfering(self) -> bool: 
        """
        Returns true if the shape can be participant of an interference

        Returns true if the shape can be participant of an interference
        """
    def Reference(self) -> int: 
        """
        Selector Returns the index of a reference information

        Selector Returns the index of a reference information
        """
    def SetBox(self,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        Modifier Sets the boundung box of the shape theBox

        Modifier Sets the boundung box of the shape theBox
        """
    @overload
    def SetFlag(self,theFlag : int) -> None: 
        """
        Modifier Sets the flag

        Modifier Sets the flag
        """
    @overload
    def SetFlag(self,theI : int) -> None: ...
    def SetReference(self,theI : int) -> None: 
        """
        Modifier Sets the index of a reference information

        Modifier Sets the index of a reference information
        """
    def SetShape(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Modifier Sets the shape <theS>

        Modifier Sets the shape <theS>
        """
    def SetShapeType(self,theType : OCP.TopAbs.TopAbs_ShapeEnum) -> None: 
        """
        Modifier Sets the type of shape theType

        Modifier Sets the type of shape theType
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Selector Returns the shape

        Selector Returns the shape
        """
    def ShapeType(self) -> OCP.TopAbs.TopAbs_ShapeEnum: 
        """
        Selector Returns the type of shape

        Selector Returns the type of shape
        """
    def SubShapes(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Selector Returns the list of indices of sub-shapes

        Selector Returns the list of indices of sub-shapes
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BOPDS_SubIterator():
    """
    The class BOPDS_SubIterator is used to compute intersections between bounding boxes of two sub-sets of BRep sub-shapes of arguments of an operation (see the class BOPDS_DS). The class provides interface to iterate the pairs of intersected sub-shapes.
    """
    def DS(self) -> BOPDS_DS: 
        """
        Returns the data structure
        """
    def ExpectedLength(self) -> int: 
        """
        Returns the number of interfering pairs
        """
    def Initialize(self) -> None: 
        """
        Initializes the iterator
        """
    def More(self) -> bool: 
        """
        Returns true if there are more pairs of intersected shapes
        """
    def Next(self) -> None: 
        """
        Moves iterations ahead
        """
    def Prepare(self) -> None: 
        """
        Perform the intersection algorithm and prepare the results to be used
        """
    def SetSubSet1(self,theLI : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Sets the first set of indices <theLI> to process
        """
    def SetSubSet2(self,theLI : OCP.TColStd.TColStd_ListOfInteger) -> None: 
        """
        Sets the second set of indices <theLI> to process
        """
    def SubSet1(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Returns the first set of indices to process
        """
    def SubSet2(self) -> OCP.TColStd.TColStd_ListOfInteger: 
        """
        Returns the second set of indices to process
        """
    def Value(self) -> Tuple[int, int]: 
        """
        Returns indices (DS) of intersected shapes theIndex1 - the index of the first shape theIndex2 - the index of the second shape
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    pass
class BOPDS_Tools():
    """
    The class BOPDS_Tools contains a set auxiliary static functions of the package BOPDS
    """
    @staticmethod
    def HasBRep_s(theT : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        Returns true if the type <theT> correspond to a shape having boundary representation
        """
    @staticmethod
    def IsInterfering_s(theT : OCP.TopAbs.TopAbs_ShapeEnum) -> bool: 
        """
        Returns true if the type <theT> can be participant of an interference
        """
    @staticmethod
    @overload
    def TypeToInteger_s(theT : OCP.TopAbs.TopAbs_ShapeEnum) -> int: 
        """
        Converts the conmbination of two types of shape <theT1>,<theT2> to the one integer value, that is returned

        Converts the type of shape <theT>, to integer value, that is returned
        """
    @staticmethod
    @overload
    def TypeToInteger_s(theT1 : OCP.TopAbs.TopAbs_ShapeEnum,theT2 : OCP.TopAbs.TopAbs_ShapeEnum) -> int: ...
    def __init__(self) -> None: ...
    pass
class BOPDS_VectorOfCurve(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_Curve) -> BOPDS_Curve: 
        """
        Append
        """
    def Appended(self) -> BOPDS_Curve: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfCurve,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_Curve: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_Curve: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_Curve: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_Curve: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_Curve: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_Curve) -> BOPDS_Curve: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_Curve: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfCurve) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfFaceInfo(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_FaceInfo) -> BOPDS_FaceInfo: 
        """
        Append
        """
    def Appended(self) -> BOPDS_FaceInfo: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfFaceInfo,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_FaceInfo: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_FaceInfo: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_FaceInfo: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_FaceInfo: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_FaceInfo: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_FaceInfo) -> BOPDS_FaceInfo: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_FaceInfo: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfFaceInfo) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfIndexRange(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_IndexRange) -> BOPDS_IndexRange: 
        """
        Append
        """
    def Appended(self) -> BOPDS_IndexRange: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfIndexRange,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_IndexRange: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_IndexRange: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_IndexRange: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_IndexRange: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_IndexRange: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_IndexRange) -> BOPDS_IndexRange: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_IndexRange: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfIndexRange) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfEE(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfEE) -> BOPDS_InterfEE: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfEE: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfEE,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfEE: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfEE: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfEE: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfEE: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfEE: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfEE) -> BOPDS_InterfEE: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfEE: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfEE) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfEF(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfEF) -> BOPDS_InterfEF: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfEF: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfEF,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfEF: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfEF: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfEF: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfEF: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfEF: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfEF) -> BOPDS_InterfEF: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfEF: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfEF) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfEZ(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfEZ) -> BOPDS_InterfEZ: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfEZ: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfEZ,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfEZ: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfEZ: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfEZ: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfEZ: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfEZ: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfEZ) -> BOPDS_InterfEZ: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfEZ: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfEZ) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfFF(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfFF) -> BOPDS_InterfFF: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfFF: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfFF,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfFF: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfFF: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfFF: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfFF: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfFF: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfFF) -> BOPDS_InterfFF: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfFF: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfFF) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfFZ(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfFZ) -> BOPDS_InterfFZ: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfFZ: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfFZ,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfFZ: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfFZ: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfFZ: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfFZ: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfFZ: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfFZ) -> BOPDS_InterfFZ: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfFZ: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfFZ) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfVE(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfVE) -> BOPDS_InterfVE: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfVE: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfVE,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfVE: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfVE: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfVE: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfVE: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfVE: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfVE) -> BOPDS_InterfVE: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfVE: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfVE) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfVF(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfVF) -> BOPDS_InterfVF: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfVF: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfVF,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfVF: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfVF: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfVF: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfVF: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfVF: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfVF) -> BOPDS_InterfVF: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfVF: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfVF) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfVV(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfVV) -> BOPDS_InterfVV: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfVV: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfVV,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfVV: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfVV: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfVV: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfVV: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfVV: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfVV) -> BOPDS_InterfVV: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfVV: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfVV) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfVZ(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfVZ) -> BOPDS_InterfVZ: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfVZ: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfVZ,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfVZ: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfVZ: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfVZ: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfVZ: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfVZ: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfVZ) -> BOPDS_InterfVZ: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfVZ: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfVZ) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfInterfZZ(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_InterfZZ) -> BOPDS_InterfZZ: 
        """
        Append
        """
    def Appended(self) -> BOPDS_InterfZZ: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfInterfZZ,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_InterfZZ: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_InterfZZ: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_InterfZZ: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_InterfZZ: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_InterfZZ: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_InterfZZ) -> BOPDS_InterfZZ: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_InterfZZ: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfInterfZZ) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfListOfPaveBlock(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_ListOfPaveBlock) -> BOPDS_ListOfPaveBlock: 
        """
        Append
        """
    def Appended(self) -> BOPDS_ListOfPaveBlock: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfListOfPaveBlock,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_ListOfPaveBlock: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_ListOfPaveBlock: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_ListOfPaveBlock: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_ListOfPaveBlock: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_ListOfPaveBlock) -> BOPDS_ListOfPaveBlock: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_ListOfPaveBlock: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfListOfPaveBlock) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfPair(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_Pair) -> BOPDS_Pair: 
        """
        Append
        """
    def Appended(self) -> BOPDS_Pair: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfPair,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_Pair: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_Pair: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_Pair: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_Pair: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_Pair: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_Pair) -> BOPDS_Pair: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_Pair: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfPair) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfPave():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : BOPDS_VectorOfPave) -> BOPDS_VectorOfPave: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> BOPDS_Pave: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_Pave: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_Pave: 
        """
        Variable value access
        """
    def First(self) -> BOPDS_Pave: 
        """
        Returns first element
        """
    def Init(self,theValue : BOPDS_Pave) -> None: 
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
    def Last(self) -> BOPDS_Pave: 
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
    def Move(self,theOther : BOPDS_VectorOfPave) -> BOPDS_VectorOfPave: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : BOPDS_Pave) -> None: 
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
    def Value(self,theIndex : int) -> BOPDS_Pave: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : BOPDS_Pave,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfPave) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfPoint(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_Point) -> BOPDS_Point: 
        """
        Append
        """
    def Appended(self) -> BOPDS_Point: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfPoint,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_Point: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_Point: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_Point: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_Point: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_Point: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_Point) -> BOPDS_Point: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_Point: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfPoint) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfShapeInfo(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_ShapeInfo) -> BOPDS_ShapeInfo: 
        """
        Append
        """
    def Appended(self) -> BOPDS_ShapeInfo: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfShapeInfo,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_ShapeInfo: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_ShapeInfo: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_ShapeInfo: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_ShapeInfo: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_ShapeInfo: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_ShapeInfo) -> BOPDS_ShapeInfo: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_ShapeInfo: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : BOPDS_VectorOfShapeInfo) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class BOPDS_VectorOfVectorOfPair(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : BOPDS_VectorOfPair) -> BOPDS_VectorOfPair: 
        """
        Append
        """
    def Appended(self) -> BOPDS_VectorOfPair: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : BOPDS_VectorOfVectorOfPair,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> BOPDS_VectorOfPair: 
        """
        Returns first element
        """
    def ChangeLast(self) -> BOPDS_VectorOfPair: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> BOPDS_VectorOfPair: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> BOPDS_VectorOfPair: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> BOPDS_VectorOfPair: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Total number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def SetIncrement(self,aIncrement : int) -> None: 
        """
        None
        """
    def SetValue(self,theIndex : int,theValue : BOPDS_VectorOfPair) -> BOPDS_VectorOfPair: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> BOPDS_VectorOfPair: 
        """
        None
        """
    @overload
    def __init__(self,theOther : BOPDS_VectorOfVectorOfPair) -> None: ...
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
