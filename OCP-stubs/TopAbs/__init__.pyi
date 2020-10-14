import OCP.TopAbs
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
__all__  = [
"TopAbs",
"TopAbs_Orientation",
"TopAbs_ShapeEnum",
"TopAbs_State",
"TopAbs_COMPOUND",
"TopAbs_COMPSOLID",
"TopAbs_EDGE",
"TopAbs_EXTERNAL",
"TopAbs_FACE",
"TopAbs_FORWARD",
"TopAbs_IN",
"TopAbs_INTERNAL",
"TopAbs_ON",
"TopAbs_OUT",
"TopAbs_REVERSED",
"TopAbs_SHAPE",
"TopAbs_SHELL",
"TopAbs_SOLID",
"TopAbs_UNKNOWN",
"TopAbs_VERTEX",
"TopAbs_WIRE"
]
class TopAbs():
    """
    This package gives resources for Topology oriented applications such as : Topological Data Structure, Topological Algorithms.
    """
    @staticmethod
    def Complement_s(Or : TopAbs_Orientation) -> TopAbs_Orientation: 
        """
        Reverses the interior/exterior status of each side of the object. So, to take the complement of an object means to reverse the interior/exterior status of its boundary, i.e. inside becomes outside. The method returns the complementary orientation, following the rules in the table below: FORWARD REVERSED REVERSED FORWARD INTERNAL EXTERNAL EXTERNAL INTERNAL
        """
    @staticmethod
    def Compose_s(Or1 : TopAbs_Orientation,Or2 : TopAbs_Orientation) -> TopAbs_Orientation: 
        """
        Compose the Orientation <Or1> and <Or2>. This composition is not symmetric (if you switch <Or1> and <Or2> the result is different). It assumes that <Or1> is the Orientation of a Shape S1 containing a Shape S2 of Orientation Or2. The result is the cumulated orientation of S2 in S1. The composition law is :
        """
    @staticmethod
    @overload
    def Print_s(theShapeType : TopAbs_ShapeEnum,theStream : Any) -> Any: 
        """
        Prints the name of Shape type as a String on the Stream.

        Prints the name of the Orientation as a String on the Stream.

        Prints the name of the State <St> as a String on the Stream <S> and returns <S>.
        """
    @staticmethod
    @overload
    def Print_s(theOrientation : TopAbs_Orientation,theStream : Any) -> Any: ...
    @staticmethod
    @overload
    def Print_s(St : TopAbs_State,S : Any) -> Any: ...
    @staticmethod
    def Reverse_s(Or : TopAbs_Orientation) -> TopAbs_Orientation: 
        """
        xchanges the interior/exterior status of the two sides. This is what happens when the sense of direction is reversed. The following rules apply:
        """
    @staticmethod
    @overload
    def ShapeOrientationFromString_s(theOrientationString : str,theOrientation : TopAbs_Orientation) -> bool: 
        """
        Returns the shape orientation from the given string identifier (using case-insensitive comparison).

        Determines the shape orientation from the given string identifier (using case-insensitive comparison).
        """
    @staticmethod
    @overload
    def ShapeOrientationFromString_s(theOrientationString : str) -> TopAbs_Orientation: ...
    @staticmethod
    def ShapeOrientationToString_s(theOrientation : TopAbs_Orientation) -> str: 
        """
        Returns the string name for a given shape orientation.
        """
    @staticmethod
    @overload
    def ShapeTypeFromString_s(theTypeString : str,theType : TopAbs_ShapeEnum) -> bool: 
        """
        Returns the shape type from the given string identifier (using case-insensitive comparison).

        Determines the shape type from the given string identifier (using case-insensitive comparison).
        """
    @staticmethod
    @overload
    def ShapeTypeFromString_s(theTypeString : str) -> TopAbs_ShapeEnum: ...
    @staticmethod
    def ShapeTypeToString_s(theType : TopAbs_ShapeEnum) -> str: 
        """
        Returns the string name for a given shape type.
        """
    def __init__(self) -> None: ...
    pass
class TopAbs_Orientation():
    """
    Identifies the orientation of a topological shape. Orientation can represent a relation between two entities, or it can apply to a shape in its own right. When used to describe a relation between two shapes, orientation allows you to use the underlying entity in either direction. For example on a curve which is oriented FORWARD (say from left to right) you can have both a FORWARD and a REVERSED edge. The FORWARD edge will be oriented from left to right, and the REVERSED edge from right to left. In this way, you share the underlying entity. In other words, two faces of a cube can share an edge, and can also be used to build compound shapes. For each case in which an element is used as the boundary of a geometric domain of a higher dimension, this element defines two local regions of which one is arbitrarily considered as the default region. A change in orientation implies a switch of default region. This allows you to apply changes of orientation to the shape as a whole.

    Members:

      TopAbs_FORWARD

      TopAbs_REVERSED

      TopAbs_INTERNAL

      TopAbs_EXTERNAL
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
    TopAbs_EXTERNAL: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_EXTERNAL
    TopAbs_FORWARD: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_FORWARD
    TopAbs_INTERNAL: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_INTERNAL
    TopAbs_REVERSED: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_REVERSED
    __entries: dict # value = {'TopAbs_FORWARD': (TopAbs_Orientation.TopAbs_FORWARD, None), 'TopAbs_REVERSED': (TopAbs_Orientation.TopAbs_REVERSED, None), 'TopAbs_INTERNAL': (TopAbs_Orientation.TopAbs_INTERNAL, None), 'TopAbs_EXTERNAL': (TopAbs_Orientation.TopAbs_EXTERNAL, None)}
    __members__: dict # value = {'TopAbs_FORWARD': TopAbs_Orientation.TopAbs_FORWARD, 'TopAbs_REVERSED': TopAbs_Orientation.TopAbs_REVERSED, 'TopAbs_INTERNAL': TopAbs_Orientation.TopAbs_INTERNAL, 'TopAbs_EXTERNAL': TopAbs_Orientation.TopAbs_EXTERNAL}
    pass
class TopAbs_ShapeEnum():
    """
    Identifies various topological shapes. This enumeration allows you to use dynamic typing of shapes. The values are listed in order of complexity, from the most complex to the most simple i.e. COMPOUND > COMPSOLID > SOLID > .... > VERTEX > SHAPE. Any shape can contain simpler shapes in its definition. Abstract topological data structure describes a basic entity, the shape (present in this enumeration as the SHAPE value), which can be divided into the following component topologies: - COMPOUND: A group of any of the shapes below. - COMPSOLID: A set of solids connected by their faces. This expands the notions of WIRE and SHELL to solids. - SOLID: A part of 3D space bounded by shells. - SHELL: A set of faces connected by some of the edges of their wire boundaries. A shell can be open or closed. - FACE: Part of a plane (in 2D geometry) or a surface (in 3D geometry) bounded by a closed wire. Its geometry is constrained (trimmed) by contours. - WIRE: A sequence of edges connected by their vertices. It can be open or closed depending on whether the edges are linked or not. - EDGE: A single dimensional shape corresponding to a curve, and bound by a vertex at each extremity. - VERTEX: A zero-dimensional shape corresponding to a point in geometry.

    Members:

      TopAbs_COMPOUND

      TopAbs_COMPSOLID

      TopAbs_SOLID

      TopAbs_SHELL

      TopAbs_FACE

      TopAbs_WIRE

      TopAbs_EDGE

      TopAbs_VERTEX

      TopAbs_SHAPE
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
    TopAbs_COMPOUND: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_COMPOUND
    TopAbs_COMPSOLID: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_COMPSOLID
    TopAbs_EDGE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_EDGE
    TopAbs_FACE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_FACE
    TopAbs_SHAPE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SHAPE
    TopAbs_SHELL: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SHELL
    TopAbs_SOLID: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SOLID
    TopAbs_VERTEX: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_VERTEX
    TopAbs_WIRE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_WIRE
    __entries: dict # value = {'TopAbs_COMPOUND': (TopAbs_ShapeEnum.TopAbs_COMPOUND, None), 'TopAbs_COMPSOLID': (TopAbs_ShapeEnum.TopAbs_COMPSOLID, None), 'TopAbs_SOLID': (TopAbs_ShapeEnum.TopAbs_SOLID, None), 'TopAbs_SHELL': (TopAbs_ShapeEnum.TopAbs_SHELL, None), 'TopAbs_FACE': (TopAbs_ShapeEnum.TopAbs_FACE, None), 'TopAbs_WIRE': (TopAbs_ShapeEnum.TopAbs_WIRE, None), 'TopAbs_EDGE': (TopAbs_ShapeEnum.TopAbs_EDGE, None), 'TopAbs_VERTEX': (TopAbs_ShapeEnum.TopAbs_VERTEX, None), 'TopAbs_SHAPE': (TopAbs_ShapeEnum.TopAbs_SHAPE, None)}
    __members__: dict # value = {'TopAbs_COMPOUND': TopAbs_ShapeEnum.TopAbs_COMPOUND, 'TopAbs_COMPSOLID': TopAbs_ShapeEnum.TopAbs_COMPSOLID, 'TopAbs_SOLID': TopAbs_ShapeEnum.TopAbs_SOLID, 'TopAbs_SHELL': TopAbs_ShapeEnum.TopAbs_SHELL, 'TopAbs_FACE': TopAbs_ShapeEnum.TopAbs_FACE, 'TopAbs_WIRE': TopAbs_ShapeEnum.TopAbs_WIRE, 'TopAbs_EDGE': TopAbs_ShapeEnum.TopAbs_EDGE, 'TopAbs_VERTEX': TopAbs_ShapeEnum.TopAbs_VERTEX, 'TopAbs_SHAPE': TopAbs_ShapeEnum.TopAbs_SHAPE}
    pass
class TopAbs_State():
    """
    Identifies the position of a vertex or a set of vertices relative to a region of a shape. The figure shown above illustrates the states of vertices found in various parts of the edge relative to the face which it intersects.

    Members:

      TopAbs_IN

      TopAbs_OUT

      TopAbs_ON

      TopAbs_UNKNOWN
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
    TopAbs_IN: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_IN
    TopAbs_ON: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_ON
    TopAbs_OUT: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_OUT
    TopAbs_UNKNOWN: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_UNKNOWN
    __entries: dict # value = {'TopAbs_IN': (TopAbs_State.TopAbs_IN, None), 'TopAbs_OUT': (TopAbs_State.TopAbs_OUT, None), 'TopAbs_ON': (TopAbs_State.TopAbs_ON, None), 'TopAbs_UNKNOWN': (TopAbs_State.TopAbs_UNKNOWN, None)}
    __members__: dict # value = {'TopAbs_IN': TopAbs_State.TopAbs_IN, 'TopAbs_OUT': TopAbs_State.TopAbs_OUT, 'TopAbs_ON': TopAbs_State.TopAbs_ON, 'TopAbs_UNKNOWN': TopAbs_State.TopAbs_UNKNOWN}
    pass
TopAbs_COMPOUND: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_COMPOUND
TopAbs_COMPSOLID: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_COMPSOLID
TopAbs_EDGE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_EDGE
TopAbs_EXTERNAL: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_EXTERNAL
TopAbs_FACE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_FACE
TopAbs_FORWARD: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_FORWARD
TopAbs_IN: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_IN
TopAbs_INTERNAL: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_INTERNAL
TopAbs_ON: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_ON
TopAbs_OUT: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_OUT
TopAbs_REVERSED: OCP.TopAbs.TopAbs_Orientation # value = TopAbs_Orientation.TopAbs_REVERSED
TopAbs_SHAPE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SHAPE
TopAbs_SHELL: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SHELL
TopAbs_SOLID: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_SOLID
TopAbs_UNKNOWN: OCP.TopAbs.TopAbs_State # value = TopAbs_State.TopAbs_UNKNOWN
TopAbs_VERTEX: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_VERTEX
TopAbs_WIRE: OCP.TopAbs.TopAbs_ShapeEnum # value = TopAbs_ShapeEnum.TopAbs_WIRE
