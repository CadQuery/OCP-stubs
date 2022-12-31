import OCP.TopClass
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopoDS
import OCP.gp
__all__  = [
"TopClass_SolidExplorer"
]
class TopClass_SolidExplorer():
    """
    Provide an exploration of a BRep Shape for the classification. Defines the description of a solid for the SolidClassifier.
    """
    def CurrentFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the current face.
        """
    def InitFace(self) -> None: 
        """
        Starts an exploration of the faces.
        """
    def InitShell(self) -> None: 
        """
        Starts an exploration of the shells.
        """
    def MoreFaces(self) -> bool: 
        """
        Returns True if there is a current face.
        """
    def MoreShells(self) -> bool: 
        """
        Returns True if there is a current shell.
        """
    def NextFace(self) -> None: 
        """
        Sets the explorer to the next face and returns False if there are no more wires.
        """
    def NextShell(self) -> None: 
        """
        Sets the explorer to the next shell and returns False if there are no more wires.
        """
    def OtherSegment(self,P : OCP.gp.gp_Pnt,L : OCP.gp.gp_Lin) -> Tuple[float]: 
        """
        Returns in <L>, <Par> a segment having at least one intersection with the shape boundary to compute intersections.
        """
    def Reject(self,P : OCP.gp.gp_Pnt) -> bool: 
        """
        Should return True if the point is outside a bounding volume of the shape.
        """
    def RejectFace(self,L : OCP.gp.gp_Lin,Par : float) -> bool: 
        """
        Returns True if the face bounding volume does not intersect the segment.
        """
    def RejectShell(self,L : OCP.gp.gp_Lin,Par : float) -> bool: 
        """
        Returns True if the shell bounding volume does not intersect the segment.
        """
    def Segment(self,P : OCP.gp.gp_Pnt,L : OCP.gp.gp_Lin) -> Tuple[float]: 
        """
        Returns in <L>, <Par> a segment having at least one intersection with the shape boundary to compute intersections.
        """
    pass
