import OCP.RWGltf
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TDF
import OCP.TShort
import OCP.TColgp
import OCP.Bnd
import OCP.Standard
import OCP.Poly
import OCP.Quantity
import OCP.TDocStd
import OCP.XCAFDoc
import OCP.TColStd
import OCP.TCollection
import io
import OCP.Message
import OCP.gp
import OCP.Image
import OCP.XCAFPrs
__all__  = [
"RWGltf_CafReader",
"RWGltf_CafWriter",
"RWGltf_GltfAccessor",
"RWGltf_GltfAccessorCompType",
"RWGltf_GltfAccessorLayout",
"RWGltf_GltfAlphaMode",
"RWGltf_GltfArrayType",
"RWGltf_GltfBufferView",
"RWGltf_GltfBufferViewTarget",
"RWGltf_GltfFace",
"RWGltf_GltfLatePrimitiveArray",
"RWGltf_GltfMaterialMap",
"RWGltf_GltfOStreamWriter",
"RWGltf_GltfPrimArrayData",
"RWGltf_GltfPrimitiveMode",
"RWGltf_GltfRootElement",
"RWGltf_GltfSceneNodeMap",
"RWGltf_GltfSharedIStream",
"RWGltf_MaterialCommon",
"RWGltf_MaterialMetallicRoughness",
"RWGltf_PrimitiveArrayReader",
"RWGltf_TriangulationReader",
"RWGltf_WriterTrsfFormat",
"RWGltf_GltfParseAccessorType",
"RWGltf_GltfParseAlphaMode",
"RWGltf_GltfParseAttribType",
"RWGltf_GltfRootElementName",
"RWGltf_GltfAccessorCompType_Float32",
"RWGltf_GltfAccessorCompType_Int16",
"RWGltf_GltfAccessorCompType_Int8",
"RWGltf_GltfAccessorCompType_UInt16",
"RWGltf_GltfAccessorCompType_UInt32",
"RWGltf_GltfAccessorCompType_UInt8",
"RWGltf_GltfAccessorCompType_UNKNOWN",
"RWGltf_GltfAccessorLayout_Mat2",
"RWGltf_GltfAccessorLayout_Mat3",
"RWGltf_GltfAccessorLayout_Mat4",
"RWGltf_GltfAccessorLayout_Scalar",
"RWGltf_GltfAccessorLayout_UNKNOWN",
"RWGltf_GltfAccessorLayout_Vec2",
"RWGltf_GltfAccessorLayout_Vec3",
"RWGltf_GltfAccessorLayout_Vec4",
"RWGltf_GltfAlphaMode_Blend",
"RWGltf_GltfAlphaMode_Mask",
"RWGltf_GltfAlphaMode_Opaque",
"RWGltf_GltfArrayType_Color",
"RWGltf_GltfArrayType_Indices",
"RWGltf_GltfArrayType_Joint",
"RWGltf_GltfArrayType_Normal",
"RWGltf_GltfArrayType_Position",
"RWGltf_GltfArrayType_TCoord0",
"RWGltf_GltfArrayType_TCoord1",
"RWGltf_GltfArrayType_UNKNOWN",
"RWGltf_GltfArrayType_Weight",
"RWGltf_GltfBufferViewTarget_ARRAY_BUFFER",
"RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER",
"RWGltf_GltfBufferViewTarget_UNKNOWN",
"RWGltf_GltfPrimitiveMode_LineLoop",
"RWGltf_GltfPrimitiveMode_LineStrip",
"RWGltf_GltfPrimitiveMode_Lines",
"RWGltf_GltfPrimitiveMode_Points",
"RWGltf_GltfPrimitiveMode_TriangleFan",
"RWGltf_GltfPrimitiveMode_TriangleStrip",
"RWGltf_GltfPrimitiveMode_Triangles",
"RWGltf_GltfPrimitiveMode_UNKNOWN",
"RWGltf_GltfRootElement_Accessors",
"RWGltf_GltfRootElement_Animations",
"RWGltf_GltfRootElement_Asset",
"RWGltf_GltfRootElement_BufferViews",
"RWGltf_GltfRootElement_Buffers",
"RWGltf_GltfRootElement_ExtensionsRequired",
"RWGltf_GltfRootElement_ExtensionsUsed",
"RWGltf_GltfRootElement_Images",
"RWGltf_GltfRootElement_Materials",
"RWGltf_GltfRootElement_Meshes",
"RWGltf_GltfRootElement_NB",
"RWGltf_GltfRootElement_NB_MANDATORY",
"RWGltf_GltfRootElement_Nodes",
"RWGltf_GltfRootElement_Programs",
"RWGltf_GltfRootElement_Samplers",
"RWGltf_GltfRootElement_Scene",
"RWGltf_GltfRootElement_Scenes",
"RWGltf_GltfRootElement_Shaders",
"RWGltf_GltfRootElement_Skins",
"RWGltf_GltfRootElement_Techniques",
"RWGltf_GltfRootElement_Textures",
"RWGltf_WriterTrsfFormat_Compact",
"RWGltf_WriterTrsfFormat_LOWER",
"RWGltf_WriterTrsfFormat_Mat4",
"RWGltf_WriterTrsfFormat_TRS",
"RWGltf_WriterTrsfFormat_UPPER"
]
class RWGltf_CafReader():
    """
    The glTF (GL Transmission Format) mesh reader into XDE document.
    """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def SetMeshNameAsFallback(self,theToFallback : bool) -> None: 
        """
        Set flag to use Mesh name in case if Node name is empty.
        """
    def SetParallel(self,theToParallel : bool) -> None: 
        """
        Setup multithreaded execution.
        """
    def SetSkipEmptyNodes(self,theToSkip : bool) -> None: 
        """
        Set flag to ignore nodes without Geometry.
        """
    def ToParallel(self) -> bool: 
        """
        Return TRUE if multithreaded optimizations are allowed; FALSE by default.
        """
    def ToSkipEmptyNodes(self) -> bool: 
        """
        Return TRUE if Nodes without Geometry should be ignored, TRUE by default.
        """
    def ToUseMeshNameAsFallback(self) -> bool: 
        """
        Set flag to use Mesh name in case if Node name is empty, TRUE by default.
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
class RWGltf_CafWriter(OCP.Standard.Standard_Transient):
    """
    glTF writer context from XCAF document.
    """
    def ChangeCoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: 
        """
        Return transformation from OCCT to glTF coordinate system.
        """
    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: 
        """
        Return transformation from OCCT to glTF coordinate system.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultStyle(self) -> OCP.XCAFPrs.XCAFPrs_Style: 
        """
        Return default material definition to be used for nodes with only color defined.
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
    def IsBinary(self) -> bool: 
        """
        Return flag to write into binary glTF format (.glb), specified within class constructor.
        """
    def IsForcedUVExport(self) -> bool: 
        """
        Return TRUE to export UV coordinates even if there are no mapped texture; FALSE by default.
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
    @overload
    def Perform(self,theDocument : OCP.TDocStd.TDocStd_Document,theRootLabels : OCP.TDF.TDF_LabelSequence,theLabelFilter : OCP.TColStd.TColStd_MapOfAsciiString,theFileInfo : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theProgress : OCP.Message.Message_ProgressRange) -> bool: 
        """
        Write glTF file and associated binary file. Triangulation data should be precomputed within shapes!

        Write glTF file and associated binary file. Triangulation data should be precomputed within shapes!
        """
    @overload
    def Perform(self,theDocument : OCP.TDocStd.TDocStd_Document,theFileInfo : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theProgress : OCP.Message.Message_ProgressRange) -> bool: ...
    def SetCoordinateSystemConverter(self,theConverter : RWMesh_CoordinateSystemConverter) -> None: 
        """
        Set transformation from OCCT to glTF coordinate system.
        """
    def SetDefaultStyle(self,theStyle : OCP.XCAFPrs.XCAFPrs_Style) -> None: 
        """
        Set default material definition to be used for nodes with only color defined.
        """
    def SetForcedUVExport(self,theToForce : bool) -> None: 
        """
        Set flag to export UV coordinates even if there are no mapped texture; FALSE by default.
        """
    def SetTransformationFormat(self,theFormat : RWGltf_WriterTrsfFormat) -> None: 
        """
        Set preferred transformation format for writing into glTF file.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformationFormat(self) -> RWGltf_WriterTrsfFormat: 
        """
        Return preferred transformation format for writing into glTF file; RWGltf_WriterTrsfFormat_Compact by default.
        """
    def __init__(self,theFile : OCP.TCollection.TCollection_AsciiString,theIsBinary : bool) -> None: ...
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
class RWGltf_GltfAccessor():
    """
    Low-level glTF data structure defining Accessor.
    """
    def __init__(self) -> None: ...
    @property
    def ComponentType(self) -> RWGltf_GltfAccessorCompType:
        """
        :type: RWGltf_GltfAccessorCompType
        """
    @ComponentType.setter
    def ComponentType(self, arg0: RWGltf_GltfAccessorCompType) -> None:
        pass
    @property
    def Type(self) -> RWGltf_GltfAccessorLayout:
        """
        :type: RWGltf_GltfAccessorLayout
        """
    @Type.setter
    def Type(self, arg0: RWGltf_GltfAccessorLayout) -> None:
        pass
    pass
class RWGltf_GltfAccessorCompType():
    """
    Low-level glTF enumeration defining Accessor component type.

    Members:

      RWGltf_GltfAccessorCompType_UNKNOWN

      RWGltf_GltfAccessorCompType_Int8

      RWGltf_GltfAccessorCompType_UInt8

      RWGltf_GltfAccessorCompType_Int16

      RWGltf_GltfAccessorCompType_UInt16

      RWGltf_GltfAccessorCompType_UInt32

      RWGltf_GltfAccessorCompType_Float32
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
    RWGltf_GltfAccessorCompType_Float32: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Float32: 5126>
    RWGltf_GltfAccessorCompType_Int16: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int16: 5122>
    RWGltf_GltfAccessorCompType_Int8: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int8: 5120>
    RWGltf_GltfAccessorCompType_UInt16: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt16: 5123>
    RWGltf_GltfAccessorCompType_UInt32: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt32: 5125>
    RWGltf_GltfAccessorCompType_UInt8: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt8: 5121>
    RWGltf_GltfAccessorCompType_UNKNOWN: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UNKNOWN: 0>
    __entries: dict # value = {'RWGltf_GltfAccessorCompType_UNKNOWN': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UNKNOWN: 0>, None), 'RWGltf_GltfAccessorCompType_Int8': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int8: 5120>, None), 'RWGltf_GltfAccessorCompType_UInt8': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt8: 5121>, None), 'RWGltf_GltfAccessorCompType_Int16': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int16: 5122>, None), 'RWGltf_GltfAccessorCompType_UInt16': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt16: 5123>, None), 'RWGltf_GltfAccessorCompType_UInt32': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt32: 5125>, None), 'RWGltf_GltfAccessorCompType_Float32': (<RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Float32: 5126>, None)}
    __members__: dict # value = {'RWGltf_GltfAccessorCompType_UNKNOWN': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UNKNOWN: 0>, 'RWGltf_GltfAccessorCompType_Int8': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int8: 5120>, 'RWGltf_GltfAccessorCompType_UInt8': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt8: 5121>, 'RWGltf_GltfAccessorCompType_Int16': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int16: 5122>, 'RWGltf_GltfAccessorCompType_UInt16': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt16: 5123>, 'RWGltf_GltfAccessorCompType_UInt32': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt32: 5125>, 'RWGltf_GltfAccessorCompType_Float32': <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Float32: 5126>}
    pass
class RWGltf_GltfAccessorLayout():
    """
    Low-level glTF enumeration defining Accessor layout. Similar to Graphic3d_TypeOfData but does not define actual type and includes matrices.

    Members:

      RWGltf_GltfAccessorLayout_UNKNOWN

      RWGltf_GltfAccessorLayout_Scalar

      RWGltf_GltfAccessorLayout_Vec2

      RWGltf_GltfAccessorLayout_Vec3

      RWGltf_GltfAccessorLayout_Vec4

      RWGltf_GltfAccessorLayout_Mat2

      RWGltf_GltfAccessorLayout_Mat3

      RWGltf_GltfAccessorLayout_Mat4
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
    RWGltf_GltfAccessorLayout_Mat2: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat2: 5>
    RWGltf_GltfAccessorLayout_Mat3: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat3: 6>
    RWGltf_GltfAccessorLayout_Mat4: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat4: 7>
    RWGltf_GltfAccessorLayout_Scalar: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Scalar: 1>
    RWGltf_GltfAccessorLayout_UNKNOWN: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_UNKNOWN: 0>
    RWGltf_GltfAccessorLayout_Vec2: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec2: 2>
    RWGltf_GltfAccessorLayout_Vec3: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec3: 3>
    RWGltf_GltfAccessorLayout_Vec4: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec4: 4>
    __entries: dict # value = {'RWGltf_GltfAccessorLayout_UNKNOWN': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_UNKNOWN: 0>, None), 'RWGltf_GltfAccessorLayout_Scalar': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Scalar: 1>, None), 'RWGltf_GltfAccessorLayout_Vec2': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec2: 2>, None), 'RWGltf_GltfAccessorLayout_Vec3': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec3: 3>, None), 'RWGltf_GltfAccessorLayout_Vec4': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec4: 4>, None), 'RWGltf_GltfAccessorLayout_Mat2': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat2: 5>, None), 'RWGltf_GltfAccessorLayout_Mat3': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat3: 6>, None), 'RWGltf_GltfAccessorLayout_Mat4': (<RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat4: 7>, None)}
    __members__: dict # value = {'RWGltf_GltfAccessorLayout_UNKNOWN': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_UNKNOWN: 0>, 'RWGltf_GltfAccessorLayout_Scalar': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Scalar: 1>, 'RWGltf_GltfAccessorLayout_Vec2': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec2: 2>, 'RWGltf_GltfAccessorLayout_Vec3': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec3: 3>, 'RWGltf_GltfAccessorLayout_Vec4': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec4: 4>, 'RWGltf_GltfAccessorLayout_Mat2': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat2: 5>, 'RWGltf_GltfAccessorLayout_Mat3': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat3: 6>, 'RWGltf_GltfAccessorLayout_Mat4': <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat4: 7>}
    pass
class RWGltf_GltfAlphaMode():
    """
    Low-level glTF enumeration defining Alpha Mode.

    Members:

      RWGltf_GltfAlphaMode_Opaque

      RWGltf_GltfAlphaMode_Mask

      RWGltf_GltfAlphaMode_Blend
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
    RWGltf_GltfAlphaMode_Blend: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Blend: 2>
    RWGltf_GltfAlphaMode_Mask: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Mask: 1>
    RWGltf_GltfAlphaMode_Opaque: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Opaque: 0>
    __entries: dict # value = {'RWGltf_GltfAlphaMode_Opaque': (<RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Opaque: 0>, None), 'RWGltf_GltfAlphaMode_Mask': (<RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Mask: 1>, None), 'RWGltf_GltfAlphaMode_Blend': (<RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Blend: 2>, None)}
    __members__: dict # value = {'RWGltf_GltfAlphaMode_Opaque': <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Opaque: 0>, 'RWGltf_GltfAlphaMode_Mask': <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Mask: 1>, 'RWGltf_GltfAlphaMode_Blend': <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Blend: 2>}
    pass
class RWGltf_GltfArrayType():
    """
    Low-level glTF enumeration defining Array type.

    Members:

      RWGltf_GltfArrayType_UNKNOWN

      RWGltf_GltfArrayType_Indices

      RWGltf_GltfArrayType_Position

      RWGltf_GltfArrayType_Normal

      RWGltf_GltfArrayType_Color

      RWGltf_GltfArrayType_TCoord0

      RWGltf_GltfArrayType_TCoord1

      RWGltf_GltfArrayType_Joint

      RWGltf_GltfArrayType_Weight
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
    RWGltf_GltfArrayType_Color: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color: 4>
    RWGltf_GltfArrayType_Indices: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices: 1>
    RWGltf_GltfArrayType_Joint: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint: 7>
    RWGltf_GltfArrayType_Normal: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal: 3>
    RWGltf_GltfArrayType_Position: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Position: 2>
    RWGltf_GltfArrayType_TCoord0: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0: 5>
    RWGltf_GltfArrayType_TCoord1: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1: 6>
    RWGltf_GltfArrayType_UNKNOWN: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN: 0>
    RWGltf_GltfArrayType_Weight: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight: 8>
    __entries: dict # value = {'RWGltf_GltfArrayType_UNKNOWN': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN: 0>, None), 'RWGltf_GltfArrayType_Indices': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices: 1>, None), 'RWGltf_GltfArrayType_Position': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Position: 2>, None), 'RWGltf_GltfArrayType_Normal': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal: 3>, None), 'RWGltf_GltfArrayType_Color': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color: 4>, None), 'RWGltf_GltfArrayType_TCoord0': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0: 5>, None), 'RWGltf_GltfArrayType_TCoord1': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1: 6>, None), 'RWGltf_GltfArrayType_Joint': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint: 7>, None), 'RWGltf_GltfArrayType_Weight': (<RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight: 8>, None)}
    __members__: dict # value = {'RWGltf_GltfArrayType_UNKNOWN': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN: 0>, 'RWGltf_GltfArrayType_Indices': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices: 1>, 'RWGltf_GltfArrayType_Position': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Position: 2>, 'RWGltf_GltfArrayType_Normal': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal: 3>, 'RWGltf_GltfArrayType_Color': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color: 4>, 'RWGltf_GltfArrayType_TCoord0': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0: 5>, 'RWGltf_GltfArrayType_TCoord1': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1: 6>, 'RWGltf_GltfArrayType_Joint': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint: 7>, 'RWGltf_GltfArrayType_Weight': <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight: 8>}
    pass
class RWGltf_GltfBufferView():
    """
    Low-level glTF data structure defining BufferView.
    """
    def __init__(self) -> None: ...
    @property
    def Target(self) -> RWGltf_GltfBufferViewTarget:
        """
        :type: RWGltf_GltfBufferViewTarget
        """
    @Target.setter
    def Target(self, arg0: RWGltf_GltfBufferViewTarget) -> None:
        pass
    pass
class RWGltf_GltfBufferViewTarget():
    """
    Low-level glTF enumeration defining BufferView target.

    Members:

      RWGltf_GltfBufferViewTarget_UNKNOWN

      RWGltf_GltfBufferViewTarget_ARRAY_BUFFER

      RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER
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
    RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: 34962>
    RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: 34963>
    RWGltf_GltfBufferViewTarget_UNKNOWN: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_UNKNOWN: 0>
    __entries: dict # value = {'RWGltf_GltfBufferViewTarget_UNKNOWN': (<RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_UNKNOWN: 0>, None), 'RWGltf_GltfBufferViewTarget_ARRAY_BUFFER': (<RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: 34962>, None), 'RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER': (<RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: 34963>, None)}
    __members__: dict # value = {'RWGltf_GltfBufferViewTarget_UNKNOWN': <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_UNKNOWN: 0>, 'RWGltf_GltfBufferViewTarget_ARRAY_BUFFER': <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: 34962>, 'RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER': <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: 34963>}
    pass
class RWGltf_GltfFace():
    """
    Low-level glTF data structure holding single Face (one primitive array) definition.
    """
    def __init__(self) -> None: ...
    @property
    def Indices(self) -> RWGltf_GltfAccessor:
        """
        :type: RWGltf_GltfAccessor
        """
    @Indices.setter
    def Indices(self, arg0: RWGltf_GltfAccessor) -> None:
        pass
    @property
    def NodeNorm(self) -> RWGltf_GltfAccessor:
        """
        :type: RWGltf_GltfAccessor
        """
    @NodeNorm.setter
    def NodeNorm(self, arg0: RWGltf_GltfAccessor) -> None:
        pass
    @property
    def NodePos(self) -> RWGltf_GltfAccessor:
        """
        :type: RWGltf_GltfAccessor
        """
    @NodePos.setter
    def NodePos(self, arg0: RWGltf_GltfAccessor) -> None:
        pass
    @property
    def NodeUV(self) -> RWGltf_GltfAccessor:
        """
        :type: RWGltf_GltfAccessor
        """
    @NodeUV.setter
    def NodeUV(self, arg0: RWGltf_GltfAccessor) -> None:
        pass
    pass
class RWGltf_GltfLatePrimitiveArray(OCP.Poly.Poly_Triangulation, OCP.Standard.Standard_Transient):
    """
    Mesh data wrapper for delayed primitive array loading from glTF file. Class inherits Poly_Triangulation so that it can be put temporarily into TopoDS_Face within assembly structure, to be replaced with proper Poly_Triangulation loaded later on.
    """
    def AddPrimArrayData(self,theType : RWGltf_GltfArrayType) -> RWGltf_GltfPrimArrayData: 
        """
        Add primitive array data element.
        """
    def BaseColor(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return base color.
        """
    def BoundingBox(self) -> OCP.Bnd.Bnd_Box: 
        """
        Return bounding box defined within glTF file, or VOID if not specified.
        """
    def ChangeNode(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Give access to the node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def ChangeNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of 3D nodes (3D points) for this triangulation. The returned array is shared. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def ChangeNormals(self) -> OCP.TShort.TShort_Array1OfShortReal: 
        """
        Gives access to the table of node normals.
        """
    def ChangeTriangle(self,theIndex : int) -> OCP.Poly.Poly_Triangle: 
        """
        Give access to the triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def ChangeTriangles(self) -> OCP.Poly.Poly_Array1OfTriangle: 
        """
        Returns the table of triangles for this triangulation. Function ChangeUVNodes shares the returned array. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def ChangeUVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Give access to the UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def ChangeUVNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of 2D nodes (2D points) associated with each 3D node of this triangulation. Function ChangeUVNodes shares the returned array. Therefore if the table is selected by reference, you can, by simply modifying it, directly modify the data structure of this triangulation.
        """
    def Copy(self) -> OCP.Poly.Poly_Triangulation: 
        """
        Creates full copy of current triangulation
        """
    def Data(self) -> Any: 
        """
        Return primitive array data elements.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    @overload
    def Deflection(self) -> float: 
        """
        Returns the deflection of this triangulation.

        Sets the deflection of this triangulation to theDeflection. See more on deflection in Polygon2D
        """
    @overload
    def Deflection(self,theDeflection : float) -> None: ...
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasNormals(self) -> bool: 
        """
        Returns Standard_True if nodal normals are defined.
        """
    def HasStyle(self) -> bool: 
        """
        Return true if primitive array has assigned material
        """
    def HasUVNodes(self) -> bool: 
        """
        Returns Standard_True if 2D nodes are associated with 3D nodes for this triangulation.
        """
    def Id(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Entity id.
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
    def MaterialCommon(self) -> RWGltf_MaterialCommon: 
        """
        Return common (obsolete) material definition.
        """
    def MaterialPbr(self) -> RWGltf_MaterialMetallicRoughness: 
        """
        Return PBR material definition.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Entity name.
        """
    def NbNodes(self) -> int: 
        """
        Returns the number of nodes for this triangulation.
        """
    def NbTriangles(self) -> int: 
        """
        Returns the number of triangles for this triangulation.
        """
    def Node(self,theIndex : int) -> OCP.gp.gp_Pnt: 
        """
        Returns node at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def Nodes(self) -> OCP.TColgp.TColgp_Array1OfPnt: 
        """
        Returns the table of 3D nodes (3D points) for this triangulation.
        """
    def Normal(self,theIndex : int) -> OCP.gp.gp_Dir: 
        """
        Returns normal at the given index. Raises Standard_OutOfRange exception.
        """
    def Normals(self) -> OCP.TShort.TShort_Array1OfShortReal: 
        """
        Returns the table of node normals.
        """
    def PrimitiveMode(self) -> RWGltf_GltfPrimitiveMode: 
        """
        Return type of primitive array.
        """
    def RemoveUVNodes(self) -> None: 
        """
        Deallocates the UV nodes.
        """
    def SetBoundingBox(self,theBox : OCP.Bnd.Bnd_Box) -> None: 
        """
        This method sets input bounding box and assigns a FAKE data to underlying Poly_Triangulation as Min/Max corners of bounding box, so that standard tools like BRepBndLib::Add() can be used transparently for computing bounding box of this face.
        """
    def SetMaterialCommon(self,theMat : RWGltf_MaterialCommon) -> None: 
        """
        Set common (obsolete) material definition.
        """
    def SetMaterialPbr(self,theMat : RWGltf_MaterialMetallicRoughness) -> None: 
        """
        Set PBR material definition.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Assign entity name.
        """
    def SetNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: 
        """
        Changes normal at the given index. Raises Standard_OutOfRange exception.
        """
    def SetNormals(self,theNormals : OCP.TShort.TShort_HArray1OfShortReal) -> None: 
        """
        Sets the table of node normals. raises exception if length of theNormals != 3*NbNodes
        """
    def SetPrimitiveMode(self,theMode : RWGltf_GltfPrimitiveMode) -> None: 
        """
        Set type of primitive array.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Triangle(self,theIndex : int) -> OCP.Poly.Poly_Triangle: 
        """
        Returns triangle at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbTriangles.
        """
    def Triangles(self) -> OCP.Poly.Poly_Array1OfTriangle: 
        """
        Returns the table of triangles for this triangulation.
        """
    def UVNode(self,theIndex : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns UVNode at the given index. Raises Standard_OutOfRange exception if theIndex is less than 1 or greater than NbNodes.
        """
    def UVNodes(self) -> OCP.TColgp.TColgp_Array1OfPnt2d: 
        """
        Returns the table of 2D nodes (2D points) associated with each 3D node of this triangulation. The function HasUVNodes checks if 2D nodes are associated with the 3D nodes of this triangulation. Const reference on the 2d nodes values.
        """
    def __init__(self,theId : OCP.TCollection.TCollection_AsciiString,theName : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class RWGltf_GltfMaterialMap():
    """
    Material manager for exporting into glTF format.
    """
    def AddImages(self,theWriter : RWGltf_GltfOStreamWriter,theStyle : OCP.XCAFPrs.XCAFPrs_Style) -> Tuple[bool]: 
        """
        Add material images.
        """
    def AddMaterial(self,theWriter : RWGltf_GltfOStreamWriter,theStyle : OCP.XCAFPrs.XCAFPrs_Style) -> Tuple[bool]: 
        """
        Add material.
        """
    def AddTextures(self,theWriter : RWGltf_GltfOStreamWriter,theStyle : OCP.XCAFPrs.XCAFPrs_Style) -> Tuple[bool]: 
        """
        Add material textures.
        """
    def NbImages(self) -> int: 
        """
        Return extent of images map.
        """
    def NbTextures(self) -> int: 
        """
        Return extent of textures map.
        """
    def __init__(self,theFile : OCP.TCollection.TCollection_AsciiString,theDefSamplerId : int) -> None: ...
    @staticmethod
    def baseColorTexture_s(theMat : OCP.XCAFDoc.XCAFDoc_VisMaterial) -> OCP.Image.Image_Texture: 
        """
        Return base color texture.
        """
    pass
class RWGltf_GltfOStreamWriter():
    """
    rapidjson::Writer wrapper for forward declaration.
    """
    def __init__(self,theOStream : Any) -> None: ...
    pass
class RWGltf_GltfPrimArrayData():
    """
    An element within primitive array - vertex attribute or element indexes.
    """
    @overload
    def __init__(self,theType : RWGltf_GltfArrayType) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def Accessor(self) -> RWGltf_GltfAccessor:
        """
        :type: RWGltf_GltfAccessor
        """
    @Accessor.setter
    def Accessor(self, arg0: RWGltf_GltfAccessor) -> None:
        pass
    @property
    def StreamUri(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @StreamUri.setter
    def StreamUri(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def Type(self) -> RWGltf_GltfArrayType:
        """
        :type: RWGltf_GltfArrayType
        """
    @Type.setter
    def Type(self, arg0: RWGltf_GltfArrayType) -> None:
        pass
    pass
class RWGltf_GltfPrimitiveMode():
    """
    Low-level glTF enumeration defining Primitive type. Similar to Graphic3d_TypeOfData but does not define actual type and includes matrices.

    Members:

      RWGltf_GltfPrimitiveMode_UNKNOWN

      RWGltf_GltfPrimitiveMode_Points

      RWGltf_GltfPrimitiveMode_Lines

      RWGltf_GltfPrimitiveMode_LineLoop

      RWGltf_GltfPrimitiveMode_LineStrip

      RWGltf_GltfPrimitiveMode_Triangles

      RWGltf_GltfPrimitiveMode_TriangleStrip

      RWGltf_GltfPrimitiveMode_TriangleFan
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
    RWGltf_GltfPrimitiveMode_LineLoop: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineLoop: 2>
    RWGltf_GltfPrimitiveMode_LineStrip: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineStrip: 3>
    RWGltf_GltfPrimitiveMode_Lines: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Lines: 1>
    RWGltf_GltfPrimitiveMode_Points: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Points: 0>
    RWGltf_GltfPrimitiveMode_TriangleFan: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleFan: 6>
    RWGltf_GltfPrimitiveMode_TriangleStrip: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleStrip: 5>
    RWGltf_GltfPrimitiveMode_Triangles: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Triangles: 4>
    RWGltf_GltfPrimitiveMode_UNKNOWN: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_UNKNOWN: -1>
    __entries: dict # value = {'RWGltf_GltfPrimitiveMode_UNKNOWN': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_UNKNOWN: -1>, None), 'RWGltf_GltfPrimitiveMode_Points': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Points: 0>, None), 'RWGltf_GltfPrimitiveMode_Lines': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Lines: 1>, None), 'RWGltf_GltfPrimitiveMode_LineLoop': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineLoop: 2>, None), 'RWGltf_GltfPrimitiveMode_LineStrip': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineStrip: 3>, None), 'RWGltf_GltfPrimitiveMode_Triangles': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Triangles: 4>, None), 'RWGltf_GltfPrimitiveMode_TriangleStrip': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleStrip: 5>, None), 'RWGltf_GltfPrimitiveMode_TriangleFan': (<RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleFan: 6>, None)}
    __members__: dict # value = {'RWGltf_GltfPrimitiveMode_UNKNOWN': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_UNKNOWN: -1>, 'RWGltf_GltfPrimitiveMode_Points': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Points: 0>, 'RWGltf_GltfPrimitiveMode_Lines': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Lines: 1>, 'RWGltf_GltfPrimitiveMode_LineLoop': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineLoop: 2>, 'RWGltf_GltfPrimitiveMode_LineStrip': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineStrip: 3>, 'RWGltf_GltfPrimitiveMode_Triangles': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Triangles: 4>, 'RWGltf_GltfPrimitiveMode_TriangleStrip': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleStrip: 5>, 'RWGltf_GltfPrimitiveMode_TriangleFan': <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleFan: 6>}
    pass
class RWGltf_GltfRootElement():
    """
    Root elements within glTF JSON document.

    Members:

      RWGltf_GltfRootElement_Asset

      RWGltf_GltfRootElement_Scenes

      RWGltf_GltfRootElement_Scene

      RWGltf_GltfRootElement_Nodes

      RWGltf_GltfRootElement_Meshes

      RWGltf_GltfRootElement_Accessors

      RWGltf_GltfRootElement_BufferViews

      RWGltf_GltfRootElement_Buffers

      RWGltf_GltfRootElement_NB_MANDATORY

      RWGltf_GltfRootElement_Animations

      RWGltf_GltfRootElement_Materials

      RWGltf_GltfRootElement_Programs

      RWGltf_GltfRootElement_Samplers

      RWGltf_GltfRootElement_Shaders

      RWGltf_GltfRootElement_Skins

      RWGltf_GltfRootElement_Techniques

      RWGltf_GltfRootElement_Textures

      RWGltf_GltfRootElement_Images

      RWGltf_GltfRootElement_ExtensionsUsed

      RWGltf_GltfRootElement_ExtensionsRequired

      RWGltf_GltfRootElement_NB
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
    RWGltf_GltfRootElement_Accessors: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Accessors: 5>
    RWGltf_GltfRootElement_Animations: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>
    RWGltf_GltfRootElement_Asset: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Asset: 0>
    RWGltf_GltfRootElement_BufferViews: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_BufferViews: 6>
    RWGltf_GltfRootElement_Buffers: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Buffers: 7>
    RWGltf_GltfRootElement_ExtensionsRequired: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsRequired: 18>
    RWGltf_GltfRootElement_ExtensionsUsed: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsUsed: 17>
    RWGltf_GltfRootElement_Images: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Images: 16>
    RWGltf_GltfRootElement_Materials: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Materials: 9>
    RWGltf_GltfRootElement_Meshes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Meshes: 4>
    RWGltf_GltfRootElement_NB: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB: 19>
    RWGltf_GltfRootElement_NB_MANDATORY: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>
    RWGltf_GltfRootElement_Nodes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Nodes: 3>
    RWGltf_GltfRootElement_Programs: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Programs: 10>
    RWGltf_GltfRootElement_Samplers: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Samplers: 11>
    RWGltf_GltfRootElement_Scene: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scene: 2>
    RWGltf_GltfRootElement_Scenes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scenes: 1>
    RWGltf_GltfRootElement_Shaders: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Shaders: 12>
    RWGltf_GltfRootElement_Skins: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Skins: 13>
    RWGltf_GltfRootElement_Techniques: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Techniques: 14>
    RWGltf_GltfRootElement_Textures: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Textures: 15>
    __entries: dict # value = {'RWGltf_GltfRootElement_Asset': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Asset: 0>, None), 'RWGltf_GltfRootElement_Scenes': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scenes: 1>, None), 'RWGltf_GltfRootElement_Scene': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scene: 2>, None), 'RWGltf_GltfRootElement_Nodes': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Nodes: 3>, None), 'RWGltf_GltfRootElement_Meshes': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Meshes: 4>, None), 'RWGltf_GltfRootElement_Accessors': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Accessors: 5>, None), 'RWGltf_GltfRootElement_BufferViews': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_BufferViews: 6>, None), 'RWGltf_GltfRootElement_Buffers': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Buffers: 7>, None), 'RWGltf_GltfRootElement_NB_MANDATORY': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>, None), 'RWGltf_GltfRootElement_Animations': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>, None), 'RWGltf_GltfRootElement_Materials': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Materials: 9>, None), 'RWGltf_GltfRootElement_Programs': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Programs: 10>, None), 'RWGltf_GltfRootElement_Samplers': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Samplers: 11>, None), 'RWGltf_GltfRootElement_Shaders': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Shaders: 12>, None), 'RWGltf_GltfRootElement_Skins': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Skins: 13>, None), 'RWGltf_GltfRootElement_Techniques': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Techniques: 14>, None), 'RWGltf_GltfRootElement_Textures': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Textures: 15>, None), 'RWGltf_GltfRootElement_Images': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_Images: 16>, None), 'RWGltf_GltfRootElement_ExtensionsUsed': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsUsed: 17>, None), 'RWGltf_GltfRootElement_ExtensionsRequired': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsRequired: 18>, None), 'RWGltf_GltfRootElement_NB': (<RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB: 19>, None)}
    __members__: dict # value = {'RWGltf_GltfRootElement_Asset': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Asset: 0>, 'RWGltf_GltfRootElement_Scenes': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scenes: 1>, 'RWGltf_GltfRootElement_Scene': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scene: 2>, 'RWGltf_GltfRootElement_Nodes': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Nodes: 3>, 'RWGltf_GltfRootElement_Meshes': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Meshes: 4>, 'RWGltf_GltfRootElement_Accessors': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Accessors: 5>, 'RWGltf_GltfRootElement_BufferViews': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_BufferViews: 6>, 'RWGltf_GltfRootElement_Buffers': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Buffers: 7>, 'RWGltf_GltfRootElement_NB_MANDATORY': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>, 'RWGltf_GltfRootElement_Animations': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>, 'RWGltf_GltfRootElement_Materials': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Materials: 9>, 'RWGltf_GltfRootElement_Programs': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Programs: 10>, 'RWGltf_GltfRootElement_Samplers': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Samplers: 11>, 'RWGltf_GltfRootElement_Shaders': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Shaders: 12>, 'RWGltf_GltfRootElement_Skins': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Skins: 13>, 'RWGltf_GltfRootElement_Techniques': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Techniques: 14>, 'RWGltf_GltfRootElement_Textures': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Textures: 15>, 'RWGltf_GltfRootElement_Images': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Images: 16>, 'RWGltf_GltfRootElement_ExtensionsUsed': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsUsed: 17>, 'RWGltf_GltfRootElement_ExtensionsRequired': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsRequired: 18>, 'RWGltf_GltfRootElement_NB': <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB: 19>}
    pass
class RWGltf_GltfSceneNodeMap():
    """
    Indexed map of scene nodes with custom search algorithm.
    """
    def FindIndex(self,theNodeId : OCP.TCollection.TCollection_AsciiString) -> int: 
        """
        Find index from document node string identifier.
        """
    def __init__(self) -> None: ...
    pass
class RWGltf_GltfSharedIStream():
    """
    The interface for shared file.
    """
    def __init__(self) -> None: ...
    @property
    def Path(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Path.setter
    def Path(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    pass
class RWGltf_MaterialCommon(OCP.Standard.Standard_Transient):
    """
    glTF 1.0 format common (obsolete) material definition.
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
        Returns a type descriptor about this object.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    @property
    def AmbientColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @AmbientColor.setter
    def AmbientColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def DiffuseColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @DiffuseColor.setter
    def DiffuseColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def EmissiveColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @EmissiveColor.setter
    def EmissiveColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def Id(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Id.setter
    def Id(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def Name(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Name.setter
    def Name(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def Shininess(self) -> float:
        """
        :type: float
        """
    @Shininess.setter
    def Shininess(self, arg0: float) -> None:
        pass
    @property
    def SpecularColor(self) -> OCP.Quantity.Quantity_Color:
        """
        :type: OCP.Quantity.Quantity_Color
        """
    @SpecularColor.setter
    def SpecularColor(self, arg0: OCP.Quantity.Quantity_Color) -> None:
        pass
    @property
    def Transparency(self) -> float:
        """
        :type: float
        """
    @Transparency.setter
    def Transparency(self, arg0: float) -> None:
        pass
    pass
class RWGltf_MaterialMetallicRoughness(OCP.Standard.Standard_Transient):
    """
    glTF 2.0 format PBR material definition.
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
        Returns a type descriptor about this object.
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
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def get_type_descriptor_s() -> OCP.Standard.Standard_Type: 
        """
        Returns type descriptor of Standard_Transient class
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    @property
    def AlphaCutOff(self) -> float:
        """
        :type: float
        """
    @AlphaCutOff.setter
    def AlphaCutOff(self, arg0: float) -> None:
        pass
    @property
    def AlphaMode(self) -> RWGltf_GltfAlphaMode:
        """
        :type: RWGltf_GltfAlphaMode
        """
    @AlphaMode.setter
    def AlphaMode(self, arg0: RWGltf_GltfAlphaMode) -> None:
        pass
    @property
    def BaseColor(self) -> OCP.Quantity.Quantity_ColorRGBA:
        """
        :type: OCP.Quantity.Quantity_ColorRGBA
        """
    @BaseColor.setter
    def BaseColor(self, arg0: OCP.Quantity.Quantity_ColorRGBA) -> None:
        pass
    @property
    def EmissiveFactor(self) -> OCP.Graphic3d.Graphic3d_Vec3:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec3
        """
    @EmissiveFactor.setter
    def EmissiveFactor(self, arg0: OCP.Graphic3d.Graphic3d_Vec3) -> None:
        pass
    @property
    def Id(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Id.setter
    def Id(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def IsDoubleSided(self) -> bool:
        """
        :type: bool
        """
    @IsDoubleSided.setter
    def IsDoubleSided(self, arg0: bool) -> None:
        pass
    @property
    def Metallic(self) -> float:
        """
        :type: float
        """
    @Metallic.setter
    def Metallic(self, arg0: float) -> None:
        pass
    @property
    def Name(self) -> OCP.TCollection.TCollection_AsciiString:
        """
        :type: OCP.TCollection.TCollection_AsciiString
        """
    @Name.setter
    def Name(self, arg0: OCP.TCollection.TCollection_AsciiString) -> None:
        pass
    @property
    def Roughness(self) -> float:
        """
        :type: float
        """
    @Roughness.setter
    def Roughness(self, arg0: float) -> None:
        pass
    pass
class RWGltf_PrimitiveArrayReader(OCP.Standard.Standard_Transient):
    """
    Interface for reading primitive array from glTF buffer.
    """
    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: 
        """
        Return transformation from glTF to OCCT coordinate system.
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
    def ErrorPrefix(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return prefix for reporting issues.
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
    def Load(self,theMesh : RWGltf_GltfLatePrimitiveArray) -> OCP.Poly.Poly_Triangulation: 
        """
        Load primitive array.
        """
    def SetCoordinateSystemConverter(self,theConverter : RWMesh_CoordinateSystemConverter) -> None: 
        """
        Set transformation from glTF to OCCT coordinate system.
        """
    def SetErrorPrefix(self,theErrPrefix : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set prefix for reporting issues.
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
class RWGltf_TriangulationReader(RWGltf_PrimitiveArrayReader, OCP.Standard.Standard_Transient):
    """
    RWGltf_PrimitiveArrayReader implementation creating Poly_Triangulation.
    """
    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter: 
        """
        Return transformation from glTF to OCCT coordinate system.
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
    def ErrorPrefix(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return prefix for reporting issues.
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
    def Load(self,theMesh : RWGltf_GltfLatePrimitiveArray) -> OCP.Poly.Poly_Triangulation: 
        """
        Load primitive array.
        """
    def SetCoordinateSystemConverter(self,theConverter : RWMesh_CoordinateSystemConverter) -> None: 
        """
        Set transformation from glTF to OCCT coordinate system.
        """
    def SetErrorPrefix(self,theErrPrefix : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set prefix for reporting issues.
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
class RWGltf_WriterTrsfFormat():
    """
    Transformation format.

    Members:

      RWGltf_WriterTrsfFormat_Compact

      RWGltf_WriterTrsfFormat_Mat4

      RWGltf_WriterTrsfFormat_TRS
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
    RWGltf_WriterTrsfFormat_Compact: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Compact: 0>
    RWGltf_WriterTrsfFormat_Mat4: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Mat4: 1>
    RWGltf_WriterTrsfFormat_TRS: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_TRS: 2>
    __entries: dict # value = {'RWGltf_WriterTrsfFormat_Compact': (<RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Compact: 0>, None), 'RWGltf_WriterTrsfFormat_Mat4': (<RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Mat4: 1>, None), 'RWGltf_WriterTrsfFormat_TRS': (<RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_TRS: 2>, None)}
    __members__: dict # value = {'RWGltf_WriterTrsfFormat_Compact': <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Compact: 0>, 'RWGltf_WriterTrsfFormat_Mat4': <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Mat4: 1>, 'RWGltf_WriterTrsfFormat_TRS': <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_TRS: 2>}
    pass
def RWGltf_GltfParseAccessorType(theType : str) -> RWGltf_GltfAccessorLayout:
    """
    Parse GltfAccessorLayout from string.
    """
def RWGltf_GltfParseAlphaMode(theType : str) -> RWGltf_GltfAlphaMode:
    """
    Parse RWGltf_GltfAlphaMode from string.
    """
def RWGltf_GltfParseAttribType(theType : str) -> RWGltf_GltfArrayType:
    """
    Parse GltfArrayType from string.
    """
def RWGltf_GltfRootElementName(theElem : RWGltf_GltfRootElement) -> str:
    """
    Root elements within glTF JSON document - names array.
    """
RWGltf_GltfAccessorCompType_Float32: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Float32: 5126>
RWGltf_GltfAccessorCompType_Int16: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int16: 5122>
RWGltf_GltfAccessorCompType_Int8: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int8: 5120>
RWGltf_GltfAccessorCompType_UInt16: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt16: 5123>
RWGltf_GltfAccessorCompType_UInt32: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt32: 5125>
RWGltf_GltfAccessorCompType_UInt8: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt8: 5121>
RWGltf_GltfAccessorCompType_UNKNOWN: OCP.RWGltf.RWGltf_GltfAccessorCompType # value = <RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UNKNOWN: 0>
RWGltf_GltfAccessorLayout_Mat2: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat2: 5>
RWGltf_GltfAccessorLayout_Mat3: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat3: 6>
RWGltf_GltfAccessorLayout_Mat4: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat4: 7>
RWGltf_GltfAccessorLayout_Scalar: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Scalar: 1>
RWGltf_GltfAccessorLayout_UNKNOWN: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_UNKNOWN: 0>
RWGltf_GltfAccessorLayout_Vec2: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec2: 2>
RWGltf_GltfAccessorLayout_Vec3: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec3: 3>
RWGltf_GltfAccessorLayout_Vec4: OCP.RWGltf.RWGltf_GltfAccessorLayout # value = <RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec4: 4>
RWGltf_GltfAlphaMode_Blend: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Blend: 2>
RWGltf_GltfAlphaMode_Mask: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Mask: 1>
RWGltf_GltfAlphaMode_Opaque: OCP.RWGltf.RWGltf_GltfAlphaMode # value = <RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Opaque: 0>
RWGltf_GltfArrayType_Color: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color: 4>
RWGltf_GltfArrayType_Indices: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices: 1>
RWGltf_GltfArrayType_Joint: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint: 7>
RWGltf_GltfArrayType_Normal: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal: 3>
RWGltf_GltfArrayType_Position: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Position: 2>
RWGltf_GltfArrayType_TCoord0: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0: 5>
RWGltf_GltfArrayType_TCoord1: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1: 6>
RWGltf_GltfArrayType_UNKNOWN: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN: 0>
RWGltf_GltfArrayType_Weight: OCP.RWGltf.RWGltf_GltfArrayType # value = <RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight: 8>
RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: 34962>
RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: 34963>
RWGltf_GltfBufferViewTarget_UNKNOWN: OCP.RWGltf.RWGltf_GltfBufferViewTarget # value = <RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_UNKNOWN: 0>
RWGltf_GltfPrimitiveMode_LineLoop: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineLoop: 2>
RWGltf_GltfPrimitiveMode_LineStrip: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineStrip: 3>
RWGltf_GltfPrimitiveMode_Lines: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Lines: 1>
RWGltf_GltfPrimitiveMode_Points: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Points: 0>
RWGltf_GltfPrimitiveMode_TriangleFan: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleFan: 6>
RWGltf_GltfPrimitiveMode_TriangleStrip: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleStrip: 5>
RWGltf_GltfPrimitiveMode_Triangles: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Triangles: 4>
RWGltf_GltfPrimitiveMode_UNKNOWN: OCP.RWGltf.RWGltf_GltfPrimitiveMode # value = <RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_UNKNOWN: -1>
RWGltf_GltfRootElement_Accessors: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Accessors: 5>
RWGltf_GltfRootElement_Animations: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>
RWGltf_GltfRootElement_Asset: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Asset: 0>
RWGltf_GltfRootElement_BufferViews: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_BufferViews: 6>
RWGltf_GltfRootElement_Buffers: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Buffers: 7>
RWGltf_GltfRootElement_ExtensionsRequired: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsRequired: 18>
RWGltf_GltfRootElement_ExtensionsUsed: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsUsed: 17>
RWGltf_GltfRootElement_Images: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Images: 16>
RWGltf_GltfRootElement_Materials: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Materials: 9>
RWGltf_GltfRootElement_Meshes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Meshes: 4>
RWGltf_GltfRootElement_NB: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB: 19>
RWGltf_GltfRootElement_NB_MANDATORY: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY: 8>
RWGltf_GltfRootElement_Nodes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Nodes: 3>
RWGltf_GltfRootElement_Programs: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Programs: 10>
RWGltf_GltfRootElement_Samplers: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Samplers: 11>
RWGltf_GltfRootElement_Scene: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scene: 2>
RWGltf_GltfRootElement_Scenes: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scenes: 1>
RWGltf_GltfRootElement_Shaders: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Shaders: 12>
RWGltf_GltfRootElement_Skins: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Skins: 13>
RWGltf_GltfRootElement_Techniques: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Techniques: 14>
RWGltf_GltfRootElement_Textures: OCP.RWGltf.RWGltf_GltfRootElement # value = <RWGltf_GltfRootElement.RWGltf_GltfRootElement_Textures: 15>
RWGltf_WriterTrsfFormat_Compact: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Compact: 0>
RWGltf_WriterTrsfFormat_LOWER = 0
RWGltf_WriterTrsfFormat_Mat4: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Mat4: 1>
RWGltf_WriterTrsfFormat_TRS: OCP.RWGltf.RWGltf_WriterTrsfFormat # value = <RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_TRS: 2>
RWGltf_WriterTrsfFormat_UPPER = 2
