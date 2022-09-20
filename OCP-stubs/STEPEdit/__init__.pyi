import OCP.STEPEdit
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import OCP.Standard
import OCP.IFSelect
import OCP.Interface
import OCP.StepData
import OCP.TCollection
import OCP.TColStd
__all__  = [
"STEPEdit",
"STEPEdit_EditContext",
"STEPEdit_EditSDR"
]
class STEPEdit():
    """
    Provides tools to exploit and edit a set of STEP data : editors, selections ..
    """
    @staticmethod
    def NewModel_s() -> OCP.StepData.StepData_StepModel: 
        """
        Returns a new empty StepModel fit for STEP i.e. with its header determined from Protocol
        """
    @staticmethod
    def NewSelectPlacedItem_s() -> OCP.IFSelect.IFSelect_SelectSignature: 
        """
        Creates a Selection for Placed Items, i.e. MappedItem or ContextDependentShapeRepresentation, which itself refers to a RepresentationRelationship with possible subtypes (Shape... and/or ...WithTransformation) By default in the whole StepModel
        """
    @staticmethod
    def NewSelectSDR_s() -> OCP.IFSelect.IFSelect_SelectSignature: 
        """
        Creates a Selection for ShapeDefinitionRepresentation By default searches among root entities
        """
    @staticmethod
    def NewSelectShapeRepr_s() -> OCP.IFSelect.IFSelect_SelectSignature: 
        """
        Creates a Selection for ShapeRepresentation and its sub-types, plus ContextDependentShapeRepresentation (which is not a sub-type of ShapeRepresentation) By default in the whole StepModel
        """
    @staticmethod
    def Protocol_s() -> OCP.Interface.Interface_Protocol: 
        """
        Returns a Protocol fit for STEP (creates the first time)
        """
    @staticmethod
    def SignType_s() -> OCP.IFSelect.IFSelect_Signature: 
        """
        Returns a SignType fit for STEP (creates the first time)
        """
    def __init__(self) -> None: ...
    pass
class STEPEdit_EditContext(OCP.IFSelect.IFSelect_Editor, OCP.Standard.Standard_Transient):
    """
    EditContext is an Editor fit for Product Definition Context (one per Model) , i.e. : - ProductDefinition - ApplicationProtocolDefinition - ProductRelatedProductCategoryEditContext is an Editor fit for Product Definition Context (one per Model) , i.e. : - ProductDefinition - ApplicationProtocolDefinition - ProductRelatedProductCategoryEditContext is an Editor fit for Product Definition Context (one per Model) , i.e. : - ProductDefinition - ApplicationProtocolDefinition - ProductRelatedProductCategory
    """
    def Apply(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def EditMode(self,num : int) -> OCP.IFSelect.IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> OCP.IFSelect.IFSelect_EditForm: 
        """
        Builds and Returns an EditForm, empty (no data yet) Can be redefined to return a specific type of EditForm
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
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ListEditor(self,num : int) -> OCP.IFSelect.IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        None
        """
    def MaxList(self,num : int) -> int: 
        """
        Returns max length allowed for a list = 0 means : list with no limit < 0 means : not a list
        """
    def MaxNameLength(self,what : int) -> int: 
        """
        Returns the MaxLength of, according to what : <what> = -1 : length of short names <what> = 0 : length of complete names <what> = 1 : length of values labels
        """
    def Name(self,num : int,isshort : bool=False) -> str: 
        """
        Returns the name of a Value (complete or short) from its ident Short Name can be empty
        """
    def NameNumber(self,name : str) -> int: 
        """
        Returns the number (ident) of a Value, from its name, short or complete. If not found, returns 0
        """
    def NbValues(self) -> int: 
        """
        Returns the count of Typed Values
        """
    def PrintDefs(self,S : io.BytesIO,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : io.BytesIO) -> None: 
        """
        None
        """
    def Recognize(self,form : OCP.IFSelect.IFSelect_EditForm) -> bool: 
        """
        None
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : OCP.IFSelect.IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    def StringValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypedValue(self,num : int) -> OCP.Interface.Interface_TypedValue: 
        """
        Returns a Typed Value from its ident
        """
    def Update(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        Updates the EditForm when a parameter is modified I.E. default does nothing, can be redefined, as follows : Returns True when done (even if does nothing), False in case of refuse (for instance, if the new value is not suitable) <num> is the rank of the parameter for the EDITOR itself <enforce> True means that protected parameters can be touched
        """
    def UpdateList(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
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
class STEPEdit_EditSDR(OCP.IFSelect.IFSelect_Editor, OCP.Standard.Standard_Transient):
    """
    EditSDR is an Editor fit for a Shape Definition Representation which designates a Product DefinitionEditSDR is an Editor fit for a Shape Definition Representation which designates a Product DefinitionEditSDR is an Editor fit for a Shape Definition Representation which designates a Product Definition
    """
    def Apply(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
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
    def EditMode(self,num : int) -> OCP.IFSelect.IFSelect_EditValue: 
        """
        Returns the edit mode of a Value
        """
    def Form(self,readonly : bool,undoable : bool=True) -> OCP.IFSelect.IFSelect_EditForm: 
        """
        Builds and Returns an EditForm, empty (no data yet) Can be redefined to return a specific type of EditForm
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
    def IsList(self,num : int) -> bool: 
        """
        Tells if a parameter is a list
        """
    def Label(self) -> OCP.TCollection.TCollection_AsciiString: 
        """
        None
        """
    def ListEditor(self,num : int) -> OCP.IFSelect.IFSelect_ListEditor: 
        """
        Returns a ListEditor for a parameter which is a List Default returns a basic ListEditor for a List, a Null Handle if <num> is not for a List. Can be redefined
        """
    def ListValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TColStd.TColStd_HSequenceOfHAsciiString: 
        """
        Returns the value of an EditForm as a List, for a given item If not a list, a Null Handle should be returned Default returns a Null Handle, because many Editors have no list to edit. To be redefined as required
        """
    def Load(self,form : OCP.IFSelect.IFSelect_EditForm,ent : OCP.Standard.Standard_Transient,model : OCP.Interface.Interface_InterfaceModel) -> bool: 
        """
        None
        """
    def MaxList(self,num : int) -> int: 
        """
        Returns max length allowed for a list = 0 means : list with no limit < 0 means : not a list
        """
    def MaxNameLength(self,what : int) -> int: 
        """
        Returns the MaxLength of, according to what : <what> = -1 : length of short names <what> = 0 : length of complete names <what> = 1 : length of values labels
        """
    def Name(self,num : int,isshort : bool=False) -> str: 
        """
        Returns the name of a Value (complete or short) from its ident Short Name can be empty
        """
    def NameNumber(self,name : str) -> int: 
        """
        Returns the number (ident) of a Value, from its name, short or complete. If not found, returns 0
        """
    def NbValues(self) -> int: 
        """
        Returns the count of Typed Values
        """
    def PrintDefs(self,S : io.BytesIO,labels : bool=False) -> None: 
        """
        None
        """
    def PrintNames(self,S : io.BytesIO) -> None: 
        """
        None
        """
    def Recognize(self,form : OCP.IFSelect.IFSelect_EditForm) -> bool: 
        """
        None
        """
    def SetList(self,num : int,max : int=0) -> None: 
        """
        Sets a parameter to be a List max < 0 : not for a list (set when starting) max = 0 : list with no length limit (default for SetList) max > 0 : list limited to <max> items
        """
    def SetValue(self,num : int,typval : OCP.Interface.Interface_TypedValue,shortname : str='',accessmode : OCP.IFSelect.IFSelect_EditValue=IFSelect_EditValue.IFSelect_Editable) -> None: 
        """
        Sets a Typed Value for a given ident and short name, with an Edit Mode
        """
    def StringValue(self,form : OCP.IFSelect.IFSelect_EditForm,num : int) -> OCP.TCollection.TCollection_HAsciiString: 
        """
        None
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def TypedValue(self,num : int) -> OCP.Interface.Interface_TypedValue: 
        """
        Returns a Typed Value from its ident
        """
    def Update(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newval : OCP.TCollection.TCollection_HAsciiString,enforce : bool) -> bool: 
        """
        Updates the EditForm when a parameter is modified I.E. default does nothing, can be redefined, as follows : Returns True when done (even if does nothing), False in case of refuse (for instance, if the new value is not suitable) <num> is the rank of the parameter for the EDITOR itself <enforce> True means that protected parameters can be touched
        """
    def UpdateList(self,form : OCP.IFSelect.IFSelect_EditForm,num : int,newlist : OCP.TColStd.TColStd_HSequenceOfHAsciiString,enforce : bool) -> bool: 
        """
        Acts as Update, but when the value is a list
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
