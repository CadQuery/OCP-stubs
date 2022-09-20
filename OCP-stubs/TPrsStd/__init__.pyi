import OCP.TPrsStd
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.AIS
import OCP.TDF
import OCP.Quantity
import io
import OCP.Graphic3d
import OCP.Standard
import OCP.V3d
import OCP.TDataXtd
import OCP.TCollection
__all__  = [
"TPrsStd_AISPresentation",
"TPrsStd_AISViewer",
"TPrsStd_Driver",
"TPrsStd_ConstraintDriver",
"TPrsStd_ConstraintTools",
"TPrsStd_AxisDriver",
"TPrsStd_DriverTable",
"TPrsStd_GeometryDriver",
"TPrsStd_NamedShapeDriver",
"TPrsStd_PlaneDriver",
"TPrsStd_PointDriver"
]
class TPrsStd_AISPresentation(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    An attribute to associate an AIS_InteractiveObject to a label in an AIS viewer. This attribute works in collaboration with TPrsStd_AISViewer. Note that all the Set... and Unset... attribute methods as well as the query methods for visualization attributes and the HasOwn... test methods are shortcuts to the respective AIS_InteractiveObject settings.An attribute to associate an AIS_InteractiveObject to a label in an AIS viewer. This attribute works in collaboration with TPrsStd_AISViewer. Note that all the Set... and Unset... attribute methods as well as the query methods for visualization attributes and the HasOwn... test methods are shortcuts to the respective AIS_InteractiveObject settings.An attribute to associate an AIS_InteractiveObject to a label in an AIS viewer. This attribute works in collaboration with TPrsStd_AISViewer. Note that all the Set... and Unset... attribute methods as well as the query methods for visualization attributes and the HasOwn... test methods are shortcuts to the respective AIS_InteractiveObject settings.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AddSelectionMode(self,theSelectionMode : int,theTransaction : bool=True) -> None: 
        """
        None
        """
    def AfterAddition(self) -> None: 
        """
        None
        """
    def AfterResume(self) -> None: 
        """
        None
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        update AIS viewer according to delta
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        None
        """
    def BeforeRemoval(self) -> None: 
        """
        None
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        None
        """
    def Color(self) -> OCP.Quantity.Quantity_NameOfColor: 
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
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Display(self,update : bool=False) -> None: 
        """
        Display presentation of object in AIS viewer. If <update> = True then AISObject is recomputed and all the visualization settings are applied
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def Erase(self,remove : bool=False) -> None: 
        """
        Removes the presentation of this AIS presentation attribute from the TPrsStd_AISViewer. If remove is true, this AIS presentation attribute is removed from the interactive context.
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    def GetAIS(self) -> OCP.AIS.AIS_InteractiveObject: 
        """
        Returns AIS_InteractiveObject stored in the presentation attribute
        """
    def GetDriverGUID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        Returns the GUID for TPrsStd_AISPresentation attributes.
        """
    def GetNbSelectionModes(self) -> int: 
        """
        Returns selection mode(s) of the attribute. It starts with 1 .. GetNbSelectionModes().
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def HasOwnColor(self) -> bool: 
        """
        Returns true if this presentation attribute already has a color setting.
        """
    def HasOwnMaterial(self) -> bool: 
        """
        Returns true if this presentation attribute already has a material setting.
        """
    def HasOwnMode(self) -> bool: 
        """
        None
        """
    def HasOwnSelectionMode(self) -> bool: 
        """
        None
        """
    def HasOwnTransparency(self) -> bool: 
        """
        Returns true if this presentation attribute already has a transparency setting.
        """
    def HasOwnWidth(self) -> bool: 
        """
        Returns true if this presentation attribute already has a width setting.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsDisplayed(self) -> bool: 
        """
        Returns true if this AIS presentation attribute is displayed.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def Material(self) -> OCP.Graphic3d.Graphic3d_NameOfMaterial: 
        """
        Returns the material setting for this presentation attribute.
        """
    def Mode(self) -> int: 
        """
        None
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    def SelectionMode(self,index : int=1) -> int: 
        """
        None
        """
    def SetColor(self,aColor : OCP.Quantity.Quantity_NameOfColor) -> None: 
        """
        Sets the color aColor for this presentation attribute.
        """
    def SetDisplayed(self,B : bool) -> None: 
        """
        None
        """
    def SetDriverGUID(self,guid : OCP.Standard.Standard_GUID) -> None: 
        """
        None
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
    def SetMaterial(self,aName : OCP.Graphic3d.Graphic3d_NameOfMaterial) -> None: 
        """
        Sets the material aName for this presentation attribute.
        """
    def SetMode(self,theMode : int) -> None: 
        """
        None
        """
    def SetSelectionMode(self,theSelectionMode : int,theTransaction : bool=True) -> None: 
        """
        Sets selection mode. If "theTransaction" flag is OFF, modification of the attribute doesn't influence the transaction mechanism (the attribute doesn't participate in undo/redo because of this modification). Certainly, if any other data of the attribute is modified (display mode, color, ...), the attribute will be included into undo/redo.
        """
    def SetTransparency(self,aValue : float=0.6) -> None: 
        """
        Sets the transparency value aValue for this presentation attribute. This value is 0.6 by default.
        """
    def SetWidth(self,aWidth : float) -> None: 
        """
        Sets the width aWidth for this presentation attribute.
        """
    @staticmethod
    @overload
    def Set_s(L : OCP.TDF.TDF_Label,driver : OCP.Standard.Standard_GUID) -> TPrsStd_AISPresentation: 
        """
        Creates or retrieves the presentation attribute on the label L, and sets the GUID driver.

        Creates or retrieves the AISPresentation attribute attached to master. The GUID of the driver will be the GUID of master. master is the attribute you want to display.
        """
    @staticmethod
    @overload
    def Set_s(master : OCP.TDF.TDF_Attribute) -> TPrsStd_AISPresentation: ...
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def Transparency(self) -> float: 
        """
        None
        """
    def UnsetColor(self) -> None: 
        """
        Removes the color setting from this presentation attribute.
        """
    def UnsetMaterial(self) -> None: 
        """
        Removes the material setting from this presentation attribute.
        """
    def UnsetMode(self) -> None: 
        """
        None
        """
    def UnsetSelectionMode(self) -> None: 
        """
        Clears all selection modes of the attribute.
        """
    def UnsetTransparency(self) -> None: 
        """
        Removes the transparency setting from this presentation attribute.
        """
    def UnsetWidth(self) -> None: 
        """
        Removes the width setting from this presentation attribute.
        """
    @staticmethod
    def Unset_s(L : OCP.TDF.TDF_Label) -> None: ...
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def Update(self) -> None: 
        """
        Recompute presentation of object and apply the visualization settings
        """
    def Width(self) -> float: 
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
class TPrsStd_AISViewer(OCP.TDF.TDF_Attribute, OCP.Standard.Standard_Transient):
    """
    The groundwork to define an interactive viewer attribute. This attribute stores an interactive context at the root label. You can only have one instance of this class per data framework.The groundwork to define an interactive viewer attribute. This attribute stores an interactive context at the root label. You can only have one instance of this class per data framework.The groundwork to define an interactive viewer attribute. This attribute stores an interactive context at the root label. You can only have one instance of this class per data framework.
    """
    def AddAttribute(self,other : OCP.TDF.TDF_Attribute) -> None: 
        """
        Adds an Attribute <other> to the label of <me>.Raises if there is already one of the same GUID fhan <other>.
        """
    def AfterAddition(self) -> None: 
        """
        Something to do after adding an Attribute to a label.
        """
    def AfterResume(self) -> None: 
        """
        Something to do after resuming an Attribute from a label.
        """
    def AfterRetrieval(self,forceIt : bool=False) -> bool: 
        """
        Something to do AFTER creation of an attribute by persistent-transient translation. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def AfterUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do after applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def Backup(self) -> None: 
        """
        Backups the attribute. The backuped attribute is flagged "Backuped" and not "Valid".
        """
    def BackupCopy(self) -> OCP.TDF.TDF_Attribute: 
        """
        Copies the attribute contents into a new other attribute. It is used by Backup().
        """
    def BeforeCommitTransaction(self) -> None: 
        """
        A callback. By default does nothing. It is called by TDF_Data::CommitTransaction() method.
        """
    def BeforeForget(self) -> None: 
        """
        Something to do before forgetting an Attribute to a label.
        """
    def BeforeRemoval(self) -> None: 
        """
        Something to do before removing an Attribute from a label.
        """
    def BeforeUndo(self,anAttDelta : OCP.TDF.TDF_AttributeDelta,forceIt : bool=False) -> bool: 
        """
        Something to do before applying <anAttDelta>. The returned status says if AfterUndo has been performed (true) or if this callback must be called once again further (false). If <forceIt> is set to true, the method MUST perform and return true. Does nothing by default and returns true.
        """
    def DecrementRefCounter(self) -> int: 
        """
        Decrements the reference counter of this object; returns the decremented value
        """
    def Delete(self) -> None: 
        """
        Memory deallocator for transient classes
        """
    def DeltaOnAddition(self) -> OCP.TDF.TDF_DeltaOnAddition: 
        """
        Makes an AttributeDelta because <me> appeared. The only known use of a redefinition of this method is to return a null handle (no delta).
        """
    def DeltaOnForget(self) -> OCP.TDF.TDF_DeltaOnForget: 
        """
        Makes an AttributeDelta because <me> has been forgotten.
        """
    @overload
    def DeltaOnModification(self,aDelta : OCP.TDF.TDF_DeltaOnModification) -> None: 
        """
        Makes a DeltaOnModification between <me> and <anOldAttribute.

        Applies a DeltaOnModification to <me>.
        """
    @overload
    def DeltaOnModification(self,anOldAttribute : OCP.TDF.TDF_Attribute) -> OCP.TDF.TDF_DeltaOnModification: ...
    def DeltaOnRemoval(self) -> OCP.TDF.TDF_DeltaOnRemoval: 
        """
        Makes a DeltaOnRemoval on <me> because <me> has disappeared from the DS.
        """
    def DeltaOnResume(self) -> OCP.TDF.TDF_DeltaOnResume: 
        """
        Makes an AttributeDelta because <me> has been resumed.
        """
    def Dump(self,anOS : io.BytesIO) -> io.BytesIO: 
        """
        Dumps the minimum information about <me> on <aStream>.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def DynamicType(self) -> OCP.Standard.Standard_Type: 
        """
        None
        """
    def ExtendedDump(self,anOS : io.BytesIO,aFilter : OCP.TDF.TDF_IDFilter,aMap : OCP.TDF.TDF_AttributeIndexedMap) -> None: 
        """
        Dumps the attribute content on <aStream>, using <aMap> like this: if an attribute is not in the map, first put add it to the map and then dump it. Use the map rank instead of dumping each attribute field.
        """
    def FindAttribute(self,anID : OCP.Standard.Standard_GUID,anAttribute : OCP.TDF.TDF_Attribute) -> bool: 
        """
        Finds an associated attribute of <me>, according to <anID>. the returned <anAttribute> is a valid one. The method returns True if found, False otherwise. A removed attribute cannot be found using this method.
        """
    @staticmethod
    @overload
    def Find_s(acces : OCP.TDF.TDF_Label,V : OCP.V3d.V3d_Viewer) -> bool: 
        """
        Finds the viewer attribute at the label access, the root of the data framework. Calling this function can be used to initialize an AIS viewer

        None

        None
        """
    @staticmethod
    @overload
    def Find_s(acces : OCP.TDF.TDF_Label,IC : OCP.AIS.AIS_InteractiveContext) -> bool: ...
    @staticmethod
    @overload
    def Find_s(acces : OCP.TDF.TDF_Label,A : TPrsStd_AISViewer) -> bool: ...
    def Forget(self,aTransaction : int) -> None: 
        """
        Forgets the attribute. <aTransaction> is the current transaction in which the forget is done. A forgotten attribute is also flagged not "Valid".
        """
    def ForgetAllAttributes(self,clearChildren : bool=True) -> None: 
        """
        Forgets all the attributes attached to the label of <me>. Does it on the sub-labels if <clearChildren> is set to true. Of course, this method is compatible with Transaction & Delta mechanisms. Be careful that if <me> will have a null label after this call
        """
    def ForgetAttribute(self,aguid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Forgets the Attribute of GUID <aguid> associated to the label of <me>. Be careful that if <me> is the attribute of <guid>, <me> will have a null label after this call. If the attribute doesn't exist returns False. Otherwise returns True.
        """
    @staticmethod
    def GetID_s() -> OCP.Standard.Standard_GUID: 
        """
        class methods =============
        """
    def GetInteractiveContext(self) -> OCP.AIS.AIS_InteractiveContext: 
        """
        Returns the interactive context in this attribute.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Has_s(acces : OCP.TDF.TDF_Label) -> bool: 
        """
        returns True if there is an AISViewer attribute in <acces> Data Framework.
        """
    def ID(self) -> OCP.Standard.Standard_GUID: 
        """
        None
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def IsAttribute(self,anID : OCP.Standard.Standard_GUID) -> bool: 
        """
        Returns true if it exists an associated attribute of <me> with <anID> as ID.
        """
    def IsBackuped(self) -> bool: 
        """
        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.

        Returns true if the attribute backup status is set. This status is set/unset by the Backup() method.
        """
    def IsForgotten(self) -> bool: 
        """
        Returns true if the attribute forgotten status is set.

        Returns true if the attribute forgotten status is set.
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
    def IsNew(self) -> bool: 
        """
        Returns true if the attribute has no backup

        Returns true if the attribute has no backup
        """
    def IsValid(self) -> bool: 
        """
        Returns true if the attribute is valid; i.e. not a backuped or removed one.

        Returns true if the attribute is valid; i.e. not a backuped or removed one.
        """
    def Label(self) -> OCP.TDF.TDF_Label: 
        """
        Returns the label to which the attribute is attached. If the label is not included in a DF, the label is null. See Label. Warning If the label is not included in a data framework, it is null. This function should not be redefined inline.
        """
    def NewEmpty(self) -> OCP.TDF.TDF_Attribute: 
        """
        None
        """
    @staticmethod
    @overload
    def New_s(access : OCP.TDF.TDF_Label,selector : OCP.AIS.AIS_InteractiveContext) -> TPrsStd_AISViewer: 
        """
        create and set an AISViewer at. Raise an exception if Has.

        create and set an AISAttribute at root label. The interactive context is build. Raise an exception if Has.
        """
    @staticmethod
    @overload
    def New_s(acces : OCP.TDF.TDF_Label,viewer : OCP.V3d.V3d_Viewer) -> TPrsStd_AISViewer: ...
    def Paste(self,into : OCP.TDF.TDF_Attribute,RT : OCP.TDF.TDF_RelocationTable) -> None: 
        """
        None
        """
    def References(self,aDataSet : OCP.TDF.TDF_DataSet) -> None: 
        """
        Adds the first level referenced attributes and labels to <aDataSet>.
        """
    def Restore(self,with_ : OCP.TDF.TDF_Attribute) -> None: 
        """
        None
        """
    @overload
    def SetID(self,arg1 : OCP.Standard.Standard_GUID) -> None: 
        """
        Sets specific ID of the attribute (supports several attributes of one type at the same label feature).

        Sets default ID defined in nested class (to be used for attributes having User ID feature).
        """
    @overload
    def SetID(self) -> None: ...
    def SetInteractiveContext(self,ctx : OCP.AIS.AIS_InteractiveContext) -> None: 
        """
        Sets the interactive context ctx for this attribute.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Transaction(self) -> int: 
        """
        Returns the transaction index in which the attribute has been created or modified.

        Returns the transaction index in which the attribute has been created or modified.
        """
    def UntilTransaction(self) -> int: 
        """
        Returns the upper transaction index until which the attribute is/was valid. This number may vary. A removed attribute validity range is reduced to its transaction index.
        """
    def Update(self) -> None: 
        """
        Updates the viewer at the label access. access is the root of the data framework.
        """
    @staticmethod
    def Update_s(acces : OCP.TDF.TDF_Label) -> None: 
        """
        AISViewer methods =================
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
class TPrsStd_Driver(OCP.Standard.Standard_Transient):
    """
    Driver for AIS ============== An abstract class, which - in classes inheriting from it - allows you to update an AIS_InteractiveObject or create one if one does not already exist. For both creation and update, the interactive object is filled with information contained in attributes. These attributes are those found on the label given as an argument in the method Update. true is returned if the interactive object was modified by the update. This class provide an algorithm to Build with its default values (if Null) or Update (if !Null) an AIS_InteractiveObject . Resources are found in attributes associated to a given label.Driver for AIS ============== An abstract class, which - in classes inheriting from it - allows you to update an AIS_InteractiveObject or create one if one does not already exist. For both creation and update, the interactive object is filled with information contained in attributes. These attributes are those found on the label given as an argument in the method Update. true is returned if the interactive object was modified by the update. This class provide an algorithm to Build with its default values (if Null) or Update (if !Null) an AIS_InteractiveObject . Resources are found in attributes associated to a given label.Driver for AIS ============== An abstract class, which - in classes inheriting from it - allows you to update an AIS_InteractiveObject or create one if one does not already exist. For both creation and update, the interactive object is filled with information contained in attributes. These attributes are those found on the label given as an argument in the method Update. true is returned if the interactive object was modified by the update. This class provide an algorithm to Build with its default values (if Null) or Update (if !Null) an AIS_InteractiveObject . Resources are found in attributes associated to a given label.
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
    def Update(self,L : OCP.TDF.TDF_Label,ais : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Updates the interactive object ais with information found on the attributes associated with the label L.
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
class TPrsStd_ConstraintDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    An implementation of TPrsStd_Driver for constraints.An implementation of TPrsStd_Driver for constraints.An implementation of TPrsStd_Driver for constraints.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
class TPrsStd_ConstraintTools():
    """
    None
    """
    @staticmethod
    def ComputeAngleForOneFace_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeAngle_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeCoincident_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeConcentric_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeDiameter_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeDistance_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeEqualDistance_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeEqualRadius_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeFix_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeMaxRadius_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeMidPoint_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeMinRadius_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeOffset_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeOthers_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeParallel_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputePerpendicular_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputePlacement_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeRadius_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeRound_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeSymmetry_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeTangent_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    @staticmethod
    def ComputeTextAndValue_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,aText : OCP.TCollection.TCollection_ExtendedString,anIsAngle : bool) -> Tuple[float]: 
        """
        None
        """
    @staticmethod
    def UpdateOnlyValue_s(aConst : OCP.TDataXtd.TDataXtd_Constraint,anAIS : OCP.AIS.AIS_InteractiveObject) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class TPrsStd_AxisDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    An implementation of TPrsStd_Driver for axes.An implementation of TPrsStd_Driver for axes.An implementation of TPrsStd_Driver for axes.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
class TPrsStd_DriverTable(OCP.Standard.Standard_Transient):
    """
    This class is a container to record (AddDriver) binding between GUID and TPrsStd_Driver. You create a new instance of TPrsStd_Driver and use the method AddDriver to load it into the driver table. the methodThis class is a container to record (AddDriver) binding between GUID and TPrsStd_Driver. You create a new instance of TPrsStd_Driver and use the method AddDriver to load it into the driver table. the methodThis class is a container to record (AddDriver) binding between GUID and TPrsStd_Driver. You create a new instance of TPrsStd_Driver and use the method AddDriver to load it into the driver table. the method
    """
    def AddDriver(self,guid : OCP.Standard.Standard_GUID,driver : TPrsStd_Driver) -> bool: 
        """
        Returns true if the driver has been added successfully to the driver table.
        """
    def Clear(self) -> None: 
        """
        Removes all drivers. Returns true if the driver has been removed successfully. If this method is used, the InitStandardDrivers method should be called to fill the table with standard drivers.
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
    def FindDriver(self,guid : OCP.Standard.Standard_GUID,driver : TPrsStd_Driver) -> bool: 
        """
        Returns true if the driver was found.
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    @staticmethod
    def Get_s() -> TPrsStd_DriverTable: 
        """
        Returns the static table. If it does not exist, creates it and fills it with standard drivers.
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def InitStandardDrivers(self) -> None: 
        """
        Fills the table with standard drivers
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
    def RemoveDriver(self,guid : OCP.Standard.Standard_GUID) -> bool: 
        """
        Removes a driver with the given GUID. Returns true if the driver has been removed successfully.
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
class TPrsStd_GeometryDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    This method is an implementation of TPrsStd_Driver for geometries.This method is an implementation of TPrsStd_Driver for geometries.This method is an implementation of TPrsStd_Driver for geometries.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
class TPrsStd_NamedShapeDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    An implementation of TPrsStd_Driver for named shapes.An implementation of TPrsStd_Driver for named shapes.An implementation of TPrsStd_Driver for named shapes.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
class TPrsStd_PlaneDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    An implementation of TPrsStd_Driver for planes.An implementation of TPrsStd_Driver for planes.An implementation of TPrsStd_Driver for planes.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
class TPrsStd_PointDriver(TPrsStd_Driver, OCP.Standard.Standard_Transient):
    """
    An implementation of TPrsStd_Driver for points.An implementation of TPrsStd_Driver for points.An implementation of TPrsStd_Driver for points.
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
    def Update(self,aLabel : OCP.TDF.TDF_Label,anAISObject : OCP.AIS.AIS_InteractiveObject) -> bool: 
        """
        Build the AISObject (if null) or update it. No compute is done. Returns <True> if information was found and AISObject updated.
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
