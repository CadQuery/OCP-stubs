import OCP.TopTrans
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.gp
__all__  = [
"TopTrans_Array2OfOrientation",
"TopTrans_CurveTransition",
"TopTrans_SurfaceTransition"
]
class TopTrans_Array2OfOrientation():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : TopTrans_Array2OfOrientation) -> TopTrans_Array2OfOrientation: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : TopTrans_Array2OfOrientation) -> TopTrans_Array2OfOrientation: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : OCP.TopAbs.TopAbs_Orientation,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : TopTrans_Array2OfOrientation) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    pass
class TopTrans_CurveTransition():
    """
    This algorithm is used to compute the transition of a Curve intersecting a curvilinear boundary.
    """
    def Compare(self,Tole : float,Tang : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir,Curv : float,S : OCP.TopAbs.TopAbs_Orientation,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Add a curve element to the boundary. If Or is REVERSED the curve is before the intersection, else if Or is FORWARD the curv is after the intersection and if Or is INTERNAL the intersection is in the middle of the curv.
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir) -> None: 
        """
        Initialize a Transition with the local description of a Curve.

        Initialize a Transition with the local description of a straight line.
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir,Curv : float) -> None: ...
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        returns the state of the curve after the intersection, this is the position relative to the boundary of a point very close to the intersection on the positive side of the tangent.
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        returns the state of the curve before the intersection, this is the position relative to the boundary of a point very close to the intersection on the negative side of the tangent.
        """
    def __init__(self) -> None: ...
    pass
class TopTrans_SurfaceTransition():
    """
    This algorithm is used to compute the transition of a 3D surface intersecting a topological surfacic boundary on a 3D curve ( intersection curve ). The boundary is described by a set of faces each face is described by - its support surface, - an orientation defining its matter side. The geometric elements are described locally at the intersection point by a second order development. A surface is described by the normal vector, the principal directions and the principal curvatures. A curve is described by the tangent, the normal and the curvature. The algorithm keeps track of the two faces elements closest to the part of the curve "before" and "after" the intersection, these two elements are updated for each new face. The position of the curve can be computed when at least one surface element has been given, this position is "In","Out" or "On" for the part of the curve "Before" or "After" the intersection.
    """
    @overload
    def Compare(self,Tole : float,Norm : OCP.gp.gp_Dir,MaxD : OCP.gp.gp_Dir,MinD : OCP.gp.gp_Dir,MaxCurv : float,MinCurv : float,S : OCP.TopAbs.TopAbs_Orientation,O : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Add a face element to the boundary.

        Add a plane or a cylindric face to the boundary.
        """
    @overload
    def Compare(self,Tole : float,Norm : OCP.gp.gp_Dir,S : OCP.TopAbs.TopAbs_Orientation,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @staticmethod
    def GetAfter_s(Tran : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    @staticmethod
    def GetBefore_s(Tran : OCP.TopAbs.TopAbs_Orientation) -> OCP.TopAbs.TopAbs_State: 
        """
        None
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir,MaxD : OCP.gp.gp_Dir,MinD : OCP.gp.gp_Dir,MaxCurv : float,MinCurv : float) -> None: 
        """
        Initialize a Surface Transition with the local description of the intersection curve and of the reference surface. PREQUESITORY : Norm oriented OUTSIDE "geometric matter"

        Initialize a Surface Transition with the local description of a straight line.
        """
    @overload
    def Reset(self,Tgt : OCP.gp.gp_Dir,Norm : OCP.gp.gp_Dir) -> None: ...
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of the reference surface after interference, this is the position relative to the surface of a point very close to the intersection on the positive side of the tangent.
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the state of the reference surface before the interference, this is the position relative to the surface of a point very close to the intersection on the negative side of the tangent.
        """
    def __init__(self) -> None: ...
    pass
