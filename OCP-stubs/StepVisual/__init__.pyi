import OCP.StepVisual
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.StepShape
import OCP.StepData
import OCP.TColStd
import OCP.TCollection
import OCP.Standard
import OCP.StepGeom
import OCP.StepRepr
import OCP.TColgp
import OCP.StepBasic
import OCP.Interface
__all__  = [
"StepVisual_StyledItem",
"StepVisual_AnnotationOccurrence",
"StepVisual_AnnotationFillArea",
"StepVisual_AnnotationFillAreaOccurrence",
"StepVisual_AnnotationCurveOccurrence",
"StepVisual_AnnotationPlane",
"StepVisual_AnnotationPlaneElement",
"StepVisual_AnnotationText",
"StepVisual_AnnotationTextOccurrence",
"StepVisual_AreaInSet",
"StepVisual_AreaOrView",
"StepVisual_Array1OfAnnotationPlaneElement",
"StepVisual_Array1OfBoxCharacteristicSelect",
"StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect",
"StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect",
"StepVisual_Array1OfCurveStyleFontPattern",
"StepVisual_Array1OfDirectionCountSelect",
"StepVisual_Array1OfDraughtingCalloutElement",
"StepVisual_Array1OfFillStyleSelect",
"StepVisual_Array1OfInvisibleItem",
"StepVisual_Array1OfLayeredItem",
"StepVisual_Array1OfPresentationStyleAssignment",
"StepVisual_Array1OfPresentationStyleSelect",
"StepVisual_Array1OfStyleContextSelect",
"StepVisual_Array1OfSurfaceStyleElementSelect",
"StepVisual_Array1OfTessellatedItem",
"StepVisual_Array1OfTextOrCharacter",
"StepVisual_Colour",
"StepVisual_BoxCharacteristicSelect",
"StepVisual_CameraImage",
"StepVisual_CameraImage2dWithScale",
"StepVisual_CameraImage3dWithScale",
"StepVisual_CameraModel",
"StepVisual_CameraModelD2",
"StepVisual_CameraModelD3",
"StepVisual_CameraModelD3MultiClipping",
"StepVisual_CameraModelD3MultiClippingInterectionSelect",
"StepVisual_CameraModelD3MultiClippingIntersection",
"StepVisual_CameraModelD3MultiClippingUnion",
"StepVisual_CameraModelD3MultiClippingUnionSelect",
"StepVisual_CameraUsage",
"StepVisual_CentralOrParallel",
"StepVisual_DraughtingModel",
"StepVisual_BackgroundColour",
"StepVisual_ColourSpecification",
"StepVisual_ColourRgb",
"StepVisual_CompositeText",
"StepVisual_CompositeTextWithExtent",
"StepVisual_Invisibility",
"StepVisual_OverRidingStyledItem",
"StepVisual_TessellatedItem",
"StepVisual_CurveStyle",
"StepVisual_CurveStyleFont",
"StepVisual_CurveStyleFontPattern",
"StepVisual_CurveStyleFontSelect",
"StepVisual_DirectionCountSelect",
"StepVisual_DraughtingAnnotationOccurrence",
"StepVisual_DraughtingCallout",
"StepVisual_DraughtingCalloutElement",
"StepVisual_CharacterizedObjectAndCharacterizedRepresentationAndDraughtingModelAndRepresentation",
"StepVisual_PreDefinedColour",
"StepVisual_PreDefinedItem",
"StepVisual_ExternallyDefinedCurveFont",
"StepVisual_ExternallyDefinedTextFont",
"StepVisual_FillAreaStyle",
"StepVisual_FillAreaStyleColour",
"StepVisual_FillStyleSelect",
"StepVisual_FontSelect",
"StepVisual_HArray1OfAnnotationPlaneElement",
"StepVisual_HArray1OfBoxCharacteristicSelect",
"StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect",
"StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect",
"StepVisual_HArray1OfCurveStyleFontPattern",
"StepVisual_HArray1OfDirectionCountSelect",
"StepVisual_HArray1OfDraughtingCalloutElement",
"StepVisual_HArray1OfFillStyleSelect",
"StepVisual_HArray1OfInvisibleItem",
"StepVisual_HArray1OfLayeredItem",
"StepVisual_HArray1OfPresentationStyleAssignment",
"StepVisual_HArray1OfPresentationStyleSelect",
"StepVisual_HArray1OfStyleContextSelect",
"StepVisual_HArray1OfSurfaceStyleElementSelect",
"StepVisual_HArray1OfTextOrCharacter",
"StepVisual_ContextDependentInvisibility",
"StepVisual_InvisibilityContext",
"StepVisual_InvisibleItem",
"StepVisual_LayeredItem",
"StepVisual_MarkerMember",
"StepVisual_MarkerSelect",
"StepVisual_MarkerType",
"StepVisual_PresentationRepresentation",
"StepVisual_MechanicalDesignGeometricPresentationRepresentation",
"StepVisual_NullStyle",
"StepVisual_NullStyleMember",
"StepVisual_ContextDependentOverRidingStyledItem",
"StepVisual_PlanarExtent",
"StepVisual_PlanarBox",
"StepVisual_PointStyle",
"StepVisual_DraughtingPreDefinedColour",
"StepVisual_PreDefinedCurveFont",
"StepVisual_DraughtingPreDefinedCurveFont",
"StepVisual_PreDefinedTextFont",
"StepVisual_PresentationArea",
"StepVisual_PresentationLayerAssignment",
"StepVisual_PresentationLayerUsage",
"StepVisual_MechanicalDesignGeometricPresentationArea",
"StepVisual_PresentationRepresentationSelect",
"StepVisual_PresentationSet",
"StepVisual_PresentationSize",
"StepVisual_PresentationSizeAssignmentSelect",
"StepVisual_PresentationStyleAssignment",
"StepVisual_PresentationStyleByContext",
"StepVisual_PresentationStyleSelect",
"StepVisual_PresentationView",
"StepVisual_PresentedItem",
"StepVisual_PresentedItemRepresentation",
"StepVisual_StyleContextSelect",
"StepVisual_AnnotationCurveOccurrenceAndAnnotationOccurrenceAndGeomReprItemAndReprItemAndStyledItem",
"StepVisual_StyledItemTarget",
"StepVisual_SurfaceSide",
"StepVisual_SurfaceSideStyle",
"StepVisual_SurfaceStyleBoundary",
"StepVisual_SurfaceStyleControlGrid",
"StepVisual_SurfaceStyleElementSelect",
"StepVisual_SurfaceStyleFillArea",
"StepVisual_SurfaceStyleParameterLine",
"StepVisual_SurfaceStyleSegmentationCurve",
"StepVisual_SurfaceStyleSilhouette",
"StepVisual_SurfaceStyleUsage",
"StepVisual_Template",
"StepVisual_TemplateInstance",
"StepVisual_TessellatedAnnotationOccurrence",
"StepVisual_TessellatedCurveSet",
"StepVisual_TessellatedGeometricSet",
"StepVisual_CoordinatesList",
"StepVisual_TextLiteral",
"StepVisual_TextOrCharacter",
"StepVisual_TextPath",
"StepVisual_TextStyle",
"StepVisual_TextStyleForDefinedFont",
"StepVisual_TextStyleWithBoxCharacteristics",
"StepVisual_VectorOfHSequenceOfInteger",
"StepVisual_ViewVolume",
"StepVisual_Null",
"StepVisual_copCentral",
"StepVisual_copParallel",
"StepVisual_mtAsterisk",
"StepVisual_mtDot",
"StepVisual_mtPlus",
"StepVisual_mtRing",
"StepVisual_mtSquare",
"StepVisual_mtTriangle",
"StepVisual_mtX",
"StepVisual_ssBoth",
"StepVisual_ssNegative",
"StepVisual_ssPositive",
"StepVisual_tpDown",
"StepVisual_tpLeft",
"StepVisual_tpRight",
"StepVisual_tpUp"
]
class StepVisual_StyledItem(OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AnnotationOccurrence(StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AnnotationFillArea(OCP.StepShape.StepShape_GeometricCurveSet, OCP.StepShape.StepShape_GeometricSet, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Elements(self) -> OCP.StepShape.StepShape_HArray1OfGeometricSetSelect: 
        """
        None
        """
    def ElementsValue(self,num : int) -> OCP.StepShape.StepShape_GeometricSetSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aElements : OCP.StepShape.StepShape_HArray1OfGeometricSetSelect) -> None: 
        """
        None
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
    def SetElements(self,aElements : OCP.StepShape.StepShape_HArray1OfGeometricSetSelect) -> None: 
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
class StepVisual_AnnotationFillAreaOccurrence(StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def FillStyleTarget(self) -> OCP.StepGeom.StepGeom_GeometricRepresentationItem: 
        """
        Returns field fill_style_target
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theStyles : StepVisual_HArray1OfPresentationStyleAssignment,theItem : OCP.Standard.Standard_Transient,theFillStyleTarget : OCP.StepGeom.StepGeom_GeometricRepresentationItem) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    def SetFillStyleTarget(self,theTarget : OCP.StepGeom.StepGeom_GeometricRepresentationItem) -> None: 
        """
        Set field fill_style_target
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AnnotationCurveOccurrence(StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AnnotationPlane(StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Elements(self) -> StepVisual_HArray1OfAnnotationPlaneElement: 
        """
        Returns field Elements
        """
    def ElementsValue(self,theNum : int) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns Elements with the given number
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theStyles : StepVisual_HArray1OfPresentationStyleAssignment,theItem : OCP.Standard.Standard_Transient,theElements : StepVisual_HArray1OfAnnotationPlaneElement) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbElements(self) -> int: 
        """
        Returns number of Elements
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    def SetElements(self,theElements : StepVisual_HArray1OfAnnotationPlaneElement) -> None: 
        """
        Set field Elements
        """
    def SetElementsValue(self,theNum : int,theItem : StepVisual_AnnotationPlaneElement) -> None: 
        """
        Sets Elements with given number
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AnnotationPlaneElement(OCP.StepData.StepData_SelectType):
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
        Recognizes a IdAttributeSelect Kind Entity that is : 1 -> DraughtingCallout 2 -> StyledItem 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DraughtingCallout(self) -> StepVisual_DraughtingCallout: 
        """
        returns Value as a DraughtingCallout (Null if another type)
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
    def StyledItem(self) -> StepVisual_StyledItem: 
        """
        returns Value as a StyledItem (Null if another type)
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
class StepVisual_AnnotationText(OCP.StepRepr.StepRepr_MappedItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappingSource(self) -> OCP.StepRepr.StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_AnnotationTextOccurrence(StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_AreaInSet(OCP.Standard.Standard_Transient):
    def Area(self) -> StepVisual_PresentationArea: 
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
    def InSet(self) -> StepVisual_PresentationSet: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aArea : StepVisual_PresentationArea,aInSet : StepVisual_PresentationSet) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetArea(self,aArea : StepVisual_PresentationArea) -> None: 
        """
        None
        """
    def SetInSet(self,aInSet : StepVisual_PresentationSet) -> None: 
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
class StepVisual_AreaOrView(OCP.StepData.StepData_SelectType):
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
        Recognizes a AreaOrView Kind Entity that is : 1 -> PresentationArea 2 -> PresentationView 0 else
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
    def PresentationArea(self) -> StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def PresentationView(self) -> StepVisual_PresentationView: 
        """
        returns Value as a PresentationView (Null if another type)
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
class StepVisual_Array1OfAnnotationPlaneElement():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_AnnotationPlaneElement: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_AnnotationPlaneElement) -> None: 
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
    def Last(self) -> StepVisual_AnnotationPlaneElement: 
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
    def Move(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_AnnotationPlaneElement) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_AnnotationPlaneElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_AnnotationPlaneElement,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfBoxCharacteristicSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_BoxCharacteristicSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_BoxCharacteristicSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_BoxCharacteristicSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_BoxCharacteristicSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_BoxCharacteristicSelect) -> None: 
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
    def Last(self) -> StepVisual_BoxCharacteristicSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_BoxCharacteristicSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_BoxCharacteristicSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_BoxCharacteristicSelect,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: 
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
    def Last(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_CameraModelD3MultiClippingInterectionSelect,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: 
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
    def Last(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_CameraModelD3MultiClippingUnionSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfCurveStyleFontPattern():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_CurveStyleFontPattern: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CurveStyleFontPattern: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CurveStyleFontPattern: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_CurveStyleFontPattern: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_CurveStyleFontPattern) -> None: 
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
    def Last(self) -> StepVisual_CurveStyleFontPattern: 
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
    def Move(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CurveStyleFontPattern) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CurveStyleFontPattern: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_CurveStyleFontPattern,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfDirectionCountSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_DirectionCountSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_DirectionCountSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_DirectionCountSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_DirectionCountSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_DirectionCountSelect) -> None: 
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
    def Last(self) -> StepVisual_DirectionCountSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_DirectionCountSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_DirectionCountSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_DirectionCountSelect,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfDraughtingCalloutElement():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_DraughtingCalloutElement: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_DraughtingCalloutElement) -> None: 
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
    def Last(self) -> StepVisual_DraughtingCalloutElement: 
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
    def Move(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_DraughtingCalloutElement) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_DraughtingCalloutElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_DraughtingCalloutElement,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfFillStyleSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfFillStyleSelect) -> StepVisual_Array1OfFillStyleSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_FillStyleSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_FillStyleSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_FillStyleSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_FillStyleSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_FillStyleSelect) -> None: 
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
    def Last(self) -> StepVisual_FillStyleSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfFillStyleSelect) -> StepVisual_Array1OfFillStyleSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_FillStyleSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_FillStyleSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfFillStyleSelect) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_FillStyleSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfInvisibleItem():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfInvisibleItem) -> StepVisual_Array1OfInvisibleItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_InvisibleItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_InvisibleItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_InvisibleItem: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_InvisibleItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_InvisibleItem) -> None: 
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
    def Last(self) -> StepVisual_InvisibleItem: 
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
    def Move(self,theOther : StepVisual_Array1OfInvisibleItem) -> StepVisual_Array1OfInvisibleItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_InvisibleItem) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_InvisibleItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfInvisibleItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_InvisibleItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfLayeredItem():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfLayeredItem) -> StepVisual_Array1OfLayeredItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_LayeredItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_LayeredItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_LayeredItem: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_LayeredItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_LayeredItem) -> None: 
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
    def Last(self) -> StepVisual_LayeredItem: 
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
    def Move(self,theOther : StepVisual_Array1OfLayeredItem) -> StepVisual_Array1OfLayeredItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_LayeredItem) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_LayeredItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfLayeredItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_LayeredItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfPresentationStyleAssignment():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_PresentationStyleAssignment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_PresentationStyleAssignment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_PresentationStyleAssignment: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_PresentationStyleAssignment: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_PresentationStyleAssignment) -> None: 
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
    def Last(self) -> StepVisual_PresentationStyleAssignment: 
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
    def Move(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_PresentationStyleAssignment) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_PresentationStyleAssignment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_PresentationStyleAssignment,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfPresentationStyleSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_PresentationStyleSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_PresentationStyleSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_PresentationStyleSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_PresentationStyleSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_PresentationStyleSelect) -> None: 
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
    def Last(self) -> StepVisual_PresentationStyleSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_PresentationStyleSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_PresentationStyleSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_PresentationStyleSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfStyleContextSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfStyleContextSelect) -> StepVisual_Array1OfStyleContextSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_StyleContextSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_StyleContextSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_StyleContextSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_StyleContextSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_StyleContextSelect) -> None: 
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
    def Last(self) -> StepVisual_StyleContextSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfStyleContextSelect) -> StepVisual_Array1OfStyleContextSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_StyleContextSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_StyleContextSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theBegin : StepVisual_StyleContextSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfStyleContextSelect) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfSurfaceStyleElementSelect():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_SurfaceStyleElementSelect) -> None: 
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
    def Last(self) -> StepVisual_SurfaceStyleElementSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_SurfaceStyleElementSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_SurfaceStyleElementSelect,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfTessellatedItem():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfTessellatedItem) -> StepVisual_Array1OfTessellatedItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_TessellatedItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_TessellatedItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_TessellatedItem: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_TessellatedItem: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_TessellatedItem) -> None: 
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
    def Last(self) -> StepVisual_TessellatedItem: 
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
    def Move(self,theOther : StepVisual_Array1OfTessellatedItem) -> StepVisual_Array1OfTessellatedItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_TessellatedItem) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_TessellatedItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfTessellatedItem) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_TessellatedItem,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Array1OfTextOrCharacter():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : StepVisual_Array1OfTextOrCharacter) -> StepVisual_Array1OfTextOrCharacter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> StepVisual_TextOrCharacter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_TextOrCharacter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_TextOrCharacter: 
        """
        Variable value access
        """
    def First(self) -> StepVisual_TextOrCharacter: 
        """
        Returns first element
        """
    def Init(self,theValue : StepVisual_TextOrCharacter) -> None: 
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
    def Last(self) -> StepVisual_TextOrCharacter: 
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
    def Move(self,theOther : StepVisual_Array1OfTextOrCharacter) -> StepVisual_Array1OfTextOrCharacter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_TextOrCharacter) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_TextOrCharacter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfTextOrCharacter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : StepVisual_TextOrCharacter,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_Colour(OCP.Standard.Standard_Transient):
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
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
class StepVisual_BoxCharacteristicSelect():
    """
    None
    """
    def RealValue(self) -> float: 
        """
        None
        """
    def SetRealValue(self,aValue : float) -> None: 
        """
        None
        """
    def SetTypeOfContent(self,aType : int) -> None: 
        """
        None
        """
    def TypeOfContent(self) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepVisual_CameraImage(OCP.StepRepr.StepRepr_MappedItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappingSource(self) -> OCP.StepRepr.StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_CameraImage2dWithScale(StepVisual_CameraImage, OCP.StepRepr.StepRepr_MappedItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappingSource(self) -> OCP.StepRepr.StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_CameraImage3dWithScale(StepVisual_CameraImage, OCP.StepRepr.StepRepr_MappedItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappingSource(self) -> OCP.StepRepr.StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_CameraModel(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_CameraModelD2(StepVisual_CameraModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aViewWindow : StepVisual_PlanarBox,aViewWindowClipping : bool) -> None: 
        """
        None
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
    def SetViewWindow(self,aViewWindow : StepVisual_PlanarBox) -> None: 
        """
        None
        """
    def SetViewWindowClipping(self,aViewWindowClipping : bool) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewWindow(self) -> StepVisual_PlanarBox: 
        """
        None
        """
    def ViewWindowClipping(self) -> bool: 
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
class StepVisual_CameraModelD3(StepVisual_CameraModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aViewReferenceSystem : OCP.StepGeom.StepGeom_Axis2Placement3d,aPerspectiveOfVolume : StepVisual_ViewVolume) -> None: 
        """
        None
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
    def PerspectiveOfVolume(self) -> StepVisual_ViewVolume: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPerspectiveOfVolume(self,aPerspectiveOfVolume : StepVisual_ViewVolume) -> None: 
        """
        None
        """
    def SetViewReferenceSystem(self,aViewReferenceSystem : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewReferenceSystem(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
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
class StepVisual_CameraModelD3MultiClipping(StepVisual_CameraModelD3, StepVisual_CameraModel, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theViewReferenceSystem : OCP.StepGeom.StepGeom_Axis2Placement3d,thePerspectiveOfVolume : StepVisual_ViewVolume,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: 
        """
        None
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
    def PerspectiveOfVolume(self) -> StepVisual_ViewVolume: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPerspectiveOfVolume(self,aPerspectiveOfVolume : StepVisual_ViewVolume) -> None: 
        """
        None
        """
    def SetShapeClipping(self,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: 
        """
        None
        """
    def SetViewReferenceSystem(self,aViewReferenceSystem : OCP.StepGeom.StepGeom_Axis2Placement3d) -> None: 
        """
        None
        """
    def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewReferenceSystem(self) -> OCP.StepGeom.StepGeom_Axis2Placement3d: 
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
class StepVisual_CameraModelD3MultiClippingInterectionSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CameraModelD3MultiClippingUnion(self) -> StepVisual_CameraModelD3MultiClippingUnion: 
        """
        returns Value as a CameraModelD3MultiClippingUnion (Null if another type)
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
        Recognizes a IdAttributeSelect Kind Entity that is : 1 -> Plane 2 -> CameraModelD3MultiClippingUnion 0 else
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
    def Plane(self) -> OCP.StepGeom.StepGeom_Plane: 
        """
        returns Value as a Plane (Null if another type)
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
class StepVisual_CameraModelD3MultiClippingIntersection(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: 
        """
        None
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
    def SetShapeClipping(self,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect) -> None: 
        """
        None
        """
    def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect: 
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
class StepVisual_CameraModelD3MultiClippingUnion(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect) -> None: 
        """
        None
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
    def SetShapeClipping(self,theShapeClipping : StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect) -> None: 
        """
        None
        """
    def ShapeClipping(self) -> StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect: 
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
class StepVisual_CameraModelD3MultiClippingUnionSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CameraModelD3MultiClippingIntersection(self) -> StepVisual_CameraModelD3MultiClippingIntersection: 
        """
        returns Value as a CameraModelD3MultiClippingIntersection (Null if another type)
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
        Recognizes a IdAttributeSelect Kind Entity that is : 1 -> Plane 2 -> CameraModelD3MultiClippingIntersection 0 else
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
    def Plane(self) -> OCP.StepGeom.StepGeom_Plane: 
        """
        returns Value as a Plane (Null if another type)
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
class StepVisual_CameraUsage(OCP.StepRepr.StepRepr_RepresentationMap, OCP.Standard.Standard_Transient):
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
    def Init(self,aMappingOrigin : OCP.StepRepr.StepRepr_RepresentationItem,aMappedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappedRepresentation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        None
        """
    def MappingOrigin(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def SetMappedRepresentation(self,aMappedRepresentation : OCP.StepRepr.StepRepr_Representation) -> None: 
        """
        None
        """
    def SetMappingOrigin(self,aMappingOrigin : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_CentralOrParallel():
    """
    None

    Members:

      StepVisual_copCentral

      StepVisual_copParallel
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepVisual_copCentral: OCP.StepVisual.StepVisual_CentralOrParallel # value = StepVisual_CentralOrParallel.StepVisual_copCentral
    StepVisual_copParallel: OCP.StepVisual.StepVisual_CentralOrParallel # value = StepVisual_CentralOrParallel.StepVisual_copParallel
    __entries: dict # value = {'StepVisual_copCentral': (StepVisual_CentralOrParallel.StepVisual_copCentral, None), 'StepVisual_copParallel': (StepVisual_CentralOrParallel.StepVisual_copParallel, None)}
    __members__: dict # value = {'StepVisual_copCentral': StepVisual_CentralOrParallel.StepVisual_copCentral, 'StepVisual_copParallel': StepVisual_CentralOrParallel.StepVisual_copParallel}
    pass
class StepVisual_DraughtingModel(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity DraughtingModelRepresentation of STEP entity DraughtingModelRepresentation of STEP entity DraughtingModel
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_BackgroundColour(StepVisual_Colour, OCP.Standard.Standard_Transient):
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
    def Init(self,aPresentation : StepVisual_AreaOrView) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Presentation(self) -> StepVisual_AreaOrView: 
        """
        None
        """
    def SetPresentation(self,aPresentation : StepVisual_AreaOrView) -> None: 
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
class StepVisual_ColourSpecification(StepVisual_Colour, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_ColourRgb(StepVisual_ColourSpecification, StepVisual_Colour, OCP.Standard.Standard_Transient):
    def Blue(self) -> float: 
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
    def Green(self) -> float: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aRed : float,aGreen : float,aBlue : float) -> None: 
        """
        None
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
    def Red(self) -> float: 
        """
        None
        """
    def SetBlue(self,aBlue : float) -> None: 
        """
        None
        """
    def SetGreen(self,aGreen : float) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetRed(self,aRed : float) -> None: 
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
class StepVisual_CompositeText(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CollectedText(self) -> StepVisual_HArray1OfTextOrCharacter: 
        """
        None
        """
    def CollectedTextValue(self,num : int) -> StepVisual_TextOrCharacter: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCollectedText : StepVisual_HArray1OfTextOrCharacter) -> None: 
        """
        None
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
    def NbCollectedText(self) -> int: 
        """
        None
        """
    def SetCollectedText(self,aCollectedText : StepVisual_HArray1OfTextOrCharacter) -> None: 
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
class StepVisual_CompositeTextWithExtent(StepVisual_CompositeText, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CollectedText(self) -> StepVisual_HArray1OfTextOrCharacter: 
        """
        None
        """
    def CollectedTextValue(self,num : int) -> StepVisual_TextOrCharacter: 
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
    def Extent(self) -> StepVisual_PlanarExtent: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCollectedText : StepVisual_HArray1OfTextOrCharacter,aExtent : StepVisual_PlanarExtent) -> None: 
        """
        None
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
    def NbCollectedText(self) -> int: 
        """
        None
        """
    def SetCollectedText(self,aCollectedText : StepVisual_HArray1OfTextOrCharacter) -> None: 
        """
        None
        """
    def SetExtent(self,aExtent : StepVisual_PlanarExtent) -> None: 
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
class StepVisual_Invisibility(OCP.Standard.Standard_Transient):
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
    def Init(self,aInvisibleItems : StepVisual_HArray1OfInvisibleItem) -> None: 
        """
        None
        """
    def InvisibleItems(self) -> StepVisual_HArray1OfInvisibleItem: 
        """
        None
        """
    def InvisibleItemsValue(self,num : int) -> StepVisual_InvisibleItem: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbInvisibleItems(self) -> int: 
        """
        None
        """
    def SetInvisibleItems(self,aInvisibleItems : StepVisual_HArray1OfInvisibleItem) -> None: 
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
class StepVisual_OverRidingStyledItem(StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient,aOverRiddenStyle : StepVisual_StyledItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    def OverRiddenStyle(self) -> StepVisual_StyledItem: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOverRiddenStyle(self,aOverRiddenStyle : StepVisual_StyledItem) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_TessellatedItem(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_CurveStyle(OCP.Standard.Standard_Transient):
    def CurveColour(self) -> StepVisual_Colour: 
        """
        None
        """
    def CurveFont(self) -> StepVisual_CurveStyleFontSelect: 
        """
        None
        """
    def CurveWidth(self) -> OCP.StepBasic.StepBasic_SizeSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCurveFont : StepVisual_CurveStyleFontSelect,aCurveWidth : OCP.StepBasic.StepBasic_SizeSelect,aCurveColour : StepVisual_Colour) -> None: 
        """
        None
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
    def SetCurveColour(self,aCurveColour : StepVisual_Colour) -> None: 
        """
        None
        """
    def SetCurveFont(self,aCurveFont : StepVisual_CurveStyleFontSelect) -> None: 
        """
        None
        """
    def SetCurveWidth(self,aCurveWidth : OCP.StepBasic.StepBasic_SizeSelect) -> None: 
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
class StepVisual_CurveStyleFont(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aPatternList : StepVisual_HArray1OfCurveStyleFontPattern) -> None: 
        """
        None
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
    def NbPatternList(self) -> int: 
        """
        None
        """
    def PatternList(self) -> StepVisual_HArray1OfCurveStyleFontPattern: 
        """
        None
        """
    def PatternListValue(self,num : int) -> StepVisual_CurveStyleFontPattern: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPatternList(self,aPatternList : StepVisual_HArray1OfCurveStyleFontPattern) -> None: 
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
class StepVisual_CurveStyleFontPattern(OCP.Standard.Standard_Transient):
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
    def Init(self,aVisibleSegmentLength : float,aInvisibleSegmentLength : float) -> None: 
        """
        None
        """
    def InvisibleSegmentLength(self) -> float: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetInvisibleSegmentLength(self,aInvisibleSegmentLength : float) -> None: 
        """
        None
        """
    def SetVisibleSegmentLength(self,aVisibleSegmentLength : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def VisibleSegmentLength(self) -> float: 
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
class StepVisual_CurveStyleFontSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a CurveStyleFontSelect Kind Entity that is : 1 -> CurveStyleFont 2 -> PreDefinedCurveFont 3 -> ExternallyDefinedCurveFont 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CurveStyleFont(self) -> StepVisual_CurveStyleFont: 
        """
        returns Value as a CurveStyleFont (Null if another type)
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ExternallyDefinedCurveFont(self) -> StepVisual_ExternallyDefinedCurveFont: 
        """
        returns Value as a ExternallyDefinedCurveFont (Null if another type)
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
    def PreDefinedCurveFont(self) -> StepVisual_PreDefinedCurveFont: 
        """
        returns Value as a PreDefinedCurveFont (Null if another type)
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
class StepVisual_DirectionCountSelect():
    """
    None
    """
    def SetTypeOfContent(self,aTypeOfContent : int) -> None: 
        """
        None
        """
    def SetUDirectionCount(self,aUDirectionCount : int) -> None: 
        """
        None
        """
    def SetVDirectionCount(self,aUDirectionCount : int) -> None: 
        """
        None
        """
    def TypeOfContent(self) -> int: 
        """
        None
        """
    def UDirectionCount(self) -> int: 
        """
        None
        """
    def VDirectionCount(self) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class StepVisual_DraughtingAnnotationOccurrence(StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_DraughtingCallout(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Contents(self) -> StepVisual_HArray1OfDraughtingCalloutElement: 
        """
        Returns field Contents
        """
    def ContentsValue(self,theNum : int) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns Contents with the given number
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theContents : StepVisual_HArray1OfDraughtingCalloutElement) -> None: 
        """
        Init
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
    def NbContents(self) -> int: 
        """
        Returns number of Contents
        """
    def SetContents(self,theContents : StepVisual_HArray1OfDraughtingCalloutElement) -> None: 
        """
        Set field Contents
        """
    def SetContentsValue(self,theNum : int,theItem : StepVisual_DraughtingCalloutElement) -> None: 
        """
        Sets Contents with given number
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
class StepVisual_DraughtingCalloutElement(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AnnotationCurveOccurrence(self) -> StepVisual_AnnotationCurveOccurrence: 
        """
        returns Value as a AnnotationCurveOccurrence (Null if another type)
        """
    def AnnotationFillAreaOccurrence(self) -> StepVisual_AnnotationFillAreaOccurrence: 
        """
        returns Value as a AnnotationFillAreaOccurrence
        """
    def AnnotationTextOccurrence(self) -> StepVisual_AnnotationTextOccurrence: 
        """
        returns Value as a AnnotationTextOccurrence
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
        Recognizes a IdAttributeSelect Kind Entity that is : 1 -> AnnotationCurveOccurrence 2 -> AnnotationTextOccurrence 3 -> TessellatedAnnotationOccurrence 4 -> AnnotationFillAreaOccurrence 0 else
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
    def TessellatedAnnotationOccurrence(self) -> StepVisual_TessellatedAnnotationOccurrence: 
        """
        returns Value as a TessellatedAnnotationOccurrence
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
class StepVisual_CharacterizedObjectAndCharacterizedRepresentationAndDraughtingModelAndRepresentation(StepVisual_DraughtingModel, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional Tolerances Complex STEP entity Characterized_Object & Characterized_Representation & Draughting_Model & RepresentationAdded for Dimensional Tolerances Complex STEP entity Characterized_Object & Characterized_Representation & Draughting_Model & RepresentationAdded for Dimensional Tolerances Complex STEP entity Characterized_Object & Characterized_Representation & Draughting_Model & Representation
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PreDefinedColour(StepVisual_Colour, OCP.Standard.Standard_Transient):
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
    def GetPreDefinedItem(self) -> StepVisual_PreDefinedItem: 
        """
        return a pre_defined_item part
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetPreDefinedItem(self,item : StepVisual_PreDefinedItem) -> None: 
        """
        set a pre_defined_item part
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
class StepVisual_PreDefinedItem(OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_ExternallyDefinedCurveFont(OCP.StepBasic.StepBasic_ExternallyDefinedItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternallyDefinedCurveFontRepresentation of STEP entity ExternallyDefinedCurveFontRepresentation of STEP entity ExternallyDefinedCurveFont
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
    def Init(self,aItemId : OCP.StepBasic.StepBasic_SourceItem,aSource : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ItemId(self) -> OCP.StepBasic.StepBasic_SourceItem: 
        """
        Returns field ItemId
        """
    def SetItemId(self,ItemId : OCP.StepBasic.StepBasic_SourceItem) -> None: 
        """
        Set field ItemId
        """
    def SetSource(self,Source : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> OCP.StepBasic.StepBasic_ExternalSource: 
        """
        Returns field Source
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
class StepVisual_ExternallyDefinedTextFont(OCP.StepBasic.StepBasic_ExternallyDefinedItem, OCP.Standard.Standard_Transient):
    """
    Representation of STEP entity ExternallyDefinedTextFontRepresentation of STEP entity ExternallyDefinedTextFontRepresentation of STEP entity ExternallyDefinedTextFont
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
    def Init(self,aItemId : OCP.StepBasic.StepBasic_SourceItem,aSource : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Initialize all fields (own and inherited)
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ItemId(self) -> OCP.StepBasic.StepBasic_SourceItem: 
        """
        Returns field ItemId
        """
    def SetItemId(self,ItemId : OCP.StepBasic.StepBasic_SourceItem) -> None: 
        """
        Set field ItemId
        """
    def SetSource(self,Source : OCP.StepBasic.StepBasic_ExternalSource) -> None: 
        """
        Set field Source
        """
    def Source(self) -> OCP.StepBasic.StepBasic_ExternalSource: 
        """
        Returns field Source
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
class StepVisual_FillAreaStyle(OCP.Standard.Standard_Transient):
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
    def FillStyles(self) -> StepVisual_HArray1OfFillStyleSelect: 
        """
        None
        """
    def FillStylesValue(self,num : int) -> StepVisual_FillStyleSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFillStyles : StepVisual_HArray1OfFillStyleSelect) -> None: 
        """
        None
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
    def NbFillStyles(self) -> int: 
        """
        None
        """
    def SetFillStyles(self,aFillStyles : StepVisual_HArray1OfFillStyleSelect) -> None: 
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
class StepVisual_FillAreaStyleColour(OCP.Standard.Standard_Transient):
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
    def FillColour(self) -> StepVisual_Colour: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aFillColour : StepVisual_Colour) -> None: 
        """
        None
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
    def SetFillColour(self,aFillColour : StepVisual_Colour) -> None: 
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
class StepVisual_FillStyleSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a FillStyleSelect Kind Entity that is : 1 -> FillAreaStyleColour 2 -> ExternallyDefinedTileStyle 3 -> FillAreaStyleTiles 4 -> ExternallyDefinedHatchStyle 5 -> FillAreaStyleHatching 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def FillAreaStyleColour(self) -> StepVisual_FillAreaStyleColour: 
        """
        returns Value as a FillAreaStyleColour (Null if another type)
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
class StepVisual_FontSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a FontSelect Kind Entity that is : 1 -> PreDefinedTextFont 2 -> ExternallyDefinedTextFont 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def ExternallyDefinedTextFont(self) -> StepVisual_ExternallyDefinedTextFont: 
        """
        returns Value as a ExternallyDefinedTextFont (Null if another type)
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
    def PreDefinedTextFont(self) -> StepVisual_PreDefinedTextFont: 
        """
        returns Value as a PreDefinedTextFont (Null if another type)
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
class StepVisual_HArray1OfAnnotationPlaneElement(StepVisual_Array1OfAnnotationPlaneElement, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_AnnotationPlaneElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_AnnotationPlaneElement: 
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
    def First(self) -> StepVisual_AnnotationPlaneElement: 
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
    def Init(self,theValue : StepVisual_AnnotationPlaneElement) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_AnnotationPlaneElement: 
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
    def Move(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> StepVisual_Array1OfAnnotationPlaneElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_AnnotationPlaneElement) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_AnnotationPlaneElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfAnnotationPlaneElement) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_AnnotationPlaneElement) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfBoxCharacteristicSelect(StepVisual_Array1OfBoxCharacteristicSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_BoxCharacteristicSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_BoxCharacteristicSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_BoxCharacteristicSelect: 
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
    def First(self) -> StepVisual_BoxCharacteristicSelect: 
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
    def Init(self,theValue : StepVisual_BoxCharacteristicSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_BoxCharacteristicSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> StepVisual_Array1OfBoxCharacteristicSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_BoxCharacteristicSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_BoxCharacteristicSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_BoxCharacteristicSelect) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfBoxCharacteristicSelect) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect(StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
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
    def First(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
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
    def Init(self,theValue : StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingInterectionSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect(StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
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
    def First(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
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
    def Init(self,theValue : StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CameraModelD3MultiClippingUnionSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfCurveStyleFontPattern(StepVisual_Array1OfCurveStyleFontPattern, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_CurveStyleFontPattern: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_CurveStyleFontPattern: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_CurveStyleFontPattern: 
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
    def First(self) -> StepVisual_CurveStyleFontPattern: 
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
    def Init(self,theValue : StepVisual_CurveStyleFontPattern) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_CurveStyleFontPattern: 
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
    def Move(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> StepVisual_Array1OfCurveStyleFontPattern: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_CurveStyleFontPattern) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_CurveStyleFontPattern: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfCurveStyleFontPattern) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_CurveStyleFontPattern) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfDirectionCountSelect(StepVisual_Array1OfDirectionCountSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_DirectionCountSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_DirectionCountSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_DirectionCountSelect: 
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
    def First(self) -> StepVisual_DirectionCountSelect: 
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
    def Init(self,theValue : StepVisual_DirectionCountSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_DirectionCountSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> StepVisual_Array1OfDirectionCountSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_DirectionCountSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_DirectionCountSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfDirectionCountSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_DirectionCountSelect) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfDraughtingCalloutElement(StepVisual_Array1OfDraughtingCalloutElement, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_DraughtingCalloutElement: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_DraughtingCalloutElement: 
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
    def First(self) -> StepVisual_DraughtingCalloutElement: 
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
    def Init(self,theValue : StepVisual_DraughtingCalloutElement) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_DraughtingCalloutElement: 
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
    def Move(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> StepVisual_Array1OfDraughtingCalloutElement: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_DraughtingCalloutElement) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_DraughtingCalloutElement: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : StepVisual_Array1OfDraughtingCalloutElement) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_DraughtingCalloutElement) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfFillStyleSelect(StepVisual_Array1OfFillStyleSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfFillStyleSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfFillStyleSelect) -> StepVisual_Array1OfFillStyleSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfFillStyleSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_FillStyleSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_FillStyleSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_FillStyleSelect: 
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
    def First(self) -> StepVisual_FillStyleSelect: 
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
    def Init(self,theValue : StepVisual_FillStyleSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_FillStyleSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfFillStyleSelect) -> StepVisual_Array1OfFillStyleSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_FillStyleSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_FillStyleSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfFillStyleSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_FillStyleSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfInvisibleItem(StepVisual_Array1OfInvisibleItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfInvisibleItem: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfInvisibleItem) -> StepVisual_Array1OfInvisibleItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfInvisibleItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_InvisibleItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_InvisibleItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_InvisibleItem: 
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
    def First(self) -> StepVisual_InvisibleItem: 
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
    def Init(self,theValue : StepVisual_InvisibleItem) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_InvisibleItem: 
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
    def Move(self,theOther : StepVisual_Array1OfInvisibleItem) -> StepVisual_Array1OfInvisibleItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_InvisibleItem) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_InvisibleItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_InvisibleItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfInvisibleItem) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfLayeredItem(StepVisual_Array1OfLayeredItem, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfLayeredItem: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfLayeredItem) -> StepVisual_Array1OfLayeredItem: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfLayeredItem: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_LayeredItem: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_LayeredItem: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_LayeredItem: 
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
    def First(self) -> StepVisual_LayeredItem: 
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
    def Init(self,theValue : StepVisual_LayeredItem) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_LayeredItem: 
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
    def Move(self,theOther : StepVisual_Array1OfLayeredItem) -> StepVisual_Array1OfLayeredItem: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_LayeredItem) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_LayeredItem: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_LayeredItem) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfLayeredItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfPresentationStyleAssignment(StepVisual_Array1OfPresentationStyleAssignment, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_PresentationStyleAssignment: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_PresentationStyleAssignment: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_PresentationStyleAssignment: 
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
    def First(self) -> StepVisual_PresentationStyleAssignment: 
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
    def Init(self,theValue : StepVisual_PresentationStyleAssignment) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_PresentationStyleAssignment: 
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
    def Move(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> StepVisual_Array1OfPresentationStyleAssignment: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_PresentationStyleAssignment) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_PresentationStyleAssignment: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfPresentationStyleAssignment) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_PresentationStyleAssignment) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfPresentationStyleSelect(StepVisual_Array1OfPresentationStyleSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_PresentationStyleSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_PresentationStyleSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_PresentationStyleSelect: 
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
    def First(self) -> StepVisual_PresentationStyleSelect: 
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
    def Init(self,theValue : StepVisual_PresentationStyleSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_PresentationStyleSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> StepVisual_Array1OfPresentationStyleSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_PresentationStyleSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_PresentationStyleSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_PresentationStyleSelect) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfPresentationStyleSelect) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfStyleContextSelect(StepVisual_Array1OfStyleContextSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfStyleContextSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfStyleContextSelect) -> StepVisual_Array1OfStyleContextSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfStyleContextSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_StyleContextSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_StyleContextSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_StyleContextSelect: 
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
    def First(self) -> StepVisual_StyleContextSelect: 
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
    def Init(self,theValue : StepVisual_StyleContextSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_StyleContextSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfStyleContextSelect) -> StepVisual_Array1OfStyleContextSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_StyleContextSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_StyleContextSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_StyleContextSelect) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfStyleContextSelect) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfSurfaceStyleElementSelect(StepVisual_Array1OfSurfaceStyleElementSelect, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_SurfaceStyleElementSelect: 
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
    def First(self) -> StepVisual_SurfaceStyleElementSelect: 
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
    def Init(self,theValue : StepVisual_SurfaceStyleElementSelect) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_SurfaceStyleElementSelect: 
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
    def Move(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> StepVisual_Array1OfSurfaceStyleElementSelect: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_SurfaceStyleElementSelect) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_SurfaceStyleElementSelect: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_SurfaceStyleElementSelect) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfSurfaceStyleElementSelect) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_HArray1OfTextOrCharacter(StepVisual_Array1OfTextOrCharacter, OCP.Standard.Standard_Transient):
    def Array1(self) -> StepVisual_Array1OfTextOrCharacter: 
        """
        None
        """
    def Assign(self,theOther : StepVisual_Array1OfTextOrCharacter) -> StepVisual_Array1OfTextOrCharacter: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> StepVisual_Array1OfTextOrCharacter: 
        """
        None
        """
    def ChangeFirst(self) -> StepVisual_TextOrCharacter: 
        """
        Returns first element
        """
    def ChangeLast(self) -> StepVisual_TextOrCharacter: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> StepVisual_TextOrCharacter: 
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
    def First(self) -> StepVisual_TextOrCharacter: 
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
    def Init(self,theValue : StepVisual_TextOrCharacter) -> None: 
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Last(self) -> StepVisual_TextOrCharacter: 
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
    def Move(self,theOther : StepVisual_Array1OfTextOrCharacter) -> StepVisual_Array1OfTextOrCharacter: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : StepVisual_TextOrCharacter) -> None: 
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
    def Value(self,theIndex : int) -> StepVisual_TextOrCharacter: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : StepVisual_TextOrCharacter) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_Array1OfTextOrCharacter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
class StepVisual_ContextDependentInvisibility(StepVisual_Invisibility, OCP.Standard.Standard_Transient):
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
    def Init(self,aInvisibleItems : StepVisual_HArray1OfInvisibleItem,aPresentationContext : StepVisual_InvisibilityContext) -> None: 
        """
        None
        """
    def InvisibleItems(self) -> StepVisual_HArray1OfInvisibleItem: 
        """
        None
        """
    def InvisibleItemsValue(self,num : int) -> StepVisual_InvisibleItem: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbInvisibleItems(self) -> int: 
        """
        None
        """
    def PresentationContext(self) -> StepVisual_InvisibilityContext: 
        """
        None
        """
    def SetInvisibleItems(self,aInvisibleItems : StepVisual_HArray1OfInvisibleItem) -> None: 
        """
        None
        """
    def SetPresentationContext(self,aPresentationContext : StepVisual_InvisibilityContext) -> None: 
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
class StepVisual_InvisibilityContext(OCP.StepData.StepData_SelectType):
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
        Recognizes a InvisibilityContext Kind Entity that is : 1 -> PresentationRepresentation 2 -> PresentationSet 2 -> DraughtingModel 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def DraughtingModel(self) -> StepVisual_DraughtingModel: 
        """
        returns Value as a PresentationSet (Null if another type)
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
    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: 
        """
        returns Value as a PresentationRepresentation (Null if another type)
        """
    def PresentationSet(self) -> StepVisual_PresentationSet: 
        """
        returns Value as a PresentationSet (Null if another type)
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
class StepVisual_InvisibleItem(OCP.StepData.StepData_SelectType):
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
        Recognizes a InvisibleItem Kind Entity that is : 1 -> StyledItem 2 -> PresentationLayerAssignment 3 -> PresentationRepresentation 0 else
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
    def PresentationLayerAssignment(self) -> StepVisual_PresentationLayerAssignment: 
        """
        returns Value as a PresentationLayerAssignment (Null if another type)
        """
    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: 
        """
        returns Value as a PresentationRepresentation (Null if another type)
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
    def StyledItem(self) -> StepVisual_StyledItem: 
        """
        returns Value as a StyledItem (Null if another type)
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
class StepVisual_LayeredItem(OCP.StepData.StepData_SelectType):
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
        Recognizes a LayeredItem Kind Entity that is : 1 -> PresentationRepresentation 2 -> RepresentationItem 0 else
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
    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: 
        """
        returns Value as a PresentationRepresentation (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        returns Value as a RepresentationItem (Null if another type)
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
class StepVisual_MarkerMember(OCP.StepData.StepData_SelectInt, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Defines MarkerType as unique member of MarkerSelect Works with an EnumToolDefines MarkerType as unique member of MarkerSelect Works with an EnumToolDefines MarkerType as unique member of MarkerSelect Works with an EnumTool
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        None
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,val : int,text : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        None
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,name : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def SetValue(self,val : StepVisual_MarkerType) -> None: 
        """
        None
        """
    def String(self) -> str: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> StepVisual_MarkerType: 
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
class StepVisual_MarkerSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def Boolean(self) -> bool: 
        """
        None
        """
    def CaseMem(self,sm : OCP.StepData.StepData_SelectMember) -> int: 
        """
        Returns 1 for a SelectMember enum, named MARKER_TYPE
        """
    def CaseMember(self) -> int: 
        """
        Returns the Type of the stored SelectMember, or zero if it is Null or Entity. Calls the method CaseMem on Value
        """
    def CaseNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Recognizes a MarkerSelect Kind Entity that is : 0 else
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
    def MarkerMember(self) -> StepVisual_MarkerMember: 
        """
        Gives access to the MarkerMember in order to get/set its value
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
        Returns a new MarkerMember
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
class StepVisual_MarkerType():
    """
    None

    Members:

      StepVisual_mtDot

      StepVisual_mtX

      StepVisual_mtPlus

      StepVisual_mtAsterisk

      StepVisual_mtRing

      StepVisual_mtSquare

      StepVisual_mtTriangle
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepVisual_mtAsterisk: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtAsterisk
    StepVisual_mtDot: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtDot
    StepVisual_mtPlus: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtPlus
    StepVisual_mtRing: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtRing
    StepVisual_mtSquare: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtSquare
    StepVisual_mtTriangle: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtTriangle
    StepVisual_mtX: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtX
    __entries: dict # value = {'StepVisual_mtDot': (StepVisual_MarkerType.StepVisual_mtDot, None), 'StepVisual_mtX': (StepVisual_MarkerType.StepVisual_mtX, None), 'StepVisual_mtPlus': (StepVisual_MarkerType.StepVisual_mtPlus, None), 'StepVisual_mtAsterisk': (StepVisual_MarkerType.StepVisual_mtAsterisk, None), 'StepVisual_mtRing': (StepVisual_MarkerType.StepVisual_mtRing, None), 'StepVisual_mtSquare': (StepVisual_MarkerType.StepVisual_mtSquare, None), 'StepVisual_mtTriangle': (StepVisual_MarkerType.StepVisual_mtTriangle, None)}
    __members__: dict # value = {'StepVisual_mtDot': StepVisual_MarkerType.StepVisual_mtDot, 'StepVisual_mtX': StepVisual_MarkerType.StepVisual_mtX, 'StepVisual_mtPlus': StepVisual_MarkerType.StepVisual_mtPlus, 'StepVisual_mtAsterisk': StepVisual_MarkerType.StepVisual_mtAsterisk, 'StepVisual_mtRing': StepVisual_MarkerType.StepVisual_mtRing, 'StepVisual_mtSquare': StepVisual_MarkerType.StepVisual_mtSquare, 'StepVisual_mtTriangle': StepVisual_MarkerType.StepVisual_mtTriangle}
    pass
class StepVisual_PresentationRepresentation(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_MechanicalDesignGeometricPresentationRepresentation(StepVisual_PresentationRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_NullStyle():
    """
    None

    Members:

      StepVisual_Null
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepVisual_Null: OCP.StepVisual.StepVisual_NullStyle # value = StepVisual_NullStyle.StepVisual_Null
    __entries: dict # value = {'StepVisual_Null': (StepVisual_NullStyle.StepVisual_Null, None)}
    __members__: dict # value = {'StepVisual_Null': StepVisual_NullStyle.StepVisual_Null}
    pass
class StepVisual_NullStyleMember(OCP.StepData.StepData_SelectInt, OCP.StepData.StepData_SelectMember, OCP.Standard.Standard_Transient):
    """
    Defines NullStyle as unique member of PresentationStyleSelect Works with an EnumToolDefines NullStyle as unique member of PresentationStyleSelect Works with an EnumToolDefines NullStyle as unique member of PresentationStyleSelect Works with an EnumTool
    """
    def Boolean(self) -> bool: 
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
    def Enum(self) -> int: 
        """
        None
        """
    def EnumText(self) -> str: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasName(self) -> bool: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Int(self) -> int: 
        """
        None
        """
    def Integer(self) -> int: 
        """
        Gets the value as an Integer
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Kind(self) -> int: 
        """
        None
        """
    def Logical(self) -> OCP.StepData.StepData_Logical: 
        """
        None
        """
    def Matches(self,name : str) -> bool: 
        """
        Tells if the name of a SelectMember matches a given one By default, compares the strings, can be redefined (optimised)
        """
    def Name(self) -> str: 
        """
        None
        """
    def ParamType(self) -> OCP.Interface.Interface_ParamType: 
        """
        Returns the Kind of the SelectMember, under the form of an enum ParamType
        """
    def Real(self) -> float: 
        """
        None
        """
    def SetBoolean(self,val : bool) -> None: 
        """
        None
        """
    def SetEnum(self,val : int,text : str='') -> None: 
        """
        None
        """
    def SetEnumText(self,theValue : int,theText : str) -> None: 
        """
        None
        """
    def SetInt(self,val : int) -> None: 
        """
        None
        """
    def SetInteger(self,val : int) -> None: 
        """
        None
        """
    def SetKind(self,kind : int) -> None: 
        """
        None
        """
    def SetLogical(self,val : OCP.StepData.StepData_Logical) -> None: 
        """
        None
        """
    def SetName(self,arg1 : str) -> bool: 
        """
        None
        """
    def SetReal(self,val : float) -> None: 
        """
        None
        """
    def SetString(self,val : str) -> None: 
        """
        None
        """
    def SetValue(self,theValue : StepVisual_NullStyle) -> None: 
        """
        None
        """
    def String(self) -> str: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> StepVisual_NullStyle: 
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
class StepVisual_ContextDependentOverRidingStyledItem(StepVisual_OverRidingStyledItem, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient,aOverRiddenStyle : StepVisual_StyledItem,aStyleContext : StepVisual_HArray1OfStyleContextSelect) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyleContext(self) -> int: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    def OverRiddenStyle(self) -> StepVisual_StyledItem: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetOverRiddenStyle(self,aOverRiddenStyle : StepVisual_StyledItem) -> None: 
        """
        None
        """
    def SetStyleContext(self,aStyleContext : StepVisual_HArray1OfStyleContextSelect) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def StyleContext(self) -> StepVisual_HArray1OfStyleContextSelect: 
        """
        None
        """
    def StyleContextValue(self,num : int) -> StepVisual_StyleContextSelect: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_PlanarExtent(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSizeInX : float,aSizeInY : float) -> None: 
        """
        None
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
    def SetSizeInX(self,aSizeInX : float) -> None: 
        """
        None
        """
    def SetSizeInY(self,aSizeInY : float) -> None: 
        """
        None
        """
    def SizeInX(self) -> float: 
        """
        None
        """
    def SizeInY(self) -> float: 
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
class StepVisual_PlanarBox(StepVisual_PlanarExtent, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aSizeInX : float,aSizeInY : float,aPlacement : OCP.StepGeom.StepGeom_Axis2Placement) -> None: 
        """
        None
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
    def Placement(self) -> OCP.StepGeom.StepGeom_Axis2Placement: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPlacement(self,aPlacement : OCP.StepGeom.StepGeom_Axis2Placement) -> None: 
        """
        None
        """
    def SetSizeInX(self,aSizeInX : float) -> None: 
        """
        None
        """
    def SetSizeInY(self,aSizeInY : float) -> None: 
        """
        None
        """
    def SizeInX(self) -> float: 
        """
        None
        """
    def SizeInY(self) -> float: 
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
class StepVisual_PointStyle(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMarker : StepVisual_MarkerSelect,aMarkerSize : OCP.StepBasic.StepBasic_SizeSelect,aMarkerColour : StepVisual_Colour) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Marker(self) -> StepVisual_MarkerSelect: 
        """
        None
        """
    def MarkerColour(self) -> StepVisual_Colour: 
        """
        None
        """
    def MarkerSize(self) -> OCP.StepBasic.StepBasic_SizeSelect: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMarker(self,aMarker : StepVisual_MarkerSelect) -> None: 
        """
        None
        """
    def SetMarkerColour(self,aMarkerColour : StepVisual_Colour) -> None: 
        """
        None
        """
    def SetMarkerSize(self,aMarkerSize : OCP.StepBasic.StepBasic_SizeSelect) -> None: 
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
class StepVisual_DraughtingPreDefinedColour(StepVisual_PreDefinedColour, StepVisual_Colour, OCP.Standard.Standard_Transient):
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
    def GetPreDefinedItem(self) -> StepVisual_PreDefinedItem: 
        """
        return a pre_defined_item part
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetPreDefinedItem(self,item : StepVisual_PreDefinedItem) -> None: 
        """
        set a pre_defined_item part
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
class StepVisual_PreDefinedCurveFont(StepVisual_PreDefinedItem, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_DraughtingPreDefinedCurveFont(StepVisual_PreDefinedCurveFont, StepVisual_PreDefinedItem, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PreDefinedTextFont(StepVisual_PreDefinedItem, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PresentationArea(StepVisual_PresentationRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PresentationLayerAssignment(OCP.Standard.Standard_Transient):
    def AssignedItems(self) -> StepVisual_HArray1OfLayeredItem: 
        """
        None
        """
    def AssignedItemsValue(self,num : int) -> StepVisual_LayeredItem: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aDescription : OCP.TCollection.TCollection_HAsciiString,aAssignedItems : StepVisual_HArray1OfLayeredItem) -> None: 
        """
        None
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
    def NbAssignedItems(self) -> int: 
        """
        None
        """
    def SetAssignedItems(self,aAssignedItems : StepVisual_HArray1OfLayeredItem) -> None: 
        """
        None
        """
    def SetDescription(self,aDescription : OCP.TCollection.TCollection_HAsciiString) -> None: 
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
class StepVisual_PresentationLayerUsage(OCP.Standard.Standard_Transient):
    """
    Added from StepVisual Rev2 to Rev4Added from StepVisual Rev2 to Rev4Added from StepVisual Rev2 to Rev4
    """
    def Assignment(self) -> StepVisual_PresentationLayerAssignment: 
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
    def Init(self,aAssignment : StepVisual_PresentationLayerAssignment,aPresentation : StepVisual_PresentationRepresentation) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Presentation(self) -> StepVisual_PresentationRepresentation: 
        """
        None
        """
    def SetAssignment(self,aAssignment : StepVisual_PresentationLayerAssignment) -> None: 
        """
        None
        """
    def SetPresentation(self,aPresentation : StepVisual_PresentationRepresentation) -> None: 
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
class StepVisual_MechanicalDesignGeometricPresentationArea(StepVisual_PresentationArea, StepVisual_PresentationRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PresentationRepresentationSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a PresentationRepresentationSelect Kind Entity that is : 1 -> PresentationRepresentation 2 -> PresentationSet 0 else
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
    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation: 
        """
        returns Value as a PresentationRepresentation (Null if another type)
        """
    def PresentationSet(self) -> StepVisual_PresentationSet: 
        """
        returns Value as a PresentationSet (Null if another type)
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
class StepVisual_PresentationSet(OCP.Standard.Standard_Transient):
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
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
class StepVisual_PresentationSize(OCP.Standard.Standard_Transient):
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
    def Init(self,aUnit : StepVisual_PresentationSizeAssignmentSelect,aSize : StepVisual_PlanarBox) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetSize(self,aSize : StepVisual_PlanarBox) -> None: 
        """
        None
        """
    def SetUnit(self,aUnit : StepVisual_PresentationSizeAssignmentSelect) -> None: 
        """
        None
        """
    def Size(self) -> StepVisual_PlanarBox: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unit(self) -> StepVisual_PresentationSizeAssignmentSelect: 
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
class StepVisual_PresentationSizeAssignmentSelect(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AreaInSet(self) -> StepVisual_AreaInSet: 
        """
        returns Value as a AreaInSet (Null if another type)
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
        Recognizes a PresentationSizeAssignmentSelect Kind Entity that is : 1 -> PresentationView 2 -> PresentationArea 3 -> AreaInSet 0 else
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
    def PresentationArea(self) -> StepVisual_PresentationArea: 
        """
        returns Value as a PresentationArea (Null if another type)
        """
    def PresentationView(self) -> StepVisual_PresentationView: 
        """
        returns Value as a PresentationView (Null if another type)
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
class StepVisual_PresentationStyleAssignment(OCP.Standard.Standard_Transient):
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
    def Init(self,aStyles : StepVisual_HArray1OfPresentationStyleSelect) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbStyles(self) -> int: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleSelect) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleSelect: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleSelect: 
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
class StepVisual_PresentationStyleByContext(StepVisual_PresentationStyleAssignment, OCP.Standard.Standard_Transient):
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
    def Init(self,aStyles : StepVisual_HArray1OfPresentationStyleSelect,aStyleContext : StepVisual_StyleContextSelect) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbStyles(self) -> int: 
        """
        None
        """
    def SetStyleContext(self,aStyleContext : StepVisual_StyleContextSelect) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleSelect) -> None: 
        """
        None
        """
    def StyleContext(self) -> StepVisual_StyleContextSelect: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleSelect: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleSelect: 
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
class StepVisual_PresentationStyleSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a PresentationStyleSelect Kind Entity that is : 1 -> PointStyle 2 -> CurveStyle 3 -> SurfaceStyleUsage 4 -> SymbolStyle 5 -> FillAreaStyle 6 -> TextStyle 7 -> NullStyle 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CurveStyle(self) -> StepVisual_CurveStyle: 
        """
        returns Value as a CurveStyle (Null if another type)
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
    def NullStyle(self) -> StepVisual_NullStyleMember: 
        """
        returns Value as a NullStyleMember (Null if another type)
        """
    def Nullify(self) -> None: 
        """
        Nullifies the Stored Entity
        """
    def PointStyle(self) -> StepVisual_PointStyle: 
        """
        returns Value as a PointStyle (Null if another type)
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
    def SurfaceStyleUsage(self) -> StepVisual_SurfaceStyleUsage: 
        """
        returns Value as a SurfaceStyleUsage (Null if another type)
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
class StepVisual_PresentationView(StepVisual_PresentationRepresentation, OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_PresentedItem(OCP.Standard.Standard_Transient):
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
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
class StepVisual_PresentedItemRepresentation(OCP.Standard.Standard_Transient):
    """
    Added from StepVisual Rev2 to Rev4Added from StepVisual Rev2 to Rev4Added from StepVisual Rev2 to Rev4
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
    def Init(self,aPresentation : StepVisual_PresentationRepresentationSelect,aItem : StepVisual_PresentedItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> StepVisual_PresentedItem: 
        """
        None
        """
    def Presentation(self) -> StepVisual_PresentationRepresentationSelect: 
        """
        None
        """
    def SetItem(self,aItem : StepVisual_PresentedItem) -> None: 
        """
        None
        """
    def SetPresentation(self,aPresentation : StepVisual_PresentationRepresentationSelect) -> None: 
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
class StepVisual_StyleContextSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a StyleContextSelect Kind Entity that is : 1 -> Representation 2 -> RepresentationItem 3 -> PresentationSet 0 else
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
    def PresentationSet(self) -> StepVisual_PresentationSet: 
        """
        returns Value as a PresentationSet (Null if another type)
        """
    def Real(self) -> float: 
        """
        None
        """
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        returns Value as a Representation (Null if another type)
        """
    def RepresentationItem(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        returns Value as a RepresentationItem (Null if another type)
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
class StepVisual_AnnotationCurveOccurrenceAndAnnotationOccurrenceAndGeomReprItemAndReprItemAndStyledItem(StepVisual_AnnotationCurveOccurrence, StepVisual_AnnotationOccurrence, StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    """
    Added for Dimensional Tolerances Complex STEP entity AnnotationCurveOccurrence & AnnotationOccurrence & GeometricRepresentationItem & RepresentationItem & StyledItemAdded for Dimensional Tolerances Complex STEP entity AnnotationCurveOccurrence & AnnotationOccurrence & GeometricRepresentationItem & RepresentationItem & StyledItemAdded for Dimensional Tolerances Complex STEP entity AnnotationCurveOccurrence & AnnotationOccurrence & GeometricRepresentationItem & RepresentationItem & StyledItem
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_StyledItemTarget(OCP.StepData.StepData_SelectType):
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
        Recognizes a StyledItemTarget Kind Entity that is : 1 -> GeometricRepresentationItem 2 -> MappedItem 3 -> Representation 4 -> TopologicalRepresentationItem 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def Description(self) -> OCP.StepData.StepData_PDescr: 
        """
        Returns the Description which corresponds to <me> Null if no specific description to give. This description is used to control reading an check validity. Default returns a Null Handle, i.e. undefined description It can suffice if CaseNum and CaseMem give enough control
        """
    def GeometricRepresentationItem(self) -> OCP.StepGeom.StepGeom_GeometricRepresentationItem: 
        """
        returns Value as a GeometricRepresentationItem (Null if another type)
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
    def MappedItem(self) -> OCP.StepRepr.StepRepr_MappedItem: 
        """
        returns Value as a MappedItem (Null if another type)
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
    def Representation(self) -> OCP.StepRepr.StepRepr_Representation: 
        """
        returns Value as a Representation (Null if another type)
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
    def TopologicalRepresentationItem(self) -> OCP.StepShape.StepShape_TopologicalRepresentationItem: 
        """
        returns Value as a TopologicalRepresentationItem (Null if another type)
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
class StepVisual_SurfaceSide():
    """
    None

    Members:

      StepVisual_ssNegative

      StepVisual_ssPositive

      StepVisual_ssBoth
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepVisual_ssBoth: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssBoth
    StepVisual_ssNegative: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssNegative
    StepVisual_ssPositive: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssPositive
    __entries: dict # value = {'StepVisual_ssNegative': (StepVisual_SurfaceSide.StepVisual_ssNegative, None), 'StepVisual_ssPositive': (StepVisual_SurfaceSide.StepVisual_ssPositive, None), 'StepVisual_ssBoth': (StepVisual_SurfaceSide.StepVisual_ssBoth, None)}
    __members__: dict # value = {'StepVisual_ssNegative': StepVisual_SurfaceSide.StepVisual_ssNegative, 'StepVisual_ssPositive': StepVisual_SurfaceSide.StepVisual_ssPositive, 'StepVisual_ssBoth': StepVisual_SurfaceSide.StepVisual_ssBoth}
    pass
class StepVisual_SurfaceSideStyle(OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfSurfaceStyleElementSelect) -> None: 
        """
        None
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
    def NbStyles(self) -> int: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfSurfaceStyleElementSelect) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfSurfaceStyleElementSelect: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_SurfaceStyleElementSelect: 
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
class StepVisual_SurfaceStyleBoundary(OCP.Standard.Standard_Transient):
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
    def Init(self,aStyleOfBoundary : StepVisual_CurveStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetStyleOfBoundary(self,aStyleOfBoundary : StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def StyleOfBoundary(self) -> StepVisual_CurveStyle: 
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
class StepVisual_SurfaceStyleControlGrid(OCP.Standard.Standard_Transient):
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
    def Init(self,aStyleOfControlGrid : StepVisual_CurveStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetStyleOfControlGrid(self,aStyleOfControlGrid : StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def StyleOfControlGrid(self) -> StepVisual_CurveStyle: 
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
class StepVisual_SurfaceStyleElementSelect(OCP.StepData.StepData_SelectType):
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
        Recognizes a SurfaceStyleElementSelect Kind Entity that is : 1 -> SurfaceStyleFillArea 2 -> SurfaceStyleBoundary 3 -> SurfaceStyleParameterLine 4 -> SurfaceStyleSilhouette 5 -> SurfaceStyleSegmentationCurve 6 -> SurfaceStyleControlGrid 0 else
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
    def SurfaceStyleBoundary(self) -> StepVisual_SurfaceStyleBoundary: 
        """
        returns Value as a SurfaceStyleBoundary (Null if another type)
        """
    def SurfaceStyleFillArea(self) -> StepVisual_SurfaceStyleFillArea: 
        """
        returns Value as a SurfaceStyleFillArea (Null if another type)
        """
    def SurfaceStyleParameterLine(self) -> StepVisual_SurfaceStyleParameterLine: 
        """
        returns Value as a SurfaceStyleParameterLine (Null if another type)
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
class StepVisual_SurfaceStyleFillArea(OCP.Standard.Standard_Transient):
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
    def FillArea(self) -> StepVisual_FillAreaStyle: 
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
    def Init(self,aFillArea : StepVisual_FillAreaStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetFillArea(self,aFillArea : StepVisual_FillAreaStyle) -> None: 
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
class StepVisual_SurfaceStyleParameterLine(OCP.Standard.Standard_Transient):
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DirectionCounts(self) -> StepVisual_HArray1OfDirectionCountSelect: 
        """
        None
        """
    def DirectionCountsValue(self,num : int) -> StepVisual_DirectionCountSelect: 
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
    def Init(self,aStyleOfParameterLines : StepVisual_CurveStyle,aDirectionCounts : StepVisual_HArray1OfDirectionCountSelect) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def NbDirectionCounts(self) -> int: 
        """
        None
        """
    def SetDirectionCounts(self,aDirectionCounts : StepVisual_HArray1OfDirectionCountSelect) -> None: 
        """
        None
        """
    def SetStyleOfParameterLines(self,aStyleOfParameterLines : StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def StyleOfParameterLines(self) -> StepVisual_CurveStyle: 
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
class StepVisual_SurfaceStyleSegmentationCurve(OCP.Standard.Standard_Transient):
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
    def Init(self,aStyleOfSegmentationCurve : StepVisual_CurveStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetStyleOfSegmentationCurve(self,aStyleOfSegmentationCurve : StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def StyleOfSegmentationCurve(self) -> StepVisual_CurveStyle: 
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
class StepVisual_SurfaceStyleSilhouette(OCP.Standard.Standard_Transient):
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
    def Init(self,aStyleOfSilhouette : StepVisual_CurveStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetStyleOfSilhouette(self,aStyleOfSilhouette : StepVisual_CurveStyle) -> None: 
        """
        None
        """
    def StyleOfSilhouette(self) -> StepVisual_CurveStyle: 
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
class StepVisual_SurfaceStyleUsage(OCP.Standard.Standard_Transient):
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
    def Init(self,aSide : StepVisual_SurfaceSide,aStyle : StepVisual_SurfaceSideStyle) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetSide(self,aSide : StepVisual_SurfaceSide) -> None: 
        """
        None
        """
    def SetStyle(self,aStyle : StepVisual_SurfaceSideStyle) -> None: 
        """
        None
        """
    def Side(self) -> StepVisual_SurfaceSide: 
        """
        None
        """
    def Style(self) -> StepVisual_SurfaceSideStyle: 
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
class StepVisual_Template(OCP.StepRepr.StepRepr_Representation, OCP.Standard.Standard_Transient):
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
    def IsInstance(self,theTypeName : str) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: ...
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
class StepVisual_TemplateInstance(OCP.StepRepr.StepRepr_MappedItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def MappingSource(self) -> OCP.StepRepr.StepRepr_RepresentationMap: 
        """
        None
        """
    def MappingTarget(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def SetMappingSource(self,aMappingSource : OCP.StepRepr.StepRepr_RepresentationMap) -> None: 
        """
        None
        """
    def SetMappingTarget(self,aMappingTarget : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
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
class StepVisual_TessellatedAnnotationOccurrence(StepVisual_StyledItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aStyles : StepVisual_HArray1OfPresentationStyleAssignment,aItem : OCP.Standard.Standard_Transient) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Item(self) -> OCP.StepRepr.StepRepr_RepresentationItem: 
        """
        None
        """
    def ItemAP242(self) -> StepVisual_StyledItemTarget: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def NbStyles(self) -> int: 
        """
        None
        """
    @overload
    def SetItem(self,aItem : OCP.StepRepr.StepRepr_RepresentationItem) -> None: 
        """
        None

        None
        """
    @overload
    def SetItem(self,aItem : StepVisual_StyledItemTarget) -> None: ...
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetStyles(self,aStyles : StepVisual_HArray1OfPresentationStyleAssignment) -> None: 
        """
        None
        """
    def Styles(self) -> StepVisual_HArray1OfPresentationStyleAssignment: 
        """
        None
        """
    def StylesValue(self,num : int) -> StepVisual_PresentationStyleAssignment: 
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
class StepVisual_TessellatedCurveSet(StepVisual_TessellatedItem, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def CoordList(self) -> StepVisual_CoordinatesList: 
        """
        None
        """
    def Curves(self) -> Any: 
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theCoordList : StepVisual_CoordinatesList,theCurves : Any) -> None: 
        """
        None
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
class StepVisual_TessellatedGeometricSet(StepVisual_TessellatedItem, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,theItems : Any) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Items(self) -> Any: 
        """
        None
        """
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
class StepVisual_CoordinatesList(StepVisual_TessellatedItem, OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
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
    def Init(self,theName : OCP.TCollection.TCollection_HAsciiString,thePoints : OCP.TColgp.TColgp_HArray1OfXYZ) -> None: 
        """
        None
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
    def Points(self) -> OCP.TColgp.TColgp_HArray1OfXYZ: 
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
class StepVisual_TextLiteral(OCP.StepGeom.StepGeom_GeometricRepresentationItem, OCP.StepRepr.StepRepr_RepresentationItem, OCP.Standard.Standard_Transient):
    def Alignment(self) -> OCP.TCollection.TCollection_HAsciiString: 
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
    def Font(self) -> StepVisual_FontSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aLiteral : OCP.TCollection.TCollection_HAsciiString,aPlacement : OCP.StepGeom.StepGeom_Axis2Placement,aAlignment : OCP.TCollection.TCollection_HAsciiString,aPath : StepVisual_TextPath,aFont : StepVisual_FontSelect) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def Literal(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Name(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def Path(self) -> StepVisual_TextPath: 
        """
        None
        """
    def Placement(self) -> OCP.StepGeom.StepGeom_Axis2Placement: 
        """
        None
        """
    def SetAlignment(self,aAlignment : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetFont(self,aFont : StepVisual_FontSelect) -> None: 
        """
        None
        """
    def SetLiteral(self,aLiteral : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetName(self,aName : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        None
        """
    def SetPath(self,aPath : StepVisual_TextPath) -> None: 
        """
        None
        """
    def SetPlacement(self,aPlacement : OCP.StepGeom.StepGeom_Axis2Placement) -> None: 
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
class StepVisual_TextOrCharacter(OCP.StepData.StepData_SelectType):
    """
    None
    """
    def AnnotationText(self) -> StepVisual_AnnotationText: 
        """
        returns Value as a AnnotationText (Null if another type)
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
        Recognizes a TextOrCharacter Kind Entity that is : 1 -> AnnotationText 2 -> CompositeText 3 -> TextLiteral 0 else
        """
    def CaseNumber(self) -> int: 
        """
        Recognizes the Type of the stored Entity, or zero if it is Null or SelectMember. Calls the first method CaseNum on Value
        """
    def CompositeText(self) -> StepVisual_CompositeText: 
        """
        returns Value as a CompositeText (Null if another type)
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
    def TextLiteral(self) -> StepVisual_TextLiteral: 
        """
        returns Value as a TextLiteral (Null if another type)
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
class StepVisual_TextPath():
    """
    None

    Members:

      StepVisual_tpUp

      StepVisual_tpRight

      StepVisual_tpDown

      StepVisual_tpLeft
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    StepVisual_tpDown: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpDown
    StepVisual_tpLeft: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpLeft
    StepVisual_tpRight: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpRight
    StepVisual_tpUp: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpUp
    __entries: dict # value = {'StepVisual_tpUp': (StepVisual_TextPath.StepVisual_tpUp, None), 'StepVisual_tpRight': (StepVisual_TextPath.StepVisual_tpRight, None), 'StepVisual_tpDown': (StepVisual_TextPath.StepVisual_tpDown, None), 'StepVisual_tpLeft': (StepVisual_TextPath.StepVisual_tpLeft, None)}
    __members__: dict # value = {'StepVisual_tpUp': StepVisual_TextPath.StepVisual_tpUp, 'StepVisual_tpRight': StepVisual_TextPath.StepVisual_tpRight, 'StepVisual_tpDown': StepVisual_TextPath.StepVisual_tpDown, 'StepVisual_tpLeft': StepVisual_TextPath.StepVisual_tpLeft}
    pass
class StepVisual_TextStyle(OCP.Standard.Standard_Transient):
    def CharacterAppearance(self) -> StepVisual_TextStyleForDefinedFont: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCharacterAppearance : StepVisual_TextStyleForDefinedFont) -> None: 
        """
        None
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
    def SetCharacterAppearance(self,aCharacterAppearance : StepVisual_TextStyleForDefinedFont) -> None: 
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
class StepVisual_TextStyleForDefinedFont(OCP.Standard.Standard_Transient):
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
    def Init(self,aTextColour : StepVisual_Colour) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def SetTextColour(self,aTextColour : StepVisual_Colour) -> None: 
        """
        None
        """
    def TextColour(self) -> StepVisual_Colour: 
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
class StepVisual_TextStyleWithBoxCharacteristics(StepVisual_TextStyle, OCP.Standard.Standard_Transient):
    def CharacterAppearance(self) -> StepVisual_TextStyleForDefinedFont: 
        """
        None
        """
    def Characteristics(self) -> StepVisual_HArray1OfBoxCharacteristicSelect: 
        """
        None
        """
    def CharacteristicsValue(self,num : int) -> StepVisual_BoxCharacteristicSelect: 
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
    def Init(self,aName : OCP.TCollection.TCollection_HAsciiString,aCharacterAppearance : StepVisual_TextStyleForDefinedFont,aCharacteristics : StepVisual_HArray1OfBoxCharacteristicSelect) -> None: 
        """
        None
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
    def NbCharacteristics(self) -> int: 
        """
        None
        """
    def SetCharacterAppearance(self,aCharacterAppearance : StepVisual_TextStyleForDefinedFont) -> None: 
        """
        None
        """
    def SetCharacteristics(self,aCharacteristics : StepVisual_HArray1OfBoxCharacteristicSelect) -> None: 
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
class StepVisual_VectorOfHSequenceOfInteger(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : OCP.TColStd.TColStd_HSequenceOfInteger) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Append
        """
    def Appended(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : StepVisual_VectorOfHSequenceOfInteger,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns first element
        """
    def ChangeLast(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
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
    def SetValue(self,theIndex : int,theValue : OCP.TColStd.TColStd_HSequenceOfInteger) -> OCP.TColStd.TColStd_HSequenceOfInteger: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OCP.TColStd.TColStd_HSequenceOfInteger: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : StepVisual_VectorOfHSequenceOfInteger) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class StepVisual_ViewVolume(OCP.Standard.Standard_Transient):
    def BackPlaneClipping(self) -> bool: 
        """
        None
        """
    def BackPlaneDistance(self) -> float: 
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
    def FrontPlaneClipping(self) -> bool: 
        """
        None
        """
    def FrontPlaneDistance(self) -> float: 
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
    def Init(self,aProjectionType : StepVisual_CentralOrParallel,aProjectionPoint : OCP.StepGeom.StepGeom_CartesianPoint,aViewPlaneDistance : float,aFrontPlaneDistance : float,aFrontPlaneClipping : bool,aBackPlaneDistance : float,aBackPlaneClipping : bool,aViewVolumeSidesClipping : bool,aViewWindow : StepVisual_PlanarBox) -> None: 
        """
        None
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def ProjectionPoint(self) -> OCP.StepGeom.StepGeom_CartesianPoint: 
        """
        None
        """
    def ProjectionType(self) -> StepVisual_CentralOrParallel: 
        """
        None
        """
    def SetBackPlaneClipping(self,aBackPlaneClipping : bool) -> None: 
        """
        None
        """
    def SetBackPlaneDistance(self,aBackPlaneDistance : float) -> None: 
        """
        None
        """
    def SetFrontPlaneClipping(self,aFrontPlaneClipping : bool) -> None: 
        """
        None
        """
    def SetFrontPlaneDistance(self,aFrontPlaneDistance : float) -> None: 
        """
        None
        """
    def SetProjectionPoint(self,aProjectionPoint : OCP.StepGeom.StepGeom_CartesianPoint) -> None: 
        """
        None
        """
    def SetProjectionType(self,aProjectionType : StepVisual_CentralOrParallel) -> None: 
        """
        None
        """
    def SetViewPlaneDistance(self,aViewPlaneDistance : float) -> None: 
        """
        None
        """
    def SetViewVolumeSidesClipping(self,aViewVolumeSidesClipping : bool) -> None: 
        """
        None
        """
    def SetViewWindow(self,aViewWindow : StepVisual_PlanarBox) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewPlaneDistance(self) -> float: 
        """
        None
        """
    def ViewVolumeSidesClipping(self) -> bool: 
        """
        None
        """
    def ViewWindow(self) -> StepVisual_PlanarBox: 
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
StepVisual_Null: OCP.StepVisual.StepVisual_NullStyle # value = StepVisual_NullStyle.StepVisual_Null
StepVisual_copCentral: OCP.StepVisual.StepVisual_CentralOrParallel # value = StepVisual_CentralOrParallel.StepVisual_copCentral
StepVisual_copParallel: OCP.StepVisual.StepVisual_CentralOrParallel # value = StepVisual_CentralOrParallel.StepVisual_copParallel
StepVisual_mtAsterisk: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtAsterisk
StepVisual_mtDot: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtDot
StepVisual_mtPlus: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtPlus
StepVisual_mtRing: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtRing
StepVisual_mtSquare: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtSquare
StepVisual_mtTriangle: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtTriangle
StepVisual_mtX: OCP.StepVisual.StepVisual_MarkerType # value = StepVisual_MarkerType.StepVisual_mtX
StepVisual_ssBoth: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssBoth
StepVisual_ssNegative: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssNegative
StepVisual_ssPositive: OCP.StepVisual.StepVisual_SurfaceSide # value = StepVisual_SurfaceSide.StepVisual_ssPositive
StepVisual_tpDown: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpDown
StepVisual_tpLeft: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpLeft
StepVisual_tpRight: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpRight
StepVisual_tpUp: OCP.StepVisual.StepVisual_TextPath # value = StepVisual_TextPath.StepVisual_tpUp
