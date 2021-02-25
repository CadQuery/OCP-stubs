import OCP.StepShape
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.StepBasic
import OCP.StepRepr
import OCP.StepGeom
import OCP.Standard
import OCP.StepData
__all__  = [
"StepShape_ShapeRepresentation",
"StepShape_TopologicalRepresentationItem",
"StepShape_AngleRelator",
"StepShape_DimensionalLocation",
"StepShape_DimensionalSize",
"StepShape_Array1OfConnectedEdgeSet",
"StepShape_Array1OfConnectedFaceSet",
"StepShape_Array1OfEdge",
"StepShape_Array1OfFace",
"StepShape_Array1OfFaceBound",
"StepShape_Array1OfGeometricSetSelect",
"StepShape_Array1OfOrientedClosedShell",
"StepShape_Array1OfOrientedEdge",
"StepShape_Array1OfShapeDimensionRepresentationItem",
"StepShape_Array1OfShell",
"StepShape_Array1OfValueQualifier",
"StepShape_Block",
"StepShape_BooleanOperand",
"StepShape_BooleanOperator",
"StepShape_BooleanResult",
"StepShape_BoxDomain",
"StepShape_HalfSpaceSolid",
"StepShape_SolidModel",
"StepShape_ConnectedFaceSet",
"StepShape_CompoundShapeRepresentation",
"StepShape_ConnectedEdgeSet",
"StepShape_ClosedShell",
"StepShape_ConnectedFaceShapeRepresentation",
"StepShape_ConnectedFaceSubSet",
"StepShape_ContextDependentShapeRepresentation",
"StepShape_CsgPrimitive",
"StepShape_CsgSelect",
"StepShape_CsgShapeRepresentation",
"StepShape_CsgSolid",
"StepShape_DefinitionalRepresentationAndShapeRepresentation",
"StepShape_DimensionalCharacteristic",
"StepShape_DimensionalCharacteristicRepresentation",
"StepShape_AngularLocation",
"StepShape_DimensionalLocationWithPath",
"StepShape_AngularSize",
"StepShape_DimensionalSizeWithPath",
"StepShape_DirectedDimensionalLocation",
"StepShape_Edge",
"StepShape_EdgeBasedWireframeModel",
"StepShape_EdgeBasedWireframeShapeRepresentation",
"StepShape_EdgeCurve",
"StepShape_Loop",
"StepShape_SweptAreaSolid",
"StepShape_SweptFaceSolid",
"StepShape_Face",
"StepShape_FaceBasedSurfaceModel",
"StepShape_FaceBound",
"StepShape_FaceOuterBound",
"StepShape_FaceSurface",
"StepShape_ManifoldSolidBrep",
"StepShape_FacetedBrepAndBrepWithVoids",
"StepShape_FacetedBrepShapeRepresentation",
"StepShape_GeometricSet",
"StepShape_GeometricCurveSet",
"StepShape_GeometricSetSelect",
"StepShape_GeometricallyBoundedSurfaceShapeRepresentation",
"StepShape_GeometricallyBoundedWireframeShapeRepresentation",
"StepShape_HArray1OfConnectedEdgeSet",
"StepShape_HArray1OfConnectedFaceSet",
"StepShape_HArray1OfEdge",
"StepShape_HArray1OfFace",
"StepShape_HArray1OfFaceBound",
"StepShape_HArray1OfGeometricSetSelect",
"StepShape_HArray1OfOrientedClosedShell",
"StepShape_HArray1OfOrientedEdge",
"StepShape_HArray1OfShapeDimensionRepresentationItem",
"StepShape_HArray1OfShell",
"StepShape_HArray1OfValueQualifier",
"StepShape_BoxedHalfSpace",
"StepShape_LimitsAndFits",
"StepShape_EdgeLoop",
"StepShape_LoopAndPath",
"StepShape_BrepWithVoids",
"StepShape_ManifoldSurfaceShapeRepresentation",
"StepShape_MeasureQualification",
"StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem",
"StepShape_NonManifoldSurfaceShapeRepresentation",
"StepShape_OpenShell",
"StepShape_OrientedClosedShell",
"StepShape_OrientedEdge",
"StepShape_OrientedFace",
"StepShape_OrientedOpenShell",
"StepShape_Path",
"StepShape_OrientedPath",
"StepShape_PlusMinusTolerance",
"StepShape_PointRepresentation",
"StepShape_PolyLoop",
"StepShape_PrecisionQualifier",
"StepShape_QualifiedRepresentationItem",
"StepShape_ReversibleTopologyItem",
"StepShape_RevolvedAreaSolid",
"StepShape_RevolvedFaceSolid",
"StepShape_RightAngularWedge",
"StepShape_RightCircularCone",
"StepShape_RightCircularCylinder",
"StepShape_SeamEdge",
"StepShape_ShapeDefinitionRepresentation",
"StepShape_ShapeDimensionRepresentation",
"StepShape_ShapeDimensionRepresentationItem",
"StepShape_AdvancedBrepShapeRepresentation",
"StepShape_ShapeRepresentationWithParameters",
"StepShape_Shell",
"StepShape_ShellBasedSurfaceModel",
"StepShape_FacetedBrep",
"StepShape_SolidReplica",
"StepShape_Sphere",
"StepShape_Subedge",
"StepShape_Subface",
"StepShape_SurfaceModel",
"StepShape_ExtrudedAreaSolid",
"StepShape_ExtrudedFaceSolid",
"StepShape_ToleranceMethodDefinition",
"StepShape_ToleranceValue",
"StepShape_AdvancedFace",
"StepShape_Torus",
"StepShape_TransitionalShapeRepresentation",
"StepShape_TypeQualifier",
"StepShape_ValueFormatTypeQualifier",
"StepShape_ValueQualifier",
"StepShape_Vertex",
"StepShape_VertexLoop",
"StepShape_VertexPoint",
"StepShape_Equal",
"StepShape_Large",
"StepShape_Small",
"StepShape_boDifference",
"StepShape_boIntersection",
"StepShape_boUnion"
]
class StepShape_ShapeRepresentation(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_TopologicalRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_AngleRelator():
    """
    None

    Members:

      StepShape_Equal

      StepShape_Large

      StepShape_Small
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
    StepShape_Equal: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Equal: 0>
    StepShape_Large: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Large: 1>
    StepShape_Small: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Small: 2>
    __entries: dict # value = {'StepShape_Equal': (<StepShape_AngleRelator.StepShape_Equal: 0>, None), 'StepShape_Large': (<StepShape_AngleRelator.StepShape_Large: 1>, None), 'StepShape_Small': (<StepShape_AngleRelator.StepShape_Small: 2>, None)}
    __members__: dict # value = {'StepShape_Equal': <StepShape_AngleRelator.StepShape_Equal: 0>, 'StepShape_Large': <StepShape_AngleRelator.StepShape_Large: 1>, 'StepShape_Small': <StepShape_AngleRelator.StepShape_Small: 2>}
    pass
class StepShape_DimensionalLocation(OCP.StepRepr.StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalLocationRepresentation of STEP entity DimensionalLocationRepresentation of STEP entity DimensionalLocation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aRelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def RelatedShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepShape_DimensionalSize(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalSizeRepresentation of STEP entity DimensionalSizeRepresentation of STEP entity DimensionalSize
    """
    def AppliesTo(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field AppliesTo
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
    def Init(self,aAppliesTo : OCP.StepRepr.StepRepr_ShapeAspect,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def SetAppliesTo(self,AppliesTo : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field AppliesTo
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepShape_Array1OfConnectedEdgeSet():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_ConnectedEdgeSet: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ConnectedEdgeSet: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ConnectedEdgeSet: 
        """
        Variable value access
        """
    def First(self) -> StepShape_ConnectedEdgeSet: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_ConnectedEdgeSet) -> None: 
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
    def Last(self) -> StepShape_ConnectedEdgeSet: 
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
    def Move(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ConnectedEdgeSet) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ConnectedEdgeSet: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepShape_ConnectedEdgeSet,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfConnectedFaceSet():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfConnectedFaceSet) -> StepShape_Array1OfConnectedFaceSet: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ConnectedFaceSet: 
        """
        Variable value access
        """
    def First(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_ConnectedFaceSet) -> None: 
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
    def Last(self) -> StepShape_ConnectedFaceSet: 
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
    def Move(self,theOther : StepShape_Array1OfConnectedFaceSet) -> StepShape_Array1OfConnectedFaceSet: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ConnectedFaceSet) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ConnectedFaceSet: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_ConnectedFaceSet,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfConnectedFaceSet) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfEdge():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfEdge) -> StepShape_Array1OfEdge: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_Edge: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Edge: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Edge: 
        """
        Variable value access
        """
    def First(self) -> StepShape_Edge: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_Edge) -> None: 
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
    def Last(self) -> StepShape_Edge: 
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
    def Move(self,theOther : StepShape_Array1OfEdge) -> StepShape_Array1OfEdge: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Edge) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Edge: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfEdge) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_Edge,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfFace():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfFace) -> StepShape_Array1OfFace: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_Face: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Face: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Face: 
        """
        Variable value access
        """
    def First(self) -> StepShape_Face: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_Face) -> None: 
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
    def Last(self) -> StepShape_Face: 
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
    def Move(self,theOther : StepShape_Array1OfFace) -> StepShape_Array1OfFace: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Face) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Face: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfFace) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_Face,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfFaceBound():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfFaceBound) -> StepShape_Array1OfFaceBound: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_FaceBound: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_FaceBound: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_FaceBound: 
        """
        Variable value access
        """
    def First(self) -> StepShape_FaceBound: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_FaceBound) -> None: 
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
    def Last(self) -> StepShape_FaceBound: 
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
    def Move(self,theOther : StepShape_Array1OfFaceBound) -> StepShape_Array1OfFaceBound: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_FaceBound) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_FaceBound: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfFaceBound) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_FaceBound,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfGeometricSetSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfGeometricSetSelect) -> StepShape_Array1OfGeometricSetSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_GeometricSetSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_GeometricSetSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_GeometricSetSelect: 
        """
        Variable value access
        """
    def First(self) -> StepShape_GeometricSetSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_GeometricSetSelect) -> None: 
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
    def Last(self) -> StepShape_GeometricSetSelect: 
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
    def Move(self,theOther : StepShape_Array1OfGeometricSetSelect) -> StepShape_Array1OfGeometricSetSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_GeometricSetSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_GeometricSetSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepShape_GeometricSetSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfGeometricSetSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfOrientedClosedShell():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfOrientedClosedShell) -> StepShape_Array1OfOrientedClosedShell: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_OrientedClosedShell: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_OrientedClosedShell: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_OrientedClosedShell: 
        """
        Variable value access
        """
    def First(self) -> StepShape_OrientedClosedShell: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_OrientedClosedShell) -> None: 
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
    def Last(self) -> StepShape_OrientedClosedShell: 
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
    def Move(self,theOther : StepShape_Array1OfOrientedClosedShell) -> StepShape_Array1OfOrientedClosedShell: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_OrientedClosedShell) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_OrientedClosedShell: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepShape_OrientedClosedShell,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfOrientedClosedShell) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfOrientedEdge():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfOrientedEdge) -> StepShape_Array1OfOrientedEdge: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_OrientedEdge: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_OrientedEdge: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_OrientedEdge: 
        """
        Variable value access
        """
    def First(self) -> StepShape_OrientedEdge: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_OrientedEdge) -> None: 
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
    def Last(self) -> StepShape_OrientedEdge: 
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
    def Move(self,theOther : StepShape_Array1OfOrientedEdge) -> StepShape_Array1OfOrientedEdge: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_OrientedEdge) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_OrientedEdge: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepShape_OrientedEdge,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfOrientedEdge) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfShapeDimensionRepresentationItem():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Variable value access
        """
    def First(self) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_ShapeDimensionRepresentationItem) -> None: 
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
    def Last(self) -> StepShape_ShapeDimensionRepresentationItem: 
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
    def Move(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ShapeDimensionRepresentationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepShape_ShapeDimensionRepresentationItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfShell():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfShell) -> StepShape_Array1OfShell: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_Shell: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Shell: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Shell: 
        """
        Variable value access
        """
    def First(self) -> StepShape_Shell: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_Shell) -> None: 
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
    def Last(self) -> StepShape_Shell: 
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
    def Move(self,theOther : StepShape_Array1OfShell) -> StepShape_Array1OfShell: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Shell) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Shell: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfShell) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_Shell,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Array1OfValueQualifier():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepShape_Array1OfValueQualifier) -> StepShape_Array1OfValueQualifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepShape_ValueQualifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ValueQualifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ValueQualifier: 
        """
        Variable value access
        """
    def First(self) -> StepShape_ValueQualifier: 
        """
        Returns first element
        """
    def Init(self,theValue : StepShape_ValueQualifier) -> None: 
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
    def Last(self) -> StepShape_ValueQualifier: 
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
    def Move(self,theOther : StepShape_Array1OfValueQualifier) -> StepShape_Array1OfValueQualifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ValueQualifier) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ValueQualifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfValueQualifier) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepShape_ValueQualifier,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class StepShape_Block(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : OCP.StepGeom.StepGeom_Axis2Placement3d,aX : float,aY : float,aZ : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetX(self,aX : float) -> None: 
        """
        None
        """
    def SetY(self,aY : float) -> None: 
        """
        None
        """
    def SetZ(self,aZ : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def X(self) -> float: 
        """
        None
        """
    def Y(self) -> float: 
        """
        None
        """
    def Z(self) -> float: 
        """
        None
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
class StepShape_BooleanOperand():
    """
    None
    """
    def BooleanResult(self) -> StepShape_BooleanResult: 
        """
        returns Value as a BooleanResult (Null if another type)
        """
    def CsgPrimitive(self) -> StepShape_CsgPrimitive: 
        """
        returns Value as a CsgPrimitive (Null if another type) CsgPrimitive is another Select Type
        """
    def HalfSpaceSolid(self) -> StepShape_HalfSpaceSolid: 
        """
        returns Value as a HalfSpaceSolid (Null if another type)
        """
    def SetBooleanResult(self,aBooleanResult : StepShape_BooleanResult) -> None: 
        """
        None
        """
    def SetCsgPrimitive(self,aCsgPrimitive : StepShape_CsgPrimitive) -> None: 
        """
        None
        """
    def SetHalfSpaceSolid(self,aHalfSpaceSolid : StepShape_HalfSpaceSolid) -> None: 
        """
        None
        """
    def SetSolidModel(self,aSolidModel : StepShape_SolidModel) -> None: 
        """
        None
        """
    def SetTypeOfContent(self,aTypeOfContent : int) -> None: 
        """
        None
        """
    def SolidModel(self) -> StepShape_SolidModel: 
        """
        returns Value as a SolidModel (Null if another type)
        """
    def TypeOfContent(self) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepShape_BooleanOperator():
    """
    None

    Members:

      StepShape_boDifference

      StepShape_boIntersection

      StepShape_boUnion
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
    StepShape_boDifference: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boDifference: 0>
    StepShape_boIntersection: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boIntersection: 1>
    StepShape_boUnion: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boUnion: 2>
    __entries: dict # value = {'StepShape_boDifference': (<StepShape_BooleanOperator.StepShape_boDifference: 0>, None), 'StepShape_boIntersection': (<StepShape_BooleanOperator.StepShape_boIntersection: 1>, None), 'StepShape_boUnion': (<StepShape_BooleanOperator.StepShape_boUnion: 2>, None)}
    __members__: dict # value = {'StepShape_boDifference': <StepShape_BooleanOperator.StepShape_boDifference: 0>, 'StepShape_boIntersection': <StepShape_BooleanOperator.StepShape_boIntersection: 1>, 'StepShape_boUnion': <StepShape_BooleanOperator.StepShape_boUnion: 2>}
    pass
class StepShape_BooleanResult(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def FirstOperand(self) -> StepShape_BooleanOperand: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOperator : StepShape_BooleanOperator,aFirstOperand : StepShape_BooleanOperand,aSecondOperand : StepShape_BooleanOperand) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Operator(self) -> StepShape_BooleanOperator: 
        """
        None
        """
    def SecondOperand(self) -> StepShape_BooleanOperand: 
        """
        None
        """
    def SetFirstOperand(self,aFirstOperand : StepShape_BooleanOperand) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOperator(self,aOperator : StepShape_BooleanOperator) -> None: 
        """
        None
        """
    def SetSecondOperand(self,aSecondOperand : StepShape_BooleanOperand) -> None: 
        """
        None
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
class StepShape_BoxDomain(OCP.Standard.Standard_Transient):
    def Corner(self) -> OCP.StepGeom.StepGeom_CartesianPoint: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aCorner : OCP.StepGeom.StepGeom_CartesianPoint,aXlength : float,aYlength : float,aZlength : float) -> None: 
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
    def SetCorner(self,aCorner : OCP.StepGeom.StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetXlength(self,aXlength : float) -> None: 
        """
        None
        """
    def SetYlength(self,aYlength : float) -> None: 
        """
        None
        """
    def SetZlength(self,aZlength : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Xlength(self) -> float: 
        """
        None
        """
    def Ylength(self) -> float: 
        """
        None
        """
    def Zlength(self) -> float: 
        """
        None
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
class StepShape_HalfSpaceSolid(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AgreementFlag(self) -> bool: 
        """
        None
        """
    def BaseSurface(self) -> OCP.StepGeom.StepGeom_Surface: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBaseSurface : OCP.StepGeom.StepGeom_Surface,aAgreementFlag : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetAgreementFlag(self,aAgreementFlag : bool) -> None: 
        """
        None
        """
    def SetBaseSurface(self,aBaseSurface : OCP.StepGeom.StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_SolidModel(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ConnectedFaceSet(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCfsFaces : StepShape_HArray1OfFace) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_CompoundShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity CompoundShapeRepresentationRepresentation of STEP entity CompoundShapeRepresentationRepresentation of STEP entity CompoundShapeRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ConnectedEdgeSet(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConnectedEdgeSetRepresentation of STEP entity ConnectedEdgeSetRepresentation of STEP entity ConnectedEdgeSet
    """
    def CesEdges(self) -> StepShape_HArray1OfEdge: 
        """
        Returns field CesEdges
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aCesEdges : StepShape_HArray1OfEdge) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetCesEdges(self,CesEdges : StepShape_HArray1OfEdge) -> None: 
        """
        Set field CesEdges
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ClosedShell(StepShape_ConnectedFaceSet, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCfsFaces : StepShape_HArray1OfFace) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ConnectedFaceShapeRepresentation(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConnectedFaceShapeRepresentationRepresentation of STEP entity ConnectedFaceShapeRepresentationRepresentation of STEP entity ConnectedFaceShapeRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ConnectedFaceSubSet(StepShape_ConnectedFaceSet, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ConnectedFaceSubSetRepresentation of STEP entity ConnectedFaceSubSetRepresentation of STEP entity ConnectedFaceSubSet
    """
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aConnectedFaceSet_CfsFaces : StepShape_HArray1OfFace,aParentFaceSet : StepShape_ConnectedFaceSet) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def ParentFaceSet(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns field ParentFaceSet
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentFaceSet(self,ParentFaceSet : StepShape_ConnectedFaceSet) -> None: 
        """
        Set field ParentFaceSet
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
class StepShape_ContextDependentShapeRepresentation(OCP.Standard.Standard_Transient):
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
    def Init(self,aRepRel : OCP.StepRepr.StepRepr_ShapeRepresentationRelationship,aProRel : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> None: 
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
    def RepresentationRelation(self) -> OCP.StepRepr.StepRepr_ShapeRepresentationRelationship: 
        """
        None
        """
    def RepresentedProductRelation(self) -> OCP.StepRepr.StepRepr_ProductDefinitionShape: 
        """
        None
        """
    def SetRepresentationRelation(self,aRepRel : OCP.StepRepr.StepRepr_ShapeRepresentationRelationship) -> None: 
        """
        None
        """
    def SetRepresentedProductRelation(self,aProRel : OCP.StepRepr.StepRepr_ProductDefinitionShape) -> None: 
        """
        None
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
class StepShape_CsgPrimitive(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Block(self) -> StepShape_Block: 
        """
        returns Value as a Block (Null if another type)
        """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a CsgPrimitive Kind Entity that is : 1 -> Sphere 2 -> Block 3 -> RightAngularWedge 4 -> Torus 5 -> RightCircularCone 6 -> RightCircularCylinder 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def RightAngularWedge(self) -> StepShape_RightAngularWedge: 
        """
        returns Value as a RightAngularWedge (Null if another type)
        """
    def RightCircularCone(self) -> StepShape_RightCircularCone: 
        """
        returns Value as a RightCircularCone (Null if another type)
        """
    def RightCircularCylinder(self) -> StepShape_RightCircularCylinder: 
        """
        returns Value as a RightCircularCylinder (Null if another type)
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Sphere(self) -> StepShape_Sphere: 
        """
        returns Value as a Sphere (Null if another type)
        """
    def Torus(self) -> StepShape_Torus: 
        """
        returns Value as a Torus (Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_CsgSelect():
    """
    None
    """
    def BooleanResult(self) -> StepShape_BooleanResult: 
        """
        returns Value as a BooleanResult (Null if another type)
        """
    def CsgPrimitive(self) -> StepShape_CsgPrimitive: 
        """
        returns Value as a CsgPrimitive (Null if another type)
        """
    def SetBooleanResult(self,aBooleanResult : StepShape_BooleanResult) -> None: 
        """
        None
        """
    def SetCsgPrimitive(self,aCsgPrimitive : StepShape_CsgPrimitive) -> None: 
        """
        None
        """
    def SetTypeOfContent(self,aTypeOfContent : int) -> None: 
        """
        None
        """
    def TypeOfContent(self) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepShape_CsgShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_CsgSolid(StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aTreeRootExpression : StepShape_CsgSelect) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetTreeRootExpression(self,aTreeRootExpression : StepShape_CsgSelect) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TreeRootExpression(self) -> StepShape_CsgSelect: 
        """
        None
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
class StepShape_DefinitionalRepresentationAndShapeRepresentation(OCP.StepRepr.StepRepr_DefinitionalRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Implements complex type (DEFINITIONAL_REPRESENTATION,REPRESENTATION,SHAPE_REPRESENTATION)Implements complex type (DEFINITIONAL_REPRESENTATION,REPRESENTATION,SHAPE_REPRESENTATION)Implements complex type (DEFINITIONAL_REPRESENTATION,REPRESENTATION,SHAPE_REPRESENTATION)
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_DimensionalCharacteristic(OCP.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type DimensionalCharacteristic
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of DimensionalCharacteristic select type 1 -> DimensionalLocation from StepShape 2 -> DimensionalSize from StepShape 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DimensionalLocation(self) -> StepShape_DimensionalLocation: 
        """
        Returns Value as DimensionalLocation (or Null if another type)
        """
    def DimensionalSize(self) -> StepShape_DimensionalSize: 
        """
        Returns Value as DimensionalSize (or Null if another type)
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_DimensionalCharacteristicRepresentation(OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalCharacteristicRepresentationRepresentation of STEP entity DimensionalCharacteristicRepresentationRepresentation of STEP entity DimensionalCharacteristicRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Dimension(self) -> StepShape_DimensionalCharacteristic: 
        """
        Returns field Dimension
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
    def Init(self,aDimension : StepShape_DimensionalCharacteristic,aRepresentation : StepShape_ShapeDimensionRepresentation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Representation(self) -> StepShape_ShapeDimensionRepresentation: 
        """
        Returns field Representation
        """
    def SetDimension(self,Dimension : StepShape_DimensionalCharacteristic) -> None: 
        """
        Set field Dimension
        """
    def SetRepresentation(self,Representation : StepShape_ShapeDimensionRepresentation) -> None: 
        """
        Set field Representation
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
class StepShape_AngularLocation(StepShape_DimensionalLocation, OCP.StepRepr.StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AngularLocationRepresentation of STEP entity AngularLocationRepresentation of STEP entity AngularLocation
    """
    def AngleSelection(self) -> StepShape_AngleRelator: 
        """
        Returns field AngleSelection
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aShapeAspectRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasShapeAspectRelationship_Description : bool,aShapeAspectRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aShapeAspectRelationship_RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aShapeAspectRelationship_RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aAngleSelection : StepShape_AngleRelator) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def RelatedShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetAngleSelection(self,AngleSelection : StepShape_AngleRelator) -> None: 
        """
        Set field AngleSelection
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepShape_DimensionalLocationWithPath(StepShape_DimensionalLocation, OCP.StepRepr.StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalLocationWithPathRepresentation of STEP entity DimensionalLocationWithPathRepresentation of STEP entity DimensionalLocationWithPath
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aShapeAspectRelationship_Name : OCP.TCollection.TCollection_HAsciiString,hasShapeAspectRelationship_Description : bool,aShapeAspectRelationship_Description : OCP.TCollection.TCollection_HAsciiString,aShapeAspectRelationship_RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aShapeAspectRelationship_RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aPath : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def Path(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field Path
        """
    def RelatedShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPath(self,Path : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field Path
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepShape_AngularSize(StepShape_DimensionalSize, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity AngularSizeRepresentation of STEP entity AngularSizeRepresentation of STEP entity AngularSize
    """
    def AngleSelection(self) -> StepShape_AngleRelator: 
        """
        Returns field AngleSelection
        """
    def AppliesTo(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field AppliesTo
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
    def Init(self,aDimensionalSize_AppliesTo : OCP.StepRepr.StepRepr_ShapeAspect,aDimensionalSize_Name : OCP.TCollection.TCollection_HAsciiString,aAngleSelection : StepShape_AngleRelator) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def SetAngleSelection(self,AngleSelection : StepShape_AngleRelator) -> None: 
        """
        Set field AngleSelection
        """
    def SetAppliesTo(self,AppliesTo : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field AppliesTo
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
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
class StepShape_DimensionalSizeWithPath(StepShape_DimensionalSize, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DimensionalSizeWithPathRepresentation of STEP entity DimensionalSizeWithPathRepresentation of STEP entity DimensionalSizeWithPath
    """
    def AppliesTo(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field AppliesTo
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
    def Init(self,aDimensionalSize_AppliesTo : OCP.StepRepr.StepRepr_ShapeAspect,aDimensionalSize_Name : OCP.TCollection.TCollection_HAsciiString,aPath : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def Path(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field Path
        """
    def SetAppliesTo(self,AppliesTo : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field AppliesTo
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetPath(self,Path : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field Path
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
class StepShape_DirectedDimensionalLocation(StepShape_DimensionalLocation, OCP.StepRepr.StepRepr_ShapeAspectRelationship, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DirectedDimensionalLocationRepresentation of STEP entity DirectedDimensionalLocationRepresentation of STEP entity DirectedDimensionalLocation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field Description
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasDescription(self) -> bool: 
        """
        Returns True if optional field Description is defined
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,hasDescription : bool,aDescription : OCP.TCollection.TCollection_HAsciiString,aRelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect,aRelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Initialize all fields (own and inherited)
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
        Returns field Name
        """
    def RelatedShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatedShapeAspect
        """
    def RelatingShapeAspect(self) -> OCP.StepRepr.StepRepr_ShapeAspect: 
        """
        Returns field RelatingShapeAspect
        """
    def SetDescription(self,Description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Description
        """
    def SetName(self,Name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field Name
        """
    def SetRelatedShapeAspect(self,RelatedShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatedShapeAspect
        """
    def SetRelatingShapeAspect(self,RelatingShapeAspect : OCP.StepRepr.StepRepr_ShapeAspect) -> None: 
        """
        Set field RelatingShapeAspect
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
class StepShape_Edge(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeEnd(self) -> StepShape_Vertex: 
        """
        None
        """
    def EdgeStart(self) -> StepShape_Vertex: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeStart : StepShape_Vertex,aEdgeEnd : StepShape_Vertex) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetEdgeEnd(self,aEdgeEnd : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetEdgeStart(self,aEdgeStart : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_EdgeBasedWireframeModel(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity EdgeBasedWireframeModelRepresentation of STEP entity EdgeBasedWireframeModelRepresentation of STEP entity EdgeBasedWireframeModel
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
    def EbwmBoundary(self) -> StepShape_HArray1OfConnectedEdgeSet: 
        """
        Returns field EbwmBoundary
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aEbwmBoundary : StepShape_HArray1OfConnectedEdgeSet) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetEbwmBoundary(self,EbwmBoundary : StepShape_HArray1OfConnectedEdgeSet) -> None: 
        """
        Set field EbwmBoundary
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_EdgeBasedWireframeShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity EdgeBasedWireframeShapeRepresentationRepresentation of STEP entity EdgeBasedWireframeShapeRepresentationRepresentation of STEP entity EdgeBasedWireframeShapeRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_EdgeCurve(StepShape_Edge, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeEnd(self) -> StepShape_Vertex: 
        """
        None
        """
    def EdgeGeometry(self) -> OCP.StepGeom.StepGeom_Curve: 
        """
        None
        """
    def EdgeStart(self) -> StepShape_Vertex: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeStart : StepShape_Vertex,aEdgeEnd : StepShape_Vertex,aEdgeGeometry : OCP.StepGeom.StepGeom_Curve,aSameSense : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SameSense(self) -> bool: 
        """
        None
        """
    def SetEdgeEnd(self,aEdgeEnd : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetEdgeGeometry(self,aEdgeGeometry : OCP.StepGeom.StepGeom_Curve) -> None: 
        """
        None
        """
    def SetEdgeStart(self,aEdgeStart : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSameSense(self,aSameSense : bool) -> None: 
        """
        None
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
class StepShape_Loop(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_SweptAreaSolid(StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptArea(self,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> None: 
        """
        None
        """
    def SweptArea(self) -> OCP.StepGeom.StepGeom_CurveBoundedSurface: 
        """
        None
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
class StepShape_SweptFaceSolid(StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : StepShape_FaceSurface) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptFace(self,aSweptArea : StepShape_FaceSurface) -> None: 
        """
        None
        """
    def SweptFace(self) -> StepShape_FaceSurface: 
        """
        None
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
class StepShape_Face(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bounds(self) -> StepShape_HArray1OfFaceBound: 
        """
        None
        """
    def BoundsValue(self,num : int) -> StepShape_FaceBound: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBounds : StepShape_HArray1OfFaceBound) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbBounds(self) -> int: 
        """
        None
        """
    def SetBounds(self,aBounds : StepShape_HArray1OfFaceBound) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_FaceBasedSurfaceModel(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity FaceBasedSurfaceModelRepresentation of STEP entity FaceBasedSurfaceModelRepresentation of STEP entity FaceBasedSurfaceModel
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
    def FbsmFaces(self) -> StepShape_HArray1OfConnectedFaceSet: 
        """
        Returns field FbsmFaces
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFbsmFaces : StepShape_HArray1OfConnectedFaceSet) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetFbsmFaces(self,FbsmFaces : StepShape_HArray1OfConnectedFaceSet) -> None: 
        """
        Set field FbsmFaces
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_FaceBound(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bound(self) -> StepShape_Loop: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBound : StepShape_Loop,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetBound(self,aBound : StepShape_Loop) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_FaceOuterBound(StepShape_FaceBound, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bound(self) -> StepShape_Loop: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBound : StepShape_Loop,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetBound(self,aBound : StepShape_Loop) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_FaceSurface(StepShape_Face, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bounds(self) -> StepShape_HArray1OfFaceBound: 
        """
        None
        """
    def BoundsValue(self,num : int) -> StepShape_FaceBound: 
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
    def FaceGeometry(self) -> OCP.StepGeom.StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBounds : StepShape_HArray1OfFaceBound,aFaceGeometry : OCP.StepGeom.StepGeom_Surface,aSameSense : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbBounds(self) -> int: 
        """
        None
        """
    def SameSense(self) -> bool: 
        """
        None
        """
    def SetBounds(self,aBounds : StepShape_HArray1OfFaceBound) -> None: 
        """
        None
        """
    def SetFaceGeometry(self,aFaceGeometry : OCP.StepGeom.StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSameSense(self,aSameSense : bool) -> None: 
        """
        None
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
class StepShape_ManifoldSolidBrep(StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ClosedShell) -> None: ...
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
    def Outer(self) -> StepShape_ConnectedFaceSet: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOuter(self,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None
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
class StepShape_FacetedBrepAndBrepWithVoids(StepShape_ManifoldSolidBrep, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def BrepWithVoids(self) -> StepShape_BrepWithVoids: 
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
    def FacetedBrep(self) -> StepShape_FacetedBrep: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ClosedShell,aFacetedBrep : StepShape_FacetedBrep,aBrepWithVoids : StepShape_BrepWithVoids) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ClosedShell,aVoids : StepShape_HArray1OfOrientedClosedShell) -> None: ...
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
    def NbVoids(self) -> int: 
        """
        None
        """
    def Outer(self) -> StepShape_ConnectedFaceSet: 
        """
        None
        """
    def SetBrepWithVoids(self,aBrepWithVoids : StepShape_BrepWithVoids) -> None: 
        """
        None
        """
    def SetFacetedBrep(self,aFacetedBrep : StepShape_FacetedBrep) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOuter(self,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None
        """
    def SetVoids(self,aVoids : StepShape_HArray1OfOrientedClosedShell) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Voids(self) -> StepShape_HArray1OfOrientedClosedShell: 
        """
        None
        """
    def VoidsValue(self,num : int) -> StepShape_OrientedClosedShell: 
        """
        None
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
class StepShape_FacetedBrepShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_GeometricSet(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Elements(self) -> StepShape_HArray1OfGeometricSetSelect: 
        """
        None
        """
    def ElementsValue(self,num : int) -> StepShape_GeometricSetSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aElements : StepShape_HArray1OfGeometricSetSelect) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbElements(self) -> int: 
        """
        None
        """
    def SetElements(self,aElements : StepShape_HArray1OfGeometricSetSelect) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_GeometricCurveSet(StepShape_GeometricSet, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Elements(self) -> StepShape_HArray1OfGeometricSetSelect: 
        """
        None
        """
    def ElementsValue(self,num : int) -> StepShape_GeometricSetSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aElements : StepShape_HArray1OfGeometricSetSelect) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbElements(self) -> int: 
        """
        None
        """
    def SetElements(self,aElements : StepShape_HArray1OfGeometricSetSelect) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_GeometricSetSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a GeometricSetSelect Kind Entity that is : 1 -> Point 2 -> Curve 3 -> Surface 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Curve(self) -> OCP.StepGeom.StepGeom_Curve: 
        """
        returns Value as a Curve (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Point(self) -> OCP.StepGeom.StepGeom_Point: 
        """
        returns Value as a Point (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Surface(self) -> OCP.StepGeom.StepGeom_Surface: 
        """
        returns Value as a Surface (Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_GeometricallyBoundedSurfaceShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_GeometricallyBoundedWireframeShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_HArray1OfConnectedEdgeSet(StepShape_Array1OfConnectedEdgeSet, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_ConnectedEdgeSet: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ConnectedEdgeSet: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ConnectedEdgeSet: 
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
    def First(self) -> StepShape_ConnectedEdgeSet: 
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
    def Init(self,theValue : StepShape_ConnectedEdgeSet) -> None: 
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
    def Last(self) -> StepShape_ConnectedEdgeSet: 
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
    def Move(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> StepShape_Array1OfConnectedEdgeSet: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ConnectedEdgeSet) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ConnectedEdgeSet: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_ConnectedEdgeSet) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfConnectedEdgeSet) -> None: ...
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
class StepShape_HArray1OfConnectedFaceSet(StepShape_Array1OfConnectedFaceSet, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfConnectedFaceSet: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfConnectedFaceSet) -> StepShape_Array1OfConnectedFaceSet: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfConnectedFaceSet: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ConnectedFaceSet: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ConnectedFaceSet: 
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
    def First(self) -> StepShape_ConnectedFaceSet: 
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
    def Init(self,theValue : StepShape_ConnectedFaceSet) -> None: 
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
    def Last(self) -> StepShape_ConnectedFaceSet: 
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
    def Move(self,theOther : StepShape_Array1OfConnectedFaceSet) -> StepShape_Array1OfConnectedFaceSet: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ConnectedFaceSet) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ConnectedFaceSet: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfConnectedFaceSet) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_ConnectedFaceSet) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepShape_HArray1OfEdge(StepShape_Array1OfEdge, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfEdge: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfEdge) -> StepShape_Array1OfEdge: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfEdge: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_Edge: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Edge: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Edge: 
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
    def First(self) -> StepShape_Edge: 
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
    def Init(self,theValue : StepShape_Edge) -> None: 
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
    def Last(self) -> StepShape_Edge: 
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
    def Move(self,theOther : StepShape_Array1OfEdge) -> StepShape_Array1OfEdge: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Edge) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Edge: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_Edge) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfEdge) -> None: ...
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
class StepShape_HArray1OfFace(StepShape_Array1OfFace, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfFace: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfFace) -> StepShape_Array1OfFace: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfFace: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_Face: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Face: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Face: 
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
    def First(self) -> StepShape_Face: 
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
    def Init(self,theValue : StepShape_Face) -> None: 
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
    def Last(self) -> StepShape_Face: 
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
    def Move(self,theOther : StepShape_Array1OfFace) -> StepShape_Array1OfFace: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Face) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Face: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfFace) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_Face) -> None: ...
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
class StepShape_HArray1OfFaceBound(StepShape_Array1OfFaceBound, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfFaceBound: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfFaceBound) -> StepShape_Array1OfFaceBound: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfFaceBound: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_FaceBound: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_FaceBound: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_FaceBound: 
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
    def First(self) -> StepShape_FaceBound: 
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
    def Init(self,theValue : StepShape_FaceBound) -> None: 
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
    def Last(self) -> StepShape_FaceBound: 
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
    def Move(self,theOther : StepShape_Array1OfFaceBound) -> StepShape_Array1OfFaceBound: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_FaceBound) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_FaceBound: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_FaceBound) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfFaceBound) -> None: ...
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
class StepShape_HArray1OfGeometricSetSelect(StepShape_Array1OfGeometricSetSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfGeometricSetSelect: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfGeometricSetSelect) -> StepShape_Array1OfGeometricSetSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfGeometricSetSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_GeometricSetSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_GeometricSetSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_GeometricSetSelect: 
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
    def First(self) -> StepShape_GeometricSetSelect: 
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
    def Init(self,theValue : StepShape_GeometricSetSelect) -> None: 
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
    def Last(self) -> StepShape_GeometricSetSelect: 
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
    def Move(self,theOther : StepShape_Array1OfGeometricSetSelect) -> StepShape_Array1OfGeometricSetSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_GeometricSetSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_GeometricSetSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_GeometricSetSelect) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfGeometricSetSelect) -> None: ...
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
class StepShape_HArray1OfOrientedClosedShell(StepShape_Array1OfOrientedClosedShell, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfOrientedClosedShell: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfOrientedClosedShell) -> StepShape_Array1OfOrientedClosedShell: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfOrientedClosedShell: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_OrientedClosedShell: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_OrientedClosedShell: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_OrientedClosedShell: 
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
    def First(self) -> StepShape_OrientedClosedShell: 
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
    def Init(self,theValue : StepShape_OrientedClosedShell) -> None: 
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
    def Last(self) -> StepShape_OrientedClosedShell: 
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
    def Move(self,theOther : StepShape_Array1OfOrientedClosedShell) -> StepShape_Array1OfOrientedClosedShell: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_OrientedClosedShell) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_OrientedClosedShell: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepShape_Array1OfOrientedClosedShell) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_OrientedClosedShell) -> None: ...
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
class StepShape_HArray1OfOrientedEdge(StepShape_Array1OfOrientedEdge, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfOrientedEdge: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfOrientedEdge) -> StepShape_Array1OfOrientedEdge: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfOrientedEdge: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_OrientedEdge: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_OrientedEdge: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_OrientedEdge: 
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
    def First(self) -> StepShape_OrientedEdge: 
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
    def Init(self,theValue : StepShape_OrientedEdge) -> None: 
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
    def Last(self) -> StepShape_OrientedEdge: 
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
    def Move(self,theOther : StepShape_Array1OfOrientedEdge) -> StepShape_Array1OfOrientedEdge: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_OrientedEdge) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_OrientedEdge: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfOrientedEdge) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_OrientedEdge) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepShape_HArray1OfShapeDimensionRepresentationItem(StepShape_Array1OfShapeDimensionRepresentationItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ShapeDimensionRepresentationItem: 
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
    def First(self) -> StepShape_ShapeDimensionRepresentationItem: 
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
    def Init(self,theValue : StepShape_ShapeDimensionRepresentationItem) -> None: 
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
    def Last(self) -> StepShape_ShapeDimensionRepresentationItem: 
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
    def Move(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> StepShape_Array1OfShapeDimensionRepresentationItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ShapeDimensionRepresentationItem) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ShapeDimensionRepresentationItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_ShapeDimensionRepresentationItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfShapeDimensionRepresentationItem) -> None: ...
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
class StepShape_HArray1OfShell(StepShape_Array1OfShell, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfShell: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfShell) -> StepShape_Array1OfShell: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfShell: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_Shell: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_Shell: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_Shell: 
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
    def First(self) -> StepShape_Shell: 
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
    def Init(self,theValue : StepShape_Shell) -> None: 
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
    def Last(self) -> StepShape_Shell: 
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
    def Move(self,theOther : StepShape_Array1OfShell) -> StepShape_Array1OfShell: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_Shell) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_Shell: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_Shell) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfShell) -> None: ...
    @overload
    def __init__(self) -> None: ...
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
class StepShape_HArray1OfValueQualifier(StepShape_Array1OfValueQualifier, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepShape_Array1OfValueQualifier: 
        """
        None
        """
    def Assign(self,theOther : StepShape_Array1OfValueQualifier) -> StepShape_Array1OfValueQualifier: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepShape_Array1OfValueQualifier: 
        """
        None
        """
    def ChangeFirst(self) -> StepShape_ValueQualifier: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepShape_ValueQualifier: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepShape_ValueQualifier: 
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
    def First(self) -> StepShape_ValueQualifier: 
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
    def Init(self,theValue : StepShape_ValueQualifier) -> None: 
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
    def Last(self) -> StepShape_ValueQualifier: 
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
    def Move(self,theOther : StepShape_Array1OfValueQualifier) -> StepShape_Array1OfValueQualifier: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepShape_ValueQualifier) -> None: 
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
    def Value(self,theIndex : int) -> StepShape_ValueQualifier: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepShape_Array1OfValueQualifier) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepShape_ValueQualifier) -> None: ...
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
class StepShape_BoxedHalfSpace(StepShape_HalfSpaceSolid, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def AgreementFlag(self) -> bool: 
        """
        None
        """
    def BaseSurface(self) -> OCP.StepGeom.StepGeom_Surface: 
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
    def Enclosure(self) -> StepShape_BoxDomain: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBaseSurface : OCP.StepGeom.StepGeom_Surface,aAgreementFlag : bool,aEnclosure : StepShape_BoxDomain) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetAgreementFlag(self,aAgreementFlag : bool) -> None: 
        """
        None
        """
    def SetBaseSurface(self,aBaseSurface : OCP.StepGeom.StepGeom_Surface) -> None: 
        """
        None
        """
    def SetEnclosure(self,aEnclosure : StepShape_BoxDomain) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_LimitsAndFits(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def FormVariance(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Grade(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,form_variance : OCP.TCollection.TCollection_HAsciiString,zone_variance : OCP.TCollection.TCollection_HAsciiString,grade : OCP.TCollection.TCollection_HAsciiString,source : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def SetFormVariance(self,form_variance : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetGrade(self,grade : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSource(self,source : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetZoneVariance(self,zone_variance : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def Source(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ZoneVariance(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
class StepShape_EdgeLoop(StepShape_Loop, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeList(self) -> StepShape_HArray1OfOrientedEdge: 
        """
        None
        """
    def EdgeListValue(self,num : int) -> StepShape_OrientedEdge: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbEdgeList(self) -> int: 
        """
        None
        """
    def SetEdgeList(self,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_LoopAndPath(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeList(self) -> StepShape_HArray1OfOrientedEdge: 
        """
        None
        """
    def EdgeListValue(self,num : int) -> StepShape_OrientedEdge: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLoop : StepShape_Loop,aPath : StepShape_Path) -> None: ...
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
    def Loop(self) -> StepShape_Loop: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbEdgeList(self) -> int: 
        """
        None
        """
    def Path(self) -> StepShape_Path: 
        """
        None
        """
    def SetEdgeList(self,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
        """
        None
        """
    def SetLoop(self,aLoop : StepShape_Loop) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPath(self,aPath : StepShape_Path) -> None: 
        """
        None
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
class StepShape_BrepWithVoids(StepShape_ManifoldSolidBrep, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ClosedShell,aVoids : StepShape_HArray1OfOrientedClosedShell) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbVoids(self) -> int: 
        """
        None
        """
    def Outer(self) -> StepShape_ConnectedFaceSet: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOuter(self,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None
        """
    def SetVoids(self,aVoids : StepShape_HArray1OfOrientedClosedShell) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Voids(self) -> StepShape_HArray1OfOrientedClosedShell: 
        """
        None
        """
    def VoidsValue(self,num : int) -> StepShape_OrientedClosedShell: 
        """
        None
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
class StepShape_ManifoldSurfaceShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_MeasureQualification(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Description(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
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
    def Init(self,name : OCP.TCollection.TCollection_HAsciiString,description : OCP.TCollection.TCollection_HAsciiString,qualified_measure : OCP.StepBasic.StepBasic_MeasureWithUnit,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbQualifiers(self) -> int: 
        """
        None
        """
    def QualifiedMeasure(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def Qualifiers(self) -> StepShape_HArray1OfValueQualifier: 
        """
        None
        """
    def QualifiersValue(self,num : int) -> StepShape_ValueQualifier: 
        """
        None
        """
    def SetDescription(self,description : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQualifiedMeasure(self,qualified_measure : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetQualifiers(self,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
        """
        None
        """
    def SetQualifiersValue(self,num : int,aqualifier : StepShape_ValueQualifier) -> None: 
        """
        None
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
class StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional Tolerances Complex Type between MeasureRepresentationItem and QualifiedRepresentationItemAdded for Dimensional Tolerances Complex Type between MeasureRepresentationItem and QualifiedRepresentationItemAdded for Dimensional Tolerances Complex Type between MeasureRepresentationItem and QualifiedRepresentationItem
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aValueComponent : OCP.StepBasic.StepBasic_MeasureValueMember,aUnitComponent : OCP.StepBasic.StepBasic_Unit,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
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
    def Measure(self) -> OCP.StepBasic.StepBasic_MeasureWithUnit: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbQualifiers(self) -> int: 
        """
        None
        """
    def Qualifiers(self) -> StepShape_HArray1OfValueQualifier: 
        """
        None
        """
    def QualifiersValue(self,num : int) -> StepShape_ValueQualifier: 
        """
        None
        """
    def SetMeasure(self,Measure : OCP.StepBasic.StepBasic_MeasureWithUnit) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQualifiers(self,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
        """
        None
        """
    def SetQualifiersValue(self,num : int,aqualifier : StepShape_ValueQualifier) -> None: 
        """
        None
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
class StepShape_NonManifoldSurfaceShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity NonManifoldSurfaceShapeRepresentationRepresentation of STEP entity NonManifoldSurfaceShapeRepresentationRepresentation of STEP entity NonManifoldSurfaceShapeRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_OpenShell(StepShape_ConnectedFaceSet, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCfsFaces : StepShape_HArray1OfFace) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_OrientedClosedShell(StepShape_ClosedShell, StepShape_ConnectedFaceSet, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
        """
        None
        """
    def ClosedShellElement(self) -> StepShape_ClosedShell: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aClosedShellElement : StepShape_ClosedShell,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetClosedShellElement(self,aClosedShellElement : StepShape_ClosedShell) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_OrientedEdge(StepShape_Edge, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeElement(self) -> StepShape_Edge: 
        """
        None
        """
    def EdgeEnd(self) -> StepShape_Vertex: 
        """
        None
        """
    def EdgeStart(self) -> StepShape_Vertex: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeElement : StepShape_Edge,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetEdgeElement(self,aEdgeElement : StepShape_Edge) -> None: 
        """
        None
        """
    def SetEdgeEnd(self,aEdgeEnd : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetEdgeStart(self,aEdgeStart : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_OrientedFace(StepShape_Face, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bounds(self) -> StepShape_HArray1OfFaceBound: 
        """
        None
        """
    def BoundsValue(self,num : int) -> StepShape_FaceBound: 
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
    def FaceElement(self) -> StepShape_Face: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFaceElement : StepShape_Face,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbBounds(self) -> int: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetBounds(self,aBounds : StepShape_HArray1OfFaceBound) -> None: 
        """
        None
        """
    def SetFaceElement(self,aFaceElement : StepShape_Face) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_OrientedOpenShell(StepShape_OpenShell, StepShape_ConnectedFaceSet, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CfsFaces(self) -> StepShape_HArray1OfFace: 
        """
        None
        """
    def CfsFacesValue(self,num : int) -> StepShape_Face: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOpenShellElement : StepShape_OpenShell,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbCfsFaces(self) -> int: 
        """
        None
        """
    def OpenShellElement(self) -> StepShape_OpenShell: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def SetCfsFaces(self,aCfsFaces : StepShape_HArray1OfFace) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOpenShellElement(self,aOpenShellElement : StepShape_OpenShell) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
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
class StepShape_Path(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeList(self) -> StepShape_HArray1OfOrientedEdge: 
        """
        None
        """
    def EdgeListValue(self,num : int) -> StepShape_OrientedEdge: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbEdgeList(self) -> int: 
        """
        None
        """
    def SetEdgeList(self,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_OrientedPath(StepShape_Path, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def EdgeList(self) -> StepShape_HArray1OfOrientedEdge: 
        """
        None
        """
    def EdgeListValue(self,num : int) -> StepShape_OrientedEdge: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPathElement : StepShape_EdgeLoop,aOrientation : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbEdgeList(self) -> int: 
        """
        None
        """
    def Orientation(self) -> bool: 
        """
        None
        """
    def PathElement(self) -> StepShape_EdgeLoop: 
        """
        None
        """
    def SetEdgeList(self,aEdgeList : StepShape_HArray1OfOrientedEdge) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
        """
    def SetPathElement(self,aPathElement : StepShape_EdgeLoop) -> None: 
        """
        None
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
class StepShape_PlusMinusTolerance(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,range : StepShape_ToleranceMethodDefinition,toleranced_dimension : StepShape_DimensionalCharacteristic) -> None: 
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
    def Range(self) -> StepShape_ToleranceMethodDefinition: 
        """
        None
        """
    def SetRange(self,range : StepShape_ToleranceMethodDefinition) -> None: 
        """
        None
        """
    def SetTolerancedDimension(self,toleranced_dimension : StepShape_DimensionalCharacteristic) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TolerancedDimension(self) -> StepShape_DimensionalCharacteristic: 
        """
        None
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
class StepShape_PointRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity PointRepresentationRepresentation of STEP entity PointRepresentationRepresentation of STEP entity PointRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_PolyLoop(StepShape_Loop, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPolygon : OCP.StepGeom.StepGeom_HArray1OfCartesianPoint) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbPolygon(self) -> int: 
        """
        None
        """
    def Polygon(self) -> OCP.StepGeom.StepGeom_HArray1OfCartesianPoint: 
        """
        None
        """
    def PolygonValue(self,num : int) -> OCP.StepGeom.StepGeom_CartesianPoint: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPolygon(self,aPolygon : OCP.StepGeom.StepGeom_HArray1OfCartesianPoint) -> None: 
        """
        None
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
class StepShape_PrecisionQualifier(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,precision_value : int) -> None: 
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
    def PrecisionValue(self) -> int: 
        """
        None
        """
    def SetPrecisionValue(self,precision_value : int) -> None: 
        """
        None
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
class StepShape_QualifiedRepresentationItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbQualifiers(self) -> int: 
        """
        None
        """
    def Qualifiers(self) -> StepShape_HArray1OfValueQualifier: 
        """
        None
        """
    def QualifiersValue(self,num : int) -> StepShape_ValueQualifier: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetQualifiers(self,qualifiers : StepShape_HArray1OfValueQualifier) -> None: 
        """
        None
        """
    def SetQualifiersValue(self,num : int,aqualifier : StepShape_ValueQualifier) -> None: 
        """
        None
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
class StepShape_ReversibleTopologyItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a ReversibleTopologyItem Kind Entity that is : 1 -> Edge 2 -> Path 3 -> Face 4 -> FaceBound 5 -> ClosedShell 6 -> OpenShell 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ClosedShell(self) -> StepShape_ClosedShell: 
        """
        returns Value as a ClosedShell (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Edge(self) -> StepShape_Edge: 
        """
        returns Value as a Edge (Null if another type)
        """
    def Face(self) -> StepShape_Face: 
        """
        returns Value as a Face (Null if another type)
        """
    def FaceBound(self) -> StepShape_FaceBound: 
        """
        returns Value as a FaceBound (Null if another type)
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def OpenShell(self) -> StepShape_OpenShell: 
        """
        returns Value as a OpenShell (Null if another type)
        """
    def Path(self) -> StepShape_Path: 
        """
        returns Value as a Path (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_RevolvedAreaSolid(StepShape_SweptAreaSolid, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Angle(self) -> float: 
        """
        None
        """
    def Axis(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface,aAxis : OCP.StepGeom.StepGeom_Axis1Placement,aAngle : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetAngle(self,aAngle : float) -> None: 
        """
        None
        """
    def SetAxis(self,aAxis : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptArea(self,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> None: 
        """
        None
        """
    def SweptArea(self) -> OCP.StepGeom.StepGeom_CurveBoundedSurface: 
        """
        None
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
class StepShape_RevolvedFaceSolid(StepShape_SweptFaceSolid, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Angle(self) -> float: 
        """
        None
        """
    def Axis(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : StepShape_FaceSurface) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : StepShape_FaceSurface,aAxis : OCP.StepGeom.StepGeom_Axis1Placement,aAngle : float) -> None: ...
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
    def SetAngle(self,aAngle : float) -> None: 
        """
        None
        """
    def SetAxis(self,aAxis : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptFace(self,aSweptArea : StepShape_FaceSurface) -> None: 
        """
        None
        """
    def SweptFace(self) -> StepShape_FaceSurface: 
        """
        None
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
class StepShape_RightAngularWedge(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : OCP.StepGeom.StepGeom_Axis2Placement3d,aX : float,aY : float,aZ : float,aLtx : float) -> None: 
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
    def Ltx(self) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
        """
        None
        """
    def SetLtx(self,aLtx : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def SetX(self,aX : float) -> None: 
        """
        None
        """
    def SetY(self,aY : float) -> None: 
        """
        None
        """
    def SetZ(self,aZ : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def X(self) -> float: 
        """
        None
        """
    def Y(self) -> float: 
        """
        None
        """
    def Z(self) -> float: 
        """
        None
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
class StepShape_RightCircularCone(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Height(self) -> float: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : OCP.StepGeom.StepGeom_Axis1Placement,aHeight : float,aRadius : float,aSemiAngle : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SemiAngle(self) -> float: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
        """
    def SetSemiAngle(self,aSemiAngle : float) -> None: 
        """
        None
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
class StepShape_RightCircularCylinder(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Height(self) -> float: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : OCP.StepGeom.StepGeom_Axis1Placement,aHeight : float,aRadius : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetHeight(self,aHeight : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
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
class StepShape_SeamEdge(StepShape_OrientedEdge, StepShape_Edge, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SeamEdgeRepresentation of STEP entity SeamEdgeRepresentation of STEP entity SeamEdge
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
    def EdgeElement(self) -> StepShape_Edge: 
        """
        None
        """
    def EdgeEnd(self) -> StepShape_Vertex: 
        """
        None
        """
    def EdgeStart(self) -> StepShape_Vertex: 
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aOrientedEdge_EdgeElement : StepShape_Edge,aOrientedEdge_Orientation : bool,aPcurveReference : OCP.StepGeom.StepGeom_Pcurve) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def Orientation(self) -> bool: 
        """
        None
        """
    def PcurveReference(self) -> OCP.StepGeom.StepGeom_Pcurve: 
        """
        Returns field PcurveReference
        """
    def SetEdgeElement(self,aEdgeElement : StepShape_Edge) -> None: 
        """
        None
        """
    def SetEdgeEnd(self,aEdgeEnd : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetEdgeStart(self,aEdgeStart : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOrientation(self,aOrientation : bool) -> None: 
        """
        None
        """
    def SetPcurveReference(self,PcurveReference : OCP.StepGeom.StepGeom_Pcurve) -> None: 
        """
        Set field PcurveReference
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
class StepShape_ShapeDefinitionRepresentation(OCP.StepRepr.StepRepr_PropertyDefinitionRepresentation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ShapeDefinitionRepresentationRepresentation of STEP entity ShapeDefinitionRepresentationRepresentation of STEP entity ShapeDefinitionRepresentation
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Definition(self) -> OCP.StepRepr.StepRepr_RepresentedDefinition: 
        """
        Returns field Definition
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
    def Init(self,aDefinition : OCP.StepRepr.StepRepr_RepresentedDefinition,aUsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def SetDefinition(self,Definition : OCP.StepRepr.StepRepr_RepresentedDefinition) -> None: 
        """
        Set field Definition
        """
    def SetUsedRepresentation(self,UsedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        Set field UsedRepresentation
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UsedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        Returns field UsedRepresentation
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
class StepShape_ShapeDimensionRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ShapeDimensionRepresentationRepresentation of STEP entity ShapeDimensionRepresentationRepresentation of STEP entity ShapeDimensionRepresentation
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theItems : StepShape_HArray1OfShapeDimensionRepresentationItem,theContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        Initialize all fields AP214

        Initialize all fields AP242
        """
    @overload
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,theContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: ...
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsAP242(self) -> StepShape_HArray1OfShapeDimensionRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetItemsAP242(self,theItems : StepShape_HArray1OfShapeDimensionRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ShapeDimensionRepresentationItem(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a ShapeDimensionRepresentationItem Kind Entity that is : 1 -> CompoundRepresentationItem 2 -> DescriptiveRepresentationItem 3 -> MeasureRepresentationItem 4 -> Placement 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CompoundRepresentationItem(self) -> OCP.StepRepr.StepRepr_CompoundRepresentationItem: 
        """
        returns Value as a CompoundRepresentationItem (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DescriptiveRepresentationItem(self) -> OCP.StepRepr.StepRepr_DescriptiveRepresentationItem: 
        """
        returns Value as a DescriptiveRepresentationItem (Null if another type)
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def MeasureRepresentationItem(self) -> OCP.StepRepr.StepRepr_MeasureRepresentationItem: 
        """
        returns Value as a MeasureRepresentationItem (Null if another type)
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Placement(self) -> OCP.StepGeom.StepGeom_Placement: 
        """
        returns Value as a Placement (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_AdvancedBrepShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ShapeRepresentationWithParameters(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ShapeRepresentationWithParametersRepresentation of STEP entity ShapeRepresentationWithParametersRepresentation of STEP entity ShapeRepresentationWithParameters
    """
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_Shell(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a Shell Kind Entity that is : 1 -> OpenShell 2 -> ClosedShell 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def ClosedShell(self) -> StepShape_ClosedShell: 
        """
        returns Value as a ClosedShell (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def OpenShell(self) -> StepShape_OpenShell: 
        """
        returns Value as a OpenShell (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_ShellBasedSurfaceModel(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSbsmBoundary : StepShape_HArray1OfShell) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbSbsmBoundary(self) -> int: 
        """
        None
        """
    def SbsmBoundary(self) -> StepShape_HArray1OfShell: 
        """
        None
        """
    def SbsmBoundaryValue(self,num : int) -> StepShape_Shell: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSbsmBoundary(self,aSbsmBoundary : StepShape_HArray1OfShell) -> None: 
        """
        None
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
class StepShape_FacetedBrep(StepShape_ManifoldSolidBrep, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None

        None
        """
    @overload
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aOuter : StepShape_ClosedShell) -> None: ...
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
    def Outer(self) -> StepShape_ConnectedFaceSet: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOuter(self,aOuter : StepShape_ConnectedFaceSet) -> None: 
        """
        None
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
class StepShape_SolidReplica(StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aParentSolid : StepShape_SolidModel,aTransformation : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def ParentSolid(self) -> StepShape_SolidModel: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentSolid(self,aParentSolid : StepShape_SolidModel) -> None: 
        """
        None
        """
    def SetTransformation(self,aTransformation : OCP.StepGeom.StepGeom_CartesianTransformationOperator3d) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transformation(self) -> OCP.StepGeom.StepGeom_CartesianTransformationOperator3d: 
        """
        None
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
class StepShape_Sphere(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Centre(self) -> OCP.StepGeom.StepGeom_Point: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aRadius : float,aCentre : OCP.StepGeom.StepGeom_Point) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Radius(self) -> float: 
        """
        None
        """
    def SetCentre(self,aCentre : OCP.StepGeom.StepGeom_Point) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRadius(self,aRadius : float) -> None: 
        """
        None
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
class StepShape_Subedge(StepShape_Edge, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SubedgeRepresentation of STEP entity SubedgeRepresentation of STEP entity Subedge
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
    def EdgeEnd(self) -> StepShape_Vertex: 
        """
        None
        """
    def EdgeStart(self) -> StepShape_Vertex: 
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
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aEdge_EdgeStart : StepShape_Vertex,aEdge_EdgeEnd : StepShape_Vertex,aParentEdge : StepShape_Edge) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def ParentEdge(self) -> StepShape_Edge: 
        """
        Returns field ParentEdge
        """
    def SetEdgeEnd(self,aEdgeEnd : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetEdgeStart(self,aEdgeStart : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentEdge(self,ParentEdge : StepShape_Edge) -> None: 
        """
        Set field ParentEdge
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
class StepShape_Subface(StepShape_Face, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity SubfaceRepresentation of STEP entity SubfaceRepresentation of STEP entity Subface
    """
    def Bounds(self) -> StepShape_HArray1OfFaceBound: 
        """
        None
        """
    def BoundsValue(self,num : int) -> StepShape_FaceBound: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aRepresentationItem_Name : OCP.TCollection.TCollection_HAsciiString,aFace_Bounds : StepShape_HArray1OfFaceBound,aParentFace : StepShape_Face) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def NbBounds(self) -> int: 
        """
        None
        """
    def ParentFace(self) -> StepShape_Face: 
        """
        Returns field ParentFace
        """
    def SetBounds(self,aBounds : StepShape_HArray1OfFaceBound) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetParentFace(self,ParentFace : StepShape_Face) -> None: 
        """
        Set field ParentFace
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
class StepShape_SurfaceModel(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a SurfaceModel Kind Entity that is : 1 -> ShellBasedSurfaceModel 2 -> FaceBasedSurfaceModel 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def ShellBasedSurfaceModel(self) -> StepShape_ShellBasedSurfaceModel: 
        """
        returns Value as a ShellBasedSurfaceModel (Null if another type)
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_ExtrudedAreaSolid(StepShape_SweptAreaSolid, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Depth(self) -> float: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtrudedDirection(self) -> OCP.StepGeom.StepGeom_Direction: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface,aExtrudedDirection : OCP.StepGeom.StepGeom_Direction,aDepth : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDepth(self,aDepth : float) -> None: 
        """
        None
        """
    def SetExtrudedDirection(self,aExtrudedDirection : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptArea(self,aSweptArea : OCP.StepGeom.StepGeom_CurveBoundedSurface) -> None: 
        """
        None
        """
    def SweptArea(self) -> OCP.StepGeom.StepGeom_CurveBoundedSurface: 
        """
        None
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
class StepShape_ExtrudedFaceSolid(StepShape_SweptFaceSolid, StepShape_SolidModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Depth(self) -> float: 
        """
        None
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtrudedDirection(self) -> OCP.StepGeom.StepGeom_Direction: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSweptArea : StepShape_FaceSurface,aExtrudedDirection : OCP.StepGeom.StepGeom_Direction,aDepth : float) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetDepth(self,aDepth : float) -> None: 
        """
        None
        """
    def SetExtrudedDirection(self,aExtrudedDirection : OCP.StepGeom.StepGeom_Direction) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSweptFace(self,aSweptArea : StepShape_FaceSurface) -> None: 
        """
        None
        """
    def SweptFace(self) -> StepShape_FaceSurface: 
        """
        None
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
class StepShape_ToleranceMethodDefinition(OCP.StepData.StepData_SelectType):
    """
    Added for Dimensional Tolerances
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of ValueQualifier Select Type : 1 -> ToleranceValue from StepShape 2 -> LimitsAndFits from StepShape
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def LimitsAndFits(self) -> StepShape_LimitsAndFits: 
        """
        Returns Value as LimitsAndFits
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def ToleranceValue(self) -> StepShape_ToleranceValue: 
        """
        Returns Value as ToleranceValue
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def __init__(self) -> None: ...
    pass
class StepShape_ToleranceValue(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,lower_bound : OCP.Standard.Standard_Transient,upper_bound : OCP.Standard.Standard_Transient) -> None: 
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
    def LowerBound(self) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def SetLowerBound(self,lower_bound : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def SetUpperBound(self,upper_bound : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpperBound(self) -> OCP.Standard.Standard_Transient: 
        """
        None
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
class StepShape_AdvancedFace(StepShape_FaceSurface, StepShape_Face, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Bounds(self) -> StepShape_HArray1OfFaceBound: 
        """
        None
        """
    def BoundsValue(self,num : int) -> StepShape_FaceBound: 
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
    def FaceGeometry(self) -> OCP.StepGeom.StepGeom_Surface: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aBounds : StepShape_HArray1OfFaceBound,aFaceGeometry : OCP.StepGeom.StepGeom_Surface,aSameSense : bool) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbBounds(self) -> int: 
        """
        None
        """
    def SameSense(self) -> bool: 
        """
        None
        """
    def SetBounds(self,aBounds : StepShape_HArray1OfFaceBound) -> None: 
        """
        None
        """
    def SetFaceGeometry(self,aFaceGeometry : OCP.StepGeom.StepGeom_Surface) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetSameSense(self,aSameSense : bool) -> None: 
        """
        None
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
class StepShape_Torus(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPosition : OCP.StepGeom.StepGeom_Axis1Placement,aMajorRadius : float,aMinorRadius : float) -> None: 
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
    def MajorRadius(self) -> float: 
        """
        None
        """
    def MinorRadius(self) -> float: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Position(self) -> OCP.StepGeom.StepGeom_Axis1Placement: 
        """
        None
        """
    def SetMajorRadius(self,aMajorRadius : float) -> None: 
        """
        None
        """
    def SetMinorRadius(self,aMinorRadius : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPosition(self,aPosition : OCP.StepGeom.StepGeom_Axis1Placement) -> None: 
        """
        None
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
class StepShape_TransitionalShapeRepresentation(StepShape_ShapeRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    def ContextOfItems(self) -> OCP.StepRepr.StepRepr_RepresentationContext: 
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
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
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
    def Items(self) -> OCP.StepRepr.StepRepr_HArray1OfRepresentationItem: 
        """
        None
        """
    def ItemsValue(self,num : int) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbItems(self) -> int: 
        """
        None
        """
    def SetContextOfItems(self,aContextOfItems : OCP.StepRepr.StepRepr_RepresentationContext) -> None: 
        """
        None
        """
    def SetItems(self,aItems : OCP.StepRepr.StepRepr_HArray1OfRepresentationItem) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_TypeQualifier(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def Init(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,name : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_ValueFormatTypeQualifier(OCP.Standard.Standard_Transient):
    """
    Added for Dimensional TolerancesAdded for Dimensional TolerancesAdded for Dimensional Tolerances
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
    def FormatType(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns field FormatType
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theFormatType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Init all field own and inherited
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
    def SetFormatType(self,theFormatType : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Set field FormatType
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
class StepShape_ValueQualifier(OCP.StepData.StepData_SelectType):
    """
    Added for Dimensional Tolerances
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,ent : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Recognize a SelectMember (kind, name). Returns a positive value which identifies the case in the List of immediate cases (distinct from the List of Entity Types). Zero if not recognizes Default returns 0, saying that no immediate value is allowed
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a kind of ValueQualifier Select Type : 1 -> PrecisionQualifier from StepShape 2 -> TypeQualifier from StepShape 3 -> UnceraintyQualifier .. not yet implemented 4 -> ValueFormatTypeQualifier
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def Int(self) -> int: 
        """
        This internal method gives access to a value implemented by an Integer (to read it)
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
        """
    def IsNull(self) -> bool: 
        """
        Returns True if there is no Stored Entity (i.e. it is Null)
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if the Type of an Entity complies with the definition list of the SelectType. Also checks for a SelectMember Default Implementation looks for CaseNum or CaseMem positive
        """
    def Member(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns Value as a SelectMember. Null if not a SelectMember
        """
    def NewMember(self) -> OCP.StepData.StepData_SelectMember: 
        """
        Returns a preferred SelectMember. Default returns a Null By default, a SelectMember can be set according to data type and Name : it is a SelectNamed if Name is defined
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def PrecisionQualifier(self) -> StepShape_PrecisionQualifier: 
        """
        Returns Value as PrecisionQualifier
        """
    def Real(self) -> float: 
        """
        None
        """
    def SelectName(self) -> str: 
        """
        Returns the type name of SelectMember. If no SelectMember or with no type name, returns an empty string To change it, pass through the SelectMember itself
        """
    def SetBoolean(self,val : bool,name : str='') -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        This internal method gives access to a value implemented by an Integer (to set it) : a SelectMember MUST ALREADY BE THERE !
        """
    def SetInteger(self,val : int,name : str='') -> None: 
        """
        Sets a new Integer value, with an optional type name Warning : If a SelectMember is already set, works on it : value and name must then be accepted by this SelectMember
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical,name : str='') -> None: 
        """
        None
        """
    def SetReal(self,val : float,name : str='') -> None: 
        """
        None
        """
    def SetValue(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        Stores an Entity. This allows to define a specific SelectType class with one read method per member Type, which returns the Value casted with the good Type.
        """
    def Type(self) -> OCP.Standard.Standard_Type: 
        """
        Returns the Effective (Dynamic) Type of the Stored Entity If it is Null, returns TYPE(Transient)
        """
    def TypeQualifier(self) -> StepShape_TypeQualifier: 
        """
        Returns Value as TypeQualifier
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the Stored Entity. Can be used to define specific read methods (see above)
        """
    def ValueFormatTypeQualifier(self) -> StepShape_ValueFormatTypeQualifier: 
        """
        Returns Value as ValueFormatTypeQualifier
        """
    def __init__(self) -> None: ...
    pass
class StepShape_Vertex(StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_VertexLoop(StepShape_Loop, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLoopVertex : StepShape_Vertex) -> None: 
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
    def LoopVertex(self) -> StepShape_Vertex: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetLoopVertex(self,aLoopVertex : StepShape_Vertex) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
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
class StepShape_VertexPoint(StepShape_Vertex, StepShape_TopologicalRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aVertexGeometry : OCP.StepGeom.StepGeom_Point) -> None: 
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
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetVertexGeometry(self,aVertexGeometry : OCP.StepGeom.StepGeom_Point) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def VertexGeometry(self) -> OCP.StepGeom.StepGeom_Point: 
        """
        None
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
StepShape_Equal: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Equal: 0>
StepShape_Large: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Large: 1>
StepShape_Small: OCP.StepShape.StepShape_AngleRelator # value = <StepShape_AngleRelator.StepShape_Small: 2>
StepShape_boDifference: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boDifference: 0>
StepShape_boIntersection: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boIntersection: 1>
StepShape_boUnion: OCP.StepShape.StepShape_BooleanOperator # value = <StepShape_BooleanOperator.StepShape_boUnion: 2>
