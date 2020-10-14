import OCP.Graphic3d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TCollection
import OCP.Font
import OCP.NCollection
import OCP.gp
import OCP.TColStd
import OCP.Select3D
import OCP.SelectMgr
import OCP.OSD
import OCP.Bnd
import OCP.Quantity
import OCP.Aspect
import OCP.Image
import OCP.Standard
import OCP.Geom
__all__  = [
"Graphic3d_AlphaMode",
"Graphic3d_Array1OfAttribute",
"Graphic3d_ArrayOfIndexedMapOfStructure",
"Graphic3d_ArrayOfPrimitives",
"Graphic3d_ArrayOfPolygons",
"Graphic3d_ArrayOfPolylines",
"Graphic3d_ArrayOfPoints",
"Graphic3d_ArrayOfQuadrangleStrips",
"Graphic3d_ArrayOfQuadrangles",
"Graphic3d_ArrayOfSegments",
"Graphic3d_ArrayOfTriangleFans",
"Graphic3d_ArrayOfTriangleStrips",
"Graphic3d_ArrayOfTriangles",
"Graphic3d_Aspects",
"Graphic3d_AspectLine3d",
"Graphic3d_AspectMarker3d",
"Graphic3d_AspectText3d",
"Graphic3d_AspectFillArea3d",
"Graphic3d_Buffer",
"Graphic3d_Attribute",
"Graphic3d_AxisAspect",
"Graphic3d_BSDF",
"Graphic3d_BndBox3d",
"Graphic3d_BndBox4d",
"Graphic3d_BndBox4f",
"Graphic3d_BoundBuffer",
"Graphic3d_AttribBuffer",
"Graphic3d_BufferRange",
"Graphic3d_BufferType",
"Graphic3d_CLight",
"Graphic3d_CStructure",
"Graphic3d_CTexture",
"Graphic3d_DataStructureManager",
"Graphic3d_Camera",
"Graphic3d_CameraLerp",
"Graphic3d_CameraTile",
"Graphic3d_CappingFlags",
"Graphic3d_ClipPlane",
"Graphic3d_ClipState",
"Graphic3d_TextureRoot",
"Graphic3d_CubeMapOrder",
"Graphic3d_TextureMap",
"Graphic3d_CubeMap",
"Graphic3d_CubeMapSide",
"Graphic3d_CullingTool",
"Graphic3d_CView",
"Graphic3d_DiagnosticInfo",
"Graphic3d_FrameStats",
"Graphic3d_FrameStatsCounter",
"Graphic3d_FrameStatsData",
"Graphic3d_FrameStatsDataTmp",
"Graphic3d_FrameStatsTimer",
"Graphic3d_Fresnel",
"Graphic3d_FresnelModel",
"Graphic3d_GraduatedTrihedron",
"Graphic3d_GraphicDriver",
"Graphic3d_Group",
"Graphic3d_GroupAspect",
"Graphic3d_GroupDefinitionError",
"Graphic3d_HatchStyle",
"Graphic3d_HorizontalTextAlignment",
"Graphic3d_IndexBuffer",
"Graphic3d_IndexedMapOfStructure",
"Graphic3d_Layer",
"Graphic3d_LevelOfTextureAnisotropy",
"Graphic3d_LightSet",
"Graphic3d_MapOfZLayerSettings",
"Graphic3d_MarkerImage",
"Graphic3d_Mat4",
"Graphic3d_Mat4d",
"Graphic3d_MaterialAspect",
"Graphic3d_MaterialDefinitionError",
"Graphic3d_Texture2D",
"Graphic3d_TextureSet",
"Graphic3d_MutableIndexBuffer",
"Graphic3d_NameOfMaterial",
"Graphic3d_NameOfTexture1D",
"Graphic3d_NameOfTexture2D",
"Graphic3d_NameOfTextureEnv",
"Graphic3d_NameOfTexturePlane",
"Graphic3d_PolygonOffset",
"Graphic3d_PresentationAttributes",
"Graphic3d_PriorityDefinitionError",
"Graphic3d_RenderTransparentMethod",
"Graphic3d_RenderingMode",
"Graphic3d_RenderingParams",
"Graphic3d_SequenceOfGroup",
"Graphic3d_SequenceOfHClipPlane",
"Graphic3d_SequenceOfStructure",
"Graphic3d_ShaderAttribute",
"Graphic3d_ShaderAttributeList",
"Graphic3d_ShaderObject",
"Graphic3d_ShaderObjectList",
"Graphic3d_ShaderProgram",
"Graphic3d_ShaderVariable",
"Graphic3d_ShaderVariableList",
"Graphic3d_StereoMode",
"Graphic3d_Structure",
"Graphic3d_StructureDefinitionError",
"Graphic3d_StructureManager",
"Graphic3d_Text",
"Graphic3d_TextPath",
"Graphic3d_Texture1D",
"Graphic3d_Texture1Dmanual",
"Graphic3d_Texture1Dsegment",
"Graphic3d_MediaTexture",
"Graphic3d_Texture2Dmanual",
"Graphic3d_Texture2Dplane",
"Graphic3d_TextureEnv",
"Graphic3d_CubeMapPacked",
"Graphic3d_TextureParams",
"Graphic3d_CubeMapSeparate",
"Graphic3d_MediaTextureSet",
"Graphic3d_TextureUnit",
"Graphic3d_ToneMappingMethod",
"Graphic3d_TransModeFlags",
"Graphic3d_TransformError",
"Graphic3d_TransformPers",
"Graphic3d_TypeOfAnswer",
"Graphic3d_TypeOfAttribute",
"Graphic3d_TypeOfBackfacingModel",
"Graphic3d_TypeOfBackground",
"Graphic3d_TypeOfComposition",
"Graphic3d_TypeOfConnection",
"Graphic3d_TypeOfData",
"Graphic3d_TypeOfLightSource",
"Graphic3d_TypeOfLimit",
"Graphic3d_TypeOfMaterial",
"Graphic3d_TypeOfPrimitiveArray",
"Graphic3d_TypeOfReflection",
"Graphic3d_TypeOfShaderObject",
"Graphic3d_TypeOfShadingModel",
"Graphic3d_TypeOfStructure",
"Graphic3d_TypeOfTexture",
"Graphic3d_TypeOfTextureFilter",
"Graphic3d_TypeOfTextureMode",
"Graphic3d_TypeOfVisualization",
"Graphic3d_ValueInterface",
"Graphic3d_UniformInt",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec2",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec2i",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec3",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec3i",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec4",
"Graphic3d_UniformValueTypeID_Graphic3d_Vec4i",
"Graphic3d_UniformValueTypeID_Standard_Integer",
"Graphic3d_UniformValueTypeID_Standard_ShortReal",
"Graphic3d_UniformVec2",
"Graphic3d_UniformVec2i",
"Graphic3d_UniformVec3",
"Graphic3d_UniformVec3i",
"Graphic3d_UniformVec4",
"Graphic3d_UniformVec4i",
"Graphic3d_ValidatedCubeMapOrder",
"Graphic3d_UniformFloat",
"Graphic3d_Vec2",
"Graphic3d_Vec2b",
"Graphic3d_Vec2d",
"Graphic3d_Vec2i",
"Graphic3d_Vec2ub",
"Graphic3d_Vec3",
"Graphic3d_Vec3b",
"Graphic3d_Vec3i",
"Graphic3d_Vec3ub",
"Graphic3d_Vec4",
"Graphic3d_Vec4b",
"Graphic3d_Vec4d",
"Graphic3d_Vec4i",
"Graphic3d_Vec4ub",
"Graphic3d_Vertex",
"Graphic3d_VerticalTextAlignment",
"Graphic3d_ViewAffinity",
"Graphic3d_WorldViewProjState",
"Graphic3d_ZLayerSetting",
"Graphic3d_ZLayerSettings",
"Graphic3d_ASPECT_FILL_AREA",
"Graphic3d_ASPECT_LINE",
"Graphic3d_ASPECT_MARKER",
"Graphic3d_ASPECT_TEXT",
"Graphic3d_AlphaMode_Blend",
"Graphic3d_AlphaMode_BlendAuto",
"Graphic3d_AlphaMode_Mask",
"Graphic3d_AlphaMode_Opaque",
"Graphic3d_ArrayFlags_AttribsDeinterleaved",
"Graphic3d_ArrayFlags_AttribsMutable",
"Graphic3d_ArrayFlags_BoundColor",
"Graphic3d_ArrayFlags_IndexesMutable",
"Graphic3d_ArrayFlags_None",
"Graphic3d_ArrayFlags_VertexColor",
"Graphic3d_ArrayFlags_VertexNormal",
"Graphic3d_ArrayFlags_VertexTexel",
"Graphic3d_BT_Depth",
"Graphic3d_BT_RGB",
"Graphic3d_BT_RGBA",
"Graphic3d_BT_RGB_RayTraceHdrLeft",
"Graphic3d_CMS_NEG_X",
"Graphic3d_CMS_NEG_Y",
"Graphic3d_CMS_NEG_Z",
"Graphic3d_CMS_POS_X",
"Graphic3d_CMS_POS_Y",
"Graphic3d_CMS_POS_Z",
"Graphic3d_CappingFlags_None",
"Graphic3d_CappingFlags_ObjectAspect",
"Graphic3d_CappingFlags_ObjectMaterial",
"Graphic3d_CappingFlags_ObjectShader",
"Graphic3d_CappingFlags_ObjectTexture",
"Graphic3d_ClipState_In",
"Graphic3d_ClipState_On",
"Graphic3d_ClipState_Out",
"Graphic3d_DiagnosticInfo_Basic",
"Graphic3d_DiagnosticInfo_Complete",
"Graphic3d_DiagnosticInfo_Device",
"Graphic3d_DiagnosticInfo_Extensions",
"Graphic3d_DiagnosticInfo_FrameBuffer",
"Graphic3d_DiagnosticInfo_Limits",
"Graphic3d_DiagnosticInfo_Memory",
"Graphic3d_DiagnosticInfo_NativePlatform",
"Graphic3d_DiagnosticInfo_Short",
"Graphic3d_FM_CONDUCTOR",
"Graphic3d_FM_CONSTANT",
"Graphic3d_FM_DIELECTRIC",
"Graphic3d_FM_SCHLICK",
"Graphic3d_FrameStatsCounter_EstimatedBytesFbos",
"Graphic3d_FrameStatsCounter_EstimatedBytesGeom",
"Graphic3d_FrameStatsCounter_EstimatedBytesTextures",
"Graphic3d_FrameStatsCounter_NB",
"Graphic3d_FrameStatsCounter_NbElemsFillNotCulled",
"Graphic3d_FrameStatsCounter_NbElemsLineNotCulled",
"Graphic3d_FrameStatsCounter_NbElemsNotCulled",
"Graphic3d_FrameStatsCounter_NbElemsPointNotCulled",
"Graphic3d_FrameStatsCounter_NbElemsTextNotCulled",
"Graphic3d_FrameStatsCounter_NbGroupsNotCulled",
"Graphic3d_FrameStatsCounter_NbLayers",
"Graphic3d_FrameStatsCounter_NbLayersNotCulled",
"Graphic3d_FrameStatsCounter_NbPointsNotCulled",
"Graphic3d_FrameStatsCounter_NbStructs",
"Graphic3d_FrameStatsCounter_NbStructsNotCulled",
"Graphic3d_FrameStatsCounter_NbTrianglesNotCulled",
"Graphic3d_FrameStatsTimer_CpuCulling",
"Graphic3d_FrameStatsTimer_CpuDynamics",
"Graphic3d_FrameStatsTimer_CpuFrame",
"Graphic3d_FrameStatsTimer_CpuPicking",
"Graphic3d_FrameStatsTimer_ElapsedFrame",
"Graphic3d_FrameStatsTimer_NB",
"Graphic3d_HTA_CENTER",
"Graphic3d_HTA_LEFT",
"Graphic3d_HTA_RIGHT",
"Graphic3d_LOTA_FAST",
"Graphic3d_LOTA_MIDDLE",
"Graphic3d_LOTA_OFF",
"Graphic3d_LOTA_QUALITY",
"Graphic3d_MATERIAL_ASPECT",
"Graphic3d_MATERIAL_PHYSIC",
"Graphic3d_NOM_ALUMINIUM",
"Graphic3d_NOM_BRASS",
"Graphic3d_NOM_BRONZE",
"Graphic3d_NOM_CHARCOAL",
"Graphic3d_NOM_CHROME",
"Graphic3d_NOM_COPPER",
"Graphic3d_NOM_DEFAULT",
"Graphic3d_NOM_DIAMOND",
"Graphic3d_NOM_GLASS",
"Graphic3d_NOM_GOLD",
"Graphic3d_NOM_JADE",
"Graphic3d_NOM_METALIZED",
"Graphic3d_NOM_NEON_GNC",
"Graphic3d_NOM_NEON_PHC",
"Graphic3d_NOM_OBSIDIAN",
"Graphic3d_NOM_PEWTER",
"Graphic3d_NOM_PLASTER",
"Graphic3d_NOM_PLASTIC",
"Graphic3d_NOM_SATIN",
"Graphic3d_NOM_SHINY_PLASTIC",
"Graphic3d_NOM_SILVER",
"Graphic3d_NOM_STEEL",
"Graphic3d_NOM_STONE",
"Graphic3d_NOM_TRANSPARENT",
"Graphic3d_NOM_UserDefined",
"Graphic3d_NOM_WATER",
"Graphic3d_NOTP_UNKNOWN",
"Graphic3d_NOTP_XY",
"Graphic3d_NOTP_YZ",
"Graphic3d_NOTP_ZX",
"Graphic3d_NOT_1D_ELEVATION",
"Graphic3d_NOT_1D_UNKNOWN",
"Graphic3d_NOT_2D_ALIENSKIN",
"Graphic3d_NOT_2D_ALUMINUM",
"Graphic3d_NOT_2D_BLUEWHITE_PAPER",
"Graphic3d_NOT_2D_BLUE_ROCK",
"Graphic3d_NOT_2D_BRUSHED",
"Graphic3d_NOT_2D_BUBBLES",
"Graphic3d_NOT_2D_BUMP",
"Graphic3d_NOT_2D_CAST",
"Graphic3d_NOT_2D_CHESS",
"Graphic3d_NOT_2D_CHIPBD",
"Graphic3d_NOT_2D_CLOUDS",
"Graphic3d_NOT_2D_FLESH",
"Graphic3d_NOT_2D_FLOOR",
"Graphic3d_NOT_2D_GALVNISD",
"Graphic3d_NOT_2D_GRASS",
"Graphic3d_NOT_2D_KNURL",
"Graphic3d_NOT_2D_MAPLE",
"Graphic3d_NOT_2D_MARBLE",
"Graphic3d_NOT_2D_MATRA",
"Graphic3d_NOT_2D_MOTTLED",
"Graphic3d_NOT_2D_RAIN",
"Graphic3d_NOT_2D_ROCK",
"Graphic3d_NOT_2D_UNKNOWN",
"Graphic3d_NOT_ENV_CLOUDS",
"Graphic3d_NOT_ENV_CV",
"Graphic3d_NOT_ENV_LINES",
"Graphic3d_NOT_ENV_MEDIT",
"Graphic3d_NOT_ENV_PEARL",
"Graphic3d_NOT_ENV_ROAD",
"Graphic3d_NOT_ENV_SKY1",
"Graphic3d_NOT_ENV_SKY2",
"Graphic3d_NOT_ENV_UNKNOWN",
"Graphic3d_RM_RASTERIZATION",
"Graphic3d_RM_RAYTRACING",
"Graphic3d_RTM_BLEND_OIT",
"Graphic3d_RTM_BLEND_UNORDERED",
"Graphic3d_StereoMode_Anaglyph",
"Graphic3d_StereoMode_ChessBoard",
"Graphic3d_StereoMode_ColumnInterlaced",
"Graphic3d_StereoMode_NB",
"Graphic3d_StereoMode_OverUnder",
"Graphic3d_StereoMode_QuadBuffer",
"Graphic3d_StereoMode_RowInterlaced",
"Graphic3d_StereoMode_SideBySide",
"Graphic3d_StereoMode_SoftPageFlip",
"Graphic3d_TMF_2d",
"Graphic3d_TMF_None",
"Graphic3d_TMF_RotatePers",
"Graphic3d_TMF_TriedronPers",
"Graphic3d_TMF_ZoomPers",
"Graphic3d_TMF_ZoomRotatePers",
"Graphic3d_TOA_COLOR",
"Graphic3d_TOA_COMPUTE",
"Graphic3d_TOA_CUSTOM",
"Graphic3d_TOA_NO",
"Graphic3d_TOA_NORM",
"Graphic3d_TOA_POS",
"Graphic3d_TOA_UV",
"Graphic3d_TOA_YES",
"Graphic3d_TOBM_AUTOMATIC",
"Graphic3d_TOBM_DISABLE",
"Graphic3d_TOBM_FORCE",
"Graphic3d_TOB_CUBEMAP",
"Graphic3d_TOB_GRADIENT",
"Graphic3d_TOB_NONE",
"Graphic3d_TOB_TEXTURE",
"Graphic3d_TOC_ANCESTOR",
"Graphic3d_TOC_DESCENDANT",
"Graphic3d_TOC_POSTCONCATENATE",
"Graphic3d_TOC_REPLACE",
"Graphic3d_TOD_FLOAT",
"Graphic3d_TOD_UINT",
"Graphic3d_TOD_USHORT",
"Graphic3d_TOD_VEC2",
"Graphic3d_TOD_VEC3",
"Graphic3d_TOD_VEC4",
"Graphic3d_TOD_VEC4UB",
"Graphic3d_TOLS_AMBIENT",
"Graphic3d_TOLS_DIRECTIONAL",
"Graphic3d_TOLS_POSITIONAL",
"Graphic3d_TOLS_SPOT",
"Graphic3d_TOPA_LINES_ADJACENCY",
"Graphic3d_TOPA_LINE_STRIP_ADJACENCY",
"Graphic3d_TOPA_POINTS",
"Graphic3d_TOPA_POLYGONS",
"Graphic3d_TOPA_POLYLINES",
"Graphic3d_TOPA_QUADRANGLES",
"Graphic3d_TOPA_QUADRANGLESTRIPS",
"Graphic3d_TOPA_SEGMENTS",
"Graphic3d_TOPA_TRIANGLEFANS",
"Graphic3d_TOPA_TRIANGLES",
"Graphic3d_TOPA_TRIANGLESTRIPS",
"Graphic3d_TOPA_TRIANGLES_ADJACENCY",
"Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY",
"Graphic3d_TOPA_UNDEFINED",
"Graphic3d_TOR_AMBIENT",
"Graphic3d_TOR_DIFFUSE",
"Graphic3d_TOR_EMISSION",
"Graphic3d_TOR_SPECULAR",
"Graphic3d_TOSM_DEFAULT",
"Graphic3d_TOSM_FACET",
"Graphic3d_TOSM_FRAGMENT",
"Graphic3d_TOSM_NONE",
"Graphic3d_TOSM_UNLIT",
"Graphic3d_TOSM_VERTEX",
"Graphic3d_TOS_ALL",
"Graphic3d_TOS_COMPUTE",
"Graphic3d_TOS_COMPUTED",
"Graphic3d_TOS_FRAGMENT",
"Graphic3d_TOS_GEOMETRY",
"Graphic3d_TOS_SHADING",
"Graphic3d_TOS_TESS_CONTROL",
"Graphic3d_TOS_TESS_EVALUATION",
"Graphic3d_TOS_VERTEX",
"Graphic3d_TOS_WIREFRAME",
"Graphic3d_TOTF_BILINEAR",
"Graphic3d_TOTF_NEAREST",
"Graphic3d_TOTF_TRILINEAR",
"Graphic3d_TOTM_EYE",
"Graphic3d_TOTM_MANUAL",
"Graphic3d_TOTM_OBJECT",
"Graphic3d_TOTM_SPHERE",
"Graphic3d_TOTM_SPRITE",
"Graphic3d_TOT_1D",
"Graphic3d_TOT_2D",
"Graphic3d_TOT_2D_MIPMAP",
"Graphic3d_TOT_CUBEMAP",
"Graphic3d_TOV_SHADING",
"Graphic3d_TOV_WIREFRAME",
"Graphic3d_TP_DOWN",
"Graphic3d_TP_LEFT",
"Graphic3d_TP_RIGHT",
"Graphic3d_TP_UP",
"Graphic3d_TextureUnit_0",
"Graphic3d_TextureUnit_1",
"Graphic3d_TextureUnit_10",
"Graphic3d_TextureUnit_11",
"Graphic3d_TextureUnit_12",
"Graphic3d_TextureUnit_13",
"Graphic3d_TextureUnit_14",
"Graphic3d_TextureUnit_15",
"Graphic3d_TextureUnit_2",
"Graphic3d_TextureUnit_3",
"Graphic3d_TextureUnit_4",
"Graphic3d_TextureUnit_5",
"Graphic3d_TextureUnit_6",
"Graphic3d_TextureUnit_7",
"Graphic3d_TextureUnit_8",
"Graphic3d_TextureUnit_9",
"Graphic3d_TextureUnit_BaseColor",
"Graphic3d_TextureUnit_EnvMap",
"Graphic3d_TextureUnit_NB",
"Graphic3d_ToneMappingMethod_Disabled",
"Graphic3d_ToneMappingMethod_Filmic",
"Graphic3d_TypeOfBackground_NB",
"Graphic3d_TypeOfLightSource_NB",
"Graphic3d_TypeOfLimit_HasBlendedOit",
"Graphic3d_TypeOfLimit_HasBlendedOitMsaa",
"Graphic3d_TypeOfLimit_HasFlatShading",
"Graphic3d_TypeOfLimit_HasMeshEdges",
"Graphic3d_TypeOfLimit_HasRayTracing",
"Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling",
"Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic",
"Graphic3d_TypeOfLimit_HasRayTracingTextures",
"Graphic3d_TypeOfLimit_IsWorkaroundFBO",
"Graphic3d_TypeOfLimit_MaxCombinedTextureUnits",
"Graphic3d_TypeOfLimit_MaxMsaa",
"Graphic3d_TypeOfLimit_MaxNbClipPlanes",
"Graphic3d_TypeOfLimit_MaxNbLights",
"Graphic3d_TypeOfLimit_MaxNbViews",
"Graphic3d_TypeOfLimit_MaxTextureSize",
"Graphic3d_TypeOfLimit_MaxViewDumpSizeX",
"Graphic3d_TypeOfLimit_MaxViewDumpSizeY",
"Graphic3d_TypeOfLimit_NB",
"Graphic3d_TypeOfReflection_NB",
"Graphic3d_TypeOfShadingModel_NB",
"Graphic3d_VTA_BOTTOM",
"Graphic3d_VTA_CENTER",
"Graphic3d_VTA_TOP",
"Graphic3d_VTA_TOPFIRSTLINE",
"Graphic3d_ZLayerDepthClear",
"Graphic3d_ZLayerDepthOffset",
"Graphic3d_ZLayerDepthTest",
"Graphic3d_ZLayerDepthWrite",
"Graphic3d_ZLayerId_BotOSD",
"Graphic3d_ZLayerId_Default",
"Graphic3d_ZLayerId_Top",
"Graphic3d_ZLayerId_TopOSD",
"Graphic3d_ZLayerId_Topmost",
"Graphic3d_ZLayerId_UNKNOWN",
"V3d_AMBIENT",
"V3d_COLOR",
"V3d_DIRECTIONAL",
"V3d_FLAT",
"V3d_GOURAUD",
"V3d_PHONG",
"V3d_POSITIONAL",
"V3d_SPOT"
]
class Graphic3d_AlphaMode():
    """
    Defines how alpha value of base color / texture should be treated.

    Members:

      Graphic3d_AlphaMode_Opaque

      Graphic3d_AlphaMode_Mask

      Graphic3d_AlphaMode_Blend

      Graphic3d_AlphaMode_BlendAuto
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_AlphaMode_Blend: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Blend
    Graphic3d_AlphaMode_BlendAuto: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_BlendAuto
    Graphic3d_AlphaMode_Mask: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Mask
    Graphic3d_AlphaMode_Opaque: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Opaque
    __entries: dict # value = {'Graphic3d_AlphaMode_Opaque': (Graphic3d_AlphaMode.Graphic3d_AlphaMode_Opaque, None), 'Graphic3d_AlphaMode_Mask': (Graphic3d_AlphaMode.Graphic3d_AlphaMode_Mask, None), 'Graphic3d_AlphaMode_Blend': (Graphic3d_AlphaMode.Graphic3d_AlphaMode_Blend, None), 'Graphic3d_AlphaMode_BlendAuto': (Graphic3d_AlphaMode.Graphic3d_AlphaMode_BlendAuto, None)}
    __members__: dict # value = {'Graphic3d_AlphaMode_Opaque': Graphic3d_AlphaMode.Graphic3d_AlphaMode_Opaque, 'Graphic3d_AlphaMode_Mask': Graphic3d_AlphaMode.Graphic3d_AlphaMode_Mask, 'Graphic3d_AlphaMode_Blend': Graphic3d_AlphaMode.Graphic3d_AlphaMode_Blend, 'Graphic3d_AlphaMode_BlendAuto': Graphic3d_AlphaMode.Graphic3d_AlphaMode_BlendAuto}
    pass
class Graphic3d_Array1OfAttribute():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Graphic3d_Array1OfAttribute) -> Graphic3d_Array1OfAttribute: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Graphic3d_Attribute: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Graphic3d_Attribute: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_Attribute: 
        """
        Variable value access
        """
    def First(self) -> Graphic3d_Attribute: 
        """
        Returns first element
        """
    def Init(self,theValue : Graphic3d_Attribute) -> None: 
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
    def Last(self) -> Graphic3d_Attribute: 
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
    def Move(self,theOther : Graphic3d_Array1OfAttribute) -> Graphic3d_Array1OfAttribute: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Graphic3d_Attribute) -> None: 
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
    def Value(self,theIndex : int) -> Graphic3d_Attribute: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_Array1OfAttribute) -> None: ...
    @overload
    def __init__(self,theBegin : Graphic3d_Attribute,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Graphic3d_ArrayOfIndexedMapOfStructure():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Graphic3d_ArrayOfIndexedMapOfStructure) -> Graphic3d_ArrayOfIndexedMapOfStructure: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Graphic3d_IndexedMapOfStructure: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Graphic3d_IndexedMapOfStructure: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_IndexedMapOfStructure: 
        """
        Variable value access
        """
    def First(self) -> Graphic3d_IndexedMapOfStructure: 
        """
        Returns first element
        """
    def Init(self,theValue : Graphic3d_IndexedMapOfStructure) -> None: 
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
    def Last(self) -> Graphic3d_IndexedMapOfStructure: 
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
    def Move(self,theOther : Graphic3d_ArrayOfIndexedMapOfStructure) -> Graphic3d_ArrayOfIndexedMapOfStructure: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Graphic3d_IndexedMapOfStructure) -> None: 
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
    def Value(self,theIndex : int) -> Graphic3d_IndexedMapOfStructure: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Graphic3d_IndexedMapOfStructure,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_ArrayOfIndexedMapOfStructure) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Graphic3d_ArrayOfPrimitives(OCP.Standard.Standard_Transient):
    """
    This class furnish services to defined and fill an array of primitives which can be passed directly to graphics rendering API.This class furnish services to defined and fill an array of primitives which can be passed directly to graphics rendering API.This class furnish services to defined and fill an array of primitives which can be passed directly to graphics rendering API.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
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
class Graphic3d_ArrayOfPolygons(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains polygons array definition. WARNING! Polygon primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.Contains polygons array definition. WARNING! Polygon primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxBounds : int=0,theMaxEdges : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasBColors : bool=False,theHasVTexels : bool=False) -> None: ...
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
class Graphic3d_ArrayOfPolylines(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains polylines array definition.Contains polylines array definition.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxBounds : int=0,theMaxEdges : int=0,theHasVColors : bool=False,theHasBColors : bool=False) -> None: ...
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
class Graphic3d_ArrayOfPoints(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains points array definition.Contains points array definition.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theHasVColors : bool=False,theHasVNormals : bool=False) -> None: ...
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
class Graphic3d_ArrayOfQuadrangleStrips(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains quadrangles strip array definition. WARNING! Quadrangle primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.Contains quadrangles strip array definition. WARNING! Quadrangle primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxStrips : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxStrips : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasSColors : bool=False,theHasVTexels : bool=False) -> None: ...
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
class Graphic3d_ArrayOfQuadrangles(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains quadrangles array definition. WARNING! Quadrangle primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.Contains quadrangles array definition. WARNING! Quadrangle primitives might be unsupported by graphics library. Triangulation should be used instead of quads for better compatibility.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasVTexels : bool=False) -> None: ...
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
class Graphic3d_ArrayOfSegments(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains segments array definition.Contains segments array definition.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int=0,theHasVColors : bool=False) -> None: ...
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
class Graphic3d_ArrayOfTriangleFans(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains triangles fan array definitionContains triangles fan array definition
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxFans : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasBColors : bool=False,theHasVTexels : bool=False) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxFans : int,theArrayFlags : int) -> None: ...
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
class Graphic3d_ArrayOfTriangleStrips(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains triangles strip array definition.Contains triangles strip array definition.
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxStrips : int,theArrayFlags : int) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxStrips : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasBColors : bool=False,theHasVTexels : bool=False) -> None: ...
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
class Graphic3d_ArrayOfTriangles(Graphic3d_ArrayOfPrimitives, OCP.Standard.Standard_Transient):
    """
    Contains triangles array definitionContains triangles array definition
    """
    @overload
    def AddBound(self,theEdgeNumber : int,theR : float,theG : float,theB : float) -> int: 
        """
        Adds a bound of length theEdgeNumber in the bound array

        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array. Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE

        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array. Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        """
    @overload
    def AddBound(self,theEdgeNumber : int) -> int: ...
    @overload
    def AddBound(self,theEdgeNumber : int,theBColor : OCP.Quantity.Quantity_Color) -> int: ...
    def AddEdge(self,theVertexIndex : int) -> int: 
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array.

        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in the array.

        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array.
        """
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddPolylineEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add line strip (polyline) into indexed segments array. N-1 segments are added from N input nodes (or N with closed flag). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    def AddQuadEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: 
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: 
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddQuadTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int,theVertexIndex4 : int) -> int: ...
    def AddSegmentEdges(self,theVertexIndex1 : int,theVertexIndex2 : int) -> int: 
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        """
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec3i) -> int: 
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.

        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddTriangleEdges(self,theVertexIndex1 : int,theVertexIndex2 : int,theVertexIndex3 : int) -> int: ...
    @overload
    def AddTriangleEdges(self,theIndexes : Graphic3d_Vec4i) -> int: ...
    def AddTriangleFanEdges(self,theVertexLower : int,theVertexUpper : int,theToClose : bool) -> None: 
        """
        Add triangle fan into indexed triangulation array. N-2 triangles are added from N input nodes (or N-1 with closed flag). Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    def AddTriangleStripEdges(self,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Add triangle strip into indexed triangulation array. N-2 triangles are added from N input nodes. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        """
    @overload
    def AddVertex(self,theVertex : Graphic3d_Vec3) -> int: 
        """
        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice in the array.

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex color in the vertex array. Warning: theColor is ignored when the hasVColors constructor parameter is FALSE

        Adds a vertice and vertex normal in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice and vertex normal in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice,vertex normal and color in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theColor is ignored when the hasVColors constructor parameter is FALSE.

        Adds a vertice and vertex texture in the vertex array. theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice and vertex texture coordinates in the vertex array. Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE and theTexel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.

        Adds a vertice,vertex normal and texture in the vertex array. Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE and Texel is ignored when the hasVTexels constructor parameter is FALSE.
        """
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theTexel : OCP.gp.gp_Pnt2d) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor32 : int) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : Graphic3d_Vec4ub) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float,theTX : float,theTY : float) -> int: ...
    @overload
    def AddVertex(self,theX : float,theY : float,theZ : float,theNX : float,theNY : float,theNZ : float) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt,theNormal : OCP.gp.gp_Dir,theColor : OCP.Quantity.Quantity_Color) -> int: ...
    @overload
    def AddVertex(self,theVertex : OCP.gp.gp_Pnt) -> int: ...
    def Attributes(self) -> Graphic3d_Buffer: 
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """
    def Bound(self,theRank : int) -> int: 
        """
        Returns the edge number at rank theRank.
        """
    @overload
    def BoundColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the bound color at rank theRank from the bound table if defined.

        Returns the bound color values at rank theRank from the bound table if defined.
        """
    @overload
    def BoundColor(self,theRank : int) -> Tuple[float, float, float]: ...
    def BoundNumber(self) -> int: 
        """
        Returns the number of defined bounds
        """
    def BoundNumberAllocated(self) -> int: 
        """
        Returns the number of allocated bounds
        """
    def Bounds(self) -> Graphic3d_BoundBuffer: 
        """
        Returns optional bounds buffer.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: 
        """
        Create an array of specified type.

        Create an array of specified type.
        """
    @staticmethod
    @overload
    def CreateArray_s(theType : Graphic3d_TypeOfPrimitiveArray,theMaxVertexs : int,theMaxBounds : int,theMaxEdges : int,theArrayFlags : int) -> Graphic3d_ArrayOfPrimitives: ...
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
    def Edge(self,theRank : int) -> int: 
        """
        Returns the vertex index at rank theRank in the range [1,EdgeNumber()]
        """
    def EdgeNumber(self) -> int: 
        """
        Returns the number of defined edges
        """
    def EdgeNumberAllocated(self) -> int: 
        """
        Returns the number of allocated edges
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasBoundColors(self) -> bool: 
        """
        Returns TRUE when bound colors array is defined.
        """
    def HasVertexColors(self) -> bool: 
        """
        Returns TRUE when vertex colors array is defined.
        """
    def HasVertexNormals(self) -> bool: 
        """
        Returns TRUE when vertex normals array is defined.
        """
    def HasVertexTexels(self) -> bool: 
        """
        Returns TRUE when vertex texels array is defined.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Indices(self) -> Graphic3d_IndexBuffer: 
        """
        Returns optional index buffer.
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
        Returns TRUE only when the contains of this array is available.
        """
    def ItemNumber(self) -> int: 
        """
        Returns the number of total items according to the array type.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the bound color of rank theIndex in the array.

        Change the bound color of rank theIndex in the array.
        """
    @overload
    def SetBoundColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex in the array.

        Change the vertex color of rank theIndex> in the array.
        """
    @overload
    def SetVertexColor(self,theIndex : int,theColor32 : int) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theR : float,theG : float,theB : float) -> None: ...
    @overload
    def SetVertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: ...
    @overload
    def SetVertexNormal(self,theIndex : int,theNX : float,theNY : float,theNZ : float) -> None: 
        """
        Change the vertex normal of rank theIndex in the array.

        Change the vertex normal of rank theIndex in the array.
        """
    @overload
    def SetVertexNormal(self,theIndex : int,theNormal : OCP.gp.gp_Dir) -> None: ...
    @overload
    def SetVertexTexel(self,theIndex : int,theTexel : OCP.gp.gp_Pnt2d) -> None: 
        """
        Change the vertex texel of rank theIndex in the array.

        Change the vertex texel of rank theIndex in the array.
        """
    @overload
    def SetVertexTexel(self,theIndex : int,theTX : float,theTY : float) -> None: ...
    @overload
    def SetVertice(self,theIndex : int,theX : float,theY : float,theZ : float) -> None: 
        """
        Change the vertice of rank theIndex in the array.

        Change the vertice of rank theIndex in the array.
        """
    @overload
    def SetVertice(self,theIndex : int,theVertex : OCP.gp.gp_Pnt) -> None: ...
    def StringType(self) -> str: 
        """
        Returns the string type of this primitive
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfPrimitiveArray: 
        """
        Returns the type of this primitive
        """
    @overload
    def VertexColor(self,theIndex : int,theColor : Graphic3d_Vec4ub) -> None: 
        """
        Returns the vertex color at rank theRank from the vertex table if defined.

        Returns the vertex color at rank theIndex from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.

        Returns the vertex color values at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexColor(self,theRank : int) -> Tuple[int]: ...
    @overload
    def VertexColor(self,theRank : int) -> OCP.Quantity.Quantity_Color: ...
    @overload
    def VertexColor(self,theRank : int) -> Tuple[float, float, float]: ...
    @overload
    def VertexNormal(self,theRank : int) -> OCP.gp.gp_Dir: 
        """
        Returns the vertex normal at rank theRank from the vertex table if defined.

        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexNormal(self,theRank : int) -> Tuple[float, float, float]: ...
    def VertexNumber(self) -> int: 
        """
        Returns the number of defined vertex
        """
    def VertexNumberAllocated(self) -> int: 
        """
        Returns the number of allocated vertex
        """
    @overload
    def VertexTexel(self,theRank : int) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.

        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def VertexTexel(self,theRank : int) -> Tuple[float, float]: ...
    @overload
    def Vertice(self,theRank : int) -> Tuple[float, float, float]: 
        """
        Returns the vertice at rank theRank from the vertex table if defined.

        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        """
    @overload
    def Vertice(self,theRank : int) -> OCP.gp.gp_Pnt: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int=0,theHasVNormals : bool=False,theHasVColors : bool=False,theHasVTexels : bool=False) -> None: ...
    @overload
    def __init__(self,theMaxVertexs : int,theMaxEdges : int,theArrayFlags : int) -> None: ...
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
class Graphic3d_Aspects(OCP.Standard.Standard_Transient):
    """
    This class defines graphic attributes.This class defines graphic attributes.
    """
    def AllowBackFace(self) -> None: 
        """
        Allows the display of back-facing filled polygons.
        """
    def AlphaCutoff(self) -> float: 
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode (0.5 by default). If the alpha value is greater than or equal to this value then it is rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """
    def AlphaMode(self) -> Graphic3d_AlphaMode: 
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default, for backward compatibility).
        """
    def BackFace(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def BackInteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return back interior color.
        """
    def BackInteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return back interior color.
        """
    def BackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return the color.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color
        """
    def ColorSubTitle(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return text background/shadow color; equals to EdgeColor() property.
        """
    def ColorSubTitleRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns text background/shadow color; equals to EdgeColor() property.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distinguish(self) -> bool: 
        """
        Returns true if material properties should be distinguished for back and front faces (false by default).
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color of edges.
        """
    def EdgeColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color of edges.
        """
    def EdgeLineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return edges line type (same as LineType()).
        """
    def EdgeWidth(self) -> float: 
        """
        Return width for edges in pixels (same as LineWidth()).
        """
    def FrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HatchStyle(self) -> Graphic3d_HatchStyle: 
        """
        Returns the hatch type used when InteriorStyle is IS_HATCH
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return interior color.
        """
    def InteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return interior color.
        """
    def InteriorStyle(self) -> OCP.Aspect.Aspect_InteriorStyle: 
        """
        Return interior rendering style; Aspect_IS_SOLID by default.
        """
    def IsEqual(self,theOther : Graphic3d_Aspects) -> bool: 
        """
        Check for equality with another aspects.
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
    def IsMarkerSprite(self) -> bool: 
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or generated).
        """
    def IsTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def LineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type; Aspect_TOL_SOLID by default.
        """
    def LineWidth(self) -> float: 
        """
        Return width for edges in pixels; 1.0 by default.
        """
    def MarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def MarkerScale(self) -> float: 
        """
        Return marker scale factor; 1.0 by default.
        """
    def MarkerType(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type; Aspect_TOM_POINT by default.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Returns current polygon offsets settings.
        """
    def PolygonOffsets(self,theFactor : float,theUnits : float) -> Tuple[int]: 
        """
        Returns current polygon offsets settings.
        """
    def SetAlphaMode(self,theMode : Graphic3d_AlphaMode,theAlphaCutoff : float=0.5) -> None: 
        """
        Defines the way how alpha value should be treated.
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the interior of the back face

        Modifies the color of the interior of the back face
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of internal faces
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies text background/shadow color; equals to EdgeColor() property.

        Modifies text background/shadow color; equals to EdgeColor() property.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetDistinguish(self,toDistinguish : bool) -> None: 
        """
        Set material distinction between front and back faces.
        """
    def SetDistinguishOff(self) -> None: 
        """
        Forbids material distinction between front and back faces.
        """
    def SetDistinguishOn(self) -> None: 
        """
        Allows material distinction between front and back faces.
        """
    def SetDrawEdges(self,theToDraw : bool) -> None: 
        """
        Set if mesh edges should be drawn or not.
        """
    def SetDrawSilhouette(self,theToDraw : bool) -> None: 
        """
        Enables/disables drawing silhouette (outline).
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the edge of the face

        Modifies the color of the edge of the face
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetEdgeLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the edge line type (same as SetLineType())
        """
    def SetEdgeOff(self) -> None: 
        """
        The edges of FillAreas are not drawn.
        """
    def SetEdgeOn(self) -> None: 
        """
        The edges of FillAreas are drawn.
        """
    def SetEdgeWidth(self,theWidth : float) -> None: 
        """
        Modifies the edge thickness (same as SetLineWidth())
        """
    def SetFrontMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of external faces
        """
    @overload
    def SetHatchStyle(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH

        Modifies the hatch type used when InteriorStyle is IS_HATCH
        """
    @overload
    def SetHatchStyle(self,theStyle : Graphic3d_HatchStyle) -> None: ...
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color of the interior of the face

        Modifies the color of the interior of the face
        """
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetInteriorStyle(self,theStyle : OCP.Aspect.Aspect_InteriorStyle) -> None: 
        """
        Modifies the interior type used for rendering
        """
    def SetLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the line type
        """
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def SetMarkerImage(self,theImage : Graphic3d_MarkerImage) -> None: 
        """
        Set marker's image texture.
        """
    def SetMarkerScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """
    def SetMarkerType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def SetPolygonOffset(self,theOffset : Graphic3d_PolygonOffset) -> None: 
        """
        Sets polygon offsets settings.
        """
    def SetPolygonOffsets(self,theMode : int,theFactor : float=1.0,theUnits : float=0.0) -> None: 
        """
        Sets up OpenGL polygon offsets mechanism. <aMode> parameter can contain various combinations of Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means that polygon offsets are not changed). If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits> arguments are used by graphic renderer to calculate a depth offset value:
        """
    def SetShaderProgram(self,theProgram : Graphic3d_ShaderProgram) -> None: 
        """
        Sets up OpenGL/GLSL shader program.
        """
    def SetShadingModel(self,theShadingModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model
        """
    def SetSkipFirstEdge(self,theToSkipFirstEdge : bool) -> None: 
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into triangles.
        """
    def SetSuppressBackFaces(self,theToSuppress : bool) -> None: 
        """
        Assign back faces culling flag.
        """
    def SetTextAngle(self,theAngle : float) -> None: 
        """
        Turns usage of text rotated
        """
    def SetTextDisplayType(self,theType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Sets display type.
        """
    def SetTextFont(self,theFont : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Modifies the font.
        """
    def SetTextFontAspect(self,theFontAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        Turns usage of Aspect text
        """
    def SetTextStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetTextZoomable(self,theFlag : bool) -> None: 
        """
        Turns usage of text zoomable on/off
        """
    def SetTextureMap(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Assign texture to be mapped. See also SetTextureMapOn() to actually activate texture mapping.
        """
    def SetTextureMapOff(self) -> None: 
        """
        Disable texture mapping.
        """
    @overload
    def SetTextureMapOn(self) -> None: 
        """
        Enable or disable texture mapping (has no effect if texture is not set).

        Enable texture mapping (has no effect if texture is not set).
        """
    @overload
    def SetTextureMapOn(self,theToMap : bool) -> None: ...
    def SetTextureSet(self,theTextures : Graphic3d_TextureSet) -> None: 
        """
        Setup texture array to be mapped.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns shading model; Graphic3d_TOSM_DEFAULT by default. Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """
    def SuppressBackFace(self) -> None: 
        """
        Suppress the display of back-facing filled polygons. A back-facing polygon is defined as a polygon whose vertices are in a clockwise order with respect to screen coordinates.
        """
    def TextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def TextDisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Returns display type; Aspect_TODT_NORMAL by default.
        """
    def TextFont(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the font; NULL string by default.
        """
    def TextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def TextStyle(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Returns the text style; Aspect_TOST_NORMAL by default.
        """
    def TextureMap(self) -> Graphic3d_TextureMap: 
        """
        Return texture to be mapped.
        """
    def TextureMapState(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def TextureSet(self) -> Graphic3d_TextureSet: 
        """
        Return texture array to be mapped.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawEdges(self) -> bool: 
        """
        Returns true if mesh edges should be drawn (false by default).
        """
    def ToDrawSilhouette(self) -> bool: 
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by default.
        """
    def ToMapTexture(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def ToSkipFirstEdge(self) -> bool: 
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default. Graphics hardware works mostly with triangles, so that wireframe presentation will draw triangle edges by default. This flag allows rendering wireframe presentation of quad-only array split into triangles. For this, quads should be split in specific order, so that the quad diagonal (to be NOT rendered) goes first: 1------2 / / Triangle #1: 2-0-1; Triangle #2: 0-2-3 0------3
        """
    def ToSuppressBackFaces(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
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
class Graphic3d_AspectLine3d(Graphic3d_Aspects, OCP.Standard.Standard_Transient):
    """
    Creates and updates a group of attributes for 3d line primitives. This group contains the color, the type of line, and its thickness.Creates and updates a group of attributes for 3d line primitives. This group contains the color, the type of line, and its thickness.
    """
    def AllowBackFace(self) -> None: 
        """
        Allows the display of back-facing filled polygons.
        """
    def AlphaCutoff(self) -> float: 
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode (0.5 by default). If the alpha value is greater than or equal to this value then it is rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """
    def AlphaMode(self) -> Graphic3d_AlphaMode: 
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default, for backward compatibility).
        """
    def BackFace(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def BackInteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return back interior color.
        """
    def BackInteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return back interior color.
        """
    def BackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return the color.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color
        """
    def ColorSubTitle(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return text background/shadow color; equals to EdgeColor() property.
        """
    def ColorSubTitleRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns text background/shadow color; equals to EdgeColor() property.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distinguish(self) -> bool: 
        """
        Returns true if material properties should be distinguished for back and front faces (false by default).
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color of edges.
        """
    def EdgeColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color of edges.
        """
    def EdgeLineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return edges line type (same as LineType()).
        """
    def EdgeWidth(self) -> float: 
        """
        Return width for edges in pixels (same as LineWidth()).
        """
    def FrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HatchStyle(self) -> Graphic3d_HatchStyle: 
        """
        Returns the hatch type used when InteriorStyle is IS_HATCH
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return interior color.
        """
    def InteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return interior color.
        """
    def InteriorStyle(self) -> OCP.Aspect.Aspect_InteriorStyle: 
        """
        Return interior rendering style; Aspect_IS_SOLID by default.
        """
    def IsEqual(self,theOther : Graphic3d_Aspects) -> bool: 
        """
        Check for equality with another aspects.
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
    def IsMarkerSprite(self) -> bool: 
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or generated).
        """
    def IsTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def LineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type; Aspect_TOL_SOLID by default.
        """
    def LineWidth(self) -> float: 
        """
        Return width for edges in pixels; 1.0 by default.
        """
    def MarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def MarkerScale(self) -> float: 
        """
        Return marker scale factor; 1.0 by default.
        """
    def MarkerType(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type; Aspect_TOM_POINT by default.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Returns current polygon offsets settings.
        """
    def PolygonOffsets(self,theFactor : float,theUnits : float) -> Tuple[int]: 
        """
        Returns current polygon offsets settings.
        """
    def SetAlphaMode(self,theMode : Graphic3d_AlphaMode,theAlphaCutoff : float=0.5) -> None: 
        """
        Defines the way how alpha value should be treated.
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the interior of the back face

        Modifies the color of the interior of the back face
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of internal faces
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies text background/shadow color; equals to EdgeColor() property.

        Modifies text background/shadow color; equals to EdgeColor() property.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetDistinguish(self,toDistinguish : bool) -> None: 
        """
        Set material distinction between front and back faces.
        """
    def SetDistinguishOff(self) -> None: 
        """
        Forbids material distinction between front and back faces.
        """
    def SetDistinguishOn(self) -> None: 
        """
        Allows material distinction between front and back faces.
        """
    def SetDrawEdges(self,theToDraw : bool) -> None: 
        """
        Set if mesh edges should be drawn or not.
        """
    def SetDrawSilhouette(self,theToDraw : bool) -> None: 
        """
        Enables/disables drawing silhouette (outline).
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the edge of the face

        Modifies the color of the edge of the face
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetEdgeLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the edge line type (same as SetLineType())
        """
    def SetEdgeOff(self) -> None: 
        """
        The edges of FillAreas are not drawn.
        """
    def SetEdgeOn(self) -> None: 
        """
        The edges of FillAreas are drawn.
        """
    def SetEdgeWidth(self,theWidth : float) -> None: 
        """
        Modifies the edge thickness (same as SetLineWidth())
        """
    def SetFrontMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of external faces
        """
    @overload
    def SetHatchStyle(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH

        Modifies the hatch type used when InteriorStyle is IS_HATCH
        """
    @overload
    def SetHatchStyle(self,theStyle : Graphic3d_HatchStyle) -> None: ...
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color of the interior of the face

        Modifies the color of the interior of the face
        """
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetInteriorStyle(self,theStyle : OCP.Aspect.Aspect_InteriorStyle) -> None: 
        """
        Modifies the interior type used for rendering
        """
    def SetLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the line type
        """
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def SetMarkerImage(self,theImage : Graphic3d_MarkerImage) -> None: 
        """
        Set marker's image texture.
        """
    def SetMarkerScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """
    def SetMarkerType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def SetPolygonOffset(self,theOffset : Graphic3d_PolygonOffset) -> None: 
        """
        Sets polygon offsets settings.
        """
    def SetPolygonOffsets(self,theMode : int,theFactor : float=1.0,theUnits : float=0.0) -> None: 
        """
        Sets up OpenGL polygon offsets mechanism. <aMode> parameter can contain various combinations of Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means that polygon offsets are not changed). If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits> arguments are used by graphic renderer to calculate a depth offset value:
        """
    def SetShaderProgram(self,theProgram : Graphic3d_ShaderProgram) -> None: 
        """
        Sets up OpenGL/GLSL shader program.
        """
    def SetShadingModel(self,theShadingModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model
        """
    def SetSkipFirstEdge(self,theToSkipFirstEdge : bool) -> None: 
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into triangles.
        """
    def SetSuppressBackFaces(self,theToSuppress : bool) -> None: 
        """
        Assign back faces culling flag.
        """
    def SetTextAngle(self,theAngle : float) -> None: 
        """
        Turns usage of text rotated
        """
    def SetTextDisplayType(self,theType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Sets display type.
        """
    def SetTextFont(self,theFont : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Modifies the font.
        """
    def SetTextFontAspect(self,theFontAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        Turns usage of Aspect text
        """
    def SetTextStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetTextZoomable(self,theFlag : bool) -> None: 
        """
        Turns usage of text zoomable on/off
        """
    def SetTextureMap(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Assign texture to be mapped. See also SetTextureMapOn() to actually activate texture mapping.
        """
    def SetTextureMapOff(self) -> None: 
        """
        Disable texture mapping.
        """
    @overload
    def SetTextureMapOn(self) -> None: 
        """
        Enable or disable texture mapping (has no effect if texture is not set).

        Enable texture mapping (has no effect if texture is not set).
        """
    @overload
    def SetTextureMapOn(self,theToMap : bool) -> None: ...
    def SetTextureSet(self,theTextures : Graphic3d_TextureSet) -> None: 
        """
        Setup texture array to be mapped.
        """
    def SetType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the type of line.
        """
    def SetWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness. Warning: Raises Standard_OutOfRange if the width is a negative value.

        Modifies the line thickness. Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns shading model; Graphic3d_TOSM_DEFAULT by default. Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """
    def SuppressBackFace(self) -> None: 
        """
        Suppress the display of back-facing filled polygons. A back-facing polygon is defined as a polygon whose vertices are in a clockwise order with respect to screen coordinates.
        """
    def TextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def TextDisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Returns display type; Aspect_TODT_NORMAL by default.
        """
    def TextFont(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the font; NULL string by default.
        """
    def TextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def TextStyle(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Returns the text style; Aspect_TOST_NORMAL by default.
        """
    def TextureMap(self) -> Graphic3d_TextureMap: 
        """
        Return texture to be mapped.
        """
    def TextureMapState(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def TextureSet(self) -> Graphic3d_TextureSet: 
        """
        Return texture array to be mapped.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawEdges(self) -> bool: 
        """
        Returns true if mesh edges should be drawn (false by default).
        """
    def ToDrawSilhouette(self) -> bool: 
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by default.
        """
    def ToMapTexture(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def ToSkipFirstEdge(self) -> bool: 
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default. Graphics hardware works mostly with triangles, so that wireframe presentation will draw triangle edges by default. This flag allows rendering wireframe presentation of quad-only array split into triangles. For this, quads should be split in specific order, so that the quad diagonal (to be NOT rendered) goes first: 1------2 / / Triangle #1: 2-0-1; Triangle #2: 0-2-3 0------3
        """
    def ToSuppressBackFaces(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def Type(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type.
        """
    def Width(self) -> float: 
        """
        Return line width.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theType : OCP.Aspect.Aspect_TypeOfLine,theWidth : float) -> None: ...
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
class Graphic3d_AspectMarker3d(Graphic3d_Aspects, OCP.Standard.Standard_Transient):
    """
    Creates and updates an attribute group for marker type primitives. This group contains the type of marker, its color, and its scale factor.Creates and updates an attribute group for marker type primitives. This group contains the type of marker, its color, and its scale factor.
    """
    def AllowBackFace(self) -> None: 
        """
        Allows the display of back-facing filled polygons.
        """
    def AlphaCutoff(self) -> float: 
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode (0.5 by default). If the alpha value is greater than or equal to this value then it is rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """
    def AlphaMode(self) -> Graphic3d_AlphaMode: 
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default, for backward compatibility).
        """
    def BackFace(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def BackInteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return back interior color.
        """
    def BackInteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return back interior color.
        """
    def BackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return the color.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color
        """
    def ColorSubTitle(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return text background/shadow color; equals to EdgeColor() property.
        """
    def ColorSubTitleRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns text background/shadow color; equals to EdgeColor() property.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distinguish(self) -> bool: 
        """
        Returns true if material properties should be distinguished for back and front faces (false by default).
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color of edges.
        """
    def EdgeColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color of edges.
        """
    def EdgeLineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return edges line type (same as LineType()).
        """
    def EdgeWidth(self) -> float: 
        """
        Return width for edges in pixels (same as LineWidth()).
        """
    def FrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def GetMarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTextureSize(self) -> Tuple[int, int]: 
        """
        Returns marker's texture size.
        """
    def HatchStyle(self) -> Graphic3d_HatchStyle: 
        """
        Returns the hatch type used when InteriorStyle is IS_HATCH
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return interior color.
        """
    def InteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return interior color.
        """
    def InteriorStyle(self) -> OCP.Aspect.Aspect_InteriorStyle: 
        """
        Return interior rendering style; Aspect_IS_SOLID by default.
        """
    def IsEqual(self,theOther : Graphic3d_Aspects) -> bool: 
        """
        Check for equality with another aspects.
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
    def IsMarkerSprite(self) -> bool: 
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or generated).
        """
    def IsTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def LineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type; Aspect_TOL_SOLID by default.
        """
    def LineWidth(self) -> float: 
        """
        Return width for edges in pixels; 1.0 by default.
        """
    def MarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def MarkerScale(self) -> float: 
        """
        Return marker scale factor; 1.0 by default.
        """
    def MarkerType(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type; Aspect_TOM_POINT by default.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Returns current polygon offsets settings.
        """
    def PolygonOffsets(self,theFactor : float,theUnits : float) -> Tuple[int]: 
        """
        Returns current polygon offsets settings.
        """
    def Scale(self) -> float: 
        """
        Return scale factor.
        """
    def SetAlphaMode(self,theMode : Graphic3d_AlphaMode,theAlphaCutoff : float=0.5) -> None: 
        """
        Defines the way how alpha value should be treated.
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the interior of the back face

        Modifies the color of the interior of the back face
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of internal faces
        """
    def SetBitMap(self,theWidth : int,theHeight : int,theTexture : OCP.TColStd.TColStd_HArray1OfByte) -> None: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies text background/shadow color; equals to EdgeColor() property.

        Modifies text background/shadow color; equals to EdgeColor() property.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetDistinguish(self,toDistinguish : bool) -> None: 
        """
        Set material distinction between front and back faces.
        """
    def SetDistinguishOff(self) -> None: 
        """
        Forbids material distinction between front and back faces.
        """
    def SetDistinguishOn(self) -> None: 
        """
        Allows material distinction between front and back faces.
        """
    def SetDrawEdges(self,theToDraw : bool) -> None: 
        """
        Set if mesh edges should be drawn or not.
        """
    def SetDrawSilhouette(self,theToDraw : bool) -> None: 
        """
        Enables/disables drawing silhouette (outline).
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the edge of the face

        Modifies the color of the edge of the face
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetEdgeLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the edge line type (same as SetLineType())
        """
    def SetEdgeOff(self) -> None: 
        """
        The edges of FillAreas are not drawn.
        """
    def SetEdgeOn(self) -> None: 
        """
        The edges of FillAreas are drawn.
        """
    def SetEdgeWidth(self,theWidth : float) -> None: 
        """
        Modifies the edge thickness (same as SetLineWidth())
        """
    def SetFrontMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of external faces
        """
    @overload
    def SetHatchStyle(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH

        Modifies the hatch type used when InteriorStyle is IS_HATCH
        """
    @overload
    def SetHatchStyle(self,theStyle : Graphic3d_HatchStyle) -> None: ...
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color of the interior of the face

        Modifies the color of the interior of the face
        """
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetInteriorStyle(self,theStyle : OCP.Aspect.Aspect_InteriorStyle) -> None: 
        """
        Modifies the interior type used for rendering
        """
    def SetLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the line type
        """
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def SetMarkerImage(self,theImage : Graphic3d_MarkerImage) -> None: 
        """
        Set marker's image texture.
        """
    def SetMarkerScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """
    def SetMarkerType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def SetPolygonOffset(self,theOffset : Graphic3d_PolygonOffset) -> None: 
        """
        Sets polygon offsets settings.
        """
    def SetPolygonOffsets(self,theMode : int,theFactor : float=1.0,theUnits : float=0.0) -> None: 
        """
        Sets up OpenGL polygon offsets mechanism. <aMode> parameter can contain various combinations of Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means that polygon offsets are not changed). If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits> arguments are used by graphic renderer to calculate a depth offset value:
        """
    def SetScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.

        Assign scale factor.
        """
    def SetShaderProgram(self,theProgram : Graphic3d_ShaderProgram) -> None: 
        """
        Sets up OpenGL/GLSL shader program.
        """
    def SetShadingModel(self,theShadingModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model
        """
    def SetSkipFirstEdge(self,theToSkipFirstEdge : bool) -> None: 
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into triangles.
        """
    def SetSuppressBackFaces(self,theToSuppress : bool) -> None: 
        """
        Assign back faces culling flag.
        """
    def SetTextAngle(self,theAngle : float) -> None: 
        """
        Turns usage of text rotated
        """
    def SetTextDisplayType(self,theType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Sets display type.
        """
    def SetTextFont(self,theFont : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Modifies the font.
        """
    def SetTextFontAspect(self,theFontAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        Turns usage of Aspect text
        """
    def SetTextStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetTextZoomable(self,theFlag : bool) -> None: 
        """
        Turns usage of text zoomable on/off
        """
    def SetTextureMap(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Assign texture to be mapped. See also SetTextureMapOn() to actually activate texture mapping.
        """
    def SetTextureMapOff(self) -> None: 
        """
        Disable texture mapping.
        """
    @overload
    def SetTextureMapOn(self) -> None: 
        """
        Enable or disable texture mapping (has no effect if texture is not set).

        Enable texture mapping (has no effect if texture is not set).
        """
    @overload
    def SetTextureMapOn(self,theToMap : bool) -> None: ...
    def SetTextureSet(self,theTextures : Graphic3d_TextureSet) -> None: 
        """
        Setup texture array to be mapped.
        """
    def SetType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns shading model; Graphic3d_TOSM_DEFAULT by default. Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """
    def SuppressBackFace(self) -> None: 
        """
        Suppress the display of back-facing filled polygons. A back-facing polygon is defined as a polygon whose vertices are in a clockwise order with respect to screen coordinates.
        """
    def TextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def TextDisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Returns display type; Aspect_TODT_NORMAL by default.
        """
    def TextFont(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the font; NULL string by default.
        """
    def TextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def TextStyle(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Returns the text style; Aspect_TOST_NORMAL by default.
        """
    def TextureMap(self) -> Graphic3d_TextureMap: 
        """
        Return texture to be mapped.
        """
    def TextureMapState(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def TextureSet(self) -> Graphic3d_TextureSet: 
        """
        Return texture array to be mapped.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawEdges(self) -> bool: 
        """
        Returns true if mesh edges should be drawn (false by default).
        """
    def ToDrawSilhouette(self) -> bool: 
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by default.
        """
    def ToMapTexture(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def ToSkipFirstEdge(self) -> bool: 
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default. Graphics hardware works mostly with triangles, so that wireframe presentation will draw triangle edges by default. This flag allows rendering wireframe presentation of quad-only array split into triangles. For this, quads should be split in specific order, so that the quad diagonal (to be NOT rendered) goes first: 1------2 / / Triangle #1: 2-0-1; Triangle #2: 0-2-3 0------3
        """
    def ToSuppressBackFaces(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def Type(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type.
        """
    @overload
    def __init__(self,theType : OCP.Aspect.Aspect_TypeOfMarker,theColor : OCP.Quantity.Quantity_Color,theScale : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theTextureImage : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theWidth : int,theHeight : int,theTextureBitmap : OCP.TColStd.TColStd_HArray1OfByte) -> None: ...
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
class Graphic3d_AspectText3d(Graphic3d_Aspects, OCP.Standard.Standard_Transient):
    """
    Creates and updates a group of attributes for text primitives.Creates and updates a group of attributes for text primitives.
    """
    def AllowBackFace(self) -> None: 
        """
        Allows the display of back-facing filled polygons.
        """
    def AlphaCutoff(self) -> float: 
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode (0.5 by default). If the alpha value is greater than or equal to this value then it is rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """
    def AlphaMode(self) -> Graphic3d_AlphaMode: 
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default, for backward compatibility).
        """
    def BackFace(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def BackInteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return back interior color.
        """
    def BackInteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return back interior color.
        """
    def BackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return the text color.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return the text color.
        """
    def ColorSubTitle(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return text background/shadow color; equals to EdgeColor() property.
        """
    def ColorSubTitleRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns text background/shadow color; equals to EdgeColor() property.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Return display type.
        """
    def Distinguish(self) -> bool: 
        """
        Returns true if material properties should be distinguished for back and front faces (false by default).
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color of edges.
        """
    def EdgeColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color of edges.
        """
    def EdgeLineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return edges line type (same as LineType()).
        """
    def EdgeWidth(self) -> float: 
        """
        Return width for edges in pixels (same as LineWidth()).
        """
    def Font(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return the font.
        """
    def FrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def GetTextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def GetTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def HatchStyle(self) -> Graphic3d_HatchStyle: 
        """
        Returns the hatch type used when InteriorStyle is IS_HATCH
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return interior color.
        """
    def InteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return interior color.
        """
    def InteriorStyle(self) -> OCP.Aspect.Aspect_InteriorStyle: 
        """
        Return interior rendering style; Aspect_IS_SOLID by default.
        """
    def IsEqual(self,theOther : Graphic3d_Aspects) -> bool: 
        """
        Check for equality with another aspects.
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
    def IsMarkerSprite(self) -> bool: 
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or generated).
        """
    def IsTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def LineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type; Aspect_TOL_SOLID by default.
        """
    def LineWidth(self) -> float: 
        """
        Return width for edges in pixels; 1.0 by default.
        """
    def MarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def MarkerScale(self) -> float: 
        """
        Return marker scale factor; 1.0 by default.
        """
    def MarkerType(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type; Aspect_TOM_POINT by default.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Returns current polygon offsets settings.
        """
    def PolygonOffsets(self,theFactor : float,theUnits : float) -> Tuple[int]: 
        """
        Returns current polygon offsets settings.
        """
    def SetAlphaMode(self,theMode : Graphic3d_AlphaMode,theAlphaCutoff : float=0.5) -> None: 
        """
        Defines the way how alpha value should be treated.
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the interior of the back face

        Modifies the color of the interior of the back face
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of internal faces
        """
    @overload
    def SetColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color.

        Modifies the color.
        """
    @overload
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies text background/shadow color; equals to EdgeColor() property.

        Modifies text background/shadow color; equals to EdgeColor() property.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetDisplayType(self,theDisplayType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Define the display type of the text.
        """
    def SetDistinguish(self,toDistinguish : bool) -> None: 
        """
        Set material distinction between front and back faces.
        """
    def SetDistinguishOff(self) -> None: 
        """
        Forbids material distinction between front and back faces.
        """
    def SetDistinguishOn(self) -> None: 
        """
        Allows material distinction between front and back faces.
        """
    def SetDrawEdges(self,theToDraw : bool) -> None: 
        """
        Set if mesh edges should be drawn or not.
        """
    def SetDrawSilhouette(self,theToDraw : bool) -> None: 
        """
        Enables/disables drawing silhouette (outline).
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the edge of the face

        Modifies the color of the edge of the face
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetEdgeLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the edge line type (same as SetLineType())
        """
    def SetEdgeOff(self) -> None: 
        """
        The edges of FillAreas are not drawn.
        """
    def SetEdgeOn(self) -> None: 
        """
        The edges of FillAreas are drawn.
        """
    def SetEdgeWidth(self,theWidth : float) -> None: 
        """
        Modifies the edge thickness (same as SetLineWidth())
        """
    @overload
    def SetFont(self,theFont : str) -> None: 
        """
        Modifies the font.

        Modifies the font.
        """
    @overload
    def SetFont(self,theFont : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def SetFrontMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of external faces
        """
    @overload
    def SetHatchStyle(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH

        Modifies the hatch type used when InteriorStyle is IS_HATCH
        """
    @overload
    def SetHatchStyle(self,theStyle : Graphic3d_HatchStyle) -> None: ...
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color of the interior of the face

        Modifies the color of the interior of the face
        """
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetInteriorStyle(self,theStyle : OCP.Aspect.Aspect_InteriorStyle) -> None: 
        """
        Modifies the interior type used for rendering
        """
    def SetLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the line type
        """
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def SetMarkerImage(self,theImage : Graphic3d_MarkerImage) -> None: 
        """
        Set marker's image texture.
        """
    def SetMarkerScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """
    def SetMarkerType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def SetPolygonOffset(self,theOffset : Graphic3d_PolygonOffset) -> None: 
        """
        Sets polygon offsets settings.
        """
    def SetPolygonOffsets(self,theMode : int,theFactor : float=1.0,theUnits : float=0.0) -> None: 
        """
        Sets up OpenGL polygon offsets mechanism. <aMode> parameter can contain various combinations of Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means that polygon offsets are not changed). If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits> arguments are used by graphic renderer to calculate a depth offset value:
        """
    def SetShaderProgram(self,theProgram : Graphic3d_ShaderProgram) -> None: 
        """
        Sets up OpenGL/GLSL shader program.
        """
    def SetShadingModel(self,theShadingModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model
        """
    def SetSkipFirstEdge(self,theToSkipFirstEdge : bool) -> None: 
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into triangles.
        """
    def SetStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetSuppressBackFaces(self,theToSuppress : bool) -> None: 
        """
        Assign back faces culling flag.
        """
    def SetTextAngle(self,theAngle : float) -> None: 
        """
        Turns usage of text rotated
        """
    def SetTextDisplayType(self,theType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Sets display type.
        """
    def SetTextFont(self,theFont : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Modifies the font.
        """
    def SetTextFontAspect(self,theFontAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        Turns usage of Aspect text
        """
    def SetTextStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetTextZoomable(self,theFlag : bool) -> None: 
        """
        Turns usage of text zoomable on/off
        """
    def SetTextureMap(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Assign texture to be mapped. See also SetTextureMapOn() to actually activate texture mapping.
        """
    def SetTextureMapOff(self) -> None: 
        """
        Disable texture mapping.
        """
    @overload
    def SetTextureMapOn(self) -> None: 
        """
        Enable or disable texture mapping (has no effect if texture is not set).

        Enable texture mapping (has no effect if texture is not set).
        """
    @overload
    def SetTextureMapOn(self,theToMap : bool) -> None: ...
    def SetTextureSet(self,theTextures : Graphic3d_TextureSet) -> None: 
        """
        Setup texture array to be mapped.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns shading model; Graphic3d_TOSM_DEFAULT by default. Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """
    def Style(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Return the text style.
        """
    def SuppressBackFace(self) -> None: 
        """
        Suppress the display of back-facing filled polygons. A back-facing polygon is defined as a polygon whose vertices are in a clockwise order with respect to screen coordinates.
        """
    def TextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def TextDisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Returns display type; Aspect_TODT_NORMAL by default.
        """
    def TextFont(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the font; NULL string by default.
        """
    def TextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def TextStyle(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Returns the text style; Aspect_TOST_NORMAL by default.
        """
    def TextureMap(self) -> Graphic3d_TextureMap: 
        """
        Return texture to be mapped.
        """
    def TextureMapState(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def TextureSet(self) -> Graphic3d_TextureSet: 
        """
        Return texture array to be mapped.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawEdges(self) -> bool: 
        """
        Returns true if mesh edges should be drawn (false by default).
        """
    def ToDrawSilhouette(self) -> bool: 
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by default.
        """
    def ToMapTexture(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def ToSkipFirstEdge(self) -> bool: 
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default. Graphics hardware works mostly with triangles, so that wireframe presentation will draw triangle edges by default. This flag allows rendering wireframe presentation of quad-only array split into triangles. For this, quads should be split in specific order, so that the quad diagonal (to be NOT rendered) goes first: 1------2 / / Triangle #1: 2-0-1; Triangle #2: 0-2-3 0------3
        """
    def ToSuppressBackFaces(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theColor : OCP.Quantity.Quantity_Color,theFont : str,theExpansionFactor : float,theSpace : float,theStyle : OCP.Aspect.Aspect_TypeOfStyleText=Aspect_TypeOfStyleText.Aspect_TOST_NORMAL,theDisplayType : OCP.Aspect.Aspect_TypeOfDisplayText=Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL) -> None: ...
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
class Graphic3d_AspectFillArea3d(Graphic3d_Aspects, OCP.Standard.Standard_Transient):
    """
    This class defines graphic attributes for opaque 3d primitives (polygons, triangles, quadrilaterals).This class defines graphic attributes for opaque 3d primitives (polygons, triangles, quadrilaterals).
    """
    def AllowBackFace(self) -> None: 
        """
        Allows the display of back-facing filled polygons.
        """
    def AlphaCutoff(self) -> float: 
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode (0.5 by default). If the alpha value is greater than or equal to this value then it is rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """
    def AlphaMode(self) -> Graphic3d_AlphaMode: 
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default, for backward compatibility).
        """
    def BackFace(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    def BackInteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return back interior color.
        """
    def BackInteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return back interior color.
        """
    def BackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of internal faces
        """
    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return the color.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color
        """
    def ColorSubTitle(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return text background/shadow color; equals to EdgeColor() property.
        """
    def ColorSubTitleRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns text background/shadow color; equals to EdgeColor() property.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Distinguish(self) -> bool: 
        """
        Returns true if material properties should be distinguished for back and front faces (false by default).
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Edge(self) -> bool: 
        """
        None
        """
    def EdgeColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color of edges.
        """
    def EdgeColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return color of edges.
        """
    def EdgeLineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return edges line type (same as LineType()).
        """
    def EdgeWidth(self) -> float: 
        """
        Return width for edges in pixels (same as LineWidth()).
        """
    def FrontMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns the surface material of external faces
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HatchStyle(self) -> Graphic3d_HatchStyle: 
        """
        Returns the hatch type used when InteriorStyle is IS_HATCH
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InteriorColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return interior color.
        """
    def InteriorColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Return interior color.
        """
    def InteriorStyle(self) -> OCP.Aspect.Aspect_InteriorStyle: 
        """
        Return interior rendering style; Aspect_IS_SOLID by default.
        """
    def IsEqual(self,theOther : Graphic3d_Aspects) -> bool: 
        """
        Check for equality with another aspects.
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
    def IsMarkerSprite(self) -> bool: 
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or generated).
        """
    def IsTextZoomable(self) -> bool: 
        """
        Returns TRUE when the Text Zoomable is on.
        """
    def LineType(self) -> OCP.Aspect.Aspect_TypeOfLine: 
        """
        Return line type; Aspect_TOL_SOLID by default.
        """
    def LineWidth(self) -> float: 
        """
        Return width for edges in pixels; 1.0 by default.
        """
    def MarkerImage(self) -> Graphic3d_MarkerImage: 
        """
        Returns marker's image texture. Could be null handle if marker aspect has been initialized as default type of marker.
        """
    def MarkerScale(self) -> float: 
        """
        Return marker scale factor; 1.0 by default.
        """
    def MarkerType(self) -> OCP.Aspect.Aspect_TypeOfMarker: 
        """
        Return marker type; Aspect_TOM_POINT by default.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Returns current polygon offsets settings.
        """
    def PolygonOffsets(self,theFactor : float,theUnits : float) -> Tuple[int]: 
        """
        Returns current polygon offsets settings.
        """
    def SetAlphaMode(self,theMode : Graphic3d_AlphaMode,theAlphaCutoff : float=0.5) -> None: 
        """
        Defines the way how alpha value should be treated.
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the interior of the back face

        Modifies the color of the interior of the back face
        """
    @overload
    def SetBackInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetBackMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of internal faces
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies text background/shadow color; equals to EdgeColor() property.

        Modifies text background/shadow color; equals to EdgeColor() property.
        """
    @overload
    def SetColorSubTitle(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetDistinguish(self,toDistinguish : bool) -> None: 
        """
        Set material distinction between front and back faces.
        """
    def SetDistinguishOff(self) -> None: 
        """
        Forbids material distinction between front and back faces.
        """
    def SetDistinguishOn(self) -> None: 
        """
        Allows material distinction between front and back faces.
        """
    def SetDrawEdges(self,theToDraw : bool) -> None: 
        """
        Set if mesh edges should be drawn or not.
        """
    def SetDrawSilhouette(self,theToDraw : bool) -> None: 
        """
        Enables/disables drawing silhouette (outline).
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: 
        """
        Modifies the color of the edge of the face

        Modifies the color of the edge of the face
        """
    @overload
    def SetEdgeColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: ...
    def SetEdgeLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the edge line type (same as SetLineType())
        """
    def SetEdgeOff(self) -> None: 
        """
        The edges of FillAreas are not drawn.
        """
    def SetEdgeOn(self) -> None: 
        """
        The edges of FillAreas are drawn.
        """
    def SetEdgeWidth(self,theWidth : float) -> None: 
        """
        Modifies the edge thickness (same as SetLineWidth())
        """
    def SetFrontMaterial(self,theMaterial : Graphic3d_MaterialAspect) -> None: 
        """
        Modifies the surface material of external faces
        """
    @overload
    def SetHatchStyle(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH

        Modifies the hatch type used when InteriorStyle is IS_HATCH
        """
    @overload
    def SetHatchStyle(self,theStyle : Graphic3d_HatchStyle) -> None: ...
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the color of the interior of the face

        Modifies the color of the interior of the face
        """
    @overload
    def SetInteriorColor(self,theColor : OCP.Quantity.Quantity_ColorRGBA) -> None: ...
    def SetInteriorStyle(self,theStyle : OCP.Aspect.Aspect_InteriorStyle) -> None: 
        """
        Modifies the interior type used for rendering
        """
    def SetLineType(self,theType : OCP.Aspect.Aspect_TypeOfLine) -> None: 
        """
        Modifies the line type
        """
    def SetLineWidth(self,theWidth : float) -> None: 
        """
        Modifies the line thickness Warning: Raises Standard_OutOfRange if the width is a negative value.
        """
    def SetMarkerImage(self,theImage : Graphic3d_MarkerImage) -> None: 
        """
        Set marker's image texture.
        """
    def SetMarkerScale(self,theScale : float) -> None: 
        """
        Modifies the scale factor. Marker type Aspect_TOM_POINT is not affected by the marker size scale factor. It is always the smallest displayable dot. Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """
    def SetMarkerType(self,theType : OCP.Aspect.Aspect_TypeOfMarker) -> None: 
        """
        Modifies the type of marker.
        """
    def SetPolygonOffset(self,theOffset : Graphic3d_PolygonOffset) -> None: 
        """
        Sets polygon offsets settings.
        """
    def SetPolygonOffsets(self,theMode : int,theFactor : float=1.0,theUnits : float=0.0) -> None: 
        """
        Sets up OpenGL polygon offsets mechanism. <aMode> parameter can contain various combinations of Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means that polygon offsets are not changed). If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits> arguments are used by graphic renderer to calculate a depth offset value:
        """
    def SetShaderProgram(self,theProgram : Graphic3d_ShaderProgram) -> None: 
        """
        Sets up OpenGL/GLSL shader program.
        """
    def SetShadingModel(self,theShadingModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets shading model
        """
    def SetSkipFirstEdge(self,theToSkipFirstEdge : bool) -> None: 
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into triangles.
        """
    def SetSuppressBackFaces(self,theToSuppress : bool) -> None: 
        """
        Assign back faces culling flag.
        """
    def SetTextAngle(self,theAngle : float) -> None: 
        """
        Turns usage of text rotated
        """
    def SetTextDisplayType(self,theType : OCP.Aspect.Aspect_TypeOfDisplayText) -> None: 
        """
        Sets display type.
        """
    def SetTextFont(self,theFont : OCP.TCollection.TCollection_HAsciiString) -> None: 
        """
        Modifies the font.
        """
    def SetTextFontAspect(self,theFontAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        Turns usage of Aspect text
        """
    def SetTextStyle(self,theStyle : OCP.Aspect.Aspect_TypeOfStyleText) -> None: 
        """
        Modifies the style of the text.
        """
    def SetTextZoomable(self,theFlag : bool) -> None: 
        """
        Turns usage of text zoomable on/off
        """
    def SetTextureMap(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Assign texture to be mapped. See also SetTextureMapOn() to actually activate texture mapping.
        """
    def SetTextureMapOff(self) -> None: 
        """
        Disable texture mapping.
        """
    @overload
    def SetTextureMapOn(self) -> None: 
        """
        Enable or disable texture mapping (has no effect if texture is not set).

        Enable texture mapping (has no effect if texture is not set).
        """
    @overload
    def SetTextureMapOn(self,theToMap : bool) -> None: ...
    def SetTextureSet(self,theTextures : Graphic3d_TextureSet) -> None: 
        """
        Setup texture array to be mapped.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns shading model; Graphic3d_TOSM_DEFAULT by default. Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """
    def SuppressBackFace(self) -> None: 
        """
        Suppress the display of back-facing filled polygons. A back-facing polygon is defined as a polygon whose vertices are in a clockwise order with respect to screen coordinates.
        """
    def TextAngle(self) -> float: 
        """
        Returns Angle of degree
        """
    def TextDisplayType(self) -> OCP.Aspect.Aspect_TypeOfDisplayText: 
        """
        Returns display type; Aspect_TODT_NORMAL by default.
        """
    def TextFont(self) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        Returns the font; NULL string by default.
        """
    def TextFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        Returns text FontAspect
        """
    def TextStyle(self) -> OCP.Aspect.Aspect_TypeOfStyleText: 
        """
        Returns the text style; Aspect_TOST_NORMAL by default.
        """
    def TextureMap(self) -> Graphic3d_TextureMap: 
        """
        Return texture to be mapped.
        """
    def TextureMapState(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def TextureSet(self) -> Graphic3d_TextureSet: 
        """
        Return texture array to be mapped.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToDrawEdges(self) -> bool: 
        """
        Returns true if mesh edges should be drawn (false by default).
        """
    def ToDrawSilhouette(self) -> bool: 
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by default.
        """
    def ToMapTexture(self) -> bool: 
        """
        Return true if texture mapping is enabled (false by default).
        """
    def ToSkipFirstEdge(self) -> bool: 
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default. Graphics hardware works mostly with triangles, so that wireframe presentation will draw triangle edges by default. This flag allows rendering wireframe presentation of quad-only array split into triangles. For this, quads should be split in specific order, so that the quad diagonal (to be NOT rendered) goes first: 1------2 / / Triangle #1: 2-0-1; Triangle #2: 0-2-3 0------3
        """
    def ToSuppressBackFaces(self) -> bool: 
        """
        Returns true if back faces should be suppressed (true by default).
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theInterior : OCP.Aspect.Aspect_InteriorStyle,theInteriorColor : OCP.Quantity.Quantity_Color,theEdgeColor : OCP.Quantity.Quantity_Color,theEdgeLineType : OCP.Aspect.Aspect_TypeOfLine,theEdgeWidth : float,theFrontMaterial : Graphic3d_MaterialAspect,theBackMaterial : Graphic3d_MaterialAspect) -> None: ...
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
class Graphic3d_Buffer(OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Buffer of vertex attributes.Buffer of vertex attributes.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def Attribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def AttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def AttributeOffset(self,theAttribIndex : int) -> int: 
        """
        Returns data offset to specified attribute
        """
    def AttributesArray(self) -> Graphic3d_Attribute: 
        """
        Returns array of attributes definitions
        """
    def ChangeAttribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def ChangeAttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def ChangeData(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
        """
    def Data(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
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
    def FindAttribute(self,theAttrib : Graphic3d_TypeOfAttribute) -> int: 
        """
        Find attribute index.
        """
    def Free(self) -> None: 
        """
        De-allocate buffer.
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
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Attribute,theNbAttribs : int) -> bool: 
        """
        Allocates new empty array

        Allocates new empty array
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Array1OfAttribute) -> bool: ...
    def Invalidate(self) -> None: 
        """
        Invalidate entire buffer.
        """
    def InvalidatedRange(self) -> Graphic3d_BufferRange: 
        """
        Return invalidated range; EMPTY by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterleaved(self) -> bool: 
        """
        Flag indicating that attributes in the buffer are interleaved; TRUE by default. Requires sub-classing for creating a non-interleaved buffer (advanced usage).
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsMutable(self) -> bool: 
        """
        Return TRUE if data can be invalidated; FALSE by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def NbMaxElements(self) -> int: 
        """
        Return number of initially allocated elements which can fit into this buffer, while NbElements can be overwritten to smaller value.
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self) -> None: 
        """
        Reset invalidated range. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def changeValue(self,theElem : int) -> int: 
        """
        Access specified element.
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
    def release(self) -> None: 
        """
        Release buffer.
        """
    def value(self,theElem : int) -> int: 
        """
        Access specified element.
        """
    @property
    def NbAttributes(self) -> int:
        """
        :type: int
        """
    @NbAttributes.setter
    def NbAttributes(self, arg0: int) -> None:
        pass
    @property
    def NbElements(self) -> int:
        """
        :type: int
        """
    @NbElements.setter
    def NbElements(self, arg0: int) -> None:
        pass
    @property
    def Stride(self) -> int:
        """
        :type: int
        """
    @Stride.setter
    def Stride(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_Attribute():
    """
    Vertex attribute definition.
    """
    def Stride(self) -> int: 
        """
        None
        """
    @staticmethod
    def Stride_s(theType : Graphic3d_TypeOfData) -> int: 
        """
        Returns size of attribute of specified data type
        """
    def __init__(self) -> None: ...
    @property
    def DataType(self) -> Graphic3d_TypeOfData:
        """
        :type: Graphic3d_TypeOfData
        """
    @DataType.setter
    def DataType(self, arg0: Graphic3d_TypeOfData) -> None:
        pass
    @property
    def Id(self) -> Graphic3d_TypeOfAttribute:
        """
        :type: Graphic3d_TypeOfAttribute
        """
    @Id.setter
    def Id(self, arg0: Graphic3d_TypeOfAttribute) -> None:
        pass
    pass
class Graphic3d_AxisAspect():
    """
    Class that stores style for one graduated trihedron axis such as colors, lengths and customization flags. It is used in Graphic3d_GraduatedTrihedron.
    """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Color of axis and values
        """
    def Name(self) -> OCP.TCollection.TCollection_ExtendedString: 
        """
        None
        """
    def NameColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def NameOffset(self) -> int: 
        """
        None
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets color of axis and values
        """
    def SetDrawName(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetDrawTickmarks(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetDrawValues(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetName(self,theName : OCP.TCollection.TCollection_ExtendedString) -> None: 
        """
        None
        """
    def SetNameColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetNameOffset(self,theValue : int) -> None: 
        """
        None
        """
    def SetTickmarksLength(self,theValue : int) -> None: 
        """
        None
        """
    def SetTickmarksNumber(self,theValue : int) -> None: 
        """
        None
        """
    def SetValuesOffset(self,theValue : int) -> None: 
        """
        None
        """
    def TickmarksLength(self) -> int: 
        """
        None
        """
    def TickmarksNumber(self) -> int: 
        """
        None
        """
    def ToDrawName(self) -> bool: 
        """
        None
        """
    def ToDrawTickmarks(self) -> bool: 
        """
        None
        """
    def ToDrawValues(self) -> bool: 
        """
        None
        """
    def ValuesOffset(self) -> int: 
        """
        None
        """
    def __init__(self,theName : OCP.TCollection.TCollection_ExtendedString=OCP.TCollection.TCollection_ExtendedString,theNameColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theValuesOffset : int=10,theNameOffset : int=30,theTickmarksNumber : int=5,theTickmarksLength : int=10,theToDrawName : bool=True,theToDrawValues : bool=True,theToDrawTickmarks : bool=True) -> None: ...
    pass
class Graphic3d_BSDF():
    """
    Describes material's BSDF (Bidirectional Scattering Distribution Function) used for physically-based rendering (in path tracing engine). BSDF is represented as weighted mixture of basic BRDFs/BTDFs (Bidirectional Reflectance (Transmittance) Distribution Functions).
    """
    @staticmethod
    def CreateDiffuse_s(theWeight : Graphic3d_Vec3) -> Graphic3d_BSDF: 
        """
        Creates BSDF describing diffuse (Lambertian) surface.
        """
    @staticmethod
    def CreateGlass_s(theWeight : Graphic3d_Vec3,theAbsorptionColor : Graphic3d_Vec3,theAbsorptionCoeff : float,theRefractionIndex : float) -> Graphic3d_BSDF: 
        """
        Creates BSDF describing glass-like object. Glass-like BSDF mixes refraction and reflection effects at grazing angles using physically-based Fresnel dielectric model.
        """
    @staticmethod
    def CreateMetallic_s(theWeight : Graphic3d_Vec3,theFresnel : Graphic3d_Fresnel,theRoughness : float) -> Graphic3d_BSDF: 
        """
        Creates BSDF describing polished metallic-like surface.
        """
    @staticmethod
    def CreateTransparent_s(theWeight : Graphic3d_Vec3,theAbsorptionColor : Graphic3d_Vec3,theAbsorptionCoeff : float) -> Graphic3d_BSDF: 
        """
        Creates BSDF describing transparent object. Transparent BSDF models simple transparency without refraction (the ray passes straight through the surface).
        """
    def Normalize(self) -> None: 
        """
        Normalizes BSDF components.
        """
    def __init__(self) -> None: ...
    @property
    def Absorption(self) -> Graphic3d_Vec4:
        """
        :type: Graphic3d_Vec4
        """
    @Absorption.setter
    def Absorption(self, arg0: Graphic3d_Vec4) -> None:
        pass
    @property
    def FresnelBase(self) -> Graphic3d_Fresnel:
        """
        :type: Graphic3d_Fresnel
        """
    @FresnelBase.setter
    def FresnelBase(self, arg0: Graphic3d_Fresnel) -> None:
        pass
    @property
    def FresnelCoat(self) -> Graphic3d_Fresnel:
        """
        :type: Graphic3d_Fresnel
        """
    @FresnelCoat.setter
    def FresnelCoat(self, arg0: Graphic3d_Fresnel) -> None:
        pass
    @property
    def Kc(self) -> Graphic3d_Vec4:
        """
        :type: Graphic3d_Vec4
        """
    @Kc.setter
    def Kc(self, arg0: Graphic3d_Vec4) -> None:
        pass
    @property
    def Kd(self) -> Graphic3d_Vec3:
        """
        :type: Graphic3d_Vec3
        """
    @Kd.setter
    def Kd(self, arg0: Graphic3d_Vec3) -> None:
        pass
    @property
    def Ks(self) -> Graphic3d_Vec4:
        """
        :type: Graphic3d_Vec4
        """
    @Ks.setter
    def Ks(self, arg0: Graphic3d_Vec4) -> None:
        pass
    @property
    def Kt(self) -> Graphic3d_Vec3:
        """
        :type: Graphic3d_Vec3
        """
    @Kt.setter
    def Kt(self, arg0: Graphic3d_Vec3) -> None:
        pass
    @property
    def Le(self) -> Graphic3d_Vec3:
        """
        :type: Graphic3d_Vec3
        """
    @Le.setter
    def Le(self, arg0: Graphic3d_Vec3) -> None:
        pass
    pass
class Graphic3d_BndBox3d():
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    """
    def Add(self,thePoint : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Appends new point to the bounding box.
        """
    def Area(self) -> float: 
        """
        Returns surface area of bounding box. If the box is degenerated into line, returns the perimeter instead.
        """
    def Center(self,theAxis : int) -> float: 
        """
        Returns center of bounding box along the given axis.
        """
    def Clear(self) -> None: 
        """
        Clears bounding box.
        """
    def Combine(self,theBox : Graphic3d_BndBox3d) -> None: 
        """
        Combines bounding box with another one.
        """
    @overload
    def Contains(self,theMinPoint : OCP.SelectMgr.SelectMgr_Vec3,theMaxPoint : OCP.SelectMgr.SelectMgr_Vec3,hasOverlap : bool) -> bool: 
        """
        Checks if the Box fully contains the other box.

        Checks if the Box is fully contains the other box.
        """
    @overload
    def Contains(self,theOther : Graphic3d_BndBox3d,hasOverlap : bool) -> bool: ...
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @overload
    def IsOut(self,theOther : Graphic3d_BndBox3d) -> bool: 
        """
        Checks if the Box is out of the other box.

        Checks if the Box is out of the other box defined by two points.

        Checks if the Point is out of the box.
        """
    @overload
    def IsOut(self,theMinPoint : OCP.SelectMgr.SelectMgr_Vec3,theMaxPoint : OCP.SelectMgr.SelectMgr_Vec3) -> bool: ...
    @overload
    def IsOut(self,thePoint : OCP.SelectMgr.SelectMgr_Vec3) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Is bounding box valid?
        """
    @overload
    def __init__(self,thePoint : OCP.SelectMgr.SelectMgr_Vec3) -> None: ...
    @overload
    def __init__(self,theBox : Graphic3d_BndBox3d) -> None: ...
    @overload
    def __init__(self,theMinPoint : OCP.SelectMgr.SelectMgr_Vec3,theMaxPoint : OCP.SelectMgr.SelectMgr_Vec3) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Graphic3d_BndBox4d():
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    """
    def Add(self,thePoint : Graphic3d_Vec4d) -> None: 
        """
        Appends new point to the bounding box.
        """
    def Area(self) -> float: 
        """
        Returns surface area of bounding box. If the box is degenerated into line, returns the perimeter instead.
        """
    def Center(self,theAxis : int) -> float: 
        """
        Returns center of bounding box along the given axis.
        """
    def Clear(self) -> None: 
        """
        Clears bounding box.
        """
    def Combine(self,theBox : Graphic3d_BndBox4d) -> None: 
        """
        Combines bounding box with another one.
        """
    @overload
    def Contains(self,theMinPoint : Graphic3d_Vec4d,theMaxPoint : Graphic3d_Vec4d,hasOverlap : bool) -> bool: 
        """
        Checks if the Box fully contains the other box.

        Checks if the Box is fully contains the other box.
        """
    @overload
    def Contains(self,theOther : Graphic3d_BndBox4d,hasOverlap : bool) -> bool: ...
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @overload
    def IsOut(self,theOther : Graphic3d_BndBox4d) -> bool: 
        """
        Checks if the Box is out of the other box.

        Checks if the Box is out of the other box defined by two points.

        Checks if the Point is out of the box.
        """
    @overload
    def IsOut(self,theMinPoint : Graphic3d_Vec4d,theMaxPoint : Graphic3d_Vec4d) -> bool: ...
    @overload
    def IsOut(self,thePoint : Graphic3d_Vec4d) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Is bounding box valid?
        """
    @overload
    def __init__(self,theBox : Graphic3d_BndBox4d) -> None: ...
    @overload
    def __init__(self,theMinPoint : Graphic3d_Vec4d,theMaxPoint : Graphic3d_Vec4d) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePoint : Graphic3d_Vec4d) -> None: ...
    pass
class Graphic3d_BndBox4f():
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    """
    def Add(self,thePoint : Graphic3d_Vec4) -> None: 
        """
        Appends new point to the bounding box.
        """
    def Area(self) -> float: 
        """
        Returns surface area of bounding box. If the box is degenerated into line, returns the perimeter instead.
        """
    def Center(self,theAxis : int) -> float: 
        """
        Returns center of bounding box along the given axis.
        """
    def Clear(self) -> None: 
        """
        Clears bounding box.
        """
    def Combine(self,theBox : Graphic3d_BndBox4f) -> None: 
        """
        Combines bounding box with another one.
        """
    @overload
    def Contains(self,theMinPoint : Graphic3d_Vec4,theMaxPoint : Graphic3d_Vec4,hasOverlap : bool) -> bool: 
        """
        Checks if the Box fully contains the other box.

        Checks if the Box is fully contains the other box.
        """
    @overload
    def Contains(self,theOther : Graphic3d_BndBox4f,hasOverlap : bool) -> bool: ...
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @overload
    def IsOut(self,theOther : Graphic3d_BndBox4f) -> bool: 
        """
        Checks if the Box is out of the other box.

        Checks if the Box is out of the other box defined by two points.

        Checks if the Point is out of the box.
        """
    @overload
    def IsOut(self,thePoint : Graphic3d_Vec4) -> bool: ...
    @overload
    def IsOut(self,theMinPoint : Graphic3d_Vec4,theMaxPoint : Graphic3d_Vec4) -> bool: ...
    def IsValid(self) -> bool: 
        """
        Is bounding box valid?
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBox : Graphic3d_BndBox4f) -> None: ...
    @overload
    def __init__(self,thePoint : Graphic3d_Vec4) -> None: ...
    @overload
    def __init__(self,theMinPoint : Graphic3d_Vec4,theMaxPoint : Graphic3d_Vec4) -> None: ...
    pass
class Graphic3d_BoundBuffer(OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Bounds buffer.Bounds buffer.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def ChangeData(self) -> int: 
        """
        Returns buffer data
        """
    def Data(self) -> int: 
        """
        Returns buffer data
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
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theNbBounds : int,theHasColors : bool) -> bool: 
        """
        Allocates new empty array
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
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
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
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
    def NbBounds(self) -> int:
        """
        :type: int
        """
    @NbBounds.setter
    def NbBounds(self, arg0: int) -> None:
        pass
    @property
    def NbMaxBounds(self) -> int:
        """
        :type: int
        """
    @NbMaxBounds.setter
    def NbMaxBounds(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_AttribBuffer(Graphic3d_Buffer, OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Buffer of vertex attributes. This class is intended for advanced usage allowing invalidation of entire buffer content or its sub-part.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def Attribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def AttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def AttributeOffset(self,theAttribIndex : int) -> int: 
        """
        Returns data offset to specified attribute
        """
    def AttributesArray(self) -> Graphic3d_Attribute: 
        """
        Returns array of attributes definitions
        """
    def ChangeAttribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def ChangeAttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def ChangeData(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
        """
    def Data(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
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
    def FindAttribute(self,theAttrib : Graphic3d_TypeOfAttribute) -> int: 
        """
        Find attribute index.
        """
    def Free(self) -> None: 
        """
        De-allocate buffer.
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
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Attribute,theNbAttribs : int) -> bool: 
        """
        Allocates new empty array

        Allocates new empty array
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Array1OfAttribute) -> bool: ...
    @overload
    def Invalidate(self,theAttributeIndex : int,theVertexLower : int,theVertexUpper : int) -> None: 
        """
        Invalidate the entire buffer data.

        Invalidate the entire attribute data.

        Invalidate attribute data within specified sub-range (starting from 0).

        Invalidate all attribute data within specified vertex sub-range (starting from 0).
        """
    @overload
    def Invalidate(self) -> None: ...
    @overload
    def Invalidate(self,theAttributeIndex : int) -> None: ...
    @overload
    def Invalidate(self,theVertexLower : int,theVertexUpper : int) -> None: ...
    def InvalidatedRange(self) -> Graphic3d_BufferRange: 
        """
        Return invalidated range.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterleaved(self) -> bool: 
        """
        Return TRUE for interleaved array; TRUE by default.
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsMutable(self) -> bool: 
        """
        Return TRUE if data can be invalidated; FALSE by default.
        """
    def NbMaxElements(self) -> int: 
        """
        Return number of initially allocated elements which can fit into this buffer, while NbElements can be overwritten to smaller value.
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def SetInterleaved(self,theIsInterleaved : bool) -> None: 
        """
        Setup interleaved/non-interleaved array. WARNING! Filling non-interleaved buffer should be implemented on user side without Graphic3d_Buffer auxiliary methods designed for interleaved data.
        """
    def SetMutable(self,theMutable : bool) -> None: 
        """
        Set if data can be invalidated.
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self) -> None: 
        """
        Reset invalidated range.
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def changeValue(self,theElem : int) -> int: 
        """
        Access specified element.
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
    def invalidate(self,theRange : Graphic3d_BufferRange) -> None: 
        """
        Invalidate specified sub-range of data (as byte offsets).
        """
    def release(self) -> None: 
        """
        Release buffer.
        """
    def value(self,theElem : int) -> int: 
        """
        Access specified element.
        """
    @property
    def NbAttributes(self) -> int:
        """
        :type: int
        """
    @NbAttributes.setter
    def NbAttributes(self, arg0: int) -> None:
        pass
    @property
    def NbElements(self) -> int:
        """
        :type: int
        """
    @NbElements.setter
    def NbElements(self, arg0: int) -> None:
        pass
    @property
    def Stride(self) -> int:
        """
        :type: int
        """
    @Stride.setter
    def Stride(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_BufferRange():
    """
    Range of values defined as Start + Length pair.
    """
    def Clear(self) -> None: 
        """
        Clear the range.
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if range is empty.
        """
    def Unite(self,theRange : Graphic3d_BufferRange) -> None: 
        """
        Add another range to this one.
        """
    def Upper(self) -> int: 
        """
        Return the Upper element within the range
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theStart : int,theLength : int) -> None: ...
    @property
    def Length(self) -> int:
        """
        :type: int
        """
    @Length.setter
    def Length(self, arg0: int) -> None:
        pass
    @property
    def Start(self) -> int:
        """
        :type: int
        """
    @Start.setter
    def Start(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_BufferType():
    """
    Define buffers available for dump

    Members:

      Graphic3d_BT_RGB

      Graphic3d_BT_RGBA

      Graphic3d_BT_Depth

      Graphic3d_BT_RGB_RayTraceHdrLeft
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_BT_Depth: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_Depth
    Graphic3d_BT_RGB: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGB
    Graphic3d_BT_RGBA: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGBA
    Graphic3d_BT_RGB_RayTraceHdrLeft: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGB_RayTraceHdrLeft
    __entries: dict # value = {'Graphic3d_BT_RGB': (Graphic3d_BufferType.Graphic3d_BT_RGB, None), 'Graphic3d_BT_RGBA': (Graphic3d_BufferType.Graphic3d_BT_RGBA, None), 'Graphic3d_BT_Depth': (Graphic3d_BufferType.Graphic3d_BT_Depth, None), 'Graphic3d_BT_RGB_RayTraceHdrLeft': (Graphic3d_BufferType.Graphic3d_BT_RGB_RayTraceHdrLeft, None)}
    __members__: dict # value = {'Graphic3d_BT_RGB': Graphic3d_BufferType.Graphic3d_BT_RGB, 'Graphic3d_BT_RGBA': Graphic3d_BufferType.Graphic3d_BT_RGBA, 'Graphic3d_BT_Depth': Graphic3d_BufferType.Graphic3d_BT_Depth, 'Graphic3d_BT_RGB_RayTraceHdrLeft': Graphic3d_BufferType.Graphic3d_BT_RGB_RayTraceHdrLeft}
    pass
class Graphic3d_CLight(OCP.Standard.Standard_Transient):
    """
    Generic light source definition. This class defines arbitrary light source - see Graphic3d_TypeOfLightSource enumeration. Some parameters are applicable only to particular light type; calling methods unrelated to current type will throw an exception.Generic light source definition. This class defines arbitrary light source - see Graphic3d_TypeOfLightSource enumeration. Some parameters are applicable only to particular light type; calling methods unrelated to current type will throw an exception.
    """
    def Angle(self) -> float: 
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """
    def Attenuation(self) -> Tuple[float, float]: 
        """
        Returns the attenuation factors.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the color of the light source; WHITE by default.
        """
    def Concentration(self) -> float: 
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default. This coefficient should be converted into spotlight exponent within [0.0, 128.0] range: The concentration factor determines the dispersion of the light on the surface, the default value (1.0) corresponds to a minimum of dispersion.
        """
    def ConstAttenuation(self) -> float: 
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    @overload
    def Direction(self) -> Tuple[float, float, float]: 
        """
        Returns direction of directional/spot light.

        Returns the theVx, theVy, theVz direction of the light source.
        """
    @overload
    def Direction(self) -> OCP.gp.gp_Dir: ...
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light resource identifier string
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def Headlight(self) -> bool: 
        """
        Alias for IsHeadlight().
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Intensity(self) -> float: 
        """
        Returns the intensity of light source; 1.0 by default.
        """
    def IsEnabled(self) -> bool: 
        """
        Check that the light source is turned on; TRUE by default. This flag affects all occurrences of light sources, where it was registered and activated; so that it is possible defining an active light in View which is actually in disabled state.
        """
    def IsHeadlight(self) -> bool: 
        """
        Returns true if the light is a headlight; FALSE by default. Headlight flag means that light position/direction are defined not in a World coordinate system, but relative to the camera orientation.
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
    def LinearAttenuation(self) -> float: 
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default. Distance attenuation factors of reducing positional/spot light intensity depending on the distance from its position:
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns light source name; empty string by default.
        """
    def PackedColor(self) -> Graphic3d_Vec4: 
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """
    def PackedDirection(self) -> Graphic3d_Vec4: 
        """
        Returns direction of directional/spot light.
        """
    def PackedParams(self) -> Graphic3d_Vec4: 
        """
        Packed light parameters.
        """
    @overload
    def Position(self) -> Tuple[float, float, float]: 
        """
        Returns location of positional/spot light.

        Returns location of positional/spot light; (0, 0, 0) by default.
        """
    @overload
    def Position(self) -> OCP.gp.gp_Pnt: ...
    def Revision(self) -> int: 
        """
        Returns modification counter
        """
    def SetAngle(self,theAngle : float) -> None: 
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """
    def SetAttenuation(self,theConstAttenuation : float,theLinearAttenuation : float) -> None: 
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be equal to 0.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Defines the color of a light source by giving the basic color.
        """
    def SetConcentration(self,theConcentration : float) -> None: 
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """
    @overload
    def SetDirection(self,theVx : float,theVy : float,theVz : float) -> None: 
        """
        Sets direction of directional/spot light.

        Sets direction of directional/spot light.
        """
    @overload
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> None: ...
    def SetEnabled(self,theIsOn : bool) -> None: 
        """
        Change enabled state of the light state. This call does not remove or deactivate light source in Views/Viewers; instead it turns it OFF so that it just have no effect.
        """
    def SetHeadlight(self,theValue : bool) -> None: 
        """
        Setup headlight flag.
        """
    def SetIntensity(self,theValue : float) -> None: 
        """
        Modifies the intensity of light source, which should be > 0.0.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets light source name.
        """
    @overload
    def SetPosition(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Setup location of positional/spot light.

        Setup location of positional/spot light.
        """
    @overload
    def SetPosition(self,thePosition : OCP.gp.gp_Pnt) -> None: ...
    def SetSmoothAngle(self,theValue : float) -> None: 
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range [0.0, M_PI/2].
        """
    def SetSmoothRadius(self,theValue : float) -> None: 
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """
    def Smoothness(self) -> float: 
        """
        Returns the smoothness of light source (either smoothing angle for directional light or smoothing radius in case of positional light); 0.0 by default.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfLightSource: 
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """
    def __init__(self,theType : Graphic3d_TypeOfLightSource) -> None: ...
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
class Graphic3d_CStructure(OCP.Standard.Standard_Transient):
    """
    Low-level graphic structure interfaceLow-level graphic structure interface
    """
    def BndBoxClipCheck(self) -> bool: 
        """
        Returns whether check of object's bounding box clipping is enabled before drawing of object; TRUE by default.
        """
    def BoundingBox(self) -> Graphic3d_BndBox3d: 
        """
        Returns bounding box of this presentation
        """
    def ChangeBoundingBox(self) -> Graphic3d_BndBox3d: 
        """
        Returns bounding box of this presentation without transformation matrix applied
        """
    def Clear(self) -> None: 
        """
        Clear graphic data
        """
    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: 
        """
        Returns associated clip planes
        """
    def Connect(self,theStructure : Graphic3d_CStructure) -> None: 
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
    def Disconnect(self,theStructure : Graphic3d_CStructure) -> None: 
        """
        Disconnect other structure to this one
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GraphicDriver(self) -> Graphic3d_GraphicDriver: 
        """
        Returns graphic driver created this structure
        """
    def GraphicHighlight(self,theStyle : Graphic3d_PresentationAttributes) -> None: 
        """
        Highlights structure with the given style
        """
    def GraphicUnhighlight(self) -> None: 
        """
        Unhighlights the structure and invalidates pointer to structure's highlight style
        """
    def Groups(self) -> Graphic3d_SequenceOfGroup: 
        """
        Returns graphic groups
        """
    def HighlightStyle(self) -> Graphic3d_PresentationAttributes: 
        """
        Returns valid handle to highlight style of the structure in case if highlight flag is set to true
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
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
    @overload
    def IsVisible(self) -> bool: 
        """
        Return structure visibility flag

        Return structure visibility considering both View Affinity and global visibility state.
        """
    @overload
    def IsVisible(self,theViewId : int) -> bool: ...
    def MarkAsNotCulled(self) -> None: 
        """
        Marks structure as overlapping the current view volume one. The method is called during traverse of BVH tree.
        """
    def NewGroup(self,theStruct : Graphic3d_Structure) -> Graphic3d_Group: 
        """
        Create new group within this structure
        """
    def OnVisibilityChanged(self) -> None: 
        """
        Update structure visibility state
        """
    def RemoveGroup(self,theGroup : Graphic3d_Group) -> None: 
        """
        Remove group from this structure
        """
    def SetBndBoxClipCheck(self,theBndBoxClipCheck : bool) -> None: 
        """
        Enable/disable check of object's bounding box clipping before drawing of object.
        """
    def SetClipPlanes(self,thePlanes : Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Pass clip planes to the associated graphic driver structure
        """
    def SetCulled(self,theIsCulled : bool) -> None: 
        """
        Marks structure as culled/not culled - note that IsAlwaysRendered() is ignored here!
        """
    def SetTransformPersistence(self,theTrsfPers : Graphic3d_TransformPers) -> None: 
        """
        Set transformation persistence.
        """
    def SetTransformation(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Assign transformation.
        """
    def SetZLayer(self,theLayerIndex : int) -> None: 
        """
        Set z layer ID to display the structure in specified layer
        """
    def ShadowLink(self,theManager : Graphic3d_StructureManager) -> Graphic3d_CStructure: 
        """
        Create shadow link to this structure
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TransformPersistence(self) -> Graphic3d_TransformPers: 
        """
        Return transformation persistence.
        """
    def Transformation(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return transformation.
        """
    def ZLayer(self) -> int: 
        """
        Get z layer ID
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
class Graphic3d_CTexture():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_DataStructureManager(OCP.Standard.Standard_Transient):
    """
    This class allows the definition of a manager to which the graphic objects are associated. It allows them to be globally manipulated. It defines the global attributes.This class allows the definition of a manager to which the graphic objects are associated. It allows them to be globally manipulated. It defines the global attributes.This class allows the definition of a manager to which the graphic objects are associated. It allows them to be globally manipulated. It defines the global attributes.
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
class Graphic3d_Camera(OCP.Standard.Standard_Transient):
    """
    Camera class provides object-oriented approach to setting up projection and orientation properties of 3D view.Camera class provides object-oriented approach to setting up projection and orientation properties of 3D view.
    """
    def Aspect(self) -> float: 
        """
        Get camera display ratio.
        """
    def AxialScale(self) -> OCP.gp.gp_XYZ: 
        """
        Get camera axial scale.
        """
    def Center(self) -> OCP.gp.gp_Pnt: 
        """
        Get Center of the camera, e.g. the point where camera looks at. This point is computed as Eye() translated along Direction() at Distance().
        """
    def ConvertProj2View(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Convert point from projection coordinate space to view coordinate space.
        """
    def ConvertView2Proj(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Convert point from view coordinate space to projection coordinate space.
        """
    def ConvertView2World(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Convert point from view coordinate space to world coordinates.
        """
    def ConvertWorld2View(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Convert point from world coordinate space to view coordinate space.
        """
    def Copy(self,theOther : Graphic3d_Camera) -> None: 
        """
        Copy properties of another camera.
        """
    def CopyMappingData(self,theOtherCamera : Graphic3d_Camera) -> None: 
        """
        Initialize mapping related parameters from other camera handle.
        """
    def CopyOrientationData(self,theOtherCamera : Graphic3d_Camera) -> None: 
        """
        Initialize orientation related parameters from other camera handle.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Direction(self) -> OCP.gp.gp_Dir: 
        """
        Get camera look direction.
        """
    def Distance(self) -> float: 
        """
        Get distance of Eye from camera Center.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Eye(self) -> OCP.gp.gp_Pnt: 
        """
        Get camera Eye position.
        """
    def FOVy(self) -> float: 
        """
        Get Field Of View (FOV) in y axis.
        """
    def Frustum(self,theLeft : OCP.gp.gp_Pln,theRight : OCP.gp.gp_Pln,theBottom : OCP.gp.gp_Pln,theTop : OCP.gp.gp_Pln,theNear : OCP.gp.gp_Pln,theFar : OCP.gp.gp_Pln) -> None: 
        """
        Calculate WCS frustum planes for the camera projection volume. Frustum is a convex volume determined by six planes directing inwards. The frustum planes are usually used as inputs for camera algorithms. Thus, if any changes to projection matrix calculation are necessary, the frustum planes calculation should be also touched.
        """
    def FrustumPoints(self,thePoints : Any) -> None: 
        """
        Fill array of current view frustum corners. The size of this array is equal to FrustumVerticesNB. The order of vertices is as defined in FrustumVert_* enumeration.
        """
    def GetIODType(self) -> Any: 
        """
        Get Intraocular distance definition type.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IOD(self) -> float: 
        """
        Get Intraocular distance value.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvalidateOrientation(self) -> None: 
        """
        Invalidate orientation matrix. The matrix will be updated on request.
        """
    def InvalidateProjection(self) -> None: 
        """
        Invalidate state of projection matrix. The matrix will be updated on request.
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
    def IsOrthographic(self) -> bool: 
        """
        Check that the camera projection is orthographic.
        """
    def IsStereo(self) -> bool: 
        """
        Check whether the camera projection is stereo. Please note that stereo rendering is now implemented with support of Quad buffering.
        """
    def MoveEyeTo(self,theEye : OCP.gp.gp_Pnt) -> None: 
        """
        Sets camera Eye position. Unlike SetEye(), this method only changes Eye point and preserves camera direction.
        """
    def OrientationMatrix(self) -> Graphic3d_Mat4d: 
        """
        Get orientation matrix.
        """
    def OrientationMatrixF(self) -> Graphic3d_Mat4: 
        """
        Get orientation matrix of Standard_ShortReal precision.
        """
    def OrthogonalizeUp(self) -> None: 
        """
        Orthogonalize up direction vector.
        """
    def OrthogonalizedUp(self) -> OCP.gp.gp_Dir: 
        """
        Return a copy of orthogonalized up direction vector.
        """
    def Project(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Project point from world coordinate space to normalized device coordinates (mapping).
        """
    def ProjectionMatrix(self) -> Graphic3d_Mat4d: 
        """
        Get monographic or middle point projection matrix used for monographic rendering and for point projection / unprojection.
        """
    def ProjectionMatrixF(self) -> Graphic3d_Mat4: 
        """
        Get monographic or middle point projection matrix of Standard_ShortReal precision used for monographic rendering and for point projection / unprojection.
        """
    def ProjectionState(self) -> int: 
        """
        Returns modification state of camera projection matrix
        """
    def ProjectionStereoLeft(self) -> Graphic3d_Mat4d: 
        """
        Returns stereographic matrix computed for left eye. Please note that this method is used for rendering for Projection_Stereo.
        """
    def ProjectionStereoLeftF(self) -> Graphic3d_Mat4: 
        """
        Returns stereographic matrix of Standard_ShortReal precision computed for left eye. Please note that this method is used for rendering for Projection_Stereo.
        """
    def ProjectionStereoRight(self) -> Graphic3d_Mat4d: 
        """
        Returns stereographic matrix computed for right eye. Please note that this method is used for rendering for Projection_Stereo.
        """
    def ProjectionStereoRightF(self) -> Graphic3d_Mat4: 
        """
        Returns stereographic matrix of Standard_ShortReal precision computed for right eye. Please note that this method is used for rendering for Projection_Stereo.
        """
    def ProjectionType(self) -> Any: 
        """
        Returns camera projection type.
        """
    def Scale(self) -> float: 
        """
        Get camera scale.
        """
    def SetAspect(self,theAspect : float) -> None: 
        """
        Changes width / height display ratio.
        """
    def SetAxialScale(self,theAxialScale : OCP.gp.gp_XYZ) -> None: 
        """
        Set camera axial scale.
        """
    def SetCenter(self,theCenter : OCP.gp.gp_Pnt) -> None: 
        """
        Sets Center of the camera, e.g. the point where camera looks at. This methods changes camera direction, so that the new direction is computed from current Eye position to specified Center position.
        """
    def SetDirection(self,theDir : OCP.gp.gp_Dir) -> None: 
        """
        Sets camera look direction and computes the new Eye position relative to current Center. WARNING! This method does NOT verify that the current Up() vector is orthogonal to the new Direction.
        """
    def SetDirectionFromEye(self,theDir : OCP.gp.gp_Dir) -> None: 
        """
        Sets camera look direction preserving the current Eye() position. WARNING! This method does NOT verify that the current Up() vector is orthogonal to the new Direction.
        """
    def SetDistance(self,theDistance : float) -> None: 
        """
        Set distance of Eye from camera Center.
        """
    def SetEye(self,theEye : OCP.gp.gp_Pnt) -> None: 
        """
        Sets camera Eye position. WARNING! For backward compatibility reasons, this method also changes view direction, so that the new direction is computed from new Eye position to old Center position.
        """
    def SetEyeAndCenter(self,theEye : OCP.gp.gp_Pnt,theCenter : OCP.gp.gp_Pnt) -> None: 
        """
        Sets camera Eye and Center positions.
        """
    def SetFOVy(self,theFOVy : float) -> None: 
        """
        Set Field Of View (FOV) in y axis for perspective projection.
        """
    def SetIOD(self,theType : Any,theIOD : float) -> None: 
        """
        Sets Intraocular distance.
        """
    def SetProjectionType(self,theProjection : Any) -> None: 
        """
        Change camera projection type. When switching to perspective projection from orthographic one, the ZNear and ZFar are reset to default values (0.001, 3000.0) if less than 0.0.
        """
    def SetScale(self,theScale : float) -> None: 
        """
        Sets camera scale. For orthographic projection the scale factor corresponds to parallel scale of view mapping (i.e. size of viewport). For perspective camera scale is converted to distance. The scale specifies equal size of the view projection in both dimensions assuming that the aspect is 1.0. The projection height and width are specified with the scale and correspondingly multiplied by the aspect.
        """
    def SetTile(self,theTile : Graphic3d_CameraTile) -> None: 
        """
        Sets the Tile defining the drawing sub-area within View. Note that tile defining a region outside the view boundaries is also valid - use method Graphic3d_CameraTile::Cropped() to assign a cropped copy.
        """
    def SetUp(self,theUp : OCP.gp.gp_Dir) -> None: 
        """
        Sets camera Up direction vector, orthogonal to camera direction. WARNING! This method does NOT verify that the new Up vector is orthogonal to the current Direction().
        """
    def SetZFocus(self,theType : Any,theZFocus : float) -> None: 
        """
        Sets stereographic focus distance.
        """
    def SetZRange(self,theZNear : float,theZFar : float) -> None: 
        """
        Change the Near and Far Z-clipping plane positions. For orthographic projection, theZNear, theZFar can be negative or positive. For perspective projection, only positive values are allowed. Program error exception is raised if non-positive values are specified for perspective projection or theZNear >= theZFar.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Tile(self) -> Graphic3d_CameraTile: 
        """
        Get current tile.
        """
    def Transform(self,theTrsf : OCP.gp.gp_Trsf) -> None: 
        """
        Transform orientation components of the camera: Eye, Up and Center points.
        """
    def UnProject(self,thePnt : OCP.gp.gp_Pnt) -> OCP.gp.gp_Pnt: 
        """
        Unproject point from normalized device coordinates to world coordinate space.
        """
    def Up(self) -> OCP.gp.gp_Dir: 
        """
        Get camera Up direction vector.
        """
    @overload
    def ViewDimensions(self) -> OCP.gp.gp_XYZ: 
        """
        Calculate view plane size at center (target) point and distance between ZFar and ZNear planes.

        Calculate view plane size at center point with specified Z offset and distance between ZFar and ZNear planes.
        """
    @overload
    def ViewDimensions(self,theZValue : float) -> OCP.gp.gp_XYZ: ...
    def WorldViewProjState(self) -> Graphic3d_WorldViewProjState: 
        """
        Returns projection modification state of the camera.
        """
    def WorldViewState(self) -> int: 
        """
        Returns modification state of camera world view transformation matrix.
        """
    def ZFar(self) -> float: 
        """
        Get the Far Z-clipping plane position.
        """
    @overload
    def ZFitAll(self,theScaleFactor : float,theMinMax : OCP.Bnd.Bnd_Box,theGraphicBB : OCP.Bnd.Bnd_Box,theZNear : float,theZFar : float) -> bool: 
        """
        Estimate Z-min and Z-max planes of projection volume to match the displayed objects. The methods ensures that view volume will be close by depth range to the displayed objects. Fitting assumes that for orthogonal projection the view volume contains the displayed objects completely. For zoomed perspective view, the view volume is adjusted such that it contains the objects or their parts, located in front of the camera.

        Change Z-min and Z-max planes of projection volume to match the displayed objects.
        """
    @overload
    def ZFitAll(self,theScaleFactor : float,theMinMax : OCP.Bnd.Bnd_Box,theGraphicBB : OCP.Bnd.Bnd_Box) -> None: ...
    def ZFocus(self) -> float: 
        """
        Get stereographic focus value.
        """
    def ZFocusType(self) -> Any: 
        """
        Get stereographic focus definition type.
        """
    def ZNear(self) -> float: 
        """
        Get the Near Z-clipping plane position.
        """
    @overload
    def __init__(self,theOther : Graphic3d_Camera) -> None: ...
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
class Graphic3d_CameraLerp():
    """
    Simple linear interpolation tool (also known as mix() in GLSL). The main purpose of this template class is making interpolation routines more readable.
    """
    def Init(self,theStart : Graphic3d_Camera,theEnd : Graphic3d_Camera) -> None: 
        """
        Initialize values.
        """
    def Interpolate(self,theT : float,theResult : Graphic3d_Camera) -> None: 
        """
        Compute interpolated value between two values.
        """
    @staticmethod
    def Interpolate_s(theStart : Graphic3d_Camera,theEnd : Graphic3d_Camera,theT : float) -> Graphic3d_Camera: 
        """
        Compute interpolated value between two values.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theStart : Graphic3d_Camera,theEnd : Graphic3d_Camera) -> None: ...
    pass
class Graphic3d_CameraTile():
    """
    Class defines the area (Tile) inside a view.
    """
    def Cropped(self) -> Graphic3d_CameraTile: 
        """
        Return the copy cropped by total size
        """
    def IsValid(self) -> bool: 
        """
        Return true if Tile has been defined.
        """
    def OffsetLowerLeft(self) -> Graphic3d_Vec2i: 
        """
        Return offset position from lower-left corner.
        """
    def __init__(self) -> None: ...
    @property
    def Offset(self) -> Graphic3d_Vec2i:
        """
        :type: Graphic3d_Vec2i
        """
    @Offset.setter
    def Offset(self, arg0: Graphic3d_Vec2i) -> None:
        pass
    @property
    def TileSize(self) -> Graphic3d_Vec2i:
        """
        :type: Graphic3d_Vec2i
        """
    @TileSize.setter
    def TileSize(self, arg0: Graphic3d_Vec2i) -> None:
        pass
    @property
    def TotalSize(self) -> Graphic3d_Vec2i:
        """
        :type: Graphic3d_Vec2i
        """
    @TotalSize.setter
    def TotalSize(self, arg0: Graphic3d_Vec2i) -> None:
        pass
    pass
class Graphic3d_CappingFlags():
    """
    Enumeration of capping flags.

    Members:

      Graphic3d_CappingFlags_None

      Graphic3d_CappingFlags_ObjectMaterial

      Graphic3d_CappingFlags_ObjectTexture

      Graphic3d_CappingFlags_ObjectShader

      Graphic3d_CappingFlags_ObjectAspect
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_CappingFlags_None: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_None
    Graphic3d_CappingFlags_ObjectAspect: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectAspect
    Graphic3d_CappingFlags_ObjectMaterial: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectMaterial
    Graphic3d_CappingFlags_ObjectShader: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectShader
    Graphic3d_CappingFlags_ObjectTexture: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectTexture
    __entries: dict # value = {'Graphic3d_CappingFlags_None': (Graphic3d_CappingFlags.Graphic3d_CappingFlags_None, None), 'Graphic3d_CappingFlags_ObjectMaterial': (Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectMaterial, None), 'Graphic3d_CappingFlags_ObjectTexture': (Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectTexture, None), 'Graphic3d_CappingFlags_ObjectShader': (Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectShader, None), 'Graphic3d_CappingFlags_ObjectAspect': (Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectAspect, None)}
    __members__: dict # value = {'Graphic3d_CappingFlags_None': Graphic3d_CappingFlags.Graphic3d_CappingFlags_None, 'Graphic3d_CappingFlags_ObjectMaterial': Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectMaterial, 'Graphic3d_CappingFlags_ObjectTexture': Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectTexture, 'Graphic3d_CappingFlags_ObjectShader': Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectShader, 'Graphic3d_CappingFlags_ObjectAspect': Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectAspect}
    pass
class Graphic3d_ClipPlane(OCP.Standard.Standard_Transient):
    """
    Container for properties describing either a Clipping halfspace (single Clipping Plane), or a chain of Clipping Planes defining logical AND (conjunction) operation. The plane equation is specified in "world" coordinate system.Container for properties describing either a Clipping halfspace (single Clipping Plane), or a chain of Clipping Planes defining logical AND (conjunction) operation. The plane equation is specified in "world" coordinate system.
    """
    def CappingAspect(self) -> Graphic3d_AspectFillArea3d: 
        """
        Return capping aspect.
        """
    def CappingColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Return color for rendering capping surface.
        """
    def CappingCustomHatch(self) -> Graphic3d_HatchStyle: 
        """
        Returns hatching style.
        """
    def CappingHatch(self) -> OCP.Aspect.Aspect_HatchStyle: 
        """
        Returns hatching style.
        """
    def CappingMaterial(self) -> Graphic3d_MaterialAspect: 
        """
        Returns capping material.
        """
    def CappingTexture(self) -> Graphic3d_TextureMap: 
        """
        Returns capping texture map.
        """
    def ChainNextPlane(self) -> Graphic3d_ClipPlane: 
        """
        Return the next plane in a Chain of Planes defining logical AND operation, or NULL if there is no chain or it is a last element in chain.
        """
    def ChainPreviousPlane(self) -> Graphic3d_ClipPlane: 
        """
        Return the previous plane in a Chain of Planes defining logical AND operation, or NULL if there is no Chain or it is a first element in Chain. When clipping is defined by a Chain of Planes, it cuts a space only in case if check fails for all Planes in Chain.
        """
    def Clone(self) -> Graphic3d_ClipPlane: 
        """
        Clone plane. Virtual method to simplify copying procedure if plane class is redefined at application level to add specific fields to it e.g. id, name, etc.
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
    def GetEquation(self) -> Graphic3d_Vec4d: 
        """
        Get 4-component equation vector for clipping plane.
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID is used for managing associated resources in graphical driver. The clip plane can be assigned within a range of IO which can be displayed in separate OpenGl contexts. For each of the context an associated OpenGl resource for graphical aspects should be created and kept. The resources are stored in graphical driver for each of individual groups of shared context under the clip plane identifier.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsBoxFullInHalfspace(self,theBox : Graphic3d_BndBox3d) -> bool: 
        """
        Check if the given bounding box is fully inside (or touches from inside) the half-space (e.g. NOT discarded by clipping plane).
        """
    def IsBoxFullOutHalfspace(self,theBox : Graphic3d_BndBox3d) -> bool: 
        """
        Check if the given bounding box is fully outside of the half-space (e.g. should be discarded by clipping plane).
        """
    def IsCapping(self) -> bool: 
        """
        Check state of capping surface rendering.
        """
    def IsChain(self) -> bool: 
        """
        Return TRUE if this item defines a conjunction (logical AND) between a set of Planes. Graphic3d_ClipPlane item defines either a Clipping halfspace (single Clipping Plane) or a Clipping volume defined by a logical AND (conjunction) operation between a set of Planes defined as a Chain (so that the volume cuts a space only in case if check fails for ALL Planes in the Chain).
        """
    def IsHatchOn(self) -> bool: 
        """
        Returns True if hatching mask is turned on.
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
    def IsOn(self) -> bool: 
        """
        Check that the clipping plane is turned on.
        """
    def IsPointOutHalfspace(self,thePoint : Graphic3d_Vec4d) -> bool: 
        """
        Check if the given point is outside of the half-space (e.g. should be discarded by clipping plane).
        """
    def MCountAspect(self) -> int: 
        """
        Returns modification counter for aspect.
        """
    def MCountEquation(self) -> int: 
        """
        Returns modification counter for equation.
        """
    def NbChainNextPlanes(self) -> int: 
        """
        Return the number of chains in forward direction (including this item, so it is always >= 1). For a head of Chain - returns the length of entire Chain.
        """
    def ProbeBox(self,theBox : Graphic3d_BndBox3d) -> Graphic3d_ClipState: 
        """
        Check if the given bounding box is fully outside / fully inside.
        """
    def ProbeBoxHalfspace(self,theBox : Graphic3d_BndBox3d) -> Graphic3d_ClipState: 
        """
        Check if the given bounding box is fully outside / fully inside the half-space.
        """
    def ProbeBoxMaxPointHalfspace(self,theBox : Graphic3d_BndBox3d) -> Graphic3d_ClipState: 
        """
        Check if the given bounding box is fully outside of the half-space (e.g. should be discarded by clipping plane).
        """
    def ProbeBoxTouch(self,theBox : Graphic3d_BndBox3d) -> bool: 
        """
        Check if the given bounding box is In and touch the clipping planes
        """
    def ProbePoint(self,thePoint : Graphic3d_Vec4d) -> Graphic3d_ClipState: 
        """
        Check if the given point is outside / inside / on section.
        """
    def ProbePointHalfspace(self,thePoint : Graphic3d_Vec4d) -> Graphic3d_ClipState: 
        """
        Check if the given point is outside of the half-space (e.g. should be discarded by clipping plane).
        """
    def ReversedEquation(self) -> Graphic3d_Vec4d: 
        """
        Get 4-component equation vector for clipping plane.
        """
    def SetCapping(self,theIsOn : bool) -> None: 
        """
        Change state of capping surface rendering.
        """
    def SetCappingAspect(self,theAspect : Graphic3d_AspectFillArea3d) -> None: 
        """
        Assign capping aspect.
        """
    def SetCappingColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Set color for rendering capping surface.
        """
    def SetCappingCustomHatch(self,theStyle : Graphic3d_HatchStyle) -> None: 
        """
        Set custom hatch style (stipple) and turn hatching on.
        """
    def SetCappingHatch(self,theStyle : OCP.Aspect.Aspect_HatchStyle) -> None: 
        """
        Set hatch style (stipple) and turn hatching on.
        """
    def SetCappingHatchOff(self) -> None: 
        """
        Turn off hatching.
        """
    def SetCappingHatchOn(self) -> None: 
        """
        Turn on hatching.
        """
    def SetCappingMaterial(self,theMat : Graphic3d_MaterialAspect) -> None: 
        """
        Set material for rendering capping surface.
        """
    def SetCappingTexture(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Set texture to be applied on capping surface.
        """
    def SetChainNextPlane(self,thePlane : Graphic3d_ClipPlane) -> None: 
        """
        Set the next plane in a Chain of Planes. This operation also updates relationship between chains (Previous/Next items), so that the previously set Next plane is cut off.
        """
    @overload
    def SetEquation(self,theEquation : Graphic3d_Vec4d) -> None: 
        """
        Set plane equation by its geometrical definition. The equation is specified in "world" coordinate system.

        Set 4-component equation vector for clipping plane. The equation is specified in "world" coordinate system.
        """
    @overload
    def SetEquation(self,thePlane : OCP.gp.gp_Pln) -> None: ...
    def SetOn(self,theIsOn : bool) -> None: 
        """
        Change state of the clipping plane.
        """
    def SetUseObjectMaterial(self,theToUse : bool) -> None: 
        """
        Set flag for controlling the source of capping plane material.
        """
    def SetUseObjectShader(self,theToUse : bool) -> None: 
        """
        Set flag for controlling the source of capping plane shader program.
        """
    def SetUseObjectTexture(self,theToUse : bool) -> None: 
        """
        Set flag for controlling the source of capping plane texture.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToPlane(self) -> OCP.gp.gp_Pln: 
        """
        Get geometrical definition.
        """
    def ToUseObjectMaterial(self) -> bool: 
        """
        Flag indicating whether material for capping plane should be taken from object. Default value: FALSE (use dedicated capping plane material).
        """
    def ToUseObjectProperties(self) -> bool: 
        """
        Return true if some fill area aspect properties should be taken from object.
        """
    def ToUseObjectShader(self) -> bool: 
        """
        Flag indicating whether shader program for capping plane should be taken from object. Default value: FALSE.
        """
    def ToUseObjectTexture(self) -> bool: 
        """
        Flag indicating whether texture for capping plane should be taken from object. Default value: FALSE.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theEquation : Graphic3d_Vec4d) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_ClipPlane) -> None: ...
    @overload
    def __init__(self,thePlane : OCP.gp.gp_Pln) -> None: ...
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
class Graphic3d_ClipState():
    """
    Clipping state.

    Members:

      Graphic3d_ClipState_Out

      Graphic3d_ClipState_In

      Graphic3d_ClipState_On
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_ClipState_In: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_In
    Graphic3d_ClipState_On: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_On
    Graphic3d_ClipState_Out: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_Out
    __entries: dict # value = {'Graphic3d_ClipState_Out': (Graphic3d_ClipState.Graphic3d_ClipState_Out, None), 'Graphic3d_ClipState_In': (Graphic3d_ClipState.Graphic3d_ClipState_In, None), 'Graphic3d_ClipState_On': (Graphic3d_ClipState.Graphic3d_ClipState_On, None)}
    __members__: dict # value = {'Graphic3d_ClipState_Out': Graphic3d_ClipState.Graphic3d_ClipState_Out, 'Graphic3d_ClipState_In': Graphic3d_ClipState.Graphic3d_ClipState_In, 'Graphic3d_ClipState_On': Graphic3d_ClipState.Graphic3d_ClipState_On}
    pass
class Graphic3d_TextureRoot(OCP.Standard.Standard_Transient):
    """
    This is the texture root class enable the dialog with the GraphicDriver allows the loading of texture.This is the texture root class enable the dialog with the GraphicDriver allows the loading of texture.
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
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
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
class Graphic3d_CubeMapOrder():
    """
    Graphic3d_CubeMapOrder maps sides of cubemap on tiles in packed cubemap image to support different tiles order in such images. Also it can be considered as permutation of numbers from 0 to 5. It stores permutation in one integer as convolution.
    """
    def Clear(self) -> Graphic3d_CubeMapOrder: 
        """
        Makes order empty.
        """
    @staticmethod
    def Default_s() -> Graphic3d_ValidatedCubeMapOrder: 
        """
        Returns default order in protector container class. It is guaranteed to be valid.
        """
    def Get(self,theCubeMapSide : Graphic3d_CubeMapSide) -> int: 
        """
        Returns value of passed cubemap side.
        """
    def HasOverflows(self) -> bool: 
        """
        Checks whether attempts to assign index greater than 5 to any side happed.
        """
    def HasRepetitions(self) -> bool: 
        """
        Checks whether order has repetitions.
        """
    def IsEmpty(self) -> bool: 
        """
        Checks whether order is empty.
        """
    def IsValid(self) -> bool: 
        """
        Checks whether order is valid. Order is valid when it doesn't have repetitions and there were not attempts to assign indexes greater than 5.
        """
    def Permute(self,anOrder : Graphic3d_ValidatedCubeMapOrder) -> Graphic3d_CubeMapOrder: 
        """
        Applies another cubemap order as permutation for the current one.
        """
    def Permuted(self,anOrder : Graphic3d_ValidatedCubeMapOrder) -> Graphic3d_CubeMapOrder: 
        """
        Returns permuted by other cubemap order copy of current one.
        """
    @overload
    def Set(self,theOrder : Graphic3d_CubeMapOrder) -> Graphic3d_CubeMapOrder: 
        """
        Alias of 'operator='.

        Sets number of tile in packed cubemap image according passed cubemap side.
        """
    @overload
    def Set(self,theCubeMapSide : Graphic3d_CubeMapSide,theValue : int) -> Graphic3d_CubeMapOrder: ...
    def SetDefault(self) -> Graphic3d_CubeMapOrder: 
        """
        Sets default order (just from 0 to 5)
        """
    def Swap(self,theFirstSide : Graphic3d_CubeMapSide,theSecondSide : Graphic3d_CubeMapSide) -> Graphic3d_CubeMapOrder: 
        """
        Swaps values of two cubemap sides.
        """
    def Swapped(self,theFirstSide : Graphic3d_CubeMapSide,theSecondSide : Graphic3d_CubeMapSide) -> Graphic3d_CubeMapOrder: 
        """
        Returns copy of current order with swapped values of two cubemap sides.
        """
    def Validated(self) -> Graphic3d_ValidatedCubeMapOrder: 
        """
        Checks whether order is valid and returns object containing it. If order is invalid then exception will be thrown. This method is only way to create Graphic3d_ValidatedCubeMapOrder except copy constructor.
        """
    @overload
    def __init__(self,thePosXLocation : int,theNegXLocation : int,thePosYLocation : int,theNegYLocation : int,thePosZLocation : int,theNegZLocation : int) -> None: ...
    @overload
    def __init__(self,theOrder : Graphic3d_ValidatedCubeMapOrder) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Graphic3d_TextureMap(Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This is an abstract class for managing texture applyable on polygons.This is an abstract class for managing texture applyable on polygons.This is an abstract class for managing texture applyable on polygons.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
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
class Graphic3d_CubeMap(Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    Base class for cubemaps. It is iterator over cubemap sides.Base class for cubemaps. It is iterator over cubemap sides.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def CurrentSide(self) -> Graphic3d_CubeMapSide: 
        """
        Returns current cubemap side (iterator state).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def IsTopDown(self) -> bool: 
        """
        Returns whether row's memory layout is top-down.
        """
    def More(self) -> bool: 
        """
        Returns whether the iterator has reached the end (true if it hasn't).
        """
    def Next(self) -> None: 
        """
        Moves iterator to the next cubemap side. Uses OpenGL cubemap sides order +X -> -X -> +Y -> -Y -> +Z -> -Z.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Reset(self) -> Graphic3d_CubeMap: 
        """
        Sets iterator state to +X cubemap side.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetZInversion(self,theZIsInverted : bool) -> None: 
        """
        Sets Z axis inversion (vertical flipping).
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    def Value(self) -> OCP.Image.Image_PixMap: 
        """
        Returns PixMap containing current side of cubemap. Returns null handle if current side is invalid.
        """
    def ZIsInverted(self) -> bool: 
        """
        Returns whether Z axis is inverted.
        """
    @overload
    def __init__(self,thePixmap : OCP.Image.Image_PixMap=None) -> None: ...
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Graphic3d_CubeMapSide():
    """
    Sides of cubemap in order of OpenGL rules

    Members:

      Graphic3d_CMS_POS_X

      Graphic3d_CMS_NEG_X

      Graphic3d_CMS_POS_Y

      Graphic3d_CMS_NEG_Y

      Graphic3d_CMS_POS_Z

      Graphic3d_CMS_NEG_Z
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_CMS_NEG_X: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_X
    Graphic3d_CMS_NEG_Y: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Y
    Graphic3d_CMS_NEG_Z: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Z
    Graphic3d_CMS_POS_X: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_X
    Graphic3d_CMS_POS_Y: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Y
    Graphic3d_CMS_POS_Z: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Z
    __entries: dict # value = {'Graphic3d_CMS_POS_X': (Graphic3d_CubeMapSide.Graphic3d_CMS_POS_X, None), 'Graphic3d_CMS_NEG_X': (Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_X, None), 'Graphic3d_CMS_POS_Y': (Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Y, None), 'Graphic3d_CMS_NEG_Y': (Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Y, None), 'Graphic3d_CMS_POS_Z': (Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Z, None), 'Graphic3d_CMS_NEG_Z': (Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Z, None)}
    __members__: dict # value = {'Graphic3d_CMS_POS_X': Graphic3d_CubeMapSide.Graphic3d_CMS_POS_X, 'Graphic3d_CMS_NEG_X': Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_X, 'Graphic3d_CMS_POS_Y': Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Y, 'Graphic3d_CMS_NEG_Y': Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Y, 'Graphic3d_CMS_POS_Z': Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Z, 'Graphic3d_CMS_NEG_Z': Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Z}
    pass
class Graphic3d_CullingTool():
    """
    Graphic3d_CullingTool class provides a possibility to store parameters of view volume, such as its vertices and equations, and contains methods detecting if given AABB overlaps view volume.
    """
    def CacheClipPtsProjections(self) -> None: 
        """
        Caches view volume's vertices projections along its normals and AABBs dimensions. Must be called at the beginning of each BVH tree traverse loop.
        """
    def Camera(self) -> Graphic3d_Camera: 
        """
        Return the camera definition.
        """
    def IsCulled(self,theCtx : Any,theMinPt : OCP.SelectMgr.SelectMgr_Vec3,theMaxPt : OCP.SelectMgr.SelectMgr_Vec3) -> bool: 
        """
        Checks whether given AABB should be entirely culled or not.
        """
    def ProjectionMatrix(self) -> Graphic3d_Mat4d: 
        """
        Returns current projection matrix.
        """
    def SetCullingDistance(self,theCtx : Any,theDistance : float) -> None: 
        """
        Setup distance culling.
        """
    def SetCullingSize(self,theCtx : Any,theSize : float) -> None: 
        """
        Setup size culling.
        """
    def SetViewVolume(self,theCamera : Graphic3d_Camera) -> None: 
        """
        Retrieves view volume's planes equations and its vertices from projection and world-view matrices.
        """
    def SetViewportSize(self,theViewportWidth : int,theViewportHeight : int,theResolutionRatio : float) -> None: 
        """
        None
        """
    def ViewportHeight(self) -> int: 
        """
        None
        """
    def ViewportWidth(self) -> int: 
        """
        None
        """
    def WorldViewMatrix(self) -> Graphic3d_Mat4d: 
        """
        Returns current world view transformation matrix.
        """
    def WorldViewProjState(self) -> Graphic3d_WorldViewProjState: 
        """
        Returns state of current world view projection transformation matrices.
        """
    def __init__(self) -> None: ...
    pass
class Graphic3d_CView(Graphic3d_DataStructureManager, OCP.Standard.Standard_Transient):
    """
    Base class of a graphical view that carries out rendering process for a concrete implementation of graphical driver. Provides virtual interfaces for redrawing its contents, management of displayed structures and render settings. The source code of the class itself implements functionality related to management of computed (HLR or "view-dependent") structures.Base class of a graphical view that carries out rendering process for a concrete implementation of graphical driver. Provides virtual interfaces for redrawing its contents, management of displayed structures and render settings. The source code of the class itself implements functionality related to management of computed (HLR or "view-dependent") structures.Base class of a graphical view that carries out rendering process for a concrete implementation of graphical driver. Provides virtual interfaces for redrawing its contents, management of displayed structures and render settings. The source code of the class itself implements functionality related to management of computed (HLR or "view-dependent") structures.
    """
    def Activate(self) -> None: 
        """
        Activates the view. Maps presentations defined within structure manager onto this view.
        """
    def BackfacingModel(self) -> Graphic3d_TypeOfBackfacingModel: 
        """
        Return backfacing model used for the view.
        """
    def Background(self) -> OCP.Aspect.Aspect_Background: 
        """
        Returns background fill color.
        """
    def BackgroundCubeMap(self) -> Graphic3d_CubeMap: 
        """
        Returns cubemap being setted last time on background.
        """
    def BackgroundImage(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns background image texture file path.
        """
    def BackgroundImageStyle(self) -> OCP.Aspect.Aspect_FillMethod: 
        """
        Returns background image fill style.
        """
    def BufferDump(self,theImage : OCP.Image.Image_PixMap,theBufferType : Graphic3d_BufferType) -> bool: 
        """
        Dump active rendering buffer into specified memory buffer.
        """
    def Camera(self) -> Graphic3d_Camera: 
        """
        Returns camera object of the view.
        """
    def ChangeHiddenObjects(self) -> Any: 
        """
        Returns map of objects hidden within this specific view (not viewer-wise).
        """
    def ChangeRenderingParams(self) -> Graphic3d_RenderingParams: 
        """
        Returns reference to current rendering parameters and effect settings.
        """
    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: 
        """
        Returns list of clip planes set for the view.
        """
    def Compute(self) -> None: 
        """
        Computes the new presentation of the structures displayed in this view with the type Graphic3d_TOS_COMPUTED.
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
    def CopySettings(self,theOther : Graphic3d_CView) -> None: 
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
    def DiagnosticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : Graphic3d_DiagnosticInfo) -> None: 
        """
        Fill in the dictionary with diagnostic info. Should be called within rendering thread.
        """
    def DisplayedStructures(self,theStructures : Any) -> None: 
        """
        Returns the set of structures displayed in this view.
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
    def GetGraduatedTrihedron(self) -> Graphic3d_GraduatedTrihedron: 
        """
        Returns data of a graduated trihedron
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GradientBackground(self) -> OCP.Aspect.Aspect_GradientBackground: 
        """
        Returns gradient background fill colors.
        """
    def GraduatedTrihedronDisplay(self,theTrihedronData : Graphic3d_GraduatedTrihedron) -> None: 
        """
        Displays Graduated Trihedron.
        """
    def GraduatedTrihedronErase(self) -> None: 
        """
        Erases Graduated Trihedron.
        """
    def GraduatedTrihedronMinMaxValues(self,theMin : Graphic3d_Vec3,theMax : Graphic3d_Vec3) -> None: 
        """
        Sets minimum and maximum points of scene bounding box for Graduated Trihedron stored in graphic view object.
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
    def InsertLayerAfter(self,theNewLayerId : int,theSettings : Graphic3d_ZLayerSettings,theLayerBefore : int) -> None: 
        """
        Add a layer to the view.
        """
    def InsertLayerBefore(self,theNewLayerId : int,theSettings : Graphic3d_ZLayerSettings,theLayerAfter : int) -> None: 
        """
        Add a layer to the view.
        """
    def Invalidate(self) -> None: 
        """
        Invalidates content of the view but does not redraw it.
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
    def IsComputed(self,theStructId : int,theComputedStruct : Graphic3d_Structure) -> bool: 
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
    def Layer(self,theLayerId : int) -> Graphic3d_Layer: 
        """
        Returns layer with given ID or NULL if undefined.
        """
    def Layers(self) -> Any: 
        """
        Returns the list of layers.
        """
    def Lights(self) -> Graphic3d_LightSet: 
        """
        Returns list of lights of the view.
        """
    @overload
    def MinMaxValues(self,theToIncludeAuxiliary : bool=False) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the bounding box of all structures displayed in the view. If theToIncludeAuxiliary is TRUE, then the boundary box also includes minimum and maximum limits of graphical elements forming parts of infinite and other auxiliary structures.

        Returns the coordinates of the boundary box of all structures in the set <theSet>. If <theToIgnoreInfiniteFlag> is TRUE, then the boundary box also includes minimum and maximum limits of graphical elements forming parts of infinite structures.
        """
    @overload
    def MinMaxValues(self,theSet : Any,theToIncludeAuxiliary : bool=False) -> OCP.Bnd.Bnd_Box: ...
    def NumberOfDisplayedStructures(self) -> int: 
        """
        Returns number of displayed structures in the view.
        """
    def ReCompute(self,theStructure : Graphic3d_Structure) -> None: 
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
    def Remove(self) -> None: 
        """
        Erases the view and removes from graphic driver. No more graphic operations are allowed in this view after the call.
        """
    def RemoveZLayer(self,theLayerId : int) -> None: 
        """
        Remove Z layer from the specified view. All structures displayed at the moment in layer will be displayed in default layer ( the bottom-level z layer ). To unset layer ID from associated structures use method UnsetZLayer (...).
        """
    def RenderingParams(self) -> Graphic3d_RenderingParams: 
        """
        Returns current rendering parameters and effect settings.
        """
    def Resized(self) -> None: 
        """
        Handle changing size of the rendering window.
        """
    def SetBackfacingModel(self,theModel : Graphic3d_TypeOfBackfacingModel) -> None: 
        """
        Sets backfacing model for the view.
        """
    def SetBackground(self,theBackground : OCP.Aspect.Aspect_Background) -> None: 
        """
        Sets background fill color.
        """
    def SetBackgroundCubeMap(self,theCubeMap : Graphic3d_CubeMap) -> None: 
        """
        Sets environment cubemap as background.
        """
    def SetBackgroundImage(self,theFilePath : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets background image texture file path.
        """
    def SetBackgroundImageStyle(self,theFillStyle : OCP.Aspect.Aspect_FillMethod) -> None: 
        """
        Sets background image fill style.
        """
    def SetCamera(self,theCamera : Graphic3d_Camera) -> None: 
        """
        Sets camera used by the view.
        """
    def SetClipPlanes(self,thePlanes : Graphic3d_SequenceOfHClipPlane) -> None: 
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
    def SetLights(self,theLights : Graphic3d_LightSet) -> None: 
        """
        Sets list of lights for the view.
        """
    def SetShadingModel(self,theModel : Graphic3d_TypeOfShadingModel) -> None: 
        """
        Sets default Shading Model of the view. Will throw an exception on attempt to set Graphic3d_TOSM_DEFAULT.
        """
    def SetTextureEnv(self,theTextureEnv : Graphic3d_TextureEnv) -> None: 
        """
        Sets environment texture for the view.
        """
    def SetVisualizationType(self,theType : Graphic3d_TypeOfVisualization) -> None: 
        """
        Sets visualization type of the view.
        """
    def SetWindow(self,theWindow : OCP.Aspect.Aspect_Window,theContext : capsule=None) -> None: 
        """
        Creates and maps rendering window to the view.
        """
    def SetZLayerSettings(self,theLayerId : int,theSettings : Graphic3d_ZLayerSettings) -> None: 
        """
        Sets the settings for a single Z layer of specified view.
        """
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: 
        """
        Returns default Shading Model of the view; Graphic3d_TOSM_FRAGMENT by default.
        """
    @overload
    def StatisticInformation(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns string with statistic performance info.

        Fills in the dictionary with statistic performance info.
        """
    @overload
    def StatisticInformation(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString) -> None: ...
    def StructureManager(self) -> Graphic3d_StructureManager: 
        """
        Returns the structure manager handle which manage structures associated with this view.
        """
    def TextureEnv(self) -> Graphic3d_TextureEnv: 
        """
        Returns environment texture set for the view.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Update(self,theLayerId : int=-1) -> None: 
        """
        Invalidates bounding box of specified ZLayerId.
        """
    def VisualizationType(self) -> Graphic3d_TypeOfVisualization: 
        """
        Returns visualization type of the view.
        """
    def Window(self) -> OCP.Aspect.Aspect_Window: 
        """
        Returns the window associated to the view.
        """
    def ZLayerMax(self) -> int: 
        """
        Returns the maximum Z layer ID. First layer ID is Graphic3d_ZLayerId_Default, last ID is ZLayerMax().
        """
    def __init__(self,theMgr : Graphic3d_StructureManager) -> None: ...
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
class Graphic3d_DiagnosticInfo():
    """
    Diagnostic info categories bit flags.

    Members:

      Graphic3d_DiagnosticInfo_Device

      Graphic3d_DiagnosticInfo_FrameBuffer

      Graphic3d_DiagnosticInfo_Limits

      Graphic3d_DiagnosticInfo_Memory

      Graphic3d_DiagnosticInfo_NativePlatform

      Graphic3d_DiagnosticInfo_Extensions

      Graphic3d_DiagnosticInfo_Short

      Graphic3d_DiagnosticInfo_Basic

      Graphic3d_DiagnosticInfo_Complete
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_DiagnosticInfo_Basic: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Basic
    Graphic3d_DiagnosticInfo_Complete: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Complete
    Graphic3d_DiagnosticInfo_Device: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Device
    Graphic3d_DiagnosticInfo_Extensions: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Extensions
    Graphic3d_DiagnosticInfo_FrameBuffer: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_FrameBuffer
    Graphic3d_DiagnosticInfo_Limits: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Limits
    Graphic3d_DiagnosticInfo_Memory: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Memory
    Graphic3d_DiagnosticInfo_NativePlatform: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_NativePlatform
    Graphic3d_DiagnosticInfo_Short: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Short
    __entries: dict # value = {'Graphic3d_DiagnosticInfo_Device': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Device, None), 'Graphic3d_DiagnosticInfo_FrameBuffer': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_FrameBuffer, None), 'Graphic3d_DiagnosticInfo_Limits': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Limits, None), 'Graphic3d_DiagnosticInfo_Memory': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Memory, None), 'Graphic3d_DiagnosticInfo_NativePlatform': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_NativePlatform, None), 'Graphic3d_DiagnosticInfo_Extensions': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Extensions, None), 'Graphic3d_DiagnosticInfo_Short': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Short, None), 'Graphic3d_DiagnosticInfo_Basic': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Basic, None), 'Graphic3d_DiagnosticInfo_Complete': (Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Complete, None)}
    __members__: dict # value = {'Graphic3d_DiagnosticInfo_Device': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Device, 'Graphic3d_DiagnosticInfo_FrameBuffer': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_FrameBuffer, 'Graphic3d_DiagnosticInfo_Limits': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Limits, 'Graphic3d_DiagnosticInfo_Memory': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Memory, 'Graphic3d_DiagnosticInfo_NativePlatform': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_NativePlatform, 'Graphic3d_DiagnosticInfo_Extensions': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Extensions, 'Graphic3d_DiagnosticInfo_Short': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Short, 'Graphic3d_DiagnosticInfo_Basic': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Basic, 'Graphic3d_DiagnosticInfo_Complete': Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Complete}
    pass
class Graphic3d_FrameStats(OCP.Standard.Standard_Transient):
    """
    Class storing the frame statistics.
    """
    def ActiveDataFrame(self) -> Graphic3d_FrameStatsDataTmp: 
        """
        Returns currently filling data frame for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def ChangeCounter(self,theCounter : Graphic3d_FrameStatsCounter) -> int: 
        """
        Returns value of specified counter for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def ChangeDataFrames(self) -> Any: 
        """
        Returns data frames.
        """
    def ChangeTimer(self,theTimer : Graphic3d_FrameStatsTimer) -> float: 
        """
        Returns value of specified timer for modification, should be called between ::FrameStart() and ::FrameEnd() calls.
        """
    def CounterValue(self,theCounter : Graphic3d_FrameStatsCounter) -> int: 
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
    def FormatStats(self,theDict : OCP.TColStd.TColStd_IndexedDataMapOfStringString,theFlags : Any) -> None: 
        """
        Returns formatted string.

        Fill in the dictionary with formatted statistic info.
        """
    @overload
    def FormatStats(self,theFlags : Any) -> OCP.TCollection.TCollection_AsciiString: ...
    def FrameDuration(self) -> float: 
        """
        Returns duration of the last frame in seconds.
        """
    def FrameEnd(self,theView : Graphic3d_CView,theIsImmediateOnly : bool) -> None: 
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
    def FrameStart(self,theView : Graphic3d_CView,theIsImmediateOnly : bool) -> None: 
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
    def LastDataFrame(self) -> Graphic3d_FrameStatsData: 
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
    def TimerValue(self,theTimer : Graphic3d_FrameStatsTimer) -> float: 
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
class Graphic3d_FrameStatsCounter():
    """
    Stats counter.

    Members:

      Graphic3d_FrameStatsCounter_NbLayers

      Graphic3d_FrameStatsCounter_NbLayersNotCulled

      Graphic3d_FrameStatsCounter_NbStructs

      Graphic3d_FrameStatsCounter_NbStructsNotCulled

      Graphic3d_FrameStatsCounter_NbGroupsNotCulled

      Graphic3d_FrameStatsCounter_NbElemsNotCulled

      Graphic3d_FrameStatsCounter_NbElemsFillNotCulled

      Graphic3d_FrameStatsCounter_NbElemsLineNotCulled

      Graphic3d_FrameStatsCounter_NbElemsPointNotCulled

      Graphic3d_FrameStatsCounter_NbElemsTextNotCulled

      Graphic3d_FrameStatsCounter_NbTrianglesNotCulled

      Graphic3d_FrameStatsCounter_NbPointsNotCulled

      Graphic3d_FrameStatsCounter_EstimatedBytesGeom

      Graphic3d_FrameStatsCounter_EstimatedBytesFbos

      Graphic3d_FrameStatsCounter_EstimatedBytesTextures
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_FrameStatsCounter_EstimatedBytesFbos: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesFbos
    Graphic3d_FrameStatsCounter_EstimatedBytesGeom: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesGeom
    Graphic3d_FrameStatsCounter_EstimatedBytesTextures: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesTextures
    Graphic3d_FrameStatsCounter_NbElemsFillNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsFillNotCulled
    Graphic3d_FrameStatsCounter_NbElemsLineNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsLineNotCulled
    Graphic3d_FrameStatsCounter_NbElemsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsNotCulled
    Graphic3d_FrameStatsCounter_NbElemsPointNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsPointNotCulled
    Graphic3d_FrameStatsCounter_NbElemsTextNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsTextNotCulled
    Graphic3d_FrameStatsCounter_NbGroupsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbGroupsNotCulled
    Graphic3d_FrameStatsCounter_NbLayers: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayers
    Graphic3d_FrameStatsCounter_NbLayersNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayersNotCulled
    Graphic3d_FrameStatsCounter_NbPointsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbPointsNotCulled
    Graphic3d_FrameStatsCounter_NbStructs: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructs
    Graphic3d_FrameStatsCounter_NbStructsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructsNotCulled
    Graphic3d_FrameStatsCounter_NbTrianglesNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbTrianglesNotCulled
    __entries: dict # value = {'Graphic3d_FrameStatsCounter_NbLayers': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayers, None), 'Graphic3d_FrameStatsCounter_NbLayersNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayersNotCulled, None), 'Graphic3d_FrameStatsCounter_NbStructs': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructs, None), 'Graphic3d_FrameStatsCounter_NbStructsNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructsNotCulled, None), 'Graphic3d_FrameStatsCounter_NbGroupsNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbGroupsNotCulled, None), 'Graphic3d_FrameStatsCounter_NbElemsNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsNotCulled, None), 'Graphic3d_FrameStatsCounter_NbElemsFillNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsFillNotCulled, None), 'Graphic3d_FrameStatsCounter_NbElemsLineNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsLineNotCulled, None), 'Graphic3d_FrameStatsCounter_NbElemsPointNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsPointNotCulled, None), 'Graphic3d_FrameStatsCounter_NbElemsTextNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsTextNotCulled, None), 'Graphic3d_FrameStatsCounter_NbTrianglesNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbTrianglesNotCulled, None), 'Graphic3d_FrameStatsCounter_NbPointsNotCulled': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbPointsNotCulled, None), 'Graphic3d_FrameStatsCounter_EstimatedBytesGeom': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesGeom, None), 'Graphic3d_FrameStatsCounter_EstimatedBytesFbos': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesFbos, None), 'Graphic3d_FrameStatsCounter_EstimatedBytesTextures': (Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesTextures, None)}
    __members__: dict # value = {'Graphic3d_FrameStatsCounter_NbLayers': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayers, 'Graphic3d_FrameStatsCounter_NbLayersNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayersNotCulled, 'Graphic3d_FrameStatsCounter_NbStructs': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructs, 'Graphic3d_FrameStatsCounter_NbStructsNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructsNotCulled, 'Graphic3d_FrameStatsCounter_NbGroupsNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbGroupsNotCulled, 'Graphic3d_FrameStatsCounter_NbElemsNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsNotCulled, 'Graphic3d_FrameStatsCounter_NbElemsFillNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsFillNotCulled, 'Graphic3d_FrameStatsCounter_NbElemsLineNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsLineNotCulled, 'Graphic3d_FrameStatsCounter_NbElemsPointNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsPointNotCulled, 'Graphic3d_FrameStatsCounter_NbElemsTextNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsTextNotCulled, 'Graphic3d_FrameStatsCounter_NbTrianglesNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbTrianglesNotCulled, 'Graphic3d_FrameStatsCounter_NbPointsNotCulled': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbPointsNotCulled, 'Graphic3d_FrameStatsCounter_EstimatedBytesGeom': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesGeom, 'Graphic3d_FrameStatsCounter_EstimatedBytesFbos': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesFbos, 'Graphic3d_FrameStatsCounter_EstimatedBytesTextures': Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesTextures}
    pass
class Graphic3d_FrameStatsData():
    """
    Data frame definition.
    """
    def CounterValue(self,theIndex : Graphic3d_FrameStatsCounter) -> int: 
        """
        Get counter value.
        """
    def FillMax(self,theOther : Graphic3d_FrameStatsData) -> None: 
        """
        Fill with maximum values.
        """
    def FrameRate(self) -> float: 
        """
        Returns FPS (frames per seconds, elapsed time). This number indicates an actual frame rate averaged for several frames within UpdateInterval() duration, basing on a real elapsed time between updates.
        """
    def FrameRateCpu(self) -> float: 
        """
        Returns CPU FPS (frames per seconds, CPU time). This number indicates a PREDICTED frame rate, basing on CPU elapsed time between updates and NOT real elapsed time (which might include periods of CPU inactivity). Number is expected to be greater then actual frame rate returned by FrameRate(). Values significantly greater actual frame rate indicate that rendering is limited by GPU performance (CPU is stalled in-between), while values around actual frame rate indicate rendering being limited by CPU performance (GPU is stalled in-between).
        """
    def Reset(self) -> None: 
        """
        Reset data.
        """
    def TimerValue(self,theIndex : Graphic3d_FrameStatsTimer) -> float: 
        """
        Get timer value.
        """
    def __init__(self) -> None: ...
    pass
class Graphic3d_FrameStatsDataTmp(Graphic3d_FrameStatsData):
    """
    Temporary data frame definition.
    """
    def ChangeCounterValue(self,theIndex : Graphic3d_FrameStatsCounter) -> int: 
        """
        Get counter value.
        """
    def ChangeTimer(self,theTimer : Graphic3d_FrameStatsTimer) -> OCP.OSD.OSD_Timer: 
        """
        Return a timer object for time measurements.
        """
    def ChangeTimerValue(self,theIndex : Graphic3d_FrameStatsTimer) -> float: 
        """
        Modify timer value.
        """
    def CounterValue(self,theIndex : Graphic3d_FrameStatsCounter) -> int: 
        """
        Get counter value.
        """
    def FillMax(self,theOther : Graphic3d_FrameStatsData) -> None: 
        """
        Fill with maximum values.
        """
    def FlushTimers(self,theNbFrames : int,theIsFinal : bool) -> None: 
        """
        Compute average data considering the amount of rendered frames.
        """
    def FrameRate(self) -> float: 
        """
        Returns FPS (frames per seconds, elapsed time). This number indicates an actual frame rate averaged for several frames within UpdateInterval() duration, basing on a real elapsed time between updates.
        """
    def FrameRateCpu(self) -> float: 
        """
        Returns CPU FPS (frames per seconds, CPU time). This number indicates a PREDICTED frame rate, basing on CPU elapsed time between updates and NOT real elapsed time (which might include periods of CPU inactivity). Number is expected to be greater then actual frame rate returned by FrameRate(). Values significantly greater actual frame rate indicate that rendering is limited by GPU performance (CPU is stalled in-between), while values around actual frame rate indicate rendering being limited by CPU performance (GPU is stalled in-between).
        """
    def Reset(self) -> None: 
        """
        Reset data.
        """
    def TimerValue(self,theIndex : Graphic3d_FrameStatsTimer) -> float: 
        """
        Get timer value.
        """
    def __init__(self) -> None: ...
    @property
    def ChangeFrameRate(self) -> float:
        """
        Returns FPS (frames per seconds, elapsed time).

        :type: float
        """
    @ChangeFrameRate.setter
    def ChangeFrameRate(self, arg1: float) -> None:
        """
        Returns FPS (frames per seconds, elapsed time).
        """
    @property
    def ChangeFrameRateCpu(self) -> float:
        """
        Returns CPU FPS (frames per seconds, CPU time).

        :type: float
        """
    @ChangeFrameRateCpu.setter
    def ChangeFrameRateCpu(self, arg1: float) -> None:
        """
        Returns CPU FPS (frames per seconds, CPU time).
        """
    pass
class Graphic3d_FrameStatsTimer():
    """
    Timers for collecting frame performance statistics.

    Members:

      Graphic3d_FrameStatsTimer_ElapsedFrame

      Graphic3d_FrameStatsTimer_CpuFrame

      Graphic3d_FrameStatsTimer_CpuCulling

      Graphic3d_FrameStatsTimer_CpuPicking

      Graphic3d_FrameStatsTimer_CpuDynamics
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_FrameStatsTimer_CpuCulling: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuCulling
    Graphic3d_FrameStatsTimer_CpuDynamics: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuDynamics
    Graphic3d_FrameStatsTimer_CpuFrame: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuFrame
    Graphic3d_FrameStatsTimer_CpuPicking: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuPicking
    Graphic3d_FrameStatsTimer_ElapsedFrame: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_ElapsedFrame
    __entries: dict # value = {'Graphic3d_FrameStatsTimer_ElapsedFrame': (Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_ElapsedFrame, None), 'Graphic3d_FrameStatsTimer_CpuFrame': (Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuFrame, None), 'Graphic3d_FrameStatsTimer_CpuCulling': (Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuCulling, None), 'Graphic3d_FrameStatsTimer_CpuPicking': (Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuPicking, None), 'Graphic3d_FrameStatsTimer_CpuDynamics': (Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuDynamics, None)}
    __members__: dict # value = {'Graphic3d_FrameStatsTimer_ElapsedFrame': Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_ElapsedFrame, 'Graphic3d_FrameStatsTimer_CpuFrame': Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuFrame, 'Graphic3d_FrameStatsTimer_CpuCulling': Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuCulling, 'Graphic3d_FrameStatsTimer_CpuPicking': Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuPicking, 'Graphic3d_FrameStatsTimer_CpuDynamics': Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuDynamics}
    pass
class Graphic3d_Fresnel():
    """
    Describes Fresnel reflectance parameters.
    """
    @staticmethod
    @overload
    def CreateConductor_s(theRefractionIndex : float,theAbsorptionIndex : float) -> Graphic3d_Fresnel: 
        """
        Creates Fresnel factor for physical-based conductor model.

        Creates Fresnel factor for physical-based conductor model (spectral version).
        """
    @staticmethod
    @overload
    def CreateConductor_s(theRefractionIndex : Graphic3d_Vec3,theAbsorptionIndex : Graphic3d_Vec3) -> Graphic3d_Fresnel: ...
    @staticmethod
    def CreateConstant_s(theReflection : float) -> Graphic3d_Fresnel: 
        """
        Creates Fresnel factor for constant reflection.
        """
    @staticmethod
    def CreateDielectric_s(theRefractionIndex : float) -> Graphic3d_Fresnel: 
        """
        Creates Fresnel factor for physical-based dielectric model.
        """
    @staticmethod
    def CreateSchlick_s(theSpecularColor : Graphic3d_Vec3) -> Graphic3d_Fresnel: 
        """
        Creates Schlick's approximation of Fresnel factor.
        """
    def FresnelType(self) -> Graphic3d_FresnelModel: 
        """
        Returns type of Fresnel.
        """
    def Serialize(self) -> Graphic3d_Vec4: 
        """
        Returns serialized representation of Fresnel factor.
        """
    def __init__(self) -> None: ...
    pass
class Graphic3d_FresnelModel():
    """
    Type of the Fresnel model.

    Members:

      Graphic3d_FM_SCHLICK

      Graphic3d_FM_CONSTANT

      Graphic3d_FM_CONDUCTOR

      Graphic3d_FM_DIELECTRIC
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_FM_CONDUCTOR: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_CONDUCTOR
    Graphic3d_FM_CONSTANT: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_CONSTANT
    Graphic3d_FM_DIELECTRIC: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_DIELECTRIC
    Graphic3d_FM_SCHLICK: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_SCHLICK
    __entries: dict # value = {'Graphic3d_FM_SCHLICK': (Graphic3d_FresnelModel.Graphic3d_FM_SCHLICK, None), 'Graphic3d_FM_CONSTANT': (Graphic3d_FresnelModel.Graphic3d_FM_CONSTANT, None), 'Graphic3d_FM_CONDUCTOR': (Graphic3d_FresnelModel.Graphic3d_FM_CONDUCTOR, None), 'Graphic3d_FM_DIELECTRIC': (Graphic3d_FresnelModel.Graphic3d_FM_DIELECTRIC, None)}
    __members__: dict # value = {'Graphic3d_FM_SCHLICK': Graphic3d_FresnelModel.Graphic3d_FM_SCHLICK, 'Graphic3d_FM_CONSTANT': Graphic3d_FresnelModel.Graphic3d_FM_CONSTANT, 'Graphic3d_FM_CONDUCTOR': Graphic3d_FresnelModel.Graphic3d_FM_CONDUCTOR, 'Graphic3d_FM_DIELECTRIC': Graphic3d_FresnelModel.Graphic3d_FM_DIELECTRIC}
    pass
class Graphic3d_GraduatedTrihedron():
    """
    Defines the class of a graduated trihedron. It contains main style parameters for implementation of graduated trihedron
    """
    def ArrowsLength(self) -> float: 
        """
        None
        """
    def AxisAspect(self,theIndex : int) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def ChangeAxisAspect(self,theIndex : int) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def ChangeXAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def ChangeYAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def ChangeZAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def GridColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        None
        """
    def NamesFont(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def NamesFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        None
        """
    def NamesSize(self) -> int: 
        """
        None
        """
    def SetArrowsLength(self,theValue : float) -> None: 
        """
        None
        """
    def SetDrawAxes(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetDrawGrid(self,theToDraw : bool) -> None: 
        """
        None
        """
    def SetGridColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        None
        """
    def SetNamesFont(self,theFont : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetNamesFontAspect(self,theAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        None
        """
    def SetNamesSize(self,theValue : int) -> None: 
        """
        None
        """
    def SetValuesFont(self,theFont : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        None
        """
    def SetValuesFontAspect(self,theAspect : OCP.Font.Font_FontAspect) -> None: 
        """
        None
        """
    def SetValuesSize(self,theValue : int) -> None: 
        """
        None
        """
    def ToDrawAxes(self) -> bool: 
        """
        None
        """
    def ToDrawGrid(self) -> bool: 
        """
        None
        """
    def ValuesFont(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ValuesFontAspect(self) -> OCP.Font.Font_FontAspect: 
        """
        None
        """
    def ValuesSize(self) -> int: 
        """
        None
        """
    def XAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def YAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def ZAxisAspect(self) -> Graphic3d_AxisAspect: 
        """
        None
        """
    def __init__(self,theNamesFont : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theNamesStyle : OCP.Font.Font_FontAspect=Font_FontAspect.Font_FontAspect_Bold,theNamesSize : int=12,theValuesFont : OCP.TCollection.TCollection_AsciiString=OCP.TCollection.TCollection_AsciiString,theValuesStyle : OCP.Font.Font_FontAspect=Font_FontAspect.Font_FontAspect_Regular,theValuesSize : int=12,theArrowsLength : float=30.0,theGridColor : OCP.Quantity.Quantity_Color=OCP.Quantity.Quantity_Color,theToDrawGrid : bool=True,theToDrawAxes : bool=True) -> None: ...
    pass
class Graphic3d_GraphicDriver(OCP.Standard.Standard_Transient):
    """
    This class allows the definition of a graphic driver for 3d interface (currently only OpenGl driver is used).This class allows the definition of a graphic driver for 3d interface (currently only OpenGl driver is used).This class allows the definition of a graphic driver for 3d interface (currently only OpenGl driver is used).
    """
    def CreateStructure(self,theManager : Graphic3d_StructureManager) -> Graphic3d_CStructure: 
        """
        Creates new empty graphic structure
        """
    def CreateView(self,theMgr : Graphic3d_StructureManager) -> Graphic3d_CView: 
        """
        Creates new view for this graphic driver.
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
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableVBO(self,status : bool) -> None: 
        """
        enables/disables usage of OpenGL vertex buffer arrays while drawing primitiev arrays
        """
    def GetDisplayConnection(self) -> OCP.Aspect.Aspect_DisplayConnection: 
        """
        returns Handle to display connection
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InquireLightLimit(self) -> int: 
        """
        Request maximum number of active light sources supported by driver and hardware.
        """
    def InquireLimit(self,theType : Graphic3d_TypeOfLimit) -> int: 
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
    def InsertLayerAfter(self,theNewLayerId : int,theSettings : Graphic3d_ZLayerSettings,theLayerBefore : int) -> None: 
        """
        Adds a layer to all views.
        """
    def InsertLayerBefore(self,theNewLayerId : int,theSettings : Graphic3d_ZLayerSettings,theLayerAfter : int) -> None: 
        """
        Adds a layer to all views. To add a structure to desired layer on display it is necessary to set the layer ID for the structure.
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
        Returns information about GPU memory usage.
        """
    def NewIdentification(self) -> int: 
        """
        Returns a new identification number for a new structure.
        """
    def RemoveIdentification(self,theId : int) -> None: 
        """
        Frees the identifier of a structure.
        """
    def RemoveStructure(self,theCStructure : Graphic3d_CStructure) -> Any: 
        """
        Removes structure from graphic driver and releases its resources.
        """
    def RemoveView(self,theView : Graphic3d_CView) -> None: 
        """
        Removes view from graphic driver and releases its resources.
        """
    def RemoveZLayer(self,theLayerId : int) -> None: 
        """
        Removes Z layer. All structures displayed at the moment in layer will be displayed in default layer (the bottom-level z layer). By default, there are always default bottom-level layer that can't be removed. The passed theLayerId should be not less than 0 (reserved for default layers that can not be removed).
        """
    def SetZLayerSettings(self,theLayerId : int,theSettings : Graphic3d_ZLayerSettings) -> None: 
        """
        Sets the settings for a single Z layer.
        """
    def TextSize(self,theView : Graphic3d_CView,theText : str,theHeight : float,theWidth : float,theAscent : float,theDescent : float) -> None: 
        """
        Computes text width.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ViewExists(self,theWindow : OCP.Aspect.Aspect_Window,theView : Graphic3d_CView) -> bool: 
        """
        Returns view associated with the window if it is exists and is activated. Returns Standard_True if the view associated to the window exists.
        """
    def ZLayerSettings(self,theLayerId : int) -> Graphic3d_ZLayerSettings: 
        """
        Returns the settings of a single Z layer.
        """
    def ZLayers(self,theLayerSeq : OCP.TColStd.TColStd_SequenceOfInteger) -> None: 
        """
        Returns list of Z layers defined for the graphical driver.
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
class Graphic3d_Group(OCP.Standard.Standard_Transient):
    """
    This class allows the definition of groups of primitives inside of graphic objects (presentations). A group contains the primitives and attributes for which the range is limited to this group. The primitives of a group can be globally suppressed.This class allows the definition of groups of primitives inside of graphic objects (presentations). A group contains the primitives and attributes for which the range is limited to this group. The primitives of a group can be globally suppressed.
    """
    @overload
    def AddPrimitiveArray(self,theType : Graphic3d_TypeOfPrimitiveArray,theIndices : Graphic3d_IndexBuffer,theAttribs : Graphic3d_Buffer,theBounds : Graphic3d_BoundBuffer,theToEvalMinMax : bool=True) -> None: 
        """
        Adds an array of primitives for display

        Adds an array of primitives for display
        """
    @overload
    def AddPrimitiveArray(self,thePrim : Graphic3d_ArrayOfPrimitives,theToEvalMinMax : bool=True) -> None: ...
    def AddText(self,theTextParams : Graphic3d_Text,theToEvalMinMax : bool=True) -> None: 
        """
        Adds a text for display
        """
    def Aspects(self) -> Graphic3d_Aspects: 
        """
        Return fill area aspect.
        """
    def BoundingBox(self) -> Graphic3d_BndBox4f: 
        """
        Returns boundary box of the group <me> without transformation applied,
        """
    def ChangeBoundingBox(self) -> Graphic3d_BndBox4f: 
        """
        Returns non-const boundary box of the group <me> without transformation applied,
        """
    def Clear(self,theUpdateStructureMgr : bool=True) -> None: 
        """
        Supress all primitives and attributes of <me>. To clear group without update in Graphic3d_StructureManager pass Standard_False as <theUpdateStructureMgr>. This used on context and viewer destruction, when the pointer to structure manager in Graphic3d_Structure could be already released (pointers are used here to avoid handle cross-reference);
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
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
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
    def Marker(self,thePoint : Graphic3d_Vertex,theToEvalMinMax : bool=True) -> None: 
        """
        Creates a primitive array with single marker using AddPrimitiveArray().
        """
    def MinMaxValues(self) -> Tuple[float, float, float, float, float, float]: 
        """
        Returns the coordinates of the boundary box of the group.
        """
    def Remove(self) -> None: 
        """
        Supress the group <me> in the structure. Warning: No more graphic operations in <me> after this call. Modifies the current modelling transform persistence (pan, zoom or rotate) Get the current modelling transform persistence (pan, zoom or rotate)
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
        sets the flipping to theIsEnabled state.
        """
    def SetGroupPrimitivesAspect(self,theAspect : Graphic3d_Aspects) -> None: 
        """
        Modifies the context for all the face primitives of the group.
        """
    def SetMinMaxValues(self,theXMin : float,theYMin : float,theZMin : float,theXMax : float,theYMax : float,theZMax : float) -> None: 
        """
        Sets the coordinates of the boundary box of the group.
        """
    def SetPrimitivesAspect(self,theAspect : Graphic3d_Aspects) -> None: 
        """
        Modifies the current context of the group to give another aspect for all the primitives created after this call in the group.
        """
    def SetStencilTestOptions(self,theIsEnabled : bool) -> None: 
        """
        sets the stencil test to theIsEnabled state;
        """
    def Structure(self) -> Graphic3d_Structure: 
        """
        Returns the structure containing the group <me>.
        """
    def SynchronizeAspects(self) -> None: 
        """
        Update presentation aspects after their modification.
        """
    @overload
    def Text(self,theText : OCP.TCollection.TCollection_ExtendedString,theOrientation : OCP.gp.gp_Ax2,theHeight : float,theAngle : float,theTp : Graphic3d_TextPath,theHTA : Graphic3d_HorizontalTextAlignment,theVTA : Graphic3d_VerticalTextAlignment,theToEvalMinMax : bool=True,theHasOwnAnchor : bool=True) -> None: 
        """
        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). AAngle : Orientation of the text (with respect to the horizontal).

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). The other attributes have the following default values: AAngle : PI / 2. ATp : TP_RIGHT AHta : HTA_LEFT AVta : VTA_BOTTOM

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). AAngle : Orientation of the text (with respect to the horizontal).

        Creates the string <AText> at position <APoint>. The 3D point of attachment is projected. The text is written in the plane of projection. The attributes are given with respect to the plane of projection. AHeight : Height of text. (Relative to the Normalized Projection Coordinates (NPC) Space). The other attributes have the following default values: AAngle : PI / 2. ATp : TP_RIGHT AHta : HTA_LEFT AVta : VTA_BOTTOM

        Creates the string <theText> at orientation <theOrientation> in 3D space.

        Creates the string <theText> at orientation <theOrientation> in 3D space.
        """
    @overload
    def Text(self,AText : OCP.TCollection.TCollection_ExtendedString,APoint : Graphic3d_Vertex,AHeight : float,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,AText : OCP.TCollection.TCollection_ExtendedString,APoint : Graphic3d_Vertex,AHeight : float,AAngle : float,ATp : Graphic3d_TextPath,AHta : Graphic3d_HorizontalTextAlignment,AVta : Graphic3d_VerticalTextAlignment,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,theTextUtf : str,theOrientation : OCP.gp.gp_Ax2,theHeight : float,theAngle : float,theTp : Graphic3d_TextPath,theHTA : Graphic3d_HorizontalTextAlignment,theVTA : Graphic3d_VerticalTextAlignment,theToEvalMinMax : bool=True,theHasOwnAnchor : bool=True) -> None: ...
    @overload
    def Text(self,AText : str,APoint : Graphic3d_Vertex,AHeight : float,AAngle : float,ATp : Graphic3d_TextPath,AHta : Graphic3d_HorizontalTextAlignment,AVta : Graphic3d_VerticalTextAlignment,EvalMinMax : bool=True) -> None: ...
    @overload
    def Text(self,AText : str,APoint : Graphic3d_Vertex,AHeight : float,EvalMinMax : bool=True) -> None: ...
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
class Graphic3d_GroupAspect():
    """
    Identifies primitives aspects defined per group. - ASPECT_LINE: aspect for line primitives; - ASPECT_TEXT: aspect for text primitives; - ASPECT_MARKER: aspect for marker primitives; - ASPECT_FILL_AREA: aspect for face primitives.

    Members:

      Graphic3d_ASPECT_LINE

      Graphic3d_ASPECT_TEXT

      Graphic3d_ASPECT_MARKER

      Graphic3d_ASPECT_FILL_AREA
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_ASPECT_FILL_AREA: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_FILL_AREA
    Graphic3d_ASPECT_LINE: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_LINE
    Graphic3d_ASPECT_MARKER: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_MARKER
    Graphic3d_ASPECT_TEXT: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_TEXT
    __entries: dict # value = {'Graphic3d_ASPECT_LINE': (Graphic3d_GroupAspect.Graphic3d_ASPECT_LINE, None), 'Graphic3d_ASPECT_TEXT': (Graphic3d_GroupAspect.Graphic3d_ASPECT_TEXT, None), 'Graphic3d_ASPECT_MARKER': (Graphic3d_GroupAspect.Graphic3d_ASPECT_MARKER, None), 'Graphic3d_ASPECT_FILL_AREA': (Graphic3d_GroupAspect.Graphic3d_ASPECT_FILL_AREA, None)}
    __members__: dict # value = {'Graphic3d_ASPECT_LINE': Graphic3d_GroupAspect.Graphic3d_ASPECT_LINE, 'Graphic3d_ASPECT_TEXT': Graphic3d_GroupAspect.Graphic3d_ASPECT_TEXT, 'Graphic3d_ASPECT_MARKER': Graphic3d_GroupAspect.Graphic3d_ASPECT_MARKER, 'Graphic3d_ASPECT_FILL_AREA': Graphic3d_GroupAspect.Graphic3d_ASPECT_FILL_AREA}
    pass
class Graphic3d_GroupDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Graphic3d', '__weakref__': <attribute '__weakref__' of 'Graphic3d_GroupDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Graphic3d_GroupDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Graphic3d_HatchStyle(OCP.Standard.Standard_Transient):
    """
    A class that provides an API to use standard OCCT hatch styles defined in Aspect_HatchStyle enum or to create custom styles from a user-defined bitmapA class that provides an API to use standard OCCT hatch styles defined in Aspect_HatchStyle enum or to create custom styles from a user-defined bitmap
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
    def HatchType(self) -> int: 
        """
        In case if predefined OCCT style is used, returns index in Aspect_HatchStyle enumeration. If the style is custom, returns unique index of the style
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
    def Pattern(self) -> int: 
        """
        Returns the pattern of custom hatch style
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,thePattern : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theType : OCP.Aspect.Aspect_HatchStyle) -> None: ...
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
class Graphic3d_HorizontalTextAlignment():
    """
    Defines the horizontal position of the text relative to its anchor.

    Members:

      Graphic3d_HTA_LEFT

      Graphic3d_HTA_CENTER

      Graphic3d_HTA_RIGHT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_HTA_CENTER: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_CENTER
    Graphic3d_HTA_LEFT: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT
    Graphic3d_HTA_RIGHT: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_RIGHT
    __entries: dict # value = {'Graphic3d_HTA_LEFT': (Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT, None), 'Graphic3d_HTA_CENTER': (Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_CENTER, None), 'Graphic3d_HTA_RIGHT': (Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_RIGHT, None)}
    __members__: dict # value = {'Graphic3d_HTA_LEFT': Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT, 'Graphic3d_HTA_CENTER': Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_CENTER, 'Graphic3d_HTA_RIGHT': Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_RIGHT}
    pass
class Graphic3d_IndexBuffer(Graphic3d_Buffer, OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Index buffer.Index buffer.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def Attribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def AttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def AttributeOffset(self,theAttribIndex : int) -> int: 
        """
        Returns data offset to specified attribute
        """
    def AttributesArray(self) -> Graphic3d_Attribute: 
        """
        Returns array of attributes definitions
        """
    def ChangeAttribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def ChangeAttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def ChangeData(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
        """
    def Data(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
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
    def FindAttribute(self,theAttrib : Graphic3d_TypeOfAttribute) -> int: 
        """
        Find attribute index.
        """
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,theIndex : int) -> int: 
        """
        Access index at specified position
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Attribute,theNbAttribs : int) -> bool: 
        """
        Allocates new empty array

        Allocates new empty array
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Array1OfAttribute) -> bool: ...
    def InitInt32(self,theNbElems : int) -> bool: 
        """
        Allocates new empty index array
        """
    def Invalidate(self) -> None: 
        """
        Invalidate entire buffer.
        """
    def InvalidatedRange(self) -> Graphic3d_BufferRange: 
        """
        Return invalidated range; EMPTY by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterleaved(self) -> bool: 
        """
        Flag indicating that attributes in the buffer are interleaved; TRUE by default. Requires sub-classing for creating a non-interleaved buffer (advanced usage).
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsMutable(self) -> bool: 
        """
        Return TRUE if data can be invalidated; FALSE by default. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def NbMaxElements(self) -> int: 
        """
        Return number of initially allocated elements which can fit into this buffer, while NbElements can be overwritten to smaller value.
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def SetIndex(self,theIndex : int,theValue : int) -> None: 
        """
        Change index at specified position
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self) -> None: 
        """
        Reset invalidated range. Requires sub-classing for creating a mutable buffer (advanced usage).
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def changeValue(self,theElem : int) -> int: 
        """
        Access specified element.
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
    def release(self) -> None: 
        """
        Release buffer.
        """
    def value(self,theElem : int) -> int: 
        """
        Access specified element.
        """
    @property
    def NbAttributes(self) -> int:
        """
        :type: int
        """
    @NbAttributes.setter
    def NbAttributes(self, arg0: int) -> None:
        pass
    @property
    def NbElements(self) -> int:
        """
        :type: int
        """
    @NbElements.setter
    def NbElements(self, arg0: int) -> None:
        pass
    @property
    def Stride(self) -> int:
        """
        :type: int
        """
    @Stride.setter
    def Stride(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_IndexedMapOfStructure(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: An indexed map is used to store keys and to bind an index to them. Each new key stored in the map gets an index. Index are incremented as keys are stored in the map. A key can be found by the index and an index by the key. No key but the last can be removed so the indices are in the range 1..Extent. See the class Map from NCollection for a discussion about the number of buckets.
    """
    def Add(self,theKey1 : Graphic3d_CStructure) -> int: 
        """
        Add
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Graphic3d_IndexedMapOfStructure) -> Graphic3d_IndexedMapOfStructure: 
        """
        Assign. This method does not change the internal allocator.
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def Contains(self,theKey1 : Graphic3d_CStructure) -> bool: 
        """
        Contains
        """
    def Exchange(self,theOther : Graphic3d_IndexedMapOfStructure) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    def FindIndex(self,theKey1 : Graphic3d_CStructure) -> int: 
        """
        FindIndex
        """
    def FindKey(self,theIndex : int) -> Graphic3d_CStructure: 
        """
        FindKey
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,theExtent : int) -> None: 
        """
        ReSize
        """
    def RemoveFromIndex(self,theIndex : int) -> None: 
        """
        Remove the key of the given index. Caution! The index of the last key can be changed.
        """
    def RemoveKey(self,theKey1 : Graphic3d_CStructure) -> bool: 
        """
        Remove the given key. Caution! The index of the last key can be changed.
        """
    def RemoveLast(self) -> None: 
        """
        RemoveLast
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def Substitute(self,theIndex : int,theKey1 : Graphic3d_CStructure) -> None: 
        """
        Substitute
        """
    def Swap(self,theIndex1 : int,theIndex2 : int) -> None: 
        """
        Swaps two elements with the given indices.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_IndexedMapOfStructure) -> None: ...
    pass
class Graphic3d_Layer(OCP.Standard.Standard_Transient):
    """
    Presentations list sorted within priorities.
    """
    def Add(self,theStruct : Graphic3d_CStructure,thePriority : int,isForChangePriority : bool=False) -> None: 
        """
        None
        """
    def Append(self,theOther : Graphic3d_Layer) -> bool: 
        """
        Append layer of acceptable type (with similar number of priorities or less). Returns Standard_False if the list can not be accepted.
        """
    def ArrayOfStructures(self) -> Graphic3d_ArrayOfIndexedMapOfStructure: 
        """
        Returns array of structures.
        """
    def BoundingBox(self,theViewId : int,theCamera : Graphic3d_Camera,theWindowWidth : int,theWindowHeight : int,theToIncludeAuxiliary : bool) -> OCP.Bnd.Bnd_Box: 
        """
        Returns layer bounding box.
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
    def FrustumCullingBVHBuilder(self) -> OCP.Select3D.Select3D_BVHBuilder3d: 
        """
        Returns BVH tree builder for frustom culling.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InvalidateBVHData(self) -> None: 
        """
        Marks BVH tree for given priority list as dirty and marks primitive set for rebuild.
        """
    def InvalidateBoundingBox(self) -> None: 
        """
        Marks cached bounding box as obsolete.
        """
    def IsCulled(self) -> bool: 
        """
        Returns TRUE if layer is empty or has been discarded entirely by culling test.
        """
    def IsImmediate(self) -> bool: 
        """
        Return true if layer was marked with immediate flag.
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
    def LayerId(self) -> int: 
        """
        Return layer id.
        """
    def LayerSettings(self) -> Graphic3d_ZLayerSettings: 
        """
        Returns settings of the layer object.
        """
    def NbOfTransformPersistenceObjects(self) -> int: 
        """
        Returns number of transform persistence objects.
        """
    def NbPriorities(self) -> int: 
        """
        Returns the number of available priority levels
        """
    def NbStructures(self) -> int: 
        """
        Returns the number of structures
        """
    def NbStructuresNotCulled(self) -> int: 
        """
        Number of NOT culled structures in the layer.
        """
    def NonCullableStructures(self) -> Graphic3d_IndexedMapOfStructure: 
        """
        Returns indexed map of always rendered structures.
        """
    def Remove(self,theStruct : Graphic3d_CStructure,thePriority : int,isForChangePriority : bool=False) -> bool: 
        """
        Remove structure and returns its priority, if the structure is not found, method returns negative value
        """
    def SetFrustumCullingBVHBuilder(self,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: 
        """
        Assigns BVH tree builder for frustom culling.
        """
    def SetLayerSettings(self,theSettings : Graphic3d_ZLayerSettings) -> None: 
        """
        Sets settings of the layer object.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateCulling(self,theViewId : int,theSelector : Graphic3d_CullingTool,theFrustumCullingState : Any) -> None: 
        """
        Update culling state - should be called before rendering. Traverses through BVH tree to determine which structures are in view volume.
        """
    def __init__(self,theId : int,theNbPriorities : int,theBuilder : OCP.Select3D.Select3D_BVHBuilder3d) -> None: ...
    def considerZoomPersistenceObjects(self,theViewId : int,theCamera : Graphic3d_Camera,theWindowWidth : int,theWindowHeight : int) -> float: 
        """
        Returns zoom-scale factor.
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
class Graphic3d_LevelOfTextureAnisotropy():
    """
    Level of anisotropy filter. Notice that actual quality depends on hardware capabilities!

    Members:

      Graphic3d_LOTA_OFF

      Graphic3d_LOTA_FAST

      Graphic3d_LOTA_MIDDLE

      Graphic3d_LOTA_QUALITY
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_LOTA_FAST: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_FAST
    Graphic3d_LOTA_MIDDLE: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_MIDDLE
    Graphic3d_LOTA_OFF: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_OFF
    Graphic3d_LOTA_QUALITY: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_QUALITY
    __entries: dict # value = {'Graphic3d_LOTA_OFF': (Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_OFF, None), 'Graphic3d_LOTA_FAST': (Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_FAST, None), 'Graphic3d_LOTA_MIDDLE': (Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_MIDDLE, None), 'Graphic3d_LOTA_QUALITY': (Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_QUALITY, None)}
    __members__: dict # value = {'Graphic3d_LOTA_OFF': Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_OFF, 'Graphic3d_LOTA_FAST': Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_FAST, 'Graphic3d_LOTA_MIDDLE': Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_MIDDLE, 'Graphic3d_LOTA_QUALITY': Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_QUALITY}
    pass
class Graphic3d_LightSet(OCP.Standard.Standard_Transient):
    """
    Class defining the set of light sources.Class defining the set of light sources.
    """
    def Add(self,theLight : Graphic3d_CLight) -> bool: 
        """
        Append new light source.
        """
    def AmbientColor(self) -> Graphic3d_Vec4: 
        """
        Returns cumulative ambient color, which is computed as sum of all enabled ambient light sources. Values are NOT clamped (can be greater than 1.0f) and alpha component is fixed to 1.0f.
        """
    def Contains(self,theLight : Graphic3d_CLight) -> bool: 
        """
        Return TRUE if light source is defined in this set.
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
    def Extent(self) -> int: 
        """
        Return number of light sources.
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
        Return TRUE if lights list is empty.
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
    def KeyEnabledLong(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a string defining a list of enabled light sources as concatenation of letters 'd' (Directional), 'p' (Point), 's' (Spot) depending on the type of light source in the list. Example: "dppp".
        """
    def KeyEnabledShort(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns a string defining a list of enabled light sources as concatenation of letters 'd' (Directional), 'p' (Point), 's' (Spot) depending on the type of light source in the list, specified only once. Example: "dp".
        """
    def Lower(self) -> int: 
        """
        Return lower light index.
        """
    def NbEnabled(self) -> int: 
        """
        Returns total amount of enabled lights EXCLUDING ambient.
        """
    def NbEnabledLightsOfType(self,theType : Graphic3d_TypeOfLightSource) -> int: 
        """
        Returns total amount of enabled lights of specified type.
        """
    def NbLightsOfType(self,theType : Graphic3d_TypeOfLightSource) -> int: 
        """
        Returns total amount of lights of specified type.
        """
    def Remove(self,theLight : Graphic3d_CLight) -> bool: 
        """
        Remove light source.
        """
    def Revision(self) -> int: 
        """
        Return light sources revision.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def UpdateRevision(self) -> int: 
        """
        Update light sources revision.
        """
    def Upper(self) -> int: 
        """
        Return upper light index.
        """
    def Value(self,theIndex : int) -> Graphic3d_CLight: 
        """
        Return the light source for specified index within range [Lower(), Upper()].
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
class Graphic3d_MapOfZLayerSettings(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Graphic3d_MapOfZLayerSettings) -> Graphic3d_MapOfZLayerSettings: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : Graphic3d_ZLayerSettings) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : Graphic3d_ZLayerSettings) -> Graphic3d_ZLayerSettings: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> Graphic3d_ZLayerSettings: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> Graphic3d_ZLayerSettings: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : Graphic3d_MapOfZLayerSettings) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int) -> Graphic3d_ZLayerSettings: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int,theValue : Graphic3d_ZLayerSettings) -> bool: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> Graphic3d_ZLayerSettings: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : Any) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_MapOfZLayerSettings) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class Graphic3d_MarkerImage(OCP.Standard.Standard_Transient):
    """
    This class is used to store bitmaps and images for markers rendering. It can convert bitmap texture stored in TColStd_HArray1OfByte to Image_PixMap and vice versa.This class is used to store bitmaps and images for markers rendering. It can convert bitmap texture stored in TColStd_HArray1OfByte to Image_PixMap and vice versa.
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
    def GetBitMapArray(self,theAlphaValue : float=0.5) -> OCP.TColStd.TColStd_HArray1OfByte: 
        """
        Returns marker image as array of bytes. If an instance of the class has been initialized with image, it will be converted to bitmap based on the parameter theAlphaValue.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        Returns marker image. If an instance of the class has been initialized with a bitmap, it will be converted to image.
        """
    def GetImageAlpha(self) -> OCP.Image.Image_PixMap: 
        """
        Returns image alpha as grayscale image. Note that if an instance of the class has been initialized with a bitmap or with grayscale image this method will return exactly the same image as GetImage()
        """
    def GetImageAlphaId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an unique ID. This ID will be used to manage resource in graphic driver.
        """
    def GetImageId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns an unique ID. This ID will be used to manage resource in graphic driver.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetTextureSize(self) -> Tuple[int, int]: 
        """
        Returns texture size
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
    def __init__(self,theImage : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theBitMap : OCP.TColStd.TColStd_HArray1OfByte,theWidth : int,theHeight : int) -> None: ...
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
class Graphic3d_Mat4():
    """
    Generic matrix of 4 x 4 elements. To be used in conjunction with NCollection_Vec4 entities. Originally introduced for 3D space projection and orientation operations.
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> float: 
        """
        Access element at the specified row and column.
        """
    @staticmethod
    def Cols_s() -> int: 
        """
        Get number of columns.
        """
    def GetColumn(self,theCol : int) -> Graphic3d_Vec4: 
        """
        Get vector of elements for the specified column.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def GetDiagonal(self) -> Graphic3d_Vec4: 
        """
        Get vector of diagonal elements.
        """
    def GetRow(self,theRow : int) -> Graphic3d_Vec4: 
        """
        Get vector of elements for the specified row.
        """
    def GetValue(self,theRow : int,theCol : int) -> float: 
        """
        Get element at the specified row and column.
        """
    def InitIdentity(self) -> None: 
        """
        Initialize the identity matrix.
        """
    def Inverted(self,theOutMx : Graphic3d_Mat4) -> bool: 
        """
        Compute inverted matrix.
        """
    def IsEqual(self,theOther : Graphic3d_Mat4) -> bool: 
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """
    def IsIdentity(self) -> bool: 
        """
        Checks the matrix for identity.
        """
    @staticmethod
    def Map_s(theData : float) -> Graphic3d_Mat4: 
        """
        Maps plain C array to matrix type.

        Maps plain C array to matrix type.
        """
    @overload
    def Multiplied(self,theMat : Graphic3d_Mat4) -> Graphic3d_Mat4: 
        """
        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def Multiplied(self,theFactor : float) -> Graphic3d_Mat4: ...
    @overload
    def Multiply(self,theMat : Graphic3d_Mat4) -> None: 
        """
        Compute matrix multiplication product: A * B.

        Compute matrix multiplication.

        Compute per-component multiplication.
        """
    @overload
    def Multiply(self,theMatA : Graphic3d_Mat4,theMatB : Graphic3d_Mat4) -> Graphic3d_Mat4: ...
    @overload
    def Multiply(self,theFactor : float) -> None: ...
    @staticmethod
    def Rows_s() -> int: 
        """
        Get number of rows.
        """
    @overload
    def SetColumn(self,theCol : int,theVec : Graphic3d_Vec4) -> None: 
        """
        Change first 3 column values by the passed vector.

        Set column values by the passed 4 element vector.
        """
    @overload
    def SetColumn(self,theCol : int,theVec : Graphic3d_Vec3) -> None: ...
    @overload
    def SetDiagonal(self,theVec : Graphic3d_Vec4) -> None: 
        """
        Change first 3 elements of the diagonal matrix.

        Set diagonal elements of the matrix by the passed vector.
        """
    @overload
    def SetDiagonal(self,theVec : Graphic3d_Vec3) -> None: ...
    @overload
    def SetRow(self,theRow : int,theVec : Graphic3d_Vec4) -> None: 
        """
        Change first 3 row values by the passed vector.

        Set row values by the passed 4 element vector.
        """
    @overload
    def SetRow(self,theRow : int,theVec : Graphic3d_Vec3) -> None: ...
    def SetValue(self,theRow : int,theCol : int,theValue : float) -> None: 
        """
        Set value for the element specified by row and columns.
        """
    def Translate(self,theVec : Graphic3d_Vec3) -> None: 
        """
        Translate the matrix on the passed vector.
        """
    def Transpose(self) -> None: 
        """
        Transpose the matrix.
        """
    def Transposed(self) -> Graphic3d_Mat4: 
        """
        Transpose the matrix.
        """
    @overload
    def __imul__(self,theMat : Graphic3d_Mat4) -> Graphic3d_Mat4: 
        """
        Multiply by the another matrix.

        Compute per-element multiplication.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Mat4: ...
    def __init__(self) -> None: ...
    @overload
    def __mul__(self,theFactor : float) -> Graphic3d_Mat4: 
        """
        Multiply by the vector (M * V).

        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def __mul__(self,theVec : Graphic3d_Vec4) -> Graphic3d_Vec4: ...
    @overload
    def __mul__(self,theMat : Graphic3d_Mat4) -> Graphic3d_Mat4: ...
    @overload
    def __rmul__(self,theVec : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Multiply by the vector (M * V).

        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def __rmul__(self,theMat : Graphic3d_Mat4) -> Graphic3d_Mat4: ...
    @overload
    def __rmul__(self,theFactor : float) -> Graphic3d_Mat4: ...
    pass
class Graphic3d_Mat4d():
    """
    Generic matrix of 4 x 4 elements. To be used in conjunction with NCollection_Vec4 entities. Originally introduced for 3D space projection and orientation operations.
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    def ChangeValue(self,theRow : int,theCol : int) -> float: 
        """
        Access element at the specified row and column.
        """
    @staticmethod
    def Cols_s() -> int: 
        """
        Get number of columns.
        """
    def GetColumn(self,theCol : int) -> Graphic3d_Vec4d: 
        """
        Get vector of elements for the specified column.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def GetDiagonal(self) -> Graphic3d_Vec4d: 
        """
        Get vector of diagonal elements.
        """
    def GetRow(self,theRow : int) -> Graphic3d_Vec4d: 
        """
        Get vector of elements for the specified row.
        """
    def GetValue(self,theRow : int,theCol : int) -> float: 
        """
        Get element at the specified row and column.
        """
    def InitIdentity(self) -> None: 
        """
        Initialize the identity matrix.
        """
    def Inverted(self,theOutMx : Graphic3d_Mat4d) -> bool: 
        """
        Compute inverted matrix.
        """
    def IsEqual(self,theOther : Graphic3d_Mat4d) -> bool: 
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """
    def IsIdentity(self) -> bool: 
        """
        Checks the matrix for identity.
        """
    @staticmethod
    def Map_s(theData : float) -> Graphic3d_Mat4d: 
        """
        Maps plain C array to matrix type.

        Maps plain C array to matrix type.
        """
    @overload
    def Multiplied(self,theMat : Graphic3d_Mat4d) -> Graphic3d_Mat4d: 
        """
        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def Multiplied(self,theFactor : float) -> Graphic3d_Mat4d: ...
    @overload
    def Multiply(self,theMat : Graphic3d_Mat4d) -> None: 
        """
        Compute matrix multiplication product: A * B.

        Compute matrix multiplication.

        Compute per-component multiplication.
        """
    @overload
    def Multiply(self,theFactor : float) -> None: ...
    @overload
    def Multiply(self,theMatA : Graphic3d_Mat4d,theMatB : Graphic3d_Mat4d) -> Graphic3d_Mat4d: ...
    @staticmethod
    def Rows_s() -> int: 
        """
        Get number of rows.
        """
    @overload
    def SetColumn(self,theCol : int,theVec : Graphic3d_Vec4d) -> None: 
        """
        Change first 3 column values by the passed vector.

        Set column values by the passed 4 element vector.
        """
    @overload
    def SetColumn(self,theCol : int,theVec : OCP.SelectMgr.SelectMgr_Vec3) -> None: ...
    @overload
    def SetDiagonal(self,theVec : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Change first 3 elements of the diagonal matrix.

        Set diagonal elements of the matrix by the passed vector.
        """
    @overload
    def SetDiagonal(self,theVec : Graphic3d_Vec4d) -> None: ...
    @overload
    def SetRow(self,theRow : int,theVec : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Change first 3 row values by the passed vector.

        Set row values by the passed 4 element vector.
        """
    @overload
    def SetRow(self,theRow : int,theVec : Graphic3d_Vec4d) -> None: ...
    def SetValue(self,theRow : int,theCol : int,theValue : float) -> None: 
        """
        Set value for the element specified by row and columns.
        """
    def Translate(self,theVec : OCP.SelectMgr.SelectMgr_Vec3) -> None: 
        """
        Translate the matrix on the passed vector.
        """
    def Transpose(self) -> None: 
        """
        Transpose the matrix.
        """
    def Transposed(self) -> Graphic3d_Mat4d: 
        """
        Transpose the matrix.
        """
    @overload
    def __imul__(self,theMat : Graphic3d_Mat4d) -> Graphic3d_Mat4d: 
        """
        Multiply by the another matrix.

        Compute per-element multiplication.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Mat4d: ...
    def __init__(self) -> None: ...
    @overload
    def __mul__(self,theVec : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Multiply by the vector (M * V).

        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def __mul__(self,theMat : Graphic3d_Mat4d) -> Graphic3d_Mat4d: ...
    @overload
    def __mul__(self,theFactor : float) -> Graphic3d_Mat4d: ...
    @overload
    def __rmul__(self,theVec : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Multiply by the vector (M * V).

        Compute matrix multiplication product.

        Compute per-element multiplication.
        """
    @overload
    def __rmul__(self,theFactor : float) -> Graphic3d_Mat4d: ...
    @overload
    def __rmul__(self,theMat : Graphic3d_Mat4d) -> Graphic3d_Mat4d: ...
    pass
class Graphic3d_MaterialAspect():
    """
    This class allows the definition of the type of a surface. Aspect attributes of a 3d face. Keywords: Material, FillArea, Shininess, Ambient, Color, Diffuse, Specular, Transparency, Emissive, ReflectionMode, BackFace, FrontFace, Reflection, Absorbtion
    """
    def Alpha(self) -> float: 
        """
        Returns the alpha coefficient of the surface (1.0 - Transparency); 1.0 means opaque.
        """
    def AmbientColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the ambient color of the surface.
        """
    def BSDF(self) -> Graphic3d_BSDF: 
        """
        Returns BSDF (bidirectional scattering distribution function).
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the diffuse color of the surface. WARNING! This method does NOT return color for Graphic3d_MATERIAL_ASPECT material (color is defined by Graphic3d_Aspects::InteriorColor()).
        """
    def DiffuseColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the diffuse color of the surface.
        """
    def EmissiveColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the emissive color of the surface.
        """
    def IncreaseShine(self,theDelta : float) -> None: 
        """
        Increases or decreases the luminosity.
        """
    def IsDifferent(self,theOther : Graphic3d_MaterialAspect) -> bool: 
        """
        Returns TRUE if this material differs from specified one.
        """
    def IsEqual(self,theOther : Graphic3d_MaterialAspect) -> bool: 
        """
        Returns TRUE if this material is identical to specified one.
        """
    @staticmethod
    @overload
    def MaterialFromName_s(theName : str,theMat : Graphic3d_NameOfMaterial) -> bool: 
        """
        Finds the material for specified name.

        Returns the material for specified name or Graphic3d_NOM_DEFAULT if name is unknown.
        """
    @staticmethod
    @overload
    def MaterialFromName_s(theName : str) -> Graphic3d_NameOfMaterial: ...
    def MaterialName(self) -> str: 
        """
        Returns the given name of this material. This might be:
        """
    @staticmethod
    def MaterialName_s(theRank : int) -> str: 
        """
        Returns the name of the predefined material of specified rank within range [1, NumberOfMaterials()].
        """
    @overload
    def MaterialType(self,theType : Graphic3d_TypeOfMaterial) -> bool: 
        """
        Returns material type.

        Returns TRUE if type of this material is equal to specified type.
        """
    @overload
    def MaterialType(self) -> Graphic3d_TypeOfMaterial: ...
    @staticmethod
    def MaterialType_s(theRank : int) -> Graphic3d_TypeOfMaterial: 
        """
        Returns the type of the predefined material of specified rank within range [1, NumberOfMaterials()].
        """
    def Name(self) -> Graphic3d_NameOfMaterial: 
        """
        Returns the material name (within predefined enumeration).
        """
    @staticmethod
    def NumberOfMaterials_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def ReflectionMode(self,theType : Graphic3d_TypeOfReflection) -> bool: 
        """
        Returns TRUE if the reflection mode is active, FALSE otherwise.
        """
    def RefractionIndex(self) -> float: 
        """
        Returns the refraction index of the material
        """
    def RequestedName(self) -> Graphic3d_NameOfMaterial: 
        """
        Returns the material name within predefined enumeration which has been requested (before modifications).
        """
    def Reset(self) -> None: 
        """
        Resets the material with the original values according to the material name but leave the current color values untouched for the material of type ASPECT.
        """
    def SetAlpha(self,theValue : float) -> None: 
        """
        Modifies the alpha coefficient of the surface, where 1.0 is opaque and 0.0 is fully transparent.
        """
    def SetAmbientColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the ambient color of the surface.
        """
    def SetBSDF(self,theBSDF : Graphic3d_BSDF) -> None: 
        """
        Modifies the BSDF (bidirectional scattering distribution function).
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the ambient and diffuse color of the surface. WARNING! Has no effect for Graphic3d_MATERIAL_ASPECT material (color should be set to Graphic3d_Aspects::SetInteriorColor()).
        """
    def SetDiffuseColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the diffuse color of the surface.
        """
    def SetEmissiveColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the emissive color of the surface.
        """
    def SetMaterialName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        The current material become a "UserDefined" material. Set the name of the "UserDefined" material.
        """
    def SetMaterialType(self,theType : Graphic3d_TypeOfMaterial) -> None: 
        """
        Set material type.
        """
    def SetReflectionModeOff(self,theType : Graphic3d_TypeOfReflection) -> None: 
        """
        Deactivates the reflective properties of the surface with specified reflection type.
        """
    def SetRefractionIndex(self,theValue : float) -> None: 
        """
        Modifies the refraction index of the material. Warning: Raises MaterialDefinitionError if given value is a lesser than 1.0.
        """
    def SetShininess(self,theValue : float) -> None: 
        """
        Modifies the luminosity of the surface. Warning: Raises MaterialDefinitionError if given value is a negative value or greater than 1.0.
        """
    def SetSpecularColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Modifies the specular color of the surface.
        """
    def SetTransparency(self,theValue : float) -> None: 
        """
        Modifies the transparency coefficient of the surface, where 0 is opaque and 1 is fully transparent. Transparency is applicable to materials that have at least one of reflection modes (ambient, diffuse, specular or emissive) enabled. See also SetReflectionModeOn() and SetReflectionModeOff() methods.
        """
    def Shininess(self) -> float: 
        """
        Returns the luminosity of the surface.
        """
    def SpecularColor(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns the specular color of the surface.
        """
    def StringName(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the given name of this material. This might be: - given name set by method ::SetMaterialName() - standard name for a material within enumeration - "UserDefined" for non-standard material without name specified externally.
        """
    def Transparency(self) -> float: 
        """
        Returns the transparency coefficient of the surface (1.0 - Alpha); 0.0 means opaque.
        """
    @overload
    def __init__(self,theName : Graphic3d_NameOfMaterial) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Graphic3d_MaterialDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Graphic3d', '__weakref__': <attribute '__weakref__' of 'Graphic3d_MaterialDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Graphic3d_MaterialDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Graphic3d_Texture2D(Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This abstract class for managing 2D texturesThis abstract class for managing 2D textures
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMipMaps(self) -> bool: 
        """
        Return true if mip-maps should be used.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture2D: 
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetImage(self,thePixMap : OCP.Image.Image_PixMap) -> None: 
        """
        Assign new image to the texture. Note that this method does not invalidate already uploaded resources - consider calling ::UpdateRevision() if needed.
        """
    def SetMipMaps(self,theToUse : bool) -> None: 
        """
        Set if mip-maps should be used (generated if needed). Note that this method should be called before loading / using the texture.
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
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
class Graphic3d_TextureSet(OCP.Standard.Standard_Transient):
    """
    Class holding array of textures to be mapped as a set.
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
    def First(self) -> Graphic3d_TextureMap: 
        """
        Return the first texture.
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
    def Lower(self) -> int: 
        """
        Return the lower index in texture set.
        """
    def SetFirst(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Return the first texture.
        """
    def SetValue(self,theIndex : int,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Return the texture at specified position within [0, Size()) range.
        """
    def Size(self) -> int: 
        """
        Return number of textures.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Return the upper index in texture set.
        """
    def Value(self,theIndex : int) -> Graphic3d_TextureMap: 
        """
        Return the texture at specified position within [0, Size()) range.
        """
    @overload
    def __init__(self,theNbTextures : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theTexture : Graphic3d_TextureMap) -> None: ...
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
class Graphic3d_MutableIndexBuffer(Graphic3d_IndexBuffer, Graphic3d_Buffer, OCP.NCollection.NCollection_Buffer, OCP.Standard.Standard_Transient):
    """
    Mutable index buffer.
    """
    def Allocate(self,theSize : int) -> bool: 
        """
        Allocate the buffer.
        """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns buffer allocator
        """
    def Attribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def AttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def AttributeOffset(self,theAttribIndex : int) -> int: 
        """
        Returns data offset to specified attribute
        """
    def AttributesArray(self) -> Graphic3d_Attribute: 
        """
        Returns array of attributes definitions
        """
    def ChangeAttribute(self,theAttribIndex : int) -> Graphic3d_Attribute: 
        """
        Returns attribute definition
        """
    def ChangeAttributeData(self,theAttrib : Graphic3d_TypeOfAttribute,theAttribIndex : int,theAttribStride : int) -> int: 
        """
        Return the attribute data with stride size specific to this attribute.
        """
    def ChangeData(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
        """
    def Data(self,theAttribIndex : int) -> int: 
        """
        Returns data for specified attribute
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
    def FindAttribute(self,theAttrib : Graphic3d_TypeOfAttribute) -> int: 
        """
        Find attribute index.
        """
    def Free(self) -> None: 
        """
        De-allocate buffer.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Index(self,theIndex : int) -> int: 
        """
        Access index at specified position
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Attribute,theNbAttribs : int) -> bool: 
        """
        Allocates new empty array

        Allocates new empty array
        """
    @overload
    def Init(self,theNbElems : int,theAttribs : Graphic3d_Array1OfAttribute) -> bool: ...
    def InitInt32(self,theNbElems : int) -> bool: 
        """
        Allocates new empty index array
        """
    @overload
    def Invalidate(self) -> None: 
        """
        Invalidate the entire buffer data.

        Invalidate the given indexes (starting from 0)
        """
    @overload
    def Invalidate(self,theIndexLower : int,theIndexUpper : int) -> None: ...
    def InvalidatedRange(self) -> Graphic3d_BufferRange: 
        """
        Return invalidated range.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns true if buffer is not allocated
        """
    @overload
    def IsInstance(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns a true value if this is an instance of Type.

        Returns a true value if this is an instance of TypeName.
        """
    @overload
    def IsInstance(self,theTypeName : str) -> bool: ...
    def IsInterleaved(self) -> bool: 
        """
        Flag indicating that attributes in the buffer are interleaved; TRUE by default. Requires sub-classing for creating a non-interleaved buffer (advanced usage).
        """
    @overload
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
    def IsMutable(self) -> bool: 
        """
        Return TRUE if data can be invalidated.
        """
    def NbMaxElements(self) -> int: 
        """
        Return number of initially allocated elements which can fit into this buffer, while NbElements can be overwritten to smaller value.
        """
    def SetAllocator(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Assign new buffer allocator with de-allocation of buffer.
        """
    def SetIndex(self,theIndex : int,theValue : int) -> None: 
        """
        Change index at specified position
        """
    def Size(self) -> int: 
        """
        Return buffer length in bytes.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Validate(self) -> None: 
        """
        Reset invalidated range.
        """
    def __init__(self,theAlloc : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def changeValue(self,theElem : int) -> int: 
        """
        Access specified element.
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
    def invalidate(self,theRange : Graphic3d_BufferRange) -> None: 
        """
        Invalidate specified sub-range of data (as byte offsets).
        """
    def release(self) -> None: 
        """
        Release buffer.
        """
    def value(self,theElem : int) -> int: 
        """
        Access specified element.
        """
    @property
    def NbAttributes(self) -> int:
        """
        :type: int
        """
    @NbAttributes.setter
    def NbAttributes(self, arg0: int) -> None:
        pass
    @property
    def NbElements(self) -> int:
        """
        :type: int
        """
    @NbElements.setter
    def NbElements(self, arg0: int) -> None:
        pass
    @property
    def Stride(self) -> int:
        """
        :type: int
        """
    @Stride.setter
    def Stride(self, arg0: int) -> None:
        pass
    pass
class Graphic3d_NameOfMaterial():
    """
    Types of aspect materials.

    Members:

      Graphic3d_NOM_BRASS

      Graphic3d_NOM_BRONZE

      Graphic3d_NOM_COPPER

      Graphic3d_NOM_GOLD

      Graphic3d_NOM_PEWTER

      Graphic3d_NOM_PLASTER

      Graphic3d_NOM_PLASTIC

      Graphic3d_NOM_SILVER

      Graphic3d_NOM_STEEL

      Graphic3d_NOM_STONE

      Graphic3d_NOM_SHINY_PLASTIC

      Graphic3d_NOM_SATIN

      Graphic3d_NOM_METALIZED

      Graphic3d_NOM_NEON_GNC

      Graphic3d_NOM_CHROME

      Graphic3d_NOM_ALUMINIUM

      Graphic3d_NOM_OBSIDIAN

      Graphic3d_NOM_NEON_PHC

      Graphic3d_NOM_JADE

      Graphic3d_NOM_CHARCOAL

      Graphic3d_NOM_WATER

      Graphic3d_NOM_GLASS

      Graphic3d_NOM_DIAMOND

      Graphic3d_NOM_TRANSPARENT

      Graphic3d_NOM_DEFAULT

      Graphic3d_NOM_UserDefined
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_NOM_ALUMINIUM: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_ALUMINIUM
    Graphic3d_NOM_BRASS: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRASS
    Graphic3d_NOM_BRONZE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRONZE
    Graphic3d_NOM_CHARCOAL: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHARCOAL
    Graphic3d_NOM_CHROME: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHROME
    Graphic3d_NOM_COPPER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_COPPER
    Graphic3d_NOM_DEFAULT: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_DEFAULT
    Graphic3d_NOM_DIAMOND: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_DIAMOND
    Graphic3d_NOM_GLASS: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_GLASS
    Graphic3d_NOM_GOLD: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_GOLD
    Graphic3d_NOM_JADE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_JADE
    Graphic3d_NOM_METALIZED: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED
    Graphic3d_NOM_NEON_GNC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_GNC
    Graphic3d_NOM_NEON_PHC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_PHC
    Graphic3d_NOM_OBSIDIAN: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_OBSIDIAN
    Graphic3d_NOM_PEWTER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PEWTER
    Graphic3d_NOM_PLASTER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTER
    Graphic3d_NOM_PLASTIC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTIC
    Graphic3d_NOM_SATIN: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SATIN
    Graphic3d_NOM_SHINY_PLASTIC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SHINY_PLASTIC
    Graphic3d_NOM_SILVER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SILVER
    Graphic3d_NOM_STEEL: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_STEEL
    Graphic3d_NOM_STONE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_STONE
    Graphic3d_NOM_TRANSPARENT: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_TRANSPARENT
    Graphic3d_NOM_UserDefined: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_UserDefined
    Graphic3d_NOM_WATER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_WATER
    __entries: dict # value = {'Graphic3d_NOM_BRASS': (Graphic3d_NameOfMaterial.Graphic3d_NOM_BRASS, None), 'Graphic3d_NOM_BRONZE': (Graphic3d_NameOfMaterial.Graphic3d_NOM_BRONZE, None), 'Graphic3d_NOM_COPPER': (Graphic3d_NameOfMaterial.Graphic3d_NOM_COPPER, None), 'Graphic3d_NOM_GOLD': (Graphic3d_NameOfMaterial.Graphic3d_NOM_GOLD, None), 'Graphic3d_NOM_PEWTER': (Graphic3d_NameOfMaterial.Graphic3d_NOM_PEWTER, None), 'Graphic3d_NOM_PLASTER': (Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTER, None), 'Graphic3d_NOM_PLASTIC': (Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTIC, None), 'Graphic3d_NOM_SILVER': (Graphic3d_NameOfMaterial.Graphic3d_NOM_SILVER, None), 'Graphic3d_NOM_STEEL': (Graphic3d_NameOfMaterial.Graphic3d_NOM_STEEL, None), 'Graphic3d_NOM_STONE': (Graphic3d_NameOfMaterial.Graphic3d_NOM_STONE, None), 'Graphic3d_NOM_SHINY_PLASTIC': (Graphic3d_NameOfMaterial.Graphic3d_NOM_SHINY_PLASTIC, None), 'Graphic3d_NOM_SATIN': (Graphic3d_NameOfMaterial.Graphic3d_NOM_SATIN, None), 'Graphic3d_NOM_METALIZED': (Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED, None), 'Graphic3d_NOM_NEON_GNC': (Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_GNC, None), 'Graphic3d_NOM_CHROME': (Graphic3d_NameOfMaterial.Graphic3d_NOM_CHROME, None), 'Graphic3d_NOM_ALUMINIUM': (Graphic3d_NameOfMaterial.Graphic3d_NOM_ALUMINIUM, None), 'Graphic3d_NOM_OBSIDIAN': (Graphic3d_NameOfMaterial.Graphic3d_NOM_OBSIDIAN, None), 'Graphic3d_NOM_NEON_PHC': (Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_PHC, None), 'Graphic3d_NOM_JADE': (Graphic3d_NameOfMaterial.Graphic3d_NOM_JADE, None), 'Graphic3d_NOM_CHARCOAL': (Graphic3d_NameOfMaterial.Graphic3d_NOM_CHARCOAL, None), 'Graphic3d_NOM_WATER': (Graphic3d_NameOfMaterial.Graphic3d_NOM_WATER, None), 'Graphic3d_NOM_GLASS': (Graphic3d_NameOfMaterial.Graphic3d_NOM_GLASS, None), 'Graphic3d_NOM_DIAMOND': (Graphic3d_NameOfMaterial.Graphic3d_NOM_DIAMOND, None), 'Graphic3d_NOM_TRANSPARENT': (Graphic3d_NameOfMaterial.Graphic3d_NOM_TRANSPARENT, None), 'Graphic3d_NOM_DEFAULT': (Graphic3d_NameOfMaterial.Graphic3d_NOM_DEFAULT, None), 'Graphic3d_NOM_UserDefined': (Graphic3d_NameOfMaterial.Graphic3d_NOM_UserDefined, None)}
    __members__: dict # value = {'Graphic3d_NOM_BRASS': Graphic3d_NameOfMaterial.Graphic3d_NOM_BRASS, 'Graphic3d_NOM_BRONZE': Graphic3d_NameOfMaterial.Graphic3d_NOM_BRONZE, 'Graphic3d_NOM_COPPER': Graphic3d_NameOfMaterial.Graphic3d_NOM_COPPER, 'Graphic3d_NOM_GOLD': Graphic3d_NameOfMaterial.Graphic3d_NOM_GOLD, 'Graphic3d_NOM_PEWTER': Graphic3d_NameOfMaterial.Graphic3d_NOM_PEWTER, 'Graphic3d_NOM_PLASTER': Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTER, 'Graphic3d_NOM_PLASTIC': Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTIC, 'Graphic3d_NOM_SILVER': Graphic3d_NameOfMaterial.Graphic3d_NOM_SILVER, 'Graphic3d_NOM_STEEL': Graphic3d_NameOfMaterial.Graphic3d_NOM_STEEL, 'Graphic3d_NOM_STONE': Graphic3d_NameOfMaterial.Graphic3d_NOM_STONE, 'Graphic3d_NOM_SHINY_PLASTIC': Graphic3d_NameOfMaterial.Graphic3d_NOM_SHINY_PLASTIC, 'Graphic3d_NOM_SATIN': Graphic3d_NameOfMaterial.Graphic3d_NOM_SATIN, 'Graphic3d_NOM_METALIZED': Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED, 'Graphic3d_NOM_NEON_GNC': Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_GNC, 'Graphic3d_NOM_CHROME': Graphic3d_NameOfMaterial.Graphic3d_NOM_CHROME, 'Graphic3d_NOM_ALUMINIUM': Graphic3d_NameOfMaterial.Graphic3d_NOM_ALUMINIUM, 'Graphic3d_NOM_OBSIDIAN': Graphic3d_NameOfMaterial.Graphic3d_NOM_OBSIDIAN, 'Graphic3d_NOM_NEON_PHC': Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_PHC, 'Graphic3d_NOM_JADE': Graphic3d_NameOfMaterial.Graphic3d_NOM_JADE, 'Graphic3d_NOM_CHARCOAL': Graphic3d_NameOfMaterial.Graphic3d_NOM_CHARCOAL, 'Graphic3d_NOM_WATER': Graphic3d_NameOfMaterial.Graphic3d_NOM_WATER, 'Graphic3d_NOM_GLASS': Graphic3d_NameOfMaterial.Graphic3d_NOM_GLASS, 'Graphic3d_NOM_DIAMOND': Graphic3d_NameOfMaterial.Graphic3d_NOM_DIAMOND, 'Graphic3d_NOM_TRANSPARENT': Graphic3d_NameOfMaterial.Graphic3d_NOM_TRANSPARENT, 'Graphic3d_NOM_DEFAULT': Graphic3d_NameOfMaterial.Graphic3d_NOM_DEFAULT, 'Graphic3d_NOM_UserDefined': Graphic3d_NameOfMaterial.Graphic3d_NOM_UserDefined}
    pass
class Graphic3d_NameOfTexture1D():
    """
    Types of standard textures.

    Members:

      Graphic3d_NOT_1D_ELEVATION

      Graphic3d_NOT_1D_UNKNOWN
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_NOT_1D_ELEVATION: OCP.Graphic3d.Graphic3d_NameOfTexture1D # value = Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_ELEVATION
    Graphic3d_NOT_1D_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexture1D # value = Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_UNKNOWN
    __entries: dict # value = {'Graphic3d_NOT_1D_ELEVATION': (Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_ELEVATION, None), 'Graphic3d_NOT_1D_UNKNOWN': (Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_UNKNOWN, None)}
    __members__: dict # value = {'Graphic3d_NOT_1D_ELEVATION': Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_ELEVATION, 'Graphic3d_NOT_1D_UNKNOWN': Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_UNKNOWN}
    pass
class Graphic3d_NameOfTexture2D():
    """
    Types of standard textures.

    Members:

      Graphic3d_NOT_2D_MATRA

      Graphic3d_NOT_2D_ALIENSKIN

      Graphic3d_NOT_2D_BLUE_ROCK

      Graphic3d_NOT_2D_BLUEWHITE_PAPER

      Graphic3d_NOT_2D_BRUSHED

      Graphic3d_NOT_2D_BUBBLES

      Graphic3d_NOT_2D_BUMP

      Graphic3d_NOT_2D_CAST

      Graphic3d_NOT_2D_CHIPBD

      Graphic3d_NOT_2D_CLOUDS

      Graphic3d_NOT_2D_FLESH

      Graphic3d_NOT_2D_FLOOR

      Graphic3d_NOT_2D_GALVNISD

      Graphic3d_NOT_2D_GRASS

      Graphic3d_NOT_2D_ALUMINUM

      Graphic3d_NOT_2D_ROCK

      Graphic3d_NOT_2D_KNURL

      Graphic3d_NOT_2D_MAPLE

      Graphic3d_NOT_2D_MARBLE

      Graphic3d_NOT_2D_MOTTLED

      Graphic3d_NOT_2D_RAIN

      Graphic3d_NOT_2D_CHESS

      Graphic3d_NOT_2D_UNKNOWN
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_NOT_2D_ALIENSKIN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALIENSKIN
    Graphic3d_NOT_2D_ALUMINUM: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALUMINUM
    Graphic3d_NOT_2D_BLUEWHITE_PAPER: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUEWHITE_PAPER
    Graphic3d_NOT_2D_BLUE_ROCK: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUE_ROCK
    Graphic3d_NOT_2D_BRUSHED: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BRUSHED
    Graphic3d_NOT_2D_BUBBLES: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUBBLES
    Graphic3d_NOT_2D_BUMP: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUMP
    Graphic3d_NOT_2D_CAST: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CAST
    Graphic3d_NOT_2D_CHESS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHESS
    Graphic3d_NOT_2D_CHIPBD: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHIPBD
    Graphic3d_NOT_2D_CLOUDS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CLOUDS
    Graphic3d_NOT_2D_FLESH: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLESH
    Graphic3d_NOT_2D_FLOOR: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLOOR
    Graphic3d_NOT_2D_GALVNISD: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GALVNISD
    Graphic3d_NOT_2D_GRASS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GRASS
    Graphic3d_NOT_2D_KNURL: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_KNURL
    Graphic3d_NOT_2D_MAPLE: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MAPLE
    Graphic3d_NOT_2D_MARBLE: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MARBLE
    Graphic3d_NOT_2D_MATRA: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MATRA
    Graphic3d_NOT_2D_MOTTLED: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MOTTLED
    Graphic3d_NOT_2D_RAIN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_RAIN
    Graphic3d_NOT_2D_ROCK: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ROCK
    Graphic3d_NOT_2D_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_UNKNOWN
    __entries: dict # value = {'Graphic3d_NOT_2D_MATRA': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MATRA, None), 'Graphic3d_NOT_2D_ALIENSKIN': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALIENSKIN, None), 'Graphic3d_NOT_2D_BLUE_ROCK': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUE_ROCK, None), 'Graphic3d_NOT_2D_BLUEWHITE_PAPER': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUEWHITE_PAPER, None), 'Graphic3d_NOT_2D_BRUSHED': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BRUSHED, None), 'Graphic3d_NOT_2D_BUBBLES': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUBBLES, None), 'Graphic3d_NOT_2D_BUMP': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUMP, None), 'Graphic3d_NOT_2D_CAST': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CAST, None), 'Graphic3d_NOT_2D_CHIPBD': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHIPBD, None), 'Graphic3d_NOT_2D_CLOUDS': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CLOUDS, None), 'Graphic3d_NOT_2D_FLESH': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLESH, None), 'Graphic3d_NOT_2D_FLOOR': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLOOR, None), 'Graphic3d_NOT_2D_GALVNISD': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GALVNISD, None), 'Graphic3d_NOT_2D_GRASS': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GRASS, None), 'Graphic3d_NOT_2D_ALUMINUM': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALUMINUM, None), 'Graphic3d_NOT_2D_ROCK': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ROCK, None), 'Graphic3d_NOT_2D_KNURL': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_KNURL, None), 'Graphic3d_NOT_2D_MAPLE': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MAPLE, None), 'Graphic3d_NOT_2D_MARBLE': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MARBLE, None), 'Graphic3d_NOT_2D_MOTTLED': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MOTTLED, None), 'Graphic3d_NOT_2D_RAIN': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_RAIN, None), 'Graphic3d_NOT_2D_CHESS': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHESS, None), 'Graphic3d_NOT_2D_UNKNOWN': (Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_UNKNOWN, None)}
    __members__: dict # value = {'Graphic3d_NOT_2D_MATRA': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MATRA, 'Graphic3d_NOT_2D_ALIENSKIN': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALIENSKIN, 'Graphic3d_NOT_2D_BLUE_ROCK': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUE_ROCK, 'Graphic3d_NOT_2D_BLUEWHITE_PAPER': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUEWHITE_PAPER, 'Graphic3d_NOT_2D_BRUSHED': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BRUSHED, 'Graphic3d_NOT_2D_BUBBLES': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUBBLES, 'Graphic3d_NOT_2D_BUMP': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUMP, 'Graphic3d_NOT_2D_CAST': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CAST, 'Graphic3d_NOT_2D_CHIPBD': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHIPBD, 'Graphic3d_NOT_2D_CLOUDS': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CLOUDS, 'Graphic3d_NOT_2D_FLESH': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLESH, 'Graphic3d_NOT_2D_FLOOR': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLOOR, 'Graphic3d_NOT_2D_GALVNISD': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GALVNISD, 'Graphic3d_NOT_2D_GRASS': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GRASS, 'Graphic3d_NOT_2D_ALUMINUM': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALUMINUM, 'Graphic3d_NOT_2D_ROCK': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ROCK, 'Graphic3d_NOT_2D_KNURL': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_KNURL, 'Graphic3d_NOT_2D_MAPLE': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MAPLE, 'Graphic3d_NOT_2D_MARBLE': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MARBLE, 'Graphic3d_NOT_2D_MOTTLED': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MOTTLED, 'Graphic3d_NOT_2D_RAIN': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_RAIN, 'Graphic3d_NOT_2D_CHESS': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHESS, 'Graphic3d_NOT_2D_UNKNOWN': Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_UNKNOWN}
    pass
class Graphic3d_NameOfTextureEnv():
    """
    Types of standard textures.

    Members:

      Graphic3d_NOT_ENV_CLOUDS

      Graphic3d_NOT_ENV_CV

      Graphic3d_NOT_ENV_MEDIT

      Graphic3d_NOT_ENV_PEARL

      Graphic3d_NOT_ENV_SKY1

      Graphic3d_NOT_ENV_SKY2

      Graphic3d_NOT_ENV_LINES

      Graphic3d_NOT_ENV_ROAD

      Graphic3d_NOT_ENV_UNKNOWN
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_NOT_ENV_CLOUDS: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CLOUDS
    Graphic3d_NOT_ENV_CV: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CV
    Graphic3d_NOT_ENV_LINES: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_LINES
    Graphic3d_NOT_ENV_MEDIT: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_MEDIT
    Graphic3d_NOT_ENV_PEARL: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_PEARL
    Graphic3d_NOT_ENV_ROAD: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_ROAD
    Graphic3d_NOT_ENV_SKY1: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY1
    Graphic3d_NOT_ENV_SKY2: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY2
    Graphic3d_NOT_ENV_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_UNKNOWN
    __entries: dict # value = {'Graphic3d_NOT_ENV_CLOUDS': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CLOUDS, None), 'Graphic3d_NOT_ENV_CV': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CV, None), 'Graphic3d_NOT_ENV_MEDIT': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_MEDIT, None), 'Graphic3d_NOT_ENV_PEARL': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_PEARL, None), 'Graphic3d_NOT_ENV_SKY1': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY1, None), 'Graphic3d_NOT_ENV_SKY2': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY2, None), 'Graphic3d_NOT_ENV_LINES': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_LINES, None), 'Graphic3d_NOT_ENV_ROAD': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_ROAD, None), 'Graphic3d_NOT_ENV_UNKNOWN': (Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_UNKNOWN, None)}
    __members__: dict # value = {'Graphic3d_NOT_ENV_CLOUDS': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CLOUDS, 'Graphic3d_NOT_ENV_CV': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CV, 'Graphic3d_NOT_ENV_MEDIT': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_MEDIT, 'Graphic3d_NOT_ENV_PEARL': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_PEARL, 'Graphic3d_NOT_ENV_SKY1': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY1, 'Graphic3d_NOT_ENV_SKY2': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY2, 'Graphic3d_NOT_ENV_LINES': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_LINES, 'Graphic3d_NOT_ENV_ROAD': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_ROAD, 'Graphic3d_NOT_ENV_UNKNOWN': Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_UNKNOWN}
    pass
class Graphic3d_NameOfTexturePlane():
    """
    Type of the texture projection plane for both S and T texture coordinate.

    Members:

      Graphic3d_NOTP_XY

      Graphic3d_NOTP_YZ

      Graphic3d_NOTP_ZX

      Graphic3d_NOTP_UNKNOWN
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_NOTP_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_UNKNOWN
    Graphic3d_NOTP_XY: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_XY
    Graphic3d_NOTP_YZ: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_YZ
    Graphic3d_NOTP_ZX: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_ZX
    __entries: dict # value = {'Graphic3d_NOTP_XY': (Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_XY, None), 'Graphic3d_NOTP_YZ': (Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_YZ, None), 'Graphic3d_NOTP_ZX': (Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_ZX, None), 'Graphic3d_NOTP_UNKNOWN': (Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_UNKNOWN, None)}
    __members__: dict # value = {'Graphic3d_NOTP_XY': Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_XY, 'Graphic3d_NOTP_YZ': Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_YZ, 'Graphic3d_NOTP_ZX': Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_ZX, 'Graphic3d_NOTP_UNKNOWN': Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_UNKNOWN}
    pass
class Graphic3d_PolygonOffset():
    """
    Polygon offset parameters.
    """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def __init__(self) -> None: ...
    @property
    def Factor(self) -> float:
        """
        :type: float
        """
    @Factor.setter
    def Factor(self, arg0: float) -> None:
        pass
    @property
    def Mode(self) -> OCP.Aspect.Aspect_PolygonOffsetMode:
        """
        :type: OCP.Aspect.Aspect_PolygonOffsetMode
        """
    @Mode.setter
    def Mode(self, arg0: OCP.Aspect.Aspect_PolygonOffsetMode) -> None:
        pass
    @property
    def Units(self) -> float:
        """
        :type: float
        """
    @Units.setter
    def Units(self, arg0: float) -> None:
        pass
    pass
class Graphic3d_PresentationAttributes(OCP.Standard.Standard_Transient):
    """
    Class defines presentation properties.Class defines presentation properties.
    """
    def BasicFillAreaAspect(self) -> Graphic3d_AspectFillArea3d: 
        """
        Return basic presentation fill area aspect, NULL by default. When set, might be used instead of Color() property.
        """
    def Color(self) -> OCP.Quantity.Quantity_Color: 
        """
        Returns basic presentation color, Quantity_NOC_WHITE by default.
        """
    def ColorRGBA(self) -> OCP.Quantity.Quantity_ColorRGBA: 
        """
        Returns basic presentation color (including alpha channel).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisplayMode(self) -> int: 
        """
        Returns display mode, 0 by default. -1 means undefined (main display mode of presentation to be used).
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
    def Method(self) -> OCP.Aspect.Aspect_TypeOfHighlightMethod: 
        """
        Returns highlight method, Aspect_TOHM_COLOR by default.
        """
    def SetBasicFillAreaAspect(self,theAspect : Graphic3d_AspectFillArea3d) -> None: 
        """
        Sets basic presentation fill area aspect.
        """
    def SetColor(self,theColor : OCP.Quantity.Quantity_Color) -> None: 
        """
        Sets basic presentation color (RGB components, does not modifies transparency).
        """
    def SetDisplayMode(self,theMode : int) -> None: 
        """
        Sets display mode.
        """
    def SetMethod(self,theMethod : OCP.Aspect.Aspect_TypeOfHighlightMethod) -> None: 
        """
        Changes highlight method to the given one.
        """
    def SetTransparency(self,theTranspCoef : float) -> None: 
        """
        Sets basic presentation transparency (0 - opaque, 1 - fully transparent).
        """
    def SetZLayer(self,theLayer : int) -> None: 
        """
        Sets presentation Zlayer.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transparency(self) -> float: 
        """
        Returns basic presentation transparency (0 - opaque, 1 - fully transparent), 0 by default (opaque).
        """
    def ZLayer(self) -> int: 
        """
        Returns presentation Zlayer, Graphic3d_ZLayerId_Default by default. Graphic3d_ZLayerId_UNKNOWN means undefined (a layer of main presentation to be used).
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
class Graphic3d_PriorityDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Graphic3d', '__weakref__': <attribute '__weakref__' of 'Graphic3d_PriorityDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Graphic3d_PriorityDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Graphic3d_RenderTransparentMethod():
    """
    Enumerates transparency rendering methods supported by rasterization mode.

    Members:

      Graphic3d_RTM_BLEND_UNORDERED

      Graphic3d_RTM_BLEND_OIT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_RTM_BLEND_OIT: OCP.Graphic3d.Graphic3d_RenderTransparentMethod # value = Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_OIT
    Graphic3d_RTM_BLEND_UNORDERED: OCP.Graphic3d.Graphic3d_RenderTransparentMethod # value = Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_UNORDERED
    __entries: dict # value = {'Graphic3d_RTM_BLEND_UNORDERED': (Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_UNORDERED, None), 'Graphic3d_RTM_BLEND_OIT': (Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_OIT, None)}
    __members__: dict # value = {'Graphic3d_RTM_BLEND_UNORDERED': Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_UNORDERED, 'Graphic3d_RTM_BLEND_OIT': Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_OIT}
    pass
class Graphic3d_RenderingMode():
    """
    Describes rendering modes. - RM_RASTERIZATION: enables OpenGL rasterization mode; - RM_RAYTRACING: enables GPU ray-tracing mode.

    Members:

      Graphic3d_RM_RASTERIZATION

      Graphic3d_RM_RAYTRACING
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_RM_RASTERIZATION: OCP.Graphic3d.Graphic3d_RenderingMode # value = Graphic3d_RenderingMode.Graphic3d_RM_RASTERIZATION
    Graphic3d_RM_RAYTRACING: OCP.Graphic3d.Graphic3d_RenderingMode # value = Graphic3d_RenderingMode.Graphic3d_RM_RAYTRACING
    __entries: dict # value = {'Graphic3d_RM_RASTERIZATION': (Graphic3d_RenderingMode.Graphic3d_RM_RASTERIZATION, None), 'Graphic3d_RM_RAYTRACING': (Graphic3d_RenderingMode.Graphic3d_RM_RAYTRACING, None)}
    __members__: dict # value = {'Graphic3d_RM_RASTERIZATION': Graphic3d_RenderingMode.Graphic3d_RM_RASTERIZATION, 'Graphic3d_RM_RAYTRACING': Graphic3d_RenderingMode.Graphic3d_RM_RAYTRACING}
    pass
class Graphic3d_RenderingParams():
    """
    Helper class to store rendering parameters.
    """
    def ResolutionRatio(self) -> float: 
        """
        Returns resolution ratio.
        """
    def __init__(self) -> None: ...
    @property
    def AdaptiveScreenSampling(self) -> bool:
        """
        :type: bool
        """
    @AdaptiveScreenSampling.setter
    def AdaptiveScreenSampling(self, arg0: bool) -> None:
        pass
    @property
    def AdaptiveScreenSamplingAtomic(self) -> bool:
        """
        :type: bool
        """
    @AdaptiveScreenSamplingAtomic.setter
    def AdaptiveScreenSamplingAtomic(self, arg0: bool) -> None:
        pass
    @property
    def AnaglyphLeft(self) -> Graphic3d_Mat4:
        """
        :type: Graphic3d_Mat4
        """
    @AnaglyphLeft.setter
    def AnaglyphLeft(self, arg0: Graphic3d_Mat4) -> None:
        pass
    @property
    def AnaglyphRight(self) -> Graphic3d_Mat4:
        """
        :type: Graphic3d_Mat4
        """
    @AnaglyphRight.setter
    def AnaglyphRight(self, arg0: Graphic3d_Mat4) -> None:
        pass
    @property
    def CameraApertureRadius(self) -> float:
        """
        :type: float
        """
    @CameraApertureRadius.setter
    def CameraApertureRadius(self, arg0: float) -> None:
        pass
    @property
    def CameraFocalPlaneDist(self) -> float:
        """
        :type: float
        """
    @CameraFocalPlaneDist.setter
    def CameraFocalPlaneDist(self, arg0: float) -> None:
        pass
    @property
    def ChartSize(self) -> Graphic3d_Vec2i:
        """
        :type: Graphic3d_Vec2i
        """
    @ChartSize.setter
    def ChartSize(self, arg0: Graphic3d_Vec2i) -> None:
        pass
    @property
    def CoherentPathTracingMode(self) -> bool:
        """
        :type: bool
        """
    @CoherentPathTracingMode.setter
    def CoherentPathTracingMode(self, arg0: bool) -> None:
        pass
    @property
    def Exposure(self) -> float:
        """
        :type: float
        """
    @Exposure.setter
    def Exposure(self, arg0: float) -> None:
        pass
    @property
    def IsAntialiasingEnabled(self) -> bool:
        """
        :type: bool
        """
    @IsAntialiasingEnabled.setter
    def IsAntialiasingEnabled(self, arg0: bool) -> None:
        pass
    @property
    def IsGlobalIlluminationEnabled(self) -> bool:
        """
        :type: bool
        """
    @IsGlobalIlluminationEnabled.setter
    def IsGlobalIlluminationEnabled(self, arg0: bool) -> None:
        pass
    @property
    def IsReflectionEnabled(self) -> bool:
        """
        :type: bool
        """
    @IsReflectionEnabled.setter
    def IsReflectionEnabled(self, arg0: bool) -> None:
        pass
    @property
    def IsShadowEnabled(self) -> bool:
        """
        :type: bool
        """
    @IsShadowEnabled.setter
    def IsShadowEnabled(self, arg0: bool) -> None:
        pass
    @property
    def IsTransparentShadowEnabled(self) -> bool:
        """
        :type: bool
        """
    @IsTransparentShadowEnabled.setter
    def IsTransparentShadowEnabled(self, arg0: bool) -> None:
        pass
    @property
    def LineFeather(self) -> float:
        """
        :type: float
        """
    @LineFeather.setter
    def LineFeather(self, arg0: float) -> None:
        pass
    @property
    def Method(self) -> Graphic3d_RenderingMode:
        """
        :type: Graphic3d_RenderingMode
        """
    @Method.setter
    def Method(self, arg0: Graphic3d_RenderingMode) -> None:
        pass
    @property
    def NbMsaaSamples(self) -> int:
        """
        :type: int
        """
    @NbMsaaSamples.setter
    def NbMsaaSamples(self, arg0: int) -> None:
        pass
    @property
    def NbRayTracingTiles(self) -> int:
        """
        :type: int
        """
    @NbRayTracingTiles.setter
    def NbRayTracingTiles(self, arg0: int) -> None:
        pass
    @property
    def OitDepthFactor(self) -> float:
        """
        :type: float
        """
    @OitDepthFactor.setter
    def OitDepthFactor(self, arg0: float) -> None:
        pass
    @property
    def RadianceClampingValue(self) -> float:
        """
        :type: float
        """
    @RadianceClampingValue.setter
    def RadianceClampingValue(self, arg0: float) -> None:
        pass
    @property
    def RayTracingTileSize(self) -> int:
        """
        :type: int
        """
    @RayTracingTileSize.setter
    def RayTracingTileSize(self, arg0: int) -> None:
        pass
    @property
    def RaytracingDepth(self) -> int:
        """
        :type: int
        """
    @RaytracingDepth.setter
    def RaytracingDepth(self, arg0: int) -> None:
        pass
    @property
    def RebuildRayTracingShaders(self) -> bool:
        """
        :type: bool
        """
    @RebuildRayTracingShaders.setter
    def RebuildRayTracingShaders(self, arg0: bool) -> None:
        pass
    @property
    def RenderResolutionScale(self) -> float:
        """
        :type: float
        """
    @RenderResolutionScale.setter
    def RenderResolutionScale(self, arg0: float) -> None:
        pass
    @property
    def SamplesPerPixel(self) -> int:
        """
        :type: int
        """
    @SamplesPerPixel.setter
    def SamplesPerPixel(self, arg0: int) -> None:
        pass
    @property
    def ShowSamplingTiles(self) -> bool:
        """
        :type: bool
        """
    @ShowSamplingTiles.setter
    def ShowSamplingTiles(self, arg0: bool) -> None:
        pass
    @property
    def StatsMaxChartTime(self) -> float:
        """
        :type: float
        """
    @StatsMaxChartTime.setter
    def StatsMaxChartTime(self, arg0: float) -> None:
        pass
    @property
    def StatsNbFrames(self) -> int:
        """
        :type: int
        """
    @StatsNbFrames.setter
    def StatsNbFrames(self, arg0: int) -> None:
        pass
    @property
    def StatsTextHeight(self) -> int:
        """
        :type: int
        """
    @StatsTextHeight.setter
    def StatsTextHeight(self, arg0: int) -> None:
        pass
    @property
    def StatsUpdateInterval(self) -> float:
        """
        :type: float
        """
    @StatsUpdateInterval.setter
    def StatsUpdateInterval(self, arg0: float) -> None:
        pass
    @property
    def StereoMode(self) -> Graphic3d_StereoMode:
        """
        :type: Graphic3d_StereoMode
        """
    @StereoMode.setter
    def StereoMode(self, arg0: Graphic3d_StereoMode) -> None:
        pass
    @property
    def ToEnableAlphaToCoverage(self) -> bool:
        """
        :type: bool
        """
    @ToEnableAlphaToCoverage.setter
    def ToEnableAlphaToCoverage(self, arg0: bool) -> None:
        pass
    @property
    def ToEnableDepthPrepass(self) -> bool:
        """
        :type: bool
        """
    @ToEnableDepthPrepass.setter
    def ToEnableDepthPrepass(self, arg0: bool) -> None:
        pass
    @property
    def ToReverseStereo(self) -> bool:
        """
        :type: bool
        """
    @ToReverseStereo.setter
    def ToReverseStereo(self, arg0: bool) -> None:
        pass
    @property
    def ToShowStats(self) -> bool:
        """
        :type: bool
        """
    @ToShowStats.setter
    def ToShowStats(self, arg0: bool) -> None:
        pass
    @property
    def ToneMappingMethod(self) -> Graphic3d_ToneMappingMethod:
        """
        :type: Graphic3d_ToneMappingMethod
        """
    @ToneMappingMethod.setter
    def ToneMappingMethod(self, arg0: Graphic3d_ToneMappingMethod) -> None:
        pass
    @property
    def TransparencyMethod(self) -> Graphic3d_RenderTransparentMethod:
        """
        :type: Graphic3d_RenderTransparentMethod
        """
    @TransparencyMethod.setter
    def TransparencyMethod(self, arg0: Graphic3d_RenderTransparentMethod) -> None:
        pass
    @property
    def TwoSidedBsdfModels(self) -> bool:
        """
        :type: bool
        """
    @TwoSidedBsdfModels.setter
    def TwoSidedBsdfModels(self, arg0: bool) -> None:
        pass
    @property
    def UseEnvironmentMapBackground(self) -> bool:
        """
        :type: bool
        """
    @UseEnvironmentMapBackground.setter
    def UseEnvironmentMapBackground(self, arg0: bool) -> None:
        pass
    @property
    def WhitePoint(self) -> float:
        """
        :type: float
        """
    @WhitePoint.setter
    def WhitePoint(self, arg0: float) -> None:
        pass
    pass
class Graphic3d_SequenceOfGroup(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Graphic3d_SequenceOfGroup) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Graphic3d_Group) -> None: ...
    def Assign(self,theOther : Graphic3d_SequenceOfGroup) -> Graphic3d_SequenceOfGroup: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Graphic3d_Group: 
        """
        First item access
        """
    def ChangeLast(self) -> Graphic3d_Group: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_Group: 
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
    def First(self) -> Graphic3d_Group: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Graphic3d_Group) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Graphic3d_SequenceOfGroup) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Graphic3d_SequenceOfGroup) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Graphic3d_Group) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Graphic3d_Group: 
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
    def Prepend(self,theSeq : Graphic3d_SequenceOfGroup) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Graphic3d_Group) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Graphic3d_Group) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Graphic3d_SequenceOfGroup) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Graphic3d_Group: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_SequenceOfGroup) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Graphic3d_SequenceOfHClipPlane(OCP.Standard.Standard_Transient):
    """
    Class defines a Clipping Volume as a logical OR (disjunction) operation between Graphic3d_ClipPlane in sequence. Each Graphic3d_ClipPlane represents either a single Plane clipping a halfspace (direction is specified by normal), or a sub-chain of planes defining a logical AND (conjunction) operation. Therefore, this collection allows defining a Clipping Volume through the limited set of Boolean operations between clipping Planes.Class defines a Clipping Volume as a logical OR (disjunction) operation between Graphic3d_ClipPlane in sequence. Each Graphic3d_ClipPlane represents either a single Plane clipping a halfspace (direction is specified by normal), or a sub-chain of planes defining a logical AND (conjunction) operation. Therefore, this collection allows defining a Clipping Volume through the limited set of Boolean operations between clipping Planes.
    """
    def Append(self,theItem : Graphic3d_ClipPlane) -> bool: 
        """
        Append a plane.
        """
    def Clear(self) -> None: 
        """
        Clear the items out.
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
    def First(self) -> Graphic3d_ClipPlane: 
        """
        Return the first item in sequence.
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
        Return TRUE if sequence is empty.
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
    def Remove(self,theItem : Graphic3d_ClipPlane) -> bool: 
        """
        Remove a plane.

        Remove a plane.
        """
    @overload
    def Remove(self,theItem : Any) -> None: ...
    def SetOverrideGlobal(self,theToOverride : bool) -> None: 
        """
        Setup flag defining if local properties should override global properties.
        """
    def Size(self) -> int: 
        """
        Return the number of items in sequence.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def ToOverrideGlobal(self) -> bool: 
        """
        Return true if local properties should override global properties.
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
class Graphic3d_SequenceOfStructure(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Graphic3d_SequenceOfStructure) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Graphic3d_Structure) -> None: ...
    def Assign(self,theOther : Graphic3d_SequenceOfStructure) -> Graphic3d_SequenceOfStructure: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Graphic3d_Structure: 
        """
        First item access
        """
    def ChangeLast(self) -> Graphic3d_Structure: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_Structure: 
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
    def First(self) -> Graphic3d_Structure: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Graphic3d_SequenceOfStructure) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Graphic3d_Structure) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Graphic3d_Structure) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Graphic3d_SequenceOfStructure) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Graphic3d_Structure: 
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
    def Prepend(self,theSeq : Graphic3d_SequenceOfStructure) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Graphic3d_Structure) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Graphic3d_Structure) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Graphic3d_SequenceOfStructure) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Graphic3d_Structure: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_SequenceOfStructure) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Graphic3d_ShaderAttribute(OCP.Standard.Standard_Transient):
    """
    Describes custom vertex shader attribute.Describes custom vertex shader attribute.
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
    def Location(self) -> int: 
        """
        Returns attribute location to be bound on GLSL program linkage stage.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns name of shader variable.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def __init__(self,theName : OCP.TCollection.TCollection_AsciiString,theLocation : int) -> None: ...
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
class Graphic3d_ShaderAttributeList(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Graphic3d_ShaderAttributeList) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Graphic3d_ShaderAttribute) -> None: ...
    def Assign(self,theOther : Graphic3d_ShaderAttributeList) -> Graphic3d_ShaderAttributeList: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Graphic3d_ShaderAttribute: 
        """
        First item access
        """
    def ChangeLast(self) -> Graphic3d_ShaderAttribute: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_ShaderAttribute: 
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
    def First(self) -> Graphic3d_ShaderAttribute: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Graphic3d_ShaderAttribute) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Graphic3d_ShaderAttributeList) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Graphic3d_ShaderAttribute) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Graphic3d_ShaderAttributeList) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Graphic3d_ShaderAttribute: 
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
    def Prepend(self,theSeq : Graphic3d_ShaderAttributeList) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Graphic3d_ShaderAttribute) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Graphic3d_ShaderAttribute) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Graphic3d_ShaderAttributeList) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Graphic3d_ShaderAttribute: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Graphic3d_ShaderAttributeList) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Graphic3d_ShaderObject(OCP.Standard.Standard_Transient):
    """
    This class is responsible for managing shader objects.This class is responsible for managing shader objects.
    """
    @staticmethod
    def CreateFromFile_s(theType : Graphic3d_TypeOfShaderObject,thePath : OCP.TCollection.TCollection_AsciiString) -> Graphic3d_ShaderObject: 
        """
        Creates new shader object from specified file.
        """
    @staticmethod
    def CreateFromSource_s(theType : Graphic3d_TypeOfShaderObject,theSource : OCP.TCollection.TCollection_AsciiString) -> Graphic3d_ShaderObject: 
        """
        Creates new shader object from specified source.
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
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns unique ID used to manage resource in graphic driver.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if the shader object is valid or not.
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
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path to the shader source.
        """
    def Source(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the source code of the shader object.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfShaderObject: 
        """
        Returns type of the shader object.
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
class Graphic3d_ShaderObjectList(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Graphic3d_ShaderObjectList) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Graphic3d_ShaderObject) -> None: ...
    def Assign(self,theOther : Graphic3d_ShaderObjectList) -> Graphic3d_ShaderObjectList: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Graphic3d_ShaderObject: 
        """
        First item access
        """
    def ChangeLast(self) -> Graphic3d_ShaderObject: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_ShaderObject: 
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
    def First(self) -> Graphic3d_ShaderObject: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Graphic3d_ShaderObject) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Graphic3d_ShaderObjectList) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Graphic3d_ShaderObject) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Graphic3d_ShaderObjectList) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Graphic3d_ShaderObject: 
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
    def Prepend(self,theItem : Graphic3d_ShaderObject) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Graphic3d_ShaderObjectList) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Graphic3d_ShaderObject) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Graphic3d_ShaderObjectList) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Graphic3d_ShaderObject: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Graphic3d_ShaderObjectList) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Graphic3d_ShaderProgram(OCP.Standard.Standard_Transient):
    """
    This class is responsible for managing shader programs.This class is responsible for managing shader programs.
    """
    def AppendToHeader(self,theHeaderLine : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Append line to GLSL header.
        """
    def AttachShader(self,theShader : Graphic3d_ShaderObject) -> bool: 
        """
        Attaches shader object to the program object.
        """
    def ClearVariables(self) -> None: 
        """
        Removes all custom uniform variables from the program.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DetachShader(self,theShader : Graphic3d_ShaderObject) -> bool: 
        """
        Detaches shader object from the program object.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns unique ID used to manage resource in graphic driver.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasAlphaTest(self) -> bool: 
        """
        Return true if Fragment Shader should perform alpha test; FALSE by default.
        """
    def HasDefaultSampler(self) -> bool: 
        """
        Return TRUE if standard program header should define default texture sampler occSampler0; TRUE by default for compatibility.
        """
    def HasWeightOitOutput(self) -> bool: 
        """
        Return true if Fragment Shader color should output the weighted OIT coverage; FALSE by default.
        """
    def Header(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns GLSL header (version code and extensions).
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if the program object is valid or not.
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
    def NbClipPlanesMax(self) -> int: 
        """
        Return the length of array of clipping planes (THE_MAX_CLIP_PLANES), to be used for initialization occClipPlaneEquations. Default value is THE_MAX_CLIP_PLANES_DEFAULT.
        """
    def NbFragmentOutputs(self) -> int: 
        """
        Returns the number (1+) of Fragment Shader outputs to be written to (more than 1 can be in case of multiple draw buffers); 1 by default.
        """
    def NbLightsMax(self) -> int: 
        """
        Return the length of array of light sources (THE_MAX_LIGHTS), to be used for initialization occLightSources. Default value is THE_MAX_LIGHTS_DEFAULT.
        """
    def PushVariableFloat(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : float) -> bool: 
        """
        Pushes float uniform.
        """
    def PushVariableInt(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : int) -> bool: 
        """
        Pushes int uniform.
        """
    def PushVariableVec2(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec2) -> bool: 
        """
        Pushes vec2 uniform.
        """
    def PushVariableVec2i(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec2i) -> bool: 
        """
        Pushes vec2i uniform.
        """
    def PushVariableVec3(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec3) -> bool: 
        """
        Pushes vec3 uniform.
        """
    def PushVariableVec3i(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec3i) -> bool: 
        """
        Pushes vec3i uniform.
        """
    def PushVariableVec4(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec4) -> bool: 
        """
        Pushes vec4 uniform.
        """
    def PushVariableVec4i(self,theName : OCP.TCollection.TCollection_AsciiString,theValue : Graphic3d_Vec4i) -> bool: 
        """
        Pushes vec4i uniform.
        """
    def SetAlphaTest(self,theAlphaTest : bool) -> None: 
        """
        Set if Fragment Shader should perform alpha test. Note that this flag is designed for usage with - custom shader program may discard fragment regardless this flag.
        """
    def SetDefaultSampler(self,theHasDefSampler : bool) -> None: 
        """
        Set if standard program header should define default texture sampler occSampler0.
        """
    def SetHeader(self,theHeader : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Setup GLSL header containing language version code and used extensions. Will be prepended to the very beginning of the source code. Example:
        """
    def SetId(self,theId : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Sets unique ID used to manage resource in graphic driver. WARNING! Graphic3d_ShaderProgram constructor generates a unique id for proper resource management; however if application overrides it, it is responsibility of application to avoid name collisions.
        """
    def SetNbClipPlanesMax(self,theNbPlanes : int) -> None: 
        """
        Specify the length of array of clipping planes (THE_MAX_CLIP_PLANES).
        """
    def SetNbFragmentOutputs(self,theNbOutputs : int) -> None: 
        """
        Sets the number of Fragment Shader outputs to be written to. Should be done before GLSL program initialization.
        """
    def SetNbLightsMax(self,theNbLights : int) -> None: 
        """
        Specify the length of array of light sources (THE_MAX_LIGHTS).
        """
    def SetVertexAttributes(self,theAttributes : Graphic3d_ShaderAttributeList) -> None: 
        """
        Assign the list of custom vertex attributes. Should be done before GLSL program initialization.
        """
    def SetWeightOitOutput(self,theOutput : bool) -> None: 
        """
        Set if Fragment Shader color should output the weighted OIT coverage. Note that weighted OIT also requires at least 2 Fragment Outputs (color + coverage).
        """
    def ShaderObjects(self) -> Graphic3d_ShaderObjectList: 
        """
        Returns list of attached shader objects.
        """
    @staticmethod
    def ShadersFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to GLSL programs determined from CSF_ShadersDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Variables(self) -> Graphic3d_ShaderVariableList: 
        """
        The list of currently pushed but not applied custom uniform variables. This list is automatically cleared after applying to GLSL program.
        """
    def VertexAttributes(self) -> Graphic3d_ShaderAttributeList: 
        """
        Return the list of custom vertex attributes.
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
class Graphic3d_ShaderVariable(OCP.Standard.Standard_Transient):
    """
    Describes custom uniform shader variable.Describes custom uniform shader variable.
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
    def IsDone(self) -> bool: 
        """
        Checks if the shader variable is valid or not.
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
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns name of shader variable.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Value(self) -> Graphic3d_ValueInterface: 
        """
        Returns interface of shader variable value.
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
class Graphic3d_ShaderVariableList(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Graphic3d_ShaderVariableList) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Graphic3d_ShaderVariable) -> None: ...
    def Assign(self,theOther : Graphic3d_ShaderVariableList) -> Graphic3d_ShaderVariableList: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Graphic3d_ShaderVariable: 
        """
        First item access
        """
    def ChangeLast(self) -> Graphic3d_ShaderVariable: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Graphic3d_ShaderVariable: 
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
    def First(self) -> Graphic3d_ShaderVariable: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Graphic3d_ShaderVariable) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Graphic3d_ShaderVariableList) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Graphic3d_ShaderVariableList) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Graphic3d_ShaderVariable) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Graphic3d_ShaderVariable: 
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
    def Prepend(self,theSeq : Graphic3d_ShaderVariableList) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Graphic3d_ShaderVariable) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Graphic3d_ShaderVariable) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Graphic3d_ShaderVariableList) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Graphic3d_ShaderVariable: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Graphic3d_ShaderVariableList) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Graphic3d_StereoMode():
    """
    This enumeration defines the list of stereoscopic output modes.

    Members:

      Graphic3d_StereoMode_QuadBuffer

      Graphic3d_StereoMode_Anaglyph

      Graphic3d_StereoMode_RowInterlaced

      Graphic3d_StereoMode_ColumnInterlaced

      Graphic3d_StereoMode_ChessBoard

      Graphic3d_StereoMode_SideBySide

      Graphic3d_StereoMode_OverUnder

      Graphic3d_StereoMode_SoftPageFlip

      Graphic3d_StereoMode_NB
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_StereoMode_Anaglyph: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_Anaglyph
    Graphic3d_StereoMode_ChessBoard: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_ChessBoard
    Graphic3d_StereoMode_ColumnInterlaced: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_ColumnInterlaced
    Graphic3d_StereoMode_NB: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_NB
    Graphic3d_StereoMode_OverUnder: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_OverUnder
    Graphic3d_StereoMode_QuadBuffer: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_QuadBuffer
    Graphic3d_StereoMode_RowInterlaced: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_RowInterlaced
    Graphic3d_StereoMode_SideBySide: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_SideBySide
    Graphic3d_StereoMode_SoftPageFlip: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_SoftPageFlip
    __entries: dict # value = {'Graphic3d_StereoMode_QuadBuffer': (Graphic3d_StereoMode.Graphic3d_StereoMode_QuadBuffer, None), 'Graphic3d_StereoMode_Anaglyph': (Graphic3d_StereoMode.Graphic3d_StereoMode_Anaglyph, None), 'Graphic3d_StereoMode_RowInterlaced': (Graphic3d_StereoMode.Graphic3d_StereoMode_RowInterlaced, None), 'Graphic3d_StereoMode_ColumnInterlaced': (Graphic3d_StereoMode.Graphic3d_StereoMode_ColumnInterlaced, None), 'Graphic3d_StereoMode_ChessBoard': (Graphic3d_StereoMode.Graphic3d_StereoMode_ChessBoard, None), 'Graphic3d_StereoMode_SideBySide': (Graphic3d_StereoMode.Graphic3d_StereoMode_SideBySide, None), 'Graphic3d_StereoMode_OverUnder': (Graphic3d_StereoMode.Graphic3d_StereoMode_OverUnder, None), 'Graphic3d_StereoMode_SoftPageFlip': (Graphic3d_StereoMode.Graphic3d_StereoMode_SoftPageFlip, None), 'Graphic3d_StereoMode_NB': (Graphic3d_StereoMode.Graphic3d_StereoMode_NB, None)}
    __members__: dict # value = {'Graphic3d_StereoMode_QuadBuffer': Graphic3d_StereoMode.Graphic3d_StereoMode_QuadBuffer, 'Graphic3d_StereoMode_Anaglyph': Graphic3d_StereoMode.Graphic3d_StereoMode_Anaglyph, 'Graphic3d_StereoMode_RowInterlaced': Graphic3d_StereoMode.Graphic3d_StereoMode_RowInterlaced, 'Graphic3d_StereoMode_ColumnInterlaced': Graphic3d_StereoMode.Graphic3d_StereoMode_ColumnInterlaced, 'Graphic3d_StereoMode_ChessBoard': Graphic3d_StereoMode.Graphic3d_StereoMode_ChessBoard, 'Graphic3d_StereoMode_SideBySide': Graphic3d_StereoMode.Graphic3d_StereoMode_SideBySide, 'Graphic3d_StereoMode_OverUnder': Graphic3d_StereoMode.Graphic3d_StereoMode_OverUnder, 'Graphic3d_StereoMode_SoftPageFlip': Graphic3d_StereoMode.Graphic3d_StereoMode_SoftPageFlip, 'Graphic3d_StereoMode_NB': Graphic3d_StereoMode.Graphic3d_StereoMode_NB}
    pass
class Graphic3d_Structure(OCP.Standard.Standard_Transient):
    """
    This class allows the definition a graphic object. This graphic structure can be displayed, erased, or highlighted. This graphic structure can be connected with another graphic structure.This class allows the definition a graphic object. This graphic structure can be displayed, erased, or highlighted. This graphic structure can be connected with another graphic structure.
    """
    @staticmethod
    def AcceptConnection_s(theStructure1 : Graphic3d_Structure,theStructure2 : Graphic3d_Structure,theType : Graphic3d_TypeOfConnection) -> bool: 
        """
        Returns Standard_True if the connection is possible between <AStructure1> and <AStructure2> without a creation of a cycle.
        """
    def Ancestors(self,SG : Any) -> None: 
        """
        Returns the group of structures to which <me> is connected.
        """
    def CStructure(self) -> Graphic3d_CStructure: 
        """
        Returns the low-level structure
        """
    def CalculateBoundBox(self) -> None: 
        """
        Computes axis-aligned bounding box of a structure.
        """
    def Clear(self,WithDestruction : bool=True) -> None: 
        """
        if WithDestruction == Standard_True then suppress all the groups of primitives in the structure. and it is mandatory to create a new group in <me>. if WithDestruction == Standard_False then clears all the groups of primitives in the structure. and all the groups are conserved and empty. They will be erased at the next screen update. The structure itself is conserved. The transformation and the attributes of <me> are conserved. The childs of <me> are conserved.
        """
    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: 
        """
        Get clip planes slicing the structure on rendering.
        """
    @overload
    def Compute(self) -> None: 
        """
        None

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization

        Returns the new Structure defined for the new visualization
        """
    @overload
    def Compute(self,theProjector : Graphic3d_DataStructureManager,theStructure : Graphic3d_Structure) -> Any: ...
    @overload
    def Compute(self,theProjector : Graphic3d_DataStructureManager,theTrsf : OCP.Geom.Geom_Transformation) -> Graphic3d_Structure: ...
    @overload
    def Compute(self,theProjector : Graphic3d_DataStructureManager) -> Graphic3d_Structure: ...
    @overload
    def Compute(self,theProjector : Graphic3d_DataStructureManager,theTrsf : OCP.Geom.Geom_Transformation,theStructure : Graphic3d_Structure) -> Any: ...
    def ComputeVisual(self) -> Graphic3d_TypeOfStructure: 
        """
        None
        """
    @overload
    def Connect(self,theStructure : Graphic3d_Structure,theType : Graphic3d_TypeOfConnection,theWithCheck : bool=False) -> None: 
        """
        If Atype is TOC_DESCENDANT then add <AStructure> as a child structure of <me>. If Atype is TOC_ANCESTOR then add <AStructure> as a parent structure of <me>. The connection propagates Display, Highlight, Erase, Remove, and stacks the transformations. No connection if the graph of the structures contains a cycle and <WithCheck> is Standard_True;

        None
        """
    @overload
    def Connect(self,thePrs : Graphic3d_Structure) -> None: ...
    def ContainsFacet(self) -> bool: 
        """
        Returns Standard_True if the structure <me> contains Polygons, Triangles or Quadrangles.
        """
    def CurrentGroup(self) -> Graphic3d_Group: 
        """
        Returns the last created group or creates new one if list is empty.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Descendants(self,SG : Any) -> None: 
        """
        Returns the group of structures connected to <me>.
        """
    def Disconnect(self,theStructure : Graphic3d_Structure) -> None: 
        """
        Suppress the connection between <AStructure> and <me>.
        """
    def DisconnectAll(self,AType : Graphic3d_TypeOfConnection) -> None: 
        """
        If Atype is TOC_DESCENDANT then suppress all the connections with the child structures of <me>. If Atype is TOC_ANCESTOR then suppress all the connections with the parent structures of <me>.
        """
    def Display(self) -> None: 
        """
        Displays the structure <me> in all the views of the visualiser.
        """
    def DisplayPriority(self) -> int: 
        """
        Returns the current display priority for this structure.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self) -> None: 
        """
        Erases the structure <me> in all the views of the visualiser.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GetZLayer(self) -> int: 
        """
        Get Z layer ID of displayed structure. The method returns -1 if the structure has no ID (deleted from graphic driver).
        """
    def GraphicClear(self,WithDestruction : bool) -> None: 
        """
        Clears the structure <me>.
        """
    def GraphicConnect(self,theDaughter : Graphic3d_Structure) -> None: 
        """
        None
        """
    def GraphicDisconnect(self,theDaughter : Graphic3d_Structure) -> None: 
        """
        None
        """
    def GraphicTransform(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Internal method which sets new transformation without calling graphic manager callbacks.
        """
    def Groups(self) -> Graphic3d_SequenceOfGroup: 
        """
        Returns the groups sequence included in this structure.
        """
    def HLRValidation(self) -> bool: 
        """
        Hidden parts stored in this structure are valid if: 1) the owner is defined. 2) they are not invalid.
        """
    def Highlight(self,theStyle : Graphic3d_PresentationAttributes,theToUpdateMgr : bool=True) -> None: 
        """
        Highlights the structure in all the views with the given style
        """
    def HighlightStyle(self) -> Graphic3d_PresentationAttributes: 
        """
        Returns the highlight attributes.
        """
    def Identification(self) -> int: 
        """
        Returns the identification number of this structure.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDeleted(self) -> bool: 
        """
        Returns TRUE if this structure is deleted (after Remove() call).
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns the display indicator for this structure.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns Standard_True if the structure <me> is empty. Warning: A structure is empty if : it do not have group or all the groups are empties and it do not have descendant or all the descendants are empties.
        """
    def IsHighlighted(self) -> bool: 
        """
        Returns the highlight indicator for this structure.
        """
    def IsInfinite(self) -> bool: 
        """
        Returns Standard_True if the structure <me> is infinite.
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
    def IsMutable(self) -> bool: 
        """
        Returns true if structure has mutable nature (content or location are be changed regularly). Mutable structure will be managed in different way than static onces.
        """
    def IsTransformed(self) -> bool: 
        """
        Returns TRUE if the structure is transformed.
        """
    def IsVisible(self) -> bool: 
        """
        Returns the visibility indicator for this structure.
        """
    def MinMaxValues(self,theToIgnoreInfiniteFlag : bool=False) -> OCP.Bnd.Bnd_Box: 
        """
        Returns the coordinates of the boundary box of the structure <me>. If <theToIgnoreInfiniteFlag> is TRUE, the method returns actual graphical boundaries of the Graphic3d_Group components. Otherwise, the method returns boundaries taking into account infinite state of the structure. This approach generally used for application specific fit operation (e.g. fitting the model into screen, not taking into accout infinite helper elements). Warning: If the structure <me> is empty then the empty box is returned, If the structure <me> is infinite then the whole box is returned.
        """
    @staticmethod
    def Network_s(theStructure : Graphic3d_Structure,theType : Graphic3d_TypeOfConnection,theSet : Any) -> None: 
        """
        Returns <ASet> the group of structures : - directly or indirectly connected to <AStructure> if the TypeOfConnection == TOC_DESCENDANT - to which <AStructure> is directly or indirectly connected if the TypeOfConnection == TOC_ANCESTOR
        """
    def NewGroup(self) -> Graphic3d_Group: 
        """
        Append new group to this structure.
        """
    def NumberOfGroups(self) -> int: 
        """
        Returns the current number of groups in this structure.
        """
    def Owner(self) -> capsule: 
        """
        None
        """
    @staticmethod
    def PrintNetwork_s(AStructure : Graphic3d_Structure,AType : Graphic3d_TypeOfConnection) -> None: 
        """
        Prints informations about the network associated with the structure <AStructure>.
        """
    @overload
    def ReCompute(self) -> None: 
        """
        Forces a new construction of the structure <me> if <me> is displayed and TOS_COMPUTED.

        Forces a new construction of the structure <me> if <me> is displayed in <aProjetor> and TOS_COMPUTED.
        """
    @overload
    def ReCompute(self,aProjector : Graphic3d_DataStructureManager) -> None: ...
    @overload
    def Remove(self,thePtr : Graphic3d_Structure,theType : Graphic3d_TypeOfConnection) -> None: 
        """
        Suppress the structure <me>. It will be erased at the next screen update. Warning: No more graphic operations in <me> after this call. Category: Methods to modify the class definition

        None

        Suppress the structure in the list of descendants or in the list of ancestors.
        """
    @overload
    def Remove(self,thePrs : Graphic3d_Structure) -> None: ...
    @overload
    def Remove(self) -> None: ...
    def RemoveAll(self) -> None: 
        """
        None
        """
    def ResetDisplayPriority(self) -> None: 
        """
        Reset the current priority of the structure to the previous priority. Category: Methods to modify the class definition Warning: If <me> is displayed then the SetDisplayPriority method erase <me> and display <me> with the previous priority.
        """
    def SetClipPlanes(self,thePlanes : Graphic3d_SequenceOfHClipPlane) -> None: 
        """
        Changes a sequence of clip planes slicing the structure on rendering.
        """
    def SetComputeVisual(self,theVisual : Graphic3d_TypeOfStructure) -> None: 
        """
        None
        """
    def SetDisplayPriority(self,Priority : int) -> None: 
        """
        Modifies the order of displaying the structure. Values are between 0 and 10. Structures are drawn according to their display priorities in ascending order. A structure of priority 10 is displayed the last and appears over the others. The default value is 5. Category: Methods to modify the class definition Warning: If <me> is displayed then the SetDisplayPriority method erase <me> and display <me> with the new priority. Raises PriorityDefinitionError if <Priority> is greater than 10 or a negative value.
        """
    def SetHLRValidation(self,theFlag : bool) -> None: 
        """
        None
        """
    def SetInfiniteState(self,theToSet : bool) -> None: 
        """
        Sets infinite flag. When TRUE, the MinMaxValues method returns: theXMin = theYMin = theZMin = RealFirst(). theXMax = theYMax = theZMax = RealLast(). By default, structure is created not infinite but empty.
        """
    def SetIsForHighlight(self,isForHighlight : bool) -> None: 
        """
        Marks the structure <me> representing wired structure needed for highlight only so it won't be added to BVH tree.
        """
    def SetMutable(self,theIsMutable : bool) -> None: 
        """
        Sets if the structure location has mutable nature (content or location will be changed regularly).
        """
    def SetOwner(self,theOwner : capsule) -> None: 
        """
        None
        """
    def SetTransformPersistence(self,theTrsfPers : Graphic3d_TransformPers) -> None: 
        """
        Modifies the current transform persistence (pan, zoom or rotate)
        """
    def SetTransformation(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Modifies the current local transformation
        """
    def SetVisible(self,AValue : bool) -> None: 
        """
        Modifies the visibility indicator to Standard_True or Standard_False for the structure <me>. The default value at the definition of <me> is Standard_True.
        """
    def SetVisual(self,AVisual : Graphic3d_TypeOfStructure) -> None: 
        """
        Modifies the visualisation mode for the structure <me>.
        """
    def SetZLayer(self,theLayerId : int) -> None: 
        """
        Set Z layer ID for the structure. The Z layer mechanism allows to display structures presented in higher layers in overlay of structures in lower layers by switching off z buffer depth test between layers
        """
    def SetZoomLimit(self,LimitInf : float,LimitSup : float) -> None: 
        """
        Modifies the minimum and maximum zoom coefficients for the structure <me>. The default value at the definition of <me> is unlimited. Category: Methods to modify the class definition Warning: Raises StructureDefinitionError if <LimitInf> is greater than <LimitSup> or if <LimitInf> or <LimitSup> is a negative value.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transform(self,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        None
        """
    def TransformPersistence(self) -> Graphic3d_TransformPers: 
        """
        Returns transform persistence of the presentable object.
        """
    def Transformation(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return local transformation.
        """
    @staticmethod
    def Transforms_s(theTrsf : OCP.gp.gp_Trsf,theX : float,theY : float,theZ : float) -> Tuple[float, float, float]: 
        """
        Transforms theX, theY, theZ with the transformation theTrsf.
        """
    def UnHighlight(self) -> None: 
        """
        Suppresses the highlight for the structure <me> in all the views of the visualiser.
        """
    def Visual(self) -> Graphic3d_TypeOfStructure: 
        """
        Returns the visualisation mode for the structure <me>.
        """
    def __init__(self,theManager : Graphic3d_StructureManager,theLinkPrs : Graphic3d_Structure=None) -> None: ...
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
class Graphic3d_StructureDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Graphic3d', '__weakref__': <attribute '__weakref__' of 'Graphic3d_StructureDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Graphic3d_StructureDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Graphic3d_StructureManager(OCP.Standard.Standard_Transient):
    """
    This class allows the definition of a manager to which the graphic objects are associated. It allows them to be globally manipulated. It defines the global attributes. Keywords: Structure, Structure Manager, Update Mode, Destroy, Highlight, VisibleThis class allows the definition of a manager to which the graphic objects are associated. It allows them to be globally manipulated. It defines the global attributes. Keywords: Structure, Structure Manager, Update Mode, Destroy, Highlight, Visible
    """
    def ChangeDisplayPriority(self,theStructure : Graphic3d_Structure,theOldPriority : int,theNewPriority : int) -> None: 
        """
        Changes the display priority of the structure <AStructure>.
        """
    def ChangeZLayer(self,theStructure : Graphic3d_Structure,theLayerId : int) -> None: 
        """
        Change Z layer for structure. The Z layer mechanism allows to display structures in higher layers in overlay of structures in lower layers.
        """
    def Clear(self,theStructure : Graphic3d_Structure,theWithDestruction : bool) -> None: 
        """
        Clears the structure.
        """
    def Connect(self,theMother : Graphic3d_Structure,theDaughter : Graphic3d_Structure) -> None: 
        """
        Connects the structures.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def DefinedViews(self) -> Any: 
        """
        Returns the group of views defined in the structure manager.
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Disconnect(self,theMother : Graphic3d_Structure,theDaughter : Graphic3d_Structure) -> None: 
        """
        Disconnects the structures.
        """
    def Display(self,theStructure : Graphic3d_Structure) -> None: 
        """
        Display the structure.
        """
    def DisplayedStructures(self,SG : Any) -> None: 
        """
        Returns the set of structures displayed in visualiser <me>.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    @overload
    def Erase(self,theStructure : Graphic3d_Structure) -> None: 
        """
        Erases all the structures.

        Erases the structure.
        """
    @overload
    def Erase(self) -> None: ...
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def GraphicDriver(self) -> Graphic3d_GraphicDriver: 
        """
        Returns the graphic driver of <me>.
        """
    def Highlight(self,theStructure : Graphic3d_Structure) -> None: 
        """
        Highlights the structure.
        """
    def HighlightedStructures(self,SG : Any) -> None: 
        """
        Returns the set of highlighted structures in a visualiser <me>.
        """
    @overload
    def Identification(self,theView : Graphic3d_CView) -> int: 
        """
        Attaches the view to this structure manager and sets its identification number within the manager.

        Returns the structure with the identification number <AId>.
        """
    @overload
    def Identification(self,AId : int) -> Graphic3d_Structure: ...
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDeviceLost(self) -> bool: 
        """
        Returns TRUE if Device Lost flag has been set and presentation data should be reuploaded onto graphics driver.
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
    def MaxNumOfViews(self) -> int: 
        """
        Returns the theoretical maximum number of definable views in the manager. Warning: It's not possible to accept an infinite number of definable views because each view must have an identification and we have different managers.
        """
    def ObjectAffinity(self,theObject : OCP.Standard.Standard_Transient) -> Graphic3d_ViewAffinity: 
        """
        None
        """
    @overload
    def ReCompute(self,theStructure : Graphic3d_Structure,theProjector : Graphic3d_DataStructureManager) -> None: 
        """
        Forces a new construction of the structure. if <theStructure> is displayed and TOS_COMPUTED.

        Forces a new construction of the structure. if <theStructure> is displayed in <theProjector> and TOS_COMPUTED.
        """
    @overload
    def ReCompute(self,theStructure : Graphic3d_Structure) -> None: ...
    @overload
    def RecomputeStructures(self) -> None: 
        """
        Recomputes all structures in the manager. Resets Device Lost flag.

        Recomputes all structures from theStructures.
        """
    @overload
    def RecomputeStructures(self,theStructures : Any) -> None: ...
    def RegisterObject(self,theObject : OCP.Standard.Standard_Transient) -> Graphic3d_ViewAffinity: 
        """
        None
        """
    def Remove(self) -> None: 
        """
        Deletes and erases the 3D structure manager.
        """
    def SetDeviceLost(self) -> None: 
        """
        Sets Device Lost flag.
        """
    def SetTransform(self,theStructure : Graphic3d_Structure,theTrsf : OCP.Geom.Geom_Transformation) -> None: 
        """
        Transforms the structure.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def UnHighlight(self,AStructure : Graphic3d_Structure) -> None: 
        """
        Suppress the highlighting on the structure <AStructure>.

        Suppresses the highlighting on all the structures in <me>.
        """
    @overload
    def UnHighlight(self) -> None: ...
    def UnIdentification(self,theView : Graphic3d_CView) -> None: 
        """
        Detach the view from this structure manager and release its identification.
        """
    def UnregisterObject(self,theObject : OCP.Standard.Standard_Transient) -> None: 
        """
        None
        """
    def Update(self,theLayerId : int=-1) -> None: 
        """
        Invalidates bounding box of specified ZLayerId.
        """
    def __init__(self,theDriver : Graphic3d_GraphicDriver) -> None: ...
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
class Graphic3d_Text(OCP.Standard.Standard_Transient):
    """
    This class allows the definition of a text object for display. The text might be defined in one of ways, using: - text value and position, - text value, orientation and the state whether the text uses position as point of attach. - text formatter. Formatter contains text, height and alignment parameter.This class allows the definition of a text object for display. The text might be defined in one of ways, using: - text value and position, - text value, orientation and the state whether the text uses position as point of attach. - text formatter. Formatter contains text, height and alignment parameter.
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
    def HasOwnAnchorPoint(self) -> bool: 
        """
        Returns true if the text has an anchor point
        """
    def HasPlane(self) -> bool: 
        """
        Returns true if the text is filled by a point
        """
    def Height(self) -> float: 
        """
        Sets height of text. (Relative to the Normalized Projection Coordinates (NPC) Space).
        """
    def HorizontalAlignment(self) -> Graphic3d_HorizontalTextAlignment: 
        """
        Returns horizontal alignment of text.
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
    def Orientation(self) -> OCP.gp.gp_Ax2: 
        """
        Returns text orientation in 3D space.
        """
    def Position(self) -> OCP.gp.gp_Pnt: 
        """
        The 3D point of attachment is projected. If the orientation is defined, the text is written in the plane of projection.
        """
    def ResetOrientation(self) -> None: 
        """
        Reset text orientation in 3D space.
        """
    def SetHeight(self,theHeight : float) -> None: 
        """
        Returns height of text
        """
    def SetHorizontalAlignment(self,theJustification : Graphic3d_HorizontalTextAlignment) -> None: 
        """
        Sets horizontal alignment of text.
        """
    def SetOrientation(self,theOrientation : OCP.gp.gp_Ax2) -> None: 
        """
        Sets text orientation in 3D space.
        """
    def SetOwnAnchorPoint(self,theHasOwnAnchor : bool) -> None: 
        """
        Returns true if the text has an anchor point
        """
    def SetPosition(self,thePoint : OCP.gp.gp_Pnt) -> None: 
        """
        Sets text point.
        """
    @overload
    def SetText(self,theText : OCP.NCollection.NCollection_Utf8String) -> None: 
        """
        Sets text value.

        Sets text value.

        Sets text value.
        """
    @overload
    def SetText(self,theText : str) -> None: ...
    @overload
    def SetText(self,theText : OCP.TCollection.TCollection_AsciiString) -> None: ...
    def SetVerticalAlignment(self,theJustification : Graphic3d_VerticalTextAlignment) -> None: 
        """
        Sets vertical alignment of text.
        """
    def Text(self) -> OCP.NCollection.NCollection_Utf8String: 
        """
        Returns text value.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def VerticalAlignment(self) -> Graphic3d_VerticalTextAlignment: 
        """
        Returns vertical alignment of text.
        """
    def __init__(self,theHeight : float) -> None: ...
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
class Graphic3d_TextPath():
    """
    Direction in which text is displayed.

    Members:

      Graphic3d_TP_UP

      Graphic3d_TP_DOWN

      Graphic3d_TP_LEFT

      Graphic3d_TP_RIGHT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TP_DOWN: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_DOWN
    Graphic3d_TP_LEFT: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_LEFT
    Graphic3d_TP_RIGHT: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_RIGHT
    Graphic3d_TP_UP: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_UP
    __entries: dict # value = {'Graphic3d_TP_UP': (Graphic3d_TextPath.Graphic3d_TP_UP, None), 'Graphic3d_TP_DOWN': (Graphic3d_TextPath.Graphic3d_TP_DOWN, None), 'Graphic3d_TP_LEFT': (Graphic3d_TextPath.Graphic3d_TP_LEFT, None), 'Graphic3d_TP_RIGHT': (Graphic3d_TextPath.Graphic3d_TP_RIGHT, None)}
    __members__: dict # value = {'Graphic3d_TP_UP': Graphic3d_TextPath.Graphic3d_TP_UP, 'Graphic3d_TP_DOWN': Graphic3d_TextPath.Graphic3d_TP_DOWN, 'Graphic3d_TP_LEFT': Graphic3d_TextPath.Graphic3d_TP_LEFT, 'Graphic3d_TP_RIGHT': Graphic3d_TextPath.Graphic3d_TP_RIGHT}
    pass
class Graphic3d_Texture1D(Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This is an abstract class for managing 1D textures.This is an abstract class for managing 1D textures.This is an abstract class for managing 1D textures.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture1D: 
        """
        Returns the name of the predefined textures or NOT_1D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    @staticmethod
    def TextureName_s(aRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
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
class Graphic3d_Texture1Dmanual(Graphic3d_Texture1D, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This class provides the implementation of a manual 1D texture. you MUST provides texture coordinates on your facets if you want to see your texture.This class provides the implementation of a manual 1D texture. you MUST provides texture coordinates on your facets if you want to see your texture.This class provides the implementation of a manual 1D texture. you MUST provides texture coordinates on your facets if you want to see your texture.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture1D: 
        """
        Returns the name of the predefined textures or NOT_1D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    @staticmethod
    def TextureName_s(aRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,theNOT : Graphic3d_NameOfTexture1D) -> None: ...
    @overload
    def __init__(self,thePixMap : OCP.Image.Image_PixMap) -> None: ...
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
class Graphic3d_Texture1Dsegment(Graphic3d_Texture1D, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This class provides the implementation of a 1D texture applyable along a segment. You might use the SetSegment() method to set the way the texture is "streched" on facets.This class provides the implementation of a 1D texture applyable along a segment. You might use the SetSegment() method to set the way the texture is "streched" on facets.This class provides the implementation of a 1D texture applyable along a segment. You might use the SetSegment() method to set the way the texture is "streched" on facets.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture1D: 
        """
        Returns the name of the predefined textures or NOT_1D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def Segment(self,theX1 : float,theY1 : float,theZ1 : float,theX2 : float,theY2 : float,theZ2 : float) -> None: 
        """
        Returns the values of the current segment X1, Y1, Z1 , X2, Y2, Z2.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetSegment(self,theX1 : float,theY1 : float,theZ1 : float,theX2 : float,theY2 : float,theZ2 : float) -> None: 
        """
        Sets the texture application bounds. Defines the way the texture is stretched across facets. Default values are <0.0, 0.0, 0.0> , <0.0, 0.0, 1.0>
        """
    @staticmethod
    def TextureName_s(aRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    @overload
    def __init__(self,thePixMap : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,theNOT : Graphic3d_NameOfTexture1D) -> None: ...
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
class Graphic3d_MediaTexture(Graphic3d_Texture2D, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    Texture adapter for Media_Frame.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def Frame(self) -> Media_Frame: 
        """
        Return the frame.
        """
    def GenerateNewId(self) -> None: 
        """
        Regenerate a new texture id
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        Image reader.
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMipMaps(self) -> bool: 
        """
        Return true if mip-maps should be used.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture2D: 
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetFrame(self,theFrame : Media_Frame) -> None: 
        """
        Set the frame.
        """
    def SetImage(self,thePixMap : OCP.Image.Image_PixMap) -> None: 
        """
        Assign new image to the texture. Note that this method does not invalidate already uploaded resources - consider calling ::UpdateRevision() if needed.
        """
    def SetMipMaps(self,theToUse : bool) -> None: 
        """
        Set if mip-maps should be used (generated if needed). Note that this method should be called before loading / using the texture.
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    def __init__(self,theMutex : Any,thePlane : int=-1) -> None: ...
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
class Graphic3d_Texture2Dmanual(Graphic3d_Texture2D, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This class defined a manual texture 2D facets MUST define texture coordinate if you want to see somethings on.This class defined a manual texture 2D facets MUST define texture coordinate if you want to see somethings on.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMipMaps(self) -> bool: 
        """
        Return true if mip-maps should be used.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture2D: 
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetImage(self,thePixMap : OCP.Image.Image_PixMap) -> None: 
        """
        Assign new image to the texture. Note that this method does not invalidate already uploaded resources - consider calling ::UpdateRevision() if needed.
        """
    def SetMipMaps(self,theToUse : bool) -> None: 
        """
        Set if mip-maps should be used (generated if needed). Note that this method should be called before loading / using the texture.
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,theNOT : Graphic3d_NameOfTexture2D) -> None: ...
    @overload
    def __init__(self,thePixMap : OCP.Image.Image_PixMap) -> None: ...
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
class Graphic3d_Texture2Dplane(Graphic3d_Texture2D, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This class allows the management of a 2D texture defined from a plane equation Use the SetXXX() methods for positioning the texture as you want.This class allows the management of a 2D texture defined from a plane equation Use the SetXXX() methods for positioning the texture as you want.This class allows the management of a 2D texture defined from a plane equation Use the SetXXX() methods for positioning the texture as you want.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasMipMaps(self) -> bool: 
        """
        Return true if mip-maps should be used.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def Name(self) -> Graphic3d_NameOfTexture2D: 
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Plane(self) -> Graphic3d_NameOfTexturePlane: 
        """
        Returns the current texture plane name or NOTP_UNKNOWN when the plane is user defined.
        """
    def PlaneS(self,A : float,B : float,C : float,D : float) -> None: 
        """
        Returns the current texture plane S equation
        """
    def PlaneT(self,A : float,B : float,C : float,D : float) -> None: 
        """
        Returns the current texture plane T equation
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def Rotation(self,theVal : float) -> None: 
        """
        Returns the current texture rotation angle
        """
    def ScaleS(self,theVal : float) -> None: 
        """
        Returns the current texture S scale value
        """
    def ScaleT(self,theVal : float) -> None: 
        """
        Returns the current texture T scale value
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetImage(self,thePixMap : OCP.Image.Image_PixMap) -> None: 
        """
        Assign new image to the texture. Note that this method does not invalidate already uploaded resources - consider calling ::UpdateRevision() if needed.
        """
    def SetMipMaps(self,theToUse : bool) -> None: 
        """
        Set if mip-maps should be used (generated if needed). Note that this method should be called before loading / using the texture.
        """
    def SetPlane(self,thePlane : Graphic3d_NameOfTexturePlane) -> None: 
        """
        Defines the texture projection plane for both S and T texture coordinate default is NOTP_XY meaning: <1.0, 0.0, 0.0, 0.0> for S and <0.0, 1.0, 0.0, 0.0> for T
        """
    def SetPlaneS(self,A : float,B : float,C : float,D : float) -> None: 
        """
        Defines the texture projection plane for texture coordinate S default is <1.0, 0.0, 0.0, 0.0>
        """
    def SetPlaneT(self,A : float,B : float,C : float,D : float) -> None: 
        """
        Defines the texture projection plane for texture coordinate T default is <0.0, 1.0, 0.0, 0.0>
        """
    def SetRotation(self,theVal : float) -> None: 
        """
        Sets the rotation angle of the whole texture. the same result might be achieved by recomputing the S and T plane equation but it's not the easiest way... the angle is expressed in degrees default is 0.0
        """
    def SetScaleS(self,theVal : float) -> None: 
        """
        Defines the texture scale for the S texture coordinate much easier than recomputing the S plane equation but the result is the same default to 1.0
        """
    def SetScaleT(self,theVal : float) -> None: 
        """
        Defines the texture scale for the T texture coordinate much easier than recompution the T plane equation but the result is the same default to 1.0
        """
    def SetTranslateS(self,theVal : float) -> None: 
        """
        Defines the texture translation for the S texture coordinate you can obtain the same effect by modifying the S plane equation but its not easier. default to 0.0
        """
    def SetTranslateT(self,theVal : float) -> None: 
        """
        Defines the texture translation for the T texture coordinate you can obtain the same effect by modifying the T plane equation but its not easier. default to 0.0
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TranslateS(self,theVal : float) -> None: 
        """
        Returns the current texture S translation value
        """
    def TranslateT(self,theVal : float) -> None: 
        """
        Returns the current texture T translation value
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    @overload
    def __init__(self,thePixMap : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
    @overload
    def __init__(self,theNOT : Graphic3d_NameOfTexture2D) -> None: ...
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
class Graphic3d_TextureEnv(Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    This class provides environment texture.This class provides environment texture.This class provides environment texture.
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
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
    def Name(self) -> Graphic3d_NameOfTextureEnv: 
        """
        Returns the name of the predefined textures or NOT_ENV_UNKNOWN when the name is given as a filename.
        """
    @staticmethod
    def NumberOfTextures_s() -> int: 
        """
        Returns the number of predefined textures.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    @staticmethod
    def TextureName_s(theRank : int) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns the name of the predefined texture of rank <aRank>
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    @overload
    def __init__(self,thePixMap : OCP.Image.Image_PixMap) -> None: ...
    @overload
    def __init__(self,theName : Graphic3d_NameOfTextureEnv) -> None: ...
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString) -> None: ...
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
class Graphic3d_CubeMapPacked(Graphic3d_CubeMap, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    Class is intended to process cubemap packed into single image plane.Class is intended to process cubemap packed into single image plane.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def CurrentSide(self) -> Graphic3d_CubeMapSide: 
        """
        Returns current cubemap side (iterator state).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        This method will be called by graphic driver each time when texture resource should be created. Default constructors allow defining the texture source as path to texture image or directly as pixmap. If the source is defined as path, then the image will be dynamically loaded when this method is called (and no copy will be preserved in this class instance). Inheritors may dynamically generate the image. Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def IsTopDown(self) -> bool: 
        """
        Returns whether row's memory layout is top-down.
        """
    def More(self) -> bool: 
        """
        Returns whether the iterator has reached the end (true if it hasn't).
        """
    def Next(self) -> None: 
        """
        Moves iterator to the next cubemap side. Uses OpenGL cubemap sides order +X -> -X -> +Y -> -Y -> +Z -> -Z.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Reset(self) -> Graphic3d_CubeMap: 
        """
        Sets iterator state to +X cubemap side.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetZInversion(self,theZIsInverted : bool) -> None: 
        """
        Sets Z axis inversion (vertical flipping).
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    def Value(self) -> OCP.Image.Image_PixMap: 
        """
        Returns current cubemap side as PixMap. Resulting PixMap is memory wrapper over original image. Returns null handle if current side or whole cubemap is invalid. Origin image has to contain six quad tiles having one sizes without any gaps to be valid.
        """
    def ZIsInverted(self) -> bool: 
        """
        Returns whether Z axis is inverted.
        """
    @overload
    def __init__(self,theFileName : OCP.TCollection.TCollection_AsciiString,theOrder : Graphic3d_ValidatedCubeMapOrder=Graphic3d_ValidatedCubeMapOrder) -> None: ...
    @overload
    def __init__(self,theImage : OCP.Image.Image_PixMap,theOrder : Graphic3d_ValidatedCubeMapOrder=Graphic3d_ValidatedCubeMapOrder) -> None: ...
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
class Graphic3d_TextureParams(OCP.Standard.Standard_Transient):
    """
    This class describes texture parameters.This class describes texture parameters.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
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
    def Filter(self) -> Graphic3d_TypeOfTextureFilter: 
        """
        Returns texture interpolation filter. Default value is Graphic3d_TOTF_NEAREST.
        """
    def GenMode(self) -> Graphic3d_TypeOfTextureMode: 
        """
        Returns texture coordinates generation mode. Default value is Graphic3d_TOTM_MANUAL.
        """
    def GenPlaneS(self) -> Graphic3d_Vec4: 
        """
        Returns texture coordinates generation plane S.
        """
    def GenPlaneT(self) -> Graphic3d_Vec4: 
        """
        Returns texture coordinates generation plane T.
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
    def IsModulate(self) -> bool: 
        """
        Returns TRUE if the texture is modulate. Default value is FALSE.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enabled. Default value is FALSE.
        """
    def Rotation(self) -> float: 
        """
        Returns rotation angle in degrees Default value is 0.
        """
    def SamplerRevision(self) -> int: 
        """
        Return modification counter of parameters related to sampler state.
        """
    def Scale(self) -> Graphic3d_Vec2: 
        """
        Returns scale factor Default value is no scaling (1.0; 1.0).
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetFilter(self,theFilter : Graphic3d_TypeOfTextureFilter) -> None: ...
    def SetGenMode(self,theMode : Graphic3d_TypeOfTextureMode,thePlaneS : Graphic3d_Vec4,thePlaneT : Graphic3d_Vec4) -> None: 
        """
        Setup texture coordinates generation mode.
        """
    def SetModulate(self,theToModulate : bool) -> None: ...
    def SetRepeat(self,theToRepeat : bool) -> None: ...
    def SetRotation(self,theAngleDegrees : float) -> None: ...
    def SetScale(self,theScale : Graphic3d_Vec2) -> None: ...
    def SetTextureUnit(self,theUnit : Graphic3d_TextureUnit) -> None: 
        """
        Setup default texture unit.
        """
    def SetTranslation(self,theVec : Graphic3d_Vec2) -> None: ...
    def TextureUnit(self) -> Graphic3d_TextureUnit: 
        """
        Default texture unit to be used, default is Graphic3d_TextureUnit_BaseColor.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Translation(self) -> Graphic3d_Vec2: 
        """
        Returns translation vector Default value is no translation (0.0; 0.0).
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
class Graphic3d_CubeMapSeparate(Graphic3d_CubeMap, Graphic3d_TextureMap, Graphic3d_TextureRoot, OCP.Standard.Standard_Transient):
    """
    Class to manage cubemap located in six different images.Class to manage cubemap located in six different images.
    """
    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy: 
        """
        Returns level of anisontropy texture filter. Default value is Graphic3d_LOTA_OFF.
        """
    def CurrentSide(self) -> Graphic3d_CubeMapSide: 
        """
        Returns current cubemap side (iterator state).
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DisableModulate(self) -> None: 
        """
        disable texture modulate mode. the image is directly decal on the surface.
        """
    def DisableRepeat(self) -> None: 
        """
        use this methods if you want to disable texture repetition on your objects.
        """
    def DisableSmooth(self) -> None: 
        """
        disable texture smoothing
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def EnableModulate(self) -> None: 
        """
        enable texture modulate mode. the image is modulate with the shading of the surface.
        """
    def EnableRepeat(self) -> None: 
        """
        use this methods if you want to enable texture repetition on your objects.
        """
    def EnableSmooth(self) -> None: 
        """
        enable texture smoothing
        """
    def GetId(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        This ID will be used to manage resource in graphic driver.
        """
    def GetImage(self) -> OCP.Image.Image_PixMap: 
        """
        Returns NULL.
        """
    def GetParams(self) -> Graphic3d_TextureParams: 
        """
        Returns low-level texture parameters
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsDone(self) -> bool: 
        """
        Checks if a texture class is valid or not. Returns true if the construction of the class is correct.
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
        Returns TRUE if the texture is modulate.
        """
    def IsRepeat(self) -> bool: 
        """
        Returns TRUE if the texture repeat is enable.
        """
    def IsSmoothed(self) -> bool: 
        """
        Returns TRUE if the texture is smoothed.
        """
    def IsTopDown(self) -> bool: 
        """
        Returns whether row's memory layout is top-down.
        """
    def More(self) -> bool: 
        """
        Returns whether the iterator has reached the end (true if it hasn't).
        """
    def Next(self) -> None: 
        """
        Moves iterator to the next cubemap side. Uses OpenGL cubemap sides order +X -> -X -> +Y -> -Y -> +Z -> -Z.
        """
    def Path(self) -> OCP.OSD.OSD_Path: 
        """
        Returns the full path of the defined texture. It could be empty path if GetImage() is overridden to load image not from file.
        """
    def Reset(self) -> Graphic3d_CubeMap: 
        """
        Sets iterator state to +X cubemap side.
        """
    def Revision(self) -> int: 
        """
        Return image revision.
        """
    def SetAnisoFilter(self,theLevel : Graphic3d_LevelOfTextureAnisotropy) -> None: ...
    def SetZInversion(self,theZIsInverted : bool) -> None: 
        """
        Sets Z axis inversion (vertical flipping).
        """
    @staticmethod
    def TexturesFolder_s() -> OCP.TCollection.TCollection_AsciiString: 
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment variables.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Type(self) -> Graphic3d_TypeOfTexture: 
        """
        Returns the texture type.
        """
    def UpdateRevision(self) -> None: 
        """
        Update image revision. Can be used for signaling changes in the texture source (e.g. file update, pixmap update) without re-creating texture source itself (since unique id should be never modified).
        """
    def Value(self) -> OCP.Image.Image_PixMap: 
        """
        Returns current side of cubemap as PixMap. Returns null handle if current side or whole cubemap is invalid. All origin images have to have the same sizes, format and quad shapes to form valid cubemap.
        """
    def ZIsInverted(self) -> bool: 
        """
        Returns whether Z axis is inverted.
        """
    @overload
    def __init__(self,thePaths : OCP.TColStd.TColStd_Array1OfAsciiString) -> None: ...
    @overload
    def __init__(self,theImages : Any) -> None: ...
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
class Graphic3d_MediaTextureSet(Graphic3d_TextureSet, OCP.Standard.Standard_Transient):
    """
    Texture adapter for Media_Frame.
    """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def Duration(self) -> float: 
        """
        Return duration in seconds.
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def First(self) -> Graphic3d_TextureMap: 
        """
        Return the first texture.
        """
    def FrameSize(self) -> Graphic3d_Vec2i: 
        """
        Return front frame dimensions.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Input(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return input media.
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if texture array is empty.
        """
    def IsFullRangeYUV(self) -> bool: 
        """
        Return TRUE if YUV range is full.
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
    def IsPlanarYUV(self) -> bool: 
        """
        Return TRUE if texture set defined 3 YUV planes.
        """
    def Lower(self) -> int: 
        """
        Return the lower index in texture set.
        """
    def Notify(self) -> None: 
        """
        Call callback.
        """
    def OpenInput(self,thePath : OCP.TCollection.TCollection_AsciiString,theToWait : bool) -> None: 
        """
        Open specified file. Passing an empty path would close current input.
        """
    def PlayerContext(self) -> Media_PlayerContext: 
        """
        Return player context; it can be NULL until first OpenInput().
        """
    def Progress(self) -> float: 
        """
        Return playback progress in seconds.
        """
    def SetCallback(self,theCallbackFunction : Any,theCallbackUserPtr : capsule) -> None: 
        """
        SetCallback(self: OCP.Graphic3d.Graphic3d_MediaTextureSet, theCallbackFunction: void (void*), theCallbackUserPtr: capsule) -> None

        Setup callback to be called on queue progress (e.g. when new frame should be displayed).
        """
    def SetFirst(self,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Return the first texture.
        """
    def SetValue(self,theIndex : int,theTexture : Graphic3d_TextureMap) -> None: 
        """
        Return the texture at specified position within [0, Size()) range.
        """
    def ShaderProgram(self) -> Graphic3d_ShaderProgram: 
        """
        Return shader program for displaying texture set.
        """
    def Size(self) -> int: 
        """
        Return number of textures.
        """
    def SwapFrames(self) -> bool: 
        """
        Swap front/back frames.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Return the upper index in texture set.
        """
    def Value(self,theIndex : int) -> Graphic3d_TextureMap: 
        """
        Return the texture at specified position within [0, Size()) range.
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
class Graphic3d_TextureUnit():
    """
    Texture unit.

    Members:

      Graphic3d_TextureUnit_0

      Graphic3d_TextureUnit_1

      Graphic3d_TextureUnit_2

      Graphic3d_TextureUnit_3

      Graphic3d_TextureUnit_4

      Graphic3d_TextureUnit_5

      Graphic3d_TextureUnit_6

      Graphic3d_TextureUnit_7

      Graphic3d_TextureUnit_8

      Graphic3d_TextureUnit_9

      Graphic3d_TextureUnit_10

      Graphic3d_TextureUnit_11

      Graphic3d_TextureUnit_12

      Graphic3d_TextureUnit_13

      Graphic3d_TextureUnit_14

      Graphic3d_TextureUnit_15

      Graphic3d_TextureUnit_BaseColor

      Graphic3d_TextureUnit_EnvMap
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TextureUnit_0: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
    Graphic3d_TextureUnit_1: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_1
    Graphic3d_TextureUnit_10: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_10
    Graphic3d_TextureUnit_11: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_11
    Graphic3d_TextureUnit_12: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_12
    Graphic3d_TextureUnit_13: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_13
    Graphic3d_TextureUnit_14: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_14
    Graphic3d_TextureUnit_15: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_15
    Graphic3d_TextureUnit_2: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_2
    Graphic3d_TextureUnit_3: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_3
    Graphic3d_TextureUnit_4: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_4
    Graphic3d_TextureUnit_5: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_5
    Graphic3d_TextureUnit_6: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_6
    Graphic3d_TextureUnit_7: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_7
    Graphic3d_TextureUnit_8: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_8
    Graphic3d_TextureUnit_9: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_9
    Graphic3d_TextureUnit_BaseColor: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
    Graphic3d_TextureUnit_EnvMap: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
    __entries: dict # value = {'Graphic3d_TextureUnit_0': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_0, None), 'Graphic3d_TextureUnit_1': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_1, None), 'Graphic3d_TextureUnit_2': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_2, None), 'Graphic3d_TextureUnit_3': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_3, None), 'Graphic3d_TextureUnit_4': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_4, None), 'Graphic3d_TextureUnit_5': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_5, None), 'Graphic3d_TextureUnit_6': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_6, None), 'Graphic3d_TextureUnit_7': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_7, None), 'Graphic3d_TextureUnit_8': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_8, None), 'Graphic3d_TextureUnit_9': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_9, None), 'Graphic3d_TextureUnit_10': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_10, None), 'Graphic3d_TextureUnit_11': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_11, None), 'Graphic3d_TextureUnit_12': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_12, None), 'Graphic3d_TextureUnit_13': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_13, None), 'Graphic3d_TextureUnit_14': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_14, None), 'Graphic3d_TextureUnit_15': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_15, None), 'Graphic3d_TextureUnit_BaseColor': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_0, None), 'Graphic3d_TextureUnit_EnvMap': (Graphic3d_TextureUnit.Graphic3d_TextureUnit_0, None)}
    __members__: dict # value = {'Graphic3d_TextureUnit_0': Graphic3d_TextureUnit.Graphic3d_TextureUnit_0, 'Graphic3d_TextureUnit_1': Graphic3d_TextureUnit.Graphic3d_TextureUnit_1, 'Graphic3d_TextureUnit_2': Graphic3d_TextureUnit.Graphic3d_TextureUnit_2, 'Graphic3d_TextureUnit_3': Graphic3d_TextureUnit.Graphic3d_TextureUnit_3, 'Graphic3d_TextureUnit_4': Graphic3d_TextureUnit.Graphic3d_TextureUnit_4, 'Graphic3d_TextureUnit_5': Graphic3d_TextureUnit.Graphic3d_TextureUnit_5, 'Graphic3d_TextureUnit_6': Graphic3d_TextureUnit.Graphic3d_TextureUnit_6, 'Graphic3d_TextureUnit_7': Graphic3d_TextureUnit.Graphic3d_TextureUnit_7, 'Graphic3d_TextureUnit_8': Graphic3d_TextureUnit.Graphic3d_TextureUnit_8, 'Graphic3d_TextureUnit_9': Graphic3d_TextureUnit.Graphic3d_TextureUnit_9, 'Graphic3d_TextureUnit_10': Graphic3d_TextureUnit.Graphic3d_TextureUnit_10, 'Graphic3d_TextureUnit_11': Graphic3d_TextureUnit.Graphic3d_TextureUnit_11, 'Graphic3d_TextureUnit_12': Graphic3d_TextureUnit.Graphic3d_TextureUnit_12, 'Graphic3d_TextureUnit_13': Graphic3d_TextureUnit.Graphic3d_TextureUnit_13, 'Graphic3d_TextureUnit_14': Graphic3d_TextureUnit.Graphic3d_TextureUnit_14, 'Graphic3d_TextureUnit_15': Graphic3d_TextureUnit.Graphic3d_TextureUnit_15, 'Graphic3d_TextureUnit_BaseColor': Graphic3d_TextureUnit.Graphic3d_TextureUnit_0, 'Graphic3d_TextureUnit_EnvMap': Graphic3d_TextureUnit.Graphic3d_TextureUnit_0}
    pass
class Graphic3d_ToneMappingMethod():
    """
    Enumerates tone mapping methods.

    Members:

      Graphic3d_ToneMappingMethod_Disabled

      Graphic3d_ToneMappingMethod_Filmic
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_ToneMappingMethod_Disabled: OCP.Graphic3d.Graphic3d_ToneMappingMethod # value = Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Disabled
    Graphic3d_ToneMappingMethod_Filmic: OCP.Graphic3d.Graphic3d_ToneMappingMethod # value = Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Filmic
    __entries: dict # value = {'Graphic3d_ToneMappingMethod_Disabled': (Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Disabled, None), 'Graphic3d_ToneMappingMethod_Filmic': (Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Filmic, None)}
    __members__: dict # value = {'Graphic3d_ToneMappingMethod_Disabled': Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Disabled, 'Graphic3d_ToneMappingMethod_Filmic': Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Filmic}
    pass
class Graphic3d_TransModeFlags():
    """
    Transform Persistence Mode defining whether to lock in object position, rotation and / or zooming relative to camera position.

    Members:

      Graphic3d_TMF_None

      Graphic3d_TMF_ZoomPers

      Graphic3d_TMF_RotatePers

      Graphic3d_TMF_TriedronPers

      Graphic3d_TMF_2d

      Graphic3d_TMF_ZoomRotatePers
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TMF_2d: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_2d
    Graphic3d_TMF_None: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_None
    Graphic3d_TMF_RotatePers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_RotatePers
    Graphic3d_TMF_TriedronPers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_TriedronPers
    Graphic3d_TMF_ZoomPers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomPers
    Graphic3d_TMF_ZoomRotatePers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomRotatePers
    __entries: dict # value = {'Graphic3d_TMF_None': (Graphic3d_TransModeFlags.Graphic3d_TMF_None, None), 'Graphic3d_TMF_ZoomPers': (Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomPers, None), 'Graphic3d_TMF_RotatePers': (Graphic3d_TransModeFlags.Graphic3d_TMF_RotatePers, None), 'Graphic3d_TMF_TriedronPers': (Graphic3d_TransModeFlags.Graphic3d_TMF_TriedronPers, None), 'Graphic3d_TMF_2d': (Graphic3d_TransModeFlags.Graphic3d_TMF_2d, None), 'Graphic3d_TMF_ZoomRotatePers': (Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomRotatePers, None)}
    __members__: dict # value = {'Graphic3d_TMF_None': Graphic3d_TransModeFlags.Graphic3d_TMF_None, 'Graphic3d_TMF_ZoomPers': Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomPers, 'Graphic3d_TMF_RotatePers': Graphic3d_TransModeFlags.Graphic3d_TMF_RotatePers, 'Graphic3d_TMF_TriedronPers': Graphic3d_TransModeFlags.Graphic3d_TMF_TriedronPers, 'Graphic3d_TMF_2d': Graphic3d_TransModeFlags.Graphic3d_TMF_2d, 'Graphic3d_TMF_ZoomRotatePers': Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomRotatePers}
    pass
class Graphic3d_TransformError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Graphic3d', '__weakref__': <attribute '__weakref__' of 'Graphic3d_TransformError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Graphic3d_TransformError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Graphic3d_TransformPers(OCP.Standard.Standard_Transient):
    """
    Transformation Persistence definition.Transformation Persistence definition.
    """
    def AnchorPoint(self) -> OCP.gp.gp_Pnt: 
        """
        Return the anchor point for zoom/rotate transformation persistence.
        """
    def Corner2d(self) -> OCP.Aspect.Aspect_TypeOfTriedronPosition: 
        """
        Return the corner for 2d/trihedron transformation persistence.
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
    def Flags(self) -> Graphic3d_TransModeFlags: 
        """
        Transformation persistence mode flags.
        """
    @staticmethod
    def FromDeprecatedParams_s(theFlag : Graphic3d_TransModeFlags,thePoint : OCP.gp.gp_Pnt) -> Graphic3d_TransformPers: 
        """
        Create Graphic3d_TransformPers instance from deprecated parameters set decoding 2D corner + offset parameters from 3D point.
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
    def IsTrihedronOr2d(self) -> bool: 
        """
        Return true for Graphic3d_TMF_TriedronPers and Graphic3d_TMF_2d modes.
        """
    @staticmethod
    def IsTrihedronOr2d_s(theMode : Graphic3d_TransModeFlags) -> bool: 
        """
        Return true if specified mode is 2d/trihedron transformation persistence.
        """
    def IsZoomOrRotate(self) -> bool: 
        """
        Return true for Graphic3d_TMF_ZoomPers, Graphic3d_TMF_ZoomRotatePers or Graphic3d_TMF_RotatePers modes.
        """
    @staticmethod
    def IsZoomOrRotate_s(theMode : Graphic3d_TransModeFlags) -> bool: 
        """
        Return true if specified mode is zoom/rotate transformation persistence.
        """
    def Mode(self) -> Graphic3d_TransModeFlags: 
        """
        Transformation persistence mode flags.
        """
    def Offset2d(self) -> Graphic3d_Vec2i: 
        """
        Return the offset from the corner for 2d/trihedron transformation persistence.
        """
    def SetAnchorPoint(self,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Set the anchor point for zoom/rotate transformation persistence.
        """
    def SetCorner2d(self,thePos : OCP.Aspect.Aspect_TypeOfTriedronPosition) -> None: 
        """
        Set the corner for 2d/trihedron transformation persistence.
        """
    def SetOffset2d(self,theOffset : Graphic3d_Vec2i) -> None: 
        """
        Set the offset from the corner for 2d/trihedron transformation persistence.
        """
    @overload
    def SetPersistence(self,theMode : Graphic3d_TransModeFlags,thePnt : OCP.gp.gp_Pnt) -> None: 
        """
        Set Zoom/Rotate transformation persistence with an anchor 3D point. Throws an exception if persistence mode is not Graphic3d_TMF_ZoomPers, Graphic3d_TMF_ZoomRotatePers or Graphic3d_TMF_RotatePers.

        Set 2d/trihedron transformation persistence with a corner and 2D offset. Throws an exception if persistence mode is not Graphic3d_TMF_TriedronPers or Graphic3d_TMF_2d.
        """
    @overload
    def SetPersistence(self,theMode : Graphic3d_TransModeFlags,theCorner : OCP.Aspect.Aspect_TypeOfTriedronPosition,theOffset : Graphic3d_Vec2i) -> None: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,theMode : Graphic3d_TransModeFlags,thePnt : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,theMode : Graphic3d_TransModeFlags,theCorner : OCP.Aspect.Aspect_TypeOfTriedronPosition,theOffset : Graphic3d_Vec2i=Graphic3d_Vec2i) -> None: ...
    @overload
    def __init__(self,theMode : Graphic3d_TransModeFlags) -> None: ...
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
class Graphic3d_TypeOfAnswer():
    """
    The answer of the method AcceptDisplay AcceptDisplay means is it possible to display the specified structure in the specified view ? TOA_YES yes TOA_NO no TOA_COMPUTE yes but we have to compute the representation

    Members:

      Graphic3d_TOA_YES

      Graphic3d_TOA_NO

      Graphic3d_TOA_COMPUTE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOA_COMPUTE: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_COMPUTE
    Graphic3d_TOA_NO: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_NO
    Graphic3d_TOA_YES: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_YES
    __entries: dict # value = {'Graphic3d_TOA_YES': (Graphic3d_TypeOfAnswer.Graphic3d_TOA_YES, None), 'Graphic3d_TOA_NO': (Graphic3d_TypeOfAnswer.Graphic3d_TOA_NO, None), 'Graphic3d_TOA_COMPUTE': (Graphic3d_TypeOfAnswer.Graphic3d_TOA_COMPUTE, None)}
    __members__: dict # value = {'Graphic3d_TOA_YES': Graphic3d_TypeOfAnswer.Graphic3d_TOA_YES, 'Graphic3d_TOA_NO': Graphic3d_TypeOfAnswer.Graphic3d_TOA_NO, 'Graphic3d_TOA_COMPUTE': Graphic3d_TypeOfAnswer.Graphic3d_TOA_COMPUTE}
    pass
class Graphic3d_TypeOfAttribute():
    """
    Type of attribute in Vertex Buffer

    Members:

      Graphic3d_TOA_POS

      Graphic3d_TOA_NORM

      Graphic3d_TOA_UV

      Graphic3d_TOA_COLOR

      Graphic3d_TOA_CUSTOM
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOA_COLOR: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_COLOR
    Graphic3d_TOA_CUSTOM: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_CUSTOM
    Graphic3d_TOA_NORM: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_NORM
    Graphic3d_TOA_POS: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_POS
    Graphic3d_TOA_UV: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_UV
    __entries: dict # value = {'Graphic3d_TOA_POS': (Graphic3d_TypeOfAttribute.Graphic3d_TOA_POS, None), 'Graphic3d_TOA_NORM': (Graphic3d_TypeOfAttribute.Graphic3d_TOA_NORM, None), 'Graphic3d_TOA_UV': (Graphic3d_TypeOfAttribute.Graphic3d_TOA_UV, None), 'Graphic3d_TOA_COLOR': (Graphic3d_TypeOfAttribute.Graphic3d_TOA_COLOR, None), 'Graphic3d_TOA_CUSTOM': (Graphic3d_TypeOfAttribute.Graphic3d_TOA_CUSTOM, None)}
    __members__: dict # value = {'Graphic3d_TOA_POS': Graphic3d_TypeOfAttribute.Graphic3d_TOA_POS, 'Graphic3d_TOA_NORM': Graphic3d_TypeOfAttribute.Graphic3d_TOA_NORM, 'Graphic3d_TOA_UV': Graphic3d_TypeOfAttribute.Graphic3d_TOA_UV, 'Graphic3d_TOA_COLOR': Graphic3d_TypeOfAttribute.Graphic3d_TOA_COLOR, 'Graphic3d_TOA_CUSTOM': Graphic3d_TypeOfAttribute.Graphic3d_TOA_CUSTOM}
    pass
class Graphic3d_TypeOfBackfacingModel():
    """
    Modes of display of back faces in the view

    Members:

      Graphic3d_TOBM_AUTOMATIC

      Graphic3d_TOBM_FORCE

      Graphic3d_TOBM_DISABLE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOBM_AUTOMATIC: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_AUTOMATIC
    Graphic3d_TOBM_DISABLE: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_DISABLE
    Graphic3d_TOBM_FORCE: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_FORCE
    __entries: dict # value = {'Graphic3d_TOBM_AUTOMATIC': (Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_AUTOMATIC, None), 'Graphic3d_TOBM_FORCE': (Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_FORCE, None), 'Graphic3d_TOBM_DISABLE': (Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_DISABLE, None)}
    __members__: dict # value = {'Graphic3d_TOBM_AUTOMATIC': Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_AUTOMATIC, 'Graphic3d_TOBM_FORCE': Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_FORCE, 'Graphic3d_TOBM_DISABLE': Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_DISABLE}
    pass
class Graphic3d_TypeOfBackground():
    """
    Describes type of view background.

    Members:

      Graphic3d_TOB_NONE

      Graphic3d_TOB_GRADIENT

      Graphic3d_TOB_TEXTURE

      Graphic3d_TOB_CUBEMAP
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOB_CUBEMAP: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_CUBEMAP
    Graphic3d_TOB_GRADIENT: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_GRADIENT
    Graphic3d_TOB_NONE: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_NONE
    Graphic3d_TOB_TEXTURE: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_TEXTURE
    __entries: dict # value = {'Graphic3d_TOB_NONE': (Graphic3d_TypeOfBackground.Graphic3d_TOB_NONE, None), 'Graphic3d_TOB_GRADIENT': (Graphic3d_TypeOfBackground.Graphic3d_TOB_GRADIENT, None), 'Graphic3d_TOB_TEXTURE': (Graphic3d_TypeOfBackground.Graphic3d_TOB_TEXTURE, None), 'Graphic3d_TOB_CUBEMAP': (Graphic3d_TypeOfBackground.Graphic3d_TOB_CUBEMAP, None)}
    __members__: dict # value = {'Graphic3d_TOB_NONE': Graphic3d_TypeOfBackground.Graphic3d_TOB_NONE, 'Graphic3d_TOB_GRADIENT': Graphic3d_TypeOfBackground.Graphic3d_TOB_GRADIENT, 'Graphic3d_TOB_TEXTURE': Graphic3d_TypeOfBackground.Graphic3d_TOB_TEXTURE, 'Graphic3d_TOB_CUBEMAP': Graphic3d_TypeOfBackground.Graphic3d_TOB_CUBEMAP}
    pass
class Graphic3d_TypeOfComposition():
    """
    To manage the transformation matrices of structures.

    Members:

      Graphic3d_TOC_REPLACE

      Graphic3d_TOC_POSTCONCATENATE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOC_POSTCONCATENATE: OCP.Graphic3d.Graphic3d_TypeOfComposition # value = Graphic3d_TypeOfComposition.Graphic3d_TOC_POSTCONCATENATE
    Graphic3d_TOC_REPLACE: OCP.Graphic3d.Graphic3d_TypeOfComposition # value = Graphic3d_TypeOfComposition.Graphic3d_TOC_REPLACE
    __entries: dict # value = {'Graphic3d_TOC_REPLACE': (Graphic3d_TypeOfComposition.Graphic3d_TOC_REPLACE, None), 'Graphic3d_TOC_POSTCONCATENATE': (Graphic3d_TypeOfComposition.Graphic3d_TOC_POSTCONCATENATE, None)}
    __members__: dict # value = {'Graphic3d_TOC_REPLACE': Graphic3d_TypeOfComposition.Graphic3d_TOC_REPLACE, 'Graphic3d_TOC_POSTCONCATENATE': Graphic3d_TypeOfComposition.Graphic3d_TOC_POSTCONCATENATE}
    pass
class Graphic3d_TypeOfConnection():
    """
    To manage the connections between the structures.

    Members:

      Graphic3d_TOC_ANCESTOR

      Graphic3d_TOC_DESCENDANT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOC_ANCESTOR: OCP.Graphic3d.Graphic3d_TypeOfConnection # value = Graphic3d_TypeOfConnection.Graphic3d_TOC_ANCESTOR
    Graphic3d_TOC_DESCENDANT: OCP.Graphic3d.Graphic3d_TypeOfConnection # value = Graphic3d_TypeOfConnection.Graphic3d_TOC_DESCENDANT
    __entries: dict # value = {'Graphic3d_TOC_ANCESTOR': (Graphic3d_TypeOfConnection.Graphic3d_TOC_ANCESTOR, None), 'Graphic3d_TOC_DESCENDANT': (Graphic3d_TypeOfConnection.Graphic3d_TOC_DESCENDANT, None)}
    __members__: dict # value = {'Graphic3d_TOC_ANCESTOR': Graphic3d_TypeOfConnection.Graphic3d_TOC_ANCESTOR, 'Graphic3d_TOC_DESCENDANT': Graphic3d_TypeOfConnection.Graphic3d_TOC_DESCENDANT}
    pass
class Graphic3d_TypeOfData():
    """
    Type of the element in Vertex or Index Buffer

    Members:

      Graphic3d_TOD_USHORT

      Graphic3d_TOD_UINT

      Graphic3d_TOD_VEC2

      Graphic3d_TOD_VEC3

      Graphic3d_TOD_VEC4

      Graphic3d_TOD_VEC4UB

      Graphic3d_TOD_FLOAT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOD_FLOAT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_FLOAT
    Graphic3d_TOD_UINT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_UINT
    Graphic3d_TOD_USHORT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_USHORT
    Graphic3d_TOD_VEC2: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC2
    Graphic3d_TOD_VEC3: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC3
    Graphic3d_TOD_VEC4: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4
    Graphic3d_TOD_VEC4UB: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4UB
    __entries: dict # value = {'Graphic3d_TOD_USHORT': (Graphic3d_TypeOfData.Graphic3d_TOD_USHORT, None), 'Graphic3d_TOD_UINT': (Graphic3d_TypeOfData.Graphic3d_TOD_UINT, None), 'Graphic3d_TOD_VEC2': (Graphic3d_TypeOfData.Graphic3d_TOD_VEC2, None), 'Graphic3d_TOD_VEC3': (Graphic3d_TypeOfData.Graphic3d_TOD_VEC3, None), 'Graphic3d_TOD_VEC4': (Graphic3d_TypeOfData.Graphic3d_TOD_VEC4, None), 'Graphic3d_TOD_VEC4UB': (Graphic3d_TypeOfData.Graphic3d_TOD_VEC4UB, None), 'Graphic3d_TOD_FLOAT': (Graphic3d_TypeOfData.Graphic3d_TOD_FLOAT, None)}
    __members__: dict # value = {'Graphic3d_TOD_USHORT': Graphic3d_TypeOfData.Graphic3d_TOD_USHORT, 'Graphic3d_TOD_UINT': Graphic3d_TypeOfData.Graphic3d_TOD_UINT, 'Graphic3d_TOD_VEC2': Graphic3d_TypeOfData.Graphic3d_TOD_VEC2, 'Graphic3d_TOD_VEC3': Graphic3d_TypeOfData.Graphic3d_TOD_VEC3, 'Graphic3d_TOD_VEC4': Graphic3d_TypeOfData.Graphic3d_TOD_VEC4, 'Graphic3d_TOD_VEC4UB': Graphic3d_TypeOfData.Graphic3d_TOD_VEC4UB, 'Graphic3d_TOD_FLOAT': Graphic3d_TypeOfData.Graphic3d_TOD_FLOAT}
    pass
class Graphic3d_TypeOfLightSource():
    """
    Definition of all the type of light source.

    Members:

      Graphic3d_TOLS_AMBIENT

      Graphic3d_TOLS_DIRECTIONAL

      Graphic3d_TOLS_POSITIONAL

      Graphic3d_TOLS_SPOT

      V3d_AMBIENT

      V3d_DIRECTIONAL

      V3d_POSITIONAL

      V3d_SPOT
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOLS_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT
    Graphic3d_TOLS_DIRECTIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL
    Graphic3d_TOLS_POSITIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL
    Graphic3d_TOLS_SPOT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT
    V3d_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT
    V3d_DIRECTIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL
    V3d_POSITIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL
    V3d_SPOT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT
    __entries: dict # value = {'Graphic3d_TOLS_AMBIENT': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT, None), 'Graphic3d_TOLS_DIRECTIONAL': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL, None), 'Graphic3d_TOLS_POSITIONAL': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL, None), 'Graphic3d_TOLS_SPOT': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT, None), 'V3d_AMBIENT': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT, None), 'V3d_DIRECTIONAL': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL, None), 'V3d_POSITIONAL': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL, None), 'V3d_SPOT': (Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT, None)}
    __members__: dict # value = {'Graphic3d_TOLS_AMBIENT': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT, 'Graphic3d_TOLS_DIRECTIONAL': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL, 'Graphic3d_TOLS_POSITIONAL': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL, 'Graphic3d_TOLS_SPOT': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT, 'V3d_AMBIENT': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT, 'V3d_DIRECTIONAL': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL, 'V3d_POSITIONAL': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL, 'V3d_SPOT': Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT}
    pass
class Graphic3d_TypeOfLimit():
    """
    Type of graphic resource limit.

    Members:

      Graphic3d_TypeOfLimit_MaxNbLights

      Graphic3d_TypeOfLimit_MaxNbClipPlanes

      Graphic3d_TypeOfLimit_MaxNbViews

      Graphic3d_TypeOfLimit_MaxTextureSize

      Graphic3d_TypeOfLimit_MaxViewDumpSizeX

      Graphic3d_TypeOfLimit_MaxViewDumpSizeY

      Graphic3d_TypeOfLimit_MaxCombinedTextureUnits

      Graphic3d_TypeOfLimit_MaxMsaa

      Graphic3d_TypeOfLimit_HasRayTracing

      Graphic3d_TypeOfLimit_HasRayTracingTextures

      Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling

      Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic

      Graphic3d_TypeOfLimit_HasBlendedOit

      Graphic3d_TypeOfLimit_HasBlendedOitMsaa

      Graphic3d_TypeOfLimit_HasFlatShading

      Graphic3d_TypeOfLimit_HasMeshEdges

      Graphic3d_TypeOfLimit_IsWorkaroundFBO

      Graphic3d_TypeOfLimit_NB
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TypeOfLimit_HasBlendedOit: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOit
    Graphic3d_TypeOfLimit_HasBlendedOitMsaa: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOitMsaa
    Graphic3d_TypeOfLimit_HasFlatShading: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasFlatShading
    Graphic3d_TypeOfLimit_HasMeshEdges: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasMeshEdges
    Graphic3d_TypeOfLimit_HasRayTracing: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracing
    Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling
    Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic
    Graphic3d_TypeOfLimit_HasRayTracingTextures: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingTextures
    Graphic3d_TypeOfLimit_IsWorkaroundFBO: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_IsWorkaroundFBO
    Graphic3d_TypeOfLimit_MaxCombinedTextureUnits: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxCombinedTextureUnits
    Graphic3d_TypeOfLimit_MaxMsaa: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxMsaa
    Graphic3d_TypeOfLimit_MaxNbClipPlanes: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbClipPlanes
    Graphic3d_TypeOfLimit_MaxNbLights: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbLights
    Graphic3d_TypeOfLimit_MaxNbViews: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbViews
    Graphic3d_TypeOfLimit_MaxTextureSize: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxTextureSize
    Graphic3d_TypeOfLimit_MaxViewDumpSizeX: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeX
    Graphic3d_TypeOfLimit_MaxViewDumpSizeY: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeY
    Graphic3d_TypeOfLimit_NB: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_NB
    __entries: dict # value = {'Graphic3d_TypeOfLimit_MaxNbLights': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbLights, None), 'Graphic3d_TypeOfLimit_MaxNbClipPlanes': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbClipPlanes, None), 'Graphic3d_TypeOfLimit_MaxNbViews': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbViews, None), 'Graphic3d_TypeOfLimit_MaxTextureSize': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxTextureSize, None), 'Graphic3d_TypeOfLimit_MaxViewDumpSizeX': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeX, None), 'Graphic3d_TypeOfLimit_MaxViewDumpSizeY': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeY, None), 'Graphic3d_TypeOfLimit_MaxCombinedTextureUnits': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxCombinedTextureUnits, None), 'Graphic3d_TypeOfLimit_MaxMsaa': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxMsaa, None), 'Graphic3d_TypeOfLimit_HasRayTracing': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracing, None), 'Graphic3d_TypeOfLimit_HasRayTracingTextures': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingTextures, None), 'Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling, None), 'Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic, None), 'Graphic3d_TypeOfLimit_HasBlendedOit': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOit, None), 'Graphic3d_TypeOfLimit_HasBlendedOitMsaa': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOitMsaa, None), 'Graphic3d_TypeOfLimit_HasFlatShading': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasFlatShading, None), 'Graphic3d_TypeOfLimit_HasMeshEdges': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasMeshEdges, None), 'Graphic3d_TypeOfLimit_IsWorkaroundFBO': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_IsWorkaroundFBO, None), 'Graphic3d_TypeOfLimit_NB': (Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_NB, None)}
    __members__: dict # value = {'Graphic3d_TypeOfLimit_MaxNbLights': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbLights, 'Graphic3d_TypeOfLimit_MaxNbClipPlanes': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbClipPlanes, 'Graphic3d_TypeOfLimit_MaxNbViews': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbViews, 'Graphic3d_TypeOfLimit_MaxTextureSize': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxTextureSize, 'Graphic3d_TypeOfLimit_MaxViewDumpSizeX': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeX, 'Graphic3d_TypeOfLimit_MaxViewDumpSizeY': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeY, 'Graphic3d_TypeOfLimit_MaxCombinedTextureUnits': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxCombinedTextureUnits, 'Graphic3d_TypeOfLimit_MaxMsaa': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxMsaa, 'Graphic3d_TypeOfLimit_HasRayTracing': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracing, 'Graphic3d_TypeOfLimit_HasRayTracingTextures': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingTextures, 'Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling, 'Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic, 'Graphic3d_TypeOfLimit_HasBlendedOit': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOit, 'Graphic3d_TypeOfLimit_HasBlendedOitMsaa': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOitMsaa, 'Graphic3d_TypeOfLimit_HasFlatShading': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasFlatShading, 'Graphic3d_TypeOfLimit_HasMeshEdges': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasMeshEdges, 'Graphic3d_TypeOfLimit_IsWorkaroundFBO': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_IsWorkaroundFBO, 'Graphic3d_TypeOfLimit_NB': Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_NB}
    pass
class Graphic3d_TypeOfMaterial():
    """
    Types of materials specifies if a material can change color.

    Members:

      Graphic3d_MATERIAL_ASPECT

      Graphic3d_MATERIAL_PHYSIC
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_MATERIAL_ASPECT: OCP.Graphic3d.Graphic3d_TypeOfMaterial # value = Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_ASPECT
    Graphic3d_MATERIAL_PHYSIC: OCP.Graphic3d.Graphic3d_TypeOfMaterial # value = Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_PHYSIC
    __entries: dict # value = {'Graphic3d_MATERIAL_ASPECT': (Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_ASPECT, None), 'Graphic3d_MATERIAL_PHYSIC': (Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_PHYSIC, None)}
    __members__: dict # value = {'Graphic3d_MATERIAL_ASPECT': Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_ASPECT, 'Graphic3d_MATERIAL_PHYSIC': Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_PHYSIC}
    pass
class Graphic3d_TypeOfPrimitiveArray():
    """
    The type of primitive array in a group in a structure.

    Members:

      Graphic3d_TOPA_UNDEFINED

      Graphic3d_TOPA_POINTS

      Graphic3d_TOPA_SEGMENTS

      Graphic3d_TOPA_POLYLINES

      Graphic3d_TOPA_TRIANGLES

      Graphic3d_TOPA_TRIANGLESTRIPS

      Graphic3d_TOPA_TRIANGLEFANS

      Graphic3d_TOPA_LINES_ADJACENCY

      Graphic3d_TOPA_LINE_STRIP_ADJACENCY

      Graphic3d_TOPA_TRIANGLES_ADJACENCY

      Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY

      Graphic3d_TOPA_QUADRANGLES

      Graphic3d_TOPA_QUADRANGLESTRIPS

      Graphic3d_TOPA_POLYGONS
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOPA_LINES_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINES_ADJACENCY
    Graphic3d_TOPA_LINE_STRIP_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINE_STRIP_ADJACENCY
    Graphic3d_TOPA_POINTS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POINTS
    Graphic3d_TOPA_POLYGONS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYGONS
    Graphic3d_TOPA_POLYLINES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYLINES
    Graphic3d_TOPA_QUADRANGLES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLES
    Graphic3d_TOPA_QUADRANGLESTRIPS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLESTRIPS
    Graphic3d_TOPA_SEGMENTS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_SEGMENTS
    Graphic3d_TOPA_TRIANGLEFANS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLEFANS
    Graphic3d_TOPA_TRIANGLES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES
    Graphic3d_TOPA_TRIANGLESTRIPS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLESTRIPS
    Graphic3d_TOPA_TRIANGLES_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES_ADJACENCY
    Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY
    Graphic3d_TOPA_UNDEFINED: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_UNDEFINED
    __entries: dict # value = {'Graphic3d_TOPA_UNDEFINED': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_UNDEFINED, None), 'Graphic3d_TOPA_POINTS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POINTS, None), 'Graphic3d_TOPA_SEGMENTS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_SEGMENTS, None), 'Graphic3d_TOPA_POLYLINES': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYLINES, None), 'Graphic3d_TOPA_TRIANGLES': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES, None), 'Graphic3d_TOPA_TRIANGLESTRIPS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLESTRIPS, None), 'Graphic3d_TOPA_TRIANGLEFANS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLEFANS, None), 'Graphic3d_TOPA_LINES_ADJACENCY': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINES_ADJACENCY, None), 'Graphic3d_TOPA_LINE_STRIP_ADJACENCY': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINE_STRIP_ADJACENCY, None), 'Graphic3d_TOPA_TRIANGLES_ADJACENCY': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES_ADJACENCY, None), 'Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY, None), 'Graphic3d_TOPA_QUADRANGLES': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLES, None), 'Graphic3d_TOPA_QUADRANGLESTRIPS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLESTRIPS, None), 'Graphic3d_TOPA_POLYGONS': (Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYGONS, None)}
    __members__: dict # value = {'Graphic3d_TOPA_UNDEFINED': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_UNDEFINED, 'Graphic3d_TOPA_POINTS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POINTS, 'Graphic3d_TOPA_SEGMENTS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_SEGMENTS, 'Graphic3d_TOPA_POLYLINES': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYLINES, 'Graphic3d_TOPA_TRIANGLES': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES, 'Graphic3d_TOPA_TRIANGLESTRIPS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLESTRIPS, 'Graphic3d_TOPA_TRIANGLEFANS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLEFANS, 'Graphic3d_TOPA_LINES_ADJACENCY': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINES_ADJACENCY, 'Graphic3d_TOPA_LINE_STRIP_ADJACENCY': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINE_STRIP_ADJACENCY, 'Graphic3d_TOPA_TRIANGLES_ADJACENCY': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES_ADJACENCY, 'Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY, 'Graphic3d_TOPA_QUADRANGLES': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLES, 'Graphic3d_TOPA_QUADRANGLESTRIPS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLESTRIPS, 'Graphic3d_TOPA_POLYGONS': Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYGONS}
    pass
class Graphic3d_TypeOfReflection():
    """
    Nature of the reflection of a material.

    Members:

      Graphic3d_TOR_AMBIENT

      Graphic3d_TOR_DIFFUSE

      Graphic3d_TOR_SPECULAR

      Graphic3d_TOR_EMISSION
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOR_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_AMBIENT
    Graphic3d_TOR_DIFFUSE: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_DIFFUSE
    Graphic3d_TOR_EMISSION: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_EMISSION
    Graphic3d_TOR_SPECULAR: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_SPECULAR
    __entries: dict # value = {'Graphic3d_TOR_AMBIENT': (Graphic3d_TypeOfReflection.Graphic3d_TOR_AMBIENT, None), 'Graphic3d_TOR_DIFFUSE': (Graphic3d_TypeOfReflection.Graphic3d_TOR_DIFFUSE, None), 'Graphic3d_TOR_SPECULAR': (Graphic3d_TypeOfReflection.Graphic3d_TOR_SPECULAR, None), 'Graphic3d_TOR_EMISSION': (Graphic3d_TypeOfReflection.Graphic3d_TOR_EMISSION, None)}
    __members__: dict # value = {'Graphic3d_TOR_AMBIENT': Graphic3d_TypeOfReflection.Graphic3d_TOR_AMBIENT, 'Graphic3d_TOR_DIFFUSE': Graphic3d_TypeOfReflection.Graphic3d_TOR_DIFFUSE, 'Graphic3d_TOR_SPECULAR': Graphic3d_TypeOfReflection.Graphic3d_TOR_SPECULAR, 'Graphic3d_TOR_EMISSION': Graphic3d_TypeOfReflection.Graphic3d_TOR_EMISSION}
    pass
class Graphic3d_TypeOfShaderObject():
    """
    Type of the shader object.

    Members:

      Graphic3d_TOS_VERTEX

      Graphic3d_TOS_TESS_CONTROL

      Graphic3d_TOS_TESS_EVALUATION

      Graphic3d_TOS_GEOMETRY

      Graphic3d_TOS_FRAGMENT

      Graphic3d_TOS_COMPUTE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOS_COMPUTE: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_COMPUTE
    Graphic3d_TOS_FRAGMENT: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_FRAGMENT
    Graphic3d_TOS_GEOMETRY: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_GEOMETRY
    Graphic3d_TOS_TESS_CONTROL: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_CONTROL
    Graphic3d_TOS_TESS_EVALUATION: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_EVALUATION
    Graphic3d_TOS_VERTEX: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_VERTEX
    __entries: dict # value = {'Graphic3d_TOS_VERTEX': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_VERTEX, None), 'Graphic3d_TOS_TESS_CONTROL': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_CONTROL, None), 'Graphic3d_TOS_TESS_EVALUATION': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_EVALUATION, None), 'Graphic3d_TOS_GEOMETRY': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_GEOMETRY, None), 'Graphic3d_TOS_FRAGMENT': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_FRAGMENT, None), 'Graphic3d_TOS_COMPUTE': (Graphic3d_TypeOfShaderObject.Graphic3d_TOS_COMPUTE, None)}
    __members__: dict # value = {'Graphic3d_TOS_VERTEX': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_VERTEX, 'Graphic3d_TOS_TESS_CONTROL': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_CONTROL, 'Graphic3d_TOS_TESS_EVALUATION': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_EVALUATION, 'Graphic3d_TOS_GEOMETRY': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_GEOMETRY, 'Graphic3d_TOS_FRAGMENT': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_FRAGMENT, 'Graphic3d_TOS_COMPUTE': Graphic3d_TypeOfShaderObject.Graphic3d_TOS_COMPUTE}
    pass
class Graphic3d_TypeOfShadingModel():
    """
    Definition of the color shading model.

    Members:

      Graphic3d_TOSM_DEFAULT

      Graphic3d_TOSM_UNLIT

      Graphic3d_TOSM_FACET

      Graphic3d_TOSM_VERTEX

      Graphic3d_TOSM_FRAGMENT

      Graphic3d_TOSM_NONE

      V3d_COLOR

      V3d_FLAT

      V3d_GOURAUD

      V3d_PHONG
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOSM_DEFAULT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_DEFAULT
    Graphic3d_TOSM_FACET: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET
    Graphic3d_TOSM_FRAGMENT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT
    Graphic3d_TOSM_NONE: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
    Graphic3d_TOSM_UNLIT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
    Graphic3d_TOSM_VERTEX: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX
    V3d_COLOR: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
    V3d_FLAT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET
    V3d_GOURAUD: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX
    V3d_PHONG: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT
    __entries: dict # value = {'Graphic3d_TOSM_DEFAULT': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_DEFAULT, None), 'Graphic3d_TOSM_UNLIT': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, None), 'Graphic3d_TOSM_FACET': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET, None), 'Graphic3d_TOSM_VERTEX': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX, None), 'Graphic3d_TOSM_FRAGMENT': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT, None), 'Graphic3d_TOSM_NONE': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, None), 'V3d_COLOR': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, None), 'V3d_FLAT': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET, None), 'V3d_GOURAUD': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX, None), 'V3d_PHONG': (Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT, None)}
    __members__: dict # value = {'Graphic3d_TOSM_DEFAULT': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_DEFAULT, 'Graphic3d_TOSM_UNLIT': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, 'Graphic3d_TOSM_FACET': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET, 'Graphic3d_TOSM_VERTEX': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX, 'Graphic3d_TOSM_FRAGMENT': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT, 'Graphic3d_TOSM_NONE': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, 'V3d_COLOR': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT, 'V3d_FLAT': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET, 'V3d_GOURAUD': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX, 'V3d_PHONG': Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT}
    pass
class Graphic3d_TypeOfStructure():
    """
    Structural attribute indicating if it can be displayed in wireframe, shadow mode, or both.

    Members:

      Graphic3d_TOS_WIREFRAME

      Graphic3d_TOS_SHADING

      Graphic3d_TOS_COMPUTED

      Graphic3d_TOS_ALL
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOS_ALL: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_ALL
    Graphic3d_TOS_COMPUTED: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_COMPUTED
    Graphic3d_TOS_SHADING: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_SHADING
    Graphic3d_TOS_WIREFRAME: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_WIREFRAME
    __entries: dict # value = {'Graphic3d_TOS_WIREFRAME': (Graphic3d_TypeOfStructure.Graphic3d_TOS_WIREFRAME, None), 'Graphic3d_TOS_SHADING': (Graphic3d_TypeOfStructure.Graphic3d_TOS_SHADING, None), 'Graphic3d_TOS_COMPUTED': (Graphic3d_TypeOfStructure.Graphic3d_TOS_COMPUTED, None), 'Graphic3d_TOS_ALL': (Graphic3d_TypeOfStructure.Graphic3d_TOS_ALL, None)}
    __members__: dict # value = {'Graphic3d_TOS_WIREFRAME': Graphic3d_TypeOfStructure.Graphic3d_TOS_WIREFRAME, 'Graphic3d_TOS_SHADING': Graphic3d_TypeOfStructure.Graphic3d_TOS_SHADING, 'Graphic3d_TOS_COMPUTED': Graphic3d_TypeOfStructure.Graphic3d_TOS_COMPUTED, 'Graphic3d_TOS_ALL': Graphic3d_TypeOfStructure.Graphic3d_TOS_ALL}
    pass
class Graphic3d_TypeOfTexture():
    """
    Type of the texture file format.

    Members:

      Graphic3d_TOT_1D

      Graphic3d_TOT_2D

      Graphic3d_TOT_2D_MIPMAP

      Graphic3d_TOT_CUBEMAP
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOT_1D: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_1D
    Graphic3d_TOT_2D: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D
    Graphic3d_TOT_2D_MIPMAP: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D_MIPMAP
    Graphic3d_TOT_CUBEMAP: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_CUBEMAP
    __entries: dict # value = {'Graphic3d_TOT_1D': (Graphic3d_TypeOfTexture.Graphic3d_TOT_1D, None), 'Graphic3d_TOT_2D': (Graphic3d_TypeOfTexture.Graphic3d_TOT_2D, None), 'Graphic3d_TOT_2D_MIPMAP': (Graphic3d_TypeOfTexture.Graphic3d_TOT_2D_MIPMAP, None), 'Graphic3d_TOT_CUBEMAP': (Graphic3d_TypeOfTexture.Graphic3d_TOT_CUBEMAP, None)}
    __members__: dict # value = {'Graphic3d_TOT_1D': Graphic3d_TypeOfTexture.Graphic3d_TOT_1D, 'Graphic3d_TOT_2D': Graphic3d_TypeOfTexture.Graphic3d_TOT_2D, 'Graphic3d_TOT_2D_MIPMAP': Graphic3d_TypeOfTexture.Graphic3d_TOT_2D_MIPMAP, 'Graphic3d_TOT_CUBEMAP': Graphic3d_TypeOfTexture.Graphic3d_TOT_CUBEMAP}
    pass
class Graphic3d_TypeOfTextureFilter():
    """
    Type of the texture filter. Notice that for textures without mipmaps linear interpolation will be used instead of TOTF_BILINEAR and TOTF_TRILINEAR.

    Members:

      Graphic3d_TOTF_NEAREST

      Graphic3d_TOTF_BILINEAR

      Graphic3d_TOTF_TRILINEAR
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOTF_BILINEAR: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_BILINEAR
    Graphic3d_TOTF_NEAREST: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_NEAREST
    Graphic3d_TOTF_TRILINEAR: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_TRILINEAR
    __entries: dict # value = {'Graphic3d_TOTF_NEAREST': (Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_NEAREST, None), 'Graphic3d_TOTF_BILINEAR': (Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_BILINEAR, None), 'Graphic3d_TOTF_TRILINEAR': (Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_TRILINEAR, None)}
    __members__: dict # value = {'Graphic3d_TOTF_NEAREST': Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_NEAREST, 'Graphic3d_TOTF_BILINEAR': Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_BILINEAR, 'Graphic3d_TOTF_TRILINEAR': Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_TRILINEAR}
    pass
class Graphic3d_TypeOfTextureMode():
    """
    Type of the texture projection.

    Members:

      Graphic3d_TOTM_OBJECT

      Graphic3d_TOTM_SPHERE

      Graphic3d_TOTM_EYE

      Graphic3d_TOTM_MANUAL

      Graphic3d_TOTM_SPRITE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOTM_EYE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_EYE
    Graphic3d_TOTM_MANUAL: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_MANUAL
    Graphic3d_TOTM_OBJECT: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_OBJECT
    Graphic3d_TOTM_SPHERE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPHERE
    Graphic3d_TOTM_SPRITE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPRITE
    __entries: dict # value = {'Graphic3d_TOTM_OBJECT': (Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_OBJECT, None), 'Graphic3d_TOTM_SPHERE': (Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPHERE, None), 'Graphic3d_TOTM_EYE': (Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_EYE, None), 'Graphic3d_TOTM_MANUAL': (Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_MANUAL, None), 'Graphic3d_TOTM_SPRITE': (Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPRITE, None)}
    __members__: dict # value = {'Graphic3d_TOTM_OBJECT': Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_OBJECT, 'Graphic3d_TOTM_SPHERE': Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPHERE, 'Graphic3d_TOTM_EYE': Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_EYE, 'Graphic3d_TOTM_MANUAL': Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_MANUAL, 'Graphic3d_TOTM_SPRITE': Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPRITE}
    pass
class Graphic3d_TypeOfVisualization():
    """
    Modes of visualisation of objects in a view

    Members:

      Graphic3d_TOV_WIREFRAME

      Graphic3d_TOV_SHADING
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_TOV_SHADING: OCP.Graphic3d.Graphic3d_TypeOfVisualization # value = Graphic3d_TypeOfVisualization.Graphic3d_TOV_SHADING
    Graphic3d_TOV_WIREFRAME: OCP.Graphic3d.Graphic3d_TypeOfVisualization # value = Graphic3d_TypeOfVisualization.Graphic3d_TOV_WIREFRAME
    __entries: dict # value = {'Graphic3d_TOV_WIREFRAME': (Graphic3d_TypeOfVisualization.Graphic3d_TOV_WIREFRAME, None), 'Graphic3d_TOV_SHADING': (Graphic3d_TypeOfVisualization.Graphic3d_TOV_SHADING, None)}
    __members__: dict # value = {'Graphic3d_TOV_WIREFRAME': Graphic3d_TypeOfVisualization.Graphic3d_TOV_WIREFRAME, 'Graphic3d_TOV_SHADING': Graphic3d_TypeOfVisualization.Graphic3d_TOV_SHADING}
    pass
class Graphic3d_ValueInterface():
    """
    Interface for generic variable value.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    pass
class Graphic3d_UniformInt(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : int) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec2():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec2i():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec3():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec3i():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec4():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Graphic3d_Vec4i():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Standard_Integer():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformValueTypeID_Standard_ShortReal():
    """
    None
    """
    def __init__(self) -> None: ...
    pass
class Graphic3d_UniformVec2(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec2) -> None: ...
    pass
class Graphic3d_UniformVec2i(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec2i) -> None: ...
    pass
class Graphic3d_UniformVec3(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec3) -> None: ...
    pass
class Graphic3d_UniformVec3i(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec3i) -> None: ...
    pass
class Graphic3d_UniformVec4(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec4) -> None: ...
    pass
class Graphic3d_UniformVec4i(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : Graphic3d_Vec4i) -> None: ...
    pass
class Graphic3d_ValidatedCubeMapOrder():
    """
    Graphic3d_ValidatedCubeMapOrder contains completely valid order object. The only way to create this class except copy constructor is 'Validated' method of Graphic3d_CubeMapOrder. This class can initialize Graphic3d_CubeMapOrder. It is supposed to be used in case of necessity of completely valid order (in function argument as example). It helps to automate order's valid checks.Graphic3d_ValidatedCubeMapOrder contains completely valid order object. The only way to create this class except copy constructor is 'Validated' method of Graphic3d_CubeMapOrder. This class can initialize Graphic3d_CubeMapOrder. It is supposed to be used in case of necessity of completely valid order (in function argument as example). It helps to automate order's valid checks.
    """
    pass
class Graphic3d_UniformFloat(Graphic3d_ValueInterface):
    """
    Describes specific value of custom uniform variable.
    """
    def TypeID(self) -> int: 
        """
        Returns unique identifier of value type.
        """
    def __init__(self,theValue : float) -> None: ...
    pass
class Graphic3d_Vec2():
    """
    Defines the 2D-vector template. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec2: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec2: 
        """
        Constuct DY unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec2) -> float: 
        """
        Computes the dot product.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec2) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> float: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : float) -> Graphic3d_Vec2: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def SetValues(self,theX : float,theY : float) -> None: 
        """
        Assign new values to the vector.
        """
    def SquareModulus(self) -> float: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec2) -> Graphic3d_Vec2: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec2) -> Graphic3d_Vec2: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Vec2: ...
    @overload
    def __init__(self,theXY : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec2) -> Graphic3d_Vec2: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> Graphic3d_Vec2: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec2) -> Graphic3d_Vec2: ...
    def __mul__(self,theFactor : float) -> Graphic3d_Vec2: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : float) -> Graphic3d_Vec2: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec2: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> Graphic3d_Vec2: 
        """
        Compute per-component division by scale factor.
        """
    def cwiseAbs(self) -> Graphic3d_Vec2: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec2) -> Graphic3d_Vec2: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec2) -> Graphic3d_Vec2: 
        """
        Compute component-wise minimum of two vectors.
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XY.

        Alias to 1st component as X coordinate in XY.
        """
    def xy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XY.

        Alias to 2nd component as Y coordinate in XY.
        """
    def yx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    pass
class Graphic3d_Vec2b():
    """
    Defines the 2D-vector template. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> str: 
        """
        None
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec2b: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec2b: 
        """
        Constuct DY unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec2b) -> str: 
        """
        Computes the dot product.
        """
    def GetData(self) -> str: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec2b) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> str: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : str) -> Graphic3d_Vec2b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : str) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def SetValues(self,theX : str,theY : str) -> None: 
        """
        Assign new values to the vector.
        """
    def SquareModulus(self) -> str: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : str) -> Graphic3d_Vec2b: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theXY : str) -> None: ...
    @overload
    def __init__(self,theX : str,theY : str) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : str) -> Graphic3d_Vec2b: ...
    def __mul__(self,theFactor : str) -> Graphic3d_Vec2b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : str) -> Graphic3d_Vec2b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec2b: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : str) -> Graphic3d_Vec2b: 
        """
        Compute per-component division by scale factor.
        """
    def cwiseAbs(self) -> Graphic3d_Vec2b: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec2b) -> Graphic3d_Vec2b: 
        """
        Compute component-wise minimum of two vectors.
        """
    def maxComp(self) -> str: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> str: 
        """
        Compute minimum component of the vector.
        """
    def x(self) -> str: 
        """
        Alias to 1st component as X coordinate in XY.

        Alias to 1st component as X coordinate in XY.
        """
    def xy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def y(self) -> str: 
        """
        Alias to 2nd component as Y coordinate in XY.

        Alias to 2nd component as Y coordinate in XY.
        """
    def yx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    pass
class Graphic3d_Vec2d():
    """
    Defines the 2D-vector template. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec2d: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec2d: 
        """
        Constuct DY unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec2d) -> float: 
        """
        Computes the dot product.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec2d) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> float: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def SetValues(self,theX : float,theY : float) -> None: 
        """
        Assign new values to the vector.
        """
    def SquareModulus(self) -> float: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec2d) -> Graphic3d_Vec2d: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec2d) -> Graphic3d_Vec2d: ...
    @overload
    def __init__(self,theX : float,theY : float) -> None: ...
    @overload
    def __init__(self,theXY : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec2d) -> Graphic3d_Vec2d: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec2d) -> Graphic3d_Vec2d: ...
    def __mul__(self,theFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec2d: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> Graphic3d_Vec2d: 
        """
        Compute per-component division by scale factor.
        """
    def cwiseAbs(self) -> Graphic3d_Vec2d: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec2d) -> Graphic3d_Vec2d: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec2d) -> Graphic3d_Vec2d: 
        """
        Compute component-wise minimum of two vectors.
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XY.

        Alias to 1st component as X coordinate in XY.
        """
    def xy(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XY.

        Alias to 2nd component as Y coordinate in XY.
        """
    def yx(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    pass
class Graphic3d_Vec2i():
    """
    Defines the 2D-vector template. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec2i: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec2i: 
        """
        Constuct DY unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec2i) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec2i) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> int: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec2i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def SetValues(self,theX : int,theY : int) -> None: 
        """
        Assign new values to the vector.
        """
    def SquareModulus(self) -> int: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec2i) -> Graphic3d_Vec2i: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec2i) -> Graphic3d_Vec2i: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec2i: ...
    @overload
    def __init__(self,theXY : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theX : int,theY : int) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec2i) -> Graphic3d_Vec2i: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec2i: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec2i) -> Graphic3d_Vec2i: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec2i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec2i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec2i: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec2i: 
        """
        Compute per-component division by scale factor.
        """
    def cwiseAbs(self) -> Graphic3d_Vec2i: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec2i) -> Graphic3d_Vec2i: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec2i) -> Graphic3d_Vec2i: 
        """
        Compute component-wise minimum of two vectors.
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XY.

        Alias to 1st component as X coordinate in XY.
        """
    def xy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XY.

        Alias to 2nd component as Y coordinate in XY.
        """
    def yx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    pass
class Graphic3d_Vec2ub():
    """
    Defines the 2D-vector template. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec2ub: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec2ub: 
        """
        Constuct DY unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec2ub) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec2ub) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> int: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec2ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def SetValues(self,theX : int,theY : int) -> None: 
        """
        Assign new values to the vector.
        """
    def SquareModulus(self) -> int: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec2ub: ...
    @overload
    def __init__(self,theXY : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theX : int,theY : int) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec2ub: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec2ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec2ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec2ub: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec2ub: 
        """
        Compute per-component division by scale factor.
        """
    def cwiseAbs(self) -> Graphic3d_Vec2ub: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec2ub) -> Graphic3d_Vec2ub: 
        """
        Compute component-wise minimum of two vectors.
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XY.

        Alias to 1st component as X coordinate in XY.
        """
    def xy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XY.

        Alias to 2nd component as Y coordinate in XY.
        """
    def yx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    pass
class Graphic3d_Vec3():
    """
    Generic 3-components vector. To be used as RGB color pixel or XYZ 3D-point. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    @staticmethod
    def Cross_s(theVec1 : Graphic3d_Vec3,theVec2 : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Computes the cross product.
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec3: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec3: 
        """
        Constuct DY unit vector.
        """
    @staticmethod
    def DZ_s() -> Graphic3d_Vec3: 
        """
        Constuct DZ unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec3) -> float: 
        """
        Computes the dot product.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    @staticmethod
    def GetLERP_s(theFrom : Graphic3d_Vec3,theTo : Graphic3d_Vec3,theT : float) -> Graphic3d_Vec3: 
        """
        Compute linear interpolation between to vectors.
        """
    def IsEqual(self,theOther : Graphic3d_Vec3) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> float: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : float) -> Graphic3d_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Normalize(self) -> None: 
        """
        Normalize the vector.
        """
    def Normalized(self) -> Graphic3d_Vec3: 
        """
        Normalize the vector.
        """
    @overload
    def SetValues(self,theVec2 : Graphic3d_Vec2,theZ : float) -> None: 
        """
        Assign new values to the vector.

        Assign new values to the vector.
        """
    @overload
    def SetValues(self,theX : float,theY : float,theZ : float) -> None: ...
    def SquareModulus(self) -> float: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Vec3: ...
    @overload
    def __init__(self,theX : float,theY : float,theZ : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2,theZ : float=0.0) -> None: ...
    @overload
    def __init__(self,theValue : float) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> Graphic3d_Vec3: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec3) -> Graphic3d_Vec3: ...
    def __mul__(self,theFactor : float) -> Graphic3d_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : float) -> Graphic3d_Vec3: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec3: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> Graphic3d_Vec3: 
        """
        Compute per-component division by scale factor.
        """
    def b(self) -> float: 
        """
        Alias to 3rd component as BLUE channel in RGB.

        Alias to 3rd component as BLUE channel in RGB.
        """
    def cwiseAbs(self) -> Graphic3d_Vec3: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec3) -> Graphic3d_Vec3: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> float: 
        """
        Alias to 2nd component as GREEN channel in RGB.

        Alias to 2nd component as GREEN channel in RGB.
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> float: 
        """
        Alias to 1st component as RED channel in RGB.

        Alias to 1st component as RED channel in RGB.
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XYZ.

        Alias to 1st component as X coordinate in XYZ.
        """
    def xy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XYZ.

        Alias to 2nd component as Y coordinate in XYZ.
        """
    def yx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def z(self) -> float: 
        """
        Alias to 3rd component as Z coordinate in XYZ.

        Alias to 3rd component as Z coordinate in XYZ.
        """
    def zx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    pass
class Graphic3d_Vec3b():
    """
    Generic 3-components vector. To be used as RGB color pixel or XYZ 3D-point. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> str: 
        """
        None
        """
    @staticmethod
    def Cross_s(theVec1 : Graphic3d_Vec3b,theVec2 : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Computes the cross product.
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec3b: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec3b: 
        """
        Constuct DY unit vector.
        """
    @staticmethod
    def DZ_s() -> Graphic3d_Vec3b: 
        """
        Constuct DZ unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec3b) -> str: 
        """
        Computes the dot product.
        """
    def GetData(self) -> str: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    @staticmethod
    def GetLERP_s(theFrom : Graphic3d_Vec3b,theTo : Graphic3d_Vec3b,theT : str) -> Graphic3d_Vec3b: 
        """
        Compute linear interpolation between to vectors.
        """
    def IsEqual(self,theOther : Graphic3d_Vec3b) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> str: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : str) -> Graphic3d_Vec3b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : str) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Normalize(self) -> None: 
        """
        Normalize the vector.
        """
    def Normalized(self) -> Graphic3d_Vec3b: 
        """
        Normalize the vector.
        """
    @overload
    def SetValues(self,theX : str,theY : str,theZ : str) -> None: 
        """
        Assign new values to the vector.

        Assign new values to the vector.
        """
    @overload
    def SetValues(self,theVec2 : Graphic3d_Vec2b,theZ : str) -> None: ...
    def SquareModulus(self) -> str: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : str) -> Graphic3d_Vec3b: ...
    @overload
    def __init__(self,theValue : str) -> None: ...
    @overload
    def __init__(self,theX : str,theY : str,theZ : str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2b,theZ : str='\x00') -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : str) -> Graphic3d_Vec3b: ...
    def __mul__(self,theFactor : str) -> Graphic3d_Vec3b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : str) -> Graphic3d_Vec3b: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec3b: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : str) -> Graphic3d_Vec3b: 
        """
        Compute per-component division by scale factor.
        """
    def b(self) -> str: 
        """
        Alias to 3rd component as BLUE channel in RGB.

        Alias to 3rd component as BLUE channel in RGB.
        """
    def cwiseAbs(self) -> Graphic3d_Vec3b: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec3b) -> Graphic3d_Vec3b: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> str: 
        """
        Alias to 2nd component as GREEN channel in RGB.

        Alias to 2nd component as GREEN channel in RGB.
        """
    def maxComp(self) -> str: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> str: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> str: 
        """
        Alias to 1st component as RED channel in RGB.

        Alias to 1st component as RED channel in RGB.
        """
    def x(self) -> str: 
        """
        Alias to 1st component as X coordinate in XYZ.

        Alias to 1st component as X coordinate in XYZ.
        """
    def xy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def y(self) -> str: 
        """
        Alias to 2nd component as Y coordinate in XYZ.

        Alias to 2nd component as Y coordinate in XYZ.
        """
    def yx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def z(self) -> str: 
        """
        Alias to 3rd component as Z coordinate in XYZ.

        Alias to 3rd component as Z coordinate in XYZ.
        """
    def zx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    pass
class Graphic3d_Vec3i():
    """
    Generic 3-components vector. To be used as RGB color pixel or XYZ 3D-point. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    @staticmethod
    def Cross_s(theVec1 : Graphic3d_Vec3i,theVec2 : Graphic3d_Vec3i) -> Graphic3d_Vec3i: 
        """
        Computes the cross product.
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec3i: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec3i: 
        """
        Constuct DY unit vector.
        """
    @staticmethod
    def DZ_s() -> Graphic3d_Vec3i: 
        """
        Constuct DZ unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec3i) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    @staticmethod
    def GetLERP_s(theFrom : Graphic3d_Vec3i,theTo : Graphic3d_Vec3i,theT : int) -> Graphic3d_Vec3i: 
        """
        Compute linear interpolation between to vectors.
        """
    def IsEqual(self,theOther : Graphic3d_Vec3i) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> int: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Normalize(self) -> None: 
        """
        Normalize the vector.
        """
    def Normalized(self) -> Graphic3d_Vec3i: 
        """
        Normalize the vector.
        """
    @overload
    def SetValues(self,theVec2 : Graphic3d_Vec2i,theZ : int) -> None: 
        """
        Assign new values to the vector.

        Assign new values to the vector.
        """
    @overload
    def SetValues(self,theX : int,theY : int,theZ : int) -> None: ...
    def SquareModulus(self) -> int: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec3i) -> Graphic3d_Vec3i: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec3i) -> Graphic3d_Vec3i: ...
    @overload
    def __init__(self,theValue : int) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2i,theZ : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theX : int,theY : int,theZ : int) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec3i) -> Graphic3d_Vec3i: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec3i) -> Graphic3d_Vec3i: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec3i: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec3i: 
        """
        Compute per-component division by scale factor.
        """
    def b(self) -> int: 
        """
        Alias to 3rd component as BLUE channel in RGB.

        Alias to 3rd component as BLUE channel in RGB.
        """
    def cwiseAbs(self) -> Graphic3d_Vec3i: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec3i) -> Graphic3d_Vec3i: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec3i) -> Graphic3d_Vec3i: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> int: 
        """
        Alias to 2nd component as GREEN channel in RGB.

        Alias to 2nd component as GREEN channel in RGB.
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> int: 
        """
        Alias to 1st component as RED channel in RGB.

        Alias to 1st component as RED channel in RGB.
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XYZ.

        Alias to 1st component as X coordinate in XYZ.
        """
    def xy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XYZ.

        Alias to 2nd component as Y coordinate in XYZ.
        """
    def yx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def z(self) -> int: 
        """
        Alias to 3rd component as Z coordinate in XYZ.

        Alias to 3rd component as Z coordinate in XYZ.
        """
    def zx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    pass
class Graphic3d_Vec3ub():
    """
    Generic 3-components vector. To be used as RGB color pixel or XYZ 3D-point. The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    @staticmethod
    def Cross_s(theVec1 : Graphic3d_Vec3ub,theVec2 : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Computes the cross product.
        """
    @staticmethod
    def DX_s() -> Graphic3d_Vec3ub: 
        """
        Constuct DX unit vector.
        """
    @staticmethod
    def DY_s() -> Graphic3d_Vec3ub: 
        """
        Constuct DY unit vector.
        """
    @staticmethod
    def DZ_s() -> Graphic3d_Vec3ub: 
        """
        Constuct DZ unit vector.
        """
    def Dot(self,theOther : Graphic3d_Vec3ub) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    @staticmethod
    def GetLERP_s(theFrom : Graphic3d_Vec3ub,theTo : Graphic3d_Vec3ub,theT : int) -> Graphic3d_Vec3ub: 
        """
        Compute linear interpolation between to vectors.
        """
    def IsEqual(self,theOther : Graphic3d_Vec3ub) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Modulus(self) -> int: 
        """
        Computes the vector modulus (magnitude, length).
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec3ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication by scale factor.
        """
    def Normalize(self) -> None: 
        """
        Normalize the vector.
        """
    def Normalized(self) -> Graphic3d_Vec3ub: 
        """
        Normalize the vector.
        """
    @overload
    def SetValues(self,theVec2 : Graphic3d_Vec2ub,theZ : int) -> None: 
        """
        Assign new values to the vector.

        Assign new values to the vector.
        """
    @overload
    def SetValues(self,theX : int,theY : int,theZ : int) -> None: ...
    def SquareModulus(self) -> int: 
        """
        Computes the square of vector modulus (magnitude, length). This method may be used for performance tricks.
        """
    def __iadd__(self,theAdd : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication by scale factor.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec3ub: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2ub,theZ : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theValue : int) -> None: ...
    @overload
    def __init__(self,theX : int,theY : int,theZ : int) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec3ub: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec3ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec3ub: 
        """
        Compute per-component multiplication by scale factor.
        """
    def __sub__(self) -> Graphic3d_Vec3ub: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec3ub: 
        """
        Compute per-component division by scale factor.
        """
    def b(self) -> int: 
        """
        Alias to 3rd component as BLUE channel in RGB.

        Alias to 3rd component as BLUE channel in RGB.
        """
    def cwiseAbs(self) -> Graphic3d_Vec3ub: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec3ub) -> Graphic3d_Vec3ub: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> int: 
        """
        Alias to 2nd component as GREEN channel in RGB.

        Alias to 2nd component as GREEN channel in RGB.
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> int: 
        """
        Alias to 1st component as RED channel in RGB.

        Alias to 1st component as RED channel in RGB.
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XYZ.

        Alias to 1st component as X coordinate in XYZ.
        """
    def xy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XYZ.

        Alias to 2nd component as Y coordinate in XYZ.
        """
    def yx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def z(self) -> int: 
        """
        Alias to 3rd component as Z coordinate in XYZ.

        Alias to 3rd component as Z coordinate in XYZ.
        """
    def zx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    pass
class Graphic3d_Vec4():
    """
    Generic 4-components vector. To be used as RGBA color vector or XYZW 3D-point with special W-component for operations with projection / model view matrices. Use this class for 3D-points carefully because declared W-component may results in incorrect results if used without matrices.
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    def Dot(self,theOther : Graphic3d_Vec4) -> float: 
        """
        Computes the dot product.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec4) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Multiplied(self,theFactor : float) -> Graphic3d_Vec4: 
        """
        Compute per-component multiplication.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication.
        """
    @overload
    def SetValues(self,theX : float,theY : float,theZ : float,theW : float) -> None: 
        """
        Assign new values to the vector.

        Assign new values as 3-component vector and a 4-th value.
        """
    @overload
    def SetValues(self,theVec3 : Graphic3d_Vec3,theW : float) -> None: ...
    def __iadd__(self,theAdd : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Vec4: ...
    @overload
    def __init__(self,theVec3 : Graphic3d_Vec3,theW : float=0.0) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float,theZ : float,theW : float) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theValue : float) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> Graphic3d_Vec4: ...
    def __mul__(self,theFactor : float) -> Graphic3d_Vec4: 
        """
        Compute per-component multiplication.
        """
    def __rmul__(self,theFactor : float) -> Graphic3d_Vec4: 
        """
        Compute per-component multiplication.
        """
    def __sub__(self) -> Graphic3d_Vec4: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> Graphic3d_Vec4: 
        """
        Compute per-component division by scale factor.
        """
    def a(self) -> float: 
        """
        Alias to 4th component as ALPHA channel in RGBA.

        Alias to 4th component as ALPHA channel in RGBA.
        """
    def b(self) -> float: 
        """
        Alias to 3rd component as BLUE channel in RGBA.

        Alias to 3rd component as BLUE channel in RGBA.
        """
    def bgr(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def brg(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def cwiseAbs(self) -> Graphic3d_Vec4: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec4) -> Graphic3d_Vec4: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> float: 
        """
        Alias to 2nd component as GREEN channel in RGBA.

        Alias to 2nd component as GREEN channel in RGBA.
        """
    def gbr(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def grb(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> float: 
        """
        Alias to 1st component as RED channel in RGBA.

        Alias to 1st component as RED channel in RGBA.
        """
    def rbg(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def rgb(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def w(self) -> float: 
        """
        Alias to 4th component as W coordinate in XYZW.

        Alias to 4th component as W coordinate in XYZW.
        """
    def wx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def wxy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def wxz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def wy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def wyx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def wyz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def wz(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def wzx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def wzy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XYZW.

        Alias to 1st component as X coordinate in XYZW.
        """
    def xw(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def xwy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xwz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def xyw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def xzw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XYZW.

        Alias to 2nd component as Y coordinate in XYZW.
        """
    def yw(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def ywx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def ywz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def yx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def yxw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def yzw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def z(self) -> float: 
        """
        Alias to 3rd component as Z coordinate in XYZW.

        Alias to 3rd component as Z coordinate in XYZW.
        """
    def zw(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def zwx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zwy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zx(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def zxw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2: 
        """
        None
        """
    def zyw(self) -> Graphic3d_Vec3: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3: 
        """
        None
        """
    pass
class Graphic3d_Vec4b():
    """
    Generic 4-components vector. To be used as RGBA color vector or XYZW 3D-point with special W-component for operations with projection / model view matrices. Use this class for 3D-points carefully because declared W-component may results in incorrect results if used without matrices.
    """
    def ChangeData(self) -> str: 
        """
        None
        """
    def Dot(self,theOther : Graphic3d_Vec4b) -> str: 
        """
        Computes the dot product.
        """
    def GetData(self) -> str: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec4b) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Multiplied(self,theFactor : str) -> Graphic3d_Vec4b: 
        """
        Compute per-component multiplication.
        """
    def Multiply(self,theFactor : str) -> None: 
        """
        Compute per-component multiplication.
        """
    @overload
    def SetValues(self,theVec3 : Graphic3d_Vec3b,theW : str) -> None: 
        """
        Assign new values to the vector.

        Assign new values as 3-component vector and a 4-th value.
        """
    @overload
    def SetValues(self,theX : str,theY : str,theZ : str,theW : str) -> None: ...
    def __iadd__(self,theAdd : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication.
        """
    @overload
    def __imul__(self,theFactor : str) -> Graphic3d_Vec4b: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theVec3 : Graphic3d_Vec3b,theW : str='\x00') -> None: ...
    @overload
    def __init__(self,theX : str,theY : str,theZ : str,theW : str) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2b) -> None: ...
    @overload
    def __init__(self,theValue : str) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : str) -> Graphic3d_Vec4b: ...
    def __mul__(self,theFactor : str) -> Graphic3d_Vec4b: 
        """
        Compute per-component multiplication.
        """
    def __rmul__(self,theFactor : str) -> Graphic3d_Vec4b: 
        """
        Compute per-component multiplication.
        """
    def __sub__(self) -> Graphic3d_Vec4b: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : str) -> Graphic3d_Vec4b: 
        """
        Compute per-component division by scale factor.
        """
    def a(self) -> str: 
        """
        Alias to 4th component as ALPHA channel in RGBA.

        Alias to 4th component as ALPHA channel in RGBA.
        """
    def b(self) -> str: 
        """
        Alias to 3rd component as BLUE channel in RGBA.

        Alias to 3rd component as BLUE channel in RGBA.
        """
    def bgr(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def brg(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def cwiseAbs(self) -> Graphic3d_Vec4b: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec4b) -> Graphic3d_Vec4b: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> str: 
        """
        Alias to 2nd component as GREEN channel in RGBA.

        Alias to 2nd component as GREEN channel in RGBA.
        """
    def gbr(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def grb(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def maxComp(self) -> str: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> str: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> str: 
        """
        Alias to 1st component as RED channel in RGBA.

        Alias to 1st component as RED channel in RGBA.
        """
    def rbg(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def rgb(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def w(self) -> str: 
        """
        Alias to 4th component as W coordinate in XYZW.

        Alias to 4th component as W coordinate in XYZW.
        """
    def wx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def wxy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def wxz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def wy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def wyx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def wyz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def wz(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def wzx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def wzy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def x(self) -> str: 
        """
        Alias to 1st component as X coordinate in XYZW.

        Alias to 1st component as X coordinate in XYZW.
        """
    def xw(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def xwy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xwz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def xyw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def xzw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def y(self) -> str: 
        """
        Alias to 2nd component as Y coordinate in XYZW.

        Alias to 2nd component as Y coordinate in XYZW.
        """
    def yw(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def ywx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def ywz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def yx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def yxw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def yzw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def z(self) -> str: 
        """
        Alias to 3rd component as Z coordinate in XYZW.

        Alias to 3rd component as Z coordinate in XYZW.
        """
    def zw(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def zwx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zwy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zx(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def zxw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2b: 
        """
        None
        """
    def zyw(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3b: 
        """
        None
        """
    pass
class Graphic3d_Vec4d():
    """
    Generic 4-components vector. To be used as RGBA color vector or XYZW 3D-point with special W-component for operations with projection / model view matrices. Use this class for 3D-points carefully because declared W-component may results in incorrect results if used without matrices.
    """
    def ChangeData(self) -> float: 
        """
        None
        """
    def Dot(self,theOther : Graphic3d_Vec4d) -> float: 
        """
        Computes the dot product.
        """
    def GetData(self) -> float: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec4d) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Multiplied(self,theFactor : float) -> Graphic3d_Vec4d: 
        """
        Compute per-component multiplication.
        """
    def Multiply(self,theFactor : float) -> None: 
        """
        Compute per-component multiplication.
        """
    @overload
    def SetValues(self,theVec3 : OCP.SelectMgr.SelectMgr_Vec3,theW : float) -> None: 
        """
        Assign new values to the vector.

        Assign new values as 3-component vector and a 4-th value.
        """
    @overload
    def SetValues(self,theX : float,theY : float,theZ : float,theW : float) -> None: ...
    def __iadd__(self,theAdd : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : float) -> Graphic3d_Vec4d: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec4d) -> Graphic3d_Vec4d: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theVec3 : OCP.SelectMgr.SelectMgr_Vec3,theW : float=0.0) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float,theZ : float,theW : float) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2d) -> None: ...
    @overload
    def __init__(self,theValue : float) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : float) -> Graphic3d_Vec4d: ...
    def __mul__(self,theFactor : float) -> Graphic3d_Vec4d: 
        """
        Compute per-component multiplication.
        """
    def __rmul__(self,theFactor : float) -> Graphic3d_Vec4d: 
        """
        Compute per-component multiplication.
        """
    def __sub__(self) -> Graphic3d_Vec4d: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : float) -> Graphic3d_Vec4d: 
        """
        Compute per-component division by scale factor.
        """
    def a(self) -> float: 
        """
        Alias to 4th component as ALPHA channel in RGBA.

        Alias to 4th component as ALPHA channel in RGBA.
        """
    def b(self) -> float: 
        """
        Alias to 3rd component as BLUE channel in RGBA.

        Alias to 3rd component as BLUE channel in RGBA.
        """
    def bgr(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def brg(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def cwiseAbs(self) -> Graphic3d_Vec4d: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec4d) -> Graphic3d_Vec4d: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> float: 
        """
        Alias to 2nd component as GREEN channel in RGBA.

        Alias to 2nd component as GREEN channel in RGBA.
        """
    def gbr(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def grb(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def maxComp(self) -> float: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> float: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> float: 
        """
        Alias to 1st component as RED channel in RGBA.

        Alias to 1st component as RED channel in RGBA.
        """
    def rbg(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def rgb(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def w(self) -> float: 
        """
        Alias to 4th component as W coordinate in XYZW.

        Alias to 4th component as W coordinate in XYZW.
        """
    def wx(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def wxy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def wxz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def wy(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def wyx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def wyz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def wz(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def wzx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def wzy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def x(self) -> float: 
        """
        Alias to 1st component as X coordinate in XYZW.

        Alias to 1st component as X coordinate in XYZW.
        """
    def xw(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def xwy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def xwz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def xy(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def xyw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def xyz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def xzw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def xzy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def y(self) -> float: 
        """
        Alias to 2nd component as Y coordinate in XYZW.

        Alias to 2nd component as Y coordinate in XYZW.
        """
    def yw(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def ywx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def ywz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def yx(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def yxw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def yxz(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def yzw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def yzx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def z(self) -> float: 
        """
        Alias to 3rd component as Z coordinate in XYZW.

        Alias to 3rd component as Z coordinate in XYZW.
        """
    def zw(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def zwx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def zwy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def zx(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def zxw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def zxy(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2d: 
        """
        None
        """
    def zyw(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    def zyx(self) -> OCP.SelectMgr.SelectMgr_Vec3: 
        """
        None
        """
    pass
class Graphic3d_Vec4i():
    """
    Generic 4-components vector. To be used as RGBA color vector or XYZW 3D-point with special W-component for operations with projection / model view matrices. Use this class for 3D-points carefully because declared W-component may results in incorrect results if used without matrices.
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    def Dot(self,theOther : Graphic3d_Vec4i) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec4i) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec4i: 
        """
        Compute per-component multiplication.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication.
        """
    @overload
    def SetValues(self,theVec3 : Graphic3d_Vec3i,theW : int) -> None: 
        """
        Assign new values to the vector.

        Assign new values as 3-component vector and a 4-th value.
        """
    @overload
    def SetValues(self,theX : int,theY : int,theZ : int,theW : int) -> None: ...
    def __iadd__(self,theAdd : Graphic3d_Vec4i) -> Graphic3d_Vec4i: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec4i: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec4i) -> Graphic3d_Vec4i: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theX : int,theY : int,theZ : int,theW : int) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2i) -> None: ...
    @overload
    def __init__(self,theValue : int) -> None: ...
    @overload
    def __init__(self,theVec3 : Graphic3d_Vec3i,theW : int=0) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec4i) -> Graphic3d_Vec4i: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec4i) -> Graphic3d_Vec4i: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec4i: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec4i: 
        """
        Compute per-component multiplication.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec4i: 
        """
        Compute per-component multiplication.
        """
    def __sub__(self) -> Graphic3d_Vec4i: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec4i: 
        """
        Compute per-component division by scale factor.
        """
    def a(self) -> int: 
        """
        Alias to 4th component as ALPHA channel in RGBA.

        Alias to 4th component as ALPHA channel in RGBA.
        """
    def b(self) -> int: 
        """
        Alias to 3rd component as BLUE channel in RGBA.

        Alias to 3rd component as BLUE channel in RGBA.
        """
    def bgr(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def brg(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def cwiseAbs(self) -> Graphic3d_Vec4i: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec4i) -> Graphic3d_Vec4i: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec4i) -> Graphic3d_Vec4i: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> int: 
        """
        Alias to 2nd component as GREEN channel in RGBA.

        Alias to 2nd component as GREEN channel in RGBA.
        """
    def gbr(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def grb(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> int: 
        """
        Alias to 1st component as RED channel in RGBA.

        Alias to 1st component as RED channel in RGBA.
        """
    def rbg(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def rgb(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def w(self) -> int: 
        """
        Alias to 4th component as W coordinate in XYZW.

        Alias to 4th component as W coordinate in XYZW.
        """
    def wx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def wxy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def wxz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def wy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def wyx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def wyz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def wz(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def wzx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def wzy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XYZW.

        Alias to 1st component as X coordinate in XYZW.
        """
    def xw(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def xwy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xwz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def xyw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def xzw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XYZW.

        Alias to 2nd component as Y coordinate in XYZW.
        """
    def yw(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def ywx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def ywz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def yx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def yxw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def yzw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def z(self) -> int: 
        """
        Alias to 3rd component as Z coordinate in XYZW.

        Alias to 3rd component as Z coordinate in XYZW.
        """
    def zw(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def zwx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zwy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zx(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def zxw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2i: 
        """
        None
        """
    def zyw(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3i: 
        """
        None
        """
    pass
class Graphic3d_Vec4ub():
    """
    Generic 4-components vector. To be used as RGBA color vector or XYZW 3D-point with special W-component for operations with projection / model view matrices. Use this class for 3D-points carefully because declared W-component may results in incorrect results if used without matrices.
    """
    def ChangeData(self) -> int: 
        """
        None
        """
    def Dot(self,theOther : Graphic3d_Vec4ub) -> int: 
        """
        Computes the dot product.
        """
    def GetData(self) -> int: 
        """
        Raw access to the data (for OpenGL exchange).
        """
    def IsEqual(self,theOther : Graphic3d_Vec4ub) -> bool: 
        """
        Check this vector with another vector for equality (without tolerance!).
        """
    @staticmethod
    def Length_s() -> int: 
        """
        Returns the number of components.
        """
    def Multiplied(self,theFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component multiplication.
        """
    def Multiply(self,theFactor : int) -> None: 
        """
        Compute per-component multiplication.
        """
    @overload
    def SetValues(self,theVec3 : Graphic3d_Vec3ub,theW : int) -> None: 
        """
        Assign new values to the vector.

        Assign new values as 3-component vector and a 4-th value.
        """
    @overload
    def SetValues(self,theX : int,theY : int,theZ : int,theW : int) -> None: ...
    def __iadd__(self,theAdd : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: 
        """
        Compute per-component summary.
        """
    @overload
    def __imul__(self,theFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component multiplication.

        Compute per-component multiplication.
        """
    @overload
    def __imul__(self,theRight : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: ...
    @overload
    def __init__(self,theX : int,theY : int,theZ : int,theW : int) -> None: ...
    @overload
    def __init__(self,theVec3 : Graphic3d_Vec3ub,theW : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theVec2 : Graphic3d_Vec2ub) -> None: ...
    @overload
    def __init__(self,theValue : int) -> None: ...
    def __isub__(self,theDec : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: 
        """
        Compute per-component subtraction.
        """
    @overload
    def __itruediv__(self,theInvFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component division by scale factor.

        Compute per-component division.
        """
    @overload
    def __itruediv__(self,theRight : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: ...
    def __mul__(self,theFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component multiplication.
        """
    def __rmul__(self,theFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component multiplication.
        """
    def __sub__(self) -> Graphic3d_Vec4ub: 
        """
        Unary -.
        """
    def __truediv__(self,theInvFactor : int) -> Graphic3d_Vec4ub: 
        """
        Compute per-component division by scale factor.
        """
    def a(self) -> int: 
        """
        Alias to 4th component as ALPHA channel in RGBA.

        Alias to 4th component as ALPHA channel in RGBA.
        """
    def b(self) -> int: 
        """
        Alias to 3rd component as BLUE channel in RGBA.

        Alias to 3rd component as BLUE channel in RGBA.
        """
    def bgr(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def brg(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def cwiseAbs(self) -> Graphic3d_Vec4ub: 
        """
        Compute component-wise modulus of the vector.
        """
    def cwiseMax(self,theVec : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: 
        """
        Compute component-wise maximum of two vectors.
        """
    def cwiseMin(self,theVec : Graphic3d_Vec4ub) -> Graphic3d_Vec4ub: 
        """
        Compute component-wise minimum of two vectors.
        """
    def g(self) -> int: 
        """
        Alias to 2nd component as GREEN channel in RGBA.

        Alias to 2nd component as GREEN channel in RGBA.
        """
    def gbr(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def grb(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def maxComp(self) -> int: 
        """
        Compute maximum component of the vector.
        """
    def minComp(self) -> int: 
        """
        Compute minimum component of the vector.
        """
    def r(self) -> int: 
        """
        Alias to 1st component as RED channel in RGBA.

        Alias to 1st component as RED channel in RGBA.
        """
    def rbg(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def rgb(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def w(self) -> int: 
        """
        Alias to 4th component as W coordinate in XYZW.

        Alias to 4th component as W coordinate in XYZW.
        """
    def wx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def wxy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def wxz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def wy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def wyx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def wyz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def wz(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def wzx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def wzy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def x(self) -> int: 
        """
        Alias to 1st component as X coordinate in XYZW.

        Alias to 1st component as X coordinate in XYZW.
        """
    def xw(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def xwy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xwz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def xyw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xyz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xz(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def xzw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def xzy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def y(self) -> int: 
        """
        Alias to 2nd component as Y coordinate in XYZW.

        Alias to 2nd component as Y coordinate in XYZW.
        """
    def yw(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def ywx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def ywz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def yx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def yxw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def yxz(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def yz(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def yzw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def yzx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def z(self) -> int: 
        """
        Alias to 3rd component as Z coordinate in XYZW.

        Alias to 3rd component as Z coordinate in XYZW.
        """
    def zw(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def zwx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zwy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zx(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def zxw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zxy(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zy(self) -> Graphic3d_Vec2ub: 
        """
        None
        """
    def zyw(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    def zyx(self) -> Graphic3d_Vec3ub: 
        """
        None
        """
    pass
class Graphic3d_Vertex():
    """
    This class represents a graphical 3D point.
    """
    @overload
    def Coord(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Returns the coordinates.

        Returns the coordinates.
        """
    @overload
    def Coord(self) -> Tuple[float, float, float]: ...
    def Distance(self,theOther : Graphic3d_Vertex) -> float: 
        """
        Returns the distance between two points.
        """
    def SetCoord(self,theX : float,theY : float,theZ : float) -> None: 
        """
        Modifies the coordinates.

        Modifies the coordinates.
        """
    def X(self) -> float: 
        """
        Returns the X coordinates.
        """
    def Y(self) -> float: 
        """
        Returns the Y coordinate.
        """
    def Z(self) -> float: 
        """
        Returns the Z coordinate.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,thePoint : Graphic3d_Vertex) -> None: ...
    @overload
    def __init__(self,theX : float,theY : float,theZ : float) -> None: ...
    pass
class Graphic3d_VerticalTextAlignment():
    """
    Defines the vertical position of the text relative to its anchor.

    Members:

      Graphic3d_VTA_BOTTOM

      Graphic3d_VTA_CENTER

      Graphic3d_VTA_TOP

      Graphic3d_VTA_TOPFIRSTLINE
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_VTA_BOTTOM: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM
    Graphic3d_VTA_CENTER: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_CENTER
    Graphic3d_VTA_TOP: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOP
    Graphic3d_VTA_TOPFIRSTLINE: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOPFIRSTLINE
    __entries: dict # value = {'Graphic3d_VTA_BOTTOM': (Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM, None), 'Graphic3d_VTA_CENTER': (Graphic3d_VerticalTextAlignment.Graphic3d_VTA_CENTER, None), 'Graphic3d_VTA_TOP': (Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOP, None), 'Graphic3d_VTA_TOPFIRSTLINE': (Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOPFIRSTLINE, None)}
    __members__: dict # value = {'Graphic3d_VTA_BOTTOM': Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM, 'Graphic3d_VTA_CENTER': Graphic3d_VerticalTextAlignment.Graphic3d_VTA_CENTER, 'Graphic3d_VTA_TOP': Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOP, 'Graphic3d_VTA_TOPFIRSTLINE': Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOPFIRSTLINE}
    pass
class Graphic3d_ViewAffinity(OCP.Standard.Standard_Transient):
    """
    Structure display state.Structure display state.
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
    def IsVisible(self,theViewId : int) -> bool: 
        """
        Return visibility flag.
        """
    @overload
    def SetVisible(self,theIsVisible : bool) -> None: 
        """
        Setup visibility flag for all views.

        Setup visibility flag.
        """
    @overload
    def SetVisible(self,theViewId : int,theIsVisible : bool) -> None: ...
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
class Graphic3d_WorldViewProjState():
    """
    Helper class for keeping reference on world-view-projection state. Helpful for synchronizing state of WVP dependent data structures.
    """
    @overload
    def Initialize(self,theCamera : OCP.Standard.Standard_Transient=None) -> None: 
        """
        Initialize world view projection state.

        Initialize world view projection state.
        """
    @overload
    def Initialize(self,theProjectionState : int,theWorldViewState : int,theCamera : OCP.Standard.Standard_Transient=None) -> None: ...
    def IsChanged(self,theState : Graphic3d_WorldViewProjState) -> bool: 
        """
        Compare with other world view projection state.
        """
    def IsProjectionChanged(self,theState : Graphic3d_WorldViewProjState) -> bool: 
        """
        Compare projection with other state.
        """
    def IsValid(self) -> bool: 
        """
        Check state validity.
        """
    def IsWorldViewChanged(self,theState : Graphic3d_WorldViewProjState) -> bool: 
        """
        Compare world view transformation with other state.
        """
    def ProjectionState(self) -> int: 
        """
        Returns projection state counter.
        """
    def Reset(self) -> None: 
        """
        Invalidate world view projection state.
        """
    def WorldViewState(self) -> int: 
        """
        Returns world view state counter.
        """
    @overload
    def __init__(self,theProjectionState : int,theWorldViewState : int,theCamera : OCP.Standard.Standard_Transient=None) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Graphic3d_ZLayerSetting():
    """
    None

    Members:

      Graphic3d_ZLayerDepthTest

      Graphic3d_ZLayerDepthWrite

      Graphic3d_ZLayerDepthClear

      Graphic3d_ZLayerDepthOffset
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Graphic3d_ZLayerDepthClear: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthClear
    Graphic3d_ZLayerDepthOffset: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthOffset
    Graphic3d_ZLayerDepthTest: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthTest
    Graphic3d_ZLayerDepthWrite: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthWrite
    __entries: dict # value = {'Graphic3d_ZLayerDepthTest': (Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthTest, None), 'Graphic3d_ZLayerDepthWrite': (Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthWrite, None), 'Graphic3d_ZLayerDepthClear': (Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthClear, None), 'Graphic3d_ZLayerDepthOffset': (Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthOffset, None)}
    __members__: dict # value = {'Graphic3d_ZLayerDepthTest': Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthTest, 'Graphic3d_ZLayerDepthWrite': Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthWrite, 'Graphic3d_ZLayerDepthClear': Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthClear, 'Graphic3d_ZLayerDepthOffset': Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthOffset}
    pass
class Graphic3d_ZLayerSettings():
    """
    Structure defines list of ZLayer properties.
    """
    def ChangePolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Modify glPolygonOffset() arguments.
        """
    def CullingDistance(self) -> float: 
        """
        Return the distance to discard drawing of distant objects (distance from camera Eye point); by default it is Infinite (distance culling is disabled). Since camera eye definition has no strong meaning within orthographic projection, option is considered only within perspective projection. Note also that this option has effect only when frustum culling is enabled.
        """
    def CullingSize(self) -> float: 
        """
        Return the size to discard drawing of small objects; by default it is Infinite (size culling is disabled). Current implementation checks the length of projected diagonal of bounding box in pixels for discarding. Note that this option has effect only when frustum culling is enabled.
        """
    def DisableSetting(self,theSetting : Graphic3d_ZLayerSetting) -> None: 
        """
        Disables theSetting
        """
    def EnableSetting(self,theSetting : Graphic3d_ZLayerSetting) -> None: 
        """
        Enables theSetting
        """
    def HasCullingDistance(self) -> bool: 
        """
        Return TRUE, if culling of distant objects (distance culling) should be performed; FALSE by default.
        """
    def HasCullingSize(self) -> bool: 
        """
        Return TRUE, if culling of small objects (size culling) should be performed; FALSE by default.
        """
    def IsImmediate(self) -> bool: 
        """
        Return true if this layer should be drawn after all normal (non-immediate) layers.
        """
    def IsRaytracable(self) -> bool: 
        """
        Returns TRUE if layer should be processed by ray-tracing renderer; TRUE by default. Note that this flag is IGNORED for layers with IsImmediate() flag.
        """
    def IsSettingEnabled(self,theSetting : Graphic3d_ZLayerSetting) -> bool: 
        """
        Returns true if theSetting is enabled.
        """
    def Lights(self) -> Graphic3d_LightSet: 
        """
        Return lights list to be used for rendering presentations within this Z-Layer; NULL by default. NULL list (but not empty list!) means that default lights assigned to the View should be used instead of per-layer lights.
        """
    def Name(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Return user-provided name.
        """
    def Origin(self) -> OCP.gp.gp_XYZ: 
        """
        Return the origin of all objects within the layer.
        """
    def OriginTransformation(self) -> OCP.Geom.Geom_Transformation: 
        """
        Return the transformation to the origin.
        """
    def PolygonOffset(self) -> Graphic3d_PolygonOffset: 
        """
        Return glPolygonOffset() arguments.
        """
    def SetClearDepth(self,theValue : bool) -> None: 
        """
        Set if depth values should be cleared before drawing the layer.
        """
    def SetCullingDistance(self,theDistance : float) -> None: 
        """
        Set the distance to discard drawing objects.
        """
    def SetCullingSize(self,theSize : float) -> None: 
        """
        Set the distance to discard drawing objects.
        """
    def SetDepthOffsetNegative(self) -> None: 
        """
        Sets minimal possible negative depth offset.
        """
    def SetDepthOffsetPositive(self) -> None: 
        """
        Sets minimal possible positive depth offset.
        """
    def SetEnableDepthTest(self,theValue : bool) -> None: 
        """
        Set if depth test should be enabled.
        """
    def SetEnableDepthWrite(self,theValue : bool) -> None: 
        """
        Set if depth values should be written during rendering.
        """
    def SetEnvironmentTexture(self,theValue : bool) -> None: 
        """
        Set the flag to allow/prevent environment texture mapping usage for specific layer.
        """
    def SetImmediate(self,theValue : bool) -> None: 
        """
        Set the flag indicating the immediate layer, which should be drawn after all normal (non-immediate) layers.
        """
    def SetLights(self,theLights : Graphic3d_LightSet) -> None: 
        """
        Assign lights list to be used.
        """
    def SetName(self,theName : OCP.TCollection.TCollection_AsciiString) -> None: 
        """
        Set custom name.
        """
    def SetOrigin(self,theOrigin : OCP.gp.gp_XYZ) -> None: 
        """
        Set the origin of all objects within the layer.
        """
    def SetPolygonOffset(self,theParams : Graphic3d_PolygonOffset) -> None: 
        """
        Setup glPolygonOffset() arguments.
        """
    def SetRaytracable(self,theToRaytrace : bool) -> None: 
        """
        Sets if layer should be processed by ray-tracing renderer.
        """
    def SetRenderInDepthPrepass(self,theToRender : bool) -> None: 
        """
        Set if layer should be rendered within depth pre-pass.
        """
    def ToClearDepth(self) -> bool: 
        """
        Return true if depth values should be cleared before drawing the layer.
        """
    def ToEnableDepthTest(self) -> bool: 
        """
        Return true if depth test should be enabled.
        """
    def ToEnableDepthWrite(self) -> bool: 
        """
        Return true depth values should be written during rendering.
        """
    def ToRenderInDepthPrepass(self) -> bool: 
        """
        Return TRUE if layer should be rendered within depth pre-pass; TRUE by default.
        """
    def UseEnvironmentTexture(self) -> bool: 
        """
        Return flag to allow/prevent environment texture mapping usage for specific layer.
        """
    def __init__(self) -> None: ...
    pass
Graphic3d_ASPECT_FILL_AREA: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_FILL_AREA
Graphic3d_ASPECT_LINE: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_LINE
Graphic3d_ASPECT_MARKER: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_MARKER
Graphic3d_ASPECT_TEXT: OCP.Graphic3d.Graphic3d_GroupAspect # value = Graphic3d_GroupAspect.Graphic3d_ASPECT_TEXT
Graphic3d_AlphaMode_Blend: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Blend
Graphic3d_AlphaMode_BlendAuto: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_BlendAuto
Graphic3d_AlphaMode_Mask: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Mask
Graphic3d_AlphaMode_Opaque: OCP.Graphic3d.Graphic3d_AlphaMode # value = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Opaque
Graphic3d_ArrayFlags_AttribsDeinterleaved = 64
Graphic3d_ArrayFlags_AttribsMutable = 32
Graphic3d_ArrayFlags_BoundColor = 16
Graphic3d_ArrayFlags_IndexesMutable = 128
Graphic3d_ArrayFlags_None = 0
Graphic3d_ArrayFlags_VertexColor = 2
Graphic3d_ArrayFlags_VertexNormal = 1
Graphic3d_ArrayFlags_VertexTexel = 4
Graphic3d_BT_Depth: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_Depth
Graphic3d_BT_RGB: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGB
Graphic3d_BT_RGBA: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGBA
Graphic3d_BT_RGB_RayTraceHdrLeft: OCP.Graphic3d.Graphic3d_BufferType # value = Graphic3d_BufferType.Graphic3d_BT_RGB_RayTraceHdrLeft
Graphic3d_CMS_NEG_X: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_X
Graphic3d_CMS_NEG_Y: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Y
Graphic3d_CMS_NEG_Z: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Z
Graphic3d_CMS_POS_X: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_X
Graphic3d_CMS_POS_Y: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Y
Graphic3d_CMS_POS_Z: OCP.Graphic3d.Graphic3d_CubeMapSide # value = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Z
Graphic3d_CappingFlags_None: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_None
Graphic3d_CappingFlags_ObjectAspect: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectAspect
Graphic3d_CappingFlags_ObjectMaterial: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectMaterial
Graphic3d_CappingFlags_ObjectShader: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectShader
Graphic3d_CappingFlags_ObjectTexture: OCP.Graphic3d.Graphic3d_CappingFlags # value = Graphic3d_CappingFlags.Graphic3d_CappingFlags_ObjectTexture
Graphic3d_ClipState_In: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_In
Graphic3d_ClipState_On: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_On
Graphic3d_ClipState_Out: OCP.Graphic3d.Graphic3d_ClipState # value = Graphic3d_ClipState.Graphic3d_ClipState_Out
Graphic3d_DiagnosticInfo_Basic: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Basic
Graphic3d_DiagnosticInfo_Complete: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Complete
Graphic3d_DiagnosticInfo_Device: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Device
Graphic3d_DiagnosticInfo_Extensions: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Extensions
Graphic3d_DiagnosticInfo_FrameBuffer: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_FrameBuffer
Graphic3d_DiagnosticInfo_Limits: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Limits
Graphic3d_DiagnosticInfo_Memory: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Memory
Graphic3d_DiagnosticInfo_NativePlatform: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_NativePlatform
Graphic3d_DiagnosticInfo_Short: OCP.Graphic3d.Graphic3d_DiagnosticInfo # value = Graphic3d_DiagnosticInfo.Graphic3d_DiagnosticInfo_Short
Graphic3d_FM_CONDUCTOR: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_CONDUCTOR
Graphic3d_FM_CONSTANT: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_CONSTANT
Graphic3d_FM_DIELECTRIC: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_DIELECTRIC
Graphic3d_FM_SCHLICK: OCP.Graphic3d.Graphic3d_FresnelModel # value = Graphic3d_FresnelModel.Graphic3d_FM_SCHLICK
Graphic3d_FrameStatsCounter_EstimatedBytesFbos: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesFbos
Graphic3d_FrameStatsCounter_EstimatedBytesGeom: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesGeom
Graphic3d_FrameStatsCounter_EstimatedBytesTextures: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_EstimatedBytesTextures
Graphic3d_FrameStatsCounter_NB = 15
Graphic3d_FrameStatsCounter_NbElemsFillNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsFillNotCulled
Graphic3d_FrameStatsCounter_NbElemsLineNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsLineNotCulled
Graphic3d_FrameStatsCounter_NbElemsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsNotCulled
Graphic3d_FrameStatsCounter_NbElemsPointNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsPointNotCulled
Graphic3d_FrameStatsCounter_NbElemsTextNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbElemsTextNotCulled
Graphic3d_FrameStatsCounter_NbGroupsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbGroupsNotCulled
Graphic3d_FrameStatsCounter_NbLayers: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayers
Graphic3d_FrameStatsCounter_NbLayersNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbLayersNotCulled
Graphic3d_FrameStatsCounter_NbPointsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbPointsNotCulled
Graphic3d_FrameStatsCounter_NbStructs: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructs
Graphic3d_FrameStatsCounter_NbStructsNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbStructsNotCulled
Graphic3d_FrameStatsCounter_NbTrianglesNotCulled: OCP.Graphic3d.Graphic3d_FrameStatsCounter # value = Graphic3d_FrameStatsCounter.Graphic3d_FrameStatsCounter_NbTrianglesNotCulled
Graphic3d_FrameStatsTimer_CpuCulling: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuCulling
Graphic3d_FrameStatsTimer_CpuDynamics: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuDynamics
Graphic3d_FrameStatsTimer_CpuFrame: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuFrame
Graphic3d_FrameStatsTimer_CpuPicking: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_CpuPicking
Graphic3d_FrameStatsTimer_ElapsedFrame: OCP.Graphic3d.Graphic3d_FrameStatsTimer # value = Graphic3d_FrameStatsTimer.Graphic3d_FrameStatsTimer_ElapsedFrame
Graphic3d_FrameStatsTimer_NB = 5
Graphic3d_HTA_CENTER: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_CENTER
Graphic3d_HTA_LEFT: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_LEFT
Graphic3d_HTA_RIGHT: OCP.Graphic3d.Graphic3d_HorizontalTextAlignment # value = Graphic3d_HorizontalTextAlignment.Graphic3d_HTA_RIGHT
Graphic3d_LOTA_FAST: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_FAST
Graphic3d_LOTA_MIDDLE: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_MIDDLE
Graphic3d_LOTA_OFF: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_OFF
Graphic3d_LOTA_QUALITY: OCP.Graphic3d.Graphic3d_LevelOfTextureAnisotropy # value = Graphic3d_LevelOfTextureAnisotropy.Graphic3d_LOTA_QUALITY
Graphic3d_MATERIAL_ASPECT: OCP.Graphic3d.Graphic3d_TypeOfMaterial # value = Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_ASPECT
Graphic3d_MATERIAL_PHYSIC: OCP.Graphic3d.Graphic3d_TypeOfMaterial # value = Graphic3d_TypeOfMaterial.Graphic3d_MATERIAL_PHYSIC
Graphic3d_NOM_ALUMINIUM: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_ALUMINIUM
Graphic3d_NOM_BRASS: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRASS
Graphic3d_NOM_BRONZE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRONZE
Graphic3d_NOM_CHARCOAL: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHARCOAL
Graphic3d_NOM_CHROME: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHROME
Graphic3d_NOM_COPPER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_COPPER
Graphic3d_NOM_DEFAULT: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_DEFAULT
Graphic3d_NOM_DIAMOND: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_DIAMOND
Graphic3d_NOM_GLASS: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_GLASS
Graphic3d_NOM_GOLD: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_GOLD
Graphic3d_NOM_JADE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_JADE
Graphic3d_NOM_METALIZED: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED
Graphic3d_NOM_NEON_GNC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_GNC
Graphic3d_NOM_NEON_PHC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_PHC
Graphic3d_NOM_OBSIDIAN: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_OBSIDIAN
Graphic3d_NOM_PEWTER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PEWTER
Graphic3d_NOM_PLASTER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTER
Graphic3d_NOM_PLASTIC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTIC
Graphic3d_NOM_SATIN: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SATIN
Graphic3d_NOM_SHINY_PLASTIC: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SHINY_PLASTIC
Graphic3d_NOM_SILVER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_SILVER
Graphic3d_NOM_STEEL: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_STEEL
Graphic3d_NOM_STONE: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_STONE
Graphic3d_NOM_TRANSPARENT: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_TRANSPARENT
Graphic3d_NOM_UserDefined: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_UserDefined
Graphic3d_NOM_WATER: OCP.Graphic3d.Graphic3d_NameOfMaterial # value = Graphic3d_NameOfMaterial.Graphic3d_NOM_WATER
Graphic3d_NOTP_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_UNKNOWN
Graphic3d_NOTP_XY: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_XY
Graphic3d_NOTP_YZ: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_YZ
Graphic3d_NOTP_ZX: OCP.Graphic3d.Graphic3d_NameOfTexturePlane # value = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_ZX
Graphic3d_NOT_1D_ELEVATION: OCP.Graphic3d.Graphic3d_NameOfTexture1D # value = Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_ELEVATION
Graphic3d_NOT_1D_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexture1D # value = Graphic3d_NameOfTexture1D.Graphic3d_NOT_1D_UNKNOWN
Graphic3d_NOT_2D_ALIENSKIN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALIENSKIN
Graphic3d_NOT_2D_ALUMINUM: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ALUMINUM
Graphic3d_NOT_2D_BLUEWHITE_PAPER: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUEWHITE_PAPER
Graphic3d_NOT_2D_BLUE_ROCK: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BLUE_ROCK
Graphic3d_NOT_2D_BRUSHED: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BRUSHED
Graphic3d_NOT_2D_BUBBLES: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUBBLES
Graphic3d_NOT_2D_BUMP: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUMP
Graphic3d_NOT_2D_CAST: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CAST
Graphic3d_NOT_2D_CHESS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHESS
Graphic3d_NOT_2D_CHIPBD: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHIPBD
Graphic3d_NOT_2D_CLOUDS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CLOUDS
Graphic3d_NOT_2D_FLESH: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLESH
Graphic3d_NOT_2D_FLOOR: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLOOR
Graphic3d_NOT_2D_GALVNISD: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GALVNISD
Graphic3d_NOT_2D_GRASS: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GRASS
Graphic3d_NOT_2D_KNURL: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_KNURL
Graphic3d_NOT_2D_MAPLE: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MAPLE
Graphic3d_NOT_2D_MARBLE: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MARBLE
Graphic3d_NOT_2D_MATRA: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MATRA
Graphic3d_NOT_2D_MOTTLED: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MOTTLED
Graphic3d_NOT_2D_RAIN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_RAIN
Graphic3d_NOT_2D_ROCK: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ROCK
Graphic3d_NOT_2D_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTexture2D # value = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_UNKNOWN
Graphic3d_NOT_ENV_CLOUDS: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CLOUDS
Graphic3d_NOT_ENV_CV: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CV
Graphic3d_NOT_ENV_LINES: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_LINES
Graphic3d_NOT_ENV_MEDIT: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_MEDIT
Graphic3d_NOT_ENV_PEARL: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_PEARL
Graphic3d_NOT_ENV_ROAD: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_ROAD
Graphic3d_NOT_ENV_SKY1: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY1
Graphic3d_NOT_ENV_SKY2: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY2
Graphic3d_NOT_ENV_UNKNOWN: OCP.Graphic3d.Graphic3d_NameOfTextureEnv # value = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_UNKNOWN
Graphic3d_RM_RASTERIZATION: OCP.Graphic3d.Graphic3d_RenderingMode # value = Graphic3d_RenderingMode.Graphic3d_RM_RASTERIZATION
Graphic3d_RM_RAYTRACING: OCP.Graphic3d.Graphic3d_RenderingMode # value = Graphic3d_RenderingMode.Graphic3d_RM_RAYTRACING
Graphic3d_RTM_BLEND_OIT: OCP.Graphic3d.Graphic3d_RenderTransparentMethod # value = Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_OIT
Graphic3d_RTM_BLEND_UNORDERED: OCP.Graphic3d.Graphic3d_RenderTransparentMethod # value = Graphic3d_RenderTransparentMethod.Graphic3d_RTM_BLEND_UNORDERED
Graphic3d_StereoMode_Anaglyph: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_Anaglyph
Graphic3d_StereoMode_ChessBoard: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_ChessBoard
Graphic3d_StereoMode_ColumnInterlaced: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_ColumnInterlaced
Graphic3d_StereoMode_NB: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_NB
Graphic3d_StereoMode_OverUnder: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_OverUnder
Graphic3d_StereoMode_QuadBuffer: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_QuadBuffer
Graphic3d_StereoMode_RowInterlaced: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_RowInterlaced
Graphic3d_StereoMode_SideBySide: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_SideBySide
Graphic3d_StereoMode_SoftPageFlip: OCP.Graphic3d.Graphic3d_StereoMode # value = Graphic3d_StereoMode.Graphic3d_StereoMode_SoftPageFlip
Graphic3d_TMF_2d: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_2d
Graphic3d_TMF_None: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_None
Graphic3d_TMF_RotatePers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_RotatePers
Graphic3d_TMF_TriedronPers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_TriedronPers
Graphic3d_TMF_ZoomPers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomPers
Graphic3d_TMF_ZoomRotatePers: OCP.Graphic3d.Graphic3d_TransModeFlags # value = Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomRotatePers
Graphic3d_TOA_COLOR: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_COLOR
Graphic3d_TOA_COMPUTE: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_COMPUTE
Graphic3d_TOA_CUSTOM: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_CUSTOM
Graphic3d_TOA_NO: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_NO
Graphic3d_TOA_NORM: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_NORM
Graphic3d_TOA_POS: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_POS
Graphic3d_TOA_UV: OCP.Graphic3d.Graphic3d_TypeOfAttribute # value = Graphic3d_TypeOfAttribute.Graphic3d_TOA_UV
Graphic3d_TOA_YES: OCP.Graphic3d.Graphic3d_TypeOfAnswer # value = Graphic3d_TypeOfAnswer.Graphic3d_TOA_YES
Graphic3d_TOBM_AUTOMATIC: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_AUTOMATIC
Graphic3d_TOBM_DISABLE: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_DISABLE
Graphic3d_TOBM_FORCE: OCP.Graphic3d.Graphic3d_TypeOfBackfacingModel # value = Graphic3d_TypeOfBackfacingModel.Graphic3d_TOBM_FORCE
Graphic3d_TOB_CUBEMAP: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_CUBEMAP
Graphic3d_TOB_GRADIENT: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_GRADIENT
Graphic3d_TOB_NONE: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_NONE
Graphic3d_TOB_TEXTURE: OCP.Graphic3d.Graphic3d_TypeOfBackground # value = Graphic3d_TypeOfBackground.Graphic3d_TOB_TEXTURE
Graphic3d_TOC_ANCESTOR: OCP.Graphic3d.Graphic3d_TypeOfConnection # value = Graphic3d_TypeOfConnection.Graphic3d_TOC_ANCESTOR
Graphic3d_TOC_DESCENDANT: OCP.Graphic3d.Graphic3d_TypeOfConnection # value = Graphic3d_TypeOfConnection.Graphic3d_TOC_DESCENDANT
Graphic3d_TOC_POSTCONCATENATE: OCP.Graphic3d.Graphic3d_TypeOfComposition # value = Graphic3d_TypeOfComposition.Graphic3d_TOC_POSTCONCATENATE
Graphic3d_TOC_REPLACE: OCP.Graphic3d.Graphic3d_TypeOfComposition # value = Graphic3d_TypeOfComposition.Graphic3d_TOC_REPLACE
Graphic3d_TOD_FLOAT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_FLOAT
Graphic3d_TOD_UINT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_UINT
Graphic3d_TOD_USHORT: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_USHORT
Graphic3d_TOD_VEC2: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC2
Graphic3d_TOD_VEC3: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC3
Graphic3d_TOD_VEC4: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4
Graphic3d_TOD_VEC4UB: OCP.Graphic3d.Graphic3d_TypeOfData # value = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4UB
Graphic3d_TOLS_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT
Graphic3d_TOLS_DIRECTIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL
Graphic3d_TOLS_POSITIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL
Graphic3d_TOLS_SPOT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT
Graphic3d_TOPA_LINES_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINES_ADJACENCY
Graphic3d_TOPA_LINE_STRIP_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_LINE_STRIP_ADJACENCY
Graphic3d_TOPA_POINTS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POINTS
Graphic3d_TOPA_POLYGONS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYGONS
Graphic3d_TOPA_POLYLINES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_POLYLINES
Graphic3d_TOPA_QUADRANGLES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLES
Graphic3d_TOPA_QUADRANGLESTRIPS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_QUADRANGLESTRIPS
Graphic3d_TOPA_SEGMENTS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_SEGMENTS
Graphic3d_TOPA_TRIANGLEFANS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLEFANS
Graphic3d_TOPA_TRIANGLES: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES
Graphic3d_TOPA_TRIANGLESTRIPS: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLESTRIPS
Graphic3d_TOPA_TRIANGLES_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLES_ADJACENCY
Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY
Graphic3d_TOPA_UNDEFINED: OCP.Graphic3d.Graphic3d_TypeOfPrimitiveArray # value = Graphic3d_TypeOfPrimitiveArray.Graphic3d_TOPA_UNDEFINED
Graphic3d_TOR_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_AMBIENT
Graphic3d_TOR_DIFFUSE: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_DIFFUSE
Graphic3d_TOR_EMISSION: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_EMISSION
Graphic3d_TOR_SPECULAR: OCP.Graphic3d.Graphic3d_TypeOfReflection # value = Graphic3d_TypeOfReflection.Graphic3d_TOR_SPECULAR
Graphic3d_TOSM_DEFAULT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_DEFAULT
Graphic3d_TOSM_FACET: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET
Graphic3d_TOSM_FRAGMENT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT
Graphic3d_TOSM_NONE: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
Graphic3d_TOSM_UNLIT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
Graphic3d_TOSM_VERTEX: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX
Graphic3d_TOS_ALL: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_ALL
Graphic3d_TOS_COMPUTE: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_COMPUTE
Graphic3d_TOS_COMPUTED: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_COMPUTED
Graphic3d_TOS_FRAGMENT: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_FRAGMENT
Graphic3d_TOS_GEOMETRY: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_GEOMETRY
Graphic3d_TOS_SHADING: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_SHADING
Graphic3d_TOS_TESS_CONTROL: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_CONTROL
Graphic3d_TOS_TESS_EVALUATION: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_TESS_EVALUATION
Graphic3d_TOS_VERTEX: OCP.Graphic3d.Graphic3d_TypeOfShaderObject # value = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_VERTEX
Graphic3d_TOS_WIREFRAME: OCP.Graphic3d.Graphic3d_TypeOfStructure # value = Graphic3d_TypeOfStructure.Graphic3d_TOS_WIREFRAME
Graphic3d_TOTF_BILINEAR: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_BILINEAR
Graphic3d_TOTF_NEAREST: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_NEAREST
Graphic3d_TOTF_TRILINEAR: OCP.Graphic3d.Graphic3d_TypeOfTextureFilter # value = Graphic3d_TypeOfTextureFilter.Graphic3d_TOTF_TRILINEAR
Graphic3d_TOTM_EYE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_EYE
Graphic3d_TOTM_MANUAL: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_MANUAL
Graphic3d_TOTM_OBJECT: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_OBJECT
Graphic3d_TOTM_SPHERE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPHERE
Graphic3d_TOTM_SPRITE: OCP.Graphic3d.Graphic3d_TypeOfTextureMode # value = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPRITE
Graphic3d_TOT_1D: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_1D
Graphic3d_TOT_2D: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D
Graphic3d_TOT_2D_MIPMAP: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D_MIPMAP
Graphic3d_TOT_CUBEMAP: OCP.Graphic3d.Graphic3d_TypeOfTexture # value = Graphic3d_TypeOfTexture.Graphic3d_TOT_CUBEMAP
Graphic3d_TOV_SHADING: OCP.Graphic3d.Graphic3d_TypeOfVisualization # value = Graphic3d_TypeOfVisualization.Graphic3d_TOV_SHADING
Graphic3d_TOV_WIREFRAME: OCP.Graphic3d.Graphic3d_TypeOfVisualization # value = Graphic3d_TypeOfVisualization.Graphic3d_TOV_WIREFRAME
Graphic3d_TP_DOWN: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_DOWN
Graphic3d_TP_LEFT: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_LEFT
Graphic3d_TP_RIGHT: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_RIGHT
Graphic3d_TP_UP: OCP.Graphic3d.Graphic3d_TextPath # value = Graphic3d_TextPath.Graphic3d_TP_UP
Graphic3d_TextureUnit_0: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
Graphic3d_TextureUnit_1: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_1
Graphic3d_TextureUnit_10: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_10
Graphic3d_TextureUnit_11: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_11
Graphic3d_TextureUnit_12: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_12
Graphic3d_TextureUnit_13: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_13
Graphic3d_TextureUnit_14: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_14
Graphic3d_TextureUnit_15: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_15
Graphic3d_TextureUnit_2: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_2
Graphic3d_TextureUnit_3: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_3
Graphic3d_TextureUnit_4: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_4
Graphic3d_TextureUnit_5: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_5
Graphic3d_TextureUnit_6: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_6
Graphic3d_TextureUnit_7: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_7
Graphic3d_TextureUnit_8: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_8
Graphic3d_TextureUnit_9: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_9
Graphic3d_TextureUnit_BaseColor: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
Graphic3d_TextureUnit_EnvMap: OCP.Graphic3d.Graphic3d_TextureUnit # value = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0
Graphic3d_TextureUnit_NB = 16
Graphic3d_ToneMappingMethod_Disabled: OCP.Graphic3d.Graphic3d_ToneMappingMethod # value = Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Disabled
Graphic3d_ToneMappingMethod_Filmic: OCP.Graphic3d.Graphic3d_ToneMappingMethod # value = Graphic3d_ToneMappingMethod.Graphic3d_ToneMappingMethod_Filmic
Graphic3d_TypeOfBackground_NB = 3
Graphic3d_TypeOfLightSource_NB = 4
Graphic3d_TypeOfLimit_HasBlendedOit: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOit
Graphic3d_TypeOfLimit_HasBlendedOitMsaa: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasBlendedOitMsaa
Graphic3d_TypeOfLimit_HasFlatShading: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasFlatShading
Graphic3d_TypeOfLimit_HasMeshEdges: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasMeshEdges
Graphic3d_TypeOfLimit_HasRayTracing: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracing
Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling
Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic
Graphic3d_TypeOfLimit_HasRayTracingTextures: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_HasRayTracingTextures
Graphic3d_TypeOfLimit_IsWorkaroundFBO: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_IsWorkaroundFBO
Graphic3d_TypeOfLimit_MaxCombinedTextureUnits: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxCombinedTextureUnits
Graphic3d_TypeOfLimit_MaxMsaa: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxMsaa
Graphic3d_TypeOfLimit_MaxNbClipPlanes: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbClipPlanes
Graphic3d_TypeOfLimit_MaxNbLights: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbLights
Graphic3d_TypeOfLimit_MaxNbViews: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxNbViews
Graphic3d_TypeOfLimit_MaxTextureSize: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxTextureSize
Graphic3d_TypeOfLimit_MaxViewDumpSizeX: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeX
Graphic3d_TypeOfLimit_MaxViewDumpSizeY: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_MaxViewDumpSizeY
Graphic3d_TypeOfLimit_NB: OCP.Graphic3d.Graphic3d_TypeOfLimit # value = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_NB
Graphic3d_TypeOfReflection_NB = 4
Graphic3d_TypeOfShadingModel_NB = 4
Graphic3d_VTA_BOTTOM: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_BOTTOM
Graphic3d_VTA_CENTER: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_CENTER
Graphic3d_VTA_TOP: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOP
Graphic3d_VTA_TOPFIRSTLINE: OCP.Graphic3d.Graphic3d_VerticalTextAlignment # value = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOPFIRSTLINE
Graphic3d_ZLayerDepthClear: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthClear
Graphic3d_ZLayerDepthOffset: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthOffset
Graphic3d_ZLayerDepthTest: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthTest
Graphic3d_ZLayerDepthWrite: OCP.Graphic3d.Graphic3d_ZLayerSetting # value = Graphic3d_ZLayerSetting.Graphic3d_ZLayerDepthWrite
Graphic3d_ZLayerId_BotOSD = -5
Graphic3d_ZLayerId_Default = 0
Graphic3d_ZLayerId_Top = -2
Graphic3d_ZLayerId_TopOSD = -4
Graphic3d_ZLayerId_Topmost = -3
Graphic3d_ZLayerId_UNKNOWN = -1
V3d_AMBIENT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_AMBIENT
V3d_COLOR: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT
V3d_DIRECTIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_DIRECTIONAL
V3d_FLAT: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET
V3d_GOURAUD: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_VERTEX
V3d_PHONG: OCP.Graphic3d.Graphic3d_TypeOfShadingModel # value = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FRAGMENT
V3d_POSITIONAL: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_POSITIONAL
V3d_SPOT: OCP.Graphic3d.Graphic3d_TypeOfLightSource # value = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT
