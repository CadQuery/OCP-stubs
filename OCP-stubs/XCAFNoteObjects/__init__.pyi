import OCP.XCAFNoteObjects
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.TopoDS
import OCP.gp
__all__  = [
"XCAFNoteObjects_NoteObject"
]
class XCAFNoteObjects_NoteObject(OCP.Standard.Standard_Transient):
    """
    object to store note auxiliary dataobject to store note auxiliary data
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
    def GetPlane(self) -> OCP.gp.gp_Ax2: 
        """
        Returns a right-handed coordinate system of the plane
        """
    def GetPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the attachment point on the annotated object
        """
    def GetPointText(self) -> OCP.gp.gp_Pnt: 
        """
        Returns the text position
        """
    def GetPresentation(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a tesselated annotation if specified
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasPlane(self) -> bool: 
        """
        Returns True if plane is specified
        """
    def HasPoint(self) -> bool: 
        """
        Returns True if the attachment point on the annotated object is specified
        """
    def HasPointText(self) -> bool: 
        """
        Returns True if the text position is specified
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
        Resets data to the state after calling the default constructor
        """
    def SetPlane(self,thePlane : OCP.gp.gp_Ax2) -> None: 
        """
        Sets a right-handed coordinate system of the plane
        """
    def SetPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the anchor point on the annotated object
        """
    def SetPointText(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Sets the text position
        """
    def SetPresentation(self,thePresentation : OCP.TopoDS.TopoDS_Shape) -> None: 
        """
        Sets a tesselated annotation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theObj : XCAFNoteObjects_NoteObject) -> None: ...
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
