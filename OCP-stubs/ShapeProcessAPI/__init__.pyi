import OCP.ShapeProcessAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.ShapeProcess
import OCP.TopoDS
import OCP.TopTools
__all__  = [
"ShapeProcessAPI_ApplySequence"
]
class ShapeProcessAPI_ApplySequence():
    """
    Applies one of the sequence read from resource file.
    """
    def ClearMap(self) -> None: 
        """
        Clears myMap with accumulated history.
        """
    def Context(self) -> OCP.ShapeProcess.ShapeProcess_ShapeContext: 
        """
        Returns object for managing resource file and sequence of operators.
        """
    def Map(self) -> OCP.TopTools.TopTools_DataMapOfShapeShape: 
        """
        Returns myMap with accumulated history.
        """
    def PrepareShape(self,shape : OCP.TopoDS.TopoDS_Shape,fillmap : bool=False,until : OCP.TopAbs.TopAbs_ShapeEnum=TopAbs_ShapeEnum.TopAbs_SHAPE) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Performs sequence of operators stored in myRsc. If <fillmap> is True adds history "shape-shape" into myMap for shape and its subshapes until level <until> (included). If <until> is TopAbs_SHAPE, all the subshapes are considered.
        """
    def PrintPreparationResult(self) -> None: 
        """
        Prints result of preparation onto the messenger of the context. Note that results can be accumulated from previous preparations it method ClearMap was not called before PrepareShape.
        """
    def __init__(self,rscName : str,seqName : str='') -> None: ...
    pass
