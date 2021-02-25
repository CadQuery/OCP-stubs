import OCP.BRepFeat
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TColGeom
import OCP.NCollection
import OCP.BRepBuilderAPI
import OCP.BRepTools
import OCP.Geom
import OCP.TColgp
import OCP.TopoDS
import OCP.BOPDS
import OCP.Standard
import OCP.LocOpe
import OCP.TopAbs
import OCP.TopTools
import OCP.BOPAlgo
import io
import OCP.Message
import OCP.gp
import OCP.IntTools
__all__  = [
"BRepFeat",
"BRepFeat_Builder",
"BRepFeat_Form",
"BRepFeat_Gluer",
"BRepFeat_MakeCylindricalHole",
"BRepFeat_MakeDPrism",
"BRepFeat_RibSlot",
"BRepFeat_MakePipe",
"BRepFeat_MakePrism",
"BRepFeat_MakeRevol",
"BRepFeat_MakeRevolutionForm",
"BRepFeat_PerfSelection",
"BRepFeat_MakeLinearForm",
"BRepFeat_SplitShape",
"BRepFeat_Status",
"BRepFeat_StatusError",
"BRepFeat_BadDirect",
"BRepFeat_BadIntersect",
"BRepFeat_EmptyBaryCurve",
"BRepFeat_EmptyCutResult",
"BRepFeat_FalseSide",
"BRepFeat_HoleTooLong",
"BRepFeat_IncDirection",
"BRepFeat_IncParameter",
"BRepFeat_IncSlidFace",
"BRepFeat_IncTypes",
"BRepFeat_IntervalOverlap",
"BRepFeat_InvFirstShape",
"BRepFeat_InvOption",
"BRepFeat_InvShape",
"BRepFeat_InvalidPlacement",
"BRepFeat_LocOpeInvNotDone",
"BRepFeat_LocOpeNotDone",
"BRepFeat_NoError",
"BRepFeat_NoExtFace",
"BRepFeat_NoFaceProf",
"BRepFeat_NoGluer",
"BRepFeat_NoIntersectF",
"BRepFeat_NoIntersectU",
"BRepFeat_NoParts",
"BRepFeat_NoProjPt",
"BRepFeat_NoSelection",
"BRepFeat_NotInitialized",
"BRepFeat_NotYetImplemented",
"BRepFeat_NullRealTool",
"BRepFeat_NullToolF",
"BRepFeat_NullToolU",
"BRepFeat_OK",
"BRepFeat_SelectionFU",
"BRepFeat_SelectionSh",
"BRepFeat_SelectionShU",
"BRepFeat_SelectionU"
]
class BRepFeat():
    """
    BRepFeat is necessary for the creation and manipulation of both form and mechanical features in a Boundary Representation framework. Form features can be depressions or protrusions and include the following types: - Cylinder - Draft Prism - Prism - Revolved feature - Pipe Depending on whether you wish to make a depression or a protrusion, you can choose your operation type between the following: - removing matter (a Boolean cut: Fuse setting 0) - adding matter (Boolean fusion: Fuse setting 1) The semantics of form feature creation is based on the construction of shapes: - for a certain length in a certain direction - up to a limiting face - from a limiting face at a height - above and/or below a plane The shape defining the construction of a feature can be either a supporting edge or a concerned area of a face. In case of supporting edge, this contour can be attached to a face of the basis shape by binding. When the contour is bound to this face, the information that the contour will slide on the face becomes available to the relevant class methods. In case of the concerned area of a face, you could, for example, cut it out and move it at a different height, which will define the limiting face of a protrusion or depression. Topological definition with local operations of this sort makes calculations simpler and faster than a global operation. The latter would entail a second phase of removing unwanted matter to get the same result. Mechanical features include ribs - protrusions - and grooves (or slots) - depressions along planar (linear) surfaces or revolution surfaces. The semantics of mechanical features is based on giving thickness to a contour. This thickness can either be unilateral - on one side of the contour - or bilateral - on both sides. As in the semantics of form features, the thickness is defined by construction of shapes in specific contexts. However, in case of mechanical features, development contexts differ. Here they include extrusion: - to a limiting face of the basis shape - to or from a limiting plane - to a height.
    """
    @staticmethod
    def Barycenter_s(S : OCP.TopoDS.TopoDS_Shape,Pt : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    @staticmethod
    def FaceUntil_s(S : OCP.TopoDS.TopoDS_Shape,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        None
        """
    @staticmethod
    def IsInside_s(F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face) -> bool: 
        """
        None
        """
    @staticmethod
    def ParametricBarycenter_s(S : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve) -> float: 
        """
        None
        """
    @staticmethod
    def ParametricMinMax_s(S : OCP.TopoDS.TopoDS_Shape,C : OCP.Geom.Geom_Curve,Ori : bool=False) -> Tuple[float, float, float, float, bool]: 
        """
        Ori = True taking account the orientation
        """
    @staticmethod
    def Print_s(SE : BRepFeat_StatusError,S : io.BytesIO) -> io.BytesIO: 
        """
        Prints the Error description of the State <St> as a String on the Stream <S> and returns <S>.
        """
    @staticmethod
    def SampleEdges_s(S : OCP.TopoDS.TopoDS_Shape,Pt : OCP.TColgp.TColgp_SequenceOfPnt) -> None: 
        """
        None
        """
    @staticmethod
    def Tool_s(SRef : OCP.TopoDS.TopoDS_Shape,Fac : OCP.TopoDS.TopoDS_Face,Orf : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopoDS.TopoDS_Solid: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class BRepFeat_Builder(OCP.BOPAlgo.BOPAlgo_BOP, OCP.BOPAlgo.BOPAlgo_ToolsProvider, OCP.BOPAlgo.BOPAlgo_Builder, OCP.BOPAlgo.BOPAlgo_BuilderShape, OCP.BOPAlgo.BOPAlgo_Algo, OCP.BOPAlgo.BOPAlgo_Options):
    """
    Provides a basic tool to implement features topological operations. The main goal of the algorithm is to perform the result of the operation according to the kept parts of the tool. Input data: a) DS; b) The kept parts of the tool; If the map of the kept parts of the tool is not filled boolean operation of the given type will be performed; c) Operation required. Steps: a) Fill myShapes, myRemoved maps; b) Rebuild edges and faces; c) Build images of the object; d) Build the result of the operation. Result: Result shape of the operation required.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddTool(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds Tool argument of the operation
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : OCP.BOPAlgo.BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def CheckSolidImages(self) -> None: 
        """
        Collects the images of the object, that contains in the images of the tool.
        """
    def Clear(self) -> None: 
        """
        Clears internal fields and arguments.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    @overload
    def FillRemoved(self,theS : OCP.TopoDS.TopoDS_Shape,theM : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        Collects the removed parts of the tool into myRemoved map.

        Adds the shape S and its sub-shapes into myRemoved map.
        """
    @overload
    def FillRemoved(self) -> None: ...
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
        """
    @staticmethod
    def GetParallelMode_s() -> bool: 
        """
        Gets the global parallel mode
        """
    def GetReport(self) -> OCP.Message.Message_Report: 
        """
        Returns report collecting all errors and warnings
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    @overload
    def Init(self,theShape : OCP.TopoDS.TopoDS_Shape,theTool : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initialyzes the object of local boolean operation.

        Initialyzes the arguments of local boolean operation.
        """
    @overload
    def Init(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def KeepPart(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds shape theS and all its sub-shapes into myShapes map.
        """
    def KeepParts(self,theIm : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Initialyzes parts of the tool for second step of algorithm. Collects shapes and all sub-shapes into myShapes map.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        None
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def PartsOfTool(self,theLT : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Collects parts of the tool.
        """
    def Perform(self) -> None: 
        """
        None
        """
    def PerformResult(self) -> None: 
        """
        Main function to build the result of the local operation required.
        """
    def PerformWithFiller(self,theFiller : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RebuildEdge(self,theE : OCP.TopoDS.TopoDS_Shape,theF : OCP.TopoDS.TopoDS_Face,theME : OCP.TopTools.TopTools_MapOfShape,aLEIm : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Rebuilds edges in accordance with the kept parts of the tool.
        """
    def RebuildFaces(self) -> None: 
        """
        Rebuilds faces in accordance with the kept parts of the tool.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @overload
    def SetOperation(self,theFuse : int) -> None: 
        """
        Sets the operation of local boolean operation. If theFuse = 0 than the operation is CUT, otherwise FUSE.

        Sets the operation of local boolean operation. If theFlag = TRUE it means that no selection of parts of the tool is needed, t.e. no second part. In that case if theFuse = 0 than operation is COMMON, otherwise CUT21. If theFlag = FALSE SetOperation(theFuse) function is called.
        """
    @overload
    def SetOperation(self,theFuse : int,theFlag : bool) -> None: ...
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theProgress : OCP.Message.Message_ProgressScope) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the Tool arguments of the operation
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments of the operation
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    pass
class BRepFeat_Form(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Provides general functions to build form features. Form features can be depressions or protrusions and include the following types: - Cylinder - Draft Prism - Prism - Revolved feature - Pipe In each case, you have a choice of operation type between the following: - removing matter (a Boolean cut: Fuse setting 0) - adding matter (Boolean fusion: Fuse setting 1) The semantics of form feature creation is based on the construction of shapes: - along a length - up to a limiting face - from a limiting face to a height - above and/or below a plane The shape defining construction of the feature can be either the supporting edge or the concerned area of a face. In case of the supporting edge, this contour can be attached to a face of the basis shape by binding. When the contour is bound to this face, the information that the contour will slide on the face becomes available to the relevant class methods. In case of the concerned area of a face, you could, for example, cut it out and move it to a different height which will define the limiting face of a protrusion or depression. Topological definition with local operations of this sort makes calculations simpler and faster than a global operation. The latter would entail a second phase of removing unwanted matter to get the same result.
    """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def BasisShapeValid(self) -> None: 
        """
        Initializes the topological construction if the basis shape is present.

        Initializes the topological construction if the basis shape is present.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def Curves(self,S : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the shape <S>.
        """
    def GeneratedShapeValid(self) -> None: 
        """
        Initializes the topological construction if the generated shape S is present.

        Initializes the topological construction if the generated shape S is present.
        """
    def GluedFacesValid(self) -> None: 
        """
        Initializes the topological construction if the glued face is present.

        Initializes the topological construction if the glued face is present.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def PerfSelectionValid(self) -> None: 
        """
        Initializes the topological construction if the selected face is present.

        Initializes the topological construction if the selected face is present.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def ShapeFromValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present from the specified integer on.

        Initializes the topological construction if the shape is present from the specified integer on.
        """
    def ShapeUntilValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present until the specified integer.

        Initializes the topological construction if the shape is present until the specified integer.
        """
    def SketchFaceValid(self) -> None: 
        """
        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.

        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    pass
class BRepFeat_Gluer(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    One of the most significant aspects of BRepFeat functionality is the use of local operations as opposed to global ones. In a global operation, you would first construct a form of the type you wanted in your final feature, and then remove matter so that it could fit into your initial basis object. In a local operation, however, you specify the domain of the feature construction with aspects of the shape on which the feature is being created. These semantics are expressed in terms of a member shape of the basis shape from which - or up to which - matter will be added or removed. As a result, local operations make calculations simpler and faster than global operations. Glueing uses wires or edges of a face in the basis shape. These are to become a part of the feature. They are first cut out and then projected to a plane outside or inside the basis shape. By rebuilding the initial shape incorporating the edges and the faces of the tool, protrusion features can be constructed.
    """
    def BasisShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the basis shape of the compound shape.

        Returns the basis shape of the compound shape.
        """
    @overload
    def Bind(self,Fnew : OCP.TopoDS.TopoDS_Face,Fbase : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Defines a contact between Fnew on the new shape Snew and Fbase on the basis shape Sbase. Informs other methods that Fnew in the new shape Snew is connected to the face Fbase in the basis shape Sbase. The contact faces of the glued shape must not have parts outside the contact faces of the basis shape. This indicates that glueing is possible.

        nforms other methods that the edge Enew in the new shape is the same as the edge Ebase in the basis shape and is therefore attached to the basis shape. This indicates that glueing is possible.

        Defines a contact between Fnew on the new shape Snew and Fbase on the basis shape Sbase. Informs other methods that Fnew in the new shape Snew is connected to the face Fbase in the basis shape Sbase. The contact faces of the glued shape must not have parts outside the contact faces of the basis shape. This indicates that glueing is possible.

        nforms other methods that the edge Enew in the new shape is the same as the edge Ebase in the basis shape and is therefore attached to the basis shape. This indicates that glueing is possible.
        """
    @overload
    def Bind(self,Enew : OCP.TopoDS.TopoDS_Edge,Ebase : OCP.TopoDS.TopoDS_Edge) -> None: ...
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def GluedShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the resulting compound shape.

        Returns the resulting compound shape.
        """
    def Init(self,Snew : OCP.TopoDS.TopoDS_Shape,Sbase : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the new shape Snew and the basis shape Sbase for the local glueing operation.

        Initializes the new shape Snew and the basis shape Sbase for the local glueing operation.
        """
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        returns the status of the Face after the shape creation.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def OpeType(self) -> OCP.LocOpe.LocOpe_Operation: 
        """
        Determine which operation type to use glueing or sliding.

        Determine which operation type to use glueing or sliding.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Snew : OCP.TopoDS.TopoDS_Shape,Sbase : OCP.TopoDS.TopoDS_Shape) -> None: ...
    pass
class BRepFeat_MakeCylindricalHole(BRepFeat_Builder, OCP.BOPAlgo.BOPAlgo_BOP, OCP.BOPAlgo.BOPAlgo_ToolsProvider, OCP.BOPAlgo.BOPAlgo_Builder, OCP.BOPAlgo.BOPAlgo_BuilderShape, OCP.BOPAlgo.BOPAlgo_Algo, OCP.BOPAlgo.BOPAlgo_Options):
    """
    Provides a tool to make cylindrical holes on a shape.
    """
    def AddArgument(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds the argument to the operation.
        """
    def AddError(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as error (fail)
        """
    def AddTool(self,theShape : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds Tool argument of the operation
        """
    def AddWarning(self,theAlert : OCP.Message.Message_Alert) -> None: 
        """
        Adds the alert as warning
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns allocator
        """
    def Arguments(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of arguments.
        """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape). Invalidates the given parts of tools if any, and performs the result of the local operation.
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theObjState : OCP.TopAbs.TopAbs_State,theTools : OCP.TopTools.TopTools_ListOfShape,theToolsState : OCP.TopAbs.TopAbs_State,theReport : OCP.Message.Message_Report) -> None: 
        """
        Builds the result shape according to the given states for the objects and tools. These states can be unambiguously converted into the Boolean operation type. Thus, it performs the Boolean operation on the given groups of shapes.

        Builds the result of Boolean operation of given type basing on the result of Builder operation (GF or any other).
        """
    @overload
    def BuildBOP(self,theObjects : OCP.TopTools.TopTools_ListOfShape,theTools : OCP.TopTools.TopTools_ListOfShape,theOperation : OCP.BOPAlgo.BOPAlgo_Operation,theReport : OCP.Message.Message_Report) -> None: ...
    def CheckInverted(self) -> bool: 
        """
        Returns the flag defining whether the check for input solids on inverted status should be performed or not.
        """
    def CheckSolidImages(self) -> None: 
        """
        Collects the images of the object, that contains in the images of the tool.
        """
    def Clear(self) -> None: 
        """
        Clears internal fields and arguments.
        """
    def ClearWarnings(self) -> None: 
        """
        Clears the warnings of the algorithm
        """
    def Context(self) -> OCP.IntTools.IntTools_Context: 
        """
        Returns the Context, tool for cashing heavy algorithms.
        """
    def DumpErrors(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the error status into the given stream
        """
    def DumpWarnings(self,theOS : io.BytesIO) -> None: 
        """
        Dumps the warning statuses into the given stream
        """
    @overload
    def FillRemoved(self,theS : OCP.TopoDS.TopoDS_Shape,theM : OCP.TopTools.TopTools_MapOfShape) -> None: 
        """
        Collects the removed parts of the tool into myRemoved map.

        Adds the shape S and its sub-shapes into myRemoved map.
        """
    @overload
    def FillRemoved(self) -> None: ...
    def FuzzyValue(self) -> float: 
        """
        Returns the additional tolerance
        """
    def Generated(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Generated from the shape theS.
        """
    @staticmethod
    def GetParallelMode_s() -> bool: 
        """
        Gets the global parallel mode
        """
    def GetReport(self) -> OCP.Message.Message_Report: 
        """
        Returns report collecting all errors and warnings
        """
    def Glue(self) -> OCP.BOPAlgo.BOPAlgo_GlueEnum: 
        """
        Returns the glue option of the algorithm
        """
    def HasDeleted(self) -> bool: 
        """
        Returns true if any of the input shapes has been deleted during operation.
        """
    def HasError(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated error of specified type
        """
    def HasErrors(self) -> bool: 
        """
        Returns true if algorithm has failed
        """
    def HasGenerated(self) -> bool: 
        """
        Returns true if any of the input shapes has generated shapes during operation.
        """
    def HasHistory(self) -> bool: 
        """
        Returns flag of history availability
        """
    def HasModified(self) -> bool: 
        """
        Returns true if any of the input shapes has been modified during operation.
        """
    def HasWarning(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if algorithm has generated warning of specified type
        """
    def HasWarnings(self) -> bool: 
        """
        Returns true if algorithm has generated some warning alerts
        """
    def History(self) -> OCP.BRepTools.BRepTools_History: 
        """
        History Tool
        """
    def Images(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of images.
        """
    @overload
    def Init(self,Axis : OCP.gp.gp_Ax1) -> None: 
        """
        Sets the axis of the hole(s).

        Sets the shape and axis on which hole(s) will be performed.

        Sets the axis of the hole(s).

        Sets the shape and axis on which hole(s) will be performed.
        """
    @overload
    def Init(self,S : OCP.TopoDS.TopoDS_Shape,Axis : OCP.gp.gp_Ax1) -> None: ...
    def IsDeleted(self,theS : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape theS has been deleted. In this case the shape will have no Modified elements, but can have Generated elements.
        """
    def KeepPart(self,theS : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Adds shape theS and all its sub-shapes into myShapes map.
        """
    def KeepParts(self,theIm : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Initialyzes parts of the tool for second step of algorithm. Collects shapes and all sub-shapes into myShapes map.
        """
    def Modified(self,theS : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes Modified from the shape theS.
        """
    def NonDestructive(self) -> bool: 
        """
        Returns the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated.
        """
    def Operation(self) -> OCP.BOPAlgo.BOPAlgo_Operation: 
        """
        None
        """
    def Origins(self) -> OCP.TopTools.TopTools_DataMapOfShapeListOfShape: 
        """
        Returns the map of origins.
        """
    def PDS(self) -> OCP.BOPDS.BOPDS_DS: 
        """
        Returns the Data Structure, holder of intersection information.
        """
    def PPaveFiller(self) -> OCP.BOPAlgo.BOPAlgo_PaveFiller: 
        """
        Returns the PaveFiller, algorithm for sub-shapes intersection.
        """
    def PartsOfTool(self,theLT : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Collects parts of the tool.
        """
    @overload
    def Perform(self,Radius : float,PFrom : float,PTo : float,WithControl : bool=True) -> None: 
        """
        Performs every holes of radius <Radius>. This command has the same effect as a cut operation with an infinite cylinder defined by the given axis and <Radius>.

        Performs evry hole of radius <Radius> located between PFrom and PTo on the given axis. If <WithControl> is set to Standard_False no control are done on the resulting shape after the operation is performed.
        """
    @overload
    def Perform(self,Radius : float) -> None: ...
    def PerformBlind(self,Radius : float,Length : float,WithControl : bool=True) -> None: 
        """
        Performs a blind hole of radius <Radius> and length <Length>. The length is measured from the origin of the given axis. If <WithControl> is set to Standard_False no control are done after the operation is performed.
        """
    def PerformResult(self) -> None: 
        """
        Main function to build the result of the local operation required.
        """
    def PerformThruNext(self,Radius : float,WithControl : bool=True) -> None: 
        """
        Performs the first hole of radius <Radius>, in the direction of the defined axis. First hole signify first encountered after the origin of the axis. If <WithControl> is set to Standard_False no control are done on the resulting shape after the operation is performed.
        """
    def PerformUntilEnd(self,Radius : float,WithControl : bool=True) -> None: 
        """
        Performs evry holes of radius <Radius> located after the origin of the given axis. If <WithControl> is set to Standard_False no control are done on the resulting shape after the operation is performed.
        """
    def PerformWithFiller(self,theFiller : OCP.BOPAlgo.BOPAlgo_PaveFiller) -> None: 
        """
        Performs the operation with the prepared filler. The intersection will not be performed in this case.
        """
    def RebuildEdge(self,theE : OCP.TopoDS.TopoDS_Shape,theF : OCP.TopoDS.TopoDS_Face,theME : OCP.TopTools.TopTools_MapOfShape,aLEIm : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Rebuilds edges in accordance with the kept parts of the tool.
        """
    def RebuildFaces(self) -> None: 
        """
        Rebuilds faces in accordance with the kept parts of the tool.
        """
    def RunParallel(self) -> bool: 
        """
        Returns the flag of parallel processing
        """
    def SetArguments(self,theLS : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Sets the list of arguments for the operation.
        """
    def SetCheckInverted(self,theCheck : bool) -> None: 
        """
        Enables/Disables the check of the input solids for inverted status
        """
    def SetFuzzyValue(self,theFuzz : float) -> None: 
        """
        Sets the additional tolerance
        """
    def SetGlue(self,theGlue : OCP.BOPAlgo.BOPAlgo_GlueEnum) -> None: 
        """
        Sets the glue option for the algorithm
        """
    def SetNonDestructive(self,theFlag : bool) -> None: 
        """
        Sets the flag that defines the mode of treatment. In non-destructive mode the argument shapes are not modified. Instead a copy of a sub-shape is created in the result if it is needed to be updated. This flag is taken into account if internal PaveFiller is used only. In the case of calling PerformWithFiller the corresponding flag of that PaveFiller is in force.
        """
    @overload
    def SetOperation(self,theFuse : int) -> None: 
        """
        Sets the operation of local boolean operation. If theFuse = 0 than the operation is CUT, otherwise FUSE.

        Sets the operation of local boolean operation. If theFlag = TRUE it means that no selection of parts of the tool is needed, t.e. no second part. In that case if theFuse = 0 than operation is COMMON, otherwise CUT21. If theFlag = FALSE SetOperation(theFuse) function is called.
        """
    @overload
    def SetOperation(self,theFuse : int,theFlag : bool) -> None: ...
    @staticmethod
    def SetParallelMode_s(theNewMode : bool) -> None: 
        """
        Sets the global parallel mode
        """
    def SetProgressIndicator(self,theProgress : OCP.Message.Message_ProgressScope) -> None: 
        """
        Set the Progress Indicator object.
        """
    def SetRunParallel(self,theFlag : bool) -> None: 
        """
        Set the flag of parallel processing if <theFlag> is true the parallel processing is switched on if <theFlag> is false the parallel processing is switched off
        """
    def SetToFillHistory(self,theHistFlag : bool) -> None: 
        """
        Allows disabling the history collection
        """
    def SetTools(self,theShapes : OCP.TopTools.TopTools_ListOfShape) -> None: 
        """
        Adds the Tool arguments of the operation
        """
    def SetUseOBB(self,theUseOBB : bool) -> None: 
        """
        Enables/Disables the usage of OBB
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the result of algorithm
        """
    def ShapesSD(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns the map of Same Domain (SD) shapes - coinciding shapes from different arguments.
        """
    def Status(self) -> BRepFeat_Status: 
        """
        Returns the status after a hole is performed.

        Returns the status after a hole is performed.
        """
    def Tools(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the Tool arguments of the operation
        """
    def UseOBB(self) -> bool: 
        """
        Returns the flag defining usage of OBB
        """
    def __init__(self) -> None: ...
    pass
class BRepFeat_MakeDPrism(BRepFeat_Form, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build draft prism topologies from basis shape surfaces. These can be depressions or protrusions. The semantics of draft prism feature creation is based on the construction of shapes: - along a length - up to a limiting face - from a limiting face to a height. The shape defining construction of the draft prism feature can be either the supporting edge or the concerned area of a face. In case of the supporting edge, this contour can be attached to a face of the basis shape by binding. When the contour is bound to this face, the information that the contour will slide on the face becomes available to the relevant class methods. In case of the concerned area of a face, you could, for example, cut it out and move it to a different height which will define the limiting face of a protrusion or depression.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def BasisShapeValid(self) -> None: 
        """
        Initializes the topological construction if the basis shape is present.

        Initializes the topological construction if the basis shape is present.
        """
    def BossEdges(self,sig : int) -> None: 
        """
        Determination of TopEdges and LatEdges. sig = 1 -> TopEdges = FirstShape of the DPrism sig = 2 -> TOpEdges = LastShape of the DPrism
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def Curves(self,S : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the shape <S>.
        """
    def GeneratedShapeValid(self) -> None: 
        """
        Initializes the topological construction if the generated shape S is present.

        Initializes the topological construction if the generated shape S is present.
        """
    def GluedFacesValid(self) -> None: 
        """
        Initializes the topological construction if the glued face is present.

        Initializes the topological construction if the glued face is present.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Face,Skface : OCP.TopoDS.TopoDS_Face,Angle : float,Fuse : int,Modify : bool) -> None: 
        """
        Initializes this algorithm for building draft prisms along surfaces. A face Pbase is selected in the basis shape Sbase to serve as the basis from the draft prism. The draft will be defined by the angle Angle and Fuse offers a choice between: - removing matter with a Boolean cut using the setting 0 - adding matter with Boolean fusion using the setting 1. The sketch face Skface serves to determine the type of operation. If it is inside the basis shape, a local operation such as glueing can be performed.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def LatEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of TopoDS Edges of the bottom of the boss.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def PerfSelectionValid(self) -> None: 
        """
        Initializes the topological construction if the selected face is present.

        Initializes the topological construction if the selected face is present.
        """
    @overload
    def Perform(self,Until : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        Assigns one of the following semantics - to a height Height - to a face Until - from a face From to a height Until. Reconstructs the feature topologically according to the semantic option chosen.
        """
    @overload
    def Perform(self,From : OCP.TopoDS.TopoDS_Shape,Until : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def Perform(self,Height : float) -> None: ...
    def PerformFromEnd(self,FUntil : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Realizes a semi-infinite prism, limited by the face Funtil.
        """
    def PerformThruAll(self) -> None: 
        """
        Builds an infinite prism. The infinite descendants will not be kept in the result.
        """
    def PerformUntilEnd(self) -> None: 
        """
        Realizes a semi-infinite prism, limited by the position of the prism base.
        """
    def PerformUntilHeight(self,Until : OCP.TopoDS.TopoDS_Shape,Height : float) -> None: 
        """
        Assigns both a limiting shape, Until from TopoDS_Shape, and a height, Height at which to stop generation of the prism feature.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def ShapeFromValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present from the specified integer on.

        Initializes the topological construction if the shape is present from the specified integer on.
        """
    def ShapeUntilValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present until the specified integer.

        Initializes the topological construction if the shape is present until the specified integer.
        """
    def SketchFaceValid(self) -> None: 
        """
        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.

        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    def TopEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of TopoDS Edges of the top of the boss.
        """
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Face,Skface : OCP.TopoDS.TopoDS_Face,Angle : float,Fuse : int,Modify : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_RibSlot(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Provides functions to build mechanical features. Mechanical features include ribs - protrusions and grooves (or slots) - depressions along planar (linear) surfaces or revolution surfaces. The semantics of mechanical features is built around giving thickness to a contour. This thickness can either be unilateral - on one side of the contour - or bilateral - on both sides. As in the semantics of form features, the thickness is defined by construction of shapes in specific contexts. The development contexts differ, however,in case of mechanical features. Here they include extrusion: - to a limiting face of the basis shape - to or from a limiting plane - to a height.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    @staticmethod
    def ChoiceOfFaces_s(faces : OCP.TopTools.TopTools_ListOfShape,cc : OCP.Geom.Geom_Curve,par : float,bnd : float,Pln : OCP.Geom.Geom_Plane) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def FacesForDraft(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing faces generated by the feature. These faces did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of a draft to a face. It may be an empty list. If a face has tangent edges, no draft is possible, and the tangent edges must subsequently be removed if you want to add a draft to the face.
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list TopTools_ListOfShape of the faces S created in the shape.
        """
    @staticmethod
    def IntPar_s(C : OCP.Geom.Geom_Curve,P : OCP.gp.gp_Pnt) -> float: 
        """
        None
        """
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if F a TopoDS_Shape of type edge or face has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of generated Faces F. This list may be empty.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    pass
class BRepFeat_MakePipe(BRepFeat_Form, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Constructs compound shapes with pipe features. These can be depressions or protrusions. The semantics of pipe feature creation is based on the construction of shapes: - along a length - up to a limiting face - from a limiting face to a height. The shape defining construction of the pipe feature can be either the supporting edge or the concerned area of a face. In case of the supporting edge, this contour can be attached to a face of the basis shape by binding. When the contour is bound to this face, the information that the contour will slide on the face becomes available to the relevant class methods. In case of the concerned area of a face, you could, for example, cut it out and move it to a different height which will define the limiting face of a protrusion or depression.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def BasisShapeValid(self) -> None: 
        """
        Initializes the topological construction if the basis shape is present.

        Initializes the topological construction if the basis shape is present.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def Curves(self,S : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the shape <S>.
        """
    def GeneratedShapeValid(self) -> None: 
        """
        Initializes the topological construction if the generated shape S is present.

        Initializes the topological construction if the generated shape S is present.
        """
    def GluedFacesValid(self) -> None: 
        """
        Initializes the topological construction if the glued face is present.

        Initializes the topological construction if the glued face is present.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Spine : OCP.TopoDS.TopoDS_Wire,Fuse : int,Modify : bool) -> None: 
        """
        Initializes this algorithm for adding pipes to shapes. A face Pbase is selected in the shape Sbase to serve as the basis for the pipe. It will be defined by the wire Spine. Fuse offers a choice between: - removing matter with a Boolean cut using the setting 0 - adding matter with Boolean fusion using the setting 1. The sketch face Skface serves to determine the type of operation. If it is inside the basis shape, a local operation such as glueing can be performed.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def PerfSelectionValid(self) -> None: 
        """
        Initializes the topological construction if the selected face is present.

        Initializes the topological construction if the selected face is present.
        """
    @overload
    def Perform(self,From : OCP.TopoDS.TopoDS_Shape,Until : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        Assigns one of the following semantics - to a face Until - from a face From to a height Until. Reconstructs the feature topologically according to the semantic option chosen.
        """
    @overload
    def Perform(self,Until : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def Perform(self) -> None: ...
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def ShapeFromValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present from the specified integer on.

        Initializes the topological construction if the shape is present from the specified integer on.
        """
    def ShapeUntilValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present until the specified integer.

        Initializes the topological construction if the shape is present until the specified integer.
        """
    def SketchFaceValid(self) -> None: 
        """
        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.

        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Spine : OCP.TopoDS.TopoDS_Wire,Fuse : int,Modify : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_MakePrism(BRepFeat_Form, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build prism features. These can be depressions or protrusions. The semantics of prism feature creation is based on the construction of shapes: - along a length - up to a limiting face - from a limiting face to a height. The shape defining construction of the prism feature can be either the supporting edge or the concerned area of a face. In case of the supporting edge, this contour can be attached to a face of the basis shape by binding. When the contour is bound to this face, the information that the contour will slide on the face becomes available to the relevant class methods. In case of the concerned area of a face, you could, for example, cut it out and move it to a different height which will define the limiting face of a protrusion or depression.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        Generates a curve along the center of mass of the primitive.
        """
    def BasisShapeValid(self) -> None: 
        """
        Initializes the topological construction if the basis shape is present.

        Initializes the topological construction if the basis shape is present.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def Curves(self,S : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        Returns the list of curves S parallel to the axis of the prism.
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the shape <S>.
        """
    def GeneratedShapeValid(self) -> None: 
        """
        Initializes the topological construction if the generated shape S is present.

        Initializes the topological construction if the generated shape S is present.
        """
    def GluedFacesValid(self) -> None: 
        """
        Initializes the topological construction if the glued face is present.

        Initializes the topological construction if the glued face is present.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Direction : OCP.gp.gp_Dir,Fuse : int,Modify : bool) -> None: 
        """
        Initializes this algorithm for building prisms along surfaces. A face Pbase is selected in the shape Sbase to serve as the basis for the prism. The orientation of the prism will be defined by the vector Direction. Fuse offers a choice between: - removing matter with a Boolean cut using the setting 0 - adding matter with Boolean fusion using the setting 1. The sketch face Skface serves to determine the type of operation. If it is inside the basis shape, a local operation such as glueing can be performed.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def PerfSelectionValid(self) -> None: 
        """
        Initializes the topological construction if the selected face is present.

        Initializes the topological construction if the selected face is present.
        """
    @overload
    def Perform(self,From : OCP.TopoDS.TopoDS_Shape,Until : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        Assigns one of the following semantics - to a height Length - to a face Until - from a face From to a height Until. Reconstructs the feature topologically according to the semantic option chosen.
        """
    @overload
    def Perform(self,Length : float) -> None: ...
    @overload
    def Perform(self,Until : OCP.TopoDS.TopoDS_Shape) -> None: ...
    def PerformFromEnd(self,FUntil : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Realizes a semi-infinite prism, limited by the face Funtil.
        """
    def PerformThruAll(self) -> None: 
        """
        Builds an infinite prism. The infinite descendants will not be kept in the result.
        """
    def PerformUntilEnd(self) -> None: 
        """
        Realizes a semi-infinite prism, limited by the position of the prism base. All other faces extend infinitely.
        """
    def PerformUntilHeight(self,Until : OCP.TopoDS.TopoDS_Shape,Length : float) -> None: 
        """
        Assigns both a limiting shape, Until from TopoDS_Shape, and a height, Length at which to stop generation of the prism feature.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def ShapeFromValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present from the specified integer on.

        Initializes the topological construction if the shape is present from the specified integer on.
        """
    def ShapeUntilValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present until the specified integer.

        Initializes the topological construction if the shape is present until the specified integer.
        """
    def SketchFaceValid(self) -> None: 
        """
        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.

        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Direction : OCP.gp.gp_Dir,Fuse : int,Modify : bool) -> None: ...
    pass
class BRepFeat_MakeRevol(BRepFeat_Form, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build revolved shells from basis shapes.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def BarycCurve(self) -> OCP.Geom.Geom_Curve: 
        """
        None
        """
    def BasisShapeValid(self) -> None: 
        """
        Initializes the topological construction if the basis shape is present.

        Initializes the topological construction if the basis shape is present.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def Curves(self,S : OCP.TColGeom.TColGeom_SequenceOfCurve) -> None: 
        """
        None
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns a list of the created faces from the shape <S>.
        """
    def GeneratedShapeValid(self) -> None: 
        """
        Initializes the topological construction if the generated shape S is present.

        Initializes the topological construction if the generated shape S is present.
        """
    def GluedFacesValid(self) -> None: 
        """
        Initializes the topological construction if the glued face is present.

        Initializes the topological construction if the glued face is present.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Axis : OCP.gp.gp_Ax1,Fuse : int,Modify : bool) -> None: 
        """
        None
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        None
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        returns the list of generated Faces.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def PerfSelectionValid(self) -> None: 
        """
        Initializes the topological construction if the selected face is present.

        Initializes the topological construction if the selected face is present.
        """
    @overload
    def Perform(self,Until : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        None

        None

        Reconstructs the feature topologically.
        """
    @overload
    def Perform(self,From : OCP.TopoDS.TopoDS_Shape,Until : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def Perform(self,Angle : float) -> None: ...
    def PerformThruAll(self) -> None: 
        """
        Builds an infinite shell. The infinite descendants will not be kept in the result.
        """
    def PerformUntilAngle(self,Until : OCP.TopoDS.TopoDS_Shape,Angle : float) -> None: 
        """
        Assigns both a limiting shape, Until from TopoDS_Shape, and an angle, Angle at which to stop generation of the revolved shell feature.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def ShapeFromValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present from the specified integer on.

        Initializes the topological construction if the shape is present from the specified integer on.
        """
    def ShapeUntilValid(self) -> None: 
        """
        Initializes the topological construction if the shape is present until the specified integer.

        Initializes the topological construction if the shape is present until the specified integer.
        """
    def SketchFaceValid(self) -> None: 
        """
        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.

        Initializes the topological construction if the sketch face is present. If the sketch face is inside the basis shape, local operations such as glueing can be performed.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,Pbase : OCP.TopoDS.TopoDS_Shape,Skface : OCP.TopoDS.TopoDS_Face,Axis : OCP.gp.gp_Ax1,Fuse : int,Modify : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_MakeRevolutionForm(BRepFeat_RibSlot, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    MakeRevolutionForm Generates a surface of revolution in the feature as it slides along a revolved face in the basis shape. The semantics of mechanical features is built around giving thickness to a contour. This thickness can either be unilateral - on one side of the contour - or bilateral - on both sides. As in the semantics of form features, the thickness is defined by construction of shapes in specific contexts. The development contexts differ, however,in case of mechanical features. Here they include extrusion: - to a limiting face of the basis shape - to or from a limiting plane - to a height.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    @staticmethod
    def ChoiceOfFaces_s(faces : OCP.TopTools.TopTools_ListOfShape,cc : OCP.Geom.Geom_Curve,par : float,bnd : float,Pln : OCP.Geom.Geom_Plane) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def FacesForDraft(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing faces generated by the feature. These faces did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of a draft to a face. It may be an empty list. If a face has tangent edges, no draft is possible, and the tangent edges must subsequently be removed if you want to add a draft to the face.
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list TopTools_ListOfShape of the faces S created in the shape.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Wire,Plane : OCP.Geom.Geom_Plane,Axis : OCP.gp.gp_Ax1,Height1 : float,Height2 : float,Fuse : int) -> Tuple[bool]: 
        """
        Initializes this construction algorithm A contour W, a shape Sbase and a plane P are initialized to serve as the basic elements in the construction of the rib or groove. The axis Axis of the revolved surface in the basis shape defines the feature's axis of revolution. Height1 and Height2 may be used as limits to the construction of the feature. Fuse offers a choice between: - removing matter with a Boolean cut using the setting 0 in case of the groove - adding matter with Boolean fusion using the setting 1 in case of the rib.
        """
    @staticmethod
    def IntPar_s(C : OCP.Geom.Geom_Curve,P : OCP.gp.gp_Pnt) -> float: 
        """
        None
        """
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if F a TopoDS_Shape of type edge or face has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of generated Faces F. This list may be empty.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def Perform(self) -> None: 
        """
        Performs a prism from the wire to the plane along the basis shape S. Reconstructs the feature topologically.
        """
    def Propagate(self,L : OCP.TopTools.TopTools_ListOfShape,F : OCP.TopoDS.TopoDS_Face,FPoint : OCP.gp.gp_Pnt,LPoint : OCP.gp.gp_Pnt,falseside : bool) -> bool: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Wire,Plane : OCP.Geom.Geom_Plane,Axis : OCP.gp.gp_Ax1,Height1 : float,Height2 : float,Fuse : int,Sliding : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_PerfSelection():
    """
    To declare the type of selection semantics for local operation Perform methods - NoSelection - SelectionFU - selection of a face up to which a local operation will be performed - SelectionU - selection of a point up to which a local operation will be performed - SelectionSh - selection of a shape on which a local operation will be performed - SelectionShU - selection of a shape up to which a local operation will be performed.

    Members:

      BRepFeat_NoSelection

      BRepFeat_SelectionFU

      BRepFeat_SelectionU

      BRepFeat_SelectionSh

      BRepFeat_SelectionShU
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
    BRepFeat_NoSelection: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_NoSelection: 0>
    BRepFeat_SelectionFU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionFU: 1>
    BRepFeat_SelectionSh: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionSh: 3>
    BRepFeat_SelectionShU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionShU: 4>
    BRepFeat_SelectionU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionU: 2>
    __entries: dict # value = {'BRepFeat_NoSelection': (<BRepFeat_PerfSelection.BRepFeat_NoSelection: 0>, None), 'BRepFeat_SelectionFU': (<BRepFeat_PerfSelection.BRepFeat_SelectionFU: 1>, None), 'BRepFeat_SelectionU': (<BRepFeat_PerfSelection.BRepFeat_SelectionU: 2>, None), 'BRepFeat_SelectionSh': (<BRepFeat_PerfSelection.BRepFeat_SelectionSh: 3>, None), 'BRepFeat_SelectionShU': (<BRepFeat_PerfSelection.BRepFeat_SelectionShU: 4>, None)}
    __members__: dict # value = {'BRepFeat_NoSelection': <BRepFeat_PerfSelection.BRepFeat_NoSelection: 0>, 'BRepFeat_SelectionFU': <BRepFeat_PerfSelection.BRepFeat_SelectionFU: 1>, 'BRepFeat_SelectionU': <BRepFeat_PerfSelection.BRepFeat_SelectionU: 2>, 'BRepFeat_SelectionSh': <BRepFeat_PerfSelection.BRepFeat_SelectionSh: 3>, 'BRepFeat_SelectionShU': <BRepFeat_PerfSelection.BRepFeat_SelectionShU: 4>}
    pass
class BRepFeat_MakeLinearForm(BRepFeat_RibSlot, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Builds a rib or a groove along a developable, planar surface. The semantics of mechanical features is built around giving thickness to a contour. This thickness can either be symmetrical - on one side of the contour - or dissymmetrical - on both sides. As in the semantics of form features, the thickness is defined by construction of shapes in specific contexts. The development contexts differ, however, in case of mechanical features. Here they include extrusion: - to a limiting face of the basis shape - to or from a limiting plane - to a height.
    """
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,OnFace : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Indicates that the edge <E> will slide on the face <OnFace>. Raises ConstructionError if the face does not belong to the basis shape, or the edge to the prismed shape.
        """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    @staticmethod
    def ChoiceOfFaces_s(faces : OCP.TopTools.TopTools_ListOfShape,cc : OCP.Geom.Geom_Curve,par : float,bnd : float,Pln : OCP.Geom.Geom_Plane) -> OCP.TopoDS.TopoDS_Face: 
        """
        None
        """
    def CurrentStatusError(self) -> BRepFeat_StatusError: 
        """
        None
        """
    def FacesForDraft(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing faces generated by the feature. These faces did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of a draft to a face. It may be an empty list. If a face has tangent edges, no draft is possible, and the tangent edges must subsequently be removed if you want to add a draft to the face.
        """
    def FirstShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the bottom of the created form. It may be an empty list.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list TopTools_ListOfShape of the faces S created in the shape.
        """
    def Init(self,Sbase : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Wire,P : OCP.Geom.Geom_Plane,Direction : OCP.gp.gp_Vec,Direction1 : OCP.gp.gp_Vec,Fuse : int,Modify : bool) -> None: 
        """
        Initializes this construction algorithm. A contour W, a shape Sbase and a plane P are initialized to serve as the basic elements in the construction of the rib or groove. The vectors for defining the direction(s) in which thickness will be built up are given by Direction and Direction1. Fuse offers a choice between: - removing matter with a Boolean cut using the setting 0 in case of the groove - adding matter with Boolean fusion using the setting 1 in case of the rib.
        """
    @staticmethod
    def IntPar_s(C : OCP.Geom.Geom_Curve,P : OCP.gp.gp_Pnt) -> float: 
        """
        None
        """
    def IsDeleted(self,F : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if F a TopoDS_Shape of type edge or face has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes created at the top of the created form. It may be an empty list.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of generated Faces F. This list may be empty.
        """
    def NewEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape. The list provides the information necessary for subsequent addition of fillets. It may be an empty list.
        """
    def Perform(self) -> None: 
        """
        Performs a prism from the wire to the plane along the basis shape Sbase. Reconstructs the feature topologically.
        """
    def Propagate(self,L : OCP.TopTools.TopTools_ListOfShape,F : OCP.TopoDS.TopoDS_Face,FPoint : OCP.gp.gp_Pnt,LPoint : OCP.gp.gp_Pnt,falseside : bool) -> bool: 
        """
        None
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def TgtEdges(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns a list of the tangent edges among the limiting and glueing edges generated by the feature. These edges did not originally exist in the basis shape and are tangent to the face against which the feature is built. The list provides the information necessary for subsequent addition of fillets. It may be an empty list. If an edge is tangent, no fillet is possible, and the edge must subsequently be removed if you want to add a fillet.
        """
    @overload
    def __init__(self,Sbase : OCP.TopoDS.TopoDS_Shape,W : OCP.TopoDS.TopoDS_Wire,P : OCP.Geom.Geom_Plane,Direction : OCP.gp.gp_Vec,Direction1 : OCP.gp.gp_Vec,Fuse : int,Modify : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_SplitShape(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    One of the most significant aspects of BRepFeat functionality is the use of local operations as opposed to global ones. In a global operation, you would first construct a form of the type you wanted in your final feature, and then remove matter so that it could fit into your initial basis object. In a local operation, however, you specify the domain of the feature construction with aspects of the shape on which the feature is being created. These semantics are expressed in terms of a member shape of the basis shape from which - or up to which - matter will be added or removed. As a result, local operations make calculations simpler and faster than global operations. In BRepFeat, the semantics of local operations define features constructed from a contour or a part of the basis shape referred to as the tool. In a SplitShape object, wires or edges of a face in the basis shape to be used as a part of the feature are cut out and projected to a plane outside or inside the basis shape. By rebuilding the initial shape incorporating the edges and the faces of the tool, protrusion or depression features can be constructed.
    """
    @overload
    def Add(self,W : OCP.TopoDS.TopoDS_Wire,F : OCP.TopoDS.TopoDS_Face) -> None: 
        """
        Add splitting edges or wires for whole initial shape withot additional specification edge->face, edge->edge This method puts edge on the corresponding faces from initial shape

        Adds the wire <W> on the face <F>. Raises NoSuchObject if <F> does not belong to the original shape.

        Adds the edge <E> on the face <F>.

        Adds the compound <Comp> on the face <F>. The compound <Comp> must consist of edges lying on the face <F>. If edges are geometrically connected, they must be connected topologically, i.e. they must share common vertices.

        Adds the edge <E> on the existing edge <EOn>.

        Add splitting edges or wires for whole initial shape withot additional specification edge->face, edge->edge This method puts edge on the corresponding faces from initial shape

        Adds the wire <W> on the face <F>. Raises NoSuchObject if <F> does not belong to the original shape.

        Adds the edge <E> on the face <F>.

        Adds the compound <Comp> on the face <F>. The compound <Comp> must consist of edges lying on the face <F>. If edges are geometrically connected, they must be connected topologically, i.e. they must share common vertices.

        Adds the edge <E> on the existing edge <EOn>.
        """
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Add(self,E : OCP.TopoDS.TopoDS_Edge,EOn : OCP.TopoDS.TopoDS_Edge) -> None: ...
    @overload
    def Add(self,Comp : OCP.TopoDS.TopoDS_Compound,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    @overload
    def Add(self,theEdges : OCP.TopTools.TopTools_SequenceOfShape) -> bool: ...
    def Build(self) -> None: 
        """
        Builds the cut and the resulting faces and edges as well.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def DirectLeft(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces which are the left of the projected wires.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def Init(self,S : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Initializes the process on the shape <S>.

        Initializes the process on the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Left(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces of the "left" part on the shape. (It is build from DirectLeft, with the faces connected to this set, and so on...). Raises NotDone if IsDone returns <Standard_False>.
        """
    def Modified(self,F : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of generated Faces.
        """
    def Right(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the faces of the "right" part on the shape.
        """
    def SetCheckInterior(self,ToCheckInterior : bool) -> None: 
        """
        Set the flag of check internal intersections default value is True (to check)

        Set the flag of check internal intersections default value is True (to check)
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepFeat_Status():
    """
    None

    Members:

      BRepFeat_NoError

      BRepFeat_InvalidPlacement

      BRepFeat_HoleTooLong
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
    BRepFeat_HoleTooLong: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_HoleTooLong: 2>
    BRepFeat_InvalidPlacement: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_InvalidPlacement: 1>
    BRepFeat_NoError: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_NoError: 0>
    __entries: dict # value = {'BRepFeat_NoError': (<BRepFeat_Status.BRepFeat_NoError: 0>, None), 'BRepFeat_InvalidPlacement': (<BRepFeat_Status.BRepFeat_InvalidPlacement: 1>, None), 'BRepFeat_HoleTooLong': (<BRepFeat_Status.BRepFeat_HoleTooLong: 2>, None)}
    __members__: dict # value = {'BRepFeat_NoError': <BRepFeat_Status.BRepFeat_NoError: 0>, 'BRepFeat_InvalidPlacement': <BRepFeat_Status.BRepFeat_InvalidPlacement: 1>, 'BRepFeat_HoleTooLong': <BRepFeat_Status.BRepFeat_HoleTooLong: 2>}
    pass
class BRepFeat_StatusError():
    """
    Discribes the error.

    Members:

      BRepFeat_OK

      BRepFeat_BadDirect

      BRepFeat_BadIntersect

      BRepFeat_EmptyBaryCurve

      BRepFeat_EmptyCutResult

      BRepFeat_FalseSide

      BRepFeat_IncDirection

      BRepFeat_IncSlidFace

      BRepFeat_IncParameter

      BRepFeat_IncTypes

      BRepFeat_IntervalOverlap

      BRepFeat_InvFirstShape

      BRepFeat_InvOption

      BRepFeat_InvShape

      BRepFeat_LocOpeNotDone

      BRepFeat_LocOpeInvNotDone

      BRepFeat_NoExtFace

      BRepFeat_NoFaceProf

      BRepFeat_NoGluer

      BRepFeat_NoIntersectF

      BRepFeat_NoIntersectU

      BRepFeat_NoParts

      BRepFeat_NoProjPt

      BRepFeat_NotInitialized

      BRepFeat_NotYetImplemented

      BRepFeat_NullRealTool

      BRepFeat_NullToolF

      BRepFeat_NullToolU
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
    BRepFeat_BadDirect: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_BadDirect: 1>
    BRepFeat_BadIntersect: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_BadIntersect: 2>
    BRepFeat_EmptyBaryCurve: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_EmptyBaryCurve: 3>
    BRepFeat_EmptyCutResult: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_EmptyCutResult: 4>
    BRepFeat_FalseSide: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_FalseSide: 5>
    BRepFeat_IncDirection: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncDirection: 6>
    BRepFeat_IncParameter: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncParameter: 8>
    BRepFeat_IncSlidFace: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncSlidFace: 7>
    BRepFeat_IncTypes: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncTypes: 9>
    BRepFeat_IntervalOverlap: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IntervalOverlap: 10>
    BRepFeat_InvFirstShape: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvFirstShape: 11>
    BRepFeat_InvOption: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvOption: 12>
    BRepFeat_InvShape: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvShape: 13>
    BRepFeat_LocOpeInvNotDone: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_LocOpeInvNotDone: 15>
    BRepFeat_LocOpeNotDone: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_LocOpeNotDone: 14>
    BRepFeat_NoExtFace: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoExtFace: 16>
    BRepFeat_NoFaceProf: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoFaceProf: 17>
    BRepFeat_NoGluer: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoGluer: 18>
    BRepFeat_NoIntersectF: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoIntersectF: 19>
    BRepFeat_NoIntersectU: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoIntersectU: 20>
    BRepFeat_NoParts: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoParts: 21>
    BRepFeat_NoProjPt: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoProjPt: 22>
    BRepFeat_NotInitialized: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NotInitialized: 23>
    BRepFeat_NotYetImplemented: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NotYetImplemented: 24>
    BRepFeat_NullRealTool: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullRealTool: 25>
    BRepFeat_NullToolF: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullToolF: 26>
    BRepFeat_NullToolU: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullToolU: 27>
    BRepFeat_OK: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_OK: 0>
    __entries: dict # value = {'BRepFeat_OK': (<BRepFeat_StatusError.BRepFeat_OK: 0>, None), 'BRepFeat_BadDirect': (<BRepFeat_StatusError.BRepFeat_BadDirect: 1>, None), 'BRepFeat_BadIntersect': (<BRepFeat_StatusError.BRepFeat_BadIntersect: 2>, None), 'BRepFeat_EmptyBaryCurve': (<BRepFeat_StatusError.BRepFeat_EmptyBaryCurve: 3>, None), 'BRepFeat_EmptyCutResult': (<BRepFeat_StatusError.BRepFeat_EmptyCutResult: 4>, None), 'BRepFeat_FalseSide': (<BRepFeat_StatusError.BRepFeat_FalseSide: 5>, None), 'BRepFeat_IncDirection': (<BRepFeat_StatusError.BRepFeat_IncDirection: 6>, None), 'BRepFeat_IncSlidFace': (<BRepFeat_StatusError.BRepFeat_IncSlidFace: 7>, None), 'BRepFeat_IncParameter': (<BRepFeat_StatusError.BRepFeat_IncParameter: 8>, None), 'BRepFeat_IncTypes': (<BRepFeat_StatusError.BRepFeat_IncTypes: 9>, None), 'BRepFeat_IntervalOverlap': (<BRepFeat_StatusError.BRepFeat_IntervalOverlap: 10>, None), 'BRepFeat_InvFirstShape': (<BRepFeat_StatusError.BRepFeat_InvFirstShape: 11>, None), 'BRepFeat_InvOption': (<BRepFeat_StatusError.BRepFeat_InvOption: 12>, None), 'BRepFeat_InvShape': (<BRepFeat_StatusError.BRepFeat_InvShape: 13>, None), 'BRepFeat_LocOpeNotDone': (<BRepFeat_StatusError.BRepFeat_LocOpeNotDone: 14>, None), 'BRepFeat_LocOpeInvNotDone': (<BRepFeat_StatusError.BRepFeat_LocOpeInvNotDone: 15>, None), 'BRepFeat_NoExtFace': (<BRepFeat_StatusError.BRepFeat_NoExtFace: 16>, None), 'BRepFeat_NoFaceProf': (<BRepFeat_StatusError.BRepFeat_NoFaceProf: 17>, None), 'BRepFeat_NoGluer': (<BRepFeat_StatusError.BRepFeat_NoGluer: 18>, None), 'BRepFeat_NoIntersectF': (<BRepFeat_StatusError.BRepFeat_NoIntersectF: 19>, None), 'BRepFeat_NoIntersectU': (<BRepFeat_StatusError.BRepFeat_NoIntersectU: 20>, None), 'BRepFeat_NoParts': (<BRepFeat_StatusError.BRepFeat_NoParts: 21>, None), 'BRepFeat_NoProjPt': (<BRepFeat_StatusError.BRepFeat_NoProjPt: 22>, None), 'BRepFeat_NotInitialized': (<BRepFeat_StatusError.BRepFeat_NotInitialized: 23>, None), 'BRepFeat_NotYetImplemented': (<BRepFeat_StatusError.BRepFeat_NotYetImplemented: 24>, None), 'BRepFeat_NullRealTool': (<BRepFeat_StatusError.BRepFeat_NullRealTool: 25>, None), 'BRepFeat_NullToolF': (<BRepFeat_StatusError.BRepFeat_NullToolF: 26>, None), 'BRepFeat_NullToolU': (<BRepFeat_StatusError.BRepFeat_NullToolU: 27>, None)}
    __members__: dict # value = {'BRepFeat_OK': <BRepFeat_StatusError.BRepFeat_OK: 0>, 'BRepFeat_BadDirect': <BRepFeat_StatusError.BRepFeat_BadDirect: 1>, 'BRepFeat_BadIntersect': <BRepFeat_StatusError.BRepFeat_BadIntersect: 2>, 'BRepFeat_EmptyBaryCurve': <BRepFeat_StatusError.BRepFeat_EmptyBaryCurve: 3>, 'BRepFeat_EmptyCutResult': <BRepFeat_StatusError.BRepFeat_EmptyCutResult: 4>, 'BRepFeat_FalseSide': <BRepFeat_StatusError.BRepFeat_FalseSide: 5>, 'BRepFeat_IncDirection': <BRepFeat_StatusError.BRepFeat_IncDirection: 6>, 'BRepFeat_IncSlidFace': <BRepFeat_StatusError.BRepFeat_IncSlidFace: 7>, 'BRepFeat_IncParameter': <BRepFeat_StatusError.BRepFeat_IncParameter: 8>, 'BRepFeat_IncTypes': <BRepFeat_StatusError.BRepFeat_IncTypes: 9>, 'BRepFeat_IntervalOverlap': <BRepFeat_StatusError.BRepFeat_IntervalOverlap: 10>, 'BRepFeat_InvFirstShape': <BRepFeat_StatusError.BRepFeat_InvFirstShape: 11>, 'BRepFeat_InvOption': <BRepFeat_StatusError.BRepFeat_InvOption: 12>, 'BRepFeat_InvShape': <BRepFeat_StatusError.BRepFeat_InvShape: 13>, 'BRepFeat_LocOpeNotDone': <BRepFeat_StatusError.BRepFeat_LocOpeNotDone: 14>, 'BRepFeat_LocOpeInvNotDone': <BRepFeat_StatusError.BRepFeat_LocOpeInvNotDone: 15>, 'BRepFeat_NoExtFace': <BRepFeat_StatusError.BRepFeat_NoExtFace: 16>, 'BRepFeat_NoFaceProf': <BRepFeat_StatusError.BRepFeat_NoFaceProf: 17>, 'BRepFeat_NoGluer': <BRepFeat_StatusError.BRepFeat_NoGluer: 18>, 'BRepFeat_NoIntersectF': <BRepFeat_StatusError.BRepFeat_NoIntersectF: 19>, 'BRepFeat_NoIntersectU': <BRepFeat_StatusError.BRepFeat_NoIntersectU: 20>, 'BRepFeat_NoParts': <BRepFeat_StatusError.BRepFeat_NoParts: 21>, 'BRepFeat_NoProjPt': <BRepFeat_StatusError.BRepFeat_NoProjPt: 22>, 'BRepFeat_NotInitialized': <BRepFeat_StatusError.BRepFeat_NotInitialized: 23>, 'BRepFeat_NotYetImplemented': <BRepFeat_StatusError.BRepFeat_NotYetImplemented: 24>, 'BRepFeat_NullRealTool': <BRepFeat_StatusError.BRepFeat_NullRealTool: 25>, 'BRepFeat_NullToolF': <BRepFeat_StatusError.BRepFeat_NullToolF: 26>, 'BRepFeat_NullToolU': <BRepFeat_StatusError.BRepFeat_NullToolU: 27>}
    pass
BRepFeat_BadDirect: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_BadDirect: 1>
BRepFeat_BadIntersect: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_BadIntersect: 2>
BRepFeat_EmptyBaryCurve: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_EmptyBaryCurve: 3>
BRepFeat_EmptyCutResult: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_EmptyCutResult: 4>
BRepFeat_FalseSide: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_FalseSide: 5>
BRepFeat_HoleTooLong: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_HoleTooLong: 2>
BRepFeat_IncDirection: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncDirection: 6>
BRepFeat_IncParameter: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncParameter: 8>
BRepFeat_IncSlidFace: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncSlidFace: 7>
BRepFeat_IncTypes: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IncTypes: 9>
BRepFeat_IntervalOverlap: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_IntervalOverlap: 10>
BRepFeat_InvFirstShape: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvFirstShape: 11>
BRepFeat_InvOption: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvOption: 12>
BRepFeat_InvShape: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_InvShape: 13>
BRepFeat_InvalidPlacement: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_InvalidPlacement: 1>
BRepFeat_LocOpeInvNotDone: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_LocOpeInvNotDone: 15>
BRepFeat_LocOpeNotDone: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_LocOpeNotDone: 14>
BRepFeat_NoError: OCP.BRepFeat.BRepFeat_Status # value = <BRepFeat_Status.BRepFeat_NoError: 0>
BRepFeat_NoExtFace: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoExtFace: 16>
BRepFeat_NoFaceProf: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoFaceProf: 17>
BRepFeat_NoGluer: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoGluer: 18>
BRepFeat_NoIntersectF: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoIntersectF: 19>
BRepFeat_NoIntersectU: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoIntersectU: 20>
BRepFeat_NoParts: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoParts: 21>
BRepFeat_NoProjPt: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NoProjPt: 22>
BRepFeat_NoSelection: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_NoSelection: 0>
BRepFeat_NotInitialized: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NotInitialized: 23>
BRepFeat_NotYetImplemented: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NotYetImplemented: 24>
BRepFeat_NullRealTool: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullRealTool: 25>
BRepFeat_NullToolF: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullToolF: 26>
BRepFeat_NullToolU: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_NullToolU: 27>
BRepFeat_OK: OCP.BRepFeat.BRepFeat_StatusError # value = <BRepFeat_StatusError.BRepFeat_OK: 0>
BRepFeat_SelectionFU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionFU: 1>
BRepFeat_SelectionSh: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionSh: 3>
BRepFeat_SelectionShU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionShU: 4>
BRepFeat_SelectionU: OCP.BRepFeat.BRepFeat_PerfSelection # value = <BRepFeat_PerfSelection.BRepFeat_SelectionU: 2>
