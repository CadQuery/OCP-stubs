import OCP.BRepPrimAPI
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.BRepSweep
import OCP.BRepBuilderAPI
import OCP.TopTools
import OCP.gp
import OCP.BRepPrim
import OCP.Geom
import OCP.TopoDS
__all__  = [
"BRepPrimAPI_MakeBox",
"BRepPrimAPI_MakeOneAxis",
"BRepPrimAPI_MakeCylinder",
"BRepPrimAPI_MakeHalfSpace",
"BRepPrimAPI_MakeCone",
"BRepPrimAPI_MakeSweep",
"BRepPrimAPI_MakeRevol",
"BRepPrimAPI_MakeRevolution",
"BRepPrimAPI_MakeSphere",
"BRepPrimAPI_MakePrism",
"BRepPrimAPI_MakeTorus",
"BRepPrimAPI_MakeWedge"
]
class BRepPrimAPI_MakeBox(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build parallelepiped boxes. A MakeBox object provides a framework for: - defining the construction of a box, - implementing the construction algorithm, and - consulting the result.
    """
    def BackFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns XMin face
        """
    def BottomFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns ZMin face
        """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def FrontFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns XMax face
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LeftFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns YMin face
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def RightFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns YMax face
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed box as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed box as a solid.
        """
    def TopFace(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns ZMax face
        """
    def Wedge(self) -> OCP.BRepPrim.BRepPrim_Wedge: 
        """
        Returns the internal algorithm.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float) -> None: ...
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt,dx : float,dy : float,dz : float) -> None: ...
    @overload
    def __init__(self,dx : float,dy : float,dz : float) -> None: ...
    @overload
    def __init__(self,P1 : OCP.gp.gp_Pnt,P2 : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepPrimAPI_MakeOneAxis(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The abstract class MakeOneAxis is the root class of algorithms used to construct rotational primitives.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        The inherited commands should provide the algorithm. Returned as a pointer.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    pass
class BRepPrimAPI_MakeCylinder(BRepPrimAPI_MakeOneAxis, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build cylinders or portions of cylinders. A MakeCylinder object provides a framework for: - defining the construction of a cylinder, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Cylinder(self) -> OCP.BRepPrim.BRepPrim_Cylinder: 
        """
        Returns the algorithm.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        Returns the algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R : float,H : float) -> None: ...
    @overload
    def __init__(self,R : float,H : float,Angle : float) -> None: ...
    @overload
    def __init__(self,R : float,H : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R : float,H : float,Angle : float) -> None: ...
    pass
class BRepPrimAPI_MakeHalfSpace(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build half-spaces. A half-space is an infinite solid, limited by a surface. It is built from a face or a shell, which bounds it, and with a reference point, which specifies the side of the surface where the matter of the half-space is located. A half-space is a tool commonly used in topological operations to cut another shape. A MakeHalfSpace object provides a framework for: - defining and implementing the construction of a half-space, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed half-space as a solid.
        """
    @overload
    def __init__(self,Face : OCP.TopoDS.TopoDS_Face,RefPnt : OCP.gp.gp_Pnt) -> None: ...
    @overload
    def __init__(self,Shell : OCP.TopoDS.TopoDS_Shell,RefPnt : OCP.gp.gp_Pnt) -> None: ...
    pass
class BRepPrimAPI_MakeCone(BRepPrimAPI_MakeOneAxis, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build cones or portions of cones. A MakeCone object provides a framework for: - defining the construction of a cone, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Cone(self) -> OCP.BRepPrim.BRepPrim_Cone: 
        """
        Returns the algorithm.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        Returns the algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    @overload
    def __init__(self,R1 : float,R2 : float,H : float,angle : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,H : float,angle : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,H : float) -> None: ...
    @overload
    def __init__(self,R1 : float,R2 : float,H : float) -> None: ...
    pass
class BRepPrimAPI_MakeSweep(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    The abstract class MakeSweep is the root class of swept primitives. Sweeps are objects you obtain by sweeping a profile along a path. The profile can be any topology and the path is usually a curve or a wire. The profile generates objects according to the following rules: - Vertices generate Edges - Edges generate Faces. - Wires generate Shells. - Faces generate Solids. - Shells generate Composite Solids. You are not allowed to sweep Solids and Composite Solids. Two kinds of sweeps are implemented in the BRepPrimAPI package: - The linear sweep called a Prism - The rotational sweep called a Revol Swept constructions along complex profiles such as BSpline curves are also available in the BRepOffsetAPI package..
    """
    def Build(self) -> None: 
        """
        This is called by Shape(). It does nothing but may be redefined.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the sweep.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the sweep.
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    pass
class BRepPrimAPI_MakeRevol(BRepPrimAPI_MakeSweep, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Class to make revolved sweep topologies.
    """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Degenerated(self) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of degenerated edges
        """
    @overload
    def FirstShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the first shape of the revol (coinciding with the generating shape).

        Returns the TopoDS Shape of the beginning of the revolution, generated with theShape (subShape of the generating shape).
        """
    @overload
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns list of shape generated from shape S Warning: shape S must be shape of type VERTEX, EDGE, FACE, SOLID. For shapes of other types method always returns empty list
        """
    def HasDegenerated(self) -> bool: 
        """
        Check if there are degenerated edges in the result.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def LastShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the end of the revol.

        Returns the TopoDS Shape of the end of the revolution, generated with theShape (subShape of the generating shape).
        """
    @overload
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Revol(self) -> OCP.BRepSweep.BRepSweep_Revol: 
        """
        Returns the internal sweeping algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,A : OCP.gp.gp_Ax1,Copy : bool=False) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,A : OCP.gp.gp_Ax1,D : float,Copy : bool=False) -> None: ...
    pass
class BRepPrimAPI_MakeRevolution(BRepPrimAPI_MakeOneAxis, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build revolved shapes. A MakeRevolution object provides a framework for: - defining the construction of a revolved shape, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        Returns the algorithm.
        """
    def Revolution(self) -> OCP.BRepPrim.BRepPrim_Revolution: 
        """
        Returns the algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Meridian : OCP.Geom.Geom_Curve,VMin : float,VMax : float,angle : float) -> None: ...
    @overload
    def __init__(self,Meridian : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Meridian : OCP.Geom.Geom_Curve,VMin : float,VMax : float) -> None: ...
    @overload
    def __init__(self,Meridian : OCP.Geom.Geom_Curve,VMin : float,VMax : float,angle : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Meridian : OCP.Geom.Geom_Curve) -> None: ...
    @overload
    def __init__(self,Meridian : OCP.Geom.Geom_Curve,angle : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,Meridian : OCP.Geom.Geom_Curve,angle : float) -> None: ...
    @overload
    def __init__(self,Meridian : OCP.Geom.Geom_Curve,VMin : float,VMax : float) -> None: ...
    pass
class BRepPrimAPI_MakeSphere(BRepPrimAPI_MakeOneAxis, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build spheres or portions of spheres. A MakeSphere object provides a framework for: - defining the construction of a sphere, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        Returns the algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    def Sphere(self) -> OCP.BRepPrim.BRepPrim_Sphere: 
        """
        Returns the algorithm.
        """
    @overload
    def __init__(self,R : float,angle1 : float,angle2 : float,angle3 : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax2,R : float,angle1 : float,angle2 : float,angle3 : float) -> None: ...
    @overload
    def __init__(self,R : float,angle1 : float,angle2 : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R : float,angle1 : float,angle2 : float,angle3 : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax2,R : float,angle : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax2,R : float,angle1 : float,angle2 : float) -> None: ...
    @overload
    def __init__(self,R : float,angle : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R : float,angle1 : float,angle2 : float) -> None: ...
    @overload
    def __init__(self,R : float) -> None: ...
    @overload
    def __init__(self,Center : OCP.gp.gp_Pnt,R : float,angle : float) -> None: ...
    @overload
    def __init__(self,Axis : OCP.gp.gp_Ax2,R : float) -> None: ...
    pass
class BRepPrimAPI_MakePrism(BRepPrimAPI_MakeSweep, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build linear swept topologies, called prisms. A prism is defined by: - a basis shape, which is swept, and - a sweeping direction, which is: - a vector for finite prisms, or - a direction for infinite or semi-infinite prisms. The basis shape must not contain any solids. The profile generates objects according to the following rules: - Vertices generate Edges - Edges generate Faces. - Wires generate Shells. - Faces generate Solids. - Shells generate Composite Solids A MakePrism object provides a framework for: - defining the construction of a prism, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Builds the resulting shape (redefined from MakeShape).
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    @overload
    def FirstShape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the bottom of the prism.

        Returns the TopoDS Shape of the bottom of the prism. generated with theShape (subShape of the generating shape).
        """
    @overload
    def FirstShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: ...
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns ListOfShape from TopTools.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    @overload
    def LastShape(self,theShape : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns the TopoDS Shape of the top of the prism. In the case of a finite prism, FirstShape returns the basis of the prism, in other words, S if Copy is false; otherwise, the copy of S belonging to the prism. LastShape returns the copy of S translated by V at the time of construction.

        Returns the TopoDS Shape of the top of the prism. generated with theShape (subShape of the generating shape).
        """
    @overload
    def LastShape(self) -> OCP.TopoDS.TopoDS_Shape: ...
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Prism(self) -> OCP.BRepSweep.BRepSweep_Prism: 
        """
        Returns the internal sweeping algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,V : OCP.gp.gp_Vec,Copy : bool=False,Canonize : bool=True) -> None: ...
    @overload
    def __init__(self,S : OCP.TopoDS.TopoDS_Shape,D : OCP.gp.gp_Dir,Inf : bool=True,Copy : bool=False,Canonize : bool=True) -> None: ...
    pass
class BRepPrimAPI_MakeTorus(BRepPrimAPI_MakeOneAxis, OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build tori or portions of tori. A MakeTorus object provides a framework for: - defining the construction of a torus, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        Returns the lateral face of the rotational primitive.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def OneAxis(self) -> capsule: 
        """
        Returns the algorithm.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed rotational primitive as a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed rotational primitive as a solid.
        """
    def Torus(self) -> OCP.BRepPrim.BRepPrim_Torus: 
        """
        Returns the algorithm.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,angle1 : float,angle2 : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,angle : float) -> None: ...
    @overload
    def __init__(self,R1 : float,R2 : float,angle1 : float,angle2 : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,R1 : float,R2 : float,angle1 : float,angle2 : float,angle : float) -> None: ...
    @overload
    def __init__(self,R1 : float,R2 : float,angle1 : float,angle2 : float,angle : float) -> None: ...
    @overload
    def __init__(self,R1 : float,R2 : float,angle : float) -> None: ...
    @overload
    def __init__(self,R1 : float,R2 : float) -> None: ...
    pass
class BRepPrimAPI_MakeWedge(OCP.BRepBuilderAPI.BRepBuilderAPI_MakeShape, OCP.BRepBuilderAPI.BRepBuilderAPI_Command):
    """
    Describes functions to build wedges, i.e. boxes with inclined faces. A MakeWedge object provides a framework for: - defining the construction of a wedge, - implementing the construction algorithm, and - consulting the result.
    """
    def Build(self) -> None: 
        """
        Stores the solid in myShape.
        """
    def Check(self) -> None: 
        """
        Raises NotDone if done is false.
        """
    def Generated(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes generated from the shape <S>.
        """
    def IsDeleted(self,S : OCP.TopoDS.TopoDS_Shape) -> bool: 
        """
        Returns true if the shape S has been deleted.
        """
    def IsDone(self) -> bool: 
        """
        None
        """
    def Modified(self,S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopTools.TopTools_ListOfShape: 
        """
        Returns the list of shapes modified from the shape <S>.
        """
    def Shape(self) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a shape built by the shape construction algorithm. Raises exception StdFail_NotDone if the shape was not built.
        """
    def Shell(self) -> OCP.TopoDS.TopoDS_Shell: 
        """
        Returns the constructed box in the form of a shell.
        """
    def Solid(self) -> OCP.TopoDS.TopoDS_Solid: 
        """
        Returns the constructed box in the form of a solid.
        """
    def Wedge(self) -> OCP.BRepPrim.BRepPrim_Wedge: 
        """
        Returns the internal algorithm.
        """
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float,ltx : float) -> None: ...
    @overload
    def __init__(self,dx : float,dy : float,dz : float,xmin : float,zmin : float,xmax : float,zmax : float) -> None: ...
    @overload
    def __init__(self,Axes : OCP.gp.gp_Ax2,dx : float,dy : float,dz : float,xmin : float,zmin : float,xmax : float,zmax : float) -> None: ...
    @overload
    def __init__(self,dx : float,dy : float,dz : float,ltx : float) -> None: ...
    pass
