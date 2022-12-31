import OCP.XCAFView
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.gp
import OCP.Standard
__all__  = [
"XCAFView_Object",
"XCAFView_ProjectionType",
"XCAFView_ProjectionType_Central",
"XCAFView_ProjectionType_NoCamera",
"XCAFView_ProjectionType_Parallel"
]
class XCAFView_Object(OCP.Standard.Standard_Transient):
    """
    Access object for saved viewAccess object for saved viewAccess object for saved view
    """
    def BackPlaneDistance(self) -> float: 
        """
        None
        """
    def ClippingExpression(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def CreateGDTPoints(self,theLenght : int) -> None: 
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
    def FrontPlaneDistance(self) -> float: 
        """
        None
        """
    def GDTPoint(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBackPlaneClipping(self) -> bool: 
        """
        None
        """
    def HasFrontPlaneClipping(self) -> bool: 
        """
        None
        """
    def HasGDTPoints(self) -> bool: 
        """
        None
        """
    def HasViewVolumeSidesClipping(self) -> bool: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbGDTPoints(self) -> int: 
        """
        None
        """
    def ProjectionPoint(self) -> OCP.gp.gp_Pnt: 
        """
        None
        """
    def SetBackPlaneDistance(self,theDistance : float) -> None: 
        """
        None
        """
    def SetClippingExpression(self,theExpression : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFrontPlaneDistance(self,theDistance : float) -> None: 
        """
        None
        """
    def SetGDTPoint(self,theIndex : int,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetProjectionPoint(self,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        None
        """
    def SetType(self,theType : XCAFView_ProjectionType) -> None: 
        """
        None
        """
    def SetUpDirection(self,theDirection : OCP.gp.gp_Dir) -> None: 
        """
        None
        """
    def SetViewDirection(self,theDirection : OCP.gp.gp_Dir) -> None: 
        """
        None
        """
    def SetViewVolumeSidesClipping(self,theViewVolumeSidesClipping : bool) -> None: 
        """
        None
        """
    def SetWindowHorizontalSize(self,theSize : float) -> None: 
        """
        None
        """
    def SetWindowVerticalSize(self,theSize : float) -> None: 
        """
        None
        """
    def SetZoomFactor(self,theZoomFactor : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> XCAFView_ProjectionType: 
        """
        None
        """
    def UnsetBackPlaneClipping(self) -> None: 
        """
        None
        """
    def UnsetFrontPlaneClipping(self) -> None: 
        """
        None
        """
    def UpDirection(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def ViewDirection(self) -> OCP.gp.gp_Dir: 
        """
        None
        """
    def WindowHorizontalSize(self) -> float: 
        """
        None
        """
    def WindowVerticalSize(self) -> float: 
        """
        None
        """
    def ZoomFactor(self) -> float: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theObj : XCAFView_Object) -> None: ...
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
class XCAFView_ProjectionType():
    """
    Defines projection types of view

    Members:

      XCAFView_ProjectionType_NoCamera

      XCAFView_ProjectionType_Parallel

      XCAFView_ProjectionType_Central
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
    XCAFView_ProjectionType_Central: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_Central: 2>
    XCAFView_ProjectionType_NoCamera: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_NoCamera: 0>
    XCAFView_ProjectionType_Parallel: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_Parallel: 1>
    __entries: dict # value = {'XCAFView_ProjectionType_NoCamera': (<XCAFView_ProjectionType.XCAFView_ProjectionType_NoCamera: 0>, None), 'XCAFView_ProjectionType_Parallel': (<XCAFView_ProjectionType.XCAFView_ProjectionType_Parallel: 1>, None), 'XCAFView_ProjectionType_Central': (<XCAFView_ProjectionType.XCAFView_ProjectionType_Central: 2>, None)}
    __members__: dict # value = {'XCAFView_ProjectionType_NoCamera': <XCAFView_ProjectionType.XCAFView_ProjectionType_NoCamera: 0>, 'XCAFView_ProjectionType_Parallel': <XCAFView_ProjectionType.XCAFView_ProjectionType_Parallel: 1>, 'XCAFView_ProjectionType_Central': <XCAFView_ProjectionType.XCAFView_ProjectionType_Central: 2>}
    pass
XCAFView_ProjectionType_Central: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_Central: 2>
XCAFView_ProjectionType_NoCamera: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_NoCamera: 0>
XCAFView_ProjectionType_Parallel: OCP.XCAFView.XCAFView_ProjectionType # value = <XCAFView_ProjectionType.XCAFView_ProjectionType_Parallel: 1>
