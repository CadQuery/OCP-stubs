import OCP.ShapeCustom
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopTools
import OCP.Message
import OCP.BRepTools
import OCP.GeomAbs
import OCP.Geom
import OCP.TColgp
import OCP.TopoDS
import OCP.gp
import OCP.TopLoc
import OCP.Geom2d
import OCP.Standard
import OCP.ShapeExtend
import OCP.Poly
__all__  = [
"ShapeCustom",
"ShapeCustom_Modification",
"ShapeCustom_ConvertToBSpline",
"ShapeCustom_ConvertToRevolution",
"ShapeCustom_Curve",
"ShapeCustom_Curve2d",
"ShapeCustom_DirectModification",
"ShapeCustom_BSplineRestriction",
"ShapeCustom_RestrictionParameters",
"ShapeCustom_Surface",
"ShapeCustom_SweptToElementary",
"ShapeCustom_TrsfModification"
]
class ShapeCustom():
    """
    This package is intended to convert geometrical objects and topological. The modifications of one geometrical object to another (one) geometrical object are provided. The supported modifications are the following: conversion of BSpline and Bezier surfaces to analytical form, conversion of indirect elementary surfaces (with left-handed coordinate systems) into direct ones, conversion of elementary surfaces to surfaces of revolution, conversion of surface of linear extrusion, revolution, offset surface to bspline, modification of parameterization, degree, number of segments of bspline surfaces, scale the shape.
    """
    @staticmethod
    def ApplyModifier_s(S : OCP.TopoDS.TopoDS_Shape,M : OCP.BRepTools.BRepTools_Modification,context : OCP.TopTools.TopTools_DataMapOfShapeShape,MD : OCP.BRepTools.BRepTools_Modifier,theProgress : OCP.Message.Message_ProgressRange=OCP.Message.Message_ProgressRange,aReShape : OCP.ShapeBuild.ShapeBuild_ReShape=None) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Applies modifier to shape and checks sharing in the case assemblies.
        """
    @staticmethod
    def BSplineRestriction_s(S : OCP.TopoDS.TopoDS_Shape,Tol3d : float,Tol2d : float,MaxDegree : int,MaxNbSegment : int,Continuity3d : OCP.GeomAbs.GeomAbs_Shape,Continuity2d : OCP.GeomAbs.GeomAbs_Shape,Degree : bool,Rational : bool,aParameters : ShapeCustom_RestrictionParameters) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape with all surfaces, curves and pcurves which type is BSpline/Bezier or based on them converted having Degree less than <MaxDegree> or number of spans less than <NbMaxSegment> in dependence on parameter priority <Degree>. <GmaxDegree> and <GMaxSegments> are maximum possible degree and number of spans correspondingly. These values will be used in those cases when approximation with specified parameters is impossible and one of GmaxDegree or GMaxSegments is selected in dependence on priority. Note that even if approximation is impossible with <GMaxDegree> then number of spans can exceed specified <GMaxSegment> <Rational> specifies if to convert Rational BSpline/Bezier into polynomial B-Spline. If flags ConvOffSurf,ConvOffCurve3d,ConvOffCurve2d are Standard_True there are means that Offset surfaces , Offset curves 3d and Offset curves 2d are converted to BSPline correspondingly.
        """
    @staticmethod
    def ConvertToBSpline_s(S : OCP.TopoDS.TopoDS_Shape,extrMode : bool,revolMode : bool,offsetMode : bool,planeMode : bool=False) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape with all surfaces of linear extrusion, revolution, offset, and planar surfaces converted according to flags to Geom_BSplineSurface (with same parameterisation).
        """
    @staticmethod
    def ConvertToRevolution_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape with all elementary periodic surfaces converted to Geom_SurfaceOfRevolution
        """
    @staticmethod
    def DirectFaces_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape without indirect surfaces.
        """
    @staticmethod
    def ScaleShape_s(S : OCP.TopoDS.TopoDS_Shape,scale : float) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape which is scaled original
        """
    @staticmethod
    def SweptToElementary_s(S : OCP.TopoDS.TopoDS_Shape) -> OCP.TopoDS.TopoDS_Shape: 
        """
        Returns a new shape with all surfaces of revolution and linear extrusion convert to elementary periodic surfaces
        """
    def __init__(self) -> None: ...
    pass
class ShapeCustom_Modification(OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    A base class of Modification's from ShapeCustom. Implements message sending mechanism.A base class of Modification's from ShapeCustom. Implements message sending mechanism.A base class of Modification's from ShapeCustom. Implements message sending mechanism.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>. <NewE> is the new edge created from <E>. <NewF1> (resp. <NewF2>) is the new face created from <F1> (resp. <F2>).
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
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns true if the edge, E, has been modified. If the edge has been modified: - C is the new geometry associated with the edge, - L is its new location, and - Tol is the new tolerance. If the edge has not been modified, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns true if the edge, E, has a new curve on surface on the face, F. If a new curve exists: - C is the new geometry of the edge, - L is the new location, and - Tol is the new tolerance. NewE is the new edge created from E, and NewF is the new face created from F. If there is no new curve on the face, this function returns false, and the values of C, L and Tol are not significant.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns true if the vertex V has a new parameter on the edge E. If a new parameter exists: - P is the parameter, and - Tol is the new tolerance. If there is no new parameter this function returns false, and the values of P and Tol are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns true if the vertex V has been modified. If V has been modified: - P is the new geometry of the vertex, and - Tol is the new tolerance. If the vertex has not been modified this function returns false, and the values of P and Tol are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns true if the face, F, has been modified. If the face has been modified: - S is the new geometry of the face, - L is its new location, and - Tol is the new tolerance. The flag, RevWires, is set to true when the modification reverses the normal of the surface, (i.e. the wires have to be reversed). The flag, RevFace, is set to true if the orientation of the modified face changes in the shells which contain it. If the face has not been modified this function returns false, and the values of S, L, Tol, RevWires and RevFace are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
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
class ShapeCustom_ConvertToBSpline(ShapeCustom_Modification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    implement a modification for BRepTools Modifier algortihm. Converts Surface of Linear Exctrusion, Revolution and Offset surfaces into BSpline Surface according to flags.implement a modification for BRepTools Modifier algortihm. Converts Surface of Linear Exctrusion, Revolution and Offset surfaces into BSpline Surface according to flags.implement a modification for BRepTools Modifier algortihm. Converts Surface of Linear Exctrusion, Revolution and Offset surfaces into BSpline Surface according to flags.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <S>, <L>, <Tol> are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetExtrusionMode(self,extrMode : bool) -> None: 
        """
        Sets mode for convertion of Surfaces of Linear extrusion.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetOffsetMode(self,offsetMode : bool) -> None: 
        """
        Sets mode for convertion of Offset surfaces.
        """
    def SetPlaneMode(self,planeMode : bool) -> None: 
        """
        Sets mode for convertion of Plane surfaces.
        """
    def SetRevolutionMode(self,revolMode : bool) -> None: 
        """
        Sets mode for convertion of Surfaces of Revolution.
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
class ShapeCustom_ConvertToRevolution(ShapeCustom_Modification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <S>, <L>, <Tol> are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
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
class ShapeCustom_Curve():
    """
    Converts BSpline curve to periodic
    """
    def ConvertToPeriodic(self,substitute : bool,preci : float=-1.0) -> OCP.Geom.Geom_Curve: 
        """
        Tries to convert the Curve to the Periodic form Returns the resulting curve Works only if the Curve is BSpline and is closed with Precision::Confusion() Else, or in case of failure, returns a Null Handle
        """
    def Init(self,C : OCP.Geom.Geom_Curve) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,C : OCP.Geom.Geom_Curve) -> None: ...
    pass
class ShapeCustom_Curve2d():
    """
    Converts curve2d to analytical form with given precision or simpify curve2d.
    """
    @staticmethod
    def ConvertToLine2d_s(theCurve : OCP.Geom2d.Geom2d_Curve,theFirstIn : float,theLastIn : float,theTolerance : float,theNewFirst : float,theNewLast : float,theDeviation : float) -> OCP.Geom2d.Geom2d_Line: 
        """
        Try to convert BSpline2d or Bezier2d to line 2d only if it is linear. Recalculate first and last parameters. Returns line2d or null curve2d.
        """
    @staticmethod
    def IsLinear_s(thePoles : OCP.TColgp.TColgp_Array1OfPnt2d,theTolerance : float,theDeviation : float) -> bool: 
        """
        Check if poleses is in the plane with given precision Returns false if no.
        """
    @staticmethod
    def SimplifyBSpline2d_s(theBSpline2d : OCP.Geom2d.Geom2d_BSplineCurve,theTolerance : float) -> bool: 
        """
        Try to remove knots from bspline where local derivatives are the same. Remove knots with given precision. Returns false if Bsplien was not modified
        """
    def __init__(self) -> None: ...
    pass
class ShapeCustom_DirectModification(ShapeCustom_Modification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    implements a modification for the BRepTools Modifier algortihm. Will redress indirect surfaces.implements a modification for the BRepTools Modifier algortihm. Will redress indirect surfaces.implements a modification for the BRepTools Modifier algortihm. Will redress indirect surfaces.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <S>, <L>, <Tol> are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
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
class ShapeCustom_BSplineRestriction(ShapeCustom_Modification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    this tool intended for aproximation surfaces, curves and pcurves with specified degree , max number of segments, tolerance 2d, tolerance 3d. Specified continuity can be reduced if approximation with specified continuity was not done.this tool intended for aproximation surfaces, curves and pcurves with specified degree , max number of segments, tolerance 2d, tolerance 3d. Specified continuity can be reduced if approximation with specified continuity was not done.this tool intended for aproximation surfaces, curves and pcurves with specified degree , max number of segments, tolerance 2d, tolerance 3d. Specified continuity can be reduced if approximation with specified continuity was not done.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        None
        """
    def ConvertCurve(self,aCurve : OCP.Geom.Geom_Curve,C : OCP.Geom.Geom_Curve,IsConvert : bool,First : float,Last : float,TolCur : float,IsOf : bool=True) -> bool: 
        """
        Returns Standard_True if the curve has been modified. if flag IsOf equals Standard_True Offset curves are aproximated to Offset if Standard_False to BSpline
        """
    def ConvertCurve2d(self,aCurve : OCP.Geom2d.Geom2d_Curve,C : OCP.Geom2d.Geom2d_Curve,IsConvert : bool,First : float,Last : float,TolCur : float,IsOf : bool=True) -> bool: 
        """
        Returns Standard_True if the pcurve has been modified. if flag IsOf equals Standard_True Offset pcurves are aproximated to Offset if Standard_False to BSpline
        """
    def ConvertSurface(self,aSurface : OCP.Geom.Geom_Surface,S : OCP.Geom.Geom_Surface,UF : float,UL : float,VF : float,VL : float,IsOf : bool=True) -> bool: 
        """
        Returns Standard_True if the surface has been modified. if flag IsOf equals Standard_True Offset surfaces are aproximated to Offset if Standard_False to BSpline
        """
    def Curve2dError(self) -> float: 
        """
        Returns error for aproximation curve2d.

        Returns error for aproximation curve2d.
        """
    def Curve3dError(self) -> float: 
        """
        Returns error for aproximation curve3d.

        Returns error for aproximation curve3d.
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
    def GetRestrictionParameters(self) -> ShapeCustom_RestrictionParameters: 
        """
        Returns the container of modes which defines what geometry should be converted to BSplines.

        Returns the container of modes which defines what geometry should be converted to BSplines.
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
    def MaxErrors(self,aCurve3dErr : float,aCurve2dErr : float) -> float: 
        """
        Returns error for aproximation surface, curve3d and curve2d.
        """
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NbOfSpan(self) -> int: 
        """
        Returns number for aproximation surface, curve3d and curve2d.
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if curve from the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_True if Surface is modified or one of pcurves of edge is modified. In this case C is copy of geometric support of the edge. In other cases returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case,if curve on the surface is modified, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. If curve on the surface is not modified C is copy curve on surface from the edge <E>.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        None
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        None
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location,<Tol> the new tolerance.<RevWires> has to be set to Standard_True when the modification reverses the normal of the surface.(the wires have to be reversed). <RevFace> has to be set to Standard_True if the orientation of the modified face changes in the shells which contain it.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetContinuity2d(self,Continuity2d : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets continuity3d for aproximation curve2d.

        Sets continuity3d for aproximation curve2d.
        """
    def SetContinuity3d(self,Continuity3d : OCP.GeomAbs.GeomAbs_Shape) -> None: 
        """
        Sets continuity3d for aproximation curve3d and surface.

        Sets continuity3d for aproximation curve3d and surface.
        """
    def SetConvRational(self,Rational : bool) -> None: 
        """
        Sets flag for define if rational BSpline or Bezier is converted to polynomial. If Rational is True approximation for rational BSpline and Bezier is made to polynomial even if degree is less then MaxDegree and number of spans is less then specified MaxNbSegment.

        Sets flag for define if rational BSpline or Bezier is converted to polynomial. If Rational is True approximation for rational BSpline and Bezier is made to polynomial even if degree is less then MaxDegree and number of spans is less then specified MaxNbSegment.
        """
    def SetMaxDegree(self,MaxDegree : int) -> None: 
        """
        Sets max degree for aproximation.

        Sets max degree for aproximation.
        """
    def SetMaxNbSegments(self,MaxNbSegments : int) -> None: 
        """
        Sets max number of segments for aproximation.

        Sets max number of segments for aproximation.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
        """
    def SetPriority(self,Degree : bool) -> None: 
        """
        Sets priority for aproximation curves and surface. If Degree is True approximation is made with degree less then specified MaxDegree at the expense of number of spanes. If Degree is False approximation is made with number of spans less then specified MaxNbSegment at the expense of specified MaxDegree.

        Sets priority for aproximation curves and surface. If Degree is True approximation is made with degree less then specified MaxDegree at the expense of number of spanes. If Degree is False approximation is made with number of spans less then specified MaxNbSegment at the expense of specified MaxDegree.
        """
    def SetRestrictionParameters(self,aModes : ShapeCustom_RestrictionParameters) -> None: 
        """
        Sets the container of modes which defines what geometry should be converted to BSplines.

        Sets the container of modes which defines what geometry should be converted to BSplines.
        """
    def SetTol2d(self,Tol2d : float) -> None: 
        """
        Sets tolerance of aproximation for curve2d

        Sets tolerance of aproximation for curve2d
        """
    def SetTol3d(self,Tol3d : float) -> None: 
        """
        Sets tolerance of aproximation for curve3d and surface

        Sets tolerance of aproximation for curve3d and surface
        """
    def SurfaceError(self) -> float: 
        """
        Returns error for aproximation surface.

        Returns error for aproximation surface.
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    @overload
    def __init__(self,anApproxSurfaceFlag : bool,anApproxCurve3dFlag : bool,anApproxCurve2dFlag : bool,aTol3d : float,aTol2d : float,aContinuity3d : OCP.GeomAbs.GeomAbs_Shape,aContinuity2d : OCP.GeomAbs.GeomAbs_Shape,aMaxDegree : int,aNbMaxSeg : int,Degree : bool,Rational : bool) -> None: ...
    @overload
    def __init__(self,anApproxSurfaceFlag : bool,anApproxCurve3dFlag : bool,anApproxCurve2dFlag : bool,aTol3d : float,aTol2d : float,aContinuity3d : OCP.GeomAbs.GeomAbs_Shape,aContinuity2d : OCP.GeomAbs.GeomAbs_Shape,aMaxDegree : int,aNbMaxSeg : int,Degree : bool,Rational : bool,aModes : ShapeCustom_RestrictionParameters) -> None: ...
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
    @property
    def ModifyApproxCurve2dFlag(self) -> bool:
        """
        :type: bool
        """
    @ModifyApproxCurve2dFlag.setter
    def ModifyApproxCurve2dFlag(self, arg1: bool) -> None:
        pass
    @property
    def ModifyApproxCurve3dFlag(self) -> bool:
        """
        :type: bool
        """
    @ModifyApproxCurve3dFlag.setter
    def ModifyApproxCurve3dFlag(self, arg1: bool) -> None:
        pass
    @property
    def ModifyApproxSurfaceFlag(self) -> bool:
        """
        :type: bool
        """
    @ModifyApproxSurfaceFlag.setter
    def ModifyApproxSurfaceFlag(self, arg1: bool) -> None:
        pass
    pass
class ShapeCustom_RestrictionParameters(OCP.Standard.Standard_Transient):
    """
    This class is axuluary tool which contains parameters for BSplineRestriction class.This class is axuluary tool which contains parameters for BSplineRestriction class.This class is axuluary tool which contains parameters for BSplineRestriction class.
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
    def ConvertBezierSurf(self) -> bool:
        """
        Sets flag for define if Bezier surface converted to BSpline surface.

        :type: bool
        """
    @ConvertBezierSurf.setter
    def ConvertBezierSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if Bezier surface converted to BSpline surface.
        """
    @property
    def ConvertConicalSurf(self) -> bool:
        """
        Sets flag for define if conical surface converted to BSpline surface.

        :type: bool
        """
    @ConvertConicalSurf.setter
    def ConvertConicalSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if conical surface converted to BSpline surface.
        """
    @property
    def ConvertCurve2d(self) -> bool:
        """
        :type: bool
        """
    @ConvertCurve2d.setter
    def ConvertCurve2d(self, arg1: bool) -> None:
        pass
    @property
    def ConvertCurve3d(self) -> bool:
        """
        Sets flag for define if 3d curve converted to BSpline curve.

        :type: bool
        """
    @ConvertCurve3d.setter
    def ConvertCurve3d(self, arg1: bool) -> None:
        """
        Sets flag for define if 3d curve converted to BSpline curve.
        """
    @property
    def ConvertCylindricalSurf(self) -> bool:
        """
        Sets flag for define if cylindrical surface converted to BSpline surface.

        :type: bool
        """
    @ConvertCylindricalSurf.setter
    def ConvertCylindricalSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if cylindrical surface converted to BSpline surface.
        """
    @property
    def ConvertExtrusionSurf(self) -> bool:
        """
        Sets flag for define if surface of LinearExtrusion converted to BSpline surface.

        :type: bool
        """
    @ConvertExtrusionSurf.setter
    def ConvertExtrusionSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if surface of LinearExtrusion converted to BSpline surface.
        """
    @property
    def ConvertOffsetCurv2d(self) -> bool:
        """
        :type: bool
        """
    @ConvertOffsetCurv2d.setter
    def ConvertOffsetCurv2d(self, arg1: bool) -> None:
        pass
    @property
    def ConvertOffsetCurv3d(self) -> bool:
        """
        Sets flag for define if Offset curve3d converted to BSpline surface.

        :type: bool
        """
    @ConvertOffsetCurv3d.setter
    def ConvertOffsetCurv3d(self, arg1: bool) -> None:
        """
        Sets flag for define if Offset curve3d converted to BSpline surface.
        """
    @property
    def ConvertOffsetSurf(self) -> bool:
        """
        Sets flag for define if Offset surface converted to BSpline surface.

        :type: bool
        """
    @ConvertOffsetSurf.setter
    def ConvertOffsetSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if Offset surface converted to BSpline surface.
        """
    @property
    def ConvertPlane(self) -> bool:
        """
        Sets flag for define if Plane converted to BSpline surface.

        :type: bool
        """
    @ConvertPlane.setter
    def ConvertPlane(self, arg1: bool) -> None:
        """
        Sets flag for define if Plane converted to BSpline surface.
        """
    @property
    def ConvertRevolutionSurf(self) -> bool:
        """
        Sets flag for define if surface of Revolution converted to BSpline surface.

        :type: bool
        """
    @ConvertRevolutionSurf.setter
    def ConvertRevolutionSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if surface of Revolution converted to BSpline surface.
        """
    @property
    def ConvertSphericalSurf(self) -> bool:
        """
        Sets flag for define if spherical surface converted to BSpline surface.

        :type: bool
        """
    @ConvertSphericalSurf.setter
    def ConvertSphericalSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if spherical surface converted to BSpline surface.
        """
    @property
    def ConvertToroidalSurf(self) -> bool:
        """
        Sets flag for define if toroidal surface converted to BSpline surface.

        :type: bool
        """
    @ConvertToroidalSurf.setter
    def ConvertToroidalSurf(self, arg1: bool) -> None:
        """
        Sets flag for define if toroidal surface converted to BSpline surface.
        """
    @property
    def GMaxDegree(self) -> int:
        """
        :type: int
        """
    @GMaxDegree.setter
    def GMaxDegree(self, arg1: int) -> None:
        pass
    @property
    def GMaxSeg(self) -> int:
        """
        :type: int
        """
    @GMaxSeg.setter
    def GMaxSeg(self, arg1: int) -> None:
        pass
    @property
    def SegmentSurfaceMode(self) -> bool:
        """
        Sets Segment mode for surface. If Segment is True surface is approximated in the bondaries of face lying on this surface.

        :type: bool
        """
    @SegmentSurfaceMode.setter
    def SegmentSurfaceMode(self, arg1: bool) -> None:
        """
        Sets Segment mode for surface. If Segment is True surface is approximated in the bondaries of face lying on this surface.
        """
    pass
class ShapeCustom_Surface():
    """
    Converts a surface to the analitical form with given precision. Conversion is done only the surface is bspline of bezier and this can be approximed by some analytical surface with that precision.
    """
    def ConvertToAnalytical(self,tol : float,substitute : bool) -> OCP.Geom.Geom_Surface: 
        """
        Tries to convert the Surface to an Analytic form Returns the result Works only if the Surface is BSpline or Bezier. Else, or in case of failure, returns a Null Handle
        """
    def ConvertToPeriodic(self,substitute : bool,preci : float=-1.0) -> OCP.Geom.Geom_Surface: 
        """
        Tries to convert the Surface to the Periodic form Returns the resulting surface Works only if the Surface is BSpline and is closed with Precision::Confusion() Else, or in case of failure, returns a Null Handle
        """
    def Gap(self) -> float: 
        """
        Returns maximal deviation of converted surface from the original one computed by last call to ConvertToAnalytical

        Returns maximal deviation of converted surface from the original one computed by last call to ConvertToAnalytical
        """
    def Init(self,S : OCP.Geom.Geom_Surface) -> None: 
        """
        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,S : OCP.Geom.Geom_Surface) -> None: ...
    pass
class ShapeCustom_SweptToElementary(ShapeCustom_Modification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.implements a modification for the BRepTools Modifier algortihm. Converts all elementary surfaces into surfaces of revolution.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def MsgRegistrator(self) -> OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator: 
        """
        Returns message registrator
        """
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has been modified. In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <C>, <L>, <Tol> are not significant.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Returns Standard_True if the edge <E> has a new curve on surface on the face <F>.In this case, <C> is the new geometric support of the edge, <L> the new location, <Tol> the new tolerance.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Returns Standard_True if the Vertex <V> has a new parameter on the edge <E>. In this case, <P> is the parameter, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Returns Standard_True if the vertex <V> has been modified. In this case, <P> is the new geometric support of the vertex, <Tol> the new tolerance. Otherwise, returns Standard_False, and <P>, <Tol> are not significant.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Returns Standard_True if the face <F> has been modified. In this case, <S> is the new geometric support of the face, <L> the new location, <Tol> the new tolerance. Otherwise, returns Standard_False, and <S>, <L>, <Tol> are not significant.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def SendMsg(self,shape : OCP.TopoDS.TopoDS_Shape,message : OCP.Message.Message_Msg,gravity : OCP.Message.Message_Gravity=Message_Gravity.Message_Info) -> None: 
        """
        Sends a message to be attached to the shape. Calls corresponding message of message registrator.
        """
    def SetMsgRegistrator(self,msgreg : OCP.ShapeExtend.ShapeExtend_BasicMsgRegistrator) -> None: 
        """
        Sets message registrator
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
class ShapeCustom_TrsfModification(OCP.BRepTools.BRepTools_TrsfModification, OCP.BRepTools.BRepTools_Modification, OCP.Standard.Standard_Transient):
    """
    Complements BRepTools_TrsfModification to provide reversible scaling regarding tolerances. Uses actual tolerances (attached to the shapes) not ones returned by BRep_Tool::Tolerance to work with tolerances lower than Precision::Confusion.Complements BRepTools_TrsfModification to provide reversible scaling regarding tolerances. Uses actual tolerances (attached to the shapes) not ones returned by BRep_Tool::Tolerance to work with tolerances lower than Precision::Confusion.Complements BRepTools_TrsfModification to provide reversible scaling regarding tolerances. Uses actual tolerances (attached to the shapes) not ones returned by BRep_Tool::Tolerance to work with tolerances lower than Precision::Confusion.
    """
    def Continuity(self,E : OCP.TopoDS.TopoDS_Edge,F1 : OCP.TopoDS.TopoDS_Face,F2 : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF1 : OCP.TopoDS.TopoDS_Face,NewF2 : OCP.TopoDS.TopoDS_Face) -> OCP.GeomAbs.GeomAbs_Shape: 
        """
        Returns the continuity of <NewE> between <NewF1> and <NewF2>.
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
    def NewCurve(self,E : OCP.TopoDS.TopoDS_Edge,C : OCP.Geom.Geom_Curve,L : OCP.TopLoc.TopLoc_Location,Tol : float) -> bool: 
        """
        Calls inherited method. Sets <Tol> as actual tolerance of <E> multiplied with scale factor.
        """
    def NewCurve2d(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,NewE : OCP.TopoDS.TopoDS_Edge,NewF : OCP.TopoDS.TopoDS_Face,C : OCP.Geom2d.Geom2d_Curve,Tol : float) -> bool: 
        """
        Calls inherited method. Sets <Tol> as actual tolerance of <E> multiplied with scale factor.
        """
    def NewParameter(self,V : OCP.TopoDS.TopoDS_Vertex,E : OCP.TopoDS.TopoDS_Edge,P : float,Tol : float) -> bool: 
        """
        Calls inherited method. Sets <Tol> as actual tolerance of <V> multiplied with scale factor.
        """
    def NewPoint(self,V : OCP.TopoDS.TopoDS_Vertex,P : OCP.gp.gp_Pnt,Tol : float) -> bool: 
        """
        Calls inherited method. Sets <Tol> as actual tolerance of <V> multiplied with scale factor.
        """
    def NewPolygon(self,E : OCP.TopoDS.TopoDS_Edge,P : OCP.Poly.Poly_Polygon3D) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon. If the edge has been modified: - P is a new polygon
        """
    def NewPolygonOnTriangulation(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face,P : OCP.Poly.Poly_PolygonOnTriangulation) -> bool: 
        """
        Returns true if the edge has been modified according to changed polygon on triangulation. If the edge has been modified: - P is a new polygon on triangulation
        """
    def NewSurface(self,F : OCP.TopoDS.TopoDS_Face,S : OCP.Geom.Geom_Surface,L : OCP.TopLoc.TopLoc_Location,Tol : float,RevWires : bool,RevFace : bool) -> bool: 
        """
        Calls inherited method. Sets <Tol> as actual tolerance of <F> multiplied with scale factor.
        """
    def NewTriangulation(self,F : OCP.TopoDS.TopoDS_Face,T : OCP.Poly.Poly_Triangulation) -> bool: 
        """
        Returns true if the face has been modified according to changed triangulation. If the face has been modified: - T is a new triangulation on the face
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Trsf(self) -> OCP.gp.gp_Trsf: 
        """
        Provides access to the gp_Trsf associated with this modification. The transformation can be changed.
        """
    def __init__(self,T : OCP.gp.gp_Trsf) -> None: ...
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
