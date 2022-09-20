import OCP.BVH
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
__all__  = [
"BVH_BinaryTree",
"BVH_BuildQueue",
"BVH_BuildThread",
"BVH_BuildTool",
"BVH_BuilderTransient",
"BVH_ObjectTransient",
"BVH_Properties",
"BVH_QuadTree",
"BVH_TreeBaseTransient",
"BVH_Constants_LeafNodeSizeAverage",
"BVH_Constants_LeafNodeSizeDefault",
"BVH_Constants_LeafNodeSizeSingle",
"BVH_Constants_LeafNodeSizeSmall",
"BVH_Constants_MaxTreeDepth",
"BVH_Constants_NbBinsBest",
"BVH_Constants_NbBinsOptimal"
]
class BVH_BinaryTree():
    """
    Type corresponding to binary BVH.
    """
    def __init__(self) -> None: ...
    pass
class BVH_BuildQueue():
    """
    Command-queue for parallel building of BVH nodes.
    """
    def Enqueue(self,theNode : int) -> None: 
        """
        Enqueues new work-item onto BVH build queue.
        """
    def Fetch(self,wasBusy : bool) -> int: 
        """
        Fetches first work-item from BVH build queue.
        """
    def HasBusyThreads(self) -> bool: 
        """
        Checks if there are active build threads.
        """
    def Size(self) -> int: 
        """
        Returns current size of BVH build queue.
        """
    def __init__(self) -> None: ...
    pass
class BVH_BuildThread(OCP.Standard.Standard_Transient):
    """
    Wrapper for BVH build thread.Wrapper for BVH build thread.
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
    def Run(self) -> None: 
        """
        Starts execution of BVH build thread.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Wait(self) -> None: 
        """
        Waits till the thread finishes execution.
        """
    def __init__(self,theBuildTool : BVH_BuildTool,theBuildQueue : BVH_BuildQueue) -> None: ...
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
class BVH_BuildTool():
    """
    Tool object to call BVH builder subroutines.
    """
    def Perform(self,theNode : int) -> None: 
        """
        Performs splitting of the given BVH node.
        """
    pass
class BVH_BuilderTransient(OCP.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Builder (just to have a named base class).
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
    def IsParallel(self) -> bool: 
        """
        Returns parallel flag.
        """
    def LeafNodeSize(self) -> int: 
        """
        Returns the maximum number of sub-elements in the leaf.
        """
    def MaxTreeDepth(self) -> int: 
        """
        Returns the maximum depth of constructed BVH.
        """
    def SetParallel(self,isParallel : bool) -> None: 
        """
        Set parallel flag contolling possibility of parallel execution.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class BVH_ObjectTransient(OCP.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_Object (just to have a named base class).
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDirty(self) -> bool: 
        """
        Returns TRUE if object state should be updated.
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
    def MarkDirty(self) -> None: 
        """
        Marks object state as outdated (needs BVH rebuilding).
        """
    def Properties(self) -> BVH_Properties: 
        """
        Returns properties of the geometric object.
        """
    def SetProperties(self,theProperties : BVH_Properties) -> None: 
        """
        Sets properties of the geometric object.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class BVH_Properties(OCP.Standard.Standard_Transient):
    """
    Abstract properties of geometric object.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
class BVH_QuadTree():
    """
    Type corresponding to quad BVH.
    """
    def __init__(self) -> None: ...
    pass
class BVH_TreeBaseTransient(OCP.Standard.Standard_Transient):
    """
    A non-template class for using as base for BVH_TreeBase (just to have a named base class).
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
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
BVH_Constants_LeafNodeSizeAverage = 4
BVH_Constants_LeafNodeSizeDefault = 5
BVH_Constants_LeafNodeSizeSingle = 1
BVH_Constants_LeafNodeSizeSmall = 8
BVH_Constants_MaxTreeDepth = 32
BVH_Constants_NbBinsBest = 48
BVH_Constants_NbBinsOptimal = 32
