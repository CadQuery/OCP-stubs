import OCP.VrmlAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Quantity
import OCP.TDocStd
import OCP.TopoDS
import OCP.Vrml
__all__  = [
"VrmlAPI",
"VrmlAPI_RepresentationOfShape",
"VrmlAPI_Writer",
"VrmlAPI_BothRepresentation",
"VrmlAPI_ShadedRepresentation",
"VrmlAPI_WireFrameRepresentation"
]
class VrmlAPI():
    """
    API for writing to VRML 1.0
    """
    @staticmethod
    def Write_s(aShape : OCP.TopoDS.TopoDS_Shape,aFileName : str,aVersion : int=2) -> bool: 
        """
        With help of this class user can change parameters of writing. Converts the shape aShape to VRML format of the passed version and writes it to the file identified by aFileName using default parameters.
        """
    def __init__(self) -> None: ...
    pass
class VrmlAPI_RepresentationOfShape():
    """
    Identifies the representation of the shape written to a VRML file. The available options are : - VrmlAPI_ShadedRepresentation : the shape is translated with a shaded representation. - VrmlAPI_WireFrameRepresentation : the shape is translated with a wireframe representation. - VrmlAPI_BothRepresentation : the shape is translated to VRML format with both representations : shaded and wireframe. This is the default option.

    Members:

      VrmlAPI_ShadedRepresentation

      VrmlAPI_WireFrameRepresentation

      VrmlAPI_BothRepresentation
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
    VrmlAPI_BothRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_BothRepresentation: 2>
    VrmlAPI_ShadedRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_ShadedRepresentation: 0>
    VrmlAPI_WireFrameRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_WireFrameRepresentation: 1>
    __entries: dict # value = {'VrmlAPI_ShadedRepresentation': (<VrmlAPI_RepresentationOfShape.VrmlAPI_ShadedRepresentation: 0>, None), 'VrmlAPI_WireFrameRepresentation': (<VrmlAPI_RepresentationOfShape.VrmlAPI_WireFrameRepresentation: 1>, None), 'VrmlAPI_BothRepresentation': (<VrmlAPI_RepresentationOfShape.VrmlAPI_BothRepresentation: 2>, None)}
    __members__: dict # value = {'VrmlAPI_ShadedRepresentation': <VrmlAPI_RepresentationOfShape.VrmlAPI_ShadedRepresentation: 0>, 'VrmlAPI_WireFrameRepresentation': <VrmlAPI_RepresentationOfShape.VrmlAPI_WireFrameRepresentation: 1>, 'VrmlAPI_BothRepresentation': <VrmlAPI_RepresentationOfShape.VrmlAPI_BothRepresentation: 2>}
    pass
class VrmlAPI_Writer():
    """
    Creates and writes VRML files from Open CASCADE shapes. A VRML file can be written to an existing VRML file or to a new one.
    """
    def Drawer(self) -> VrmlConverter_Drawer: 
        """
        Returns drawer object
        """
    def GetFreeBoundsMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetFrontMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetLineMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetPointsMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetRepresentation(self) -> VrmlAPI_RepresentationOfShape: 
        """
        Returns the representation of the shape which is written to the VRML file. Types of representation are set through the VrmlAPI_RepresentationOfShape enumeration.
        """
    def GetUisoMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetUnfreeBoundsMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetVisoMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def GetWireMaterial(self) -> OCP.Vrml.Vrml_Material: 
        """
        None
        """
    def ResetToDefaults(self) -> None: 
        """
        Resets all parameters (representation, deflection) to their default values..
        """
    def SetAmbientColorToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,Color : OCP.Quantity.Quantity_HArray1OfColor) -> Any: 
        """
        None
        """
    def SetDeflection(self,aDef : float) -> None: 
        """
        Sets the deflection aDef of the mesh algorithm which is used to compute the shaded representation of the translated shape. The default value is -1. When the deflection value is less than 0, the deflection is calculated from the relative size of the shaped.
        """
    def SetDiffuseColorToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,Color : OCP.Quantity.Quantity_HArray1OfColor) -> Any: 
        """
        None
        """
    def SetEmissiveColorToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,Color : OCP.Quantity.Quantity_HArray1OfColor) -> Any: 
        """
        None
        """
    def SetRepresentation(self,aRep : VrmlAPI_RepresentationOfShape) -> None: 
        """
        Sets the representation of the shape aRep which is written to the VRML file. The three options are : - shaded - wireframe - both shaded and wireframe (default) defined through the VrmlAPI_RepresentationOfShape enumeration.
        """
    def SetShininessToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,aShininess : float) -> Any: 
        """
        None
        """
    def SetSpecularColorToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,Color : OCP.Quantity.Quantity_HArray1OfColor) -> Any: 
        """
        None
        """
    def SetTransparencyToMaterial(self,aMaterial : OCP.Vrml.Vrml_Material,aTransparency : float) -> Any: 
        """
        Set transparency to given material
        """
    def Write(self,aShape : OCP.TopoDS.TopoDS_Shape,aFile : str,aVersion : int=2) -> bool: 
        """
        Converts the shape aShape to VRML format of the passed version and writes it to the file identified by aFile.
        """
    def WriteDoc(self,theDoc : OCP.TDocStd.TDocStd_Document,theFile : str,theScale : float) -> bool: 
        """
        Converts the document to VRML format of the passed version and writes it to the file identified by aFile.
        """
    def __init__(self) -> None: ...
    pass
VrmlAPI_BothRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_BothRepresentation: 2>
VrmlAPI_ShadedRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_ShadedRepresentation: 0>
VrmlAPI_WireFrameRepresentation: OCP.VrmlAPI.VrmlAPI_RepresentationOfShape # value = <VrmlAPI_RepresentationOfShape.VrmlAPI_WireFrameRepresentation: 1>
