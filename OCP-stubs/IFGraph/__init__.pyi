import OCP.IFGraph
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.TColStd
import OCP.Interface
__all__  = [
"IFGraph_AllConnected",
"IFGraph_AllShared",
"IFGraph_Articulations",
"IFGraph_Compare",
"IFGraph_SubPartsIterator",
"IFGraph_Cumulate",
"IFGraph_Cycles",
"IFGraph_ExternalSources",
"IFGraph_StrongComponants",
"IFGraph_SCRoots",
"IFGraph_ConnectedComponants"
]
class IFGraph_AllConnected(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class gives content of the CONNECTED COMPONENT(S) which include specific Entity(ies)
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        does the specific evaluation (Connected entities atall levels)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        adds an entity and its Connected ones to the list (allows to cumulate all Entities Connected by some ones) Note that if "ent" is in the already computed list,, no entity will be added, but if "ent" is not already in the list, a new Connected Component will be cumulated
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph) -> None: ...
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph,ent : OCP.Standard.Standard_Transient) -> None: ...
    pass
class IFGraph_AllShared(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class determines all Entities shared by some specific ones, at any level (those which will be lead in a Transfer for instance)
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        does the specific evaluation (shared entities atall levels)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        adds an entity and its shared ones to the list (allows to cumulate all Entities shared by some ones)
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds Entities from an EntityIterator and all their shared ones at any level
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph) -> None: ...
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph,ent : OCP.Standard.Standard_Transient) -> None: ...
    pass
class IFGraph_Articulations(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class gives entities which are Articulation points in a whole Model or in a sub-part An Articulation Point divides the graph in two (or more) disconnected sub-graphs Identifying Articulation Points allows improving efficiency of splitting a set of Entities into sub-sets
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        Evaluates the list of Articulation points
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        adds an entity and its shared ones to the list
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        adds a list of entities (as an iterator)
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    pass
class IFGraph_Compare(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class evaluates effect of two compared sub-parts : cumulation (union), common part (intersection-overlapping) part specific to first sub-part or to the second one Results are kept in a Graph, several question can be set Basic Iteration gives Cumulation (union)
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Common(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns entities common to the both parts
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        Recomputes result of comparing to sub-parts
        """
    def FirstOnly(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns entities which are exclusively in the first list
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,first : bool) -> None: 
        """
        adds an entity and its shared ones to the list : first True means adds to the first sub-list, else to the 2nd
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator,first : bool) -> None: 
        """
        adds a list of entities (as an iterator) as such, that is, their shared entities are not considered (use AllShared to have them) first True means adds to the first sub-list, else to the 2nd
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def KeepCommon(self) -> None: 
        """
        Keeps only Common part, sets it as First list and clears second list
        """
    def Merge(self) -> None: 
        """
        merges the second list into the first one, hence the second list is empty
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def RemoveSecond(self) -> None: 
        """
        Removes the contents of second list
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SecondOnly(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns entities which are exclusively in the second part
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph) -> None: ...
    pass
class IFGraph_SubPartsIterator():
    """
    defines general form for graph classes of which result is not a single iteration on Entities, but a nested one : External iteration works on sub-parts, identified by each class (according to its algorithm) Internal Iteration concerns Entities of a sub-part Sub-Parts are assumed to be disjoined; if they are not, the first one has priority
    """
    def AddPart(self) -> None: 
        """
        Adds an empty part and sets it to receive entities
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns current sub-part, not as a "Value", but as an Iterator on Entities it contains Error : same as above (end of iteration)
        """
    def EntityPartNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns number of the sub-part in which an Entity has been set if it is not in a sub-part (or not loaded at all), Returns 0
        """
    def Evaluate(self) -> None: 
        """
        Called by Clear, this method allows evaluation just before iteration; its default is doing nothing, it is designed to be redefined
        """
    def FirstEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the first entity of current sub-part, that is for a Single one, the only one it contains Error : same as above (end of iteration)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool) -> None: 
        """
        Adds an Entity : into load status if in Load mode, to the current part if there is one. If shared is True, adds also its shared ones (shared at all levels)
        """
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds a list of Entities (into Load mode or to a Part), given as an Iterator
        """
    def GetParts(self,other : IFGraph_SubPartsIterator) -> None: 
        """
        Gets Parts from another SubPartsIterator (in addition to the ones already recorded) Error if both SubPartsIterators are not based on the same Model
        """
    def IsInPart(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is Present in a sub-part
        """
    def IsLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is loaded (either set into a sub-part or not)
        """
    def IsSingle(self) -> bool: 
        """
        Returns True if current sub-part is single (has only one Entity) Error if there is no sub-part to iterate now
        """
    def Loaded(self) -> OCP.Interface.Interface_GraphContent: 
        """
        Returns entities which where loaded (not set into a sub-part)
        """
    def LoadedGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Same as above, but under the form of a Graph
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model with which this Iterator was created
        """
    def More(self) -> bool: 
        """
        Returns True if there are more sub-parts to iterate on Note : an empty sub-part is not taken in account by Iteration
        """
    def NbParts(self) -> int: 
        """
        Returns count of registered parts
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next sub-part if there is not, IsSingle-Entities will raises an exception
        """
    def PartNum(self) -> int: 
        """
        Returns numero of part which currently receives entities (0 at load time)
        """
    def Reset(self) -> None: 
        """
        Erases data (parts, entities) : "me" becomes empty and in load status
        """
    def SetLoad(self) -> None: 
        """
        Sets SubPartIterator to get Entities (by GetFromEntity & GetFromIter) into load status, to be analysed later
        """
    def SetPartNum(self,num : int) -> None: 
        """
        Sets numero of receiving part to a new value Error if not in range (1-NbParts)
        """
    def Start(self) -> None: 
        """
        Sets iteration to its beginning; calls Evaluate
        """
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    @overload
    def __init__(self,other : IFGraph_SubPartsIterator) -> None: ...
    pass
class IFGraph_Cumulate(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class evaluates effect of cumulated sub-parts : overlapping, forgotten entities Results are kept in a Graph, several question can be set Basic Iteration gives entities which are part of Cumulation
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        Evaluates the result of cumulation
        """
    def Forgotten(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns entities which are not taken
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        adds an entity and its shared ones to the list
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        adds a list of entities (as an iterator) as such, that is, without their shared entities (use AllShared to have them)
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def HighestNbTimes(self) -> int: 
        """
        Returns the highest number of times recorded for every Entity (0 means empty, 1 means no overlap)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTimes(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        returns number of times an Entity has been counted (0 means forgotten, more than 1 means overlap, 1 is normal)
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def Overlapped(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        returns entities which are taken several times
        """
    def PerCount(self,count : int=1) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns entities taken a given count of times (0 : same as Forgotten, 1 : same as no Overlap : default)
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph) -> None: ...
    pass
class IFGraph_Cycles(IFGraph_SubPartsIterator):
    """
    determines strong components in a graph which are Cycles
    """
    def AddPart(self) -> None: 
        """
        Adds an empty part and sets it to receive entities
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns current sub-part, not as a "Value", but as an Iterator on Entities it contains Error : same as above (end of iteration)
        """
    def EntityPartNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns number of the sub-part in which an Entity has been set if it is not in a sub-part (or not loaded at all), Returns 0
        """
    def Evaluate(self) -> None: 
        """
        does the computation. Cycles are StrongComponants which are not Single
        """
    def FirstEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the first entity of current sub-part, that is for a Single one, the only one it contains Error : same as above (end of iteration)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool) -> None: 
        """
        Adds an Entity : into load status if in Load mode, to the current part if there is one. If shared is True, adds also its shared ones (shared at all levels)
        """
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds a list of Entities (into Load mode or to a Part), given as an Iterator
        """
    def GetParts(self,other : IFGraph_SubPartsIterator) -> None: 
        """
        Gets Parts from another SubPartsIterator (in addition to the ones already recorded) Error if both SubPartsIterators are not based on the same Model
        """
    def IsInPart(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is Present in a sub-part
        """
    def IsLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is loaded (either set into a sub-part or not)
        """
    def IsSingle(self) -> bool: 
        """
        Returns True if current sub-part is single (has only one Entity) Error if there is no sub-part to iterate now
        """
    def Loaded(self) -> OCP.Interface.Interface_GraphContent: 
        """
        Returns entities which where loaded (not set into a sub-part)
        """
    def LoadedGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Same as above, but under the form of a Graph
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model with which this Iterator was created
        """
    def More(self) -> bool: 
        """
        Returns True if there are more sub-parts to iterate on Note : an empty sub-part is not taken in account by Iteration
        """
    def NbParts(self) -> int: 
        """
        Returns count of registered parts
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next sub-part if there is not, IsSingle-Entities will raises an exception
        """
    def PartNum(self) -> int: 
        """
        Returns numero of part which currently receives entities (0 at load time)
        """
    def Reset(self) -> None: 
        """
        Erases data (parts, entities) : "me" becomes empty and in load status
        """
    def SetLoad(self) -> None: 
        """
        Sets SubPartIterator to get Entities (by GetFromEntity & GetFromIter) into load status, to be analysed later
        """
    def SetPartNum(self,num : int) -> None: 
        """
        Sets numero of receiving part to a new value Error if not in range (1-NbParts)
        """
    def Start(self) -> None: 
        """
        Sets iteration to its beginning; calls Evaluate
        """
    @overload
    def __init__(self,subparts : IFGraph_StrongComponants) -> None: ...
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    pass
class IFGraph_ExternalSources(OCP.Interface.Interface_GraphContent, OCP.Interface.Interface_EntityIterator):
    """
    this class gives entities which are Source of entities of a sub-part, but are not contained by this sub-part
    """
    def AddItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        Adds to the iteration list a defined entity
        """
    def AddList(self,list : OCP.TColStd.TColStd_HSequenceOfTransient) -> None: 
        """
        Gets a list of entities and adds its to the iteration list
        """
    def Begin(self) -> None: 
        """
        Does the Evaluation before starting the iteration itself (in out)
        """
    def Content(self) -> OCP.TColStd.TColStd_HSequenceOfTransient: 
        """
        Returns the content of the Iterator, accessed through a Handle to be used by a frontal-engine logic Returns an empty Sequence if the Iterator is empty Calls Start if not yet done
        """
    def Destroy(self) -> None: 
        """
        Clears data of iteration
        """
    def Evaluate(self) -> None: 
        """
        Evaluates external sources of a set of entities
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient) -> None: 
        """
        adds an entity and its shared ones to the list
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph) -> None: 
        """
        Gets all Entities designated by a Graph (once created), adds them to those already recorded

        Gets entities from a graph which have a specific Status value (one created), adds them to those already recorded
        """
    @overload
    def GetFromGraph(self,agraph : OCP.Interface.Interface_Graph,stat : int) -> None: ...
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        adds a list of entities (as an iterator) with shared ones
        """
    def GetOneItem(self,anentity : OCP.Standard.Standard_Transient) -> None: 
        """
        same as AddItem (kept for compatibility)
        """
    def IsEmpty(self) -> bool: 
        """
        Returns True if no External Source are found It means that we have a "root" set (performs an Evaluation as necessary)
        """
    def More(self) -> bool: 
        """
        Says if there are other entities (vertices) to iterate the first time, calls Start
        """
    def NbEntities(self) -> int: 
        """
        Returns count of entities which will be iterated on Calls Start if not yet done
        """
    def NbTyped(self,type : OCP.Standard.Standard_Type) -> int: 
        """
        Returns count of entities of a given type (kind of)
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next entity (vertex) to give
        """
    def ResetData(self) -> None: 
        """
        Allows to restart on a new data set
        """
    def Result(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns Result under the exact form of an EntityIterator : Can be used when EntityIterator itself is required (as a returned value for instance), without way for a sub-class
        """
    def SelectType(self,atype : OCP.Standard.Standard_Type,keep : bool) -> None: 
        """
        Selects entities with are Kind of a given type, keep only them (is keep is True) or reject only them (if keep is False)
        """
    def Start(self) -> None: 
        """
        Allows re-iteration (useless for the first iteration)
        """
    def Typed(self,type : OCP.Standard.Standard_Type) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns the list of entities of a given type (kind of)
        """
    def Value(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the current Entity iterated, to be used by Interface tools
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph) -> None: ...
    pass
class IFGraph_StrongComponants(IFGraph_SubPartsIterator):
    """
    determines strong components of a graph, that is isolated entities (single components) or loops
    """
    def AddPart(self) -> None: 
        """
        Adds an empty part and sets it to receive entities
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns current sub-part, not as a "Value", but as an Iterator on Entities it contains Error : same as above (end of iteration)
        """
    def EntityPartNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns number of the sub-part in which an Entity has been set if it is not in a sub-part (or not loaded at all), Returns 0
        """
    def Evaluate(self) -> None: 
        """
        does the computation
        """
    def FirstEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the first entity of current sub-part, that is for a Single one, the only one it contains Error : same as above (end of iteration)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool) -> None: 
        """
        Adds an Entity : into load status if in Load mode, to the current part if there is one. If shared is True, adds also its shared ones (shared at all levels)
        """
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds a list of Entities (into Load mode or to a Part), given as an Iterator
        """
    def GetParts(self,other : IFGraph_SubPartsIterator) -> None: 
        """
        Gets Parts from another SubPartsIterator (in addition to the ones already recorded) Error if both SubPartsIterators are not based on the same Model
        """
    def IsInPart(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is Present in a sub-part
        """
    def IsLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is loaded (either set into a sub-part or not)
        """
    def IsSingle(self) -> bool: 
        """
        Returns True if current sub-part is single (has only one Entity) Error if there is no sub-part to iterate now
        """
    def Loaded(self) -> OCP.Interface.Interface_GraphContent: 
        """
        Returns entities which where loaded (not set into a sub-part)
        """
    def LoadedGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Same as above, but under the form of a Graph
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model with which this Iterator was created
        """
    def More(self) -> bool: 
        """
        Returns True if there are more sub-parts to iterate on Note : an empty sub-part is not taken in account by Iteration
        """
    def NbParts(self) -> int: 
        """
        Returns count of registered parts
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next sub-part if there is not, IsSingle-Entities will raises an exception
        """
    def PartNum(self) -> int: 
        """
        Returns numero of part which currently receives entities (0 at load time)
        """
    def Reset(self) -> None: 
        """
        Erases data (parts, entities) : "me" becomes empty and in load status
        """
    def SetLoad(self) -> None: 
        """
        Sets SubPartIterator to get Entities (by GetFromEntity & GetFromIter) into load status, to be analysed later
        """
    def SetPartNum(self,num : int) -> None: 
        """
        Sets numero of receiving part to a new value Error if not in range (1-NbParts)
        """
    def Start(self) -> None: 
        """
        Sets iteration to its beginning; calls Evaluate
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    pass
class IFGraph_SCRoots(IFGraph_StrongComponants, IFGraph_SubPartsIterator):
    """
    determines strong components in a graph which are Roots
    """
    def AddPart(self) -> None: 
        """
        Adds an empty part and sets it to receive entities
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns current sub-part, not as a "Value", but as an Iterator on Entities it contains Error : same as above (end of iteration)
        """
    def EntityPartNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns number of the sub-part in which an Entity has been set if it is not in a sub-part (or not loaded at all), Returns 0
        """
    def Evaluate(self) -> None: 
        """
        does the computation
        """
    def FirstEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the first entity of current sub-part, that is for a Single one, the only one it contains Error : same as above (end of iteration)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool) -> None: 
        """
        Adds an Entity : into load status if in Load mode, to the current part if there is one. If shared is True, adds also its shared ones (shared at all levels)
        """
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds a list of Entities (into Load mode or to a Part), given as an Iterator
        """
    def GetParts(self,other : IFGraph_SubPartsIterator) -> None: 
        """
        Gets Parts from another SubPartsIterator (in addition to the ones already recorded) Error if both SubPartsIterators are not based on the same Model
        """
    def IsInPart(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is Present in a sub-part
        """
    def IsLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is loaded (either set into a sub-part or not)
        """
    def IsSingle(self) -> bool: 
        """
        Returns True if current sub-part is single (has only one Entity) Error if there is no sub-part to iterate now
        """
    def Loaded(self) -> OCP.Interface.Interface_GraphContent: 
        """
        Returns entities which where loaded (not set into a sub-part)
        """
    def LoadedGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Same as above, but under the form of a Graph
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model with which this Iterator was created
        """
    def More(self) -> bool: 
        """
        Returns True if there are more sub-parts to iterate on Note : an empty sub-part is not taken in account by Iteration
        """
    def NbParts(self) -> int: 
        """
        Returns count of registered parts
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next sub-part if there is not, IsSingle-Entities will raises an exception
        """
    def PartNum(self) -> int: 
        """
        Returns numero of part which currently receives entities (0 at load time)
        """
    def Reset(self) -> None: 
        """
        Erases data (parts, entities) : "me" becomes empty and in load status
        """
    def SetLoad(self) -> None: 
        """
        Sets SubPartIterator to get Entities (by GetFromEntity & GetFromIter) into load status, to be analysed later
        """
    def SetPartNum(self,num : int) -> None: 
        """
        Sets numero of receiving part to a new value Error if not in range (1-NbParts)
        """
    def Start(self) -> None: 
        """
        Sets iteration to its beginning; calls Evaluate
        """
    @overload
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    @overload
    def __init__(self,subparts : IFGraph_StrongComponants) -> None: ...
    pass
class IFGraph_ConnectedComponants(IFGraph_SubPartsIterator):
    """
    determines Connected Components in a Graph. They define disjoined sets of Entities.
    """
    def AddPart(self) -> None: 
        """
        Adds an empty part and sets it to receive entities
        """
    def Entities(self) -> OCP.Interface.Interface_EntityIterator: 
        """
        Returns current sub-part, not as a "Value", but as an Iterator on Entities it contains Error : same as above (end of iteration)
        """
    def EntityPartNum(self,ent : OCP.Standard.Standard_Transient) -> int: 
        """
        Returns number of the sub-part in which an Entity has been set if it is not in a sub-part (or not loaded at all), Returns 0
        """
    def Evaluate(self) -> None: 
        """
        does the computation
        """
    def FirstEntity(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns the first entity of current sub-part, that is for a Single one, the only one it contains Error : same as above (end of iteration)
        """
    def GetFromEntity(self,ent : OCP.Standard.Standard_Transient,shared : bool) -> None: 
        """
        Adds an Entity : into load status if in Load mode, to the current part if there is one. If shared is True, adds also its shared ones (shared at all levels)
        """
    def GetFromIter(self,iter : OCP.Interface.Interface_EntityIterator) -> None: 
        """
        Adds a list of Entities (into Load mode or to a Part), given as an Iterator
        """
    def GetParts(self,other : IFGraph_SubPartsIterator) -> None: 
        """
        Gets Parts from another SubPartsIterator (in addition to the ones already recorded) Error if both SubPartsIterators are not based on the same Model
        """
    def IsInPart(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is Present in a sub-part
        """
    def IsLoaded(self,ent : OCP.Standard.Standard_Transient) -> bool: 
        """
        Returns True if an Entity is loaded (either set into a sub-part or not)
        """
    def IsSingle(self) -> bool: 
        """
        Returns True if current sub-part is single (has only one Entity) Error if there is no sub-part to iterate now
        """
    def Loaded(self) -> OCP.Interface.Interface_GraphContent: 
        """
        Returns entities which where loaded (not set into a sub-part)
        """
    def LoadedGraph(self) -> OCP.Interface.Interface_Graph: 
        """
        Same as above, but under the form of a Graph
        """
    def Model(self) -> OCP.Interface.Interface_InterfaceModel: 
        """
        Returns the Model with which this Iterator was created
        """
    def More(self) -> bool: 
        """
        Returns True if there are more sub-parts to iterate on Note : an empty sub-part is not taken in account by Iteration
        """
    def NbParts(self) -> int: 
        """
        Returns count of registered parts
        """
    def Next(self) -> None: 
        """
        Sets iteration to the next sub-part if there is not, IsSingle-Entities will raises an exception
        """
    def PartNum(self) -> int: 
        """
        Returns numero of part which currently receives entities (0 at load time)
        """
    def Reset(self) -> None: 
        """
        Erases data (parts, entities) : "me" becomes empty and in load status
        """
    def SetLoad(self) -> None: 
        """
        Sets SubPartIterator to get Entities (by GetFromEntity & GetFromIter) into load status, to be analysed later
        """
    def SetPartNum(self,num : int) -> None: 
        """
        Sets numero of receiving part to a new value Error if not in range (1-NbParts)
        """
    def Start(self) -> None: 
        """
        Sets iteration to its beginning; calls Evaluate
        """
    def __init__(self,agraph : OCP.Interface.Interface_Graph,whole : bool) -> None: ...
    pass
