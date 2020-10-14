import OCP.BRepBndLib
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Bnd
import OCP.TopoDS
__all__  = [
"BRepBndLib"
]
class BRepBndLib():
    """
    This package provides the bounding boxes for curves and surfaces from BRepAdaptor. Functions to add a topological shape to a bounding box
    """
    @staticmethod
    def AddClose_s(S : OCP.TopoDS.TopoDS_Shape,B : OCP.Bnd.Bnd_Box) -> None: 
        """
        Adds the shape S to the bounding box B. This is a quick algorithm but only works if the shape S is composed of polygonal planar faces, as is the case if S is an approached polyhedral representation of an exact shape. Pay particular attention to this because this condition is not checked and, if it not respected, an error may occur in the algorithm for which the bounding box is built. Note that the resulting bounding box is not enlarged by the tolerance value of the sub-shapes as is the case with the Add function. So the added part of the resulting bounding box is closer to the shape S.
        """
    @staticmethod
    def AddOBB_s(theS : OCP.TopoDS.TopoDS_Shape,theOBB : OCP.Bnd.Bnd_OBB,theIsTriangulationUsed : bool=True,theIsOptimal : bool=False,theIsShapeToleranceUsed : bool=True) -> None: 
        """
        Computes the Oriented Bounding box for the shape <theS>. Two independent methods of computation are implemented: first method based on set of points (so, it demands the triangulated shape or shape with planar faces and linear edges). The second method is based on use of inertia axes and is called if use of the first method is impossible. If theIsTriangulationUsed == FALSE then the triangulation will be ignored at all. If theIsShapeToleranceUsed == TRUE then resulting box will be extended on the tolerance of the shape. theIsOptimal flag defines whether to look for the more tight OBB for the cost of performance or not.
        """
    @staticmethod
    def AddOptimal_s(S : OCP.TopoDS.TopoDS_Shape,B : OCP.Bnd.Bnd_Box,useTriangulation : bool=True,useShapeTolerance : bool=False) -> None: 
        """
        Adds the shape S to the bounding box B. This algorith builds precise bounding box, which differs from exact geometry boundaries of shape only on shape entities tolerances Algorithm is the same as for method Add(..), but uses more precise methods for building boxes for geometry objects. If useShapeTolerance = True, bounding box is enlardged by shape tolerances and these tolerances are used for numerical methods of bounding box size calculations, otherwise bounding box is built according to sizes of uderlined geometrical entities, numerical calculation use tolerance Precision::Confusion().
        """
    @staticmethod
    def Add_s(S : OCP.TopoDS.TopoDS_Shape,B : OCP.Bnd.Bnd_Box,useTriangulation : bool=True) -> None: 
        """
        Adds the shape S to the bounding box B. More precisely are successively added to B: - each face of S; the triangulation of the face is used if it exists, - then each edge of S which does not belong to a face, the polygon of the edge is used if it exists - and last each vertex of S which does not belong to an edge. After each elementary operation, the bounding box B is enlarged by the tolerance value of the relative sub-shape. When working with the triangulation of a face this value of enlargement is the sum of the triangulation deflection and the face tolerance. When working with the polygon of an edge this value of enlargement is the sum of the polygon deflection and the edge tolerance. Warning - This algorithm is time consuming if triangulation has not been inserted inside the data structure of the shape S. - The resulting bounding box may be somewhat larger than the object.
        """
    def __init__(self) -> None: ...
    pass
