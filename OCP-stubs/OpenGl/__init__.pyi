import OCP.OpenGl
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.Font
import OCP.Bnd
import OCP.Standard
import OCP.Quantity
import OCP.TColStd
import OCP.TCollection
import io
import OCP.Message
import OCP.Image
import OCP.gp
import OCP.Graphic3d.Graphic3d_Camera
import OCP.Graphic3d
import OCP.Aspect
import OCP.TopLoc
__all__  = [
"NSOpenGLContext",
"OpenGl_ArbDbg",
"OpenGl_ArbFBO",
"OpenGl_ArbFBOBlit",
"OpenGl_ArbIns",
"OpenGl_ArbSamplerObject",
"OpenGl_ArbTBO",
"OpenGl_ArbTexBindless",
"OpenGl_Element",
"OpenGl_AspectsProgram",
"OpenGl_AspectsSprite",
"OpenGl_AspectsTextureSet",
"OpenGl_BVHTriangulation3f",
"OpenGl_PrimitiveArray",
"OpenGl_CappingAlgo",
"OpenGl_Resource",
"OpenGl_Caps",
"OpenGl_Clipping",
"OpenGl_ClippingIterator",
"OpenGl_ClippingState",
"OpenGl_ColorFormats",
"OpenGl_Context",
"OpenGl_Aspects",
"OpenGl_ElementNode",
"OpenGl_ExtGS",
"OpenGl_FeatureFlag",
"OpenGl_Flipper",
"OpenGl_Font",
"OpenGl_FrameBuffer",
"OpenGl_FrameStats",
"OpenGl_FrameStatsPrs",
"OpenGl_GlCore11",
"OpenGl_GlCore11Fwd",
"OpenGl_GlCore12",
"OpenGl_GlCore12Fwd",
"OpenGl_GlCore13",
"OpenGl_GlCore13Fwd",
"OpenGl_GlCore14",
"OpenGl_GlCore14Fwd",
"OpenGl_GlCore15",
"OpenGl_GlCore15Fwd",
"OpenGl_GlCore20",
"OpenGl_GlCore20Fwd",
"OpenGl_GlCore21",
"OpenGl_GlCore21Fwd",
"OpenGl_GlCore30",
"OpenGl_GlCore30Fwd",
"OpenGl_GlCore31",
"OpenGl_GlCore31Back",
"OpenGl_GlCore32",
"OpenGl_GlCore32Back",
"OpenGl_GlCore33",
"OpenGl_GlCore33Back",
"OpenGl_GlCore40",
"OpenGl_GlCore40Back",
"OpenGl_GlCore41",
"OpenGl_GlCore41Back",
"OpenGl_GlCore42",
"OpenGl_GlCore42Back",
"OpenGl_GlCore43",
"OpenGl_GlCore43Back",
"OpenGl_GlCore44",
"OpenGl_GlCore44Back",
"OpenGl_GlCore45",
"OpenGl_GlCore45Back",
"OpenGl_GlFunctions",
"OpenGl_GraphicDriver",
"OpenGl_Group",
"OpenGl_HaltonSampler",
"OpenGl_VertexBuffer",
"OpenGl_LayerFilter",
"OpenGl_StateInterface",
"OpenGl_LineAttributes",
"OpenGl_ListOfStructure",
"OpenGl_Material",
"OpenGl_MaterialCommon",
"OpenGl_MaterialFlag",
"OpenGl_MaterialPBR",
"OpenGl_MaterialState",
"OpenGl_Matrix",
"OpenGl_ModelWorldState",
"OpenGl_NamedResource",
"OpenGl_OitState",
"OpenGl_PBREnvironment",
"OpenGl_Texture",
"OpenGl_BackgroundArray",
"OpenGl_ProgramOptions",
"OpenGl_ProjectionState",
"OpenGl_RaytraceLight",
"OpenGl_RaytraceMaterial",
"OpenGl_RenderFilter",
"OpenGl_CappingPlaneResource",
"OpenGl_Sampler",
"OpenGl_SetOfPrograms",
"OpenGl_SetOfShaderPrograms",
"OpenGl_SetterInterface",
"OpenGl_ShaderList",
"OpenGl_ShaderManager",
"OpenGl_ShaderObject",
"OpenGl_ShaderProgram",
"OpenGl_ShaderProgramDumpLevel",
"OpenGl_ShaderProgramList",
"OpenGl_ShaderUniformLocation",
"OpenGl_StateCounter",
"OpenGl_LightSourceState",
"OpenGl_StateVariable",
"OpenGl_StencilTest",
"OpenGl_Structure",
"OpenGl_StructureShadow",
"OpenGl_Text",
"OpenGl_TextBuilder",
"OpenGl_PointSprite",
"OpenGl_TextureBufferArb",
"OpenGl_TextureFormat",
"OpenGl_TextureFormatSelector_GLbyte",
"OpenGl_TextureFormatSelector_GLfloat",
"OpenGl_TextureFormatSelector_GLint",
"OpenGl_TextureFormatSelector_GLshort",
"OpenGl_TextureFormatSelector_GLubyte",
"OpenGl_TextureFormatSelector_GLuint",
"OpenGl_TextureFormatSelector_GLushort",
"OpenGl_TextureSet",
"OpenGl_TextureSetPairIterator",
"OpenGl_TileSampler",
"OpenGl_TriangleSet",
"OpenGl_UniformStateType",
"OpenGl_IndexBuffer",
"OpenGl_VertexBufferCompat",
"OpenGl_View",
"OpenGl_Window",
"OpenGl_Workspace",
"OpenGl_WorldViewState",
"OpenGL_OIT_STATE",
"OpenGl_CLIP_PLANES_STATE",
"OpenGl_FeatureInCore",
"OpenGl_FeatureInExtensions",
"OpenGl_FeatureNotAvailable",
"OpenGl_LF_All",
"OpenGl_LF_Bottom",
"OpenGl_LF_RayTracable",
"OpenGl_LF_Upper",
"OpenGl_LIGHT_SOURCES_STATE",
"OpenGl_MATERIAL_STATE",
"OpenGl_MODEL_WORLD_STATE",
"OpenGl_MaterialFlag_Back",
"OpenGl_MaterialFlag_Front",
"OpenGl_OCCT_ALPHA_CUTOFF",
"OpenGl_OCCT_COLOR",
"OpenGl_OCCT_COMMON_BACK_MATERIAL",
"OpenGl_OCCT_COMMON_FRONT_MATERIAL",
"OpenGl_OCCT_DISTINGUISH_MODE",
"OpenGl_OCCT_LINE_FEATHER",
"OpenGl_OCCT_LINE_STIPPLE_FACTOR",
"OpenGl_OCCT_LINE_STIPPLE_PATTERN",
"OpenGl_OCCT_LINE_WIDTH",
"OpenGl_OCCT_NB_SPEC_IBL_LEVELS",
"OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES",
"OpenGl_OCCT_OIT_DEPTH_FACTOR",
"OpenGl_OCCT_OIT_OUTPUT",
"OpenGl_OCCT_ORTHO_SCALE",
"OpenGl_OCCT_PBR_BACK_MATERIAL",
"OpenGl_OCCT_PBR_FRONT_MATERIAL",
"OpenGl_OCCT_POINT_SIZE",
"OpenGl_OCCT_QUAD_MODE_STATE",
"OpenGl_OCCT_SILHOUETTE_THICKNESS",
"OpenGl_OCCT_TEXTURE_ENABLE",
"OpenGl_OCCT_TEXTURE_TRSF2D",
"OpenGl_OCCT_VIEWPORT",
"OpenGl_OCCT_WIREFRAME_COLOR",
"OpenGl_OCC_CLIP_PLANE_CHAINS",
"OpenGl_OCC_CLIP_PLANE_COUNT",
"OpenGl_OCC_CLIP_PLANE_EQUATIONS",
"OpenGl_OCC_LIGHT_AMBIENT",
"OpenGl_OCC_LIGHT_SOURCE_COUNT",
"OpenGl_OCC_LIGHT_SOURCE_PARAMS",
"OpenGl_OCC_LIGHT_SOURCE_TYPES",
"OpenGl_OCC_MODEL_WORLD_MATRIX",
"OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE",
"OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE",
"OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE",
"OpenGl_OCC_PROJECTION_MATRIX",
"OpenGl_OCC_PROJECTION_MATRIX_INVERSE",
"OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE",
"OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE",
"OpenGl_OCC_WORLD_VIEW_MATRIX",
"OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE",
"OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE",
"OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE",
"OpenGl_PO_AlphaTest",
"OpenGl_PO_ClipChains",
"OpenGl_PO_ClipPlanes1",
"OpenGl_PO_ClipPlanes2",
"OpenGl_PO_ClipPlanesN",
"OpenGl_PO_HasTextures",
"OpenGl_PO_IsPoint",
"OpenGl_PO_MeshEdges",
"OpenGl_PO_NB",
"OpenGl_PO_NeedsGeomShader",
"OpenGl_PO_PointSimple",
"OpenGl_PO_PointSprite",
"OpenGl_PO_PointSpriteA",
"OpenGl_PO_StippleLine",
"OpenGl_PO_TextureEnv",
"OpenGl_PO_TextureNormal",
"OpenGl_PO_TextureRGB",
"OpenGl_PO_VertColor",
"OpenGl_PO_WriteOit",
"OpenGl_PROJECTION_STATE",
"OpenGl_RenderFilter_Empty",
"OpenGl_RenderFilter_FillModeOnly",
"OpenGl_RenderFilter_NonRaytraceableOnly",
"OpenGl_RenderFilter_OpaqueOnly",
"OpenGl_RenderFilter_TransparentOnly",
"OpenGl_SURF_DETAIL_STATE",
"OpenGl_ShaderProgramDumpLevel_Full",
"OpenGl_ShaderProgramDumpLevel_Off",
"OpenGl_ShaderProgramDumpLevel_Short",
"OpenGl_UniformStateType_NB",
"OpenGl_WORLD_VIEW_STATE"
]
class NSOpenGLContext():
    pass
class OpenGl_ArbDbg():
    """
    Debug context routines
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbFBO():
    """
    FBO is available on OpenGL 2.0+ hardware
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbFBOBlit():
    """
    FBO blit is available in OpenGL 3.0+. Moved out from OpenGl_ArbFBO since it is unavailable in OpenGL ES 2.0.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbIns():
    """
    Instancing is available on OpenGL 3.0+ hardware (in core since OpenGL 3.1 or GL_ARB_draw_instanced extension).
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbSamplerObject():
    """
    Provide Sampler Object functionality (texture parameters stored independently from texture itself). Available since OpenGL 3.3+ (GL_ARB_sampler_objects extension) and OpenGL ES 3.0+.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbTBO():
    """
    TBO is available on OpenGL 3.0+ and OpenGL ES 3.2+ hardware
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ArbTexBindless():
    """
    Provides bindless textures. This extension allows OpenGL applications to access texture objects in shaders without first binding each texture to one of a limited number of texture image units.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_Element():
    """
    Base interface for drawable elements.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        Release GPU resources. Pointer to the context is used because this method might be called when the context is already being destroyed and usage of a handle would be unsafe
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        None
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_AspectsProgram():
    """
    OpenGl resources for custom shading program.
    """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Release resource.
        """
    def ShaderProgram(self,theCtx : OpenGl_Context,theShader : OCP.Graphic3d.Graphic3d_ShaderProgram) -> OpenGl_ShaderProgram: 
        """
        Return shading program.
        """
    def UpdateRediness(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Update shader resource up-to-date state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_AspectsSprite():
    """
    OpenGl resources for custom point sprites.
    """
    def HasPointSprite(self,theCtx : OpenGl_Context,theAspects : OCP.Graphic3d.Graphic3d_Aspects) -> bool: 
        """
        Return TRUE if OpenGl point sprite resource defines texture.
        """
    def Invalidate(self) -> None: 
        """
        Invalidate resource state.
        """
    def IsDisplayListSprite(self,theCtx : OpenGl_Context,theAspects : OCP.Graphic3d.Graphic3d_Aspects) -> bool: 
        """
        Return TRUE if OpenGl point sprite resource defined by obsolete Display List (bitmap).
        """
    def IsReady(self) -> bool: 
        """
        Return TRUE if resource is up-to-date.
        """
    def MarkerSize(self) -> float: 
        """
        None
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Release texture resource.
        """
    def Sprite(self,theCtx : OpenGl_Context,theAspects : OCP.Graphic3d.Graphic3d_Aspects,theIsAlphaSprite : bool) -> OpenGl_PointSprite: 
        """
        Return sprite.
        """
    def UpdateRediness(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Update texture resource up-to-date state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_AspectsTextureSet():
    """
    OpenGl resources for custom textures.
    """
    def Invalidate(self) -> None: 
        """
        Invalidate resource state.
        """
    def IsReady(self) -> bool: 
        """
        Return TRUE if resource is up-to-date.
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Release texture resource.
        """
    def TextureSet(self,theCtx : OpenGl_Context,theAspect : OCP.Graphic3d.Graphic3d_Aspects,theSprite : OpenGl_PointSprite,theSpriteA : OpenGl_PointSprite,theToHighlight : bool) -> OpenGl_TextureSet: 
        """
        Return textures array.
        """
    def UpdateRediness(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Update texture resource up-to-date state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_BVHTriangulation3f():
    """
    Triangulation as an example of BVH primitive set.
    """
    def Box(self,theIndex : int) -> Any: 
        """
        Returns AABB of the given triangle.
        """
    def Center(self,theIndex : int,theAxis : int) -> float: 
        """
        Returns centroid position along the given axis.
        """
    def Size(self) -> int: 
        """
        Returns total number of triangles.
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Performs transposing the two given triangles in the set.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBuilder : Any) -> None: ...
    pass
class OpenGl_PrimitiveArray(OpenGl_Element):
    """
    Class for rendering of arbitrary primitive array.
    """
    def Attributes(self) -> OCP.Graphic3d.Graphic3d_Buffer: 
        """
        Returns attributes array
        """
    def AttributesVbo(self) -> OpenGl_VertexBuffer: 
        """
        Returns attributes VBO.
        """
    def Bounds(self) -> OCP.Graphic3d.Graphic3d_BoundBuffer: 
        """
        Returns bounds array
        """
    def DrawMode(self) -> int: 
        """
        Returns primitive type (GL_LINES, GL_TRIANGLES and others)
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetUID(self) -> int: 
        """
        Returns unique ID of primitive array.
        """
    def IndexVbo(self) -> OpenGl_VertexBuffer: 
        """
        Returns index VBO.
        """
    def Indices(self) -> OCP.Graphic3d.Graphic3d_IndexBuffer: 
        """
        Returns indices array
        """
    def InitBuffers(self,theContext : OpenGl_Context,theType : OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theAttribs : OCP.Graphic3d.Graphic3d_Buffer,theBounds : OCP.Graphic3d.Graphic3d_BoundBuffer) -> None: 
        """
        Initialize indices, attributes and bounds with new data.
        """
    def Invalidate(self) -> None: 
        """
        Invalidate VBO content without destruction.
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation.
        """
    def IsInitialized(self) -> bool: 
        """
        Return true if VBOs initialization has been performed. VBO initialization is performed during first Render() call. Notice that this flag does not indicate VBOs validity.
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        Release OpenGL resources (VBOs)
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Render primitives to the window
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    @overload
    def __init__(self,theDriver : OpenGl_GraphicDriver,theType : OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theAttribs : OCP.Graphic3d.Graphic3d_Buffer,theBounds : OCP.Graphic3d.Graphic3d_BoundBuffer) -> None: ...
    @overload
    def __init__(self,theDriver : OpenGl_GraphicDriver) -> None: ...
    DRAW_MODE_NONE = -1
    pass
class OpenGl_CappingAlgo():
    """
    Capping surface rendering algorithm.
    """
    @staticmethod
    def RenderCapping_s(theWorkspace : OpenGl_Workspace,theStructure : OpenGl_Structure) -> None: 
        """
        Draw capping surfaces by OpenGl for the clipping planes enabled in current context state. Depth buffer must be generated for the passed groups.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_Resource(OCP.Standard.Standard_Transient):
    """
    Interface for OpenGl resource with following meaning: - object can be constructed at any time; - should be explicitly Initialized within active OpenGL context; - should be explicitly Released within active OpenGL context (virtual Release() method); - can be destroyed at any time. Destruction of object with unreleased GPU resources will cause leaks which will be ignored in release mode and will immediately stop program execution in debug mode using assert.Interface for OpenGl resource with following meaning: - object can be constructed at any time; - should be explicitly Initialized within active OpenGL context; - should be explicitly Released within active OpenGL context (virtual Release() method); - can be destroyed at any time. Destruction of object with unreleased GPU resources will cause leaks which will be ignored in release mode and will immediately stop program execution in debug mode using assert.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
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
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Release GPU resources. Notice that implementation should be SAFE for several consecutive calls (thus should invalidate internal structures / ids to avoid multiple-free errors).
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
class OpenGl_Caps(OCP.Standard.Standard_Transient):
    """
    Class to define graphic driver capabilities. Notice that these options will be ignored if particular functionality does not provided by GL driverClass to define graphic driver capabilities. Notice that these options will be ignored if particular functionality does not provided by GL driver
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
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    @property
    def buffersNoSwap(self) -> bool:
        """
        :type: bool
        """
    @buffersNoSwap.setter
    def buffersNoSwap(self, arg0: bool) -> None:
        pass
    @property
    def compressedTexturesDisable(self) -> bool:
        """
        :type: bool
        """
    @compressedTexturesDisable.setter
    def compressedTexturesDisable(self, arg0: bool) -> None:
        pass
    @property
    def contextCompatible(self) -> bool:
        """
        :type: bool
        """
    @contextCompatible.setter
    def contextCompatible(self, arg0: bool) -> None:
        pass
    @property
    def contextDebug(self) -> bool:
        """
        :type: bool
        """
    @contextDebug.setter
    def contextDebug(self, arg0: bool) -> None:
        pass
    @property
    def contextMajorVersionUpper(self) -> int:
        """
        :type: int
        """
    @contextMajorVersionUpper.setter
    def contextMajorVersionUpper(self, arg0: int) -> None:
        pass
    @property
    def contextMinorVersionUpper(self) -> int:
        """
        :type: int
        """
    @contextMinorVersionUpper.setter
    def contextMinorVersionUpper(self, arg0: int) -> None:
        pass
    @property
    def contextNoAccel(self) -> bool:
        """
        :type: bool
        """
    @contextNoAccel.setter
    def contextNoAccel(self, arg0: bool) -> None:
        pass
    @property
    def contextNoExtensions(self) -> bool:
        """
        :type: bool
        """
    @contextNoExtensions.setter
    def contextNoExtensions(self, arg0: bool) -> None:
        pass
    @property
    def contextStereo(self) -> bool:
        """
        :type: bool
        """
    @contextStereo.setter
    def contextStereo(self, arg0: bool) -> None:
        pass
    @property
    def contextSyncDebug(self) -> bool:
        """
        :type: bool
        """
    @contextSyncDebug.setter
    def contextSyncDebug(self, arg0: bool) -> None:
        pass
    @property
    def ffpEnable(self) -> bool:
        """
        :type: bool
        """
    @ffpEnable.setter
    def ffpEnable(self, arg0: bool) -> None:
        pass
    @property
    def glslDumpLevel(self) -> OpenGl_ShaderProgramDumpLevel:
        """
        :type: OpenGl_ShaderProgramDumpLevel
        """
    @glslDumpLevel.setter
    def glslDumpLevel(self, arg0: OpenGl_ShaderProgramDumpLevel) -> None:
        pass
    @property
    def glslWarnings(self) -> bool:
        """
        :type: bool
        """
    @glslWarnings.setter
    def glslWarnings(self, arg0: bool) -> None:
        pass
    @property
    def isTopDownTextureUV(self) -> bool:
        """
        :type: bool
        """
    @isTopDownTextureUV.setter
    def isTopDownTextureUV(self, arg0: bool) -> None:
        pass
    @property
    def keepArrayData(self) -> bool:
        """
        :type: bool
        """
    @keepArrayData.setter
    def keepArrayData(self, arg0: bool) -> None:
        pass
    @property
    def pntSpritesDisable(self) -> bool:
        """
        :type: bool
        """
    @pntSpritesDisable.setter
    def pntSpritesDisable(self, arg0: bool) -> None:
        pass
    @property
    def sRGBDisable(self) -> bool:
        """
        :type: bool
        """
    @sRGBDisable.setter
    def sRGBDisable(self, arg0: bool) -> None:
        pass
    @property
    def suppressExtraMsg(self) -> bool:
        """
        :type: bool
        """
    @suppressExtraMsg.setter
    def suppressExtraMsg(self, arg0: bool) -> None:
        pass
    @property
    def swapInterval(self) -> int:
        """
        :type: int
        """
    @swapInterval.setter
    def swapInterval(self, arg0: int) -> None:
        pass
    @property
    def usePolygonMode(self) -> bool:
        """
        :type: bool
        """
    @usePolygonMode.setter
    def usePolygonMode(self, arg0: bool) -> None:
        pass
    @property
    def useSystemBuffer(self) -> bool:
        """
        :type: bool
        """
    @useSystemBuffer.setter
    def useSystemBuffer(self, arg0: bool) -> None:
        pass
    @property
    def vboDisable(self) -> bool:
        """
        :type: bool
        """
    @vboDisable.setter
    def vboDisable(self, arg0: bool) -> None:
        pass
    pass
class OpenGl_Clipping():
    """
    This class contains logics related to tracking and modification of clipping plane state for particular OpenGl context. It contains information about enabled clipping planes and provides method to change clippings in context. The methods should be executed within OpenGl context associated with instance of this class.
    """
    def CappedChain(self) -> OCP.Graphic3d.Graphic3d_ClipPlane: 
        """
        Chain which is either temporary disabled or the only one enabled for Capping algorithm.
        """
    def CappedSubPlane(self) -> int: 
        """
        Sub-plane index within filtered Chain; positive number for DisableAllExcept and negative for EnableAllExcept.
        """
    def DisableAllExcept(self,theChain : OCP.Graphic3d.Graphic3d_ClipPlane,theSubPlaneIndex : int) -> None: 
        """
        Temporarily disable all planes except specified one for Capping algorithm. Does not affect already disabled planes.
        """
    def DisableGlobal(self) -> None: 
        """
        Temporarily disable all planes from the global (view) list, keep only local (object) list.
        """
    def EnableAllExcept(self,theChain : OCP.Graphic3d.Graphic3d_ClipPlane,theSubPlaneIndex : int) -> None: 
        """
        Enable back planes disabled by ::DisableAllExcept() for Capping algorithm. Keeps only specified plane enabled.
        """
    def HasClippingChains(self) -> bool: 
        """
        Return TRUE if there are clipping chains in the list (defining more than 1 sub-plane)
        """
    def HasDisabled(self) -> bool: 
        """
        Return true if some clipping planes have been temporarily disabled.
        """
    def Init(self) -> None: 
        """
        Initialize.
        """
    def IsCappingDisableAllExcept(self) -> bool: 
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are temporarily disabled except currently processed one.
        """
    def IsCappingEnableAllExcept(self) -> bool: 
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are enabled except currently rendered one.
        """
    def IsCappingFilterOn(self) -> bool: 
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are temporarily disabled except currently processed one.
        """
    def IsCappingOn(self) -> bool: 
        """
        Returns true if there are enabled capping planes
        """
    def IsClippingOrCappingOn(self) -> bool: 
        """
        Returns true if there are enabled clipping or capping planes
        """
    def NbClippingOrCappingOn(self) -> int: 
        """
        Returns number of enabled clipping + capping planes
        """
    def Reset(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Setup list of global (for entire view) clipping planes and clears local plane list if it was not released before.
        """
    def ResetCappingFilter(self) -> None: 
        """
        Resets chain filter for Capping algorithm.
        """
    def RestoreDisabled(self) -> None: 
        """
        Restore all temporarily disabled planes. Does NOT affect constantly disabled planes Graphic3d_ClipPlane::IsOn().
        """
    def SetEnabled(self,thePlane : OpenGl_ClippingIterator,theIsEnabled : bool) -> bool: 
        """
        Disable plane temporarily.
        """
    def SetLocalPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Setup list of local (for current object) clipping planes.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_ClippingIterator():
    """
    The iterator through clipping planes.
    """
    def IsDisabled(self) -> bool: 
        """
        Return true if plane has been temporarily disabled either by Graphic3d_ClipPlane->IsOn() property or by temporary filter. Beware that this method does NOT handle a Chain filter for Capping algorithm OpenGl_Clipping::CappedChain()!
        """
    def IsGlobal(self) -> bool: 
        """
        Return true if plane from the global (view) list.
        """
    def More(self) -> bool: 
        """
        Return true if iterator points to the valid clipping plane.
        """
    def Next(self) -> None: 
        """
        Go to the next clipping plane.
        """
    def PlaneIndex(self) -> int: 
        """
        Return the plane index.
        """
    def Value(self) -> OCP.Graphic3d.Graphic3d_ClipPlane: 
        """
        Return the plane at current iterator position.
        """
    def __init__(self,theClipping : OpenGl_Clipping) -> None: ...
    pass
class OpenGl_ClippingState():
    """
    Defines generic state of OCCT clipping state.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def Revert(self) -> None: 
        """
        Reverts current state.
        """
    def Update(self) -> None: 
        """
        Updates current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_ColorFormats(OCP.NCollection.NCollection_BaseVector):
    """
    Class NCollection_Vector (dynamic array of objects)
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Append(self,theValue : int) -> int: 
        """
        Append
        """
    def Appended(self) -> int: 
        """
        Appends an empty value and returns the reference to it
        """
    def Assign(self,theOther : OpenGl_ColorFormats,theOwnAllocator : bool=True) -> None: 
        """
        Assignment to the collection of the same type
        """
    def ChangeFirst(self) -> int: 
        """
        Returns first element
        """
    def ChangeLast(self) -> int: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> int: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        Empty the vector of its objects
        """
    def First(self) -> int: 
        """
        Returns first element
        """
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> int: 
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
    def SetValue(self,theIndex : int,theValue : int) -> int: ...
    def Size(self) -> int: 
        """
        Total number of items in the vector
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> int: 
        """
        None
        """
    @overload
    def __init__(self,theIncrement : int=256,theAlloc : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : OpenGl_ColorFormats) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class OpenGl_Context(OCP.Standard.Standard_Transient):
    """
    This class generalize access to the GL context and available extensions.This class generalize access to the GL context and available extensions.
    """
    def ActiveProgram(self) -> OpenGl_ShaderProgram: 
        """
        Returns active GLSL program
        """
    def ActiveTextures(self) -> OpenGl_TextureSet: 
        """
        Returns active textures
        """
    def AllowSampleAlphaToCoverage(self) -> bool: 
        """
        Return TRUE if GL_SAMPLE_ALPHA_TO_COVERAGE usage is allowed.
        """
    def ApplyModelViewMatrix(self) -> None: 
        """
        Applies combination of matrices stored in ModelWorldState and WorldViewState to OpenGl. In "model -> world -> view -> projection" it performs: model -> world -> view
        """
    def ApplyModelWorldMatrix(self) -> None: 
        """
        Applies matrix into shader manager stored in ModelWorldState to OpenGl. In "model -> world -> view -> projection" it performs: model -> world
        """
    def ApplyProjectionMatrix(self) -> None: 
        """
        Applies matrix stored in ProjectionState to OpenGl. In "model -> world -> view -> projection" it performs: view -> projection
        """
    def ApplyWorldViewMatrix(self) -> None: 
        """
        Applies matrix stored in WorldViewState to OpenGl. In "model -> world -> view -> projection" it performs: model -> world -> view, where model -> world is identical matrix
        """
    def AvailableMemory(self) -> int: 
        """
        This function retrieves information from GL about free GPU memory that is: - OS-dependent. On some OS it is per-process and on others - for entire system. - Vendor-dependent. Currently available only on NVIDIA and AMD/ATi drivers only. - Numbers meaning may vary. You should use this info only for diagnostics purposes.
        """
    def BindDefaultVao(self) -> None: 
        """
        Bind default Vertex Array Object
        """
    def BindProgram(self,theProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Bind specified program to current context, or unbind previous one when NULL specified.
        """
    @overload
    def BindTextures(self,theTextures : OpenGl_TextureSet,theProgram : OpenGl_ShaderProgram) -> OpenGl_TextureSet: 
        """
        Bind specified texture set to current context taking into account active GLSL program.

        Bind specified texture set to current context, or unbind previous one when NULL specified.
        """
    @overload
    def BindTextures(self,theTextures : OpenGl_TextureSet) -> OpenGl_TextureSet: ...
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns camera object.
        """
    def ChangeClipping(self) -> OpenGl_Clipping: 
        """
        Returns tool for management of clippings within this context.
        """
    def CheckExtension(self,theExtName : str) -> bool: 
        """
        Check if theExtName extension is supported by active GL context.
        """
    @staticmethod
    def CheckExtension_s(theExtString : str,theExtName : str) -> bool: 
        """
        Check if theExtName extension is in extensions string.
        """
    @staticmethod
    @overload
    def CheckIsTransparent_s(theAspect : OpenGl_Aspects,theHighlight : OCP.Graphic3d.Graphic3d_PresentationAttributes,theAlphaFront : float,theAlphaBack : float) -> bool: 
        """
        Checks if transparency is required for the given aspect and highlight style.

        Checks if transparency is required for the given aspect and highlight style.
        """
    @staticmethod
    @overload
    def CheckIsTransparent_s(theAspect : OpenGl_Aspects,theHighlight : OCP.Graphic3d.Graphic3d_PresentationAttributes) -> bool: ...
    def Clipping(self) -> OpenGl_Clipping: 
        """
        Returns tool for management of clippings within this context.
        """
    def ColorMask(self) -> bool: 
        """
        Return cached flag indicating writing into color buffer is enabled or disabled (glColorMask).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultFrameBuffer(self) -> OpenGl_FrameBuffer: 
        """
        Default Frame Buffer Object.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DiagnosticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : OCP.Graphic3d.Graphic3d_DiagnosticInfo) -> None: 
        """
        Fill in the dictionary with OpenGL info. Should be called with bound context.
        """
    def DisableFeatures(self) -> None: 
        """
        None
        """
    def DrawBuffer(self,theIndex : int=0) -> int: 
        """
        Return active draw buffer attached to a render target referred by index (layout location).
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @staticmethod
    def DumpJsonOpenGlState_s(theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of openGL state into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableFeatures(self) -> None: 
        """
        None
        """
    def ExcludeMessage(self,theSource : int,theId : int) -> bool: 
        """
        Adds a filter for messages with theId and theSource (GL_DEBUG_SOURCE_)
        """
    def FetchState(self) -> None: 
        """
        Fetch OpenGl context state. This class tracks value of several OpenGl state variables. Consulting the cached values is quicker than doing the same via OpenGl API. Call this method if any of the controlled OpenGl state variables has a possibility of being out-of-date.
        """
    def FrameStats(self) -> OpenGl_FrameStats: 
        """
        Return structure holding frame statistics.
        """
    def Functions(self) -> OpenGl_GlFunctions: 
        """
        Access entire map of loaded OpenGL functions.
        """
    def GetBufferSubData(self,theTarget : int,theOffset : int,theSize : int,theData : capsule) -> bool: 
        """
        Wrapper over glGetBufferSubData(), implemented as: - OpenGL 1.5+ (desktop) via glGetBufferSubData(); - OpenGL ES 3.0+ via glMapBufferRange(); - WebGL 2.0+ via gl.getBufferSubData().
        """
    @staticmethod
    def GetPowerOfTwo_s(theNumber : int,theThreshold : int) -> int: 
        """
        Function for getting power of to number larger or equal to input number.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetResource(self,theKey : OCP.TCollection.TCollection_AsciiString) -> OpenGl_Resource: 
        """
        Access shared resource by its name.
        """
    def HasPBR(self) -> bool: 
        """
        Returns TRUE if PBR shading model is supported. Basically, feature requires OpenGL 3.0+ / OpenGL ES 3.0+ hardware; more precisely: - Graphics hardware with moderate capabilities for compiling long enough GLSL program. - FBO (e.g. for baking environment). - Multi-texturing with >= 4 units (LUT and IBL textures). - GL_RG32F texture format (arbTexRG + arbTexFloat) - Cubemap texture lookup textureCubeLod()/textureLod() with LOD index within Fragment Shader, which requires GLSL OpenGL 3.0+ / OpenGL ES 3.0+ or OpenGL 2.1 + GL_EXT_gpu_shader4 extension.
        """
    def HasRayTracing(self) -> bool: 
        """
        Returns TRUE if ray tracing mode is supported
        """
    def HasRayTracingAdaptiveSampling(self) -> bool: 
        """
        Returns TRUE if adaptive screen sampling in ray tracing mode is supported
        """
    def HasRayTracingAdaptiveSamplingAtomic(self) -> bool: 
        """
        Returns TRUE if atomic adaptive screen sampling in ray tracing mode is supported
        """
    def HasRayTracingTextures(self) -> bool: 
        """
        Returns TRUE if textures in ray tracing mode are supported
        """
    def HasRenderScale(self) -> bool: 
        """
        Return TRUE if rendering scale factor is not 1.
        """
    def HasSRGB(self) -> bool: 
        """
        Returns TRUE if sRGB rendering is supported.
        """
    def HasStereoBuffers(self) -> bool: 
        """
        Returns true if OpenGl context supports left and right rendering buffers.
        """
    def HasTextureBaseLevel(self) -> bool: 
        """
        Returns true if texture parameters GL_TEXTURE_BASE_LEVEL/GL_TEXTURE_MAX_LEVEL are supported.
        """
    def IncludeMessage(self,theSource : int,theId : int) -> bool: 
        """
        Removes a filter for messages with theId and theSource (GL_DEBUG_SOURCE_)
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theIsCoreProfile : bool=False) -> bool: 
        """
        Initialize class from currently bound OpenGL context. Method should be called only once.

        Initialize class from specified window and rendering context. Method should be called only once.
        """
    @overload
    def Init(self,theWindow : int,theDisplay : capsule,theGContext : capsule,theIsCoreProfile : bool=False) -> bool: ...
    def IsCurrent(self) -> bool: 
        """
        This method uses system-dependent API to retrieve information about GL context bound to the current thread.
        """
    def IsDebugContext(self) -> bool: 
        """
        Return debug context initialization state.
        """
    def IsFeedback(self) -> bool: 
        """
        Return true if active mode is GL_FEEDBACK (cached state)
        """
    def IsFrameBufferSRGB(self) -> bool: 
        """
        Returns cached GL_FRAMEBUFFER_SRGB state. If TRUE, GLSL program is expected to write linear RGB color. Otherwise, GLSL program might need manually converting result color into sRGB color space.
        """
    def IsGlGreaterEqual(self,theVerMajor : int,theVerMinor : int) -> bool: 
        """
        Returns true if detected GL version is greater or equal to requested one.
        """
    def IsGlNormalizeEnabled(self) -> bool: 
        """
        Returns cached state of GL_NORMALIZE.
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
    def IsPolygonHatchEnabled(self) -> bool: 
        """
        Returns cached enabled state of polygon hatching rasterization.
        """
    def IsRender(self) -> bool: 
        """
        Return true if active mode is GL_RENDER (cached state)
        """
    def IsValid(self) -> bool: 
        """
        Returns true if this context is valid (has been initialized)
        """
    def IsWindowSRGB(self) -> bool: 
        """
        Returns TRUE if window/surface buffer is sRGB-ready.
        """
    def LineFeather(self) -> float: 
        """
        Return line feater width in pixels.
        """
    def LineWidthScale(self) -> float: 
        """
        Return scale factor for line width.
        """
    def MakeCurrent(self) -> bool: 
        """
        Activates current context. Class should be initialized with appropriate info.
        """
    def MaxClipPlanes(self) -> int: 
        """
        Get maximum number of clip planes supported by OpenGl. This value is implementation dependent. At least 6 planes should be supported by OpenGl (see specs).
        """
    def MaxColorAttachments(self) -> int: 
        """
        Returns value for GL_MAX_COLOR_ATTACHMENTS
        """
    def MaxCombinedTextureUnits(self) -> int: 
        """
        Returns value for GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS
        """
    def MaxDegreeOfAnisotropy(self) -> int: 
        """
        Returns maximum degree of anisotropy texture filter
        """
    def MaxDrawBuffers(self) -> int: 
        """
        Returns value for GL_MAX_DRAW_BUFFERS
        """
    def MaxDumpSizeX(self) -> int: 
        """
        Returns maximum FBO width for image dump
        """
    def MaxDumpSizeY(self) -> int: 
        """
        Returns maximum FBO height for image dump
        """
    def MaxMsaaSamples(self) -> int: 
        """
        Returns value for GL_MAX_SAMPLES
        """
    def MaxTextureSize(self) -> int: 
        """
        Returns value for GL_MAX_TEXTURE_SIZE
        """
    def MaxTextureUnitsFFP(self) -> int: 
        """
        This method returns the multi-texture limit for obsolete fixed-function pipeline. Use MaxCombinedTextureUnits() instead for limits for using programmable pipeline.
        """
    @overload
    def MemoryInfo(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString) -> None: 
        """
        This function retrieves information from GL about GPU memory and contains more vendor-specific values than AvailableMemory().

        This function retrieves information from GL about GPU memory.
        """
    @overload
    def MemoryInfo(self) -> OCP.TCollection.TCollection_AsciiString: ...
    def Messenger(self) -> OCP.Message.Message_Messenger: 
        """
        Returns messenger instance
        """
    def PBRDiffIBLMapSHTexUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Returns texture unit where Diffuse (irradiance) IBL map's spherical harmonics coefficients is expected to be bound, or 0 if PBR is unavailable.
        """
    def PBREnvLUTTexUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Returns texture unit where Environment Lookup Table is expected to be bound, or 0 if PBR is unavailable.
        """
    def PBRSpecIBLMapTexUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Returns texture unit where Specular IBL map is expected to be bound, or 0 if PBR is unavailable.
        """
    def PolygonHatchStyle(self) -> int: 
        """
        Returns cached state of polygon hatch type.
        """
    def PolygonMode(self) -> int: 
        """
        Returns cached state of polygon rasterization mode (glPolygonMode()).
        """
    def PolygonOffset(self) -> OCP.Graphic3d.Graphic3d_PolygonOffset: 
        """
        Returns currently applied polygon offset parameters.
        """
    def PushMessage(self,theSource : int,theType : int,theId : int,theSeverity : int,theMessage : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        Callback for GL_ARB_debug_output extension
        """
    def ReadBuffer(self) -> int: 
        """
        Return active read buffer.
        """
    @staticmethod
    def ReadGlVersion_s() -> Tuple[int, int]: 
        """
        Read OpenGL version information from active context.
        """
    def ReleaseDelayed(self) -> None: 
        """
        Clean up the delayed release queue.
        """
    def ReleaseResource(self,theKey : OCP.TCollection.TCollection_AsciiString,theToDelay : bool=False) -> None: 
        """
        Release shared resource. If there are more than one reference to this resource (also used by some other existing object) then call will be ignored. This means that current object itself should nullify handle before this call. Notice that this is unrecommended operation at all and should be used only in case of fat resources to release memory for other needs.
        """
    def RenderScale(self) -> float: 
        """
        Rendering scale factor (rendering viewport height to real window buffer height).
        """
    def RenderScaleInv(self) -> float: 
        """
        Rendering scale factor (inverted value).
        """
    def ResetErrors(self,theToPrintErrors : bool=False) -> bool: 
        """
        Clean up errors stack for this GL context (glGetError() in loop).
        """
    def ResizeViewport(self,theRect : int) -> None: 
        """
        Resize the viewport (alias for glViewport).
        """
    def Resolution(self) -> int: 
        """
        Return resolution for rendering text.
        """
    def ResolutionRatio(self) -> float: 
        """
        Resolution scale factor (rendered resolution to standard resolution). This scaling factor for parameters like text size to be properly displayed on device (screen / printer).
        """
    def SampleAlphaToCoverage(self) -> bool: 
        """
        Return GL_SAMPLE_ALPHA_TO_COVERAGE state.
        """
    def SetAllowSampleAlphaToCoverage(self,theToEnable : bool) -> None: 
        """
        Allow GL_SAMPLE_ALPHA_TO_COVERAGE usage.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Sets camera object to the context and update matrices.
        """
    def SetColor4fv(self,theColor : OCP.Graphic3d.Graphic3d_Vec4) -> None: 
        """
        Setup current color.
        """
    def SetColorMask(self,theToWriteColor : bool) -> bool: 
        """
        Enable/disable writing into color buffer (wrapper for glColorMask).
        """
    def SetCullBackFaces(self,theToEnable : bool) -> None: 
        """
        Enable or disable back face culling (glEnable (GL_CULL_FACE)).
        """
    def SetDefaultFrameBuffer(self,theFbo : OpenGl_FrameBuffer) -> OpenGl_FrameBuffer: 
        """
        Setup new Default Frame Buffer Object and return previously set. This call doesn't change Active FBO!
        """
    def SetDrawBuffer(self,theDrawBuffer : int) -> None: 
        """
        Switch draw buffer, wrapper for ::glDrawBuffer().
        """
    def SetDrawBuffers(self,theNb : int,theDrawBuffers : int) -> None: 
        """
        Switch draw buffer, wrapper for ::glDrawBuffers (GLsizei, const GLenum*).
        """
    def SetFrameBufferSRGB(self,theIsFbo : bool,theIsFboSRgb : bool=True) -> None: 
        """
        Enables/disables GL_FRAMEBUFFER_SRGB flag. This flag can be set to: - TRUE when writing into offscreen FBO (always expected to be in sRGB or RGBF formats). - TRUE when writing into sRGB-ready window buffer (might require choosing proper pixel format on window creation). - FALSE if sRGB rendering is not supported or sRGB-not-ready window buffer is used for drawing.
        """
    def SetFrameStats(self,theStats : OpenGl_FrameStats) -> None: 
        """
        Set structure holding frame statistics. This call makes sense only if application defines OpenGl_FrameStats sub-class.
        """
    def SetGlNormalizeEnabled(self,isEnabled : bool) -> bool: 
        """
        Sets GL_NORMALIZE enabled or disabled.
        """
    def SetLineFeather(self,theValue : float) -> None: 
        """
        Set line feater width.
        """
    @overload
    def SetLineStipple(self,theFactor : float,thePattern : int) -> None: 
        """
        Setup stipple line pattern with 1.0f factor; wrapper for glLineStipple().

        Setup type of line; wrapper for glLineStipple().
        """
    @overload
    def SetLineStipple(self,thePattern : int) -> None: ...
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Setup width of line.
        """
    def SetPointSize(self,theSize : float) -> None: 
        """
        Setup point size.
        """
    def SetPointSpriteOrigin(self) -> None: 
        """
        Setup point sprite origin using GL_POINT_SPRITE_COORD_ORIGIN state: - GL_UPPER_LEFT when GLSL program is active; flipping should be handled in GLSL program for compatibility with OpenGL ES - GL_LOWER_LEFT for FFP
        """
    def SetPolygonHatchEnabled(self,theIsEnabled : bool) -> bool: 
        """
        Sets enabled state of polygon hatching rasterization without affecting currently selected hatching pattern.
        """
    def SetPolygonHatchStyle(self,theStyle : OCP.Graphic3d.Graphic3d_HatchStyle) -> int: 
        """
        Sets polygon hatch pattern. Zero-index value is a default alias for solid filling.
        """
    def SetPolygonMode(self,theMode : int) -> int: 
        """
        Sets polygon rasterization mode (glPolygonMode() function).
        """
    def SetPolygonOffset(self,theOffset : OCP.Graphic3d.Graphic3d_PolygonOffset) -> None: 
        """
        Sets and applies current polygon offset.
        """
    def SetReadBuffer(self,theReadBuffer : int) -> None: 
        """
        Switch read buffer, wrapper for ::glReadBuffer().
        """
    def SetReadDrawBuffer(self,theBuffer : int) -> None: 
        """
        Switch read/draw buffers.
        """
    def SetResolution(self,theResolution : int,theRatio : float,theScale : float) -> None: 
        """
        Set resolution ratio. Note that this method rounds to nearest integer.
        """
    def SetResolutionRatio(self,theRatio : float) -> None: 
        """
        Set resolution ratio. Note that this method rounds to nearest integer.
        """
    def SetSampleAlphaToCoverage(self,theToEnable : bool) -> bool: 
        """
        Enable/disable GL_SAMPLE_ALPHA_TO_COVERAGE.
        """
    def SetShadeModel(self,theModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel) -> None: 
        """
        Set GL_SHADE_MODEL value.
        """
    def SetShadingMaterial(self,theAspect : OpenGl_Aspects,theHighlight : OCP.Graphic3d.Graphic3d_PresentationAttributes) -> None: 
        """
        Setup current shading material.
        """
    def SetSwapInterval(self,theInterval : int) -> bool: 
        """
        Setup swap interval (VSync).
        """
    def SetTextureMatrix(self,theParams : OCP.Graphic3d.Graphic3d_TextureParams,theIsTopDown : bool) -> None: 
        """
        Setup texture matrix to active GLSL program or to FFP global state using glMatrixMode (GL_TEXTURE).
        """
    def SetTypeOfLine(self,theType : OCP.Aspect.Aspect_TypeOfLine,theFactor : float=1.0) -> None: 
        """
        Setup type of line.
        """
    def SetWindowSRGB(self,theIsSRgb : bool) -> None: 
        """
        Overrides if window/surface buffer is sRGB-ready or not (initialized with the context).
        """
    def ShaderManager(self) -> OpenGl_ShaderManager: 
        """
        Returns tool for management of shader programs within this context.
        """
    def Share(self,theShareCtx : OpenGl_Context) -> None: 
        """
        Share GL context resources. theShareCtx - handle to context to retrieve handles to shared resources.
        """
    def ShareResource(self,theKey : OCP.TCollection.TCollection_AsciiString,theResource : OpenGl_Resource) -> bool: 
        """
        Register shared resource. Notice that after registration caller shouldn't release it by himself - it will be automatically released on context destruction.
        """
    def SharedResources(self) -> Any: 
        """
        Return map of shared resources.
        """
    def SpriteTextureUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Return texture unit to be used for sprites (Graphic3d_TextureUnit_PointSprite by default).
        """
    def SupportedTextureFormats(self) -> OCP.Image.Image_SupportedFormats: 
        """
        Return map of supported texture formats.
        """
    def SwapBuffers(self) -> None: 
        """
        Swap front/back buffers for this GL context (should be activated before!).
        """
    def TextureWrapClamp(self) -> int: 
        """
        Either GL_CLAMP_TO_EDGE (1.2+) or GL_CLAMP (1.1).
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToCullBackFaces(self) -> bool: 
        """
        Return back face culling state.
        """
    def ToRenderSRGB(self) -> bool: 
        """
        Returns TRUE if sRGB rendering is supported and permitted.
        """
    def ToUseVbo(self) -> bool: 
        """
        Returns true if VBO is supported and permitted.
        """
    def Vec4FromQuantityColor(self,theColor : OCP.Graphic3d.Graphic3d_Vec4) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Convert Quantity_ColorRGBA into vec4 with conversion or no conversion into non-linear sRGB basing on ToRenderSRGB() flag.
        """
    def Vec4LinearFromQuantityColor(self,theColor : OCP.Graphic3d.Graphic3d_Vec4) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Convert Quantity_ColorRGBA into vec4. Quantity_Color is expected to be linear RGB, hence conversion is NOT required
        """
    def Vec4sRGBFromQuantityColor(self,theColor : OCP.Graphic3d.Graphic3d_Vec4) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Convert Quantity_ColorRGBA (linear RGB) into non-linear sRGB vec4.
        """
    def Vendor(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return Graphics Driver's vendor.
        """
    def VersionMajor(self) -> int: 
        """
        Return cached GL version major number.
        """
    def VersionMinor(self) -> int: 
        """
        Return cached GL version minor number.
        """
    def Viewport(self) -> int: 
        """
        Return cached viewport definition (x, y, width, height).
        """
    def VirtualViewport(self) -> int: 
        """
        Return virtual viewport definition (x, y, width, height).
        """
    def Window(self) -> int: 
        """
        Returns the window handle (GLXDrawable) currently bound to this OpenGL context
        """
    def __init__(self,theCaps : OpenGl_Caps=None) -> None: ...
    def forcedRelease(self) -> None: 
        """
        Release all resources, including shared ones
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
    @property
    def arbDrawBuffers(self) -> bool:
        """
        :type: bool
        """
    @arbDrawBuffers.setter
    def arbDrawBuffers(self, arg0: bool) -> None:
        pass
    @property
    def arbNPTW(self) -> bool:
        """
        :type: bool
        """
    @arbNPTW.setter
    def arbNPTW(self, arg0: bool) -> None:
        pass
    @property
    def arbSampleShading(self) -> bool:
        """
        :type: bool
        """
    @arbSampleShading.setter
    def arbSampleShading(self, arg0: bool) -> None:
        pass
    @property
    def arbTboRGB32(self) -> bool:
        """
        :type: bool
        """
    @arbTboRGB32.setter
    def arbTboRGB32(self, arg0: bool) -> None:
        pass
    @property
    def arbTexFloat(self) -> bool:
        """
        :type: bool
        """
    @arbTexFloat.setter
    def arbTexFloat(self, arg0: bool) -> None:
        pass
    @property
    def arbTexRG(self) -> bool:
        """
        :type: bool
        """
    @arbTexRG.setter
    def arbTexRG(self, arg0: bool) -> None:
        pass
    @property
    def atiMem(self) -> bool:
        """
        :type: bool
        """
    @atiMem.setter
    def atiMem(self, arg0: bool) -> None:
        pass
    @property
    def extAnis(self) -> bool:
        """
        :type: bool
        """
    @extAnis.setter
    def extAnis(self, arg0: bool) -> None:
        pass
    @property
    def extBgra(self) -> bool:
        """
        :type: bool
        """
    @extBgra.setter
    def extBgra(self, arg0: bool) -> None:
        pass
    @property
    def extDrawBuffers(self) -> bool:
        """
        :type: bool
        """
    @extDrawBuffers.setter
    def extDrawBuffers(self, arg0: bool) -> None:
        pass
    @property
    def extFragDepth(self) -> bool:
        """
        :type: bool
        """
    @extFragDepth.setter
    def extFragDepth(self, arg0: bool) -> None:
        pass
    @property
    def extPDS(self) -> bool:
        """
        :type: bool
        """
    @extPDS.setter
    def extPDS(self, arg0: bool) -> None:
        pass
    @property
    def hasDrawBuffers(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasDrawBuffers.setter
    def hasDrawBuffers(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasFboSRGB(self) -> bool:
        """
        :type: bool
        """
    @hasFboSRGB.setter
    def hasFboSRGB(self, arg0: bool) -> None:
        pass
    @property
    def hasFlatShading(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasFlatShading.setter
    def hasFlatShading(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasFloatBuffer(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasFloatBuffer.setter
    def hasFloatBuffer(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasGeometryStage(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasGeometryStage.setter
    def hasGeometryStage(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasGetBufferData(self) -> bool:
        """
        :type: bool
        """
    @hasGetBufferData.setter
    def hasGetBufferData(self, arg0: bool) -> None:
        pass
    @property
    def hasGlslBitwiseOps(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasGlslBitwiseOps.setter
    def hasGlslBitwiseOps(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasHalfFloatBuffer(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasHalfFloatBuffer.setter
    def hasHalfFloatBuffer(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasHighp(self) -> bool:
        """
        :type: bool
        """
    @hasHighp.setter
    def hasHighp(self, arg0: bool) -> None:
        pass
    @property
    def hasSRGBControl(self) -> bool:
        """
        :type: bool
        """
    @hasSRGBControl.setter
    def hasSRGBControl(self, arg0: bool) -> None:
        pass
    @property
    def hasSampleVariables(self) -> OpenGl_FeatureFlag:
        """
        :type: OpenGl_FeatureFlag
        """
    @hasSampleVariables.setter
    def hasSampleVariables(self, arg0: OpenGl_FeatureFlag) -> None:
        pass
    @property
    def hasTexFloatLinear(self) -> bool:
        """
        :type: bool
        """
    @hasTexFloatLinear.setter
    def hasTexFloatLinear(self, arg0: bool) -> None:
        pass
    @property
    def hasTexRGBA8(self) -> bool:
        """
        :type: bool
        """
    @hasTexRGBA8.setter
    def hasTexRGBA8(self, arg0: bool) -> None:
        pass
    @property
    def hasTexSRGB(self) -> bool:
        """
        :type: bool
        """
    @hasTexSRGB.setter
    def hasTexSRGB(self, arg0: bool) -> None:
        pass
    @property
    def hasUintIndex(self) -> bool:
        """
        :type: bool
        """
    @hasUintIndex.setter
    def hasUintIndex(self, arg0: bool) -> None:
        pass
    @property
    def nvxMem(self) -> bool:
        """
        :type: bool
        """
    @nvxMem.setter
    def nvxMem(self, arg0: bool) -> None:
        pass
    @property
    def oesSampleVariables(self) -> bool:
        """
        :type: bool
        """
    @oesSampleVariables.setter
    def oesSampleVariables(self, arg0: bool) -> None:
        pass
    @property
    def oesStdDerivatives(self) -> bool:
        """
        :type: bool
        """
    @oesStdDerivatives.setter
    def oesStdDerivatives(self, arg0: bool) -> None:
        pass
    pass
class OpenGl_Aspects(OpenGl_Element):
    """
    The element holding Graphic3d_Aspects.
    """
    def Aspect(self) -> OCP.Graphic3d.Graphic3d_Aspects: 
        """
        Return aspect.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def HasPointSprite(self,theCtx : OpenGl_Context) -> bool: 
        """
        Return TRUE if OpenGl point sprite resource defines texture.
        """
    def IsDisplayListSprite(self,theCtx : OpenGl_Context) -> bool: 
        """
        Return TRUE if OpenGl point sprite resource defined by obsolete Display List (bitmap).
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def MarkerSize(self) -> float: 
        """
        Returns marker size
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        None
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        None
        """
    def SetAspect(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Assign parameters.
        """
    def SetNoLighting(self) -> None: 
        """
        Set if lighting should be disabled or not.
        """
    def ShaderProgramRes(self,theCtx : OpenGl_Context) -> OpenGl_ShaderProgram: 
        """
        Init and return OpenGl shader program resource.
        """
    def ShadingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Returns Shading Model.
        """
    def SpriteRes(self,theCtx : OpenGl_Context,theIsAlphaSprite : bool) -> OpenGl_PointSprite: 
        """
        Init and return OpenGl point sprite resource.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update presentation aspects parameters after their modification.
        """
    def TextureSet(self,theCtx : OpenGl_Context,theToHighlight : bool=False) -> OpenGl_TextureSet: 
        """
        Returns textures map.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: ...
    pass
class OpenGl_ElementNode():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ExtGS():
    """
    Geometry shader as extension is available on OpenGL 2.0+
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_FeatureFlag():
    """
    None

    Members:

      OpenGl_FeatureNotAvailable

      OpenGl_FeatureInExtensions

      OpenGl_FeatureInCore
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
    OpenGl_FeatureInCore: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureInCore: 2>
    OpenGl_FeatureInExtensions: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureInExtensions: 1>
    OpenGl_FeatureNotAvailable: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureNotAvailable: 0>
    __entries: dict # value = {'OpenGl_FeatureNotAvailable': (<OpenGl_FeatureFlag.OpenGl_FeatureNotAvailable: 0>, None), 'OpenGl_FeatureInExtensions': (<OpenGl_FeatureFlag.OpenGl_FeatureInExtensions: 1>, None), 'OpenGl_FeatureInCore': (<OpenGl_FeatureFlag.OpenGl_FeatureInCore: 2>, None)}
    __members__: dict # value = {'OpenGl_FeatureNotAvailable': <OpenGl_FeatureFlag.OpenGl_FeatureNotAvailable: 0>, 'OpenGl_FeatureInExtensions': <OpenGl_FeatureFlag.OpenGl_FeatureInExtensions: 1>, 'OpenGl_FeatureInCore': <OpenGl_FeatureFlag.OpenGl_FeatureInCore: 2>}
    pass
class OpenGl_Flipper(OpenGl_Element):
    """
    Being rendered, the elements modifies current model-view matrix such that the axes of the specified reference system (in model space) become oriented in the following way: - X - heads to the right side of view. - Y - heads to the up side of view. - N(Z) - heads towards the screen. Originally, this element serves for need of flipping the 3D text of dimension presentations.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        None
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        None
        """
    def SetOptions(self,theIsEnabled : bool) -> None: 
        """
        Set options for the element.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    def __init__(self,theReferenceSystem : OCP.gp.gp_Ax2) -> None: ...
    pass
class OpenGl_Font(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Texture font.Texture font.
    """
    def Ascender(self) -> float: 
        """
        Returns vertical distance from the horizontal baseline to the highest character coordinate
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Descender(self) -> float: 
        """
        Returns vertical distance from the horizontal baseline to the lowest character coordinate
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage.
        """
    def FTFont(self) -> OCP.Font.Font_FTFont: 
        """
        Returns FreeType font instance specified on construction.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theCtx : OpenGl_Context) -> bool: 
        """
        Initialize GL resources. FreeType font instance should be already initialized!
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
    def IsValid(self) -> bool: 
        """
        Returns true if font was loaded successfully.
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any
        """
    def RenderGlyph(self,theCtx : OpenGl_Context,theUChar : str,theGlyph : Any) -> bool: 
        """
        Render glyph to texture if not already.
        """
    def ResourceKey(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns key of shared resource
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def WasInitialized(self) -> bool: 
        """
        Notice that this method doesn't return initialization success state. Use IsValid() instead.
        """
    def __init__(self,theFont : OCP.Font.Font_FTFont,theKey : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class OpenGl_FrameBuffer(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Class implements FrameBuffer Object (FBO) resource intended for off-screen rendering.Class implements FrameBuffer Object (FBO) resource intended for off-screen rendering.Class implements FrameBuffer Object (FBO) resource intended for off-screen rendering.
    """
    def BindBuffer(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind frame buffer for drawing and reading (to render into the texture).
        """
    def BindDrawBuffer(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind frame buffer for drawing GL_DRAW_FRAMEBUFFER (to render into the texture).
        """
    def BindReadBuffer(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind frame buffer for reading GL_READ_FRAMEBUFFER
        """
    @staticmethod
    def BufferDump_s(theGlCtx : OpenGl_Context,theFbo : OpenGl_FrameBuffer,theImage : OCP.Image.Image_PixMap,theBufferType : OCP.Graphic3d.Graphic3d_BufferType) -> bool: 
        """
        Dump content into image.
        """
    def ChangeViewport(self,theVPSizeX : int,theVPSizeY : int) -> None: 
        """
        Override viewport settings
        """
    def ColorRenderBuffer(self) -> int: 
        """
        Returns the color Render Buffer.
        """
    def ColorTexture(self,theColorBufferIndex : int=0) -> OpenGl_Texture: 
        """
        Returns the color texture for the given color buffer index.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DepthStencilRenderBuffer(self) -> int: 
        """
        Returns the depth Render Buffer.
        """
    def DepthStencilTexture(self) -> OpenGl_Texture: 
        """
        Returns the depth-stencil texture.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetInitVPSizeX(self) -> int: 
        """
        Viewport width.
        """
    def GetInitVPSizeY(self) -> int: 
        """
        Viewport height.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSizeX(self) -> int: 
        """
        Textures width.
        """
    def GetSizeY(self) -> int: 
        """
        Textures height.
        """
    def GetVPSizeX(self) -> int: 
        """
        Viewport width.
        """
    def GetVPSizeY(self) -> int: 
        """
        Viewport height.
        """
    def HasColor(self) -> bool: 
        """
        Return true if FBO has been created with color attachment.
        """
    def HasDepth(self) -> bool: 
        """
        Return true if FBO has been created with depth attachment.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theColorFormats : OpenGl_ColorFormats,theDepthFormat : int,theNbSamples : int=0) -> bool: 
        """
        Initialize FBO for rendering into single/multiple color buffer and depth textures.

        Initialize FBO for rendering into textures.

        Initialize FBO for rendering into single/multiple color buffer and depth textures.
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theColorFormats : OpenGl_ColorFormats,theDepthStencilTexture : OpenGl_Texture,theNbSamples : int=0) -> bool: ...
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theColorFormat : int,theDepthFormat : int,theNbSamples : int=0) -> bool: ...
    @overload
    def InitLazy(self,theGlCtx : OpenGl_Context,theViewportSizeX : int,theViewportSizeY : int,theColorFormat : int,theDepthFormat : int,theNbSamples : int=0) -> bool: 
        """
        (Re-)initialize FBO with specified dimensions.

        (Re-)initialize FBO with specified dimensions.

        (Re-)initialize FBO with properties taken from another FBO.
        """
    @overload
    def InitLazy(self,theGlCtx : OpenGl_Context,theViewportSizeX : int,theViewportSizeY : int,theColorFormats : OpenGl_ColorFormats,theDepthFormat : int,theNbSamples : int=0) -> bool: ...
    @overload
    def InitLazy(self,theGlCtx : OpenGl_Context,theFbo : OpenGl_FrameBuffer) -> bool: ...
    def InitWithRB(self,theGlCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theColorFormat : int,theDepthFormat : int,theColorRBufferFromWindow : int=0) -> bool: 
        """
        (Re-)initialize FBO with specified dimensions. The Render Buffer Objects will be used for Color, Depth and Stencil attachments (as opposite to textures).
        """
    def InitWrapper(self,theGlCtx : OpenGl_Context) -> bool: 
        """
        Initialize class from currently bound FBO. Retrieved OpenGL objects will not be destroyed on Release.
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def NbColorBuffers(self) -> int: 
        """
        Number of color buffers.
        """
    def NbSamples(self) -> int: 
        """
        Number of multisampling samples.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def SetupViewport(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Setup viewport to render into FBO
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UnbindBuffer(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind frame buffer.
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
class OpenGl_FrameStats(OCP.Graphic3d.Graphic3d_FrameStats, OCP.Standard.Standard_Transient):
    """
    Class storing the frame statistics.Class storing the frame statistics.
    """
    def ActiveDataFrame(self) -> OCP.Graphic3d.Graphic3d_FrameStatsDataTmp: 
        """
        Returns currently filling data frame for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def ChangeCounter(self,theCounter : OCP.Graphic3d.Graphic3d_FrameStatsCounter) -> int: 
        """
        Returns value of specified counter for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def ChangeDataFrames(self) -> Any: 
        """
        Returns data frames.
        """
    def ChangeTimer(self,theTimer : OCP.Graphic3d.Graphic3d_FrameStatsTimer) -> float: 
        """
        Returns value of specified timer for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def CounterValue(self,theCounter : OCP.Graphic3d.Graphic3d_FrameStatsCounter) -> int: 
        """
        Returns value of specified counter, cached between stats updates. Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def DataFrames(self) -> Any: 
        """
        Returns data frames.
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
    @overload
    def FormatStats(self,theFlags : Any) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns formatted string.

        Fill in the dictionary with formatted statistic info.
        """
    @overload
    def FormatStats(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : Any) -> None: ...
    def FrameDuration(self) -> float: 
        """
        Returns duration of the last frame in seconds.
        """
    def FrameEnd(self,theView : OCP.Graphic3d.Graphic3d_CView,theIsImmediateOnly : bool) -> None: 
        """
        Frame redraw finished.
        """
    def FrameRate(self) -> float: 
        """
        Returns FPS (frames per seconds, elapsed time). This number indicates an actual frame rate averaged for several frames within UpdateInterval() duration, basing on a real elapsed time between updates.
        """
    def FrameRateCpu(self) -> float: 
        """
        Returns CPU FPS (frames per seconds, CPU time). This number indicates a PREDICTED frame rate, basing on CPU elapsed time between updates and NOT real elapsed time (which might include periods of CPU inactivity). Number is expected to be greater then actual frame rate returned by FrameRate(). Values significantly greater actual frame rate indicate that rendering is limited by GPU performance (CPU is stalled in-between), while values around actual frame rate indicate rendering being limited by CPU performance (GPU is stalled in-between).
        """
    def FrameStart(self,theView : OCP.Graphic3d.Graphic3d_CView,theIsImmediateOnly : bool) -> None: 
        """
        Frame redraw started.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasCulledLayers(self) -> bool: 
        """
        Returns TRUE if some Layers have been culled.
        """
    def HasCulledStructs(self) -> bool: 
        """
        Returns TRUE if some structures have been culled.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsFrameUpdated(self,thePrev : OpenGl_FrameStats) -> bool: 
        """
        Copy stats values into another instance (create new instance, if not exists). The main use of this method is to track changes in statistics (e.g. in conjunction with IsEqual() method).
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
    def IsLongLineFormat(self) -> bool: 
        """
        Prefer longer lines over more greater of lines.
        """
    def LastDataFrame(self) -> OCP.Graphic3d.Graphic3d_FrameStatsData: 
        """
        Returns last data frame, cached between stats updates. Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def LastDataFrameIndex(self) -> int: 
        """
        Returns last data frame index.
        """
    def SetLongLineFormat(self,theValue : bool) -> None: 
        """
        Set if format should prefer longer lines over greater number of lines.
        """
    def SetUpdateInterval(self,theInterval : float) -> None: 
        """
        Sets interval in seconds for updating values.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TimerValue(self,theTimer : OCP.Graphic3d.Graphic3d_FrameStatsTimer) -> float: 
        """
        Returns value of specified timer for modification, should be called between ::FrameStart() and ::FrameEnd() calls. Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def UpdateInterval(self) -> float: 
        """
        Returns interval in seconds for updating meters across several frames; 1 second by default.
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
class OpenGl_FrameStatsPrs(OpenGl_Element):
    """
    Element rendering frame statistics.
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Release OpenGL resources.
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Render element.
        """
    def SetTextAspect(self,theAspect : OCP.Graphic3d.Graphic3d_AspectText3d) -> None: 
        """
        Assign text aspect.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def Update(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Update text.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_GlCore11():
    """
    OpenGL 1.1 core. Notice that all functions within this structure are actually exported by system GL library. The main purpose for these hint - to control visibility of functions per GL version (global functions should not be used directly to achieve this effect!).
    """
    def __init__(self) -> None: ...
    def glAccum(self,theOp : int,theValue : float) -> None: 
        """
        None
        """
    def glAreTexturesResident(self,n : int,textures : int,residences : int) -> int: 
        """
        None
        """
    def glBegin(self,theMode : int) -> None: ...
    def glBitmap(self,width : int,height : int,xorig : float,yorig : float,xmove : float,ymove : float,bitmap : int) -> None: 
        """
        None
        """
    def glCallList(self,theList : int) -> None: 
        """
        None
        """
    def glCallLists(self,theNb : int,theType : int,theLists : capsule) -> None: 
        """
        None
        """
    def glClearAccum(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: ...
    def glClipPlane(self,thePlane : int,theEquation : float) -> None: ...
    def glColor3b(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3bv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor3d(self,theRed : float,theGreen : float,theBlue : float) -> None: 
        """
        None
        """
    def glColor3dv(self,theVec : float) -> None: 
        """
        None
        """
    def glColor3f(self,theRed : float,theGreen : float,theBlue : float) -> None: 
        """
        None
        """
    def glColor3fv(self,theVec : float) -> None: 
        """
        None
        """
    def glColor3i(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3iv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor3s(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3sv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor3ub(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3ubv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor3ui(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3uiv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor3us(self,theRed : int,theGreen : int,theBlue : int) -> None: 
        """
        None
        """
    def glColor3usv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4b(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4bv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4d(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: 
        """
        None
        """
    def glColor4dv(self,theVec : float) -> None: 
        """
        None
        """
    def glColor4f(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: 
        """
        None
        """
    def glColor4fv(self,theVec : float) -> None: 
        """
        None
        """
    def glColor4i(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4iv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4s(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4sv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4ub(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4ubv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4ui(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4uiv(self,theVec : int) -> None: 
        """
        None
        """
    def glColor4us(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glColor4usv(self,theVec : int) -> None: 
        """
        None
        """
    def glColorMaterial(self,face : int,mode : int) -> None: 
        """
        None
        """
    def glColorPointer(self,theSize : int,theType : int,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    def glCopyPixels(self,x : int,y : int,width : int,height : int,type : int) -> None: 
        """
        None
        """
    def glDeleteLists(self,theList : int,theRange : int) -> None: 
        """
        None
        """
    def glDisableClientState(self,theCap : int) -> None: 
        """
        None
        """
    def glDrawPixels(self,width : int,height : int,format : int,type : int,pixels : capsule) -> None: ...
    def glEdgeFlag(self,theFlag : int) -> None: ...
    def glEdgeFlagPointer(self,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    def glEdgeFlagv(self,theFlag : int) -> None: 
        """
        None
        """
    def glEnableClientState(self,theCap : int) -> None: 
        """
        None
        """
    def glEnd(self) -> None: 
        """
        None
        """
    def glEndList(self) -> None: 
        """
        None
        """
    def glEvalCoord1d(self,u : float) -> None: 
        """
        None
        """
    def glEvalCoord1dv(self,u : float) -> None: 
        """
        None
        """
    def glEvalCoord1f(self,u : float) -> None: 
        """
        None
        """
    def glEvalCoord1fv(self,u : float) -> None: 
        """
        None
        """
    def glEvalCoord2d(self,u : float,v : float) -> None: 
        """
        None
        """
    def glEvalCoord2dv(self,u : float) -> None: 
        """
        None
        """
    def glEvalCoord2f(self,u : float,v : float) -> None: 
        """
        None
        """
    def glEvalCoord2fv(self,u : float) -> None: 
        """
        None
        """
    def glEvalMesh1(self,mode : int,i1 : int,i2 : int) -> None: 
        """
        None
        """
    def glEvalMesh2(self,mode : int,i1 : int,i2 : int,j1 : int,j2 : int) -> None: 
        """
        None
        """
    def glEvalPoint1(self,i : int) -> None: 
        """
        None
        """
    def glEvalPoint2(self,i : int,j : int) -> None: 
        """
        None
        """
    def glFeedbackBuffer(self,theSize : int,theType : int,theBuffer : float) -> None: ...
    def glFogf(self,pname : int,param : float) -> None: ...
    def glFogfv(self,pname : int,params : float) -> None: 
        """
        None
        """
    def glFogi(self,pname : int,param : int) -> None: 
        """
        None
        """
    def glFogiv(self,pname : int,params : int) -> None: 
        """
        None
        """
    def glFrustum(self,theLeft : float,theRight : float,theBottom : float,theTop : float,theNearVal : float,theFarVal : float) -> None: 
        """
        None
        """
    def glGenLists(self,theRange : int) -> int: 
        """
        None
        """
    def glGetClipPlane(self,thePlane : int,theEquation : float) -> None: 
        """
        None
        """
    def glGetLightfv(self,theLight : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glGetLightiv(self,theLight : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glGetMapdv(self,target : int,query : int,v : float) -> None: 
        """
        None
        """
    def glGetMapfv(self,target : int,query : int,v : float) -> None: 
        """
        None
        """
    def glGetMapiv(self,target : int,query : int,v : int) -> None: 
        """
        None
        """
    def glGetMaterialfv(self,face : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glGetMaterialiv(self,face : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glGetPolygonStipple(self,theMask : int) -> None: 
        """
        None
        """
    def glGetTexGendv(self,coord : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glGetTexGenfv(self,coord : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glGetTexGeniv(self,coord : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glIndexPointer(self,theType : int,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    def glIndexd(self,c : float) -> None: 
        """
        None
        """
    def glIndexdv(self,c : float) -> None: 
        """
        None
        """
    def glIndexf(self,c : float) -> None: 
        """
        None
        """
    def glIndexfv(self,c : float) -> None: 
        """
        None
        """
    def glIndexi(self,c : int) -> None: 
        """
        None
        """
    def glIndexiv(self,c : int) -> None: 
        """
        None
        """
    def glIndexs(self,c : int) -> None: 
        """
        None
        """
    def glIndexsv(self,c : int) -> None: 
        """
        None
        """
    def glIndexub(self,c : int) -> None: 
        """
        None
        """
    def glIndexubv(self,c : int) -> None: 
        """
        None
        """
    def glInitNames(self) -> None: 
        """
        None
        """
    def glInterleavedArrays(self,theFormat : int,theStride : int,thePointer : capsule) -> None: 
        """
        None
        """
    def glIsList(self,theList : int) -> int: ...
    def glLightModelf(self,pname : int,param : float) -> None: 
        """
        None
        """
    def glLightModelfv(self,pname : int,params : float) -> None: 
        """
        None
        """
    def glLightModeli(self,pname : int,param : int) -> None: 
        """
        None
        """
    def glLightModeliv(self,pname : int,params : int) -> None: 
        """
        None
        """
    def glLightf(self,theLight : int,pname : int,param : float) -> None: 
        """
        None
        """
    def glLightfv(self,theLight : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glLighti(self,theLight : int,pname : int,param : int) -> None: 
        """
        None
        """
    def glLightiv(self,theLight : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glLineStipple(self,theFactor : int,thePattern : int) -> None: 
        """
        None
        """
    def glListBase(self,theBase : int) -> None: 
        """
        None
        """
    def glLoadIdentity(self) -> None: 
        """
        None
        """
    def glLoadMatrixd(self,theMatrix : float) -> None: 
        """
        None
        """
    def glLoadMatrixf(self,theMatrix : float) -> None: 
        """
        None
        """
    def glLoadName(self,theName : int) -> None: 
        """
        None
        """
    def glMap1d(self,target : int,u1 : float,u2 : float,stride : int,order : int,points : float) -> None: ...
    def glMap1f(self,target : int,u1 : float,u2 : float,stride : int,order : int,points : float) -> None: 
        """
        None
        """
    def glMap2d(self,target : int,u1 : float,u2 : float,ustride : int,uorder : int,v1 : float,v2 : float,vstride : int,vorder : int,points : float) -> None: 
        """
        None
        """
    def glMap2f(self,target : int,u1 : float,u2 : float,ustride : int,uorder : int,v1 : float,v2 : float,vstride : int,vorder : int,points : float) -> None: 
        """
        None
        """
    def glMapGrid1d(self,un : int,u1 : float,u2 : float) -> None: 
        """
        None
        """
    def glMapGrid1f(self,un : int,u1 : float,u2 : float) -> None: 
        """
        None
        """
    def glMapGrid2d(self,un : int,u1 : float,u2 : float,vn : int,v1 : float,v2 : float) -> None: 
        """
        None
        """
    def glMapGrid2f(self,un : int,u1 : float,u2 : float,vn : int,v1 : float,v2 : float) -> None: 
        """
        None
        """
    def glMaterialf(self,face : int,pname : int,param : float) -> None: 
        """
        None
        """
    def glMaterialfv(self,face : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glMateriali(self,face : int,pname : int,param : int) -> None: 
        """
        None
        """
    def glMaterialiv(self,face : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glMatrixMode(self,theMode : int) -> None: ...
    def glMultMatrixd(self,theMatrix : float) -> None: 
        """
        None
        """
    def glMultMatrixf(self,theMatrix : float) -> None: 
        """
        None
        """
    def glNewList(self,theList : int,theMode : int) -> None: 
        """
        None
        """
    def glNormal3b(self,nx : int,ny : int,nz : int) -> None: 
        """
        None
        """
    def glNormal3bv(self,theVec : int) -> None: 
        """
        None
        """
    def glNormal3d(self,nx : float,ny : float,nz : float) -> None: 
        """
        None
        """
    def glNormal3dv(self,theVec : float) -> None: 
        """
        None
        """
    def glNormal3f(self,nx : float,ny : float,nz : float) -> None: 
        """
        None
        """
    def glNormal3fv(self,theVec : float) -> None: 
        """
        None
        """
    def glNormal3i(self,nx : int,ny : int,nz : int) -> None: 
        """
        None
        """
    def glNormal3iv(self,theVec : int) -> None: 
        """
        None
        """
    def glNormal3s(self,nx : int,ny : int,nz : int) -> None: 
        """
        None
        """
    def glNormal3sv(self,theVec : int) -> None: 
        """
        None
        """
    def glNormalPointer(self,theType : int,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    def glOrtho(self,theLeft : float,theRight : float,theBottom : float,theTop : float,theNearVal : float,theFarVal : float) -> None: 
        """
        None
        """
    def glPassThrough(self,token : float) -> None: 
        """
        None
        """
    def glPixelZoom(self,xfactor : float,yfactor : float) -> None: 
        """
        None
        """
    def glPolygonStipple(self,theMask : int) -> None: 
        """
        None
        """
    def glPopAttrib(self) -> None: 
        """
        None
        """
    def glPopClientAttrib(self) -> None: 
        """
        None
        """
    def glPopMatrix(self) -> None: 
        """
        None
        """
    def glPopName(self) -> None: 
        """
        None
        """
    def glPrioritizeTextures(self,n : int,textures : int,priorities : float) -> None: ...
    def glPushAttrib(self,theMask : int) -> None: ...
    def glPushClientAttrib(self,theMask : int) -> None: 
        """
        None
        """
    def glPushMatrix(self) -> None: 
        """
        None
        """
    def glPushName(self,theName : int) -> None: 
        """
        None
        """
    def glRasterPos2d(self,x : float,y : float) -> None: ...
    def glRasterPos2dv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos2f(self,x : float,y : float) -> None: 
        """
        None
        """
    def glRasterPos2fv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos2i(self,x : int,y : int) -> None: 
        """
        None
        """
    def glRasterPos2iv(self,theVec : int) -> None: 
        """
        None
        """
    def glRasterPos2s(self,x : int,y : int) -> None: 
        """
        None
        """
    def glRasterPos2sv(self,theVec : int) -> None: 
        """
        None
        """
    def glRasterPos3d(self,x : float,y : float,z : float) -> None: 
        """
        None
        """
    def glRasterPos3dv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos3f(self,x : float,y : float,z : float) -> None: 
        """
        None
        """
    def glRasterPos3fv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos3i(self,x : int,y : int,z : int) -> None: 
        """
        None
        """
    def glRasterPos3iv(self,theVec : int) -> None: 
        """
        None
        """
    def glRasterPos3s(self,x : int,y : int,z : int) -> None: 
        """
        None
        """
    def glRasterPos3sv(self,theVec : int) -> None: 
        """
        None
        """
    def glRasterPos4d(self,x : float,y : float,z : float,w : float) -> None: 
        """
        None
        """
    def glRasterPos4dv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos4f(self,x : float,y : float,z : float,w : float) -> None: 
        """
        None
        """
    def glRasterPos4fv(self,theVec : float) -> None: 
        """
        None
        """
    def glRasterPos4i(self,x : int,y : int,z : int,w : int) -> None: 
        """
        None
        """
    def glRasterPos4iv(self,theVec : int) -> None: 
        """
        None
        """
    def glRasterPos4s(self,x : int,y : int,z : int,w : int) -> None: 
        """
        None
        """
    def glRasterPos4sv(self,theVec : int) -> None: 
        """
        None
        """
    def glRectd(self,x1 : float,y1 : float,x2 : float,y2 : float) -> None: 
        """
        None
        """
    def glRectdv(self,v1 : float,v2 : float) -> None: 
        """
        None
        """
    def glRectf(self,x1 : float,y1 : float,x2 : float,y2 : float) -> None: 
        """
        None
        """
    def glRectfv(self,v1 : float,v2 : float) -> None: 
        """
        None
        """
    def glRecti(self,x1 : int,y1 : int,x2 : int,y2 : int) -> None: 
        """
        None
        """
    def glRectiv(self,v1 : int,v2 : int) -> None: 
        """
        None
        """
    def glRects(self,x1 : int,y1 : int,x2 : int,y2 : int) -> None: 
        """
        None
        """
    def glRectsv(self,v1 : int,v2 : int) -> None: 
        """
        None
        """
    def glRotated(self,theAngleDegrees : float,theX : float,theY : float,theZ : float) -> None: 
        """
        None
        """
    def glScaled(self,theX : float,theY : float,theZ : float) -> None: 
        """
        None
        """
    def glSelectBuffer(self,theSize : int,theBuffer : int) -> None: 
        """
        None
        """
    def glShadeModel(self,theMode : int) -> None: ...
    def glTexCoord1d(self,s : float) -> None: 
        """
        None
        """
    def glTexCoord1dv(self,theVec1 : float) -> None: 
        """
        None
        """
    def glTexCoord1f(self,s : float) -> None: 
        """
        None
        """
    def glTexCoord1fv(self,theVec1 : float) -> None: 
        """
        None
        """
    def glTexCoord1i(self,s : int) -> None: 
        """
        None
        """
    def glTexCoord1iv(self,theVec1 : int) -> None: 
        """
        None
        """
    def glTexCoord1s(self,s : int) -> None: 
        """
        None
        """
    def glTexCoord1sv(self,theVec1 : int) -> None: 
        """
        None
        """
    def glTexCoord2d(self,s : float,t : float) -> None: 
        """
        None
        """
    def glTexCoord2dv(self,theVec2 : float) -> None: 
        """
        None
        """
    def glTexCoord2f(self,s : float,t : float) -> None: 
        """
        None
        """
    def glTexCoord2fv(self,theVec2 : float) -> None: 
        """
        None
        """
    def glTexCoord2i(self,s : int,t : int) -> None: 
        """
        None
        """
    def glTexCoord2iv(self,theVec2 : int) -> None: 
        """
        None
        """
    def glTexCoord2s(self,s : int,t : int) -> None: 
        """
        None
        """
    def glTexCoord2sv(self,theVec : int) -> None: 
        """
        None
        """
    def glTexCoord3d(self,s : float,t : float,r : float) -> None: 
        """
        None
        """
    def glTexCoord3dv(self,theVec3 : float) -> None: 
        """
        None
        """
    def glTexCoord3f(self,s : float,t : float,r : float) -> None: 
        """
        None
        """
    def glTexCoord3fv(self,theVec3 : float) -> None: 
        """
        None
        """
    def glTexCoord3i(self,s : int,t : int,r : int) -> None: 
        """
        None
        """
    def glTexCoord3iv(self,theVec3 : int) -> None: 
        """
        None
        """
    def glTexCoord3s(self,s : int,t : int,r : int) -> None: 
        """
        None
        """
    def glTexCoord3sv(self,theVec3 : int) -> None: 
        """
        None
        """
    def glTexCoord4d(self,s : float,t : float,r : float,q : float) -> None: 
        """
        None
        """
    def glTexCoord4dv(self,theVec4 : float) -> None: 
        """
        None
        """
    def glTexCoord4f(self,s : float,t : float,r : float,q : float) -> None: 
        """
        None
        """
    def glTexCoord4fv(self,theVec4 : float) -> None: 
        """
        None
        """
    def glTexCoord4i(self,s : int,t : int,r : int,q : int) -> None: 
        """
        None
        """
    def glTexCoord4iv(self,theVec4 : int) -> None: 
        """
        None
        """
    def glTexCoord4s(self,s : int,t : int,r : int,q : int) -> None: 
        """
        None
        """
    def glTexCoord4sv(self,theVec4 : int) -> None: 
        """
        None
        """
    def glTexCoordPointer(self,theSize : int,theType : int,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    def glTexGend(self,coord : int,pname : int,param : float) -> None: ...
    def glTexGendv(self,coord : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glTexGenf(self,coord : int,pname : int,param : float) -> None: 
        """
        None
        """
    def glTexGenfv(self,coord : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glTexGeni(self,coord : int,pname : int,param : int) -> None: 
        """
        None
        """
    def glTexGeniv(self,coord : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glTranslated(self,theX : float,theY : float,theZ : float) -> None: 
        """
        None
        """
    def glVertex2d(self,theX : float,theY : float) -> None: 
        """
        None
        """
    def glVertex2dv(self,theVec2 : float) -> None: 
        """
        None
        """
    def glVertex2f(self,theX : float,theY : float) -> None: 
        """
        None
        """
    def glVertex2fv(self,theVec2 : float) -> None: 
        """
        None
        """
    def glVertex2i(self,theX : int,theY : int) -> None: 
        """
        None
        """
    def glVertex2iv(self,theVec2 : int) -> None: 
        """
        None
        """
    def glVertex2s(self,theX : int,theY : int) -> None: 
        """
        None
        """
    def glVertex2sv(self,theVec2 : int) -> None: 
        """
        None
        """
    def glVertex3d(self,theX : float,theY : float,theZ : float) -> None: 
        """
        None
        """
    def glVertex3dv(self,theVec3 : float) -> None: 
        """
        None
        """
    def glVertex3f(self,theX : float,theY : float,theZ : float) -> None: 
        """
        None
        """
    def glVertex3fv(self,theVec3 : float) -> None: 
        """
        None
        """
    def glVertex3i(self,theX : int,theY : int,theZ : int) -> None: 
        """
        None
        """
    def glVertex3iv(self,theVec3 : int) -> None: 
        """
        None
        """
    def glVertex3s(self,theX : int,theY : int,theZ : int) -> None: 
        """
        None
        """
    def glVertex3sv(self,theVec3 : int) -> None: 
        """
        None
        """
    def glVertex4d(self,theX : float,theY : float,theZ : float,theW : float) -> None: 
        """
        None
        """
    def glVertex4dv(self,theVec4 : float) -> None: 
        """
        None
        """
    def glVertex4f(self,theX : float,theY : float,theZ : float,theW : float) -> None: 
        """
        None
        """
    def glVertex4fv(self,theVec4 : float) -> None: 
        """
        None
        """
    def glVertex4i(self,theX : int,theY : int,theZ : int,theW : int) -> None: 
        """
        None
        """
    def glVertex4iv(self,theVec4 : int) -> None: 
        """
        None
        """
    def glVertex4s(self,theX : int,theY : int,theZ : int,theW : int) -> None: 
        """
        None
        """
    def glVertex4sv(self,theVec4 : int) -> None: 
        """
        None
        """
    def glVertexPointer(self,theSize : int,theType : int,theStride : int,thePtr : capsule) -> None: 
        """
        None
        """
    pass
class OpenGl_GlCore11Fwd():
    """
    OpenGL 1.1 core without deprecated Fixed Pipeline entry points. Notice that all functions within this structure are actually exported by system GL library. The main purpose for these hint - to control visibility of functions per GL version (global functions should not be used directly to achieve this effect!).
    """
    def __init__(self) -> None: ...
    def glAlphaFunc(self,theFunc : int,theRef : float) -> None: 
        """
        None
        """
    def glBindTexture(self,target : int,texture : int) -> None: 
        """
        None
        """
    def glBlendFunc(self,sfactor : int,dfactor : int) -> None: 
        """
        None
        """
    def glClear(self,theMask : int) -> None: 
        """
        None
        """
    def glClearColor(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: ...
    def glClearDepth(self,theDepth : float) -> None: ...
    def glClearDepthf(self,theDepth : float) -> None: 
        """
        None
        """
    def glClearStencil(self,s : int) -> None: 
        """
        None
        """
    def glColorMask(self,theRed : int,theGreen : int,theBlue : int,theAlpha : int) -> None: 
        """
        None
        """
    def glCopyTexImage1D(self,target : int,level : int,internalformat : int,x : int,y : int,width : int,border : int) -> None: 
        """
        None
        """
    def glCopyTexImage2D(self,target : int,level : int,internalformat : int,x : int,y : int,width : int,height : int,border : int) -> None: 
        """
        None
        """
    def glCopyTexSubImage1D(self,target : int,level : int,xoffset : int,x : int,y : int,width : int) -> None: 
        """
        None
        """
    def glCopyTexSubImage2D(self,target : int,level : int,xoffset : int,yoffset : int,x : int,y : int,width : int,height : int) -> None: 
        """
        None
        """
    def glCullFace(self,theMode : int) -> None: 
        """
        None
        """
    def glDeleteTextures(self,n : int,textures : int) -> None: 
        """
        None
        """
    def glDepthFunc(self,theFunc : int) -> None: 
        """
        None
        """
    def glDepthMask(self,theFlag : int) -> None: 
        """
        None
        """
    def glDepthRange(self,theNearValue : float,theFarValue : float) -> None: 
        """
        None
        """
    def glDepthRangef(self,theNearValue : float,theFarValue : float) -> None: 
        """
        None
        """
    def glDisable(self,theCap : int) -> None: 
        """
        None
        """
    def glDrawArrays(self,theMode : int,theFirst : int,theCount : int) -> None: ...
    def glDrawElements(self,theMode : int,theCount : int,theType : int,theIndices : capsule) -> None: 
        """
        None
        """
    def glEnable(self,theCap : int) -> None: 
        """
        None
        """
    def glFinish(self) -> None: 
        """
        None
        """
    def glFlush(self) -> None: 
        """
        None
        """
    def glFrontFace(self,theMode : int) -> None: 
        """
        None
        """
    def glGenTextures(self,n : int,textures : int) -> None: 
        """
        None
        """
    def glGetBooleanv(self,theParamName : int,theValues : int) -> None: 
        """
        None
        """
    def glGetError(self) -> int: 
        """
        None
        """
    def glGetFloatv(self,theParamName : int,theValues : float) -> None: 
        """
        None
        """
    def glGetIntegerv(self,theParamName : int,theValues : int) -> None: 
        """
        None
        """
    def glGetString(self,theName : int) -> int: 
        """
        None
        """
    def glGetTexImage(self,target : int,level : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glGetTexParameterfv(self,target : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glGetTexParameteriv(self,target : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glHint(self,theTarget : int,theMode : int) -> None: 
        """
        None
        """
    def glIsEnabled(self,theCap : int) -> int: 
        """
        None
        """
    def glIsTexture(self,texture : int) -> int: 
        """
        None
        """
    def glLineWidth(self,theWidth : float) -> None: 
        """
        None
        """
    def glPixelStorei(self,theParamName : int,theParam : int) -> None: ...
    def glPointSize(self,theSize : float) -> None: 
        """
        None
        """
    def glPolygonOffset(self,theFactor : float,theUnits : float) -> None: 
        """
        None
        """
    def glReadPixels(self,x : int,y : int,width : int,height : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glScissor(self,theX : int,theY : int,theWidth : int,theHeight : int) -> None: 
        """
        None
        """
    def glStencilFunc(self,func : int,ref : int,mask : int) -> None: ...
    def glStencilMask(self,mask : int) -> None: 
        """
        None
        """
    def glStencilOp(self,fail : int,zfail : int,zpass : int) -> None: 
        """
        None
        """
    def glTexImage1D(self,target : int,level : int,internalFormat : int,width : int,border : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glTexImage2D(self,target : int,level : int,internalFormat : int,width : int,height : int,border : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glTexParameterf(self,target : int,pname : int,param : float) -> None: ...
    def glTexParameterfv(self,target : int,pname : int,params : float) -> None: 
        """
        None
        """
    def glTexParameteri(self,target : int,pname : int,param : int) -> None: 
        """
        None
        """
    def glTexParameteriv(self,target : int,pname : int,params : int) -> None: 
        """
        None
        """
    def glTexSubImage1D(self,target : int,level : int,xoffset : int,width : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glTexSubImage2D(self,target : int,level : int,xoffset : int,yoffset : int,width : int,height : int,format : int,type : int,pixels : capsule) -> None: 
        """
        None
        """
    def glViewport(self,theX : int,theY : int,theWidth : int,theHeight : int) -> None: ...
    pass
class OpenGl_GlCore12():
    """
    OpenGL 1.2 core based on 1.1 version.
    """
    pass
class OpenGl_GlCore12Fwd():
    """
    OpenGL 1.2 core based on 1.1 version.
    """
    pass
class OpenGl_GlCore13():
    """
    OpenGL 1.3 core based on 1.2 version.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_GlCore13Fwd():
    """
    OpenGL 1.3 without deprecated entry points.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_GlCore14():
    """
    OpenGL 1.4 core based on 1.3 version.
    """
    pass
class OpenGl_GlCore14Fwd():
    """
    OpenGL 1.4 core based on 1.3 version.
    """
    pass
class OpenGl_GlCore15():
    """
    OpenGL 1.5 core based on 1.4 version.
    """
    pass
class OpenGl_GlCore15Fwd():
    """
    OpenGL 1.5 core based on 1.4 version.
    """
    pass
class OpenGl_GlCore20():
    """
    OpenGL 2.0 core based on 1.5 version.
    """
    pass
class OpenGl_GlCore20Fwd():
    """
    OpenGL 2.0 core based on 1.5 version.
    """
    pass
class OpenGl_GlCore21():
    """
    OpenGL 2.1 core based on 2.0 version.
    """
    pass
class OpenGl_GlCore21Fwd():
    """
    OpenGL 2.1 core based on 2.0 version.
    """
    pass
class OpenGl_GlCore30():
    """
    OpenGL 3.0 core. This is first version with deprecation model introduced - a lot of functionality regarding to fixed pipeline were marked deprecated. Notice that nothing were actually removed in this version (unless Forward context loaded)!
    """
    pass
class OpenGl_GlCore30Fwd():
    """
    OpenGL 3.0 core. This is first version with deprecation model introduced - a lot of functionality regarding to fixed pipeline were marked deprecated. Notice that nothing were actually removed in this version (unless Forward context loaded)!
    """
    pass
class OpenGl_GlCore31():
    """
    OpenGL 3.1 definition.
    """
    pass
class OpenGl_GlCore31Back():
    """
    OpenGL 3.1 definition.
    """
    pass
class OpenGl_GlCore32():
    """
    OpenGL 3.2 definition.
    """
    pass
class OpenGl_GlCore32Back():
    """
    OpenGL 3.2 definition.
    """
    pass
class OpenGl_GlCore33():
    """
    OpenGL 3.3 definition.
    """
    pass
class OpenGl_GlCore33Back():
    """
    OpenGL 3.3 definition.
    """
    pass
class OpenGl_GlCore40():
    """
    OpenGL 4.0 definition.
    """
    pass
class OpenGl_GlCore40Back():
    """
    OpenGL 4.0 definition.
    """
    pass
class OpenGl_GlCore41():
    """
    OpenGL 4.1 definition.
    """
    pass
class OpenGl_GlCore41Back():
    """
    OpenGL 4.1 definition.
    """
    pass
class OpenGl_GlCore42():
    """
    OpenGL 4.2 definition.
    """
    pass
class OpenGl_GlCore42Back():
    """
    OpenGL 4.2 definition.
    """
    pass
class OpenGl_GlCore43():
    """
    OpenGL 4.3 definition.
    """
    pass
class OpenGl_GlCore43Back():
    """
    OpenGL 4.3 definition.
    """
    pass
class OpenGl_GlCore44():
    """
    OpenGL 4.4 definition.
    """
    pass
class OpenGl_GlCore44Back():
    """
    OpenGL 4.4 definition.
    """
    pass
class OpenGl_GlCore45():
    """
    OpenGL 4.5 definition.
    """
    pass
class OpenGl_GlCore45Back():
    """
    OpenGL 4.5 definition.
    """
    pass
class OpenGl_GlFunctions():
    """
    Mega structure defines the complete list of OpenGL functions.
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_GraphicDriver(OCP.Graphic3d.Graphic3d_GraphicDriver, OCP.Standard.Standard_Transient):
    """
    This class defines an OpenGl graphic driverThis class defines an OpenGl graphic driver
    """
    def ChangeOptions(self) -> OpenGl_Caps: 
        """
        Returns the visualization options
        """
    def CreateRenderWindow(self,theWindow : OCP.Aspect.Aspect_Window,theContext : capsule) -> OpenGl_Window: 
        """
        None
        """
    def CreateStructure(self,theManager : OCP.Graphic3d.Graphic3d_StructureManager) -> OCP.Graphic3d.Graphic3d_CStructure: 
        """
        None
        """
    def CreateView(self,theMgr : OCP.Graphic3d.Graphic3d_StructureManager) -> OCP.Graphic3d.Graphic3d_CView: 
        """
        None
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefaultTextHeight(self) -> float: 
        """
        None
        """
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
    def EnableVBO(self,theToTurnOn : bool) -> None: 
        """
        VBO usage can be forbidden by this method even if it is supported by GL driver. Notice that disabling of VBO will cause rendering performance degradation. Warning! This method should be called only before any primitives are displayed in GL scene!
        """
    def GetDisplayConnection(self) -> OCP.Aspect.Aspect_DisplayConnection: 
        """
        returns Handle to display connection
        """
    def GetNextPrimitiveArrayUID(self) -> int: 
        """
        Returns unique ID for primitive arrays.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetSharedContext(self,theBound : bool=False) -> OpenGl_Context: 
        """
        Method to retrieve valid GL context. Could return NULL-handle if no window created by this driver.
        """
    def GetStateCounter(self) -> OpenGl_StateCounter: 
        """
        State counter for OpenGl structures.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitContext(self) -> bool: 
        """
        Perform initialization of default OpenGL context.
        """
    def InquireLightLimit(self) -> int: 
        """
        Request maximum number of active light sources supported by driver and hardware.
        """
    def InquireLimit(self,theType : OCP.Graphic3d.Graphic3d_TypeOfLimit) -> int: 
        """
        Request limit of graphic resource of specific type.
        """
    def InquirePlaneLimit(self) -> int: 
        """
        Request maximum number of active clipping planes supported by driver and hardware.
        """
    def InquireViewLimit(self) -> int: 
        """
        Request maximum number of views supported by driver.
        """
    def InsertLayerAfter(self,theNewLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerBefore : int) -> None: 
        """
        Adds a layer to all views.
        """
    def InsertLayerBefore(self,theNewLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerAfter : int) -> None: 
        """
        Adds a layer to all views.
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
    def MemoryInfo(self,theFreeBytes : int,theInfo : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Returns information about GPU memory usage. Please read OpenGl_Context::MemoryInfo() for more description.
        """
    def NewIdentification(self) -> int: 
        """
        Returns a new identification number for a new structure.
        """
    def Options(self) -> OpenGl_Caps: 
        """
        Returns the visualization options
        """
    def ReleaseContext(self) -> None: 
        """
        Release default context.
        """
    def RemoveIdentification(self,theId : int) -> None: 
        """
        Frees the identifier of a structure.
        """
    def RemoveStructure(self,theCStructure : OCP.Graphic3d.Graphic3d_CStructure) -> Any: 
        """
        None
        """
    def RemoveView(self,theView : OCP.Graphic3d.Graphic3d_CView) -> None: 
        """
        None
        """
    def RemoveZLayer(self,theLayerId : int) -> None: 
        """
        Removes Z layer. All structures displayed at the moment in layer will be displayed in default layer (the bottom-level z layer). By default, there are always default bottom-level layer that can't be removed. The passed theLayerId should be not less than 0 (reserved for default layers that can not be removed).
        """
    def SetBuffersNoSwap(self,theIsNoSwap : bool) -> None: 
        """
        Specify swap buffer behavior.
        """
    def SetZLayerSettings(self,theLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings) -> None: 
        """
        Sets the settings for a single Z layer.
        """
    def TextSize(self,theView : OCP.Graphic3d.Graphic3d_CView,theText : str,theHeight : float,theWidth : float,theAscent : float,theDescent : float) -> None: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewExists(self,theWindow : OCP.Aspect.Aspect_Window,theView : OCP.Graphic3d.Graphic3d_CView) -> bool: 
        """
        None
        """
    def ZLayerSettings(self,theLayerId : int) -> OCP.Graphic3d.Graphic3d_ZLayerSettings: 
        """
        Returns the settings of a single Z layer.
        """
    def ZLayers(self,theLayerSeq : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Returns list of Z layers defined for the graphical driver.
        """
    def __init__(self,theDisp : OCP.Aspect.Aspect_DisplayConnection,theToInitialize : bool=True) -> None: ...
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
    def setDeviceLost(self) -> None: 
        """
        Set device lost flag for redrawn views.
        """
    pass
class OpenGl_Group(OCP.Graphic3d.Graphic3d_Group, OCP.Standard.Standard_Transient):
    """
    Implementation of low-level graphic group.Implementation of low-level graphic group.Implementation of low-level graphic group.
    """
    def AddElement(self,theElem : OpenGl_Element) -> None: 
        """
        None
        """
    def AddPrimitiveArray(self,theType : OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theAttribs : OCP.Graphic3d.Graphic3d_Buffer,theBounds : OCP.Graphic3d.Graphic3d_BoundBuffer,theToEvalMinMax : bool) -> None: 
        """
        Add primitive array element
        """
    def AddText(self,theTextParams : OCP.Graphic3d.Graphic3d_Text,theToEvalMinMax : bool) -> None: 
        """
        Adds a text for display
        """
    def Aspects(self) -> OCP.Graphic3d.Graphic3d_Aspects: 
        """
        Return line aspect.
        """
    def BoundingBox(self) -> Any: 
        """
        Returns boundary box of the group <me> without transformation applied,
        """
    def ChangeBoundingBox(self) -> Any: 
        """
        Returns non-const boundary box of the group <me> without transformation applied,
        """
    def Clear(self,theToUpdateStructureMgr : bool) -> None: 
        """
        None
        """
    def ContainsFacet(self) -> bool: 
        """
        Returns true if the group contains Polygons, Triangles or Quadrangles.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def FirstNode(self) -> OpenGl_ElementNode: 
        """
        Returns first OpenGL element node of the group.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlAspects(self) -> OpenGl_Aspects: 
        """
        Returns OpenGL aspect.
        """
    def GlStruct(self) -> OpenGl_Structure: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsClosed(self) -> bool: 
        """
        Return true if primitive arrays within this graphic group form closed volume (do no contain open shells).
        """
    def IsDeleted(self) -> bool: 
        """
        Returns Standard_True if the group <me> is deleted. <me> is deleted after the call Remove (me) or the associated structure is deleted.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns Standard_True if the group <me> is empty.
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
    def IsRaytracable(self) -> bool: 
        """
        Is the group ray-tracable (contains ray-tracable elements)?
        """
    def Marker(self,thePoint : OCP.Graphic3d.Graphic3d_Vertex,theToEvalMinMax : bool=True) -> None: 
        """
        Creates a primitive array with single marker using AddPrimitiveArray().
        """
    def MinMaxValues(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the coordinates of the boundary box of the group.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        None
        """
    def Remove(self) -> None: 
        """
        Supress the group <me> in the structure. Warning: No more graphic operations in <me> after this call. Modifies the current modelling transform persistence (pan, zoom or rotate) Get the current modelling transform persistence (pan, zoom or rotate)
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        None
        """
    def ReplaceAspects(self,theMap : Any) -> None: 
        """
        Replace aspects specified in the replacement map.
        """
    def SetClosed(self,theIsClosed : bool) -> None: 
        """
        Changes property shown that primitive arrays within this group form closed volume (do no contain open shells).
        """
    def SetFlippingOptions(self,theIsEnabled : bool,theRefPlane : OCP.gp.gp_Ax2) -> None: 
        """
        Add flipping element
        """
    def SetGroupPrimitivesAspect(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Update aspect.
        """
    def SetMinMaxValues(self,theXMin : float,theYMin : float,theZMin : float,theXMax : float,theYMax : float,theZMax : float) -> None: 
        """
        Sets the coordinates of the boundary box of the group.
        """
    def SetPrimitivesAspect(self,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Append aspect as an element.
        """
    def SetStencilTestOptions(self,theIsEnabled : bool) -> None: 
        """
        Add stencil test element
        """
    def Structure(self) -> OCP.Graphic3d.Graphic3d_Structure: 
        """
        Returns the structure containing the group <me>.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update presentation aspects after their modification.
        """
    @overload
    def Text(self,theTextUtf : str,theOrientation : OCP.gp.gp_Ax2,theHeight : float,theAngle : float,theTp : OCP.Graphic3d.Graphic3d_TextPath,theHTA : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,theVTA : OCP.Graphic3d.Graphic3d_VerticalTextAlignment,theToEvalMinMax : bool=True,theHasOwnAnchor : bool=True) -> None: 
        """
        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). AAngle : Orientation of the text (with respect to the horizontal).

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). The other attributes have the following default values: AAngle : PI / 2. ATp : TP_RIGHT AHta : HTA_LEFT AVta : VTA_BOTTOM

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). AAngle : Orientation of the text (with respect to the horizontal).

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). The other attributes have the following default values: AAngle : PI / 2. ATp : TP_RIGHT AHta : HTA_LEFT AVta : VTA_BOTTOM

        Creates the string <theText> at orientation <theOrientation> in 3D space.

        Creates the string <theText> at orientation <theOrientation> in 3D space.
        """
    @overload
    def Text(self,AText : str,APoint : OCP.Graphic3d.Graphic3d_Vertex,AHeight : float,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,theText : OCP.TCollection.TCollection_ExtendedString,theOrientation : OCP.gp.gp_Ax2,theHeight : float,theAngle : float,theTp : OCP.Graphic3d.Graphic3d_TextPath,theHTA : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,theVTA : OCP.Graphic3d.Graphic3d_VerticalTextAlignment,theToEvalMinMax : bool=True,theHasOwnAnchor : bool=True) -> None: ...
    @overload
    def Text(self,AText : str,APoint : OCP.Graphic3d.Graphic3d_Vertex,AHeight : float,AAngle : float,ATp : OCP.Graphic3d.Graphic3d_TextPath,AHta : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,AVta : OCP.Graphic3d.Graphic3d_VerticalTextAlignment,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,AText : OCP.TCollection.TCollection_ExtendedString,APoint : OCP.Graphic3d.Graphic3d_Vertex,AHeight : float,AAngle : float,ATp : OCP.Graphic3d.Graphic3d_TextPath,AHta : OCP.Graphic3d.Graphic3d_HorizontalTextAlignment,AVta : OCP.Graphic3d.Graphic3d_VerticalTextAlignment,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,AText : OCP.TCollection.TCollection_ExtendedString,APoint : OCP.Graphic3d.Graphic3d_Vertex,AHeight : float,EvalMinMax : bool=True) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theStruct : OCP.Graphic3d.Graphic3d_Structure) -> None: ...
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
class OpenGl_HaltonSampler():
    """
    Compute points of the Halton sequence with digit-permutations for different bases.
    """
    def __init__(self) -> None: ...
    @staticmethod
    def get_num_dimensions_s() -> int: 
        """
        Return the number of supported dimensions.
        """
    def sample(self,theDimension : int,theIndex : int) -> float: 
        """
        Return the Halton sample for the given dimension (component) and index. The client must have called initFaure() at least once before. dimension must be smaller than the value returned by get_num_dimensions().
        """
    pass
class OpenGl_VertexBuffer(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Vertex Buffer Object - is a general storage object for vertex attributes (position, normal, color). Notice that you should use OpenGl_IndexBuffer specialization for array of indices.Vertex Buffer Object - is a general storage object for vertex attributes (position, normal, color). Notice that you should use OpenGl_IndexBuffer specialization for array of indices.
    """
    def Bind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind this VBO.
        """
    def BindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind all vertex attributes to active program OpenGl_Context::ActiveProgram() or for FFP. Default implementation does nothing.
        """
    def BindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Bind this VBO and enable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def BindPositionAttribute(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind vertex position attribute only. Default implementation does nothing.
        """
    def BindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Bind this VBO to active GLSL program.
        """
    def Create(self,theGlCtx : OpenGl_Context) -> bool: 
        """
        Creates VBO name (id) if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetComponentsNb(self) -> int: 
        """
        Returns the number of components per generic vertex attribute.
        """
    def GetDataOffset(self) -> int: 
        """
        Returns offset to data, NULL by default
        """
    def GetDataType(self) -> int: 
        """
        Returns data type of each component in the array.
        """
    def GetElemsNb(self) -> int: 
        """
        Returns number of vertex attributes / number of vertices specified within ::Init()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: 
        """
        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: ...
    def GetTarget(self) -> int: 
        """
        None
        """
    def HasColorAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex color attribute
        """
    def HasNormalAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex normal attribute
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : int) -> bool: 
        """
        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : float) -> bool: ...
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def IsVirtual(self) -> bool: 
        """
        Return TRUE if this is a virtual (for backward compatibility) VBO object.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def SetElemsNb(self,theNbElems : int) -> None: 
        """
        Overrides the number of vertex attributes / number of vertexes. It is up to user specifying this number correct (e.g. below initial value)!
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: 
        """
        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unbind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind this VBO.
        """
    def UnbindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind all vertex attributes. Default implementation does nothing.
        """
    def UnbindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Unbind this VBO and disable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def UnbindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Unbind any VBO from active GLSL program.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def bindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theNbComp : int,theDataType : int,theStride : int,theOffset : capsule) -> None: 
        """
        Setup array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using bindFixed() when no program bound.
        """
    def getSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Read back buffer sub-range.
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
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Initialize buffer with new data.

        Initialize buffer with new data.
        """
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int,theStride : int) -> bool: ...
    @staticmethod
    def sizeOfGlType_s(theType : int) -> int: 
        """
        Returns size of specified GL type
        """
    def subData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Update part of the buffer with new data.
        """
    @staticmethod
    def unbindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Disable GLSL array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using unbindFixed() when no program bound.
        """
    pass
class OpenGl_LayerFilter():
    """
    Tool object to specify processed OpenGL layers for intermixed rendering of raytracable and non-raytracable layers.

    Members:

      OpenGl_LF_All

      OpenGl_LF_Upper

      OpenGl_LF_Bottom

      OpenGl_LF_RayTracable
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
    OpenGl_LF_All: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_All: 0>
    OpenGl_LF_Bottom: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_Bottom: 2>
    OpenGl_LF_RayTracable: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_RayTracable: 3>
    OpenGl_LF_Upper: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_Upper: 1>
    __entries: dict # value = {'OpenGl_LF_All': (<OpenGl_LayerFilter.OpenGl_LF_All: 0>, None), 'OpenGl_LF_Upper': (<OpenGl_LayerFilter.OpenGl_LF_Upper: 1>, None), 'OpenGl_LF_Bottom': (<OpenGl_LayerFilter.OpenGl_LF_Bottom: 2>, None), 'OpenGl_LF_RayTracable': (<OpenGl_LayerFilter.OpenGl_LF_RayTracable: 3>, None)}
    __members__: dict # value = {'OpenGl_LF_All': <OpenGl_LayerFilter.OpenGl_LF_All: 0>, 'OpenGl_LF_Upper': <OpenGl_LayerFilter.OpenGl_LF_Upper: 1>, 'OpenGl_LF_Bottom': <OpenGl_LayerFilter.OpenGl_LF_Bottom: 2>, 'OpenGl_LF_RayTracable': <OpenGl_LayerFilter.OpenGl_LF_RayTracable: 3>}
    pass
class OpenGl_StateInterface():
    """
    Defines interface for OpenGL state.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_LineAttributes(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Utility class to manage OpenGL resources of polygon hatching styles.Utility class to manage OpenGL resources of polygon hatching styles.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage - not implemented.
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
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Release GL resources.
        """
    def SetTypeOfHatch(self,theGlCtx : OpenGl_Context,theStyle : OCP.Graphic3d.Graphic3d_HatchStyle) -> bool: 
        """
        Sets type of the hatch.
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
class OpenGl_ListOfStructure(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theOther : OpenGl_ListOfStructure) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : OpenGl_Structure,theIter : Any) -> None: ...
    @overload
    def Append(self,theItem : OpenGl_Structure) -> OpenGl_Structure: ...
    def Assign(self,theOther : OpenGl_ListOfStructure) -> OpenGl_ListOfStructure: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> OpenGl_Structure: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theOther : OpenGl_ListOfStructure,theIter : Any) -> None: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theItem : OpenGl_Structure,theIter : Any) -> OpenGl_Structure: ...
    @overload
    def InsertBefore(self,theOther : OpenGl_ListOfStructure,theIter : Any) -> None: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theItem : OpenGl_Structure,theIter : Any) -> OpenGl_Structure: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> OpenGl_Structure: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : OpenGl_ListOfStructure) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : OpenGl_Structure) -> OpenGl_Structure: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self,theOther : OpenGl_ListOfStructure) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class OpenGl_Material():
    """
    OpenGL material definition
    """
    def Init(self,theCtx : OpenGl_Context,theProp : OCP.Graphic3d.Graphic3d_MaterialAspect,theInteriorColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Initialize material
        """
    def IsEqual(self,theOther : OpenGl_Material) -> bool: 
        """
        Check this material for equality with another material (without tolerance!).
        """
    def SetColor(self,theColor : OCP.Graphic3d.Graphic3d_Vec4) -> None: 
        """
        Set material color.
        """
    def __init__(self) -> None: ...
    @property
    def Common(self) -> OpenGl_MaterialCommon:
        """
        :type: OpenGl_MaterialCommon
        """
    @Common.setter
    def Common(self, arg0: OpenGl_MaterialCommon) -> None:
        pass
    @property
    def Pbr(self) -> OpenGl_MaterialPBR:
        """
        :type: OpenGl_MaterialPBR
        """
    @Pbr.setter
    def Pbr(self, arg0: OpenGl_MaterialPBR) -> None:
        pass
    pass
class OpenGl_MaterialCommon():
    """
    OpenGL material definition
    """
    def ChangeShine(self) -> float: 
        """
        None
        """
    def ChangeTransparency(self) -> float: 
        """
        None
        """
    @staticmethod
    def NbOfVec4_s() -> int: 
        """
        None
        """
    def Packed(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns packed (serialized) representation of material properties
        """
    def Shine(self) -> float: 
        """
        None
        """
    def Transparency(self) -> float: 
        """
        None
        """
    def __init__(self) -> None: ...
    @property
    def Ambient(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Ambient.setter
    def Ambient(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def Diffuse(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Diffuse.setter
    def Diffuse(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def Emission(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Emission.setter
    def Emission(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def Params(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Params.setter
    def Params(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def Specular(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Specular.setter
    def Specular(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    pass
class OpenGl_MaterialFlag():
    """
    Material flag

    Members:

      OpenGl_MaterialFlag_Front

      OpenGl_MaterialFlag_Back
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
    OpenGl_MaterialFlag_Back: OCP.OpenGl.OpenGl_MaterialFlag # value = <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Back: 1>
    OpenGl_MaterialFlag_Front: OCP.OpenGl.OpenGl_MaterialFlag # value = <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Front: 0>
    __entries: dict # value = {'OpenGl_MaterialFlag_Front': (<OpenGl_MaterialFlag.OpenGl_MaterialFlag_Front: 0>, None), 'OpenGl_MaterialFlag_Back': (<OpenGl_MaterialFlag.OpenGl_MaterialFlag_Back: 1>, None)}
    __members__: dict # value = {'OpenGl_MaterialFlag_Front': <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Front: 0>, 'OpenGl_MaterialFlag_Back': <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Back: 1>}
    pass
class OpenGl_MaterialPBR():
    """
    OpenGL material definition
    """
    def ChangeMetallic(self) -> float: 
        """
        None
        """
    def ChangeRoughness(self) -> float: 
        """
        None
        """
    def Metallic(self) -> float: 
        """
        None
        """
    @staticmethod
    def NbOfVec4_s() -> int: 
        """
        None
        """
    def Packed(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns packed (serialized) representation of material properties
        """
    def Roughness(self) -> float: 
        """
        None
        """
    def __init__(self) -> None: ...
    @property
    def BaseColor(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @BaseColor.setter
    def BaseColor(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def EmissionIOR(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @EmissionIOR.setter
    def EmissionIOR(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    @property
    def Params(self) -> OCP.Graphic3d.Graphic3d_Vec4:
        """
        :type: OCP.Graphic3d.Graphic3d_Vec4
        """
    @Params.setter
    def Params(self, arg0: OCP.Graphic3d.Graphic3d_Vec4) -> None:
        pass
    pass
class OpenGl_MaterialState(OpenGl_StateInterface):
    """
    Defines generic state of material properties.
    """
    def AlphaCutoff(self) -> float: 
        """
        Alpha cutoff value.
        """
    def BackMaterial(self) -> OpenGl_Material: 
        """
        Return back material.
        """
    def FrontMaterial(self) -> OpenGl_Material: 
        """
        Return front material.
        """
    def HasAlphaCutoff(self) -> bool: 
        """
        Return TRUE if alpha test should be enabled.
        """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def Set(self,theFrontMat : OpenGl_Material,theBackMat : OpenGl_Material,theAlphaCutoff : float,theToDistinguish : bool,theToMapTexture : bool) -> None: 
        """
        Sets new material aspect.
        """
    def ToDistinguish(self) -> bool: 
        """
        Distinguish front/back flag.
        """
    def ToMapTexture(self) -> bool: 
        """
        Flag for mapping a texture.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_Matrix():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class OpenGl_ModelWorldState(OpenGl_StateInterface):
    """
    Defines state of OCCT model-world transformation.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def ModelWorldMatrix(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns current model-world matrix.
        """
    def ModelWorldMatrixInverse(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns inverse of current model-world matrix.
        """
    def Set(self,theModelWorldMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Sets new model-world matrix.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_NamedResource(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Named resource object.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
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
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Release GPU resources. Notice that implementation should be SAFE for several consecutive calls (thus should invalidate internal structures / ids to avoid multiple-free errors).
        """
    def ResourceId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return resource name.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theId : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class OpenGl_OitState(OpenGl_StateInterface):
    """
    Defines generic state of order-independent transparency rendering properties.
    """
    def DepthFactor(self) -> float: 
        """
        Returns factor defining influence of depth component of a fragment to its final coverage coefficient.
        """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def Set(self,theToEnableWrite : bool,theDepthFactor : float) -> None: 
        """
        Sets the uniform values.
        """
    def ToEnableWrite(self) -> bool: 
        """
        Returns flag indicating whether writing of output for OIT processing should be enabled/disabled.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_PBREnvironment(OpenGl_NamedResource, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    This class contains specular and diffuse maps required for Image Base Lighting (IBL) in PBR shading model with it's generation methods.
    """
    def Bake(self,theCtx : OpenGl_Context,theEnvMap : OpenGl_Texture,theZIsInverted : bool=False,theIsTopDown : bool=True,theDiffMapNbSamples : int=1024,theSpecMapNbSamples : int=256,theProbability : float=0.9900000095367432) -> None: 
        """
        Generates specular and diffuse (irradiance) IBL maps.
        """
    def Bind(self,theCtx : OpenGl_Context) -> None: 
        """
        Binds diffuse and specular IBL maps to the corresponding texture units.
        """
    def Clear(self,theCtx : OpenGl_Context,theColor : OCP.Graphic3d.Graphic3d_Vec3=OCP.Graphic3d.Graphic3d_Vec3) -> None: 
        """
        Fills all mipmaps of specular IBL map and diffuse IBL map with one color. So that environment illumination will be constant.
        """
    @staticmethod
    def Create_s(theCtx : OpenGl_Context,thePow2Size : int=9,theSpecMapLevelsNum : int=6,theId : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> OpenGl_PBREnvironment: 
        """
        Creates and initializes new PBR environment. It is the only way to create OpenGl_PBREnvironment.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsComplete(self) -> bool: 
        """
        Checks completeness of PBR environment. Creation method returns only completed objects or null handles otherwise.
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
    def IsNeededToBeBound(self) -> bool: 
        """
        Indicates whether IBL map's textures have to be bound or it is not obligate.
        """
    def Pow2Size(self) -> int: 
        """
        Returns size of IBL maps sides as power of 2. So that the real size can be calculated as 2^Pow2Size()
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Releases all OpenGL resources. It must be called before destruction.
        """
    def ResourceId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return resource name.
        """
    def SizesAreDifferent(self,thePow2Size : int,theSpecMapLevelsNumber : int) -> bool: 
        """
        Checks whether the given sizes affects to the current ones. It can be imagined as creation of new PBR environment. If creation method with this values returns the PBR environment having real sizes which are equals to current ones then this method will return false. It is handful when sizes are required to be changed. If this method returns false there is no reason to recreate PBR environment in order to change sizes.
        """
    def SpecMapLevelsNumber(self) -> int: 
        """
        Returns number of mipmap levels used in specular IBL map. It can be different from value passed to creation method.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unbind(self,theCtx : OpenGl_Context) -> None: 
        """
        Unbinds diffuse and specular IBL maps.
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
class OpenGl_Texture(OpenGl_NamedResource, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Texture resource.Texture resource.
    """
    @overload
    def Bind(self,theCtx : OpenGl_Context) -> None: 
        """
        Bind this Texture to the unit specified in sampler parameters. Also binds Sampler Object if it is allocated.

        Bind this Texture to specified unit. Also binds Sampler Object if it is allocated.
        """
    @overload
    def Bind(self,theCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: ...
    def Create(self,theCtx : OpenGl_Context) -> bool: 
        """
        Creates Texture id if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    @staticmethod
    @overload
    def GetDataFormat_s(theCtx : OpenGl_Context,theFormat : OCP.Image.Image_Format,theTextFormat : int,thePixelFormat : int,theDataType : int) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GetDataFormat_s(theCtx : OpenGl_Context,theData : OCP.Image.Image_PixMap,theTextFormat : int,thePixelFormat : int,theDataType : int) -> bool: ...
    def GetFormat(self) -> int: 
        """
        Returns texture format (not sized)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTarget(self) -> int: 
        """
        Returns target to which the texture is bound (GL_TEXTURE_1D, GL_TEXTURE_2D)
        """
    def HasMipmaps(self) -> bool: 
        """
        Returns true if texture was generated within mipmaps
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theCtx : OpenGl_Context,theTextFormat : int,thePixelFormat : int,theDataType : int,theSizeX : int,theSizeY : int,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theImage : OCP.Image.Image_PixMap=None) -> bool: 
        """
        Notice that texture will be unbound after this call.

        Initialize the texture with specified format, size and texture type. If theImage is empty the texture data will contain trash. Notice that texture will be unbound after this call.

        Initialize the texture with Graphic3d_TextureMap. It is an universal way to initialize. Suitable initialization method will be chosen.

        None

        None
        """
    @overload
    def Init(self,theCtx : OpenGl_Context,theTextureMap : OCP.Graphic3d.Graphic3d_TextureMap) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_PixMap,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theFormat : OpenGl_TextureFormat,theSizeXY : OCP.Graphic3d.Graphic3d_Vec2i,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theImage : OCP.Image.Image_PixMap=None) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_PixMap,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theIsColorMap : bool) -> bool: ...
    def Init2DMultisample(self,theCtx : OpenGl_Context,theNbSamples : int,theTextFormat : int,theSizeX : int,theSizeY : int) -> bool: 
        """
        Initialize the 2D multisampling texture using glTexImage2DMultisample().
        """
    @overload
    def Init3D(self,theCtx : OpenGl_Context,theFormat : OpenGl_TextureFormat,theSizeXYZ : OCP.Graphic3d.Graphic3d_Vec3i,thePixels : capsule) -> bool: 
        """
        Initializes 3D texture rectangle with specified format and size.

        None
        """
    @overload
    def Init3D(self,theCtx : OpenGl_Context,theTextFormat : int,thePixelFormat : int,theDataType : int,theSizeX : int,theSizeY : int,theSizeZ : int,thePixels : capsule) -> bool: ...
    def InitCompressed(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_CompressedPixMap,theIsColorMap : bool) -> bool: 
        """
        Initialize the texture with Image_CompressedPixMap.
        """
    def InitCubeMap(self,theCtx : OpenGl_Context,theCubeMap : OCP.Graphic3d.Graphic3d_CubeMap,theSize : int,theFormat : OCP.Image.Image_Format,theToGenMipmap : bool,theIsColorMap : bool) -> bool: 
        """
        Initializes 6 sides of cubemap. If theCubeMap is not NULL then size and format will be taken from it and corresponding arguments will be ignored. Otherwise this parametres will be taken from arguments.
        """
    def InitRectangle(self,theCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theFormat : OpenGl_TextureFormat) -> bool: 
        """
        Allocates texture rectangle with specified format and size.
        """
    def InitSamplerObject(self,theCtx : OpenGl_Context) -> bool: 
        """
        Initialize the Sampler Object (as OpenGL object).
        """
    def IsAlpha(self) -> bool: 
        """
        Return true for GL_RED and GL_ALPHA formats.
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
    def IsPointSprite(self) -> bool: 
        """
        Returns TRUE for point sprite texture.
        """
    def IsTopDown(self) -> bool: 
        """
        Return if 2D surface is defined top-down (TRUE) or bottom-up (FALSE). Normally set from Image_PixMap::IsTopDown() within texture initialization.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def MaxMipmapLevel(self) -> int: 
        """
        Return upper mipmap level index (0 means no mipmaps).
        """
    @staticmethod
    def PixelSizeOfPixelFormat_s(theInternalFormat : int) -> int: 
        """
        Return pixel size of pixel format in bytes. Note that this method considers that OpenGL natively supports this pixel format, which might be not the case - in the latter case, actual pixel size might differ!
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def ResourceId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return resource name.
        """
    def Revision(self) -> int: 
        """
        Revision of associated data source.
        """
    def Sampler(self) -> OpenGl_Sampler: 
        """
        Return texture sampler.
        """
    def SetAlpha(self,theValue : bool) -> None: 
        """
        Setup to interpret the format as Alpha by Shader Manager (should be GL_ALPHA within compatible context or GL_RED otherwise).
        """
    def SetRevision(self,theRevision : int) -> None: 
        """
        Set revision of associated data source.
        """
    def SetSampler(self,theSampler : OpenGl_Sampler) -> None: 
        """
        Set texture sampler.
        """
    def SetTopDown(self,theIsTopDown : bool) -> None: 
        """
        Set if 2D surface is defined top-down (TRUE) or bottom-up (FALSE).
        """
    def SizeX(self) -> int: 
        """
        Returns texture width (0 LOD)
        """
    def SizeY(self) -> int: 
        """
        Returns texture height (0 LOD)
        """
    def SizedFormat(self) -> int: 
        """
        Returns texture format (sized)
        """
    def TextureId(self) -> int: 
        """
        Returns texture ID
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: 
        """
        Unbind texture from the unit specified in sampler parameters. Also unbinds Sampler Object if it is allocated.

        Unbind texture from specified unit. Also unbinds Sampler Object if it is allocated.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context) -> None: ...
    def __init__(self,theResourceId : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theParams : OCP.Graphic3d.Graphic3d_TextureParams=None) -> None: ...
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
class OpenGl_BackgroundArray(OpenGl_PrimitiveArray, OpenGl_Element):
    """
    Tool class for generating reusable data for gradient or texture background rendering.
    """
    def Attributes(self) -> OCP.Graphic3d.Graphic3d_Buffer: 
        """
        Returns attributes array
        """
    def AttributesVbo(self) -> OpenGl_VertexBuffer: 
        """
        Returns attributes VBO.
        """
    def Bounds(self) -> OCP.Graphic3d.Graphic3d_BoundBuffer: 
        """
        Returns bounds array
        """
    def DrawMode(self) -> int: 
        """
        Returns primitive type (GL_LINES, GL_TRIANGLES and others)
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetUID(self) -> int: 
        """
        Returns unique ID of primitive array.
        """
    def GradientColor(self,theIndex : int) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Returns color of gradient background for the given index.
        """
    def GradientFillMethod(self) -> OCP.Aspect.Aspect_GradientFillMethod: 
        """
        Gets background gradient fill method
        """
    def IndexVbo(self) -> OpenGl_VertexBuffer: 
        """
        Returns index VBO.
        """
    def Indices(self) -> OCP.Graphic3d.Graphic3d_IndexBuffer: 
        """
        Returns indices array
        """
    def InitBuffers(self,theContext : OpenGl_Context,theType : OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray,theIndices : OCP.Graphic3d.Graphic3d_IndexBuffer,theAttribs : OCP.Graphic3d.Graphic3d_Buffer,theBounds : OCP.Graphic3d.Graphic3d_BoundBuffer) -> None: 
        """
        Initialize indices, attributes and bounds with new data.
        """
    def Invalidate(self) -> None: 
        """
        Invalidate VBO content without destruction.
        """
    def IsDefined(self) -> bool: 
        """
        Check if background parameters are set properly
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation.
        """
    def IsInitialized(self) -> bool: 
        """
        Return true if VBOs initialization has been performed. VBO initialization is performed during first Render() call. Notice that this flag does not indicate VBOs validity.
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        Release OpenGL resources (VBOs)
        """
    def Render(self,theWorkspace : OpenGl_Workspace,theProjection : OCP.Graphic3d.Graphic3d_Camera.Projection_e) -> None: 
        """
        Render primitives to the window
        """
    def SetGradientFillMethod(self,theType : OCP.Aspect.Aspect_GradientFillMethod) -> None: 
        """
        Sets type of gradient fill method
        """
    def SetGradientParameters(self,theColor1 : OCP.Quantity.Quantity_Color,theColor2 : OCP.Quantity.Quantity_Color,theType : OCP.Aspect.Aspect_GradientFillMethod) -> None: 
        """
        Sets background gradient parameters
        """
    def SetTextureFillMethod(self,theFillMethod : OCP.Aspect.Aspect_FillMethod) -> None: 
        """
        Sets texture fill method
        """
    def SetTextureParameters(self,theFillMethod : OCP.Aspect.Aspect_FillMethod) -> None: 
        """
        Sets background texture parameters
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def TextureFillMethod(self) -> OCP.Aspect.Aspect_FillMethod: 
        """
        Gets background texture fill method
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    def __init__(self,theType : OCP.Graphic3d.Graphic3d_TypeOfBackground) -> None: ...
    DRAW_MODE_NONE = -1
    pass
class OpenGl_ProgramOptions():
    """
    Standard GLSL program combination bits.

    Members:

      OpenGl_PO_VertColor

      OpenGl_PO_TextureRGB

      OpenGl_PO_TextureEnv

      OpenGl_PO_TextureNormal

      OpenGl_PO_PointSimple

      OpenGl_PO_PointSprite

      OpenGl_PO_PointSpriteA

      OpenGl_PO_StippleLine

      OpenGl_PO_ClipPlanes1

      OpenGl_PO_ClipPlanes2

      OpenGl_PO_ClipPlanesN

      OpenGl_PO_ClipChains

      OpenGl_PO_MeshEdges

      OpenGl_PO_AlphaTest

      OpenGl_PO_WriteOit

      OpenGl_PO_NB

      OpenGl_PO_IsPoint

      OpenGl_PO_HasTextures

      OpenGl_PO_NeedsGeomShader
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
    OpenGl_PO_AlphaTest: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_AlphaTest: 1024>
    OpenGl_PO_ClipChains: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipChains: 256>
    OpenGl_PO_ClipPlanes1: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes1: 64>
    OpenGl_PO_ClipPlanes2: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes2: 128>
    OpenGl_PO_ClipPlanesN: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanesN: 192>
    OpenGl_PO_HasTextures: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>
    OpenGl_PO_IsPoint: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>
    OpenGl_PO_MeshEdges: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>
    OpenGl_PO_NB: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_NB: 4096>
    OpenGl_PO_NeedsGeomShader: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>
    OpenGl_PO_PointSimple: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSimple: 8>
    OpenGl_PO_PointSprite: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSprite: 16>
    OpenGl_PO_PointSpriteA: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>
    OpenGl_PO_StippleLine: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_StippleLine: 32>
    OpenGl_PO_TextureEnv: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureEnv: 4>
    OpenGl_PO_TextureNormal: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>
    OpenGl_PO_TextureRGB: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureRGB: 2>
    OpenGl_PO_VertColor: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_VertColor: 1>
    OpenGl_PO_WriteOit: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_WriteOit: 2048>
    __entries: dict # value = {'OpenGl_PO_VertColor': (<OpenGl_ProgramOptions.OpenGl_PO_VertColor: 1>, None), 'OpenGl_PO_TextureRGB': (<OpenGl_ProgramOptions.OpenGl_PO_TextureRGB: 2>, None), 'OpenGl_PO_TextureEnv': (<OpenGl_ProgramOptions.OpenGl_PO_TextureEnv: 4>, None), 'OpenGl_PO_TextureNormal': (<OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>, None), 'OpenGl_PO_PointSimple': (<OpenGl_ProgramOptions.OpenGl_PO_PointSimple: 8>, None), 'OpenGl_PO_PointSprite': (<OpenGl_ProgramOptions.OpenGl_PO_PointSprite: 16>, None), 'OpenGl_PO_PointSpriteA': (<OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>, None), 'OpenGl_PO_StippleLine': (<OpenGl_ProgramOptions.OpenGl_PO_StippleLine: 32>, None), 'OpenGl_PO_ClipPlanes1': (<OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes1: 64>, None), 'OpenGl_PO_ClipPlanes2': (<OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes2: 128>, None), 'OpenGl_PO_ClipPlanesN': (<OpenGl_ProgramOptions.OpenGl_PO_ClipPlanesN: 192>, None), 'OpenGl_PO_ClipChains': (<OpenGl_ProgramOptions.OpenGl_PO_ClipChains: 256>, None), 'OpenGl_PO_MeshEdges': (<OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>, None), 'OpenGl_PO_AlphaTest': (<OpenGl_ProgramOptions.OpenGl_PO_AlphaTest: 1024>, None), 'OpenGl_PO_WriteOit': (<OpenGl_ProgramOptions.OpenGl_PO_WriteOit: 2048>, None), 'OpenGl_PO_NB': (<OpenGl_ProgramOptions.OpenGl_PO_NB: 4096>, None), 'OpenGl_PO_IsPoint': (<OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>, None), 'OpenGl_PO_HasTextures': (<OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>, None), 'OpenGl_PO_NeedsGeomShader': (<OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>, None)}
    __members__: dict # value = {'OpenGl_PO_VertColor': <OpenGl_ProgramOptions.OpenGl_PO_VertColor: 1>, 'OpenGl_PO_TextureRGB': <OpenGl_ProgramOptions.OpenGl_PO_TextureRGB: 2>, 'OpenGl_PO_TextureEnv': <OpenGl_ProgramOptions.OpenGl_PO_TextureEnv: 4>, 'OpenGl_PO_TextureNormal': <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>, 'OpenGl_PO_PointSimple': <OpenGl_ProgramOptions.OpenGl_PO_PointSimple: 8>, 'OpenGl_PO_PointSprite': <OpenGl_ProgramOptions.OpenGl_PO_PointSprite: 16>, 'OpenGl_PO_PointSpriteA': <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>, 'OpenGl_PO_StippleLine': <OpenGl_ProgramOptions.OpenGl_PO_StippleLine: 32>, 'OpenGl_PO_ClipPlanes1': <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes1: 64>, 'OpenGl_PO_ClipPlanes2': <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes2: 128>, 'OpenGl_PO_ClipPlanesN': <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanesN: 192>, 'OpenGl_PO_ClipChains': <OpenGl_ProgramOptions.OpenGl_PO_ClipChains: 256>, 'OpenGl_PO_MeshEdges': <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>, 'OpenGl_PO_AlphaTest': <OpenGl_ProgramOptions.OpenGl_PO_AlphaTest: 1024>, 'OpenGl_PO_WriteOit': <OpenGl_ProgramOptions.OpenGl_PO_WriteOit: 2048>, 'OpenGl_PO_NB': <OpenGl_ProgramOptions.OpenGl_PO_NB: 4096>, 'OpenGl_PO_IsPoint': <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>, 'OpenGl_PO_HasTextures': <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>, 'OpenGl_PO_NeedsGeomShader': <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>}
    pass
class OpenGl_ProjectionState(OpenGl_StateInterface):
    """
    Defines state of OCCT projection transformation.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def ProjectionMatrix(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns current projection matrix.
        """
    def ProjectionMatrixInverse(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns inverse of current projection matrix.
        """
    def Set(self,theProjectionMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Sets new projection matrix.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_RaytraceLight():
    """
    Stores properties of OpenGL light source.
    """
    def Packed(self) -> float: 
        """
        Returns packed (serialized) representation of light source.
        """
    @overload
    def __init__(self,theEmission : OCP.Graphic3d.Graphic3d_Vec4,thePosition : OCP.Graphic3d.Graphic3d_Vec4) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OpenGl_RaytraceMaterial():
    """
    Stores properties of surface material.
    """
    def Packed(self) -> float: 
        """
        Returns packed (serialized) representation of material.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_RenderFilter():
    """
    Filter for rendering elements.

    Members:

      OpenGl_RenderFilter_Empty

      OpenGl_RenderFilter_OpaqueOnly

      OpenGl_RenderFilter_TransparentOnly

      OpenGl_RenderFilter_NonRaytraceableOnly

      OpenGl_RenderFilter_FillModeOnly
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
    OpenGl_RenderFilter_Empty: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_Empty: 0>
    OpenGl_RenderFilter_FillModeOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_FillModeOnly: 8>
    OpenGl_RenderFilter_NonRaytraceableOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_NonRaytraceableOnly: 4>
    OpenGl_RenderFilter_OpaqueOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_OpaqueOnly: 1>
    OpenGl_RenderFilter_TransparentOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_TransparentOnly: 2>
    __entries: dict # value = {'OpenGl_RenderFilter_Empty': (<OpenGl_RenderFilter.OpenGl_RenderFilter_Empty: 0>, None), 'OpenGl_RenderFilter_OpaqueOnly': (<OpenGl_RenderFilter.OpenGl_RenderFilter_OpaqueOnly: 1>, None), 'OpenGl_RenderFilter_TransparentOnly': (<OpenGl_RenderFilter.OpenGl_RenderFilter_TransparentOnly: 2>, None), 'OpenGl_RenderFilter_NonRaytraceableOnly': (<OpenGl_RenderFilter.OpenGl_RenderFilter_NonRaytraceableOnly: 4>, None), 'OpenGl_RenderFilter_FillModeOnly': (<OpenGl_RenderFilter.OpenGl_RenderFilter_FillModeOnly: 8>, None)}
    __members__: dict # value = {'OpenGl_RenderFilter_Empty': <OpenGl_RenderFilter.OpenGl_RenderFilter_Empty: 0>, 'OpenGl_RenderFilter_OpaqueOnly': <OpenGl_RenderFilter.OpenGl_RenderFilter_OpaqueOnly: 1>, 'OpenGl_RenderFilter_TransparentOnly': <OpenGl_RenderFilter.OpenGl_RenderFilter_TransparentOnly: 2>, 'OpenGl_RenderFilter_NonRaytraceableOnly': <OpenGl_RenderFilter.OpenGl_RenderFilter_NonRaytraceableOnly: 4>, 'OpenGl_RenderFilter_FillModeOnly': <OpenGl_RenderFilter.OpenGl_RenderFilter_FillModeOnly: 8>}
    pass
class OpenGl_CappingPlaneResource(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Container of graphical resources for rendering capping plane associated to graphical clipping plane. This resource holds data necessary for OpenGl_CappingAlgo. This object is implemented as OpenGl resource for the following reasons: - one instance should be shared between contexts. - instance associated to Graphic3d_ClipPlane data by id. - should created and released within context (owns OpenGl elements and resources).Container of graphical resources for rendering capping plane associated to graphical clipping plane. This resource holds data necessary for OpenGl_CappingAlgo. This object is implemented as OpenGl resource for the following reasons: - one instance should be shared between contexts. - instance associated to Graphic3d_ClipPlane data by id. - should created and released within context (owns OpenGl elements and resources).Container of graphical resources for rendering capping plane associated to graphical clipping plane. This resource holds data necessary for OpenGl_CappingAlgo. This object is implemented as OpenGl resource for the following reasons: - one instance should be shared between contexts. - instance associated to Graphic3d_ClipPlane data by id. - should created and released within context (owns OpenGl elements and resources).
    """
    def AspectFace(self) -> OpenGl_Aspects: 
        """
        Returns aspect face for rendering capping surface.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage - not implemented.
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
    def Orientation(self) -> OpenGl_Matrix: 
        """
        Returns evaluated orientation matrix to transform infinite plane.
        """
    def Plane(self) -> OCP.Graphic3d.Graphic3d_ClipPlane: 
        """
        Return parent clipping plane structure.
        """
    def Primitives(self) -> OpenGl_PrimitiveArray: 
        """
        Returns primitive array of vertices to render infinite plane.
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        Release associated OpenGl resources.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,theContext : OpenGl_Context,theObjAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Update resource data in the passed context.
        """
    def __init__(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> None: ...
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
class OpenGl_Sampler(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Class implements OpenGL sampler object resource that stores the sampling parameters for a texture access.Class implements OpenGL sampler object resource that stores the sampling parameters for a texture access.
    """
    @overload
    def Bind(self,theCtx : OpenGl_Context) -> None: 
        """
        Binds sampler object to texture unit specified in parameters.

        Binds sampler object to the given texture unit.
        """
    @overload
    def Bind(self,theCtx : OpenGl_Context,theUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: ...
    def Create(self,theContext : OpenGl_Context) -> bool: 
        """
        Creates an uninitialized sampler object.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage - not implemented.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theContext : OpenGl_Context,theTexture : OpenGl_Texture) -> bool: 
        """
        Creates and initializes sampler object. Existing object will be reused if possible, however if existing Sampler Object has Immutable flag and texture parameters should be re-initialized, then Sampler Object will be recreated.
        """
    def IsImmutable(self) -> bool: 
        """
        Return immutable flag preventing further modifications of sampler parameters, FALSE by default. Immutable flag might be set when Sampler Object is used within Bindless Texture.
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized.
        """
    def Parameters(self) -> OCP.Graphic3d.Graphic3d_TextureParams: 
        """
        Returns texture parameters.
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        Destroys object - will release GPU memory if any.
        """
    def SamplerID(self) -> int: 
        """
        Returns OpenGL sampler ID.
        """
    def SetImmutable(self) -> None: 
        """
        Setup immutable flag. It is not possible unsetting this flag without Sampler destruction.
        """
    def SetParameter(self,theCtx : OpenGl_Context,theTarget : int,theParam : int,theValue : int) -> None: 
        """
        Sets specific sampler parameter.
        """
    def SetParameters(self,theParams : OCP.Graphic3d.Graphic3d_TextureParams) -> None: 
        """
        Sets texture parameters.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToUpdateParameters(self) -> bool: 
        """
        Returns texture parameters initialization state.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context) -> None: 
        """
        Unbinds sampler object from texture unit specified in parameters.

        Unbinds sampler object from the given texture unit.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context,theUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: ...
    def __init__(self,theParams : OCP.Graphic3d.Graphic3d_TextureParams) -> None: ...
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
class OpenGl_SetOfPrograms(OCP.Standard.Standard_Transient):
    """
    Alias to programs array of predefined length
    """
    def ChangeValue(self,theProgramBits : int) -> OpenGl_ShaderProgram: 
        """
        Access program by index
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
        None
        """
    @staticmethod
    def get_type_name_s() -> str: 
        """
        None
        """
    pass
class OpenGl_SetOfShaderPrograms(OCP.Standard.Standard_Transient):
    """
    Alias to 2D programs array of predefined length
    """
    def ChangeValue(self,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theProgramBits : int) -> OpenGl_ShaderProgram: 
        """
        Access program by index
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
    @overload
    def __init__(self,thePrograms : OpenGl_SetOfPrograms) -> None: ...
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
class OpenGl_SetterInterface():
    """
    Interface for generic setter of user-defined uniform variables.
    """
    def Set(self,theCtx : OpenGl_Context,theVariable : OCP.Graphic3d.Graphic3d_ShaderVariable,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Sets user-defined uniform variable to specified program.
        """
    pass
class OpenGl_ShaderList(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : OpenGl_ShaderList) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OpenGl_ShaderObject) -> None: ...
    def Assign(self,theOther : OpenGl_ShaderList) -> OpenGl_ShaderList: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OpenGl_ShaderObject: 
        """
        First item access
        """
    def ChangeLast(self) -> OpenGl_ShaderObject: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OpenGl_ShaderObject: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OpenGl_ShaderObject: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OpenGl_ShaderObject) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : OpenGl_ShaderList) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : OpenGl_ShaderList) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OpenGl_ShaderObject) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OpenGl_ShaderObject: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theSeq : OpenGl_ShaderList) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : OpenGl_ShaderObject) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OpenGl_ShaderObject) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : OpenGl_ShaderList) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OpenGl_ShaderObject: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : OpenGl_ShaderList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class OpenGl_ShaderManager(OCP.Standard.Standard_Transient):
    """
    This class is responsible for managing shader programs.This class is responsible for managing shader programs.
    """
    def BindBoundBoxProgram(self) -> bool: 
        """
        Bind program for rendering bounding box.
        """
    @overload
    def BindFaceProgram(self,theTextures : OpenGl_TextureSet,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theAlphaMode : OCP.Graphic3d.Graphic3d_AlphaMode,theInteriorStyle : OCP.Aspect.Aspect_InteriorStyle,theHasVertColor : bool,theEnableEnvMap : bool,theEnableMeshEdges : bool,theCustomProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Bind program for filled primitives rendering

        Bind program for filled primitives rendering
        """
    @overload
    def BindFaceProgram(self,theTextures : OpenGl_TextureSet,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theAlphaMode : OCP.Graphic3d.Graphic3d_AlphaMode,theHasVertColor : bool,theEnableEnvMap : bool,theCustomProgram : OpenGl_ShaderProgram) -> bool: ...
    def BindFboBlitProgram(self,theNbSamples : int,theIsFallback_sRGB : bool) -> bool: 
        """
        Bind program for FBO blit operation.
        """
    def BindFontProgram(self,theCustomProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Bind program for rendering alpha-textured font.
        """
    def BindLineProgram(self,theTextures : OpenGl_TextureSet,theLineType : OCP.Aspect.Aspect_TypeOfLine,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theAlphaMode : OCP.Graphic3d.Graphic3d_AlphaMode,theHasVertColor : bool,theCustomProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Bind program for line rendering
        """
    def BindMarkerProgram(self,theTextures : OpenGl_TextureSet,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theAlphaMode : OCP.Graphic3d.Graphic3d_AlphaMode,theHasVertColor : bool,theCustomProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Bind program for point rendering
        """
    def BindOitCompositingProgram(self,theIsMSAAEnabled : bool) -> bool: 
        """
        Bind program for blended order-independent transparency buffers compositing.
        """
    def BindOutlineProgram(self) -> bool: 
        """
        Bind program for outline rendering
        """
    def BindPBREnvBakingProgram(self) -> bool: 
        """
        Bind program for IBL maps generation in PBR pipeline.
        """
    def BindStereoProgram(self,theStereoMode : OCP.Graphic3d.Graphic3d_StereoMode) -> bool: 
        """
        Bind program for rendering stereoscopic image.
        """
    def BoundBoxVertBuffer(self) -> OpenGl_VertexBuffer: 
        """
        Returns bounding box vertex buffer.
        """
    def ChooseFaceShadingModel(self,theCustomModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theHasNodalNormals : bool) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Choose Shading Model for filled primitives. Fallbacks to FACET model if there are no normal attributes. Fallbacks to corresponding non-PBR models if PBR is unavailable.
        """
    def ChooseLineShadingModel(self,theCustomModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theHasNodalNormals : bool) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Choose Shading Model for line primitives. Fallbacks to UNLIT model if there are no normal attributes. Fallbacks to corresponding non-PBR models if PBR is unavailable.
        """
    def ChooseMarkerShadingModel(self,theCustomModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theHasNodalNormals : bool) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Choose Shading Model for Marker primitives.
        """
    def Create(self,theProxy : OCP.Graphic3d.Graphic3d_ShaderProgram,theShareKey : OCP.TCollection.TCollection_AsciiString,theProgram : OpenGl_ShaderProgram) -> bool: 
        """
        Creates new shader program or re-use shared instance.
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
    def GetBgCubeMapProgram(self) -> OCP.Graphic3d.Graphic3d_ShaderProgram: 
        """
        Generates shader program to render environment cubemap as background.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if no program objects are registered in the manager.
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
    def IsSameContext(self,theCtx : OpenGl_Context) -> bool: 
        """
        Returns true when provided context is the same as used one by shader manager.
        """
    def IsSameView(self,theView : OpenGl_View) -> bool: 
        """
        Returns true when provided view is the same as cached one.
        """
    def LightSourceState(self) -> OpenGl_LightSourceState: 
        """
        Returns current state of OCCT light sources.
        """
    def LocalClippingPlaneW(self,thePlane : OCP.Graphic3d.Graphic3d_ClipPlane) -> float: 
        """
        Return clipping plane W equation value moved considering local camera transformation.
        """
    def LocalOrigin(self) -> OCP.gp.gp_XYZ: 
        """
        Return local camera transformation.
        """
    def MaterialState(self) -> OpenGl_MaterialState: 
        """
        Returns current state of material.
        """
    def ModelWorldState(self) -> OpenGl_ModelWorldState: 
        """
        Returns current state of OCCT model-world transform.
        """
    def OitState(self) -> OpenGl_OitState: 
        """
        Returns state of OIT uniforms.
        """
    @staticmethod
    def PBRShadingModelFallback_s(theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel,theIsPbrAllowed : bool=False) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Resets PBR shading models to corresponding non-PBR ones if PBR is not allowed.
        """
    def ProjectionState(self) -> OpenGl_ProjectionState: 
        """
        Returns current state of OCCT projection transform.
        """
    def PushClippingState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT clipping planes to specified program (only on state change).
        """
    def PushInteriorState(self,theProgram : OpenGl_ShaderProgram,theAspect : OCP.Graphic3d.Graphic3d_Aspects) -> None: 
        """
        Setup interior style line edges variables.
        """
    def PushLightSourceState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT light sources to specified program (only on state change).
        """
    def PushMaterialState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of material to specified program (only on state change).
        """
    def PushModelWorldState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT model-world transform to specified program (only on state change).
        """
    def PushOitState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes state of OIT uniforms to the specified program.
        """
    def PushProjectionState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT projection transform to specified program (only on state change).
        """
    def PushState(self,theProgram : OpenGl_ShaderProgram,theShadingModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel=Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT) -> None: 
        """
        Pushes current state of OCCT graphics parameters to specified program.
        """
    def PushWorldViewState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT world-view transform to specified program (only on state change).
        """
    def RevertClippingState(self) -> None: 
        """
        Reverts state of OCCT clipping planes.
        """
    def SetContext(self,theCtx : OpenGl_Context) -> None: 
        """
        Overwrites context
        """
    def SetLastView(self,theLastView : OpenGl_View) -> None: 
        """
        Sets last view manger used with. Helps to handle matrix states in multi-view configurations.
        """
    def SetLocalOrigin(self,theOrigin : OCP.gp.gp_XYZ) -> None: 
        """
        Setup local camera transformation for compensating float precision issues.
        """
    def SetOitState(self,theToEnableOitWrite : bool,theDepthFactor : float) -> None: 
        """
        Set the state of OIT rendering pass (only on state change).
        """
    def SetShadingModel(self,theModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model.
        """
    def ShaderPrograms(self) -> OpenGl_ShaderProgramList: 
        """
        Returns list of registered shader programs.
        """
    def ShadingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Returns default Shading Model.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unregister(self,theShareKey : OCP.TCollection.TCollection_AsciiString,theProgram : OpenGl_ShaderProgram) -> Any: 
        """
        Unregisters specified shader program.
        """
    def UpdateClippingState(self) -> None: 
        """
        Updates state of OCCT clipping planes.
        """
    def UpdateLightSourceState(self) -> None: 
        """
        Invalidate state of OCCT light sources.
        """
    def UpdateLightSourceStateTo(self,theLights : OCP.Graphic3d.Graphic3d_LightSet,theSpecIBLMapLevels : int=0) -> None: 
        """
        Updates state of OCCT light sources.
        """
    def UpdateMaterialState(self) -> None: 
        """
        Updates state of material.
        """
    def UpdateMaterialStateTo(self,theFrontMat : OpenGl_Material,theBackMat : OpenGl_Material,theAlphaCutoff : float,theToDistinguish : bool,theToMapTexture : bool) -> None: 
        """
        Updates state of material.
        """
    def UpdateModelWorldStateTo(self,theModelWorldMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Updates state of OCCT model-world transform.
        """
    def UpdateProjectionStateTo(self,theProjectionMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Updates state of OCCT projection transform.
        """
    def UpdateSRgbState(self) -> None: 
        """
        Fetch sRGB state from caps and invalidates programs, if necessary.
        """
    def UpdateWorldViewStateTo(self,theWorldViewMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Updates state of OCCT world-view transform.
        """
    def WorldViewState(self) -> OpenGl_WorldViewState: 
        """
        Returns current state of OCCT world-view transform.
        """
    def __init__(self,theContext : OpenGl_Context) -> None: ...
    def clear(self) -> None: 
        """
        Release all resources.
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
    def pushClippingState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT clipping planes to specified program.
        """
    def pushLightSourceState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT light sources to specified program.
        """
    def pushMaterialState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of material to specified program.
        """
    def pushModelWorldState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT model-world transform to specified program.
        """
    def pushOitState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes state of OIT uniforms to the specified program.
        """
    def pushProjectionState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT projection transform to specified program.
        """
    def pushWorldViewState(self,theProgram : OpenGl_ShaderProgram) -> None: 
        """
        Pushes current state of OCCT world-view transform to specified program.
        """
    pass
class OpenGl_ShaderObject(OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Wrapper for OpenGL shader object.Wrapper for OpenGL shader object.
    """
    def Compile(self,theCtx : OpenGl_Context) -> bool: 
        """
        Compiles the shader object.
        """
    def Create(self,theCtx : OpenGl_Context) -> bool: 
        """
        Creates new empty shader object of specified type.
        """
    @staticmethod
    def CreateFromSource_s(theSource : OCP.TCollection.TCollection_AsciiString,theType : OCP.Graphic3d.Graphic3d_TypeOfShaderObject,theUniforms : Any,theStageInOuts : Any,theInName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theOutName : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theNbGeomInputVerts : int=0) -> OCP.Graphic3d.Graphic3d_ShaderObject: 
        """
        This is a preprocessor for Graphic3d_ShaderObject::CreateFromSource() function. Creates a new shader object from specified source according to list of uniforms and in/out variables.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DumpSourceCode(self,theCtx : OpenGl_Context,theId : OCP.TCollection.TCollection_AsciiString,theSource : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Print source code of this shader object to messenger.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage - not implemented.
        """
    def FetchInfoLog(self,theCtx : OpenGl_Context,theLog : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Fetches information log of the last compile operation.
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
    def LoadAndCompile(self,theCtx : OpenGl_Context,theId : OCP.TCollection.TCollection_AsciiString,theSource : OCP.TCollection.TCollection_AsciiString,theIsVerbose : bool=True,theToPrintSource : bool=True) -> bool: 
        """
        Wrapper for compiling shader object with verbose printing on error.
        """
    def LoadSource(self,theCtx : OpenGl_Context,theSource : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Loads shader source code.
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Destroys shader object.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> int: 
        """
        Returns type of shader object.
        """
    def __init__(self,theType : int) -> None: ...
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
    def updateDebugDump(self,theCtx : OpenGl_Context,theId : OCP.TCollection.TCollection_AsciiString,theFolder : OCP.TCollection.TCollection_AsciiString,theToBeautify : bool,theToReset : bool) -> bool: 
        """
        Update the shader object from external file in the following way: 1) If external file does not exist, then it will be created (current source code will be dumped, no recompilation) and FALSE will be returned. 2) If external file exists and it has the same timestamp as myDumpDate, nothing will be done and FALSE will be returned. 3) If external file exists and it has newer timestamp than myDumpDate, shader will be recompiled and TRUE will be returned.
        """
    pass
class OpenGl_ShaderProgram(OpenGl_NamedResource, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Wrapper for OpenGL program object.Wrapper for OpenGL program object.Wrapper for OpenGL program object.
    """
    def ApplyVariables(self,theCtx : OpenGl_Context) -> bool: 
        """
        Fetches uniform variables from proxy shader program.
        """
    def AttachShader(self,theCtx : OpenGl_Context,theShader : OpenGl_ShaderObject) -> bool: 
        """
        Attaches shader object to the program object.
        """
    def Create(self,theCtx : OpenGl_Context) -> bool: 
        """
        Creates new empty shader program of specified type.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetachShader(self,theCtx : OpenGl_Context,theShader : OpenGl_ShaderObject) -> bool: 
        """
        Detaches shader object to the program object.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage - cannot be easily estimated.
        """
    def FetchInfoLog(self,theCtx : OpenGl_Context,theLog : OCP.TCollection.TCollection_AsciiString) -> bool: 
        """
        Fetches information log of the last link operation.
        """
    @overload
    def GetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: 
        """
        Returns the integer vertex attribute.

        Returns the integer vertex attribute.

        Returns the float vertex attribute.

        Returns the float vertex attribute.
        """
    @overload
    def GetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    @overload
    def GetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def GetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    def GetAttributeLocation(self,theCtx : OpenGl_Context,theName : str) -> int: 
        """
        Returns index of the generic vertex attribute by variable name.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetStateLocation(self,theVariable : OpenGl_StateVariable) -> OpenGl_ShaderUniformLocation: 
        """
        Returns location of the OCCT state uniform variable.
        """
    @overload
    def GetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: 
        """
        Returns the value of the integer uniform variable.

        None

        Returns the value of the float uniform variable.

        Returns the value of the float uniform variable.
        """
    @overload
    def GetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    @overload
    def GetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def GetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    def GetUniformLocation(self,theCtx : OpenGl_Context,theName : str) -> OpenGl_ShaderUniformLocation: 
        """
        Returns location of the specific uniform variable.
        """
    def HasAlphaTest(self) -> bool: 
        """
        Return true if Fragment Shader should perform alpha test; FALSE by default.
        """
    def HasTessellationStage(self) -> bool: 
        """
        Return TRUE if program defines tessellation stage.
        """
    def HasWeightOitOutput(self) -> bool: 
        """
        Return true if Fragment Shader color should output the weighted OIT coverage; FALSE by default.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Initialize(self,theCtx : OpenGl_Context,theShaders : OCP.Graphic3d.Graphic3d_ShaderObjectList) -> bool: 
        """
        Initializes program object with the list of shader objects.
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def Link(self,theCtx : OpenGl_Context,theIsVerbose : bool=True) -> bool: 
        """
        Links the program object.
        """
    def NbClipPlanesMax(self) -> int: 
        """
        Return the length of array of clipping planes (THE_MAX_CLIP_PLANES), to be used for initialization occClipPlaneEquations (OpenGl_OCC_CLIP_PLANE_EQUATIONS) and occClipPlaneChains (OpenGl_OCC_CLIP_PLANE_CHAINS).
        """
    def NbFragmentOutputs(self) -> int: 
        """
        Return the length of array of Fragment Shader outputs (THE_NB_FRAG_OUTPUTS), to be used for initialization occFragColorArray/occFragColorN.
        """
    def NbLightsMax(self) -> int: 
        """
        Return the length of array of light sources (THE_MAX_LIGHTS), to be used for initialization occLightSources (OpenGl_OCC_LIGHT_SOURCE_PARAMS).
        """
    def ProgramId(self) -> int: 
        """
        Returns program ID
        """
    def Proxy(self) -> OCP.Graphic3d.Graphic3d_ShaderProgram: 
        """
        Returns proxy shader program.
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Destroys shader program.
        """
    def ResourceId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return resource name.
        """
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec2) -> bool: 
        """
        Wrapper for glVertexAttrib1f()

        Wrapper for glVertexAttrib1f()

        Wrapper for glVertexAttrib2fv()

        Wrapper for glVertexAttrib2fv()

        Wrapper for glVertexAttrib3fv()

        Wrapper for glVertexAttrib3fv()

        Wrapper for glVertexAttrib4fv()

        Wrapper for glVertexAttrib4fv()
        """
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec3) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : float) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : OCP.Graphic3d.Graphic3d_Vec3) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : float) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def SetAttribute(self,theCtx : OpenGl_Context,theIndex : int,theValue : OCP.Graphic3d.Graphic3d_Vec2) -> bool: ...
    def SetAttributeName(self,theCtx : OpenGl_Context,theIndex : int,theName : str) -> bool: 
        """
        Wrapper for glBindAttribLocation()
        """
    @overload
    def SetSampler(self,theCtx : OpenGl_Context,theName : str,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> bool: 
        """
        Specifies the value of the sampler uniform variable.

        Specifies the value of the sampler uniform variable.
        """
    @overload
    def SetSampler(self,theCtx : OpenGl_Context,theLocation : int,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec3) -> bool: 
        """
        Specifies the value of the integer uniform variable.

        Specifies the value of the integer uniform variable.

        Specifies the value of the integer uniform 2D vector.

        Specifies the value of the integer uniform 2D vector.

        Specifies the value of the integer uniform 3D vector.

        Specifies the value of the integer uniform 3D vector.

        Specifies the value of the integer uniform 4D vector.

        Specifies the value of the integer uniform 4D vector.

        Specifies the value of the unsigned integer uniform 2D vector (uvec2).

        Specifies the value of the unsigned integer uniform 2D vector (uvec2).

        Specifies the value of the uvec2 uniform array

        Specifies the value of the uvec2 uniform array

        Specifies the value of the float uniform variable.

        Specifies the value of the float uniform variable.

        Specifies the value of the float uniform 2D vector.

        Specifies the value of the float uniform 2D vector.

        Specifies the value of the float uniform 3D vector.

        Specifies the value of the float uniform 3D vector.

        Specifies the value of the float uniform 4D vector.

        Specifies the value of the float uniform 4D vector.

        Specifies the value of the float uniform 4x4 matrix.

        Specifies the value of the float uniform 4x4 matrix.

        Specifies the value of the float uniform 4x4 matrix.

        Specifies the value of the float uniform 4x4 matrix.

        Specifies the value of the float uniform array

        Specifies the value of the float2 uniform array

        Specifies the value of the float3 uniform array

        Specifies the value of the float4 uniform array

        Specifies the value of the integer uniform array

        Specifies the value of the int2 uniform array

        Specifies the value of the int3 uniform array

        Specifies the value of the int4 uniform array
        """
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : float) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : int) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theCount : int,theValue : Any) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec2) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : float) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : int) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Mat4,theTranspose : int=0) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec2) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec3i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OpenGl_Matrix,theTranspose : int=0) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Mat4,theTranspose : int=0) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec2i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec2) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : Any) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec4) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec3i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec2i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec3) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OpenGl_Matrix,theTranspose : int=0) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : float) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theName : str,theValue : OCP.Graphic3d.Graphic3d_Vec3i) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : int) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : OCP.Graphic3d.Graphic3d_Vec3) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theValue : Any) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theValue : Any) -> bool: ...
    @overload
    def SetUniform(self,theCtx : OpenGl_Context,theLocation : int,theCount : int,theData : OCP.Graphic3d.Graphic3d_Vec2i) -> bool: ...
    def TextureSetBits(self) -> int: 
        """
        Return texture units declared within the program,
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateDebugDump(self,theCtx : OpenGl_Context,theFolder : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theToBeautify : bool=False,theToReset : bool=False) -> bool: 
        """
        Update the shader program from external files (per shader stage) in the following way: 1) If external file does not exist, then it will be created (current source code will be dumped, no recompilation) and FALSE will be returned. 2) If external file exists and it has the same timestamp as myDumpDate, nothing will be done and FALSE will be returned. 3) If external file exists and it has newer timestamp than myDumpDate, shader will be recompiled and relinked and TRUE will be returned.
        """
    def __init__(self,theProxy : OCP.Graphic3d.Graphic3d_ShaderProgram=None,theId : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class OpenGl_ShaderProgramDumpLevel():
    """
    Definition of shader programs source code dump levels.

    Members:

      OpenGl_ShaderProgramDumpLevel_Off

      OpenGl_ShaderProgramDumpLevel_Short

      OpenGl_ShaderProgramDumpLevel_Full
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
    OpenGl_ShaderProgramDumpLevel_Full: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Full: 2>
    OpenGl_ShaderProgramDumpLevel_Off: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Off: 0>
    OpenGl_ShaderProgramDumpLevel_Short: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Short: 1>
    __entries: dict # value = {'OpenGl_ShaderProgramDumpLevel_Off': (<OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Off: 0>, None), 'OpenGl_ShaderProgramDumpLevel_Short': (<OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Short: 1>, None), 'OpenGl_ShaderProgramDumpLevel_Full': (<OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Full: 2>, None)}
    __members__: dict # value = {'OpenGl_ShaderProgramDumpLevel_Off': <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Off: 0>, 'OpenGl_ShaderProgramDumpLevel_Short': <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Short: 1>, 'OpenGl_ShaderProgramDumpLevel_Full': <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Full: 2>}
    pass
class OpenGl_ShaderProgramList(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : OpenGl_ShaderProgramList) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : OpenGl_ShaderProgram) -> None: ...
    def Assign(self,theOther : OpenGl_ShaderProgramList) -> OpenGl_ShaderProgramList: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> OpenGl_ShaderProgram: 
        """
        First item access
        """
    def ChangeLast(self) -> OpenGl_ShaderProgram: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> OpenGl_ShaderProgram: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> OpenGl_ShaderProgram: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : OpenGl_ShaderProgram) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : OpenGl_ShaderProgramList) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : OpenGl_ShaderProgramList) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : OpenGl_ShaderProgram) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> OpenGl_ShaderProgram: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : OpenGl_ShaderProgram) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : OpenGl_ShaderProgramList) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : OpenGl_ShaderProgram) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : OpenGl_ShaderProgramList) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> OpenGl_ShaderProgram: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : OpenGl_ShaderProgramList) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class OpenGl_ShaderUniformLocation():
    """
    Simple class represents GLSL program variable location.
    """
    def IsValid(self) -> bool: 
        """
        Note you may safely put invalid location in functions like glUniform* - the data passed in will be silently ignored.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLocation : int) -> None: ...
    pass
class OpenGl_StateCounter():
    """
    Tool class to implement consistent state counter for objects inside the same driver instance.
    """
    def Increment(self) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_LightSourceState(OpenGl_StateInterface):
    """
    Defines state of OCCT light sources.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def LightSources(self) -> OCP.Graphic3d.Graphic3d_LightSet: 
        """
        Returns current list of light sources.
        """
    def Set(self,theLightSources : OCP.Graphic3d.Graphic3d_LightSet) -> None: 
        """
        Sets new light sources.
        """
    def SetSpecIBLMapLevels(self,theSpecIBLMapLevels : int) -> None: 
        """
        Sets number of mipmap levels used in specular IBL map.
        """
    def SpecIBLMapLevels(self) -> int: 
        """
        Returns number of mipmap levels used in specular IBL map. 0 by default or in case of using non-PBR shading model.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_StateVariable():
    """
    The enumeration of OCCT-specific OpenGL/GLSL variables.

    Members:

      OpenGl_OCC_MODEL_WORLD_MATRIX

      OpenGl_OCC_WORLD_VIEW_MATRIX

      OpenGl_OCC_PROJECTION_MATRIX

      OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE

      OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE

      OpenGl_OCC_PROJECTION_MATRIX_INVERSE

      OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE

      OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE

      OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE

      OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE

      OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE

      OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE

      OpenGl_OCC_CLIP_PLANE_EQUATIONS

      OpenGl_OCC_CLIP_PLANE_CHAINS

      OpenGl_OCC_CLIP_PLANE_COUNT

      OpenGl_OCC_LIGHT_SOURCE_COUNT

      OpenGl_OCC_LIGHT_SOURCE_TYPES

      OpenGl_OCC_LIGHT_SOURCE_PARAMS

      OpenGl_OCC_LIGHT_AMBIENT

      OpenGl_OCCT_TEXTURE_ENABLE

      OpenGl_OCCT_DISTINGUISH_MODE

      OpenGl_OCCT_PBR_FRONT_MATERIAL

      OpenGl_OCCT_PBR_BACK_MATERIAL

      OpenGl_OCCT_COMMON_FRONT_MATERIAL

      OpenGl_OCCT_COMMON_BACK_MATERIAL

      OpenGl_OCCT_ALPHA_CUTOFF

      OpenGl_OCCT_COLOR

      OpenGl_OCCT_OIT_OUTPUT

      OpenGl_OCCT_OIT_DEPTH_FACTOR

      OpenGl_OCCT_TEXTURE_TRSF2D

      OpenGl_OCCT_POINT_SIZE

      OpenGl_OCCT_VIEWPORT

      OpenGl_OCCT_LINE_WIDTH

      OpenGl_OCCT_LINE_FEATHER

      OpenGl_OCCT_LINE_STIPPLE_PATTERN

      OpenGl_OCCT_LINE_STIPPLE_FACTOR

      OpenGl_OCCT_WIREFRAME_COLOR

      OpenGl_OCCT_QUAD_MODE_STATE

      OpenGl_OCCT_ORTHO_SCALE

      OpenGl_OCCT_SILHOUETTE_THICKNESS

      OpenGl_OCCT_NB_SPEC_IBL_LEVELS

      OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES
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
    OpenGl_OCCT_ALPHA_CUTOFF: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_ALPHA_CUTOFF: 25>
    OpenGl_OCCT_COLOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COLOR: 26>
    OpenGl_OCCT_COMMON_BACK_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COMMON_BACK_MATERIAL: 24>
    OpenGl_OCCT_COMMON_FRONT_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COMMON_FRONT_MATERIAL: 23>
    OpenGl_OCCT_DISTINGUISH_MODE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_DISTINGUISH_MODE: 20>
    OpenGl_OCCT_LINE_FEATHER: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_FEATHER: 33>
    OpenGl_OCCT_LINE_STIPPLE_FACTOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_FACTOR: 35>
    OpenGl_OCCT_LINE_STIPPLE_PATTERN: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_PATTERN: 34>
    OpenGl_OCCT_LINE_WIDTH: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_WIDTH: 32>
    OpenGl_OCCT_NB_SPEC_IBL_LEVELS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_NB_SPEC_IBL_LEVELS: 40>
    OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: 41>
    OpenGl_OCCT_OIT_DEPTH_FACTOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_OIT_DEPTH_FACTOR: 28>
    OpenGl_OCCT_OIT_OUTPUT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_OIT_OUTPUT: 27>
    OpenGl_OCCT_ORTHO_SCALE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_ORTHO_SCALE: 38>
    OpenGl_OCCT_PBR_BACK_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_PBR_BACK_MATERIAL: 22>
    OpenGl_OCCT_PBR_FRONT_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_PBR_FRONT_MATERIAL: 21>
    OpenGl_OCCT_POINT_SIZE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_POINT_SIZE: 30>
    OpenGl_OCCT_QUAD_MODE_STATE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_QUAD_MODE_STATE: 37>
    OpenGl_OCCT_SILHOUETTE_THICKNESS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_SILHOUETTE_THICKNESS: 39>
    OpenGl_OCCT_TEXTURE_ENABLE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_ENABLE: 19>
    OpenGl_OCCT_TEXTURE_TRSF2D: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_TRSF2D: 29>
    OpenGl_OCCT_VIEWPORT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_VIEWPORT: 31>
    OpenGl_OCCT_WIREFRAME_COLOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_WIREFRAME_COLOR: 36>
    OpenGl_OCC_CLIP_PLANE_CHAINS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_CHAINS: 13>
    OpenGl_OCC_CLIP_PLANE_COUNT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_COUNT: 14>
    OpenGl_OCC_CLIP_PLANE_EQUATIONS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_EQUATIONS: 12>
    OpenGl_OCC_LIGHT_AMBIENT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_AMBIENT: 18>
    OpenGl_OCC_LIGHT_SOURCE_COUNT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_COUNT: 15>
    OpenGl_OCC_LIGHT_SOURCE_PARAMS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_PARAMS: 17>
    OpenGl_OCC_LIGHT_SOURCE_TYPES: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_TYPES: 16>
    OpenGl_OCC_MODEL_WORLD_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX: 0>
    OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: 3>
    OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: 9>
    OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: 6>
    OpenGl_OCC_PROJECTION_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX: 2>
    OpenGl_OCC_PROJECTION_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE: 5>
    OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: 11>
    OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: 8>
    OpenGl_OCC_WORLD_VIEW_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX: 1>
    OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: 4>
    OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: 10>
    OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: 7>
    __entries: dict # value = {'OpenGl_OCC_MODEL_WORLD_MATRIX': (<OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX: 0>, None), 'OpenGl_OCC_WORLD_VIEW_MATRIX': (<OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX: 1>, None), 'OpenGl_OCC_PROJECTION_MATRIX': (<OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX: 2>, None), 'OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE': (<OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: 3>, None), 'OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE': (<OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: 4>, None), 'OpenGl_OCC_PROJECTION_MATRIX_INVERSE': (<OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE: 5>, None), 'OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: 6>, None), 'OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: 7>, None), 'OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: 8>, None), 'OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: 9>, None), 'OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: 10>, None), 'OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE': (<OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: 11>, None), 'OpenGl_OCC_CLIP_PLANE_EQUATIONS': (<OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_EQUATIONS: 12>, None), 'OpenGl_OCC_CLIP_PLANE_CHAINS': (<OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_CHAINS: 13>, None), 'OpenGl_OCC_CLIP_PLANE_COUNT': (<OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_COUNT: 14>, None), 'OpenGl_OCC_LIGHT_SOURCE_COUNT': (<OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_COUNT: 15>, None), 'OpenGl_OCC_LIGHT_SOURCE_TYPES': (<OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_TYPES: 16>, None), 'OpenGl_OCC_LIGHT_SOURCE_PARAMS': (<OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_PARAMS: 17>, None), 'OpenGl_OCC_LIGHT_AMBIENT': (<OpenGl_StateVariable.OpenGl_OCC_LIGHT_AMBIENT: 18>, None), 'OpenGl_OCCT_TEXTURE_ENABLE': (<OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_ENABLE: 19>, None), 'OpenGl_OCCT_DISTINGUISH_MODE': (<OpenGl_StateVariable.OpenGl_OCCT_DISTINGUISH_MODE: 20>, None), 'OpenGl_OCCT_PBR_FRONT_MATERIAL': (<OpenGl_StateVariable.OpenGl_OCCT_PBR_FRONT_MATERIAL: 21>, None), 'OpenGl_OCCT_PBR_BACK_MATERIAL': (<OpenGl_StateVariable.OpenGl_OCCT_PBR_BACK_MATERIAL: 22>, None), 'OpenGl_OCCT_COMMON_FRONT_MATERIAL': (<OpenGl_StateVariable.OpenGl_OCCT_COMMON_FRONT_MATERIAL: 23>, None), 'OpenGl_OCCT_COMMON_BACK_MATERIAL': (<OpenGl_StateVariable.OpenGl_OCCT_COMMON_BACK_MATERIAL: 24>, None), 'OpenGl_OCCT_ALPHA_CUTOFF': (<OpenGl_StateVariable.OpenGl_OCCT_ALPHA_CUTOFF: 25>, None), 'OpenGl_OCCT_COLOR': (<OpenGl_StateVariable.OpenGl_OCCT_COLOR: 26>, None), 'OpenGl_OCCT_OIT_OUTPUT': (<OpenGl_StateVariable.OpenGl_OCCT_OIT_OUTPUT: 27>, None), 'OpenGl_OCCT_OIT_DEPTH_FACTOR': (<OpenGl_StateVariable.OpenGl_OCCT_OIT_DEPTH_FACTOR: 28>, None), 'OpenGl_OCCT_TEXTURE_TRSF2D': (<OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_TRSF2D: 29>, None), 'OpenGl_OCCT_POINT_SIZE': (<OpenGl_StateVariable.OpenGl_OCCT_POINT_SIZE: 30>, None), 'OpenGl_OCCT_VIEWPORT': (<OpenGl_StateVariable.OpenGl_OCCT_VIEWPORT: 31>, None), 'OpenGl_OCCT_LINE_WIDTH': (<OpenGl_StateVariable.OpenGl_OCCT_LINE_WIDTH: 32>, None), 'OpenGl_OCCT_LINE_FEATHER': (<OpenGl_StateVariable.OpenGl_OCCT_LINE_FEATHER: 33>, None), 'OpenGl_OCCT_LINE_STIPPLE_PATTERN': (<OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_PATTERN: 34>, None), 'OpenGl_OCCT_LINE_STIPPLE_FACTOR': (<OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_FACTOR: 35>, None), 'OpenGl_OCCT_WIREFRAME_COLOR': (<OpenGl_StateVariable.OpenGl_OCCT_WIREFRAME_COLOR: 36>, None), 'OpenGl_OCCT_QUAD_MODE_STATE': (<OpenGl_StateVariable.OpenGl_OCCT_QUAD_MODE_STATE: 37>, None), 'OpenGl_OCCT_ORTHO_SCALE': (<OpenGl_StateVariable.OpenGl_OCCT_ORTHO_SCALE: 38>, None), 'OpenGl_OCCT_SILHOUETTE_THICKNESS': (<OpenGl_StateVariable.OpenGl_OCCT_SILHOUETTE_THICKNESS: 39>, None), 'OpenGl_OCCT_NB_SPEC_IBL_LEVELS': (<OpenGl_StateVariable.OpenGl_OCCT_NB_SPEC_IBL_LEVELS: 40>, None), 'OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES': (<OpenGl_StateVariable.OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: 41>, None)}
    __members__: dict # value = {'OpenGl_OCC_MODEL_WORLD_MATRIX': <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX: 0>, 'OpenGl_OCC_WORLD_VIEW_MATRIX': <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX: 1>, 'OpenGl_OCC_PROJECTION_MATRIX': <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX: 2>, 'OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE': <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: 3>, 'OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE': <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: 4>, 'OpenGl_OCC_PROJECTION_MATRIX_INVERSE': <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE: 5>, 'OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: 6>, 'OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: 7>, 'OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: 8>, 'OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: 9>, 'OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: 10>, 'OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE': <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: 11>, 'OpenGl_OCC_CLIP_PLANE_EQUATIONS': <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_EQUATIONS: 12>, 'OpenGl_OCC_CLIP_PLANE_CHAINS': <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_CHAINS: 13>, 'OpenGl_OCC_CLIP_PLANE_COUNT': <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_COUNT: 14>, 'OpenGl_OCC_LIGHT_SOURCE_COUNT': <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_COUNT: 15>, 'OpenGl_OCC_LIGHT_SOURCE_TYPES': <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_TYPES: 16>, 'OpenGl_OCC_LIGHT_SOURCE_PARAMS': <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_PARAMS: 17>, 'OpenGl_OCC_LIGHT_AMBIENT': <OpenGl_StateVariable.OpenGl_OCC_LIGHT_AMBIENT: 18>, 'OpenGl_OCCT_TEXTURE_ENABLE': <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_ENABLE: 19>, 'OpenGl_OCCT_DISTINGUISH_MODE': <OpenGl_StateVariable.OpenGl_OCCT_DISTINGUISH_MODE: 20>, 'OpenGl_OCCT_PBR_FRONT_MATERIAL': <OpenGl_StateVariable.OpenGl_OCCT_PBR_FRONT_MATERIAL: 21>, 'OpenGl_OCCT_PBR_BACK_MATERIAL': <OpenGl_StateVariable.OpenGl_OCCT_PBR_BACK_MATERIAL: 22>, 'OpenGl_OCCT_COMMON_FRONT_MATERIAL': <OpenGl_StateVariable.OpenGl_OCCT_COMMON_FRONT_MATERIAL: 23>, 'OpenGl_OCCT_COMMON_BACK_MATERIAL': <OpenGl_StateVariable.OpenGl_OCCT_COMMON_BACK_MATERIAL: 24>, 'OpenGl_OCCT_ALPHA_CUTOFF': <OpenGl_StateVariable.OpenGl_OCCT_ALPHA_CUTOFF: 25>, 'OpenGl_OCCT_COLOR': <OpenGl_StateVariable.OpenGl_OCCT_COLOR: 26>, 'OpenGl_OCCT_OIT_OUTPUT': <OpenGl_StateVariable.OpenGl_OCCT_OIT_OUTPUT: 27>, 'OpenGl_OCCT_OIT_DEPTH_FACTOR': <OpenGl_StateVariable.OpenGl_OCCT_OIT_DEPTH_FACTOR: 28>, 'OpenGl_OCCT_TEXTURE_TRSF2D': <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_TRSF2D: 29>, 'OpenGl_OCCT_POINT_SIZE': <OpenGl_StateVariable.OpenGl_OCCT_POINT_SIZE: 30>, 'OpenGl_OCCT_VIEWPORT': <OpenGl_StateVariable.OpenGl_OCCT_VIEWPORT: 31>, 'OpenGl_OCCT_LINE_WIDTH': <OpenGl_StateVariable.OpenGl_OCCT_LINE_WIDTH: 32>, 'OpenGl_OCCT_LINE_FEATHER': <OpenGl_StateVariable.OpenGl_OCCT_LINE_FEATHER: 33>, 'OpenGl_OCCT_LINE_STIPPLE_PATTERN': <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_PATTERN: 34>, 'OpenGl_OCCT_LINE_STIPPLE_FACTOR': <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_FACTOR: 35>, 'OpenGl_OCCT_WIREFRAME_COLOR': <OpenGl_StateVariable.OpenGl_OCCT_WIREFRAME_COLOR: 36>, 'OpenGl_OCCT_QUAD_MODE_STATE': <OpenGl_StateVariable.OpenGl_OCCT_QUAD_MODE_STATE: 37>, 'OpenGl_OCCT_ORTHO_SCALE': <OpenGl_StateVariable.OpenGl_OCCT_ORTHO_SCALE: 38>, 'OpenGl_OCCT_SILHOUETTE_THICKNESS': <OpenGl_StateVariable.OpenGl_OCCT_SILHOUETTE_THICKNESS: 39>, 'OpenGl_OCCT_NB_SPEC_IBL_LEVELS': <OpenGl_StateVariable.OpenGl_OCCT_NB_SPEC_IBL_LEVELS: 40>, 'OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES': <OpenGl_StateVariable.OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: 41>}
    pass
class OpenGl_StencilTest(OpenGl_Element):
    """
    None
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        None
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Render primitives to the window
        """
    def SetOptions(self,theIsEnabled : bool) -> None: 
        """
        None
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_Structure(OCP.Graphic3d.Graphic3d_CStructure, OCP.Standard.Standard_Transient):
    """
    Implementation of low-level graphic structure.Implementation of low-level graphic structure.
    """
    def BndBoxClipCheck(self) -> bool: 
        """
        Returns whether check of object's bounding box clipping is enabled before drawing of object; TRUE by default.
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of this presentation
        """
    def ChangeBoundingBox(self) -> Any: 
        """
        Returns bounding box of this presentation without transformation matrix applied
        """
    @overload
    def Clear(self) -> None: 
        """
        Clear graphic data

        None
        """
    @overload
    def Clear(self,theGlCtx : OpenGl_Context) -> None: ...
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Returns associated clip planes
        """
    def Connect(self,theStructure : OCP.Graphic3d.Graphic3d_CStructure) -> None: 
        """
        Connect other structure to this one
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Disconnect(self,theStructure : OCP.Graphic3d.Graphic3d_CStructure) -> None: 
        """
        Disconnect other structure to this one
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
    def GlDriver(self) -> OpenGl_GraphicDriver: 
        """
        Access graphic driver
        """
    def GraphicDriver(self) -> OCP.Graphic3d.Graphic3d_GraphicDriver: 
        """
        Returns graphic driver created this structure
        """
    def GraphicHighlight(self,theStyle : OCP.Graphic3d.Graphic3d_PresentationAttributes) -> None: 
        """
        Highlights structure according to the given style and updates corresponding class fields (highlight status and style)
        """
    def GraphicUnhighlight(self) -> None: 
        """
        Unighlights structure and updates corresponding class fields (highlight status and style)
        """
    def Groups(self) -> OCP.Graphic3d.Graphic3d_SequenceOfGroup: 
        """
        Returns graphic groups
        """
    def HighlightStyle(self) -> OCP.Graphic3d.Graphic3d_PresentationAttributes: 
        """
        Returns valid handle to highlight style of the structure in case if highlight flag is set to true
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InstancedStructure(self) -> OpenGl_Structure: 
        """
        Returns instanced OpenGL structure.
        """
    def IsAlwaysRendered(self) -> bool: 
        """
        Checks if the structure should be included into BVH tree or not.
        """
    def IsCulled(self) -> bool: 
        """
        Returns FALSE if the structure hits the current view volume, otherwise returns TRUE.
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
    def IsRaytracable(self) -> bool: 
        """
        Is the structure ray-tracable (contains ray-tracable elements)?
        """
    @overload
    def IsVisible(self,theViewId : int) -> bool: 
        """
        Return structure visibility flag

        Return structure visibility considering both View Affinity and global visibility state.
        """
    @overload
    def IsVisible(self) -> bool: ...
    def MarkAsNotCulled(self) -> None: 
        """
        Marks structure as overlapping the current view volume one. The method is called during traverse of BVH tree.
        """
    def ModificationState(self) -> int: 
        """
        Returns structure modification state (for ray-tracing).
        """
    def NewGroup(self,theStruct : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Create new group within this structure
        """
    def OnVisibilityChanged(self) -> None: 
        """
        Setup structure graphic state
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Releases structure resources.
        """
    def ReleaseGlResources(self,theGlCtx : OpenGl_Context) -> None: 
        """
        This method releases GL resources without actual elements destruction. As result structure could be correctly destroyed layer without GL context (after last window was closed for example).
        """
    def RemoveGroup(self,theGroup : OCP.Graphic3d.Graphic3d_Group) -> None: 
        """
        Remove group from this structure
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Renders the structure.
        """
    def ResetModificationState(self) -> None: 
        """
        Resets structure modification state (for ray-tracing).
        """
    def SetBndBoxClipCheck(self,theBndBoxClipCheck : bool) -> None: 
        """
        Enable/disable check of object's bounding box clipping before drawing of object.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Pass clip planes to the associated graphic driver structure
        """
    def SetCulled(self,theIsCulled : bool) -> None: 
        """
        Marks structure as culled/not culled - note that IsAlwaysRendered() is ignored here!
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def SetTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: 
        """
        Synchronize structure transformation
        """
    def SetZLayer(self,theLayerIndex : int) -> None: 
        """
        Set z layer ID to display the structure in specified layer
        """
    def ShadowLink(self,theManager : OCP.Graphic3d.Graphic3d_StructureManager) -> OCP.Graphic3d.Graphic3d_CStructure: 
        """
        Create shadow link to this structure
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def Transformation(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return transformation.
        """
    def ZLayer(self) -> int: 
        """
        Get z layer ID
        """
    def __init__(self,theManager : OCP.Graphic3d.Graphic3d_StructureManager) -> None: ...
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
    def updateLayerTransformation(self) -> None: 
        """
        Update render transformation matrix.
        """
    @property
    def myZLayer(self) -> int:
        """
        :type: int
        """
    @myZLayer.setter
    def myZLayer(self, arg0: int) -> None:
        pass
    pass
class OpenGl_StructureShadow(OpenGl_Structure, OCP.Graphic3d.Graphic3d_CStructure, OCP.Standard.Standard_Transient):
    """
    Dummy structure which just redirects to groups of another structure.Dummy structure which just redirects to groups of another structure.
    """
    def BndBoxClipCheck(self) -> bool: 
        """
        Returns whether check of object's bounding box clipping is enabled before drawing of object; TRUE by default.
        """
    def BoundingBox(self) -> Any: 
        """
        Returns bounding box of this presentation
        """
    def ChangeBoundingBox(self) -> Any: 
        """
        Returns bounding box of this presentation without transformation matrix applied
        """
    @overload
    def Clear(self) -> None: 
        """
        Clear graphic data

        None
        """
    @overload
    def Clear(self,theGlCtx : OpenGl_Context) -> None: ...
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Returns associated clip planes
        """
    def Connect(self,arg1 : OCP.Graphic3d.Graphic3d_CStructure) -> None: 
        """
        Raise exception on API misuse.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Disconnect(self,arg1 : OCP.Graphic3d.Graphic3d_CStructure) -> None: 
        """
        Raise exception on API misuse.
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
    def GlDriver(self) -> OpenGl_GraphicDriver: 
        """
        Access graphic driver
        """
    def GraphicDriver(self) -> OCP.Graphic3d.Graphic3d_GraphicDriver: 
        """
        Returns graphic driver created this structure
        """
    def GraphicHighlight(self,theStyle : OCP.Graphic3d.Graphic3d_PresentationAttributes) -> None: 
        """
        Highlights structure according to the given style and updates corresponding class fields (highlight status and style)
        """
    def GraphicUnhighlight(self) -> None: 
        """
        Unighlights structure and updates corresponding class fields (highlight status and style)
        """
    def Groups(self) -> OCP.Graphic3d.Graphic3d_SequenceOfGroup: 
        """
        Returns graphic groups
        """
    def HighlightStyle(self) -> OCP.Graphic3d.Graphic3d_PresentationAttributes: 
        """
        Returns valid handle to highlight style of the structure in case if highlight flag is set to true
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InstancedStructure(self) -> OpenGl_Structure: 
        """
        Returns instanced OpenGL structure.
        """
    def IsAlwaysRendered(self) -> bool: 
        """
        Checks if the structure should be included into BVH tree or not.
        """
    def IsCulled(self) -> bool: 
        """
        Returns FALSE if the structure hits the current view volume, otherwise returns TRUE.
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
    def IsRaytracable(self) -> bool: 
        """
        Is the structure ray-tracable (contains ray-tracable elements)?
        """
    @overload
    def IsVisible(self,theViewId : int) -> bool: 
        """
        Return structure visibility flag

        Return structure visibility considering both View Affinity and global visibility state.
        """
    @overload
    def IsVisible(self) -> bool: ...
    def MarkAsNotCulled(self) -> None: 
        """
        Marks structure as overlapping the current view volume one. The method is called during traverse of BVH tree.
        """
    def ModificationState(self) -> int: 
        """
        Returns structure modification state (for ray-tracing).
        """
    def NewGroup(self,theStruct : OCP.Graphic3d.Graphic3d_Structure) -> OCP.Graphic3d.Graphic3d_Group: 
        """
        Create new group within this structure
        """
    def OnVisibilityChanged(self) -> None: 
        """
        Setup structure graphic state
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Releases structure resources.
        """
    def ReleaseGlResources(self,theGlCtx : OpenGl_Context) -> None: 
        """
        This method releases GL resources without actual elements destruction. As result structure could be correctly destroyed layer without GL context (after last window was closed for example).
        """
    def RemoveGroup(self,theGroup : OCP.Graphic3d.Graphic3d_Group) -> None: 
        """
        Remove group from this structure
        """
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        Renders the structure.
        """
    def ResetModificationState(self) -> None: 
        """
        Resets structure modification state (for ray-tracing).
        """
    def SetBndBoxClipCheck(self,theBndBoxClipCheck : bool) -> None: 
        """
        Enable/disable check of object's bounding box clipping before drawing of object.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Pass clip planes to the associated graphic driver structure
        """
    def SetCulled(self,theIsCulled : bool) -> None: 
        """
        Marks structure as culled/not culled - note that IsAlwaysRendered() is ignored here!
        """
    def SetTransformPersistence(self,theTrsfPers : OCP.Graphic3d.Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def SetTransformation(self,theTrsf : OCP.TopLoc.TopLoc_Datum3D) -> None: 
        """
        Synchronize structure transformation
        """
    def SetZLayer(self,theLayerIndex : int) -> None: 
        """
        Set z layer ID to display the structure in specified layer
        """
    def ShadowLink(self,theManager : OCP.Graphic3d.Graphic3d_StructureManager) -> OCP.Graphic3d.Graphic3d_CStructure: 
        """
        Create shadow link to this structure
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformPersistence(self) -> OCP.Graphic3d.Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def Transformation(self) -> OCP.TopLoc.TopLoc_Datum3D: 
        """
        Return transformation.
        """
    def ZLayer(self) -> int: 
        """
        Get z layer ID
        """
    def __init__(self,theManager : OCP.Graphic3d.Graphic3d_StructureManager,theStructure : OpenGl_Structure) -> None: ...
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
    def updateLayerTransformation(self) -> None: 
        """
        Update render transformation matrix.
        """
    @property
    def myZLayer(self) -> int:
        """
        :type: int
        """
    @myZLayer.setter
    def myZLayer(self, arg0: int) -> None:
        pass
    pass
class OpenGl_Text(OpenGl_Element):
    """
    Text rendering
    """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    @staticmethod
    def FindFont_s(theCtx : OpenGl_Context,theAspect : OpenGl_Aspects,theHeight : int,theResolution : int,theKey : OCP.TCollection.TCollection_AsciiString) -> OpenGl_Font: 
        """
        Find shared resource for specified font or initialize new one
        """
    @staticmethod
    def FontKey_s(theAspect : OpenGl_Aspects,theHeight : int,theResolution : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Create key for shared resource
        """
    def Init(self,theCtx : OpenGl_Context,theText : str,thePoint : OCP.Graphic3d.Graphic3d_Vec3) -> None: 
        """
        Setup new string and position
        """
    def Is2D(self) -> bool: 
        """
        Return true if text is 2D
        """
    def IsFillDrawMode(self) -> bool: 
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """
    def Release(self,theContext : OpenGl_Context) -> None: 
        """
        None
        """
    @overload
    def Render(self,theWorkspace : OpenGl_Workspace) -> None: 
        """
        None

        Perform rendering
        """
    @overload
    def Render(self,theCtx : OpenGl_Context,theTextAspect : OpenGl_Aspects,theResolution : int=72) -> None: ...
    def Reset(self,theCtx : OpenGl_Context) -> None: 
        """
        Release cached VBO resources and the previous font if height changed. Cached structures will be refilled by the next render. Call Reset after modifying text parameters.
        """
    def Set2D(self,theEnable : bool) -> None: 
        """
        Set true if text is 2D
        """
    def SetFontSize(self,theContext : OpenGl_Context,theFontSize : int) -> None: 
        """
        Setup new font size
        """
    def SetPosition(self,thePoint : OCP.Graphic3d.Graphic3d_Vec3) -> None: 
        """
        Setup new position
        """
    def SetText(self,theText : OCP.Graphic3d.Graphic3d_Text) -> None: 
        """
        Sets text parameters
        """
    @staticmethod
    def StringSize_s(theCtx : OpenGl_Context,theText : OCP.NCollection.NCollection_Utf8String,theTextAspect : OpenGl_Aspects,theHeight : float,theResolution : int,theWidth : float,theAscent : float,theDescent : float) -> None: 
        """
        Compute text width
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update parameters of the drawable elements.
        """
    def Text(self) -> OCP.Graphic3d.Graphic3d_Text: 
        """
        Returns text parameters
        """
    def UpdateDrawStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp,theIsDetailed : bool) -> None: 
        """
        Increment draw calls statistics.
        """
    def UpdateMemStats(self,theStats : OCP.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None: 
        """
        Increment memory usage statistics. Default implementation puts EstimatedDataSize() into Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """
    @overload
    def __init__(self,theTextParams : OCP.Graphic3d.Graphic3d_Text) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class OpenGl_TextBuilder():
    """
    This class generates primitive array required for rendering textured text using OpenGl_Font instance.
    """
    def Perform(self,theFormatter : OCP.Font.Font_TextFormatter,theContext : OpenGl_Context,theFont : OpenGl_Font,theTextures : Any,theVertsPerTexture : Any,theTCrdsPerTexture : Any) -> None: 
        """
        Creates texture quads for the given text.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_PointSprite(OpenGl_Texture, OpenGl_NamedResource, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Point sprite resource. On modern hardware it will be texture with extra parameters. On ancient hardware sprites will be drawn using bitmaps.Point sprite resource. On modern hardware it will be texture with extra parameters. On ancient hardware sprites will be drawn using bitmaps.Point sprite resource. On modern hardware it will be texture with extra parameters. On ancient hardware sprites will be drawn using bitmaps.
    """
    @overload
    def Bind(self,theCtx : OpenGl_Context) -> None: 
        """
        Bind this Texture to the unit specified in sampler parameters. Also binds Sampler Object if it is allocated.

        Bind this Texture to specified unit. Also binds Sampler Object if it is allocated.
        """
    @overload
    def Bind(self,theCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: ...
    def Create(self,theCtx : OpenGl_Context) -> bool: 
        """
        Creates Texture id if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DrawBitmap(self,theCtx : OpenGl_Context) -> None: 
        """
        Draw sprite using glBitmap. Please call glRasterPos3fv() before to setup sprite position.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    @staticmethod
    @overload
    def GetDataFormat_s(theCtx : OpenGl_Context,theFormat : OCP.Image.Image_Format,theTextFormat : int,thePixelFormat : int,theDataType : int) -> bool: 
        """
        None

        None
        """
    @staticmethod
    @overload
    def GetDataFormat_s(theCtx : OpenGl_Context,theData : OCP.Image.Image_PixMap,theTextFormat : int,thePixelFormat : int,theDataType : int) -> bool: ...
    def GetFormat(self) -> int: 
        """
        Returns texture format (not sized)
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTarget(self) -> int: 
        """
        Returns target to which the texture is bound (GL_TEXTURE_1D, GL_TEXTURE_2D)
        """
    def HasMipmaps(self) -> bool: 
        """
        Returns true if texture was generated within mipmaps
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theCtx : OpenGl_Context,theTextFormat : int,thePixelFormat : int,theDataType : int,theSizeX : int,theSizeY : int,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theImage : OCP.Image.Image_PixMap=None) -> bool: 
        """
        Notice that texture will be unbound after this call.

        Initialize the texture with specified format, size and texture type. If theImage is empty the texture data will contain trash. Notice that texture will be unbound after this call.

        Initialize the texture with Graphic3d_TextureMap. It is an universal way to initialize. Suitable initialization method will be chosen.

        None

        None
        """
    @overload
    def Init(self,theCtx : OpenGl_Context,theTextureMap : OCP.Graphic3d.Graphic3d_TextureMap) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_PixMap,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theFormat : OpenGl_TextureFormat,theSizeXY : OCP.Graphic3d.Graphic3d_Vec2i,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theImage : OCP.Image.Image_PixMap=None) -> bool: ...
    @overload
    def Init(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_PixMap,theType : OCP.Graphic3d.Graphic3d_TypeOfTexture,theIsColorMap : bool) -> bool: ...
    def Init2DMultisample(self,theCtx : OpenGl_Context,theNbSamples : int,theTextFormat : int,theSizeX : int,theSizeY : int) -> bool: 
        """
        Initialize the 2D multisampling texture using glTexImage2DMultisample().
        """
    @overload
    def Init3D(self,theCtx : OpenGl_Context,theFormat : OpenGl_TextureFormat,theSizeXYZ : OCP.Graphic3d.Graphic3d_Vec3i,thePixels : capsule) -> bool: 
        """
        Initializes 3D texture rectangle with specified format and size.

        None
        """
    @overload
    def Init3D(self,theCtx : OpenGl_Context,theTextFormat : int,thePixelFormat : int,theDataType : int,theSizeX : int,theSizeY : int,theSizeZ : int,thePixels : capsule) -> bool: ...
    def InitCompressed(self,theCtx : OpenGl_Context,theImage : OCP.Image.Image_CompressedPixMap,theIsColorMap : bool) -> bool: 
        """
        Initialize the texture with Image_CompressedPixMap.
        """
    def InitCubeMap(self,theCtx : OpenGl_Context,theCubeMap : OCP.Graphic3d.Graphic3d_CubeMap,theSize : int,theFormat : OCP.Image.Image_Format,theToGenMipmap : bool,theIsColorMap : bool) -> bool: 
        """
        Initializes 6 sides of cubemap. If theCubeMap is not NULL then size and format will be taken from it and corresponding arguments will be ignored. Otherwise this parametres will be taken from arguments.
        """
    def InitRectangle(self,theCtx : OpenGl_Context,theSizeX : int,theSizeY : int,theFormat : OpenGl_TextureFormat) -> bool: 
        """
        Allocates texture rectangle with specified format and size.
        """
    def InitSamplerObject(self,theCtx : OpenGl_Context) -> bool: 
        """
        Initialize the Sampler Object (as OpenGL object).
        """
    def IsAlpha(self) -> bool: 
        """
        Return true for GL_RED and GL_ALPHA formats.
        """
    def IsDisplayList(self) -> bool: 
        """
        Returns true if this is display list bitmap
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
    def IsPointSprite(self) -> bool: 
        """
        Returns TRUE for point sprite texture.
        """
    def IsTopDown(self) -> bool: 
        """
        Return if 2D surface is defined top-down (TRUE) or bottom-up (FALSE). Normally set from Image_PixMap::IsTopDown() within texture initialization.
        """
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def MaxMipmapLevel(self) -> int: 
        """
        Return upper mipmap level index (0 means no mipmaps).
        """
    @staticmethod
    def PixelSizeOfPixelFormat_s(theInternalFormat : int) -> int: 
        """
        Return pixel size of pixel format in bytes. Note that this method considers that OpenGL natively supports this pixel format, which might be not the case - in the latter case, actual pixel size might differ!
        """
    def Release(self,theCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def ResourceId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return resource name.
        """
    def Revision(self) -> int: 
        """
        Revision of associated data source.
        """
    def Sampler(self) -> OpenGl_Sampler: 
        """
        Return texture sampler.
        """
    def SetAlpha(self,theValue : bool) -> None: 
        """
        Setup to interpret the format as Alpha by Shader Manager (should be GL_ALPHA within compatible context or GL_RED otherwise).
        """
    def SetDisplayList(self,theCtx : OpenGl_Context,theBitmapList : int) -> None: 
        """
        Initialize point sprite as display list
        """
    def SetRevision(self,theRevision : int) -> None: 
        """
        Set revision of associated data source.
        """
    def SetSampler(self,theSampler : OpenGl_Sampler) -> None: 
        """
        Set texture sampler.
        """
    def SetTopDown(self,theIsTopDown : bool) -> None: 
        """
        Set if 2D surface is defined top-down (TRUE) or bottom-up (FALSE).
        """
    def SizeX(self) -> int: 
        """
        Returns texture width (0 LOD)
        """
    def SizeY(self) -> int: 
        """
        Returns texture height (0 LOD)
        """
    def SizedFormat(self) -> int: 
        """
        Returns texture format (sized)
        """
    def TextureId(self) -> int: 
        """
        Returns texture ID
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: 
        """
        Unbind texture from the unit specified in sampler parameters. Also unbinds Sampler Object if it is allocated.

        Unbind texture from specified unit. Also unbinds Sampler Object if it is allocated.
        """
    @overload
    def Unbind(self,theCtx : OpenGl_Context) -> None: ...
    def __init__(self,theResourceId : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class OpenGl_TextureBufferArb(OpenGl_VertexBuffer, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Texture Buffer Object. This is a special 1D texture that VBO-style initialized. The main differences from general 1D texture: - no interpolation between field; - greater sizes; - special sampler object in GLSL shader to access data by index.Texture Buffer Object. This is a special 1D texture that VBO-style initialized. The main differences from general 1D texture: - no interpolation between field; - greater sizes; - special sampler object in GLSL shader to access data by index.
    """
    def Bind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind this VBO.
        """
    def BindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind all vertex attributes to active program OpenGl_Context::ActiveProgram() or for FFP. Default implementation does nothing.
        """
    def BindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Bind this VBO and enable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def BindPositionAttribute(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind vertex position attribute only. Default implementation does nothing.
        """
    def BindTexture(self,theGlCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: 
        """
        Bind TBO to specified Texture Unit.
        """
    def BindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Bind this VBO to active GLSL program.
        """
    def Create(self,theGlCtx : OpenGl_Context) -> bool: 
        """
        Creates VBO and Texture names (ids) if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetComponentsNb(self) -> int: 
        """
        Returns the number of components per generic vertex attribute.
        """
    def GetDataOffset(self) -> int: 
        """
        Returns offset to data, NULL by default
        """
    def GetDataType(self) -> int: 
        """
        Returns data type of each component in the array.
        """
    def GetElemsNb(self) -> int: 
        """
        Returns number of vertex attributes / number of vertices specified within ::Init()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: 
        """
        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: ...
    def GetTarget(self) -> int: 
        """
        Override VBO target
        """
    def HasColorAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex color attribute
        """
    def HasNormalAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex normal attribute
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : float) -> bool: 
        """
        Perform TBO initialization with specified data. Existing data will be deleted.

        Perform TBO initialization with specified data. Existing data will be deleted.

        Perform TBO initialization with specified data. Existing data will be deleted.

        Perform TBO initialization with specified data. Existing data will be deleted.
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : int) -> bool: ...
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
    def IsValid(self) -> bool: 
        """
        Returns true if TBO is valid. Notice that no any real GL call is performed!
        """
    def IsVirtual(self) -> bool: 
        """
        Return TRUE if this is a virtual (for backward compatibility) VBO object.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def SetElemsNb(self,theNbElems : int) -> None: 
        """
        Overrides the number of vertex attributes / number of vertexes. It is up to user specifying this number correct (e.g. below initial value)!
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: 
        """
        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: ...
    def TextureFormat(self) -> int: 
        """
        Returns internal texture format.
        """
    def TextureId(self) -> int: 
        """
        Returns name of TBO.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unbind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind this VBO.
        """
    def UnbindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind all vertex attributes. Default implementation does nothing.
        """
    def UnbindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Unbind this VBO and disable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def UnbindTexture(self,theGlCtx : OpenGl_Context,theTextureUnit : OCP.Graphic3d.Graphic3d_TextureUnit) -> None: 
        """
        Unbind TBO.
        """
    def UnbindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Unbind any VBO from active GLSL program.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def bindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theNbComp : int,theDataType : int,theStride : int,theOffset : capsule) -> None: 
        """
        Setup array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using bindFixed() when no program bound.
        """
    def getSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Read back buffer sub-range.
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
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Initialize buffer with new data.

        Initialize buffer with new data.
        """
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int,theStride : int) -> bool: ...
    @staticmethod
    def sizeOfGlType_s(theType : int) -> int: 
        """
        Returns size of specified GL type
        """
    def subData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Update part of the buffer with new data.
        """
    @staticmethod
    def unbindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Disable GLSL array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using unbindFixed() when no program bound.
        """
    pass
class OpenGl_TextureFormat():
    """
    Stores parameters of OpenGL texture format.
    """
    def DataType(self) -> int: 
        """
        Returns OpenGL data type of the pixel data (example: GL_FLOAT).
        """
    @staticmethod
    def FindCompressedFormat_s(theCtx : OpenGl_Context,theFormat : OCP.Image.Image_CompressedFormat,theIsColorMap : bool) -> OpenGl_TextureFormat: 
        """
        Find texture format suitable to specified compressed texture format.
        """
    @staticmethod
    def FindFormat_s(theCtx : OpenGl_Context,theFormat : OCP.Image.Image_Format,theIsColorMap : bool) -> OpenGl_TextureFormat: 
        """
        Find texture format suitable to specified image format.
        """
    @staticmethod
    def FindSizedFormat_s(theCtx : OpenGl_Context,theSizedFormat : int) -> OpenGl_TextureFormat: 
        """
        Find texture format suitable to specified internal (sized) texture format.
        """
    def Format(self) -> int: 
        """
        Returns OpenGL format of the pixel data (example: GL_RED).
        """
    def Internal(self) -> int: 
        """
        Returns OpenGL internal format of the pixel data (example: GL_R32F).
        """
    def InternalFormat(self) -> int: 
        """
        Returns OpenGL internal format of the pixel data (example: GL_R32F).
        """
    def IsSRGB(self) -> bool: 
        """
        Return TRUE if internal texture format is sRGB(A).
        """
    def IsValid(self) -> bool: 
        """
        Return TRUE if format is defined.
        """
    def NbComponents(self) -> int: 
        """
        Returns number of components (channels). Here for debugging purposes.
        """
    def PixelFormat(self) -> int: 
        """
        Returns OpenGL format of the pixel data (example: GL_RED).
        """
    def SetDataType(self,theType : int) -> None: 
        """
        Sets OpenGL data type of the pixel data.
        """
    def SetInternalFormat(self,theInternal : int) -> None: 
        """
        Sets texture internal format.
        """
    def SetNbComponents(self,theNbComponents : int) -> None: 
        """
        Sets number of components (channels).
        """
    def SetPixelFormat(self,theFormat : int) -> None: 
        """
        Sets OpenGL format of the pixel data.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLbyte():
    """
    Specialization for signed byte.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLfloat():
    """
    Specialization for float.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLint():
    """
    Specialization for signed int.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLshort():
    """
    Specialization for signed short.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLubyte():
    """
    Specialization for unsigned byte.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLuint():
    """
    Specialization for unsigned int.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureFormatSelector_GLushort():
    """
    Specialization for unsigned short.
    """
    @staticmethod
    def DataType_s() -> int: 
        """
        None
        """
    @staticmethod
    def Internal_s(theChannels : int) -> int: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TextureSet(OCP.Standard.Standard_Transient):
    """
    Class holding array of textures to be mapped as a set. Textures should be defined in ascending order of texture units within the set.
    """
    def ChangeFirst(self) -> OpenGl_Texture: 
        """
        Return the first texture.
        """
    def ChangeLast(self) -> OpenGl_Texture: 
        """
        Return the last texture.
        """
    def ChangeLastUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Return the last texture unit.
        """
    def ChangeValue(self,theIndex : int) -> OpenGl_Texture: 
        """
        Return the texture at specified position within [0, Size()) range.
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
    def First(self) -> OpenGl_Texture: 
        """
        Return the first texture.
        """
    def FirstUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Return the first texture unit.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasNonPointSprite(self) -> bool: 
        """
        Return TRUE if other than point sprite textures are defined within point set.
        """
    def HasPointSprite(self) -> bool: 
        """
        Return TRUE if last texture is a point sprite.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitZero(self) -> None: 
        """
        Nullify all handles.
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if texture array is empty.
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
    def IsModulate(self) -> bool: 
        """
        Return TRUE if texture color modulation has been enabled for the first texture or if texture is not set at all.
        """
    def Last(self) -> OpenGl_Texture: 
        """
        Return the last texture.
        """
    def LastUnit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Return the last texture unit.
        """
    def Lower(self) -> int: 
        """
        Return the lower index in texture set.
        """
    def Size(self) -> int: 
        """
        Return number of textures.
        """
    def TextureSetBits(self) -> int: 
        """
        Return texture units declared within the program,
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Return the upper index in texture set.
        """
    def Value(self,theIndex : int) -> OpenGl_Texture: 
        """
        Return the texture at specified position within [0, Size()) range.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbTextures : int) -> None: ...
    @overload
    def __init__(self,theTexture : OpenGl_Texture) -> None: ...
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
    @property
    def ChangeTextureSetBits(self) -> int:
        """
        Return texture units declared within the program,

        :type: int
        """
    @ChangeTextureSetBits.setter
    def ChangeTextureSetBits(self, arg1: int) -> None:
        """
        Return texture units declared within the program,
        """
    pass
class OpenGl_TextureSetPairIterator():
    """
    Class for iterating pair of texture sets through each defined texture slot. Note that iterator considers texture slots being in ascending order within OpenGl_TextureSet.
    """
    def More(self) -> bool: 
        """
        Return TRUE if there are more texture units to pass through.
        """
    def Next(self) -> None: 
        """
        Move iterator position to the next pair.
        """
    def Texture1(self) -> OpenGl_Texture: 
        """
        Access texture from first texture set.
        """
    def Texture2(self) -> OpenGl_Texture: 
        """
        Access texture from second texture set.
        """
    def Unit(self) -> OCP.Graphic3d.Graphic3d_TextureUnit: 
        """
        Return current texture unit.
        """
    def __init__(self,theSet1 : OpenGl_TextureSet,theSet2 : OpenGl_TextureSet) -> None: ...
    pass
class OpenGl_TileSampler():
    """
    Tool object used for sampling screen tiles according to estimated pixel variance (used in path tracing engine). To improve GPU thread coherency, rendering window is split into pixel blocks or tiles. The important feature of this approach is that it is possible to keep the same number of tiles for any screen resolution (e.g. 256 tiles can be used for both 512 x 512 window and 1920 x 1080 window). So, a smaller number of tiles allows to increase interactivity (FPS), but at the cost of higher per-frame variance ('noise'). On the contrary a larger number of tiles decrease interactivity, but leads to lower per-frame variance. Note that the total time needed to produce final final image is the same for both cases.
    """
    def GrabVarianceMap(self,theContext : OpenGl_Context,theTexture : OpenGl_Texture) -> None: 
        """
        Fetches current error estimation from the GPU and builds 2D discrete distribution for tile sampling.
        """
    def MaxTileSamples(self) -> int: 
        """
        Return maximum number of samples per tile.
        """
    def NbOffsetTiles(self,theAdaptive : bool) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Number of tiles within offsets texture.
        """
    def NbOffsetTilesMax(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Maximum number of tiles within offsets texture.
        """
    def NbTiles(self) -> int: 
        """
        Returns total number of tiles in viewport.
        """
    def NbTilesX(self) -> int: 
        """
        Returns number of tiles in X dimension.
        """
    def NbTilesY(self) -> int: 
        """
        Returns number of tiles in Y dimension.
        """
    def OffsetTilesViewport(self,theAdaptive : bool) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Viewport for rendering using offsets texture.
        """
    def OffsetTilesViewportMax(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Maximum viewport for rendering using offsets texture.
        """
    def Reset(self) -> None: ...
    def SetSize(self,theParams : OCP.Graphic3d.Graphic3d_RenderingParams,theSize : OCP.Graphic3d.Graphic3d_Vec2i) -> None: 
        """
        Specifies size of ray-tracing viewport and recomputes tile size.
        """
    def TileSize(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Size of individual tile in pixels.
        """
    def UploadOffsets(self,theContext : OpenGl_Context,theOffsetsTexture : OpenGl_Texture,theAdaptive : bool) -> bool: 
        """
        Uploads offsets of sampled tiles to the given OpenGL texture.
        """
    def UploadSamples(self,theContext : OpenGl_Context,theSamplesTexture : OpenGl_Texture,theAdaptive : bool) -> bool: 
        """
        Uploads tile samples to the given OpenGL texture.
        """
    def VarianceScaleFactor(self) -> float: 
        """
        Scale factor for quantization of visual error (float) into signed integer.
        """
    def ViewSize(self) -> OCP.Graphic3d.Graphic3d_Vec2i: 
        """
        Returns ray-tracing viewport.
        """
    def __init__(self) -> None: ...
    pass
class OpenGl_TriangleSet(OpenGl_BVHTriangulation3f):
    """
    Triangulation of single OpenGL primitive array.
    """
    def AssociatedPArrayID(self) -> int: 
        """
        Returns ID of associated primitive array.
        """
    def Box(self) -> Any: 
        """
        Returns AABB of primitive set.
        """
    def Center(self,theIndex : int,theAxis : int) -> float: 
        """
        Returns centroid position along the given axis.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def MaterialIndex(self) -> int: 
        """
        Returns material index of triangle set.
        """
    def QuadBVH(self) -> Any: 
        """
        Returns quad BVH (QBVH) tree produced from binary BVH.
        """
    def SetMaterialIndex(self,theMatID : int) -> None: 
        """
        Sets material index for entire triangle set.
        """
    def Size(self) -> int: 
        """
        Returns total number of triangles.
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Performs transposing the two given triangles in the set.
        """
    def __init__(self,theArrayID : int,theBuilder : Any) -> None: ...
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
class OpenGl_UniformStateType():
    """
    Defines types of uniform state variables.

    Members:

      OpenGl_LIGHT_SOURCES_STATE

      OpenGl_CLIP_PLANES_STATE

      OpenGl_MODEL_WORLD_STATE

      OpenGl_WORLD_VIEW_STATE

      OpenGl_PROJECTION_STATE

      OpenGl_MATERIAL_STATE

      OpenGl_SURF_DETAIL_STATE

      OpenGL_OIT_STATE

      OpenGl_UniformStateType_NB
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
    OpenGL_OIT_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGL_OIT_STATE: 7>
    OpenGl_CLIP_PLANES_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_CLIP_PLANES_STATE: 1>
    OpenGl_LIGHT_SOURCES_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_LIGHT_SOURCES_STATE: 0>
    OpenGl_MATERIAL_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_MATERIAL_STATE: 5>
    OpenGl_MODEL_WORLD_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_MODEL_WORLD_STATE: 2>
    OpenGl_PROJECTION_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_PROJECTION_STATE: 4>
    OpenGl_SURF_DETAIL_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_SURF_DETAIL_STATE: 6>
    OpenGl_UniformStateType_NB: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_UniformStateType_NB: 8>
    OpenGl_WORLD_VIEW_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_WORLD_VIEW_STATE: 3>
    __entries: dict # value = {'OpenGl_LIGHT_SOURCES_STATE': (<OpenGl_UniformStateType.OpenGl_LIGHT_SOURCES_STATE: 0>, None), 'OpenGl_CLIP_PLANES_STATE': (<OpenGl_UniformStateType.OpenGl_CLIP_PLANES_STATE: 1>, None), 'OpenGl_MODEL_WORLD_STATE': (<OpenGl_UniformStateType.OpenGl_MODEL_WORLD_STATE: 2>, None), 'OpenGl_WORLD_VIEW_STATE': (<OpenGl_UniformStateType.OpenGl_WORLD_VIEW_STATE: 3>, None), 'OpenGl_PROJECTION_STATE': (<OpenGl_UniformStateType.OpenGl_PROJECTION_STATE: 4>, None), 'OpenGl_MATERIAL_STATE': (<OpenGl_UniformStateType.OpenGl_MATERIAL_STATE: 5>, None), 'OpenGl_SURF_DETAIL_STATE': (<OpenGl_UniformStateType.OpenGl_SURF_DETAIL_STATE: 6>, None), 'OpenGL_OIT_STATE': (<OpenGl_UniformStateType.OpenGL_OIT_STATE: 7>, None), 'OpenGl_UniformStateType_NB': (<OpenGl_UniformStateType.OpenGl_UniformStateType_NB: 8>, None)}
    __members__: dict # value = {'OpenGl_LIGHT_SOURCES_STATE': <OpenGl_UniformStateType.OpenGl_LIGHT_SOURCES_STATE: 0>, 'OpenGl_CLIP_PLANES_STATE': <OpenGl_UniformStateType.OpenGl_CLIP_PLANES_STATE: 1>, 'OpenGl_MODEL_WORLD_STATE': <OpenGl_UniformStateType.OpenGl_MODEL_WORLD_STATE: 2>, 'OpenGl_WORLD_VIEW_STATE': <OpenGl_UniformStateType.OpenGl_WORLD_VIEW_STATE: 3>, 'OpenGl_PROJECTION_STATE': <OpenGl_UniformStateType.OpenGl_PROJECTION_STATE: 4>, 'OpenGl_MATERIAL_STATE': <OpenGl_UniformStateType.OpenGl_MATERIAL_STATE: 5>, 'OpenGl_SURF_DETAIL_STATE': <OpenGl_UniformStateType.OpenGl_SURF_DETAIL_STATE: 6>, 'OpenGL_OIT_STATE': <OpenGl_UniformStateType.OpenGL_OIT_STATE: 7>, 'OpenGl_UniformStateType_NB': <OpenGl_UniformStateType.OpenGl_UniformStateType_NB: 8>}
    pass
class OpenGl_IndexBuffer(OpenGl_VertexBuffer, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Index buffer is just a VBO with special target (GL_ELEMENT_ARRAY_BUFFER).Index buffer is just a VBO with special target (GL_ELEMENT_ARRAY_BUFFER).
    """
    def Bind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind this VBO.
        """
    def BindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind all vertex attributes to active program OpenGl_Context::ActiveProgram() or for FFP. Default implementation does nothing.
        """
    def BindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Bind this VBO and enable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def BindPositionAttribute(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind vertex position attribute only. Default implementation does nothing.
        """
    def BindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Bind this VBO to active GLSL program.
        """
    def Create(self,theGlCtx : OpenGl_Context) -> bool: 
        """
        Creates VBO name (id) if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetComponentsNb(self) -> int: 
        """
        Returns the number of components per generic vertex attribute.
        """
    def GetDataOffset(self) -> int: 
        """
        Returns offset to data, NULL by default
        """
    def GetDataType(self) -> int: 
        """
        Returns data type of each component in the array.
        """
    def GetElemsNb(self) -> int: 
        """
        Returns number of vertex attributes / number of vertices specified within ::Init()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: 
        """
        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: ...
    def GetTarget(self) -> int: 
        """
        None
        """
    def HasColorAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex color attribute
        """
    def HasNormalAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex normal attribute
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : int) -> bool: 
        """
        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : float) -> bool: ...
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def IsVirtual(self) -> bool: 
        """
        Return TRUE if this is a virtual (for backward compatibility) VBO object.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release GPU memory if any.
        """
    def SetElemsNb(self,theNbElems : int) -> None: 
        """
        Overrides the number of vertex attributes / number of vertexes. It is up to user specifying this number correct (e.g. below initial value)!
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: 
        """
        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unbind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind this VBO.
        """
    def UnbindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind all vertex attributes. Default implementation does nothing.
        """
    def UnbindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Unbind this VBO and disable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def UnbindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Unbind any VBO from active GLSL program.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def bindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theNbComp : int,theDataType : int,theStride : int,theOffset : capsule) -> None: 
        """
        Setup array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using bindFixed() when no program bound.
        """
    def getSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Read back buffer sub-range.
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
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Initialize buffer with new data.

        Initialize buffer with new data.
        """
    @overload
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int,theStride : int) -> bool: ...
    @staticmethod
    def sizeOfGlType_s(theType : int) -> int: 
        """
        Returns size of specified GL type
        """
    def subData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Update part of the buffer with new data.
        """
    @staticmethod
    def unbindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Disable GLSL array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using unbindFixed() when no program bound.
        """
    pass
class OpenGl_VertexBufferCompat(OpenGl_VertexBuffer, OpenGl_Resource, OCP.Standard.Standard_Transient):
    """
    Compatibility layer for old OpenGL without VBO. Make sure to pass pointer from GetDataOffset() instead of NULL. Method GetDataOffset() returns pointer to real data in this class (while base class OpenGl_VertexBuffer always return NULL).Compatibility layer for old OpenGL without VBO. Make sure to pass pointer from GetDataOffset() instead of NULL. Method GetDataOffset() returns pointer to real data in this class (while base class OpenGl_VertexBuffer always return NULL).
    """
    def Bind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind this VBO.
        """
    def BindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind all vertex attributes to active program OpenGl_Context::ActiveProgram() or for FFP. Default implementation does nothing.
        """
    def BindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Bind this VBO and enable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def BindPositionAttribute(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Bind vertex position attribute only. Default implementation does nothing.
        """
    def BindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Bind this VBO to active GLSL program.
        """
    def Create(self,theGlCtx : OpenGl_Context) -> bool: 
        """
        Creates VBO name (id) if not yet generated. Data should be initialized by another method.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
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
    def EstimatedDataSize(self) -> int: 
        """
        Returns estimated GPU memory usage for holding data without considering overheads and allocation alignment rules.
        """
    def GetComponentsNb(self) -> int: 
        """
        Returns the number of components per generic vertex attribute.
        """
    def GetDataOffset(self) -> int: 
        """
        Returns offset to data, NULL by default
        """
    def GetDataType(self) -> int: 
        """
        Returns data type of each component in the array.
        """
    def GetElemsNb(self) -> int: 
        """
        Returns number of vertex attributes / number of vertices specified within ::Init()
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: 
        """
        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().

        Read back buffer sub-range. Notice that VBO will be unbound after this call. Function reads portion of data from this VBO using glGetBufferSubData().
        """
    @overload
    def GetSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: ...
    def GetTarget(self) -> int: 
        """
        None
        """
    def HasColorAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex color attribute
        """
    def HasNormalAttribute(self) -> bool: 
        """
        Returns true if buffer contains per-vertex normal attribute
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : int) -> bool: 
        """
        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.

        Notice that VBO will be unbound after this call.
        """
    @overload
    def Init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : float) -> bool: ...
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
    def IsValid(self) -> bool: 
        """
        Returns true if current object was initialized
        """
    def IsVirtual(self) -> bool: 
        """
        Return TRUE.
        """
    def Release(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Destroy object - will release memory if any.
        """
    def SetElemsNb(self,theNbElems : int) -> None: 
        """
        Overrides the number of vertex attributes / number of vertexes. It is up to user specifying this number correct (e.g. below initial value)!
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : float) -> bool: 
        """
        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.

        Notice that VBO will be unbound after this call. Function replaces portion of data within this VBO using glBufferSubData(). The VBO should be initialized before call.
        """
    @overload
    def SubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : int) -> bool: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Unbind(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind this VBO.
        """
    def UnbindAllAttributes(self,theGlCtx : OpenGl_Context) -> None: 
        """
        Unbind all vertex attributes. Default implementation does nothing.
        """
    def UnbindAttribute(self,theCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Unbind this VBO and disable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        """
    def UnbindVertexAttrib(self,theGlCtx : OpenGl_Context,theAttribLoc : int) -> None: 
        """
        Unbind any VBO from active GLSL program.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def bindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute,theNbComp : int,theDataType : int,theStride : int,theOffset : capsule) -> None: 
        """
        Setup array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using bindFixed() when no program bound.
        """
    def getSubData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Read back buffer sub-range.
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
    def init(self,theGlCtx : OpenGl_Context,theComponentsNb : int,theElemsNb : int,theData : capsule,theDataType : int,theStride : int) -> bool: 
        """
        Initialize buffer with new data (data will be copied).
        """
    def initLink(self,theData : OCP.NCollection.NCollection_Buffer,theComponentsNb : int,theElemsNb : int,theDataType : int) -> bool: 
        """
        Initialize buffer with existing data. Data will NOT be copied by this method!
        """
    @staticmethod
    def sizeOfGlType_s(theType : int) -> int: 
        """
        Returns size of specified GL type
        """
    def subData(self,theGlCtx : OpenGl_Context,theElemFrom : int,theElemsNb : int,theData : capsule,theDataType : int) -> bool: 
        """
        Update part of the buffer with new data.
        """
    @staticmethod
    def unbindAttribute_s(theGlCtx : OpenGl_Context,theMode : OCP.Graphic3d.Graphic3d_TypeOfAttribute) -> None: 
        """
        Disable GLSL array pointer - either for active GLSL program OpenGl_Context::ActiveProgram() or for FFP using unbindFixed() when no program bound.
        """
    pass
class OpenGl_View(OCP.Graphic3d.Graphic3d_CView, OCP.Graphic3d.Graphic3d_DataStructureManager, OCP.Standard.Standard_Transient):
    """
    Implementation of OpenGl view.Implementation of OpenGl view.Implementation of OpenGl view.
    """
    def Activate(self) -> None: 
        """
        Activates the view. Maps presentations defined within structure manager onto this view.
        """
    def BVHTreeSelector(self) -> OCP.Graphic3d.Graphic3d_CullingTool: 
        """
        Returns selector for BVH tree, providing a possibility to store information about current view volume and to detect which objects are overlapping it.
        """
    def BackfacingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel: 
        """
        Return backfacing model used for the view.
        """
    def Background(self) -> OCP.Aspect.Aspect_Background: 
        """
        Returns background fill color.
        """
    def BackgroundColor(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns background color.
        """
    def BackgroundCubeMap(self) -> OCP.Graphic3d.Graphic3d_CubeMap: 
        """
        Returns cubemap being set last time on background.
        """
    def BackgroundImage(self) -> OCP.Graphic3d.Graphic3d_TextureMap: 
        """
        Returns background image texture map.
        """
    def BackgroundImageStyle(self) -> OCP.Aspect.Aspect_FillMethod: 
        """
        Returns background image fill style.
        """
    def BaseXRCamera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns anchor camera definition (without tracked head orientation).
        """
    def BufferDump(self,theImage : OCP.Image.Image_PixMap,theBufferType : OCP.Graphic3d.Graphic3d_BufferType) -> bool: 
        """
        Dump active rendering buffer into specified memory buffer. In Ray-Tracing allow to get a raw HDR buffer using Graphic3d_BT_RGB_RayTraceHdrLeft buffer type, only Left view will be dumped ignoring stereoscopic parameter.
        """
    def Camera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns camera object of the view.
        """
    def ChangeHiddenObjects(self) -> Any: 
        """
        Returns map of objects hidden within this specific view (not viewer-wise).
        """
    def ChangeRenderingParams(self) -> OCP.Graphic3d.Graphic3d_RenderingParams: 
        """
        Returns reference to current rendering parameters and effect settings.
        """
    def ClearPBREnvironment(self) -> None: 
        """
        Fills PBR specular probe and irradiance map with white color. So that environment indirect illumination will be constant and will be fully controlled by ambient light sources. If PBR is unavailable it does nothing.
        """
    def ClipPlanes(self) -> OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane: 
        """
        Returns list of clip planes set for the view.
        """
    def Compute(self) -> None: 
        """
        Computes the new presentation of the structures displayed in this view with the type Graphic3d_TOS_COMPUTED.
        """
    def ComputeXRBaseCameraFromPosed(self,theCamPosed : OCP.Graphic3d.Graphic3d_Camera,thePoseTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Update based camera from posed camera by applying reversed transformation.
        """
    def ComputeXRPosedCameraFromBase(self,theCam : OCP.Graphic3d.Graphic3d_Camera,theXRTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Compute camera position based on XR pose.
        """
    def ComputedMode(self) -> bool: 
        """
        Returns the computed HLR mode state
        """
    def ConsiderZoomPersistenceObjects(self) -> float: 
        """
        Returns zoom-scale factor.
        """
    @overload
    def ContainsFacet(self) -> bool: 
        """
        Returns Standard_True if one of the structures displayed in the view contains Polygons, Triangles or Quadrangles.

        Returns Standard_True if one of the structures in the set contains Polygons, Triangles or Quadrangles.
        """
    @overload
    def ContainsFacet(self,theSet : Any) -> bool: ...
    def CopySettings(self,theOther : OCP.Graphic3d.Graphic3d_CView) -> None: 
        """
        Copy visualization settings from another view. Method is used for cloning views in viewer when its required to create view with same view properties.
        """
    def Deactivate(self) -> None: 
        """
        Deactivates the view. Unmaps presentations defined within structure manager. The view in deactivated state will ignore actions on structures such as Display().
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DiagnosticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : OCP.Graphic3d.Graphic3d_DiagnosticInfo) -> None: 
        """
        Fill in the dictionary with diagnostic info. Should be called within rendering thread.
        """
    def DisplayedStructures(self,theStructures : Any) -> None: 
        """
        Returns the set of structures displayed in this view.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def FBO(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns pointer to an assigned framebuffer object.
        """
    def FBOChangeViewport(self,theFbo : OCP.Standard.Standard_Transient,theWidth : int,theHeight : int) -> None: 
        """
        Change offscreen FBO viewport.
        """
    def FBOCreate(self,theWidth : int,theHeight : int) -> OCP.Standard.Standard_Transient: 
        """
        Generate offscreen FBO in the graphic library. If not supported on hardware returns NULL.
        """
    def FBOGetDimensions(self,theFbo : OCP.Standard.Standard_Transient) -> Tuple[int, int, int, int]: 
        """
        Read offscreen FBO configuration.
        """
    def FBORelease(self,theFbo : OCP.Standard.Standard_Transient) -> Any: 
        """
        Remove offscreen FBO from the graphic library
        """
    def GeneratePBREnvironment(self) -> None: 
        """
        Generates PBR specular probe and irradiance map in order to provide environment indirect illumination in PBR shading model (Image Based Lighting). The source of environment data is background cubemap. If PBR is unavailable it does nothing. If PBR is available but there is no cubemap being set to background it clears all IBL maps (see 'ClearPBREnvironment').
        """
    def GetGraduatedTrihedron(self) -> OCP.Graphic3d.Graphic3d_GraduatedTrihedron: 
        """
        Returns data of a graduated trihedron
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GlTextureEnv(self) -> OpenGl_TextureSet: 
        """
        Returns OpenGL environment map.
        """
    def GlWindow(self) -> OpenGl_Window: 
        """
        Returns OpenGL window implementation.
        """
    def GradientBackground(self) -> OCP.Aspect.Aspect_GradientBackground: 
        """
        Returns gradient background fill colors.
        """
    def GraduatedTrihedronDisplay(self,theTrihedronData : OCP.Graphic3d.Graphic3d_GraduatedTrihedron) -> None: 
        """
        Displays Graduated Trihedron.
        """
    def GraduatedTrihedronErase(self) -> None: 
        """
        Erases Graduated Trihedron.
        """
    def GraduatedTrihedronMinMaxValues(self,theMin : OCP.Graphic3d.Graphic3d_Vec3,theMax : OCP.Graphic3d.Graphic3d_Vec3) -> None: 
        """
        Sets minimum and maximum points of scene bounding box for Graduated Trihedron stored in graphic view object.
        """
    def HasImmediateStructures(self) -> bool: 
        """
        Returns true if there are immediate structures to display
        """
    def HiddenObjects(self) -> Any: 
        """
        Returns map of objects hidden within this specific view (not viewer-wise).
        """
    def Identification(self) -> int: 
        """
        Returns the identification number of the view.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitXR(self) -> bool: 
        """
        Initialize XR session.
        """
    def InsertLayerAfter(self,theNewLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerBefore : int) -> None: 
        """
        Add a layer to the view.
        """
    def InsertLayerBefore(self,theLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings,theLayerAfter : int) -> None: 
        """
        Add a layer to the view.
        """
    def Invalidate(self) -> None: 
        """
        Marks BVH tree for given priority list as dirty and marks primitive set for rebuild.
        """
    def InvalidateBVHData(self,theLayerId : int) -> None: 
        """
        Marks BVH tree and the set of BVH primitives of correspondent priority list with id theLayerId as outdated.
        """
    def InvalidateZLayerBoundingBox(self,theLayerId : int) -> None: 
        """
        Returns the bounding box of all structures displayed in the Z layer.
        """
    def IsActive(self) -> bool: 
        """
        Returns the activity flag of the view.
        """
    def IsActiveXR(self) -> bool: 
        """
        Return TRUE if there is active XR session.
        """
    def IsComputed(self,theStructId : int,theComputedStruct : OCP.Graphic3d.Graphic3d_Structure) -> bool: 
        """
        Returns Standard_True in case if the structure with the given <theStructId> is in list of structures to be computed and stores computed struct to <theComputedStruct>.
        """
    def IsDefined(self) -> bool: 
        """
        Returns True if the window associated to the view is defined.
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInvalidated(self) -> bool: 
        """
        Return true if view content cache has been invalidated.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsRemoved(self) -> bool: 
        """
        Returns true if the view was removed.
        """
    def Layer(self,theLayerId : int) -> OCP.Graphic3d.Graphic3d_Layer: 
        """
        Returns layer with given ID or NULL if undefined.
        """
    def Layers(self) -> Any: 
        """
        Returns the list of layers.
        """
    def Lights(self) -> OCP.Graphic3d.Graphic3d_LightSet: 
        """
        Returns list of lights of the view.
        """
    def LocalOrigin(self) -> OCP.gp.gp_XYZ: 
        """
        Returns local camera origin currently set for rendering, might be modified during rendering.
        """
    def MinMaxValues(self,theToIncludeAuxiliary : bool) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of all structures displayed in the view. If theToIncludeAuxiliary is TRUE, then the boundary box also includes minimum and maximum limits of graphical elements forming parts of infinite and other auxiliary structures.
        """
    def NumberOfDisplayedStructures(self) -> int: 
        """
        Returns number of displayed structures in the view.
        """
    def PoseXRToWorld(self,thePoseXR : OCP.gp.gp_Trsf) -> OCP.gp.gp_Trsf: 
        """
        Convert XR pose to world space.
        """
    def PosedXRCamera(self) -> OCP.Graphic3d.Graphic3d_Camera: 
        """
        Returns transient XR camera position with tracked head orientation applied.
        """
    def ProcessXRInput(self) -> None: 
        """
        Process input.
        """
    def ReCompute(self,theStructure : OCP.Graphic3d.Graphic3d_Structure) -> None: 
        """
        Computes the new presentation of the structure displayed in this view with the type Graphic3d_TOS_COMPUTED.
        """
    def Redraw(self) -> None: 
        """
        Redraw content of the view.
        """
    def RedrawImmediate(self) -> None: 
        """
        Redraw immediate content of the view.
        """
    def ReleaseGlResources(self,theCtx : OpenGl_Context) -> None: 
        """
        Release OpenGL resources.
        """
    def ReleaseXR(self) -> None: 
        """
        Release XR session.
        """
    def Remove(self) -> None: 
        """
        Deletes and erases the view.
        """
    def RemoveZLayer(self,theLayerId : int) -> None: 
        """
        Remove a z layer with the given ID.
        """
    def RenderingParams(self) -> OCP.Graphic3d.Graphic3d_RenderingParams: 
        """
        Returns current rendering parameters and effect settings.
        """
    def Resized(self) -> None: 
        """
        Handle changing size of the rendering window.
        """
    def SetBackfacingModel(self,theModel : OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel) -> None: 
        """
        Sets backfacing model for the view.
        """
    def SetBackground(self,theBackground : OCP.Aspect.Aspect_Background) -> None: 
        """
        Sets background fill color.
        """
    def SetBackgroundImage(self,theTextureMap : OCP.Graphic3d.Graphic3d_TextureMap,theToUpdatePBREnv : bool=True) -> None: 
        """
        Sets image texture or environment cubemap as backround.
        """
    def SetBackgroundImageStyle(self,theFillStyle : OCP.Aspect.Aspect_FillMethod) -> None: 
        """
        Sets background image fill style.
        """
    def SetBaseXRCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Sets anchor camera definition.
        """
    def SetCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Sets camera used by the view.
        """
    def SetClipPlanes(self,thePlanes : OCP.Graphic3d.Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Sets list of clip planes for the view.
        """
    def SetComputedMode(self,theMode : bool) -> None: 
        """
        Switches computed HLR mode in the view
        """
    def SetFBO(self,theFbo : OCP.Standard.Standard_Transient) -> None: 
        """
        Sets framebuffer object for offscreen rendering.
        """
    def SetGradientBackground(self,theBackground : OCP.Aspect.Aspect_GradientBackground) -> None: 
        """
        Sets gradient background fill colors.
        """
    def SetImmediateModeDrawToFront(self,theDrawToFrontBuffer : bool) -> bool: 
        """
        Returns previous mode.
        """
    def SetLights(self,theLights : OCP.Graphic3d.Graphic3d_LightSet) -> None: 
        """
        Sets list of lights for the view.
        """
    def SetLocalOrigin(self,theOrigin : OCP.gp.gp_XYZ) -> None: 
        """
        Setup local camera origin currently set for rendering.
        """
    def SetPosedXRCamera(self,theCamera : OCP.Graphic3d.Graphic3d_Camera) -> None: 
        """
        Sets transient XR camera position with tracked head orientation applied.
        """
    def SetShadingModel(self,theModel : OCP.Graphic3d.Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets default Shading Model of the view. Will throw an exception on attempt to set Graphic3d_TOSM_DEFAULT.
        """
    def SetTextureEnv(self,theTextureEnv : OCP.Graphic3d.Graphic3d_TextureEnv) -> None: 
        """
        Sets environment texture for the view.
        """
    def SetUnitFactor(self,theFactor : float) -> None: 
        """
        Set unit scale factor.
        """
    def SetVisualizationType(self,theType : OCP.Graphic3d.Graphic3d_TypeOfVisualization) -> None: 
        """
        Sets visualization type of the view.
        """
    def SetWindow(self,theWindow : OCP.Aspect.Aspect_Window,theContext : capsule) -> None: 
        """
        Creates and maps rendering window to the view.
        """
    def SetXRSession(self,theSession : OCP.Aspect.Aspect_XRSession) -> None: 
        """
        Set XR session.
        """
    def SetZLayerSettings(self,theLayerId : int,theSettings : OCP.Graphic3d.Graphic3d_ZLayerSettings) -> None: 
        """
        Sets the settings for a single Z layer of specified view.
        """
    def SetupXRPosedCamera(self) -> None: 
        """
        Compute PosedXRCamera() based on current XR head pose and make it active.
        """
    def ShadingModel(self) -> OCP.Graphic3d.Graphic3d_TypeOfShadingModel: 
        """
        Returns default Shading Model of the view; Graphic3d_TOSM_FRAGMENT by default.
        """
    def SpecIBLMapLevels(self) -> int: 
        """
        Returns number of mipmap levels used in specular IBL map. 0 if PBR environment is not created.
        """
    @overload
    def StatisticInformation(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns string with statistic performance info.

        Fills in the dictionary with statistic performance info.
        """
    @overload
    def StatisticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString) -> None: ...
    def StructureManager(self) -> OCP.Graphic3d.Graphic3d_StructureManager: 
        """
        Returns the structure manager handle which manage structures associated with this view.
        """
    def SynchronizeXRBaseToPosedCamera(self) -> None: 
        """
        Recomputes PosedXRCamera() based on BaseXRCamera() and head orientation.
        """
    def SynchronizeXRPosedToBaseCamera(self) -> None: 
        """
        Checks if PosedXRCamera() has been modified since SetupXRPosedCamera() and copies these modifications to BaseXRCamera().
        """
    def TextureEnv(self) -> OCP.Graphic3d.Graphic3d_TextureEnv: 
        """
        Returns environment texture set for the view.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TurnViewXRCamera(self,theTrsfTurn : OCP.gp.gp_Trsf) -> None: 
        """
        Turn XR camera direction using current (head) eye position as anchor.
        """
    def UnitFactor(self) -> float: 
        """
        Return unit scale factor defined as scale factor for m (meters); 1.0 by default. Normally, view definition is unitless, however some operations like VR input requires proper units mapping.
        """
    def UnsetXRPosedCamera(self) -> None: 
        """
        Set current camera back to BaseXRCamera() and copy temporary modifications of PosedXRCamera(). Calls SynchronizeXRPosedToBaseCamera() beforehand.
        """
    def Update(self,theLayerId : int=-1) -> None: 
        """
        Invalidates bounding box of specified ZLayerId.
        """
    def VisualizationType(self) -> OCP.Graphic3d.Graphic3d_TypeOfVisualization: 
        """
        Returns visualization type of the view.
        """
    def Window(self) -> OCP.Aspect.Aspect_Window: 
        """
        Returns window associated with the view.
        """
    def XRSession(self) -> OCP.Aspect.Aspect_XRSession: 
        """
        Return XR session.
        """
    def ZLayerMax(self) -> int: 
        """
        Returns the maximum Z layer ID. First layer ID is Graphic3d_ZLayerId_Default, last ID is ZLayerMax().
        """
    def __init__(self,theMgr : OCP.Graphic3d.Graphic3d_StructureManager,theDriver : OpenGl_GraphicDriver,theCaps : OpenGl_Caps,theCounter : OpenGl_StateCounter) -> None: ...
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
class OpenGl_Window(OCP.Standard.Standard_Transient):
    """
    This class represents low-level wrapper over window with GL context. The window itself should be provided to constructor.This class represents low-level wrapper over window with GL context. The window itself should be provided to constructor.This class represents low-level wrapper over window with GL context. The window itself should be provided to constructor.
    """
    def Activate(self) -> bool: 
        """
        Makes GL context for this window active in current thread
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
    def GetGlContext(self) -> OpenGl_Context: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Height(self) -> int: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self) -> None: 
        """
        Activates GL context and setup viewport.
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
    def PlatformWindow(self) -> OCP.Aspect.Aspect_Window: 
        """
        None
        """
    def Resize(self) -> None: 
        """
        Resizes the window.
        """
    def SetSwapInterval(self,theToForceNoSync : bool) -> None: 
        """
        Sets swap interval for this window according to the context's settings.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Width(self) -> int: 
        """
        None
        """
    def __init__(self,theDriver : OpenGl_GraphicDriver,thePlatformWindow : OCP.Aspect.Aspect_Window,theGContext : capsule,theCaps : OpenGl_Caps,theShareCtx : OpenGl_Context) -> None: ...
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
class OpenGl_Workspace(OCP.Standard.Standard_Transient):
    """
    Rendering workspace. Provides methods to render primitives and maintain GL state.Rendering workspace. Provides methods to render primitives and maintain GL state.Rendering workspace. Provides methods to render primitives and maintain GL state.
    """
    def Activate(self) -> bool: 
        """
        Activate rendering context.
        """
    def ApplyAspects(self,theToBindTextures : bool=True) -> OpenGl_Aspects: 
        """
        Apply aspects.
        """
    def Aspects(self) -> OpenGl_Aspects: 
        """
        Currently set aspects (can differ from applied).
        """
    def BufferDump(self,theFbo : OpenGl_FrameBuffer,theImage : OCP.Image.Image_PixMap,theBufferType : OCP.Graphic3d.Graphic3d_BufferType) -> bool: 
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
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Return edge color taking into account highlight flag.
        """
    def EnvironmentTexture(self) -> OpenGl_TextureSet: 
        """
        Returns environment texture.
        """
    def FBOCreate(self,theWidth : int,theHeight : int) -> OpenGl_FrameBuffer: 
        """
        None
        """
    def FBORelease(self,theFbo : OpenGl_FrameBuffer) -> Any: 
        """
        None
        """
    def FrontCulling(self) -> OpenGl_Aspects: 
        """
        Returns face aspect for front face culling mode.
        """
    def GetGlContext(self) -> OpenGl_Context: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Height(self) -> int: 
        """
        None
        """
    def HighlightStyle(self) -> OCP.Graphic3d.Graphic3d_PresentationAttributes: 
        """
        Return highlight style.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Return Interior color taking into account highlight flag.
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
    def ModelMatrix(self) -> OpenGl_Matrix: 
        """
        Returns applied model structure matrix.
        """
    def NbSkippedTransparentElements(self) -> int: 
        """
        Return the number of skipped transparent elements within active OpenGl_RenderFilter_OpaqueOnly filter.
        """
    def NoneCulling(self) -> OpenGl_Aspects: 
        """
        Returns face aspect for none culling mode.
        """
    def RenderFilter(self) -> int: 
        """
        Get rendering filter.
        """
    def ResetAppliedAspect(self) -> None: 
        """
        Clear the applied aspect state to default values.
        """
    def ResetSkippedCounter(self) -> None: 
        """
        Reset skipped transparent elements counter.
        """
    def SetAllowFaceCulling(self,theToAllow : bool) -> bool: 
        """
        Allow or disallow face culling. This call does NOT affect current state of back face culling; ApplyAspectFace() should be called to update state.
        """
    def SetAspects(self,theAspect : OpenGl_Aspects) -> OpenGl_Aspects: 
        """
        Assign new aspects (will be applied within ApplyAspects()).
        """
    def SetDefaultPolygonOffset(self,theOffset : OCP.Graphic3d.Graphic3d_PolygonOffset) -> OCP.Graphic3d.Graphic3d_PolygonOffset: 
        """
        Configure default polygon offset parameters. Return previous settings.
        """
    def SetEnvironmentTexture(self,theTexture : OpenGl_TextureSet) -> None: 
        """
        Sets a new environment texture.
        """
    def SetHighlightStyle(self,theStyle : OCP.Graphic3d.Graphic3d_PresentationAttributes) -> None: 
        """
        Set highlight style.
        """
    def SetRenderFilter(self,theFilter : int) -> None: 
        """
        Set filter for restricting rendering of particular elements.
        """
    def SetUseZBuffer(self,theToUse : bool) -> bool: 
        """
        Setup Z-buffer usage flag (without affecting GL state!). Returns previously set flag.
        """
    def ShouldRender(self,theElement : OpenGl_Element) -> bool: 
        """
        Checks whether the element can be rendered or not.
        """
    def TextColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Return text color taking into account highlight flag.
        """
    def TextSubtitleColor(self) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Return text Subtitle color taking into account highlight flag.
        """
    def TextureSet(self) -> OpenGl_TextureSet: 
        """
        Return TextureSet from set Aspects or Environment texture.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToAllowFaceCulling(self) -> bool: 
        """
        Return true if active group might activate face culling (e.g. primitives are closed).
        """
    def ToHighlight(self) -> bool: 
        """
        Return true if following structures should apply highlight color.
        """
    def View(self) -> OpenGl_View: 
        """
        None
        """
    def ViewMatrix(self) -> OpenGl_Matrix: 
        """
        Returns applied view matrix.
        """
    def Width(self) -> int: 
        """
        None
        """
    def __init__(self,theView : OpenGl_View,theWindow : OpenGl_Window) -> None: ...
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
    @property
    def UseDepthWrite(self) -> bool:
        """
        Returns true if depth writing is enabled.

        :type: bool
        """
    @UseDepthWrite.setter
    def UseDepthWrite(self, arg1: bool) -> None:
        """
        Returns true if depth writing is enabled.
        """
    @property
    def UseZBuffer(self) -> bool:
        """
        Returns true if usage of Z buffer is enabled.

        :type: bool
        """
    @UseZBuffer.setter
    def UseZBuffer(self, arg1: bool) -> None:
        """
        Returns true if usage of Z buffer is enabled.
        """
    pass
class OpenGl_WorldViewState(OpenGl_StateInterface):
    """
    Defines state of OCCT world-view transformation.
    """
    def Index(self) -> int: 
        """
        Returns current state index.
        """
    def Set(self,theWorldViewMatrix : OCP.Graphic3d.Graphic3d_Mat4) -> None: 
        """
        Sets new world-view matrix.
        """
    def Update(self) -> None: 
        """
        Increment current state.
        """
    def WorldViewMatrix(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns current world-view matrix.
        """
    def WorldViewMatrixInverse(self) -> OCP.Graphic3d.Graphic3d_Mat4: 
        """
        Returns inverse of current world-view matrix.
        """
    def __init__(self) -> None: ...
    pass
OpenGL_OIT_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGL_OIT_STATE: 7>
OpenGl_CLIP_PLANES_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_CLIP_PLANES_STATE: 1>
OpenGl_FeatureInCore: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureInCore: 2>
OpenGl_FeatureInExtensions: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureInExtensions: 1>
OpenGl_FeatureNotAvailable: OCP.OpenGl.OpenGl_FeatureFlag # value = <OpenGl_FeatureFlag.OpenGl_FeatureNotAvailable: 0>
OpenGl_LF_All: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_All: 0>
OpenGl_LF_Bottom: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_Bottom: 2>
OpenGl_LF_RayTracable: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_RayTracable: 3>
OpenGl_LF_Upper: OCP.OpenGl.OpenGl_LayerFilter # value = <OpenGl_LayerFilter.OpenGl_LF_Upper: 1>
OpenGl_LIGHT_SOURCES_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_LIGHT_SOURCES_STATE: 0>
OpenGl_MATERIAL_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_MATERIAL_STATE: 5>
OpenGl_MODEL_WORLD_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_MODEL_WORLD_STATE: 2>
OpenGl_MaterialFlag_Back: OCP.OpenGl.OpenGl_MaterialFlag # value = <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Back: 1>
OpenGl_MaterialFlag_Front: OCP.OpenGl.OpenGl_MaterialFlag # value = <OpenGl_MaterialFlag.OpenGl_MaterialFlag_Front: 0>
OpenGl_OCCT_ALPHA_CUTOFF: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_ALPHA_CUTOFF: 25>
OpenGl_OCCT_COLOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COLOR: 26>
OpenGl_OCCT_COMMON_BACK_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COMMON_BACK_MATERIAL: 24>
OpenGl_OCCT_COMMON_FRONT_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_COMMON_FRONT_MATERIAL: 23>
OpenGl_OCCT_DISTINGUISH_MODE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_DISTINGUISH_MODE: 20>
OpenGl_OCCT_LINE_FEATHER: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_FEATHER: 33>
OpenGl_OCCT_LINE_STIPPLE_FACTOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_FACTOR: 35>
OpenGl_OCCT_LINE_STIPPLE_PATTERN: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_STIPPLE_PATTERN: 34>
OpenGl_OCCT_LINE_WIDTH: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_LINE_WIDTH: 32>
OpenGl_OCCT_NB_SPEC_IBL_LEVELS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_NB_SPEC_IBL_LEVELS: 40>
OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: 41>
OpenGl_OCCT_OIT_DEPTH_FACTOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_OIT_DEPTH_FACTOR: 28>
OpenGl_OCCT_OIT_OUTPUT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_OIT_OUTPUT: 27>
OpenGl_OCCT_ORTHO_SCALE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_ORTHO_SCALE: 38>
OpenGl_OCCT_PBR_BACK_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_PBR_BACK_MATERIAL: 22>
OpenGl_OCCT_PBR_FRONT_MATERIAL: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_PBR_FRONT_MATERIAL: 21>
OpenGl_OCCT_POINT_SIZE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_POINT_SIZE: 30>
OpenGl_OCCT_QUAD_MODE_STATE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_QUAD_MODE_STATE: 37>
OpenGl_OCCT_SILHOUETTE_THICKNESS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_SILHOUETTE_THICKNESS: 39>
OpenGl_OCCT_TEXTURE_ENABLE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_ENABLE: 19>
OpenGl_OCCT_TEXTURE_TRSF2D: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_TRSF2D: 29>
OpenGl_OCCT_VIEWPORT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_VIEWPORT: 31>
OpenGl_OCCT_WIREFRAME_COLOR: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCCT_WIREFRAME_COLOR: 36>
OpenGl_OCC_CLIP_PLANE_CHAINS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_CHAINS: 13>
OpenGl_OCC_CLIP_PLANE_COUNT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_COUNT: 14>
OpenGl_OCC_CLIP_PLANE_EQUATIONS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_EQUATIONS: 12>
OpenGl_OCC_LIGHT_AMBIENT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_AMBIENT: 18>
OpenGl_OCC_LIGHT_SOURCE_COUNT: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_COUNT: 15>
OpenGl_OCC_LIGHT_SOURCE_PARAMS: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_PARAMS: 17>
OpenGl_OCC_LIGHT_SOURCE_TYPES: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_LIGHT_SOURCE_TYPES: 16>
OpenGl_OCC_MODEL_WORLD_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX: 0>
OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: 3>
OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: 9>
OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: 6>
OpenGl_OCC_PROJECTION_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX: 2>
OpenGl_OCC_PROJECTION_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE: 5>
OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: 11>
OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: 8>
OpenGl_OCC_WORLD_VIEW_MATRIX: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX: 1>
OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: 4>
OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: 10>
OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: OCP.OpenGl.OpenGl_StateVariable # value = <OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: 7>
OpenGl_PO_AlphaTest: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_AlphaTest: 1024>
OpenGl_PO_ClipChains: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipChains: 256>
OpenGl_PO_ClipPlanes1: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes1: 64>
OpenGl_PO_ClipPlanes2: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanes2: 128>
OpenGl_PO_ClipPlanesN: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_ClipPlanesN: 192>
OpenGl_PO_HasTextures: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>
OpenGl_PO_IsPoint: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>
OpenGl_PO_MeshEdges: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>
OpenGl_PO_NB: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_NB: 4096>
OpenGl_PO_NeedsGeomShader: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_MeshEdges: 512>
OpenGl_PO_PointSimple: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSimple: 8>
OpenGl_PO_PointSprite: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSprite: 16>
OpenGl_PO_PointSpriteA: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_PointSpriteA: 24>
OpenGl_PO_StippleLine: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_StippleLine: 32>
OpenGl_PO_TextureEnv: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureEnv: 4>
OpenGl_PO_TextureNormal: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureNormal: 6>
OpenGl_PO_TextureRGB: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_TextureRGB: 2>
OpenGl_PO_VertColor: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_VertColor: 1>
OpenGl_PO_WriteOit: OCP.OpenGl.OpenGl_ProgramOptions # value = <OpenGl_ProgramOptions.OpenGl_PO_WriteOit: 2048>
OpenGl_PROJECTION_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_PROJECTION_STATE: 4>
OpenGl_RenderFilter_Empty: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_Empty: 0>
OpenGl_RenderFilter_FillModeOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_FillModeOnly: 8>
OpenGl_RenderFilter_NonRaytraceableOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_NonRaytraceableOnly: 4>
OpenGl_RenderFilter_OpaqueOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_OpaqueOnly: 1>
OpenGl_RenderFilter_TransparentOnly: OCP.OpenGl.OpenGl_RenderFilter # value = <OpenGl_RenderFilter.OpenGl_RenderFilter_TransparentOnly: 2>
OpenGl_SURF_DETAIL_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_SURF_DETAIL_STATE: 6>
OpenGl_ShaderProgramDumpLevel_Full: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Full: 2>
OpenGl_ShaderProgramDumpLevel_Off: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Off: 0>
OpenGl_ShaderProgramDumpLevel_Short: OCP.OpenGl.OpenGl_ShaderProgramDumpLevel # value = <OpenGl_ShaderProgramDumpLevel.OpenGl_ShaderProgramDumpLevel_Short: 1>
OpenGl_UniformStateType_NB: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_UniformStateType_NB: 8>
OpenGl_WORLD_VIEW_STATE: OCP.OpenGl.OpenGl_UniformStateType # value = <OpenGl_UniformStateType.OpenGl_WORLD_VIEW_STATE: 3>
