import OCP.Quantity
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import io
import OCP.gp
import OCP.Graphic3d
import OCP.Standard
import OCP.TCollection
__all__  = [
"Quantity_Array1OfColor",
"Quantity_Array2OfColor",
"Quantity_Color",
"Quantity_ColorHasher",
"Quantity_ColorRGBA",
"Quantity_ColorRGBAHasher",
"Quantity_Date",
"Quantity_DateDefinitionError",
"Quantity_HArray1OfColor",
"Quantity_NameOfColor",
"Quantity_Period",
"Quantity_PeriodDefinitionError",
"Quantity_PhysicalQuantity",
"Quantity_TypeOfColor",
"Quantity_ABSORBEDDOSE",
"Quantity_ACCELERATION",
"Quantity_ACOUSTICINTENSITY",
"Quantity_ACTIVITY",
"Quantity_ADMITTANCE",
"Quantity_AMOUNTOFSUBSTANCE",
"Quantity_ANGULARVELOCITY",
"Quantity_AREA",
"Quantity_CAPACITANCE",
"Quantity_COEFFICIENTOFEXPANSION",
"Quantity_CONCENTRATION",
"Quantity_CONDUCTIVITY",
"Quantity_CONSUMPTION",
"Quantity_DENSITY",
"Quantity_DOSEEQUIVALENT",
"Quantity_ELECTRICCAPACITANCE",
"Quantity_ELECTRICCHARGE",
"Quantity_ELECTRICCURRENT",
"Quantity_ELECTRICFIELDSTRENGTH",
"Quantity_ELECTRICPOTENTIAL",
"Quantity_ENERGY",
"Quantity_ENTHALPY",
"Quantity_ENTROPY",
"Quantity_FORCE",
"Quantity_FREQUENCY",
"Quantity_ILLUMINANCE",
"Quantity_IMPEDANCE",
"Quantity_INDUCTANCE",
"Quantity_KINEMATICVISCOSITY",
"Quantity_KINETICMOMENT",
"Quantity_LENGTH",
"Quantity_LUMINANCE",
"Quantity_LUMINOUSEFFICACITY",
"Quantity_LUMINOUSEXPOSITION",
"Quantity_LUMINOUSFLUX",
"Quantity_LUMINOUSINTENSITY",
"Quantity_MAGNETICFIELDSTRENGTH",
"Quantity_MAGNETICFLUX",
"Quantity_MAGNETICFLUXDENSITY",
"Quantity_MASS",
"Quantity_MASSFLOW",
"Quantity_MOLARCONCENTRATION",
"Quantity_MOLARITY",
"Quantity_MOLARMASS",
"Quantity_MOLARVOLUME",
"Quantity_MOMENTOFAFORCE",
"Quantity_MOMENTOFINERTIA",
"Quantity_MOMENTUM",
"Quantity_NOC_ALICEBLUE",
"Quantity_NOC_ANTIQUEWHITE",
"Quantity_NOC_ANTIQUEWHITE1",
"Quantity_NOC_ANTIQUEWHITE2",
"Quantity_NOC_ANTIQUEWHITE3",
"Quantity_NOC_ANTIQUEWHITE4",
"Quantity_NOC_AQUAMARINE1",
"Quantity_NOC_AQUAMARINE2",
"Quantity_NOC_AQUAMARINE4",
"Quantity_NOC_AZURE",
"Quantity_NOC_AZURE2",
"Quantity_NOC_AZURE3",
"Quantity_NOC_AZURE4",
"Quantity_NOC_BEET",
"Quantity_NOC_BEIGE",
"Quantity_NOC_BISQUE",
"Quantity_NOC_BISQUE2",
"Quantity_NOC_BISQUE3",
"Quantity_NOC_BISQUE4",
"Quantity_NOC_BLACK",
"Quantity_NOC_BLANCHEDALMOND",
"Quantity_NOC_BLUE",
"Quantity_NOC_BLUE1",
"Quantity_NOC_BLUE2",
"Quantity_NOC_BLUE3",
"Quantity_NOC_BLUE4",
"Quantity_NOC_BLUEVIOLET",
"Quantity_NOC_BROWN",
"Quantity_NOC_BROWN1",
"Quantity_NOC_BROWN2",
"Quantity_NOC_BROWN3",
"Quantity_NOC_BROWN4",
"Quantity_NOC_BURLYWOOD",
"Quantity_NOC_BURLYWOOD1",
"Quantity_NOC_BURLYWOOD2",
"Quantity_NOC_BURLYWOOD3",
"Quantity_NOC_BURLYWOOD4",
"Quantity_NOC_CADETBLUE",
"Quantity_NOC_CADETBLUE1",
"Quantity_NOC_CADETBLUE2",
"Quantity_NOC_CADETBLUE3",
"Quantity_NOC_CADETBLUE4",
"Quantity_NOC_CHARTREUSE",
"Quantity_NOC_CHARTREUSE1",
"Quantity_NOC_CHARTREUSE2",
"Quantity_NOC_CHARTREUSE3",
"Quantity_NOC_CHARTREUSE4",
"Quantity_NOC_CHOCOLATE",
"Quantity_NOC_CHOCOLATE1",
"Quantity_NOC_CHOCOLATE2",
"Quantity_NOC_CHOCOLATE3",
"Quantity_NOC_CHOCOLATE4",
"Quantity_NOC_CORAL",
"Quantity_NOC_CORAL1",
"Quantity_NOC_CORAL2",
"Quantity_NOC_CORAL3",
"Quantity_NOC_CORAL4",
"Quantity_NOC_CORNFLOWERBLUE",
"Quantity_NOC_CORNSILK1",
"Quantity_NOC_CORNSILK2",
"Quantity_NOC_CORNSILK3",
"Quantity_NOC_CORNSILK4",
"Quantity_NOC_CYAN",
"Quantity_NOC_CYAN1",
"Quantity_NOC_CYAN2",
"Quantity_NOC_CYAN3",
"Quantity_NOC_CYAN4",
"Quantity_NOC_DARKGOLDENROD",
"Quantity_NOC_DARKGOLDENROD1",
"Quantity_NOC_DARKGOLDENROD2",
"Quantity_NOC_DARKGOLDENROD3",
"Quantity_NOC_DARKGOLDENROD4",
"Quantity_NOC_DARKGREEN",
"Quantity_NOC_DARKKHAKI",
"Quantity_NOC_DARKOLIVEGREEN",
"Quantity_NOC_DARKOLIVEGREEN1",
"Quantity_NOC_DARKOLIVEGREEN2",
"Quantity_NOC_DARKOLIVEGREEN3",
"Quantity_NOC_DARKOLIVEGREEN4",
"Quantity_NOC_DARKORANGE",
"Quantity_NOC_DARKORANGE1",
"Quantity_NOC_DARKORANGE2",
"Quantity_NOC_DARKORANGE3",
"Quantity_NOC_DARKORANGE4",
"Quantity_NOC_DARKORCHID",
"Quantity_NOC_DARKORCHID1",
"Quantity_NOC_DARKORCHID2",
"Quantity_NOC_DARKORCHID3",
"Quantity_NOC_DARKORCHID4",
"Quantity_NOC_DARKSALMON",
"Quantity_NOC_DARKSEAGREEN",
"Quantity_NOC_DARKSEAGREEN1",
"Quantity_NOC_DARKSEAGREEN2",
"Quantity_NOC_DARKSEAGREEN3",
"Quantity_NOC_DARKSEAGREEN4",
"Quantity_NOC_DARKSLATEBLUE",
"Quantity_NOC_DARKSLATEGRAY",
"Quantity_NOC_DARKSLATEGRAY1",
"Quantity_NOC_DARKSLATEGRAY2",
"Quantity_NOC_DARKSLATEGRAY3",
"Quantity_NOC_DARKSLATEGRAY4",
"Quantity_NOC_DARKTURQUOISE",
"Quantity_NOC_DARKVIOLET",
"Quantity_NOC_DEEPPINK",
"Quantity_NOC_DEEPPINK2",
"Quantity_NOC_DEEPPINK3",
"Quantity_NOC_DEEPPINK4",
"Quantity_NOC_DEEPSKYBLUE1",
"Quantity_NOC_DEEPSKYBLUE2",
"Quantity_NOC_DEEPSKYBLUE3",
"Quantity_NOC_DEEPSKYBLUE4",
"Quantity_NOC_DODGERBLUE1",
"Quantity_NOC_DODGERBLUE2",
"Quantity_NOC_DODGERBLUE3",
"Quantity_NOC_DODGERBLUE4",
"Quantity_NOC_FIREBRICK",
"Quantity_NOC_FIREBRICK1",
"Quantity_NOC_FIREBRICK2",
"Quantity_NOC_FIREBRICK3",
"Quantity_NOC_FIREBRICK4",
"Quantity_NOC_FLORALWHITE",
"Quantity_NOC_FORESTGREEN",
"Quantity_NOC_GAINSBORO",
"Quantity_NOC_GHOSTWHITE",
"Quantity_NOC_GOLD",
"Quantity_NOC_GOLD1",
"Quantity_NOC_GOLD2",
"Quantity_NOC_GOLD3",
"Quantity_NOC_GOLD4",
"Quantity_NOC_GOLDENROD",
"Quantity_NOC_GOLDENROD1",
"Quantity_NOC_GOLDENROD2",
"Quantity_NOC_GOLDENROD3",
"Quantity_NOC_GOLDENROD4",
"Quantity_NOC_GRAY",
"Quantity_NOC_GRAY0",
"Quantity_NOC_GRAY1",
"Quantity_NOC_GRAY10",
"Quantity_NOC_GRAY11",
"Quantity_NOC_GRAY12",
"Quantity_NOC_GRAY13",
"Quantity_NOC_GRAY14",
"Quantity_NOC_GRAY15",
"Quantity_NOC_GRAY16",
"Quantity_NOC_GRAY17",
"Quantity_NOC_GRAY18",
"Quantity_NOC_GRAY19",
"Quantity_NOC_GRAY2",
"Quantity_NOC_GRAY20",
"Quantity_NOC_GRAY21",
"Quantity_NOC_GRAY22",
"Quantity_NOC_GRAY23",
"Quantity_NOC_GRAY24",
"Quantity_NOC_GRAY25",
"Quantity_NOC_GRAY26",
"Quantity_NOC_GRAY27",
"Quantity_NOC_GRAY28",
"Quantity_NOC_GRAY29",
"Quantity_NOC_GRAY3",
"Quantity_NOC_GRAY30",
"Quantity_NOC_GRAY31",
"Quantity_NOC_GRAY32",
"Quantity_NOC_GRAY33",
"Quantity_NOC_GRAY34",
"Quantity_NOC_GRAY35",
"Quantity_NOC_GRAY36",
"Quantity_NOC_GRAY37",
"Quantity_NOC_GRAY38",
"Quantity_NOC_GRAY39",
"Quantity_NOC_GRAY4",
"Quantity_NOC_GRAY40",
"Quantity_NOC_GRAY41",
"Quantity_NOC_GRAY42",
"Quantity_NOC_GRAY43",
"Quantity_NOC_GRAY44",
"Quantity_NOC_GRAY45",
"Quantity_NOC_GRAY46",
"Quantity_NOC_GRAY47",
"Quantity_NOC_GRAY48",
"Quantity_NOC_GRAY49",
"Quantity_NOC_GRAY5",
"Quantity_NOC_GRAY50",
"Quantity_NOC_GRAY51",
"Quantity_NOC_GRAY52",
"Quantity_NOC_GRAY53",
"Quantity_NOC_GRAY54",
"Quantity_NOC_GRAY55",
"Quantity_NOC_GRAY56",
"Quantity_NOC_GRAY57",
"Quantity_NOC_GRAY58",
"Quantity_NOC_GRAY59",
"Quantity_NOC_GRAY6",
"Quantity_NOC_GRAY60",
"Quantity_NOC_GRAY61",
"Quantity_NOC_GRAY62",
"Quantity_NOC_GRAY63",
"Quantity_NOC_GRAY64",
"Quantity_NOC_GRAY65",
"Quantity_NOC_GRAY66",
"Quantity_NOC_GRAY67",
"Quantity_NOC_GRAY68",
"Quantity_NOC_GRAY69",
"Quantity_NOC_GRAY7",
"Quantity_NOC_GRAY70",
"Quantity_NOC_GRAY71",
"Quantity_NOC_GRAY72",
"Quantity_NOC_GRAY73",
"Quantity_NOC_GRAY74",
"Quantity_NOC_GRAY75",
"Quantity_NOC_GRAY76",
"Quantity_NOC_GRAY77",
"Quantity_NOC_GRAY78",
"Quantity_NOC_GRAY79",
"Quantity_NOC_GRAY8",
"Quantity_NOC_GRAY80",
"Quantity_NOC_GRAY81",
"Quantity_NOC_GRAY82",
"Quantity_NOC_GRAY83",
"Quantity_NOC_GRAY85",
"Quantity_NOC_GRAY86",
"Quantity_NOC_GRAY87",
"Quantity_NOC_GRAY88",
"Quantity_NOC_GRAY89",
"Quantity_NOC_GRAY9",
"Quantity_NOC_GRAY90",
"Quantity_NOC_GRAY91",
"Quantity_NOC_GRAY92",
"Quantity_NOC_GRAY93",
"Quantity_NOC_GRAY94",
"Quantity_NOC_GRAY95",
"Quantity_NOC_GRAY97",
"Quantity_NOC_GRAY98",
"Quantity_NOC_GRAY99",
"Quantity_NOC_GREEN",
"Quantity_NOC_GREEN1",
"Quantity_NOC_GREEN2",
"Quantity_NOC_GREEN3",
"Quantity_NOC_GREEN4",
"Quantity_NOC_GREENYELLOW",
"Quantity_NOC_HONEYDEW",
"Quantity_NOC_HONEYDEW2",
"Quantity_NOC_HONEYDEW3",
"Quantity_NOC_HONEYDEW4",
"Quantity_NOC_HOTPINK",
"Quantity_NOC_HOTPINK1",
"Quantity_NOC_HOTPINK2",
"Quantity_NOC_HOTPINK3",
"Quantity_NOC_HOTPINK4",
"Quantity_NOC_INDIANRED",
"Quantity_NOC_INDIANRED1",
"Quantity_NOC_INDIANRED2",
"Quantity_NOC_INDIANRED3",
"Quantity_NOC_INDIANRED4",
"Quantity_NOC_IVORY",
"Quantity_NOC_IVORY2",
"Quantity_NOC_IVORY3",
"Quantity_NOC_IVORY4",
"Quantity_NOC_KHAKI",
"Quantity_NOC_KHAKI1",
"Quantity_NOC_KHAKI2",
"Quantity_NOC_KHAKI3",
"Quantity_NOC_KHAKI4",
"Quantity_NOC_LAVENDER",
"Quantity_NOC_LAVENDERBLUSH1",
"Quantity_NOC_LAVENDERBLUSH2",
"Quantity_NOC_LAVENDERBLUSH3",
"Quantity_NOC_LAVENDERBLUSH4",
"Quantity_NOC_LAWNGREEN",
"Quantity_NOC_LEMONCHIFFON1",
"Quantity_NOC_LEMONCHIFFON2",
"Quantity_NOC_LEMONCHIFFON3",
"Quantity_NOC_LEMONCHIFFON4",
"Quantity_NOC_LIGHTBLUE",
"Quantity_NOC_LIGHTBLUE1",
"Quantity_NOC_LIGHTBLUE2",
"Quantity_NOC_LIGHTBLUE3",
"Quantity_NOC_LIGHTBLUE4",
"Quantity_NOC_LIGHTCORAL",
"Quantity_NOC_LIGHTCYAN",
"Quantity_NOC_LIGHTCYAN1",
"Quantity_NOC_LIGHTCYAN2",
"Quantity_NOC_LIGHTCYAN3",
"Quantity_NOC_LIGHTCYAN4",
"Quantity_NOC_LIGHTGOLDENROD",
"Quantity_NOC_LIGHTGOLDENROD1",
"Quantity_NOC_LIGHTGOLDENROD2",
"Quantity_NOC_LIGHTGOLDENROD3",
"Quantity_NOC_LIGHTGOLDENROD4",
"Quantity_NOC_LIGHTGOLDENRODYELLOW",
"Quantity_NOC_LIGHTGRAY",
"Quantity_NOC_LIGHTPINK",
"Quantity_NOC_LIGHTPINK1",
"Quantity_NOC_LIGHTPINK2",
"Quantity_NOC_LIGHTPINK3",
"Quantity_NOC_LIGHTPINK4",
"Quantity_NOC_LIGHTSALMON1",
"Quantity_NOC_LIGHTSALMON2",
"Quantity_NOC_LIGHTSALMON3",
"Quantity_NOC_LIGHTSALMON4",
"Quantity_NOC_LIGHTSEAGREEN",
"Quantity_NOC_LIGHTSKYBLUE",
"Quantity_NOC_LIGHTSKYBLUE1",
"Quantity_NOC_LIGHTSKYBLUE2",
"Quantity_NOC_LIGHTSKYBLUE3",
"Quantity_NOC_LIGHTSKYBLUE4",
"Quantity_NOC_LIGHTSLATEBLUE",
"Quantity_NOC_LIGHTSLATEGRAY",
"Quantity_NOC_LIGHTSTEELBLUE",
"Quantity_NOC_LIGHTSTEELBLUE1",
"Quantity_NOC_LIGHTSTEELBLUE2",
"Quantity_NOC_LIGHTSTEELBLUE3",
"Quantity_NOC_LIGHTSTEELBLUE4",
"Quantity_NOC_LIGHTYELLOW",
"Quantity_NOC_LIGHTYELLOW2",
"Quantity_NOC_LIGHTYELLOW3",
"Quantity_NOC_LIGHTYELLOW4",
"Quantity_NOC_LIMEGREEN",
"Quantity_NOC_LINEN",
"Quantity_NOC_MAGENTA",
"Quantity_NOC_MAGENTA1",
"Quantity_NOC_MAGENTA2",
"Quantity_NOC_MAGENTA3",
"Quantity_NOC_MAGENTA4",
"Quantity_NOC_MAROON",
"Quantity_NOC_MAROON1",
"Quantity_NOC_MAROON2",
"Quantity_NOC_MAROON3",
"Quantity_NOC_MAROON4",
"Quantity_NOC_MATRABLUE",
"Quantity_NOC_MATRAGRAY",
"Quantity_NOC_MEDIUMAQUAMARINE",
"Quantity_NOC_MEDIUMORCHID",
"Quantity_NOC_MEDIUMORCHID1",
"Quantity_NOC_MEDIUMORCHID2",
"Quantity_NOC_MEDIUMORCHID3",
"Quantity_NOC_MEDIUMORCHID4",
"Quantity_NOC_MEDIUMPURPLE",
"Quantity_NOC_MEDIUMPURPLE1",
"Quantity_NOC_MEDIUMPURPLE2",
"Quantity_NOC_MEDIUMPURPLE3",
"Quantity_NOC_MEDIUMPURPLE4",
"Quantity_NOC_MEDIUMSEAGREEN",
"Quantity_NOC_MEDIUMSLATEBLUE",
"Quantity_NOC_MEDIUMSPRINGGREEN",
"Quantity_NOC_MEDIUMTURQUOISE",
"Quantity_NOC_MEDIUMVIOLETRED",
"Quantity_NOC_MIDNIGHTBLUE",
"Quantity_NOC_MINTCREAM",
"Quantity_NOC_MISTYROSE",
"Quantity_NOC_MISTYROSE2",
"Quantity_NOC_MISTYROSE3",
"Quantity_NOC_MISTYROSE4",
"Quantity_NOC_MOCCASIN",
"Quantity_NOC_NAVAJOWHITE1",
"Quantity_NOC_NAVAJOWHITE2",
"Quantity_NOC_NAVAJOWHITE3",
"Quantity_NOC_NAVAJOWHITE4",
"Quantity_NOC_NAVYBLUE",
"Quantity_NOC_OLDLACE",
"Quantity_NOC_OLIVEDRAB",
"Quantity_NOC_OLIVEDRAB1",
"Quantity_NOC_OLIVEDRAB2",
"Quantity_NOC_OLIVEDRAB3",
"Quantity_NOC_OLIVEDRAB4",
"Quantity_NOC_ORANGE",
"Quantity_NOC_ORANGE1",
"Quantity_NOC_ORANGE2",
"Quantity_NOC_ORANGE3",
"Quantity_NOC_ORANGE4",
"Quantity_NOC_ORANGERED",
"Quantity_NOC_ORANGERED1",
"Quantity_NOC_ORANGERED2",
"Quantity_NOC_ORANGERED3",
"Quantity_NOC_ORANGERED4",
"Quantity_NOC_ORCHID",
"Quantity_NOC_ORCHID1",
"Quantity_NOC_ORCHID2",
"Quantity_NOC_ORCHID3",
"Quantity_NOC_ORCHID4",
"Quantity_NOC_PALEGOLDENROD",
"Quantity_NOC_PALEGREEN",
"Quantity_NOC_PALEGREEN1",
"Quantity_NOC_PALEGREEN2",
"Quantity_NOC_PALEGREEN3",
"Quantity_NOC_PALEGREEN4",
"Quantity_NOC_PALETURQUOISE",
"Quantity_NOC_PALETURQUOISE1",
"Quantity_NOC_PALETURQUOISE2",
"Quantity_NOC_PALETURQUOISE3",
"Quantity_NOC_PALETURQUOISE4",
"Quantity_NOC_PALEVIOLETRED",
"Quantity_NOC_PALEVIOLETRED1",
"Quantity_NOC_PALEVIOLETRED2",
"Quantity_NOC_PALEVIOLETRED3",
"Quantity_NOC_PALEVIOLETRED4",
"Quantity_NOC_PAPAYAWHIP",
"Quantity_NOC_PEACHPUFF",
"Quantity_NOC_PEACHPUFF2",
"Quantity_NOC_PEACHPUFF3",
"Quantity_NOC_PEACHPUFF4",
"Quantity_NOC_PERU",
"Quantity_NOC_PINK",
"Quantity_NOC_PINK1",
"Quantity_NOC_PINK2",
"Quantity_NOC_PINK3",
"Quantity_NOC_PINK4",
"Quantity_NOC_PLUM",
"Quantity_NOC_PLUM1",
"Quantity_NOC_PLUM2",
"Quantity_NOC_PLUM3",
"Quantity_NOC_PLUM4",
"Quantity_NOC_POWDERBLUE",
"Quantity_NOC_PURPLE",
"Quantity_NOC_PURPLE1",
"Quantity_NOC_PURPLE2",
"Quantity_NOC_PURPLE3",
"Quantity_NOC_PURPLE4",
"Quantity_NOC_RED",
"Quantity_NOC_RED1",
"Quantity_NOC_RED2",
"Quantity_NOC_RED3",
"Quantity_NOC_RED4",
"Quantity_NOC_ROSYBROWN",
"Quantity_NOC_ROSYBROWN1",
"Quantity_NOC_ROSYBROWN2",
"Quantity_NOC_ROSYBROWN3",
"Quantity_NOC_ROSYBROWN4",
"Quantity_NOC_ROYALBLUE",
"Quantity_NOC_ROYALBLUE1",
"Quantity_NOC_ROYALBLUE2",
"Quantity_NOC_ROYALBLUE3",
"Quantity_NOC_ROYALBLUE4",
"Quantity_NOC_SADDLEBROWN",
"Quantity_NOC_SALMON",
"Quantity_NOC_SALMON1",
"Quantity_NOC_SALMON2",
"Quantity_NOC_SALMON3",
"Quantity_NOC_SALMON4",
"Quantity_NOC_SANDYBROWN",
"Quantity_NOC_SEAGREEN",
"Quantity_NOC_SEAGREEN1",
"Quantity_NOC_SEAGREEN2",
"Quantity_NOC_SEAGREEN3",
"Quantity_NOC_SEAGREEN4",
"Quantity_NOC_SEASHELL",
"Quantity_NOC_SEASHELL2",
"Quantity_NOC_SEASHELL3",
"Quantity_NOC_SEASHELL4",
"Quantity_NOC_SIENNA",
"Quantity_NOC_SIENNA1",
"Quantity_NOC_SIENNA2",
"Quantity_NOC_SIENNA3",
"Quantity_NOC_SIENNA4",
"Quantity_NOC_SKYBLUE",
"Quantity_NOC_SKYBLUE1",
"Quantity_NOC_SKYBLUE2",
"Quantity_NOC_SKYBLUE3",
"Quantity_NOC_SKYBLUE4",
"Quantity_NOC_SLATEBLUE",
"Quantity_NOC_SLATEBLUE1",
"Quantity_NOC_SLATEBLUE2",
"Quantity_NOC_SLATEBLUE3",
"Quantity_NOC_SLATEBLUE4",
"Quantity_NOC_SLATEGRAY",
"Quantity_NOC_SLATEGRAY1",
"Quantity_NOC_SLATEGRAY2",
"Quantity_NOC_SLATEGRAY3",
"Quantity_NOC_SLATEGRAY4",
"Quantity_NOC_SNOW",
"Quantity_NOC_SNOW2",
"Quantity_NOC_SNOW3",
"Quantity_NOC_SNOW4",
"Quantity_NOC_SPRINGGREEN",
"Quantity_NOC_SPRINGGREEN2",
"Quantity_NOC_SPRINGGREEN3",
"Quantity_NOC_SPRINGGREEN4",
"Quantity_NOC_STEELBLUE",
"Quantity_NOC_STEELBLUE1",
"Quantity_NOC_STEELBLUE2",
"Quantity_NOC_STEELBLUE3",
"Quantity_NOC_STEELBLUE4",
"Quantity_NOC_TAN",
"Quantity_NOC_TAN1",
"Quantity_NOC_TAN2",
"Quantity_NOC_TAN3",
"Quantity_NOC_TAN4",
"Quantity_NOC_TEAL",
"Quantity_NOC_THISTLE",
"Quantity_NOC_THISTLE1",
"Quantity_NOC_THISTLE2",
"Quantity_NOC_THISTLE3",
"Quantity_NOC_THISTLE4",
"Quantity_NOC_TOMATO",
"Quantity_NOC_TOMATO1",
"Quantity_NOC_TOMATO2",
"Quantity_NOC_TOMATO3",
"Quantity_NOC_TOMATO4",
"Quantity_NOC_TURQUOISE",
"Quantity_NOC_TURQUOISE1",
"Quantity_NOC_TURQUOISE2",
"Quantity_NOC_TURQUOISE3",
"Quantity_NOC_TURQUOISE4",
"Quantity_NOC_VIOLET",
"Quantity_NOC_VIOLETRED",
"Quantity_NOC_VIOLETRED1",
"Quantity_NOC_VIOLETRED2",
"Quantity_NOC_VIOLETRED3",
"Quantity_NOC_VIOLETRED4",
"Quantity_NOC_WHEAT",
"Quantity_NOC_WHEAT1",
"Quantity_NOC_WHEAT2",
"Quantity_NOC_WHEAT3",
"Quantity_NOC_WHEAT4",
"Quantity_NOC_WHITE",
"Quantity_NOC_WHITESMOKE",
"Quantity_NOC_YELLOW",
"Quantity_NOC_YELLOW1",
"Quantity_NOC_YELLOW2",
"Quantity_NOC_YELLOW3",
"Quantity_NOC_YELLOW4",
"Quantity_NOC_YELLOWGREEN",
"Quantity_PLANEANGLE",
"Quantity_POWER",
"Quantity_PRESSURE",
"Quantity_RELUCTANCE",
"Quantity_RESISTANCE",
"Quantity_RESISTIVITY",
"Quantity_SOLIDANGLE",
"Quantity_SOUNDINTENSITY",
"Quantity_SPECIFICHEATCAPACITY",
"Quantity_SPEED",
"Quantity_SURFACETENSION",
"Quantity_TEMPERATURE",
"Quantity_THERMALCONDUCTIVITY",
"Quantity_TOC_CIELab",
"Quantity_TOC_CIELch",
"Quantity_TOC_HLS",
"Quantity_TOC_RGB",
"Quantity_TOC_sRGB",
"Quantity_TORQUE",
"Quantity_VELOCITY",
"Quantity_VISCOSITY",
"Quantity_VOLUME",
"Quantity_VOLUMEFLOW",
"Quantity_WEIGHT",
"Quantity_WORK"
]
class Quantity_Array1OfColor():
    """
    The class NCollection_Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : Quantity_Array1OfColor) -> Quantity_Array1OfColor: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> Quantity_Color: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Quantity_Color: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Quantity_Color: 
        """
        Variable value access
        """
    def First(self) -> Quantity_Color: 
        """
        Returns first element
        """
    def Init(self,theValue : Quantity_Color) -> None: 
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
    def Last(self) -> Quantity_Color: 
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
    def Move(self,theOther : Quantity_Array1OfColor) -> Quantity_Array1OfColor: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Quantity_Color) -> None: 
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
    def Value(self,theIndex : int) -> Quantity_Color: 
        """
        Constant value access
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Quantity_Color,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Quantity_Array1OfColor) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
class Quantity_Array2OfColor():
    """
    Purpose: The class Array2 represents bi-dimensional arrays of fixed size known at run time. The ranges of indices are user defined.
    """
    def Assign(self,theOther : Quantity_Array2OfColor) -> Quantity_Array2OfColor: 
        """
        Assignment
        """
    def ChangeValue(self,theRow : int,theCol : int) -> Quantity_Color: 
        """
        Variable value access
        """
    def ColLength(self) -> int: 
        """
        Returns length of the column, i.e. number of rows
        """
    def Init(self,theValue : Quantity_Color) -> None: 
        """
        Initialise the values
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def Length(self) -> int: ...
    def LowerCol(self) -> int: 
        """
        LowerCol
        """
    def LowerRow(self) -> int: 
        """
        LowerRow
        """
    def Move(self,theOther : Quantity_Array2OfColor) -> Quantity_Array2OfColor: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will be left uninitialized and should not be used anymore.
        """
    def NbColumns(self) -> int: 
        """
        Returns number of columns
        """
    def NbRows(self) -> int: 
        """
        Returns number of rows
        """
    def Resize(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def RowLength(self) -> int: 
        """
        Returns length of the row, i.e. number of columns
        """
    def SetValue(self,theRow : int,theCol : int,theItem : Quantity_Color) -> None: 
        """
        SetValue
        """
    def Size(self) -> int: ...
    def UpperCol(self) -> int: 
        """
        UpperCol
        """
    def UpperRow(self) -> int: 
        """
        UpperRow
        """
    def Value(self,theRow : int,theCol : int) -> Quantity_Color: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : Quantity_Color,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Quantity_Array2OfColor) -> None: ...
    pass
class Quantity_Color():
    """
    This class allows the definition of an RGB color as triplet of 3 normalized floating point values (red, green, blue).
    """
    @staticmethod
    def Argb2color_s(theARGB : int,theColor : Quantity_Color) -> None: 
        """
        Convert integer ARGB value to Color. Alpha bits are ignored. Note that this packing does NOT involve linear -> non-linear sRGB conversion, as would be usually expected to preserve higher (for human eye) color precision in 4 bytes.
        """
    def Blue(self) -> float: 
        """
        Returns the Blue component (quantity of blue) of the color within range [0.0; 1.0].
        """
    def ChangeContrast(self,theDelta : float) -> None: 
        """
        Increases or decreases the contrast (variation of the saturation). The delta is a percentage. Any value greater than zero will increase the contrast. The variation is expressed as a percentage of the current value.
        """
    def ChangeIntensity(self,theDelta : float) -> None: 
        """
        Increases or decreases the intensity (variation of the lightness). The delta is a percentage. Any value greater than zero will increase the intensity. The variation is expressed as a percentage of the current value.
        """
    @staticmethod
    def Color2argb_s(theColor : Quantity_Color) -> Tuple[int]: 
        """
        Convert the color value to ARGB integer value, with alpha equals to 0. So the output is formatted as 0x00RRGGBB. Note that this unpacking does NOT involve non-linear sRGB -> linear RGB conversion, as would be usually expected for RGB color packed into 4 bytes.
        """
    @staticmethod
    def ColorFromHex_s(theHexColorString : str,theColor : Quantity_Color) -> bool: 
        """
        Parses the string as a hex color (like "#FF0" for short sRGB color, or "#FFFF00" for sRGB color)
        """
    @staticmethod
    @overload
    def ColorFromName_s(theName : str,theColor : Quantity_NameOfColor) -> bool: 
        """
        Finds color from predefined names. For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK. Returns FALSE if name is unknown.

        Finds color from predefined names.
        """
    @staticmethod
    @overload
    def ColorFromName_s(theColorNameString : str,theColor : Quantity_Color) -> bool: ...
    @staticmethod
    def ColorToHex_s(theColor : Quantity_Color,theToPrefixHash : bool=True) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns hex sRGB string in format "#FFAAFF".
        """
    @staticmethod
    def Convert_HLS_To_LinearRGB_s(theHls : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts HLS components into linear RGB ones.
        """
    @staticmethod
    def Convert_HLS_To_sRGB_s(theHls : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts HLS components into RGB ones.
        """
    @staticmethod
    def Convert_Lab_To_Lch_s(theLab : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts CIE Lab components into CIE Lch ones.
        """
    @staticmethod
    def Convert_Lab_To_LinearRGB_s(theLab : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts CIE Lab components into linear RGB ones. Note that the resulting values may be out of the valid range for RGB.
        """
    @staticmethod
    def Convert_Lch_To_Lab_s(theLch : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts CIE Lch components into CIE Lab ones.
        """
    @staticmethod
    def Convert_LinearRGB_To_HLS_s(theRgb : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts Linear RGB components into HLS ones.
        """
    @staticmethod
    def Convert_LinearRGB_To_Lab_s(theRgb : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts linear RGB components into CIE Lab ones.
        """
    @staticmethod
    @overload
    def Convert_LinearRGB_To_sRGB_approx22_s(theRGB : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Convert linear RGB component into sRGB using approximated uniform gamma coefficient 2.2.

        Convert linear RGB components into sRGB using approximated uniform gamma coefficient 2.2
        """
    @staticmethod
    @overload
    def Convert_LinearRGB_To_sRGB_approx22_s(theLinearValue : float) -> float: ...
    @staticmethod
    def Convert_LinearRGB_To_sRGB_s(theLinearValue : float) -> float: 
        """
        Convert linear RGB component into sRGB using OpenGL specs formula (double precision), also known as gamma correction.

        Convert linear RGB component into sRGB using OpenGL specs formula (single precision), also known as gamma correction.
        """
    @staticmethod
    def Convert_sRGB_To_HLS_s(theRgb : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: 
        """
        Converts sRGB components into HLS ones.
        """
    @staticmethod
    @overload
    def Convert_sRGB_To_LinearRGB_approx22_s(thesRGBValue : float) -> float: 
        """
        Convert sRGB component into linear RGB using approximated uniform gamma coefficient 2.2

        Convert sRGB components into linear RGB using approximated uniform gamma coefficient 2.2
        """
    @staticmethod
    @overload
    def Convert_sRGB_To_LinearRGB_approx22_s(theRGB : OCP.gp.gp_Vec3f) -> OCP.gp.gp_Vec3f: ...
    @staticmethod
    def Convert_sRGB_To_LinearRGB_s(thesRGBValue : float) -> float: 
        """
        Convert sRGB component into linear RGB using OpenGL specs formula (double precision), also known as gamma correction.

        Convert sRGB component into linear RGB using OpenGL specs formula (single precision), also known as gamma correction.
        """
    def Delta(self,theColor : Quantity_Color) -> Tuple[float, float]: 
        """
        Returns the percentage change of contrast and intensity between this and another color. <DC> and <DI> are percentages, either positive or negative. The calculation is with respect to this color. If <DC> is positive then <me> is more contrasty. If <DI> is positive then <me> is more intense.
        """
    def DeltaE2000(self,theOther : Quantity_Color) -> float: 
        """
        Returns the value of the perceptual difference between this color and theOther, computed using the CIEDE2000 formula. The difference is in range [0, 100.], with 1 approximately corresponding to the minimal percievable difference (usually difference 5 or greater is needed for the difference to be recognizable in practice).
        """
    def Distance(self,theColor : Quantity_Color) -> float: 
        """
        Returns the distance between two colors. It's a value between 0 and the square root of 3 (the black/white distance).
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @staticmethod
    def Epsilon_s() -> float: 
        """
        Returns the value used to compare two colors for equality; 0.0001 by default.
        """
    def Green(self) -> float: 
        """
        Returns the Green component (quantity of green) of the color within range [0.0; 1.0].
        """
    @staticmethod
    def HlsRgb_s(theH : float,theL : float,theS : float) -> Tuple[float, float, float]: 
        """
        Converts HLS components into sRGB ones.
        """
    def Hue(self) -> float: 
        """
        Returns the Hue component (hue angle) of the color in degrees within range [0.0; 360.0], 0.0 being Red. -1.0 is a special value reserved for grayscale color (S should be 0.0)
        """
    def InitFromJson(self,theSStream : Any,theStreamPos : int) -> bool: 
        """
        Inits the content of me from the stream
        """
    def IsDifferent(self,theOther : Quantity_Color) -> bool: 
        """
        Returns TRUE if the distance between two colors is greater than Epsilon().
        """
    def IsEqual(self,theOther : Quantity_Color) -> bool: 
        """
        Returns TRUE if the distance between two colors is no greater than Epsilon().
        """
    def Light(self) -> float: 
        """
        Returns the Light component (value of the lightness) of the color within range [0.0; 1.0].
        """
    def Name(self) -> Quantity_NameOfColor: 
        """
        Returns the name of the nearest color from the Quantity_NameOfColor enumeration.
        """
    @staticmethod
    def Name_s(theR : float,theG : float,theB : float) -> Quantity_NameOfColor: 
        """
        Returns the color from Quantity_NameOfColor enumeration nearest to specified RGB values.
        """
    def Red(self) -> float: 
        """
        Returns the Red component (quantity of red) of the color within range [0.0; 1.0].
        """
    def Rgb(self) -> OCP.gp.gp_Vec3f: 
        """
        Return the color as vector of 3 float elements.
        """
    @staticmethod
    def RgbHls_s(theR : float,theG : float,theB : float) -> Tuple[float, float, float]: 
        """
        Converts sRGB components into HLS ones.
        """
    def Saturation(self) -> float: 
        """
        Returns the Saturation component (value of the saturation) of the color within range [0.0; 1.0].
        """
    @staticmethod
    def SetEpsilon_s(theEpsilon : float) -> None: 
        """
        Set the value used to compare two colors for equality.
        """
    @overload
    def SetValues(self,theName : Quantity_NameOfColor) -> None: 
        """
        Updates the color from specified named color.

        Updates a color according to the mode specified by theType. Throws exception if values are out of range.
        """
    @overload
    def SetValues(self,theC1 : float,theC2 : float,theC3 : float,theType : Quantity_TypeOfColor) -> None: ...
    def SquareDistance(self,theColor : Quantity_Color) -> float: 
        """
        Returns the square of distance between two colors.
        """
    @staticmethod
    def StringName_s(theColor : Quantity_NameOfColor) -> str: 
        """
        Returns the name of the color identified by the given Quantity_NameOfColor enumeration value.
        """
    def Values(self,theType : Quantity_TypeOfColor) -> Tuple[float, float, float]: 
        """
        Returns in theC1, theC2 and theC3 the components of this color according to the color system definition theType.
        """
    @overload
    def __init__(self,theRgb : OCP.gp.gp_Vec3f) -> None: ...
    @overload
    def __init__(self,theC1 : float,theC2 : float,theC3 : float,theType : Quantity_TypeOfColor) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theName : Quantity_NameOfColor) -> None: ...
    pass
class Quantity_ColorHasher():
    """
    Hasher of Quantity_Color.
    """
    @staticmethod
    def HashCode_s(theColor : Quantity_Color,theUpperBound : int) -> int: 
        """
        Returns hash code for the given RGB color, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theColor1 : Quantity_Color,theColor2 : Quantity_Color) -> bool: 
        """
        Returns true if two colors are equal.
        """
    def __init__(self) -> None: ...
    pass
class Quantity_ColorRGBA():
    """
    The pair of Quantity_Color and Alpha component (1.0 opaque, 0.0 transparent).
    """
    def Alpha(self) -> float: 
        """
        Return alpha value (1.0 means opaque, 0.0 means fully transparent).
        """
    def ChangeRGB(self) -> Quantity_Color: 
        """
        Modify RGB color components without affecting alpha value.
        """
    @staticmethod
    def ColorFromHex_s(theHexColorString : str,theColor : Quantity_ColorRGBA,theAlphaComponentIsOff : bool=False) -> bool: 
        """
        Parses the string as a hex color (like "#FF0" for short sRGB color, "#FF0F" for short sRGBA color, "#FFFF00" for RGB color, or "#FFFF00FF" for RGBA color)
        """
    @staticmethod
    def ColorFromName_s(theColorNameString : str,theColor : Quantity_ColorRGBA) -> bool: 
        """
        Finds color from predefined names. For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK. An alpha component is set to 1.0.
        """
    @staticmethod
    def ColorToHex_s(theColor : Quantity_ColorRGBA,theToPrefixHash : bool=True) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns hex sRGBA string in format "#RRGGBBAA".
        """
    @staticmethod
    def Convert_LinearRGB_To_sRGB_s(theRGB : OCP.Graphic3d.Graphic3d_Vec4) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Convert linear RGB components into sRGB using OpenGL specs formula.
        """
    @staticmethod
    def Convert_sRGB_To_LinearRGB_s(theRGB : OCP.Graphic3d.Graphic3d_Vec4) -> OCP.Graphic3d.Graphic3d_Vec4: 
        """
        Convert sRGB components into linear RGB using OpenGL specs formula.
        """
    def DumpJson(self,theOStream : io.BytesIO,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetRGB(self) -> Quantity_Color: 
        """
        Return RGB color value.
        """
    def InitFromJson(self,theSStream : Any,theStreamPos : int) -> bool: 
        """
        Inits the content of me from the stream
        """
    def IsDifferent(self,theOther : Quantity_ColorRGBA) -> bool: 
        """
        Returns true if the distance between colors is greater than Epsilon().
        """
    def IsEqual(self,theOther : Quantity_ColorRGBA) -> bool: 
        """
        Two colors are considered to be equal if their distance is no greater than Epsilon().
        """
    def SetAlpha(self,theAlpha : float) -> None: 
        """
        Assign the alpha value.
        """
    def SetRGB(self,theRgb : Quantity_Color) -> None: 
        """
        Assign RGB color components without affecting alpha value.
        """
    def SetValues(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: 
        """
        Assign new values to the color.
        """
    @overload
    def __init__(self,theRgb : Quantity_Color) -> None: ...
    @overload
    def __init__(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRgb : Quantity_Color,theAlpha : float) -> None: ...
    @overload
    def __init__(self,theRgba : OCP.Graphic3d.Graphic3d_Vec4) -> None: ...
    pass
class Quantity_ColorRGBAHasher():
    """
    Hasher of Quantity_ColorRGBA.
    """
    @staticmethod
    def HashCode_s(theColor : Quantity_ColorRGBA,theUpperBound : int) -> int: 
        """
        Returns hash code for the given RGBA color, in the range [1, theUpperBound]
        """
    @staticmethod
    def IsEqual_s(theColor1 : Quantity_ColorRGBA,theColor2 : Quantity_ColorRGBA) -> bool: 
        """
        Returns true if two colors are equal.
        """
    def __init__(self) -> None: ...
    pass
class Quantity_Date():
    """
    This class provides services to manage date information. A date represents the following time intervals: year, month, day, hour, minute, second, millisecond and microsecond. Current time is expressed in elapsed seconds and microseconds beginning from 00:00 GMT, January 1, 1979 (zero hour). The valid date can only be later than this one. Note: a Period object gives the interval between two dates.
    """
    def Add(self,aPeriod : Quantity_Period) -> Quantity_Date: 
        """
        Adds a Period to a Date and returns the new Date.
        """
    def Day(self) -> int: 
        """
        Returns Day of a Date.
        """
    def Difference(self,anOther : Quantity_Date) -> Quantity_Period: 
        """
        Subtracts one Date from another one to find the period between and returns the value. The result is the absolute value between the difference of two dates.
        """
    def Hour(self) -> int: 
        """
        Returns Hour of a Date.
        """
    def IsEarlier(self,anOther : Quantity_Date) -> bool: 
        """
        Returns TRUE if <me> is earlier than <other>.
        """
    def IsEqual(self,anOther : Quantity_Date) -> bool: 
        """
        Returns TRUE if both <me> and <other> are equal. This method is an alias of operator ==.
        """
    def IsLater(self,anOther : Quantity_Date) -> bool: 
        """
        Returns TRUE if <me> is later then <other>.
        """
    @staticmethod
    def IsLeap_s(yy : int) -> bool: 
        """
        Returns true if a year is a leap year. The leap years are divisible by 4 and not by 100 except the years divisible by 400.
        """
    @staticmethod
    def IsValid_s(mm : int,dd : int,yy : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> bool: 
        """
        Checks the validity of a date - returns true if a date defined from the year yyyy, the month mm, the day dd, the hour hh, the minute mn, the second ss, the millisecond mis (defaulted to 0) and the microsecond mics (defaulted to 0) is valid. A date must satisfy the conditions above: - yyyy is greater than or equal to 1979, - mm lies within the range [1, 12] (with 1 corresponding to January and 12 to December), - dd lies within a valid range for the month mm (from 1 to 28, 29, 30 or 31 depending on mm and whether yyyy is a leap year or not), - hh lies within the range [0, 23], - mn lies within the range [0, 59], - ss lies within the range [0, 59], - mis lies within the range [0, 999], - mics lies within the range [0, 999].C
        """
    def MicroSecond(self) -> int: 
        """
        Returns microsecond of a Date.
        """
    def MilliSecond(self) -> int: 
        """
        Returns millisecond of a Date.
        """
    def Minute(self) -> int: 
        """
        Returns minute of a Date.
        """
    def Month(self) -> int: 
        """
        Returns month of a Date.
        """
    def Second(self) -> int: 
        """
        Returns seconde of a Date.
        """
    def SetValues(self,mm : int,dd : int,yy : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: 
        """
        Assigns to this date the year yyyy, the month mm, the day dd, the hour hh, the minute mn, the second ss, the millisecond mis (defaulted to 0) and the microsecond mics (defaulted to 0). Exceptions Quantity_DateDefinitionError if mm, dd, hh, mn, ss, mis and mics are not components of a valid date.
        """
    def Subtract(self,aPeriod : Quantity_Period) -> Quantity_Date: 
        """
        Subtracts a period from a Date and returns the new Date. Raises an exception if the result date is anterior to Jan 1, 1979.
        """
    def Values(self) -> Tuple[int, int, int, int, int, int, int, int]: 
        """
        Gets a complete Date. - in mm - the month, - in dd - the day, - in yyyy - the year, - in hh - the hour, - in mn - the minute, - in ss - the second, - in mis - the millisecond, and - in mics - the microsecond
        """
    def Year(self) -> int: 
        """
        Returns year of a Date.
        """
    def __add__(self,aPeriod : Quantity_Period) -> Quantity_Date: 
        """
        None
        """
    @overload
    def __init__(self,mm : int,dd : int,yyyy : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __sub__(self,aPeriod : Quantity_Period) -> Quantity_Date: 
        """
        None
        """
    pass
class Quantity_DateDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Quantity', '__weakref__': <attribute '__weakref__' of 'Quantity_DateDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Quantity_DateDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Quantity_HArray1OfColor(Quantity_Array1OfColor, OCP.Standard.Standard_Transient):
    def Array1(self) -> Quantity_Array1OfColor: 
        """
        None
        """
    def Assign(self,theOther : Quantity_Array1OfColor) -> Quantity_Array1OfColor: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeArray1(self) -> Quantity_Array1OfColor: 
        """
        None
        """
    def ChangeFirst(self) -> Quantity_Color: 
        """
        Returns first element
        """
    def ChangeLast(self) -> Quantity_Color: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> Quantity_Color: 
        """
        Variable value access
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
    def First(self) -> Quantity_Color: 
        """
        Returns first element
        """
    def GetRefCount(self) -> int: 
        """
        Get the reference counter of this object
        """
    def IncrementRefCounter(self) -> None: 
        """
        Increments the reference counter of this object
        """
    def Init(self,theValue : Quantity_Color) -> None: 
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
    def Last(self) -> Quantity_Color: 
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
    def Move(self,theOther : Quantity_Array1OfColor) -> Quantity_Array1OfColor: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : Quantity_Color) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def This(self) -> OCP.Standard.Standard_Transient: 
        """
        Returns non-const pointer to this object (like const_cast). For protection against creating handle to objects allocated in stack or call from constructor, it will raise exception Standard_ProgramError if reference counter is zero.
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> Quantity_Color: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Quantity_Color) -> None: ...
    @overload
    def __init__(self,theOther : Quantity_Array1OfColor) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
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
class Quantity_NameOfColor():
    """
    Definition of names of known colors. The names come (mostly) from the X11 specification.

    Members:

      Quantity_NOC_BLACK

      Quantity_NOC_MATRABLUE

      Quantity_NOC_MATRAGRAY

      Quantity_NOC_ALICEBLUE

      Quantity_NOC_ANTIQUEWHITE

      Quantity_NOC_ANTIQUEWHITE1

      Quantity_NOC_ANTIQUEWHITE2

      Quantity_NOC_ANTIQUEWHITE3

      Quantity_NOC_ANTIQUEWHITE4

      Quantity_NOC_AQUAMARINE1

      Quantity_NOC_AQUAMARINE2

      Quantity_NOC_AQUAMARINE4

      Quantity_NOC_AZURE

      Quantity_NOC_AZURE2

      Quantity_NOC_AZURE3

      Quantity_NOC_AZURE4

      Quantity_NOC_BEIGE

      Quantity_NOC_BISQUE

      Quantity_NOC_BISQUE2

      Quantity_NOC_BISQUE3

      Quantity_NOC_BISQUE4

      Quantity_NOC_BLANCHEDALMOND

      Quantity_NOC_BLUE

      Quantity_NOC_BLUE1

      Quantity_NOC_BLUE2

      Quantity_NOC_BLUE3

      Quantity_NOC_BLUE4

      Quantity_NOC_BLUEVIOLET

      Quantity_NOC_BROWN

      Quantity_NOC_BROWN1

      Quantity_NOC_BROWN2

      Quantity_NOC_BROWN3

      Quantity_NOC_BROWN4

      Quantity_NOC_BURLYWOOD

      Quantity_NOC_BURLYWOOD1

      Quantity_NOC_BURLYWOOD2

      Quantity_NOC_BURLYWOOD3

      Quantity_NOC_BURLYWOOD4

      Quantity_NOC_CADETBLUE

      Quantity_NOC_CADETBLUE1

      Quantity_NOC_CADETBLUE2

      Quantity_NOC_CADETBLUE3

      Quantity_NOC_CADETBLUE4

      Quantity_NOC_CHARTREUSE

      Quantity_NOC_CHARTREUSE1

      Quantity_NOC_CHARTREUSE2

      Quantity_NOC_CHARTREUSE3

      Quantity_NOC_CHARTREUSE4

      Quantity_NOC_CHOCOLATE

      Quantity_NOC_CHOCOLATE1

      Quantity_NOC_CHOCOLATE2

      Quantity_NOC_CHOCOLATE3

      Quantity_NOC_CHOCOLATE4

      Quantity_NOC_CORAL

      Quantity_NOC_CORAL1

      Quantity_NOC_CORAL2

      Quantity_NOC_CORAL3

      Quantity_NOC_CORAL4

      Quantity_NOC_CORNFLOWERBLUE

      Quantity_NOC_CORNSILK1

      Quantity_NOC_CORNSILK2

      Quantity_NOC_CORNSILK3

      Quantity_NOC_CORNSILK4

      Quantity_NOC_CYAN

      Quantity_NOC_CYAN1

      Quantity_NOC_CYAN2

      Quantity_NOC_CYAN3

      Quantity_NOC_CYAN4

      Quantity_NOC_DARKGOLDENROD

      Quantity_NOC_DARKGOLDENROD1

      Quantity_NOC_DARKGOLDENROD2

      Quantity_NOC_DARKGOLDENROD3

      Quantity_NOC_DARKGOLDENROD4

      Quantity_NOC_DARKGREEN

      Quantity_NOC_DARKKHAKI

      Quantity_NOC_DARKOLIVEGREEN

      Quantity_NOC_DARKOLIVEGREEN1

      Quantity_NOC_DARKOLIVEGREEN2

      Quantity_NOC_DARKOLIVEGREEN3

      Quantity_NOC_DARKOLIVEGREEN4

      Quantity_NOC_DARKORANGE

      Quantity_NOC_DARKORANGE1

      Quantity_NOC_DARKORANGE2

      Quantity_NOC_DARKORANGE3

      Quantity_NOC_DARKORANGE4

      Quantity_NOC_DARKORCHID

      Quantity_NOC_DARKORCHID1

      Quantity_NOC_DARKORCHID2

      Quantity_NOC_DARKORCHID3

      Quantity_NOC_DARKORCHID4

      Quantity_NOC_DARKSALMON

      Quantity_NOC_DARKSEAGREEN

      Quantity_NOC_DARKSEAGREEN1

      Quantity_NOC_DARKSEAGREEN2

      Quantity_NOC_DARKSEAGREEN3

      Quantity_NOC_DARKSEAGREEN4

      Quantity_NOC_DARKSLATEBLUE

      Quantity_NOC_DARKSLATEGRAY1

      Quantity_NOC_DARKSLATEGRAY2

      Quantity_NOC_DARKSLATEGRAY3

      Quantity_NOC_DARKSLATEGRAY4

      Quantity_NOC_DARKSLATEGRAY

      Quantity_NOC_DARKTURQUOISE

      Quantity_NOC_DARKVIOLET

      Quantity_NOC_DEEPPINK

      Quantity_NOC_DEEPPINK2

      Quantity_NOC_DEEPPINK3

      Quantity_NOC_DEEPPINK4

      Quantity_NOC_DEEPSKYBLUE1

      Quantity_NOC_DEEPSKYBLUE2

      Quantity_NOC_DEEPSKYBLUE3

      Quantity_NOC_DEEPSKYBLUE4

      Quantity_NOC_DODGERBLUE1

      Quantity_NOC_DODGERBLUE2

      Quantity_NOC_DODGERBLUE3

      Quantity_NOC_DODGERBLUE4

      Quantity_NOC_FIREBRICK

      Quantity_NOC_FIREBRICK1

      Quantity_NOC_FIREBRICK2

      Quantity_NOC_FIREBRICK3

      Quantity_NOC_FIREBRICK4

      Quantity_NOC_FLORALWHITE

      Quantity_NOC_FORESTGREEN

      Quantity_NOC_GAINSBORO

      Quantity_NOC_GHOSTWHITE

      Quantity_NOC_GOLD

      Quantity_NOC_GOLD1

      Quantity_NOC_GOLD2

      Quantity_NOC_GOLD3

      Quantity_NOC_GOLD4

      Quantity_NOC_GOLDENROD

      Quantity_NOC_GOLDENROD1

      Quantity_NOC_GOLDENROD2

      Quantity_NOC_GOLDENROD3

      Quantity_NOC_GOLDENROD4

      Quantity_NOC_GRAY

      Quantity_NOC_GRAY0

      Quantity_NOC_GRAY1

      Quantity_NOC_GRAY2

      Quantity_NOC_GRAY3

      Quantity_NOC_GRAY4

      Quantity_NOC_GRAY5

      Quantity_NOC_GRAY6

      Quantity_NOC_GRAY7

      Quantity_NOC_GRAY8

      Quantity_NOC_GRAY9

      Quantity_NOC_GRAY10

      Quantity_NOC_GRAY11

      Quantity_NOC_GRAY12

      Quantity_NOC_GRAY13

      Quantity_NOC_GRAY14

      Quantity_NOC_GRAY15

      Quantity_NOC_GRAY16

      Quantity_NOC_GRAY17

      Quantity_NOC_GRAY18

      Quantity_NOC_GRAY19

      Quantity_NOC_GRAY20

      Quantity_NOC_GRAY21

      Quantity_NOC_GRAY22

      Quantity_NOC_GRAY23

      Quantity_NOC_GRAY24

      Quantity_NOC_GRAY25

      Quantity_NOC_GRAY26

      Quantity_NOC_GRAY27

      Quantity_NOC_GRAY28

      Quantity_NOC_GRAY29

      Quantity_NOC_GRAY30

      Quantity_NOC_GRAY31

      Quantity_NOC_GRAY32

      Quantity_NOC_GRAY33

      Quantity_NOC_GRAY34

      Quantity_NOC_GRAY35

      Quantity_NOC_GRAY36

      Quantity_NOC_GRAY37

      Quantity_NOC_GRAY38

      Quantity_NOC_GRAY39

      Quantity_NOC_GRAY40

      Quantity_NOC_GRAY41

      Quantity_NOC_GRAY42

      Quantity_NOC_GRAY43

      Quantity_NOC_GRAY44

      Quantity_NOC_GRAY45

      Quantity_NOC_GRAY46

      Quantity_NOC_GRAY47

      Quantity_NOC_GRAY48

      Quantity_NOC_GRAY49

      Quantity_NOC_GRAY50

      Quantity_NOC_GRAY51

      Quantity_NOC_GRAY52

      Quantity_NOC_GRAY53

      Quantity_NOC_GRAY54

      Quantity_NOC_GRAY55

      Quantity_NOC_GRAY56

      Quantity_NOC_GRAY57

      Quantity_NOC_GRAY58

      Quantity_NOC_GRAY59

      Quantity_NOC_GRAY60

      Quantity_NOC_GRAY61

      Quantity_NOC_GRAY62

      Quantity_NOC_GRAY63

      Quantity_NOC_GRAY64

      Quantity_NOC_GRAY65

      Quantity_NOC_GRAY66

      Quantity_NOC_GRAY67

      Quantity_NOC_GRAY68

      Quantity_NOC_GRAY69

      Quantity_NOC_GRAY70

      Quantity_NOC_GRAY71

      Quantity_NOC_GRAY72

      Quantity_NOC_GRAY73

      Quantity_NOC_GRAY74

      Quantity_NOC_GRAY75

      Quantity_NOC_GRAY76

      Quantity_NOC_GRAY77

      Quantity_NOC_GRAY78

      Quantity_NOC_GRAY79

      Quantity_NOC_GRAY80

      Quantity_NOC_GRAY81

      Quantity_NOC_GRAY82

      Quantity_NOC_GRAY83

      Quantity_NOC_GRAY85

      Quantity_NOC_GRAY86

      Quantity_NOC_GRAY87

      Quantity_NOC_GRAY88

      Quantity_NOC_GRAY89

      Quantity_NOC_GRAY90

      Quantity_NOC_GRAY91

      Quantity_NOC_GRAY92

      Quantity_NOC_GRAY93

      Quantity_NOC_GRAY94

      Quantity_NOC_GRAY95

      Quantity_NOC_GRAY97

      Quantity_NOC_GRAY98

      Quantity_NOC_GRAY99

      Quantity_NOC_GREEN

      Quantity_NOC_GREEN1

      Quantity_NOC_GREEN2

      Quantity_NOC_GREEN3

      Quantity_NOC_GREEN4

      Quantity_NOC_GREENYELLOW

      Quantity_NOC_HONEYDEW

      Quantity_NOC_HONEYDEW2

      Quantity_NOC_HONEYDEW3

      Quantity_NOC_HONEYDEW4

      Quantity_NOC_HOTPINK

      Quantity_NOC_HOTPINK1

      Quantity_NOC_HOTPINK2

      Quantity_NOC_HOTPINK3

      Quantity_NOC_HOTPINK4

      Quantity_NOC_INDIANRED

      Quantity_NOC_INDIANRED1

      Quantity_NOC_INDIANRED2

      Quantity_NOC_INDIANRED3

      Quantity_NOC_INDIANRED4

      Quantity_NOC_IVORY

      Quantity_NOC_IVORY2

      Quantity_NOC_IVORY3

      Quantity_NOC_IVORY4

      Quantity_NOC_KHAKI

      Quantity_NOC_KHAKI1

      Quantity_NOC_KHAKI2

      Quantity_NOC_KHAKI3

      Quantity_NOC_KHAKI4

      Quantity_NOC_LAVENDER

      Quantity_NOC_LAVENDERBLUSH1

      Quantity_NOC_LAVENDERBLUSH2

      Quantity_NOC_LAVENDERBLUSH3

      Quantity_NOC_LAVENDERBLUSH4

      Quantity_NOC_LAWNGREEN

      Quantity_NOC_LEMONCHIFFON1

      Quantity_NOC_LEMONCHIFFON2

      Quantity_NOC_LEMONCHIFFON3

      Quantity_NOC_LEMONCHIFFON4

      Quantity_NOC_LIGHTBLUE

      Quantity_NOC_LIGHTBLUE1

      Quantity_NOC_LIGHTBLUE2

      Quantity_NOC_LIGHTBLUE3

      Quantity_NOC_LIGHTBLUE4

      Quantity_NOC_LIGHTCORAL

      Quantity_NOC_LIGHTCYAN

      Quantity_NOC_LIGHTCYAN1

      Quantity_NOC_LIGHTCYAN2

      Quantity_NOC_LIGHTCYAN3

      Quantity_NOC_LIGHTCYAN4

      Quantity_NOC_LIGHTGOLDENROD

      Quantity_NOC_LIGHTGOLDENROD1

      Quantity_NOC_LIGHTGOLDENROD2

      Quantity_NOC_LIGHTGOLDENROD3

      Quantity_NOC_LIGHTGOLDENROD4

      Quantity_NOC_LIGHTGOLDENRODYELLOW

      Quantity_NOC_LIGHTGRAY

      Quantity_NOC_LIGHTPINK

      Quantity_NOC_LIGHTPINK1

      Quantity_NOC_LIGHTPINK2

      Quantity_NOC_LIGHTPINK3

      Quantity_NOC_LIGHTPINK4

      Quantity_NOC_LIGHTSALMON1

      Quantity_NOC_LIGHTSALMON2

      Quantity_NOC_LIGHTSALMON3

      Quantity_NOC_LIGHTSALMON4

      Quantity_NOC_LIGHTSEAGREEN

      Quantity_NOC_LIGHTSKYBLUE

      Quantity_NOC_LIGHTSKYBLUE1

      Quantity_NOC_LIGHTSKYBLUE2

      Quantity_NOC_LIGHTSKYBLUE3

      Quantity_NOC_LIGHTSKYBLUE4

      Quantity_NOC_LIGHTSLATEBLUE

      Quantity_NOC_LIGHTSLATEGRAY

      Quantity_NOC_LIGHTSTEELBLUE

      Quantity_NOC_LIGHTSTEELBLUE1

      Quantity_NOC_LIGHTSTEELBLUE2

      Quantity_NOC_LIGHTSTEELBLUE3

      Quantity_NOC_LIGHTSTEELBLUE4

      Quantity_NOC_LIGHTYELLOW

      Quantity_NOC_LIGHTYELLOW2

      Quantity_NOC_LIGHTYELLOW3

      Quantity_NOC_LIGHTYELLOW4

      Quantity_NOC_LIMEGREEN

      Quantity_NOC_LINEN

      Quantity_NOC_MAGENTA

      Quantity_NOC_MAGENTA1

      Quantity_NOC_MAGENTA2

      Quantity_NOC_MAGENTA3

      Quantity_NOC_MAGENTA4

      Quantity_NOC_MAROON

      Quantity_NOC_MAROON1

      Quantity_NOC_MAROON2

      Quantity_NOC_MAROON3

      Quantity_NOC_MAROON4

      Quantity_NOC_MEDIUMAQUAMARINE

      Quantity_NOC_MEDIUMORCHID

      Quantity_NOC_MEDIUMORCHID1

      Quantity_NOC_MEDIUMORCHID2

      Quantity_NOC_MEDIUMORCHID3

      Quantity_NOC_MEDIUMORCHID4

      Quantity_NOC_MEDIUMPURPLE

      Quantity_NOC_MEDIUMPURPLE1

      Quantity_NOC_MEDIUMPURPLE2

      Quantity_NOC_MEDIUMPURPLE3

      Quantity_NOC_MEDIUMPURPLE4

      Quantity_NOC_MEDIUMSEAGREEN

      Quantity_NOC_MEDIUMSLATEBLUE

      Quantity_NOC_MEDIUMSPRINGGREEN

      Quantity_NOC_MEDIUMTURQUOISE

      Quantity_NOC_MEDIUMVIOLETRED

      Quantity_NOC_MIDNIGHTBLUE

      Quantity_NOC_MINTCREAM

      Quantity_NOC_MISTYROSE

      Quantity_NOC_MISTYROSE2

      Quantity_NOC_MISTYROSE3

      Quantity_NOC_MISTYROSE4

      Quantity_NOC_MOCCASIN

      Quantity_NOC_NAVAJOWHITE1

      Quantity_NOC_NAVAJOWHITE2

      Quantity_NOC_NAVAJOWHITE3

      Quantity_NOC_NAVAJOWHITE4

      Quantity_NOC_NAVYBLUE

      Quantity_NOC_OLDLACE

      Quantity_NOC_OLIVEDRAB

      Quantity_NOC_OLIVEDRAB1

      Quantity_NOC_OLIVEDRAB2

      Quantity_NOC_OLIVEDRAB3

      Quantity_NOC_OLIVEDRAB4

      Quantity_NOC_ORANGE

      Quantity_NOC_ORANGE1

      Quantity_NOC_ORANGE2

      Quantity_NOC_ORANGE3

      Quantity_NOC_ORANGE4

      Quantity_NOC_ORANGERED

      Quantity_NOC_ORANGERED1

      Quantity_NOC_ORANGERED2

      Quantity_NOC_ORANGERED3

      Quantity_NOC_ORANGERED4

      Quantity_NOC_ORCHID

      Quantity_NOC_ORCHID1

      Quantity_NOC_ORCHID2

      Quantity_NOC_ORCHID3

      Quantity_NOC_ORCHID4

      Quantity_NOC_PALEGOLDENROD

      Quantity_NOC_PALEGREEN

      Quantity_NOC_PALEGREEN1

      Quantity_NOC_PALEGREEN2

      Quantity_NOC_PALEGREEN3

      Quantity_NOC_PALEGREEN4

      Quantity_NOC_PALETURQUOISE

      Quantity_NOC_PALETURQUOISE1

      Quantity_NOC_PALETURQUOISE2

      Quantity_NOC_PALETURQUOISE3

      Quantity_NOC_PALETURQUOISE4

      Quantity_NOC_PALEVIOLETRED

      Quantity_NOC_PALEVIOLETRED1

      Quantity_NOC_PALEVIOLETRED2

      Quantity_NOC_PALEVIOLETRED3

      Quantity_NOC_PALEVIOLETRED4

      Quantity_NOC_PAPAYAWHIP

      Quantity_NOC_PEACHPUFF

      Quantity_NOC_PEACHPUFF2

      Quantity_NOC_PEACHPUFF3

      Quantity_NOC_PEACHPUFF4

      Quantity_NOC_PERU

      Quantity_NOC_PINK

      Quantity_NOC_PINK1

      Quantity_NOC_PINK2

      Quantity_NOC_PINK3

      Quantity_NOC_PINK4

      Quantity_NOC_PLUM

      Quantity_NOC_PLUM1

      Quantity_NOC_PLUM2

      Quantity_NOC_PLUM3

      Quantity_NOC_PLUM4

      Quantity_NOC_POWDERBLUE

      Quantity_NOC_PURPLE

      Quantity_NOC_PURPLE1

      Quantity_NOC_PURPLE2

      Quantity_NOC_PURPLE3

      Quantity_NOC_PURPLE4

      Quantity_NOC_RED

      Quantity_NOC_RED1

      Quantity_NOC_RED2

      Quantity_NOC_RED3

      Quantity_NOC_RED4

      Quantity_NOC_ROSYBROWN

      Quantity_NOC_ROSYBROWN1

      Quantity_NOC_ROSYBROWN2

      Quantity_NOC_ROSYBROWN3

      Quantity_NOC_ROSYBROWN4

      Quantity_NOC_ROYALBLUE

      Quantity_NOC_ROYALBLUE1

      Quantity_NOC_ROYALBLUE2

      Quantity_NOC_ROYALBLUE3

      Quantity_NOC_ROYALBLUE4

      Quantity_NOC_SADDLEBROWN

      Quantity_NOC_SALMON

      Quantity_NOC_SALMON1

      Quantity_NOC_SALMON2

      Quantity_NOC_SALMON3

      Quantity_NOC_SALMON4

      Quantity_NOC_SANDYBROWN

      Quantity_NOC_SEAGREEN

      Quantity_NOC_SEAGREEN1

      Quantity_NOC_SEAGREEN2

      Quantity_NOC_SEAGREEN3

      Quantity_NOC_SEAGREEN4

      Quantity_NOC_SEASHELL

      Quantity_NOC_SEASHELL2

      Quantity_NOC_SEASHELL3

      Quantity_NOC_SEASHELL4

      Quantity_NOC_BEET

      Quantity_NOC_TEAL

      Quantity_NOC_SIENNA

      Quantity_NOC_SIENNA1

      Quantity_NOC_SIENNA2

      Quantity_NOC_SIENNA3

      Quantity_NOC_SIENNA4

      Quantity_NOC_SKYBLUE

      Quantity_NOC_SKYBLUE1

      Quantity_NOC_SKYBLUE2

      Quantity_NOC_SKYBLUE3

      Quantity_NOC_SKYBLUE4

      Quantity_NOC_SLATEBLUE

      Quantity_NOC_SLATEBLUE1

      Quantity_NOC_SLATEBLUE2

      Quantity_NOC_SLATEBLUE3

      Quantity_NOC_SLATEBLUE4

      Quantity_NOC_SLATEGRAY1

      Quantity_NOC_SLATEGRAY2

      Quantity_NOC_SLATEGRAY3

      Quantity_NOC_SLATEGRAY4

      Quantity_NOC_SLATEGRAY

      Quantity_NOC_SNOW

      Quantity_NOC_SNOW2

      Quantity_NOC_SNOW3

      Quantity_NOC_SNOW4

      Quantity_NOC_SPRINGGREEN

      Quantity_NOC_SPRINGGREEN2

      Quantity_NOC_SPRINGGREEN3

      Quantity_NOC_SPRINGGREEN4

      Quantity_NOC_STEELBLUE

      Quantity_NOC_STEELBLUE1

      Quantity_NOC_STEELBLUE2

      Quantity_NOC_STEELBLUE3

      Quantity_NOC_STEELBLUE4

      Quantity_NOC_TAN

      Quantity_NOC_TAN1

      Quantity_NOC_TAN2

      Quantity_NOC_TAN3

      Quantity_NOC_TAN4

      Quantity_NOC_THISTLE

      Quantity_NOC_THISTLE1

      Quantity_NOC_THISTLE2

      Quantity_NOC_THISTLE3

      Quantity_NOC_THISTLE4

      Quantity_NOC_TOMATO

      Quantity_NOC_TOMATO1

      Quantity_NOC_TOMATO2

      Quantity_NOC_TOMATO3

      Quantity_NOC_TOMATO4

      Quantity_NOC_TURQUOISE

      Quantity_NOC_TURQUOISE1

      Quantity_NOC_TURQUOISE2

      Quantity_NOC_TURQUOISE3

      Quantity_NOC_TURQUOISE4

      Quantity_NOC_VIOLET

      Quantity_NOC_VIOLETRED

      Quantity_NOC_VIOLETRED1

      Quantity_NOC_VIOLETRED2

      Quantity_NOC_VIOLETRED3

      Quantity_NOC_VIOLETRED4

      Quantity_NOC_WHEAT

      Quantity_NOC_WHEAT1

      Quantity_NOC_WHEAT2

      Quantity_NOC_WHEAT3

      Quantity_NOC_WHEAT4

      Quantity_NOC_WHITESMOKE

      Quantity_NOC_YELLOW

      Quantity_NOC_YELLOW1

      Quantity_NOC_YELLOW2

      Quantity_NOC_YELLOW3

      Quantity_NOC_YELLOW4

      Quantity_NOC_YELLOWGREEN

      Quantity_NOC_WHITE
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    Quantity_NOC_ALICEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ALICEBLUE: 3>
    Quantity_NOC_ANTIQUEWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE: 4>
    Quantity_NOC_ANTIQUEWHITE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1: 5>
    Quantity_NOC_ANTIQUEWHITE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2: 6>
    Quantity_NOC_ANTIQUEWHITE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3: 7>
    Quantity_NOC_ANTIQUEWHITE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4: 8>
    Quantity_NOC_AQUAMARINE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1: 9>
    Quantity_NOC_AQUAMARINE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2: 10>
    Quantity_NOC_AQUAMARINE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4: 11>
    Quantity_NOC_AZURE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE: 12>
    Quantity_NOC_AZURE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE2: 13>
    Quantity_NOC_AZURE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE3: 14>
    Quantity_NOC_AZURE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE4: 15>
    Quantity_NOC_BEET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BEET: 437>
    Quantity_NOC_BEIGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BEIGE: 16>
    Quantity_NOC_BISQUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE: 17>
    Quantity_NOC_BISQUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE2: 18>
    Quantity_NOC_BISQUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE3: 19>
    Quantity_NOC_BISQUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE4: 20>
    Quantity_NOC_BLACK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLACK: 0>
    Quantity_NOC_BLANCHEDALMOND: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND: 21>
    Quantity_NOC_BLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>
    Quantity_NOC_BLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>
    Quantity_NOC_BLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE2: 23>
    Quantity_NOC_BLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE3: 24>
    Quantity_NOC_BLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE4: 25>
    Quantity_NOC_BLUEVIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET: 26>
    Quantity_NOC_BROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN: 27>
    Quantity_NOC_BROWN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN1: 28>
    Quantity_NOC_BROWN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN2: 29>
    Quantity_NOC_BROWN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN3: 30>
    Quantity_NOC_BROWN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN4: 31>
    Quantity_NOC_BURLYWOOD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD: 32>
    Quantity_NOC_BURLYWOOD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1: 33>
    Quantity_NOC_BURLYWOOD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2: 34>
    Quantity_NOC_BURLYWOOD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3: 35>
    Quantity_NOC_BURLYWOOD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4: 36>
    Quantity_NOC_CADETBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE: 37>
    Quantity_NOC_CADETBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE1: 38>
    Quantity_NOC_CADETBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE2: 39>
    Quantity_NOC_CADETBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE3: 40>
    Quantity_NOC_CADETBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE4: 41>
    Quantity_NOC_CHARTREUSE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>
    Quantity_NOC_CHARTREUSE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>
    Quantity_NOC_CHARTREUSE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2: 43>
    Quantity_NOC_CHARTREUSE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3: 44>
    Quantity_NOC_CHARTREUSE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4: 45>
    Quantity_NOC_CHOCOLATE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE: 46>
    Quantity_NOC_CHOCOLATE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1: 47>
    Quantity_NOC_CHOCOLATE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2: 48>
    Quantity_NOC_CHOCOLATE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3: 49>
    Quantity_NOC_CHOCOLATE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4: 50>
    Quantity_NOC_CORAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL: 51>
    Quantity_NOC_CORAL1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL1: 52>
    Quantity_NOC_CORAL2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL2: 53>
    Quantity_NOC_CORAL3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL3: 54>
    Quantity_NOC_CORAL4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL4: 55>
    Quantity_NOC_CORNFLOWERBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE: 56>
    Quantity_NOC_CORNSILK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK1: 57>
    Quantity_NOC_CORNSILK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK2: 58>
    Quantity_NOC_CORNSILK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK3: 59>
    Quantity_NOC_CORNSILK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK4: 60>
    Quantity_NOC_CYAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>
    Quantity_NOC_CYAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>
    Quantity_NOC_CYAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN2: 62>
    Quantity_NOC_CYAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN3: 63>
    Quantity_NOC_CYAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN4: 64>
    Quantity_NOC_DARKGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD: 65>
    Quantity_NOC_DARKGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1: 66>
    Quantity_NOC_DARKGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2: 67>
    Quantity_NOC_DARKGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3: 68>
    Quantity_NOC_DARKGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4: 69>
    Quantity_NOC_DARKGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGREEN: 70>
    Quantity_NOC_DARKKHAKI: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKKHAKI: 71>
    Quantity_NOC_DARKOLIVEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN: 72>
    Quantity_NOC_DARKOLIVEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1: 73>
    Quantity_NOC_DARKOLIVEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2: 74>
    Quantity_NOC_DARKOLIVEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3: 75>
    Quantity_NOC_DARKOLIVEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4: 76>
    Quantity_NOC_DARKORANGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE: 77>
    Quantity_NOC_DARKORANGE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE1: 78>
    Quantity_NOC_DARKORANGE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE2: 79>
    Quantity_NOC_DARKORANGE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE3: 80>
    Quantity_NOC_DARKORANGE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE4: 81>
    Quantity_NOC_DARKORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID: 82>
    Quantity_NOC_DARKORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID1: 83>
    Quantity_NOC_DARKORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID2: 84>
    Quantity_NOC_DARKORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID3: 85>
    Quantity_NOC_DARKORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID4: 86>
    Quantity_NOC_DARKSALMON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSALMON: 87>
    Quantity_NOC_DARKSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN: 88>
    Quantity_NOC_DARKSEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1: 89>
    Quantity_NOC_DARKSEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2: 90>
    Quantity_NOC_DARKSEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3: 91>
    Quantity_NOC_DARKSEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4: 92>
    Quantity_NOC_DARKSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE: 93>
    Quantity_NOC_DARKSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY: 98>
    Quantity_NOC_DARKSLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1: 94>
    Quantity_NOC_DARKSLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2: 95>
    Quantity_NOC_DARKSLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3: 96>
    Quantity_NOC_DARKSLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4: 97>
    Quantity_NOC_DARKTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE: 99>
    Quantity_NOC_DARKVIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKVIOLET: 100>
    Quantity_NOC_DEEPPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK: 101>
    Quantity_NOC_DEEPPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK2: 102>
    Quantity_NOC_DEEPPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK3: 103>
    Quantity_NOC_DEEPPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK4: 104>
    Quantity_NOC_DEEPSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1: 105>
    Quantity_NOC_DEEPSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2: 106>
    Quantity_NOC_DEEPSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3: 107>
    Quantity_NOC_DEEPSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4: 108>
    Quantity_NOC_DODGERBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1: 109>
    Quantity_NOC_DODGERBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2: 110>
    Quantity_NOC_DODGERBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3: 111>
    Quantity_NOC_DODGERBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4: 112>
    Quantity_NOC_FIREBRICK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK: 113>
    Quantity_NOC_FIREBRICK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK1: 114>
    Quantity_NOC_FIREBRICK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK2: 115>
    Quantity_NOC_FIREBRICK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK3: 116>
    Quantity_NOC_FIREBRICK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK4: 117>
    Quantity_NOC_FLORALWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FLORALWHITE: 118>
    Quantity_NOC_FORESTGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FORESTGREEN: 119>
    Quantity_NOC_GAINSBORO: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GAINSBORO: 120>
    Quantity_NOC_GHOSTWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE: 121>
    Quantity_NOC_GOLD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>
    Quantity_NOC_GOLD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>
    Quantity_NOC_GOLD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD2: 123>
    Quantity_NOC_GOLD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD3: 124>
    Quantity_NOC_GOLD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD4: 125>
    Quantity_NOC_GOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD: 126>
    Quantity_NOC_GOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD1: 127>
    Quantity_NOC_GOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD2: 128>
    Quantity_NOC_GOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD3: 129>
    Quantity_NOC_GOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD4: 130>
    Quantity_NOC_GRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY: 131>
    Quantity_NOC_GRAY0: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY0: 132>
    Quantity_NOC_GRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY1: 133>
    Quantity_NOC_GRAY10: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY10: 142>
    Quantity_NOC_GRAY11: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY11: 143>
    Quantity_NOC_GRAY12: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY12: 144>
    Quantity_NOC_GRAY13: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY13: 145>
    Quantity_NOC_GRAY14: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY14: 146>
    Quantity_NOC_GRAY15: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY15: 147>
    Quantity_NOC_GRAY16: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY16: 148>
    Quantity_NOC_GRAY17: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY17: 149>
    Quantity_NOC_GRAY18: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY18: 150>
    Quantity_NOC_GRAY19: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY19: 151>
    Quantity_NOC_GRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY2: 134>
    Quantity_NOC_GRAY20: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY20: 152>
    Quantity_NOC_GRAY21: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY21: 153>
    Quantity_NOC_GRAY22: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY22: 154>
    Quantity_NOC_GRAY23: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY23: 155>
    Quantity_NOC_GRAY24: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY24: 156>
    Quantity_NOC_GRAY25: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY25: 157>
    Quantity_NOC_GRAY26: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY26: 158>
    Quantity_NOC_GRAY27: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY27: 159>
    Quantity_NOC_GRAY28: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY28: 160>
    Quantity_NOC_GRAY29: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY29: 161>
    Quantity_NOC_GRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY3: 135>
    Quantity_NOC_GRAY30: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY30: 162>
    Quantity_NOC_GRAY31: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY31: 163>
    Quantity_NOC_GRAY32: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY32: 164>
    Quantity_NOC_GRAY33: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY33: 165>
    Quantity_NOC_GRAY34: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY34: 166>
    Quantity_NOC_GRAY35: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY35: 167>
    Quantity_NOC_GRAY36: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY36: 168>
    Quantity_NOC_GRAY37: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY37: 169>
    Quantity_NOC_GRAY38: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY38: 170>
    Quantity_NOC_GRAY39: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY39: 171>
    Quantity_NOC_GRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY4: 136>
    Quantity_NOC_GRAY40: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY40: 172>
    Quantity_NOC_GRAY41: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY41: 173>
    Quantity_NOC_GRAY42: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY42: 174>
    Quantity_NOC_GRAY43: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY43: 175>
    Quantity_NOC_GRAY44: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY44: 176>
    Quantity_NOC_GRAY45: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY45: 177>
    Quantity_NOC_GRAY46: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY46: 178>
    Quantity_NOC_GRAY47: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY47: 179>
    Quantity_NOC_GRAY48: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY48: 180>
    Quantity_NOC_GRAY49: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY49: 181>
    Quantity_NOC_GRAY5: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY5: 137>
    Quantity_NOC_GRAY50: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY50: 182>
    Quantity_NOC_GRAY51: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY51: 183>
    Quantity_NOC_GRAY52: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY52: 184>
    Quantity_NOC_GRAY53: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY53: 185>
    Quantity_NOC_GRAY54: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY54: 186>
    Quantity_NOC_GRAY55: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY55: 187>
    Quantity_NOC_GRAY56: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY56: 188>
    Quantity_NOC_GRAY57: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY57: 189>
    Quantity_NOC_GRAY58: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY58: 190>
    Quantity_NOC_GRAY59: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY59: 191>
    Quantity_NOC_GRAY6: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY6: 138>
    Quantity_NOC_GRAY60: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY60: 192>
    Quantity_NOC_GRAY61: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY61: 193>
    Quantity_NOC_GRAY62: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY62: 194>
    Quantity_NOC_GRAY63: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY63: 195>
    Quantity_NOC_GRAY64: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY64: 196>
    Quantity_NOC_GRAY65: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY65: 197>
    Quantity_NOC_GRAY66: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY66: 198>
    Quantity_NOC_GRAY67: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY67: 199>
    Quantity_NOC_GRAY68: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY68: 200>
    Quantity_NOC_GRAY69: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY69: 201>
    Quantity_NOC_GRAY7: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY7: 139>
    Quantity_NOC_GRAY70: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY70: 202>
    Quantity_NOC_GRAY71: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY71: 203>
    Quantity_NOC_GRAY72: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY72: 204>
    Quantity_NOC_GRAY73: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY73: 205>
    Quantity_NOC_GRAY74: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY74: 206>
    Quantity_NOC_GRAY75: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY75: 207>
    Quantity_NOC_GRAY76: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY76: 208>
    Quantity_NOC_GRAY77: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY77: 209>
    Quantity_NOC_GRAY78: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY78: 210>
    Quantity_NOC_GRAY79: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY79: 211>
    Quantity_NOC_GRAY8: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY8: 140>
    Quantity_NOC_GRAY80: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY80: 212>
    Quantity_NOC_GRAY81: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY81: 213>
    Quantity_NOC_GRAY82: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY82: 214>
    Quantity_NOC_GRAY83: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY83: 215>
    Quantity_NOC_GRAY85: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY85: 216>
    Quantity_NOC_GRAY86: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY86: 217>
    Quantity_NOC_GRAY87: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY87: 218>
    Quantity_NOC_GRAY88: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY88: 219>
    Quantity_NOC_GRAY89: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY89: 220>
    Quantity_NOC_GRAY9: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY9: 141>
    Quantity_NOC_GRAY90: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY90: 221>
    Quantity_NOC_GRAY91: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY91: 222>
    Quantity_NOC_GRAY92: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY92: 223>
    Quantity_NOC_GRAY93: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY93: 224>
    Quantity_NOC_GRAY94: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY94: 225>
    Quantity_NOC_GRAY95: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY95: 226>
    Quantity_NOC_GRAY97: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY97: 227>
    Quantity_NOC_GRAY98: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY98: 228>
    Quantity_NOC_GRAY99: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY99: 229>
    Quantity_NOC_GREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>
    Quantity_NOC_GREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>
    Quantity_NOC_GREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN2: 231>
    Quantity_NOC_GREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN3: 232>
    Quantity_NOC_GREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN4: 233>
    Quantity_NOC_GREENYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREENYELLOW: 234>
    Quantity_NOC_HONEYDEW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW: 235>
    Quantity_NOC_HONEYDEW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW2: 236>
    Quantity_NOC_HONEYDEW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW3: 237>
    Quantity_NOC_HONEYDEW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW4: 238>
    Quantity_NOC_HOTPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK: 239>
    Quantity_NOC_HOTPINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK1: 240>
    Quantity_NOC_HOTPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK2: 241>
    Quantity_NOC_HOTPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK3: 242>
    Quantity_NOC_HOTPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK4: 243>
    Quantity_NOC_INDIANRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED: 244>
    Quantity_NOC_INDIANRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED1: 245>
    Quantity_NOC_INDIANRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED2: 246>
    Quantity_NOC_INDIANRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED3: 247>
    Quantity_NOC_INDIANRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED4: 248>
    Quantity_NOC_IVORY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY: 249>
    Quantity_NOC_IVORY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY2: 250>
    Quantity_NOC_IVORY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY3: 251>
    Quantity_NOC_IVORY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY4: 252>
    Quantity_NOC_KHAKI: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI: 253>
    Quantity_NOC_KHAKI1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI1: 254>
    Quantity_NOC_KHAKI2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI2: 255>
    Quantity_NOC_KHAKI3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI3: 256>
    Quantity_NOC_KHAKI4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI4: 257>
    Quantity_NOC_LAVENDER: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDER: 258>
    Quantity_NOC_LAVENDERBLUSH1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1: 259>
    Quantity_NOC_LAVENDERBLUSH2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2: 260>
    Quantity_NOC_LAVENDERBLUSH3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3: 261>
    Quantity_NOC_LAVENDERBLUSH4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4: 262>
    Quantity_NOC_LAWNGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAWNGREEN: 263>
    Quantity_NOC_LEMONCHIFFON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1: 264>
    Quantity_NOC_LEMONCHIFFON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2: 265>
    Quantity_NOC_LEMONCHIFFON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3: 266>
    Quantity_NOC_LEMONCHIFFON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4: 267>
    Quantity_NOC_LIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE: 268>
    Quantity_NOC_LIGHTBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1: 269>
    Quantity_NOC_LIGHTBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2: 270>
    Quantity_NOC_LIGHTBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3: 271>
    Quantity_NOC_LIGHTBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4: 272>
    Quantity_NOC_LIGHTCORAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL: 273>
    Quantity_NOC_LIGHTCYAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>
    Quantity_NOC_LIGHTCYAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>
    Quantity_NOC_LIGHTCYAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2: 275>
    Quantity_NOC_LIGHTCYAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3: 276>
    Quantity_NOC_LIGHTCYAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4: 277>
    Quantity_NOC_LIGHTGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD: 278>
    Quantity_NOC_LIGHTGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1: 279>
    Quantity_NOC_LIGHTGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2: 280>
    Quantity_NOC_LIGHTGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3: 281>
    Quantity_NOC_LIGHTGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4: 282>
    Quantity_NOC_LIGHTGOLDENRODYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW: 283>
    Quantity_NOC_LIGHTGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY: 284>
    Quantity_NOC_LIGHTPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK: 285>
    Quantity_NOC_LIGHTPINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1: 286>
    Quantity_NOC_LIGHTPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2: 287>
    Quantity_NOC_LIGHTPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3: 288>
    Quantity_NOC_LIGHTPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4: 289>
    Quantity_NOC_LIGHTSALMON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1: 290>
    Quantity_NOC_LIGHTSALMON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2: 291>
    Quantity_NOC_LIGHTSALMON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3: 292>
    Quantity_NOC_LIGHTSALMON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4: 293>
    Quantity_NOC_LIGHTSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN: 294>
    Quantity_NOC_LIGHTSKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE: 295>
    Quantity_NOC_LIGHTSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1: 296>
    Quantity_NOC_LIGHTSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2: 297>
    Quantity_NOC_LIGHTSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3: 298>
    Quantity_NOC_LIGHTSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4: 299>
    Quantity_NOC_LIGHTSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE: 300>
    Quantity_NOC_LIGHTSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY: 301>
    Quantity_NOC_LIGHTSTEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE: 302>
    Quantity_NOC_LIGHTSTEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1: 303>
    Quantity_NOC_LIGHTSTEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2: 304>
    Quantity_NOC_LIGHTSTEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3: 305>
    Quantity_NOC_LIGHTSTEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4: 306>
    Quantity_NOC_LIGHTYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW: 307>
    Quantity_NOC_LIGHTYELLOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2: 308>
    Quantity_NOC_LIGHTYELLOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3: 309>
    Quantity_NOC_LIGHTYELLOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4: 310>
    Quantity_NOC_LIMEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIMEGREEN: 311>
    Quantity_NOC_LINEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LINEN: 312>
    Quantity_NOC_MAGENTA: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>
    Quantity_NOC_MAGENTA1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>
    Quantity_NOC_MAGENTA2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA2: 314>
    Quantity_NOC_MAGENTA3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA3: 315>
    Quantity_NOC_MAGENTA4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA4: 316>
    Quantity_NOC_MAROON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON: 317>
    Quantity_NOC_MAROON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON1: 318>
    Quantity_NOC_MAROON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON2: 319>
    Quantity_NOC_MAROON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON3: 320>
    Quantity_NOC_MAROON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON4: 321>
    Quantity_NOC_MATRABLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MATRABLUE: 1>
    Quantity_NOC_MATRAGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MATRAGRAY: 2>
    Quantity_NOC_MEDIUMAQUAMARINE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE: 322>
    Quantity_NOC_MEDIUMORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID: 323>
    Quantity_NOC_MEDIUMORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1: 324>
    Quantity_NOC_MEDIUMORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2: 325>
    Quantity_NOC_MEDIUMORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3: 326>
    Quantity_NOC_MEDIUMORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4: 327>
    Quantity_NOC_MEDIUMPURPLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE: 328>
    Quantity_NOC_MEDIUMPURPLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1: 329>
    Quantity_NOC_MEDIUMPURPLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2: 330>
    Quantity_NOC_MEDIUMPURPLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3: 331>
    Quantity_NOC_MEDIUMPURPLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4: 332>
    Quantity_NOC_MEDIUMSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN: 333>
    Quantity_NOC_MEDIUMSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE: 334>
    Quantity_NOC_MEDIUMSPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN: 335>
    Quantity_NOC_MEDIUMTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE: 336>
    Quantity_NOC_MEDIUMVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED: 337>
    Quantity_NOC_MIDNIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE: 338>
    Quantity_NOC_MINTCREAM: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MINTCREAM: 339>
    Quantity_NOC_MISTYROSE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE: 340>
    Quantity_NOC_MISTYROSE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE2: 341>
    Quantity_NOC_MISTYROSE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE3: 342>
    Quantity_NOC_MISTYROSE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE4: 343>
    Quantity_NOC_MOCCASIN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MOCCASIN: 344>
    Quantity_NOC_NAVAJOWHITE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1: 345>
    Quantity_NOC_NAVAJOWHITE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2: 346>
    Quantity_NOC_NAVAJOWHITE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3: 347>
    Quantity_NOC_NAVAJOWHITE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4: 348>
    Quantity_NOC_NAVYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVYBLUE: 349>
    Quantity_NOC_OLDLACE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLDLACE: 350>
    Quantity_NOC_OLIVEDRAB: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB: 351>
    Quantity_NOC_OLIVEDRAB1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1: 352>
    Quantity_NOC_OLIVEDRAB2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2: 353>
    Quantity_NOC_OLIVEDRAB3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3: 354>
    Quantity_NOC_OLIVEDRAB4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4: 355>
    Quantity_NOC_ORANGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>
    Quantity_NOC_ORANGE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>
    Quantity_NOC_ORANGE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE2: 357>
    Quantity_NOC_ORANGE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE3: 358>
    Quantity_NOC_ORANGE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE4: 359>
    Quantity_NOC_ORANGERED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>
    Quantity_NOC_ORANGERED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>
    Quantity_NOC_ORANGERED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED2: 361>
    Quantity_NOC_ORANGERED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED3: 362>
    Quantity_NOC_ORANGERED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED4: 363>
    Quantity_NOC_ORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID: 364>
    Quantity_NOC_ORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID1: 365>
    Quantity_NOC_ORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID2: 366>
    Quantity_NOC_ORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID3: 367>
    Quantity_NOC_ORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID4: 368>
    Quantity_NOC_PALEGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD: 369>
    Quantity_NOC_PALEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN: 370>
    Quantity_NOC_PALEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN1: 371>
    Quantity_NOC_PALEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN2: 372>
    Quantity_NOC_PALEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN3: 373>
    Quantity_NOC_PALEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN4: 374>
    Quantity_NOC_PALETURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE: 375>
    Quantity_NOC_PALETURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1: 376>
    Quantity_NOC_PALETURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2: 377>
    Quantity_NOC_PALETURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3: 378>
    Quantity_NOC_PALETURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4: 379>
    Quantity_NOC_PALEVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED: 380>
    Quantity_NOC_PALEVIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1: 381>
    Quantity_NOC_PALEVIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2: 382>
    Quantity_NOC_PALEVIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3: 383>
    Quantity_NOC_PALEVIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4: 384>
    Quantity_NOC_PAPAYAWHIP: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP: 385>
    Quantity_NOC_PEACHPUFF: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF: 386>
    Quantity_NOC_PEACHPUFF2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2: 387>
    Quantity_NOC_PEACHPUFF3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3: 388>
    Quantity_NOC_PEACHPUFF4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4: 389>
    Quantity_NOC_PERU: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PERU: 390>
    Quantity_NOC_PINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK: 391>
    Quantity_NOC_PINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK1: 392>
    Quantity_NOC_PINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK2: 393>
    Quantity_NOC_PINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK3: 394>
    Quantity_NOC_PINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK4: 395>
    Quantity_NOC_PLUM: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM: 396>
    Quantity_NOC_PLUM1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM1: 397>
    Quantity_NOC_PLUM2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM2: 398>
    Quantity_NOC_PLUM3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM3: 399>
    Quantity_NOC_PLUM4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM4: 400>
    Quantity_NOC_POWDERBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_POWDERBLUE: 401>
    Quantity_NOC_PURPLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE: 402>
    Quantity_NOC_PURPLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE1: 403>
    Quantity_NOC_PURPLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE2: 404>
    Quantity_NOC_PURPLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE3: 405>
    Quantity_NOC_PURPLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE4: 406>
    Quantity_NOC_RED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED: 407>
    Quantity_NOC_RED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED: 407>
    Quantity_NOC_RED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED2: 408>
    Quantity_NOC_RED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED3: 409>
    Quantity_NOC_RED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED4: 410>
    Quantity_NOC_ROSYBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN: 411>
    Quantity_NOC_ROSYBROWN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1: 412>
    Quantity_NOC_ROSYBROWN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2: 413>
    Quantity_NOC_ROSYBROWN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3: 414>
    Quantity_NOC_ROSYBROWN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4: 415>
    Quantity_NOC_ROYALBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE: 416>
    Quantity_NOC_ROYALBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1: 417>
    Quantity_NOC_ROYALBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2: 418>
    Quantity_NOC_ROYALBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3: 419>
    Quantity_NOC_ROYALBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4: 420>
    Quantity_NOC_SADDLEBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN: 421>
    Quantity_NOC_SALMON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON: 422>
    Quantity_NOC_SALMON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON1: 423>
    Quantity_NOC_SALMON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON2: 424>
    Quantity_NOC_SALMON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON3: 425>
    Quantity_NOC_SALMON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON4: 426>
    Quantity_NOC_SANDYBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SANDYBROWN: 427>
    Quantity_NOC_SEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN: 428>
    Quantity_NOC_SEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN1: 429>
    Quantity_NOC_SEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN2: 430>
    Quantity_NOC_SEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN3: 431>
    Quantity_NOC_SEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN4: 432>
    Quantity_NOC_SEASHELL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL: 433>
    Quantity_NOC_SEASHELL2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL2: 434>
    Quantity_NOC_SEASHELL3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL3: 435>
    Quantity_NOC_SEASHELL4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL4: 436>
    Quantity_NOC_SIENNA: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA: 439>
    Quantity_NOC_SIENNA1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA1: 440>
    Quantity_NOC_SIENNA2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA2: 441>
    Quantity_NOC_SIENNA3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA3: 442>
    Quantity_NOC_SIENNA4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA4: 443>
    Quantity_NOC_SKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE: 444>
    Quantity_NOC_SKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE1: 445>
    Quantity_NOC_SKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE2: 446>
    Quantity_NOC_SKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE3: 447>
    Quantity_NOC_SKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE4: 448>
    Quantity_NOC_SLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE: 449>
    Quantity_NOC_SLATEBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1: 450>
    Quantity_NOC_SLATEBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2: 451>
    Quantity_NOC_SLATEBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3: 452>
    Quantity_NOC_SLATEBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4: 453>
    Quantity_NOC_SLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY: 458>
    Quantity_NOC_SLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1: 454>
    Quantity_NOC_SLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2: 455>
    Quantity_NOC_SLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3: 456>
    Quantity_NOC_SLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4: 457>
    Quantity_NOC_SNOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW: 459>
    Quantity_NOC_SNOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW2: 460>
    Quantity_NOC_SNOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW3: 461>
    Quantity_NOC_SNOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW4: 462>
    Quantity_NOC_SPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN: 463>
    Quantity_NOC_SPRINGGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2: 464>
    Quantity_NOC_SPRINGGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3: 465>
    Quantity_NOC_SPRINGGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4: 466>
    Quantity_NOC_STEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE: 467>
    Quantity_NOC_STEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE1: 468>
    Quantity_NOC_STEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE2: 469>
    Quantity_NOC_STEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE3: 470>
    Quantity_NOC_STEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE4: 471>
    Quantity_NOC_TAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN: 472>
    Quantity_NOC_TAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN1: 473>
    Quantity_NOC_TAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN2: 474>
    Quantity_NOC_TAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN3: 475>
    Quantity_NOC_TAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN4: 476>
    Quantity_NOC_TEAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TEAL: 438>
    Quantity_NOC_THISTLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE: 477>
    Quantity_NOC_THISTLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE1: 478>
    Quantity_NOC_THISTLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE2: 479>
    Quantity_NOC_THISTLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE3: 480>
    Quantity_NOC_THISTLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE4: 481>
    Quantity_NOC_TOMATO: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>
    Quantity_NOC_TOMATO1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>
    Quantity_NOC_TOMATO2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO2: 483>
    Quantity_NOC_TOMATO3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO3: 484>
    Quantity_NOC_TOMATO4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO4: 485>
    Quantity_NOC_TURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE: 486>
    Quantity_NOC_TURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE1: 487>
    Quantity_NOC_TURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE2: 488>
    Quantity_NOC_TURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE3: 489>
    Quantity_NOC_TURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE4: 490>
    Quantity_NOC_VIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLET: 491>
    Quantity_NOC_VIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED: 492>
    Quantity_NOC_VIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED1: 493>
    Quantity_NOC_VIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED2: 494>
    Quantity_NOC_VIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED3: 495>
    Quantity_NOC_VIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED4: 496>
    Quantity_NOC_WHEAT: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT: 497>
    Quantity_NOC_WHEAT1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT1: 498>
    Quantity_NOC_WHEAT2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT2: 499>
    Quantity_NOC_WHEAT3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT3: 500>
    Quantity_NOC_WHEAT4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT4: 501>
    Quantity_NOC_WHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHITE: 508>
    Quantity_NOC_WHITESMOKE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHITESMOKE: 502>
    Quantity_NOC_YELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>
    Quantity_NOC_YELLOW1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>
    Quantity_NOC_YELLOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW2: 504>
    Quantity_NOC_YELLOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW3: 505>
    Quantity_NOC_YELLOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW4: 506>
    Quantity_NOC_YELLOWGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN: 507>
    __entries: dict # value = {'Quantity_NOC_BLACK': (<Quantity_NameOfColor.Quantity_NOC_BLACK: 0>, None), 'Quantity_NOC_MATRABLUE': (<Quantity_NameOfColor.Quantity_NOC_MATRABLUE: 1>, None), 'Quantity_NOC_MATRAGRAY': (<Quantity_NameOfColor.Quantity_NOC_MATRAGRAY: 2>, None), 'Quantity_NOC_ALICEBLUE': (<Quantity_NameOfColor.Quantity_NOC_ALICEBLUE: 3>, None), 'Quantity_NOC_ANTIQUEWHITE': (<Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE: 4>, None), 'Quantity_NOC_ANTIQUEWHITE1': (<Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1: 5>, None), 'Quantity_NOC_ANTIQUEWHITE2': (<Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2: 6>, None), 'Quantity_NOC_ANTIQUEWHITE3': (<Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3: 7>, None), 'Quantity_NOC_ANTIQUEWHITE4': (<Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4: 8>, None), 'Quantity_NOC_AQUAMARINE1': (<Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1: 9>, None), 'Quantity_NOC_AQUAMARINE2': (<Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2: 10>, None), 'Quantity_NOC_AQUAMARINE4': (<Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4: 11>, None), 'Quantity_NOC_AZURE': (<Quantity_NameOfColor.Quantity_NOC_AZURE: 12>, None), 'Quantity_NOC_AZURE2': (<Quantity_NameOfColor.Quantity_NOC_AZURE2: 13>, None), 'Quantity_NOC_AZURE3': (<Quantity_NameOfColor.Quantity_NOC_AZURE3: 14>, None), 'Quantity_NOC_AZURE4': (<Quantity_NameOfColor.Quantity_NOC_AZURE4: 15>, None), 'Quantity_NOC_BEIGE': (<Quantity_NameOfColor.Quantity_NOC_BEIGE: 16>, None), 'Quantity_NOC_BISQUE': (<Quantity_NameOfColor.Quantity_NOC_BISQUE: 17>, None), 'Quantity_NOC_BISQUE2': (<Quantity_NameOfColor.Quantity_NOC_BISQUE2: 18>, None), 'Quantity_NOC_BISQUE3': (<Quantity_NameOfColor.Quantity_NOC_BISQUE3: 19>, None), 'Quantity_NOC_BISQUE4': (<Quantity_NameOfColor.Quantity_NOC_BISQUE4: 20>, None), 'Quantity_NOC_BLANCHEDALMOND': (<Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND: 21>, None), 'Quantity_NOC_BLUE': (<Quantity_NameOfColor.Quantity_NOC_BLUE: 22>, None), 'Quantity_NOC_BLUE1': (<Quantity_NameOfColor.Quantity_NOC_BLUE: 22>, None), 'Quantity_NOC_BLUE2': (<Quantity_NameOfColor.Quantity_NOC_BLUE2: 23>, None), 'Quantity_NOC_BLUE3': (<Quantity_NameOfColor.Quantity_NOC_BLUE3: 24>, None), 'Quantity_NOC_BLUE4': (<Quantity_NameOfColor.Quantity_NOC_BLUE4: 25>, None), 'Quantity_NOC_BLUEVIOLET': (<Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET: 26>, None), 'Quantity_NOC_BROWN': (<Quantity_NameOfColor.Quantity_NOC_BROWN: 27>, None), 'Quantity_NOC_BROWN1': (<Quantity_NameOfColor.Quantity_NOC_BROWN1: 28>, None), 'Quantity_NOC_BROWN2': (<Quantity_NameOfColor.Quantity_NOC_BROWN2: 29>, None), 'Quantity_NOC_BROWN3': (<Quantity_NameOfColor.Quantity_NOC_BROWN3: 30>, None), 'Quantity_NOC_BROWN4': (<Quantity_NameOfColor.Quantity_NOC_BROWN4: 31>, None), 'Quantity_NOC_BURLYWOOD': (<Quantity_NameOfColor.Quantity_NOC_BURLYWOOD: 32>, None), 'Quantity_NOC_BURLYWOOD1': (<Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1: 33>, None), 'Quantity_NOC_BURLYWOOD2': (<Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2: 34>, None), 'Quantity_NOC_BURLYWOOD3': (<Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3: 35>, None), 'Quantity_NOC_BURLYWOOD4': (<Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4: 36>, None), 'Quantity_NOC_CADETBLUE': (<Quantity_NameOfColor.Quantity_NOC_CADETBLUE: 37>, None), 'Quantity_NOC_CADETBLUE1': (<Quantity_NameOfColor.Quantity_NOC_CADETBLUE1: 38>, None), 'Quantity_NOC_CADETBLUE2': (<Quantity_NameOfColor.Quantity_NOC_CADETBLUE2: 39>, None), 'Quantity_NOC_CADETBLUE3': (<Quantity_NameOfColor.Quantity_NOC_CADETBLUE3: 40>, None), 'Quantity_NOC_CADETBLUE4': (<Quantity_NameOfColor.Quantity_NOC_CADETBLUE4: 41>, None), 'Quantity_NOC_CHARTREUSE': (<Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>, None), 'Quantity_NOC_CHARTREUSE1': (<Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>, None), 'Quantity_NOC_CHARTREUSE2': (<Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2: 43>, None), 'Quantity_NOC_CHARTREUSE3': (<Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3: 44>, None), 'Quantity_NOC_CHARTREUSE4': (<Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4: 45>, None), 'Quantity_NOC_CHOCOLATE': (<Quantity_NameOfColor.Quantity_NOC_CHOCOLATE: 46>, None), 'Quantity_NOC_CHOCOLATE1': (<Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1: 47>, None), 'Quantity_NOC_CHOCOLATE2': (<Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2: 48>, None), 'Quantity_NOC_CHOCOLATE3': (<Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3: 49>, None), 'Quantity_NOC_CHOCOLATE4': (<Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4: 50>, None), 'Quantity_NOC_CORAL': (<Quantity_NameOfColor.Quantity_NOC_CORAL: 51>, None), 'Quantity_NOC_CORAL1': (<Quantity_NameOfColor.Quantity_NOC_CORAL1: 52>, None), 'Quantity_NOC_CORAL2': (<Quantity_NameOfColor.Quantity_NOC_CORAL2: 53>, None), 'Quantity_NOC_CORAL3': (<Quantity_NameOfColor.Quantity_NOC_CORAL3: 54>, None), 'Quantity_NOC_CORAL4': (<Quantity_NameOfColor.Quantity_NOC_CORAL4: 55>, None), 'Quantity_NOC_CORNFLOWERBLUE': (<Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE: 56>, None), 'Quantity_NOC_CORNSILK1': (<Quantity_NameOfColor.Quantity_NOC_CORNSILK1: 57>, None), 'Quantity_NOC_CORNSILK2': (<Quantity_NameOfColor.Quantity_NOC_CORNSILK2: 58>, None), 'Quantity_NOC_CORNSILK3': (<Quantity_NameOfColor.Quantity_NOC_CORNSILK3: 59>, None), 'Quantity_NOC_CORNSILK4': (<Quantity_NameOfColor.Quantity_NOC_CORNSILK4: 60>, None), 'Quantity_NOC_CYAN': (<Quantity_NameOfColor.Quantity_NOC_CYAN: 61>, None), 'Quantity_NOC_CYAN1': (<Quantity_NameOfColor.Quantity_NOC_CYAN: 61>, None), 'Quantity_NOC_CYAN2': (<Quantity_NameOfColor.Quantity_NOC_CYAN2: 62>, None), 'Quantity_NOC_CYAN3': (<Quantity_NameOfColor.Quantity_NOC_CYAN3: 63>, None), 'Quantity_NOC_CYAN4': (<Quantity_NameOfColor.Quantity_NOC_CYAN4: 64>, None), 'Quantity_NOC_DARKGOLDENROD': (<Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD: 65>, None), 'Quantity_NOC_DARKGOLDENROD1': (<Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1: 66>, None), 'Quantity_NOC_DARKGOLDENROD2': (<Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2: 67>, None), 'Quantity_NOC_DARKGOLDENROD3': (<Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3: 68>, None), 'Quantity_NOC_DARKGOLDENROD4': (<Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4: 69>, None), 'Quantity_NOC_DARKGREEN': (<Quantity_NameOfColor.Quantity_NOC_DARKGREEN: 70>, None), 'Quantity_NOC_DARKKHAKI': (<Quantity_NameOfColor.Quantity_NOC_DARKKHAKI: 71>, None), 'Quantity_NOC_DARKOLIVEGREEN': (<Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN: 72>, None), 'Quantity_NOC_DARKOLIVEGREEN1': (<Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1: 73>, None), 'Quantity_NOC_DARKOLIVEGREEN2': (<Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2: 74>, None), 'Quantity_NOC_DARKOLIVEGREEN3': (<Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3: 75>, None), 'Quantity_NOC_DARKOLIVEGREEN4': (<Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4: 76>, None), 'Quantity_NOC_DARKORANGE': (<Quantity_NameOfColor.Quantity_NOC_DARKORANGE: 77>, None), 'Quantity_NOC_DARKORANGE1': (<Quantity_NameOfColor.Quantity_NOC_DARKORANGE1: 78>, None), 'Quantity_NOC_DARKORANGE2': (<Quantity_NameOfColor.Quantity_NOC_DARKORANGE2: 79>, None), 'Quantity_NOC_DARKORANGE3': (<Quantity_NameOfColor.Quantity_NOC_DARKORANGE3: 80>, None), 'Quantity_NOC_DARKORANGE4': (<Quantity_NameOfColor.Quantity_NOC_DARKORANGE4: 81>, None), 'Quantity_NOC_DARKORCHID': (<Quantity_NameOfColor.Quantity_NOC_DARKORCHID: 82>, None), 'Quantity_NOC_DARKORCHID1': (<Quantity_NameOfColor.Quantity_NOC_DARKORCHID1: 83>, None), 'Quantity_NOC_DARKORCHID2': (<Quantity_NameOfColor.Quantity_NOC_DARKORCHID2: 84>, None), 'Quantity_NOC_DARKORCHID3': (<Quantity_NameOfColor.Quantity_NOC_DARKORCHID3: 85>, None), 'Quantity_NOC_DARKORCHID4': (<Quantity_NameOfColor.Quantity_NOC_DARKORCHID4: 86>, None), 'Quantity_NOC_DARKSALMON': (<Quantity_NameOfColor.Quantity_NOC_DARKSALMON: 87>, None), 'Quantity_NOC_DARKSEAGREEN': (<Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN: 88>, None), 'Quantity_NOC_DARKSEAGREEN1': (<Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1: 89>, None), 'Quantity_NOC_DARKSEAGREEN2': (<Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2: 90>, None), 'Quantity_NOC_DARKSEAGREEN3': (<Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3: 91>, None), 'Quantity_NOC_DARKSEAGREEN4': (<Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4: 92>, None), 'Quantity_NOC_DARKSLATEBLUE': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE: 93>, None), 'Quantity_NOC_DARKSLATEGRAY1': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1: 94>, None), 'Quantity_NOC_DARKSLATEGRAY2': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2: 95>, None), 'Quantity_NOC_DARKSLATEGRAY3': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3: 96>, None), 'Quantity_NOC_DARKSLATEGRAY4': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4: 97>, None), 'Quantity_NOC_DARKSLATEGRAY': (<Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY: 98>, None), 'Quantity_NOC_DARKTURQUOISE': (<Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE: 99>, None), 'Quantity_NOC_DARKVIOLET': (<Quantity_NameOfColor.Quantity_NOC_DARKVIOLET: 100>, None), 'Quantity_NOC_DEEPPINK': (<Quantity_NameOfColor.Quantity_NOC_DEEPPINK: 101>, None), 'Quantity_NOC_DEEPPINK2': (<Quantity_NameOfColor.Quantity_NOC_DEEPPINK2: 102>, None), 'Quantity_NOC_DEEPPINK3': (<Quantity_NameOfColor.Quantity_NOC_DEEPPINK3: 103>, None), 'Quantity_NOC_DEEPPINK4': (<Quantity_NameOfColor.Quantity_NOC_DEEPPINK4: 104>, None), 'Quantity_NOC_DEEPSKYBLUE1': (<Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1: 105>, None), 'Quantity_NOC_DEEPSKYBLUE2': (<Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2: 106>, None), 'Quantity_NOC_DEEPSKYBLUE3': (<Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3: 107>, None), 'Quantity_NOC_DEEPSKYBLUE4': (<Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4: 108>, None), 'Quantity_NOC_DODGERBLUE1': (<Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1: 109>, None), 'Quantity_NOC_DODGERBLUE2': (<Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2: 110>, None), 'Quantity_NOC_DODGERBLUE3': (<Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3: 111>, None), 'Quantity_NOC_DODGERBLUE4': (<Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4: 112>, None), 'Quantity_NOC_FIREBRICK': (<Quantity_NameOfColor.Quantity_NOC_FIREBRICK: 113>, None), 'Quantity_NOC_FIREBRICK1': (<Quantity_NameOfColor.Quantity_NOC_FIREBRICK1: 114>, None), 'Quantity_NOC_FIREBRICK2': (<Quantity_NameOfColor.Quantity_NOC_FIREBRICK2: 115>, None), 'Quantity_NOC_FIREBRICK3': (<Quantity_NameOfColor.Quantity_NOC_FIREBRICK3: 116>, None), 'Quantity_NOC_FIREBRICK4': (<Quantity_NameOfColor.Quantity_NOC_FIREBRICK4: 117>, None), 'Quantity_NOC_FLORALWHITE': (<Quantity_NameOfColor.Quantity_NOC_FLORALWHITE: 118>, None), 'Quantity_NOC_FORESTGREEN': (<Quantity_NameOfColor.Quantity_NOC_FORESTGREEN: 119>, None), 'Quantity_NOC_GAINSBORO': (<Quantity_NameOfColor.Quantity_NOC_GAINSBORO: 120>, None), 'Quantity_NOC_GHOSTWHITE': (<Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE: 121>, None), 'Quantity_NOC_GOLD': (<Quantity_NameOfColor.Quantity_NOC_GOLD: 122>, None), 'Quantity_NOC_GOLD1': (<Quantity_NameOfColor.Quantity_NOC_GOLD: 122>, None), 'Quantity_NOC_GOLD2': (<Quantity_NameOfColor.Quantity_NOC_GOLD2: 123>, None), 'Quantity_NOC_GOLD3': (<Quantity_NameOfColor.Quantity_NOC_GOLD3: 124>, None), 'Quantity_NOC_GOLD4': (<Quantity_NameOfColor.Quantity_NOC_GOLD4: 125>, None), 'Quantity_NOC_GOLDENROD': (<Quantity_NameOfColor.Quantity_NOC_GOLDENROD: 126>, None), 'Quantity_NOC_GOLDENROD1': (<Quantity_NameOfColor.Quantity_NOC_GOLDENROD1: 127>, None), 'Quantity_NOC_GOLDENROD2': (<Quantity_NameOfColor.Quantity_NOC_GOLDENROD2: 128>, None), 'Quantity_NOC_GOLDENROD3': (<Quantity_NameOfColor.Quantity_NOC_GOLDENROD3: 129>, None), 'Quantity_NOC_GOLDENROD4': (<Quantity_NameOfColor.Quantity_NOC_GOLDENROD4: 130>, None), 'Quantity_NOC_GRAY': (<Quantity_NameOfColor.Quantity_NOC_GRAY: 131>, None), 'Quantity_NOC_GRAY0': (<Quantity_NameOfColor.Quantity_NOC_GRAY0: 132>, None), 'Quantity_NOC_GRAY1': (<Quantity_NameOfColor.Quantity_NOC_GRAY1: 133>, None), 'Quantity_NOC_GRAY2': (<Quantity_NameOfColor.Quantity_NOC_GRAY2: 134>, None), 'Quantity_NOC_GRAY3': (<Quantity_NameOfColor.Quantity_NOC_GRAY3: 135>, None), 'Quantity_NOC_GRAY4': (<Quantity_NameOfColor.Quantity_NOC_GRAY4: 136>, None), 'Quantity_NOC_GRAY5': (<Quantity_NameOfColor.Quantity_NOC_GRAY5: 137>, None), 'Quantity_NOC_GRAY6': (<Quantity_NameOfColor.Quantity_NOC_GRAY6: 138>, None), 'Quantity_NOC_GRAY7': (<Quantity_NameOfColor.Quantity_NOC_GRAY7: 139>, None), 'Quantity_NOC_GRAY8': (<Quantity_NameOfColor.Quantity_NOC_GRAY8: 140>, None), 'Quantity_NOC_GRAY9': (<Quantity_NameOfColor.Quantity_NOC_GRAY9: 141>, None), 'Quantity_NOC_GRAY10': (<Quantity_NameOfColor.Quantity_NOC_GRAY10: 142>, None), 'Quantity_NOC_GRAY11': (<Quantity_NameOfColor.Quantity_NOC_GRAY11: 143>, None), 'Quantity_NOC_GRAY12': (<Quantity_NameOfColor.Quantity_NOC_GRAY12: 144>, None), 'Quantity_NOC_GRAY13': (<Quantity_NameOfColor.Quantity_NOC_GRAY13: 145>, None), 'Quantity_NOC_GRAY14': (<Quantity_NameOfColor.Quantity_NOC_GRAY14: 146>, None), 'Quantity_NOC_GRAY15': (<Quantity_NameOfColor.Quantity_NOC_GRAY15: 147>, None), 'Quantity_NOC_GRAY16': (<Quantity_NameOfColor.Quantity_NOC_GRAY16: 148>, None), 'Quantity_NOC_GRAY17': (<Quantity_NameOfColor.Quantity_NOC_GRAY17: 149>, None), 'Quantity_NOC_GRAY18': (<Quantity_NameOfColor.Quantity_NOC_GRAY18: 150>, None), 'Quantity_NOC_GRAY19': (<Quantity_NameOfColor.Quantity_NOC_GRAY19: 151>, None), 'Quantity_NOC_GRAY20': (<Quantity_NameOfColor.Quantity_NOC_GRAY20: 152>, None), 'Quantity_NOC_GRAY21': (<Quantity_NameOfColor.Quantity_NOC_GRAY21: 153>, None), 'Quantity_NOC_GRAY22': (<Quantity_NameOfColor.Quantity_NOC_GRAY22: 154>, None), 'Quantity_NOC_GRAY23': (<Quantity_NameOfColor.Quantity_NOC_GRAY23: 155>, None), 'Quantity_NOC_GRAY24': (<Quantity_NameOfColor.Quantity_NOC_GRAY24: 156>, None), 'Quantity_NOC_GRAY25': (<Quantity_NameOfColor.Quantity_NOC_GRAY25: 157>, None), 'Quantity_NOC_GRAY26': (<Quantity_NameOfColor.Quantity_NOC_GRAY26: 158>, None), 'Quantity_NOC_GRAY27': (<Quantity_NameOfColor.Quantity_NOC_GRAY27: 159>, None), 'Quantity_NOC_GRAY28': (<Quantity_NameOfColor.Quantity_NOC_GRAY28: 160>, None), 'Quantity_NOC_GRAY29': (<Quantity_NameOfColor.Quantity_NOC_GRAY29: 161>, None), 'Quantity_NOC_GRAY30': (<Quantity_NameOfColor.Quantity_NOC_GRAY30: 162>, None), 'Quantity_NOC_GRAY31': (<Quantity_NameOfColor.Quantity_NOC_GRAY31: 163>, None), 'Quantity_NOC_GRAY32': (<Quantity_NameOfColor.Quantity_NOC_GRAY32: 164>, None), 'Quantity_NOC_GRAY33': (<Quantity_NameOfColor.Quantity_NOC_GRAY33: 165>, None), 'Quantity_NOC_GRAY34': (<Quantity_NameOfColor.Quantity_NOC_GRAY34: 166>, None), 'Quantity_NOC_GRAY35': (<Quantity_NameOfColor.Quantity_NOC_GRAY35: 167>, None), 'Quantity_NOC_GRAY36': (<Quantity_NameOfColor.Quantity_NOC_GRAY36: 168>, None), 'Quantity_NOC_GRAY37': (<Quantity_NameOfColor.Quantity_NOC_GRAY37: 169>, None), 'Quantity_NOC_GRAY38': (<Quantity_NameOfColor.Quantity_NOC_GRAY38: 170>, None), 'Quantity_NOC_GRAY39': (<Quantity_NameOfColor.Quantity_NOC_GRAY39: 171>, None), 'Quantity_NOC_GRAY40': (<Quantity_NameOfColor.Quantity_NOC_GRAY40: 172>, None), 'Quantity_NOC_GRAY41': (<Quantity_NameOfColor.Quantity_NOC_GRAY41: 173>, None), 'Quantity_NOC_GRAY42': (<Quantity_NameOfColor.Quantity_NOC_GRAY42: 174>, None), 'Quantity_NOC_GRAY43': (<Quantity_NameOfColor.Quantity_NOC_GRAY43: 175>, None), 'Quantity_NOC_GRAY44': (<Quantity_NameOfColor.Quantity_NOC_GRAY44: 176>, None), 'Quantity_NOC_GRAY45': (<Quantity_NameOfColor.Quantity_NOC_GRAY45: 177>, None), 'Quantity_NOC_GRAY46': (<Quantity_NameOfColor.Quantity_NOC_GRAY46: 178>, None), 'Quantity_NOC_GRAY47': (<Quantity_NameOfColor.Quantity_NOC_GRAY47: 179>, None), 'Quantity_NOC_GRAY48': (<Quantity_NameOfColor.Quantity_NOC_GRAY48: 180>, None), 'Quantity_NOC_GRAY49': (<Quantity_NameOfColor.Quantity_NOC_GRAY49: 181>, None), 'Quantity_NOC_GRAY50': (<Quantity_NameOfColor.Quantity_NOC_GRAY50: 182>, None), 'Quantity_NOC_GRAY51': (<Quantity_NameOfColor.Quantity_NOC_GRAY51: 183>, None), 'Quantity_NOC_GRAY52': (<Quantity_NameOfColor.Quantity_NOC_GRAY52: 184>, None), 'Quantity_NOC_GRAY53': (<Quantity_NameOfColor.Quantity_NOC_GRAY53: 185>, None), 'Quantity_NOC_GRAY54': (<Quantity_NameOfColor.Quantity_NOC_GRAY54: 186>, None), 'Quantity_NOC_GRAY55': (<Quantity_NameOfColor.Quantity_NOC_GRAY55: 187>, None), 'Quantity_NOC_GRAY56': (<Quantity_NameOfColor.Quantity_NOC_GRAY56: 188>, None), 'Quantity_NOC_GRAY57': (<Quantity_NameOfColor.Quantity_NOC_GRAY57: 189>, None), 'Quantity_NOC_GRAY58': (<Quantity_NameOfColor.Quantity_NOC_GRAY58: 190>, None), 'Quantity_NOC_GRAY59': (<Quantity_NameOfColor.Quantity_NOC_GRAY59: 191>, None), 'Quantity_NOC_GRAY60': (<Quantity_NameOfColor.Quantity_NOC_GRAY60: 192>, None), 'Quantity_NOC_GRAY61': (<Quantity_NameOfColor.Quantity_NOC_GRAY61: 193>, None), 'Quantity_NOC_GRAY62': (<Quantity_NameOfColor.Quantity_NOC_GRAY62: 194>, None), 'Quantity_NOC_GRAY63': (<Quantity_NameOfColor.Quantity_NOC_GRAY63: 195>, None), 'Quantity_NOC_GRAY64': (<Quantity_NameOfColor.Quantity_NOC_GRAY64: 196>, None), 'Quantity_NOC_GRAY65': (<Quantity_NameOfColor.Quantity_NOC_GRAY65: 197>, None), 'Quantity_NOC_GRAY66': (<Quantity_NameOfColor.Quantity_NOC_GRAY66: 198>, None), 'Quantity_NOC_GRAY67': (<Quantity_NameOfColor.Quantity_NOC_GRAY67: 199>, None), 'Quantity_NOC_GRAY68': (<Quantity_NameOfColor.Quantity_NOC_GRAY68: 200>, None), 'Quantity_NOC_GRAY69': (<Quantity_NameOfColor.Quantity_NOC_GRAY69: 201>, None), 'Quantity_NOC_GRAY70': (<Quantity_NameOfColor.Quantity_NOC_GRAY70: 202>, None), 'Quantity_NOC_GRAY71': (<Quantity_NameOfColor.Quantity_NOC_GRAY71: 203>, None), 'Quantity_NOC_GRAY72': (<Quantity_NameOfColor.Quantity_NOC_GRAY72: 204>, None), 'Quantity_NOC_GRAY73': (<Quantity_NameOfColor.Quantity_NOC_GRAY73: 205>, None), 'Quantity_NOC_GRAY74': (<Quantity_NameOfColor.Quantity_NOC_GRAY74: 206>, None), 'Quantity_NOC_GRAY75': (<Quantity_NameOfColor.Quantity_NOC_GRAY75: 207>, None), 'Quantity_NOC_GRAY76': (<Quantity_NameOfColor.Quantity_NOC_GRAY76: 208>, None), 'Quantity_NOC_GRAY77': (<Quantity_NameOfColor.Quantity_NOC_GRAY77: 209>, None), 'Quantity_NOC_GRAY78': (<Quantity_NameOfColor.Quantity_NOC_GRAY78: 210>, None), 'Quantity_NOC_GRAY79': (<Quantity_NameOfColor.Quantity_NOC_GRAY79: 211>, None), 'Quantity_NOC_GRAY80': (<Quantity_NameOfColor.Quantity_NOC_GRAY80: 212>, None), 'Quantity_NOC_GRAY81': (<Quantity_NameOfColor.Quantity_NOC_GRAY81: 213>, None), 'Quantity_NOC_GRAY82': (<Quantity_NameOfColor.Quantity_NOC_GRAY82: 214>, None), 'Quantity_NOC_GRAY83': (<Quantity_NameOfColor.Quantity_NOC_GRAY83: 215>, None), 'Quantity_NOC_GRAY85': (<Quantity_NameOfColor.Quantity_NOC_GRAY85: 216>, None), 'Quantity_NOC_GRAY86': (<Quantity_NameOfColor.Quantity_NOC_GRAY86: 217>, None), 'Quantity_NOC_GRAY87': (<Quantity_NameOfColor.Quantity_NOC_GRAY87: 218>, None), 'Quantity_NOC_GRAY88': (<Quantity_NameOfColor.Quantity_NOC_GRAY88: 219>, None), 'Quantity_NOC_GRAY89': (<Quantity_NameOfColor.Quantity_NOC_GRAY89: 220>, None), 'Quantity_NOC_GRAY90': (<Quantity_NameOfColor.Quantity_NOC_GRAY90: 221>, None), 'Quantity_NOC_GRAY91': (<Quantity_NameOfColor.Quantity_NOC_GRAY91: 222>, None), 'Quantity_NOC_GRAY92': (<Quantity_NameOfColor.Quantity_NOC_GRAY92: 223>, None), 'Quantity_NOC_GRAY93': (<Quantity_NameOfColor.Quantity_NOC_GRAY93: 224>, None), 'Quantity_NOC_GRAY94': (<Quantity_NameOfColor.Quantity_NOC_GRAY94: 225>, None), 'Quantity_NOC_GRAY95': (<Quantity_NameOfColor.Quantity_NOC_GRAY95: 226>, None), 'Quantity_NOC_GRAY97': (<Quantity_NameOfColor.Quantity_NOC_GRAY97: 227>, None), 'Quantity_NOC_GRAY98': (<Quantity_NameOfColor.Quantity_NOC_GRAY98: 228>, None), 'Quantity_NOC_GRAY99': (<Quantity_NameOfColor.Quantity_NOC_GRAY99: 229>, None), 'Quantity_NOC_GREEN': (<Quantity_NameOfColor.Quantity_NOC_GREEN: 230>, None), 'Quantity_NOC_GREEN1': (<Quantity_NameOfColor.Quantity_NOC_GREEN: 230>, None), 'Quantity_NOC_GREEN2': (<Quantity_NameOfColor.Quantity_NOC_GREEN2: 231>, None), 'Quantity_NOC_GREEN3': (<Quantity_NameOfColor.Quantity_NOC_GREEN3: 232>, None), 'Quantity_NOC_GREEN4': (<Quantity_NameOfColor.Quantity_NOC_GREEN4: 233>, None), 'Quantity_NOC_GREENYELLOW': (<Quantity_NameOfColor.Quantity_NOC_GREENYELLOW: 234>, None), 'Quantity_NOC_HONEYDEW': (<Quantity_NameOfColor.Quantity_NOC_HONEYDEW: 235>, None), 'Quantity_NOC_HONEYDEW2': (<Quantity_NameOfColor.Quantity_NOC_HONEYDEW2: 236>, None), 'Quantity_NOC_HONEYDEW3': (<Quantity_NameOfColor.Quantity_NOC_HONEYDEW3: 237>, None), 'Quantity_NOC_HONEYDEW4': (<Quantity_NameOfColor.Quantity_NOC_HONEYDEW4: 238>, None), 'Quantity_NOC_HOTPINK': (<Quantity_NameOfColor.Quantity_NOC_HOTPINK: 239>, None), 'Quantity_NOC_HOTPINK1': (<Quantity_NameOfColor.Quantity_NOC_HOTPINK1: 240>, None), 'Quantity_NOC_HOTPINK2': (<Quantity_NameOfColor.Quantity_NOC_HOTPINK2: 241>, None), 'Quantity_NOC_HOTPINK3': (<Quantity_NameOfColor.Quantity_NOC_HOTPINK3: 242>, None), 'Quantity_NOC_HOTPINK4': (<Quantity_NameOfColor.Quantity_NOC_HOTPINK4: 243>, None), 'Quantity_NOC_INDIANRED': (<Quantity_NameOfColor.Quantity_NOC_INDIANRED: 244>, None), 'Quantity_NOC_INDIANRED1': (<Quantity_NameOfColor.Quantity_NOC_INDIANRED1: 245>, None), 'Quantity_NOC_INDIANRED2': (<Quantity_NameOfColor.Quantity_NOC_INDIANRED2: 246>, None), 'Quantity_NOC_INDIANRED3': (<Quantity_NameOfColor.Quantity_NOC_INDIANRED3: 247>, None), 'Quantity_NOC_INDIANRED4': (<Quantity_NameOfColor.Quantity_NOC_INDIANRED4: 248>, None), 'Quantity_NOC_IVORY': (<Quantity_NameOfColor.Quantity_NOC_IVORY: 249>, None), 'Quantity_NOC_IVORY2': (<Quantity_NameOfColor.Quantity_NOC_IVORY2: 250>, None), 'Quantity_NOC_IVORY3': (<Quantity_NameOfColor.Quantity_NOC_IVORY3: 251>, None), 'Quantity_NOC_IVORY4': (<Quantity_NameOfColor.Quantity_NOC_IVORY4: 252>, None), 'Quantity_NOC_KHAKI': (<Quantity_NameOfColor.Quantity_NOC_KHAKI: 253>, None), 'Quantity_NOC_KHAKI1': (<Quantity_NameOfColor.Quantity_NOC_KHAKI1: 254>, None), 'Quantity_NOC_KHAKI2': (<Quantity_NameOfColor.Quantity_NOC_KHAKI2: 255>, None), 'Quantity_NOC_KHAKI3': (<Quantity_NameOfColor.Quantity_NOC_KHAKI3: 256>, None), 'Quantity_NOC_KHAKI4': (<Quantity_NameOfColor.Quantity_NOC_KHAKI4: 257>, None), 'Quantity_NOC_LAVENDER': (<Quantity_NameOfColor.Quantity_NOC_LAVENDER: 258>, None), 'Quantity_NOC_LAVENDERBLUSH1': (<Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1: 259>, None), 'Quantity_NOC_LAVENDERBLUSH2': (<Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2: 260>, None), 'Quantity_NOC_LAVENDERBLUSH3': (<Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3: 261>, None), 'Quantity_NOC_LAVENDERBLUSH4': (<Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4: 262>, None), 'Quantity_NOC_LAWNGREEN': (<Quantity_NameOfColor.Quantity_NOC_LAWNGREEN: 263>, None), 'Quantity_NOC_LEMONCHIFFON1': (<Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1: 264>, None), 'Quantity_NOC_LEMONCHIFFON2': (<Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2: 265>, None), 'Quantity_NOC_LEMONCHIFFON3': (<Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3: 266>, None), 'Quantity_NOC_LEMONCHIFFON4': (<Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4: 267>, None), 'Quantity_NOC_LIGHTBLUE': (<Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE: 268>, None), 'Quantity_NOC_LIGHTBLUE1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1: 269>, None), 'Quantity_NOC_LIGHTBLUE2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2: 270>, None), 'Quantity_NOC_LIGHTBLUE3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3: 271>, None), 'Quantity_NOC_LIGHTBLUE4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4: 272>, None), 'Quantity_NOC_LIGHTCORAL': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL: 273>, None), 'Quantity_NOC_LIGHTCYAN': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>, None), 'Quantity_NOC_LIGHTCYAN1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>, None), 'Quantity_NOC_LIGHTCYAN2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2: 275>, None), 'Quantity_NOC_LIGHTCYAN3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3: 276>, None), 'Quantity_NOC_LIGHTCYAN4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4: 277>, None), 'Quantity_NOC_LIGHTGOLDENROD': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD: 278>, None), 'Quantity_NOC_LIGHTGOLDENROD1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1: 279>, None), 'Quantity_NOC_LIGHTGOLDENROD2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2: 280>, None), 'Quantity_NOC_LIGHTGOLDENROD3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3: 281>, None), 'Quantity_NOC_LIGHTGOLDENROD4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4: 282>, None), 'Quantity_NOC_LIGHTGOLDENRODYELLOW': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW: 283>, None), 'Quantity_NOC_LIGHTGRAY': (<Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY: 284>, None), 'Quantity_NOC_LIGHTPINK': (<Quantity_NameOfColor.Quantity_NOC_LIGHTPINK: 285>, None), 'Quantity_NOC_LIGHTPINK1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1: 286>, None), 'Quantity_NOC_LIGHTPINK2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2: 287>, None), 'Quantity_NOC_LIGHTPINK3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3: 288>, None), 'Quantity_NOC_LIGHTPINK4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4: 289>, None), 'Quantity_NOC_LIGHTSALMON1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1: 290>, None), 'Quantity_NOC_LIGHTSALMON2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2: 291>, None), 'Quantity_NOC_LIGHTSALMON3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3: 292>, None), 'Quantity_NOC_LIGHTSALMON4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4: 293>, None), 'Quantity_NOC_LIGHTSEAGREEN': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN: 294>, None), 'Quantity_NOC_LIGHTSKYBLUE': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE: 295>, None), 'Quantity_NOC_LIGHTSKYBLUE1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1: 296>, None), 'Quantity_NOC_LIGHTSKYBLUE2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2: 297>, None), 'Quantity_NOC_LIGHTSKYBLUE3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3: 298>, None), 'Quantity_NOC_LIGHTSKYBLUE4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4: 299>, None), 'Quantity_NOC_LIGHTSLATEBLUE': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE: 300>, None), 'Quantity_NOC_LIGHTSLATEGRAY': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY: 301>, None), 'Quantity_NOC_LIGHTSTEELBLUE': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE: 302>, None), 'Quantity_NOC_LIGHTSTEELBLUE1': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1: 303>, None), 'Quantity_NOC_LIGHTSTEELBLUE2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2: 304>, None), 'Quantity_NOC_LIGHTSTEELBLUE3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3: 305>, None), 'Quantity_NOC_LIGHTSTEELBLUE4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4: 306>, None), 'Quantity_NOC_LIGHTYELLOW': (<Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW: 307>, None), 'Quantity_NOC_LIGHTYELLOW2': (<Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2: 308>, None), 'Quantity_NOC_LIGHTYELLOW3': (<Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3: 309>, None), 'Quantity_NOC_LIGHTYELLOW4': (<Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4: 310>, None), 'Quantity_NOC_LIMEGREEN': (<Quantity_NameOfColor.Quantity_NOC_LIMEGREEN: 311>, None), 'Quantity_NOC_LINEN': (<Quantity_NameOfColor.Quantity_NOC_LINEN: 312>, None), 'Quantity_NOC_MAGENTA': (<Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>, None), 'Quantity_NOC_MAGENTA1': (<Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>, None), 'Quantity_NOC_MAGENTA2': (<Quantity_NameOfColor.Quantity_NOC_MAGENTA2: 314>, None), 'Quantity_NOC_MAGENTA3': (<Quantity_NameOfColor.Quantity_NOC_MAGENTA3: 315>, None), 'Quantity_NOC_MAGENTA4': (<Quantity_NameOfColor.Quantity_NOC_MAGENTA4: 316>, None), 'Quantity_NOC_MAROON': (<Quantity_NameOfColor.Quantity_NOC_MAROON: 317>, None), 'Quantity_NOC_MAROON1': (<Quantity_NameOfColor.Quantity_NOC_MAROON1: 318>, None), 'Quantity_NOC_MAROON2': (<Quantity_NameOfColor.Quantity_NOC_MAROON2: 319>, None), 'Quantity_NOC_MAROON3': (<Quantity_NameOfColor.Quantity_NOC_MAROON3: 320>, None), 'Quantity_NOC_MAROON4': (<Quantity_NameOfColor.Quantity_NOC_MAROON4: 321>, None), 'Quantity_NOC_MEDIUMAQUAMARINE': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE: 322>, None), 'Quantity_NOC_MEDIUMORCHID': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID: 323>, None), 'Quantity_NOC_MEDIUMORCHID1': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1: 324>, None), 'Quantity_NOC_MEDIUMORCHID2': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2: 325>, None), 'Quantity_NOC_MEDIUMORCHID3': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3: 326>, None), 'Quantity_NOC_MEDIUMORCHID4': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4: 327>, None), 'Quantity_NOC_MEDIUMPURPLE': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE: 328>, None), 'Quantity_NOC_MEDIUMPURPLE1': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1: 329>, None), 'Quantity_NOC_MEDIUMPURPLE2': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2: 330>, None), 'Quantity_NOC_MEDIUMPURPLE3': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3: 331>, None), 'Quantity_NOC_MEDIUMPURPLE4': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4: 332>, None), 'Quantity_NOC_MEDIUMSEAGREEN': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN: 333>, None), 'Quantity_NOC_MEDIUMSLATEBLUE': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE: 334>, None), 'Quantity_NOC_MEDIUMSPRINGGREEN': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN: 335>, None), 'Quantity_NOC_MEDIUMTURQUOISE': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE: 336>, None), 'Quantity_NOC_MEDIUMVIOLETRED': (<Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED: 337>, None), 'Quantity_NOC_MIDNIGHTBLUE': (<Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE: 338>, None), 'Quantity_NOC_MINTCREAM': (<Quantity_NameOfColor.Quantity_NOC_MINTCREAM: 339>, None), 'Quantity_NOC_MISTYROSE': (<Quantity_NameOfColor.Quantity_NOC_MISTYROSE: 340>, None), 'Quantity_NOC_MISTYROSE2': (<Quantity_NameOfColor.Quantity_NOC_MISTYROSE2: 341>, None), 'Quantity_NOC_MISTYROSE3': (<Quantity_NameOfColor.Quantity_NOC_MISTYROSE3: 342>, None), 'Quantity_NOC_MISTYROSE4': (<Quantity_NameOfColor.Quantity_NOC_MISTYROSE4: 343>, None), 'Quantity_NOC_MOCCASIN': (<Quantity_NameOfColor.Quantity_NOC_MOCCASIN: 344>, None), 'Quantity_NOC_NAVAJOWHITE1': (<Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1: 345>, None), 'Quantity_NOC_NAVAJOWHITE2': (<Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2: 346>, None), 'Quantity_NOC_NAVAJOWHITE3': (<Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3: 347>, None), 'Quantity_NOC_NAVAJOWHITE4': (<Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4: 348>, None), 'Quantity_NOC_NAVYBLUE': (<Quantity_NameOfColor.Quantity_NOC_NAVYBLUE: 349>, None), 'Quantity_NOC_OLDLACE': (<Quantity_NameOfColor.Quantity_NOC_OLDLACE: 350>, None), 'Quantity_NOC_OLIVEDRAB': (<Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB: 351>, None), 'Quantity_NOC_OLIVEDRAB1': (<Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1: 352>, None), 'Quantity_NOC_OLIVEDRAB2': (<Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2: 353>, None), 'Quantity_NOC_OLIVEDRAB3': (<Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3: 354>, None), 'Quantity_NOC_OLIVEDRAB4': (<Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4: 355>, None), 'Quantity_NOC_ORANGE': (<Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>, None), 'Quantity_NOC_ORANGE1': (<Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>, None), 'Quantity_NOC_ORANGE2': (<Quantity_NameOfColor.Quantity_NOC_ORANGE2: 357>, None), 'Quantity_NOC_ORANGE3': (<Quantity_NameOfColor.Quantity_NOC_ORANGE3: 358>, None), 'Quantity_NOC_ORANGE4': (<Quantity_NameOfColor.Quantity_NOC_ORANGE4: 359>, None), 'Quantity_NOC_ORANGERED': (<Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>, None), 'Quantity_NOC_ORANGERED1': (<Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>, None), 'Quantity_NOC_ORANGERED2': (<Quantity_NameOfColor.Quantity_NOC_ORANGERED2: 361>, None), 'Quantity_NOC_ORANGERED3': (<Quantity_NameOfColor.Quantity_NOC_ORANGERED3: 362>, None), 'Quantity_NOC_ORANGERED4': (<Quantity_NameOfColor.Quantity_NOC_ORANGERED4: 363>, None), 'Quantity_NOC_ORCHID': (<Quantity_NameOfColor.Quantity_NOC_ORCHID: 364>, None), 'Quantity_NOC_ORCHID1': (<Quantity_NameOfColor.Quantity_NOC_ORCHID1: 365>, None), 'Quantity_NOC_ORCHID2': (<Quantity_NameOfColor.Quantity_NOC_ORCHID2: 366>, None), 'Quantity_NOC_ORCHID3': (<Quantity_NameOfColor.Quantity_NOC_ORCHID3: 367>, None), 'Quantity_NOC_ORCHID4': (<Quantity_NameOfColor.Quantity_NOC_ORCHID4: 368>, None), 'Quantity_NOC_PALEGOLDENROD': (<Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD: 369>, None), 'Quantity_NOC_PALEGREEN': (<Quantity_NameOfColor.Quantity_NOC_PALEGREEN: 370>, None), 'Quantity_NOC_PALEGREEN1': (<Quantity_NameOfColor.Quantity_NOC_PALEGREEN1: 371>, None), 'Quantity_NOC_PALEGREEN2': (<Quantity_NameOfColor.Quantity_NOC_PALEGREEN2: 372>, None), 'Quantity_NOC_PALEGREEN3': (<Quantity_NameOfColor.Quantity_NOC_PALEGREEN3: 373>, None), 'Quantity_NOC_PALEGREEN4': (<Quantity_NameOfColor.Quantity_NOC_PALEGREEN4: 374>, None), 'Quantity_NOC_PALETURQUOISE': (<Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE: 375>, None), 'Quantity_NOC_PALETURQUOISE1': (<Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1: 376>, None), 'Quantity_NOC_PALETURQUOISE2': (<Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2: 377>, None), 'Quantity_NOC_PALETURQUOISE3': (<Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3: 378>, None), 'Quantity_NOC_PALETURQUOISE4': (<Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4: 379>, None), 'Quantity_NOC_PALEVIOLETRED': (<Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED: 380>, None), 'Quantity_NOC_PALEVIOLETRED1': (<Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1: 381>, None), 'Quantity_NOC_PALEVIOLETRED2': (<Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2: 382>, None), 'Quantity_NOC_PALEVIOLETRED3': (<Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3: 383>, None), 'Quantity_NOC_PALEVIOLETRED4': (<Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4: 384>, None), 'Quantity_NOC_PAPAYAWHIP': (<Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP: 385>, None), 'Quantity_NOC_PEACHPUFF': (<Quantity_NameOfColor.Quantity_NOC_PEACHPUFF: 386>, None), 'Quantity_NOC_PEACHPUFF2': (<Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2: 387>, None), 'Quantity_NOC_PEACHPUFF3': (<Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3: 388>, None), 'Quantity_NOC_PEACHPUFF4': (<Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4: 389>, None), 'Quantity_NOC_PERU': (<Quantity_NameOfColor.Quantity_NOC_PERU: 390>, None), 'Quantity_NOC_PINK': (<Quantity_NameOfColor.Quantity_NOC_PINK: 391>, None), 'Quantity_NOC_PINK1': (<Quantity_NameOfColor.Quantity_NOC_PINK1: 392>, None), 'Quantity_NOC_PINK2': (<Quantity_NameOfColor.Quantity_NOC_PINK2: 393>, None), 'Quantity_NOC_PINK3': (<Quantity_NameOfColor.Quantity_NOC_PINK3: 394>, None), 'Quantity_NOC_PINK4': (<Quantity_NameOfColor.Quantity_NOC_PINK4: 395>, None), 'Quantity_NOC_PLUM': (<Quantity_NameOfColor.Quantity_NOC_PLUM: 396>, None), 'Quantity_NOC_PLUM1': (<Quantity_NameOfColor.Quantity_NOC_PLUM1: 397>, None), 'Quantity_NOC_PLUM2': (<Quantity_NameOfColor.Quantity_NOC_PLUM2: 398>, None), 'Quantity_NOC_PLUM3': (<Quantity_NameOfColor.Quantity_NOC_PLUM3: 399>, None), 'Quantity_NOC_PLUM4': (<Quantity_NameOfColor.Quantity_NOC_PLUM4: 400>, None), 'Quantity_NOC_POWDERBLUE': (<Quantity_NameOfColor.Quantity_NOC_POWDERBLUE: 401>, None), 'Quantity_NOC_PURPLE': (<Quantity_NameOfColor.Quantity_NOC_PURPLE: 402>, None), 'Quantity_NOC_PURPLE1': (<Quantity_NameOfColor.Quantity_NOC_PURPLE1: 403>, None), 'Quantity_NOC_PURPLE2': (<Quantity_NameOfColor.Quantity_NOC_PURPLE2: 404>, None), 'Quantity_NOC_PURPLE3': (<Quantity_NameOfColor.Quantity_NOC_PURPLE3: 405>, None), 'Quantity_NOC_PURPLE4': (<Quantity_NameOfColor.Quantity_NOC_PURPLE4: 406>, None), 'Quantity_NOC_RED': (<Quantity_NameOfColor.Quantity_NOC_RED: 407>, None), 'Quantity_NOC_RED1': (<Quantity_NameOfColor.Quantity_NOC_RED: 407>, None), 'Quantity_NOC_RED2': (<Quantity_NameOfColor.Quantity_NOC_RED2: 408>, None), 'Quantity_NOC_RED3': (<Quantity_NameOfColor.Quantity_NOC_RED3: 409>, None), 'Quantity_NOC_RED4': (<Quantity_NameOfColor.Quantity_NOC_RED4: 410>, None), 'Quantity_NOC_ROSYBROWN': (<Quantity_NameOfColor.Quantity_NOC_ROSYBROWN: 411>, None), 'Quantity_NOC_ROSYBROWN1': (<Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1: 412>, None), 'Quantity_NOC_ROSYBROWN2': (<Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2: 413>, None), 'Quantity_NOC_ROSYBROWN3': (<Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3: 414>, None), 'Quantity_NOC_ROSYBROWN4': (<Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4: 415>, None), 'Quantity_NOC_ROYALBLUE': (<Quantity_NameOfColor.Quantity_NOC_ROYALBLUE: 416>, None), 'Quantity_NOC_ROYALBLUE1': (<Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1: 417>, None), 'Quantity_NOC_ROYALBLUE2': (<Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2: 418>, None), 'Quantity_NOC_ROYALBLUE3': (<Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3: 419>, None), 'Quantity_NOC_ROYALBLUE4': (<Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4: 420>, None), 'Quantity_NOC_SADDLEBROWN': (<Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN: 421>, None), 'Quantity_NOC_SALMON': (<Quantity_NameOfColor.Quantity_NOC_SALMON: 422>, None), 'Quantity_NOC_SALMON1': (<Quantity_NameOfColor.Quantity_NOC_SALMON1: 423>, None), 'Quantity_NOC_SALMON2': (<Quantity_NameOfColor.Quantity_NOC_SALMON2: 424>, None), 'Quantity_NOC_SALMON3': (<Quantity_NameOfColor.Quantity_NOC_SALMON3: 425>, None), 'Quantity_NOC_SALMON4': (<Quantity_NameOfColor.Quantity_NOC_SALMON4: 426>, None), 'Quantity_NOC_SANDYBROWN': (<Quantity_NameOfColor.Quantity_NOC_SANDYBROWN: 427>, None), 'Quantity_NOC_SEAGREEN': (<Quantity_NameOfColor.Quantity_NOC_SEAGREEN: 428>, None), 'Quantity_NOC_SEAGREEN1': (<Quantity_NameOfColor.Quantity_NOC_SEAGREEN1: 429>, None), 'Quantity_NOC_SEAGREEN2': (<Quantity_NameOfColor.Quantity_NOC_SEAGREEN2: 430>, None), 'Quantity_NOC_SEAGREEN3': (<Quantity_NameOfColor.Quantity_NOC_SEAGREEN3: 431>, None), 'Quantity_NOC_SEAGREEN4': (<Quantity_NameOfColor.Quantity_NOC_SEAGREEN4: 432>, None), 'Quantity_NOC_SEASHELL': (<Quantity_NameOfColor.Quantity_NOC_SEASHELL: 433>, None), 'Quantity_NOC_SEASHELL2': (<Quantity_NameOfColor.Quantity_NOC_SEASHELL2: 434>, None), 'Quantity_NOC_SEASHELL3': (<Quantity_NameOfColor.Quantity_NOC_SEASHELL3: 435>, None), 'Quantity_NOC_SEASHELL4': (<Quantity_NameOfColor.Quantity_NOC_SEASHELL4: 436>, None), 'Quantity_NOC_BEET': (<Quantity_NameOfColor.Quantity_NOC_BEET: 437>, None), 'Quantity_NOC_TEAL': (<Quantity_NameOfColor.Quantity_NOC_TEAL: 438>, None), 'Quantity_NOC_SIENNA': (<Quantity_NameOfColor.Quantity_NOC_SIENNA: 439>, None), 'Quantity_NOC_SIENNA1': (<Quantity_NameOfColor.Quantity_NOC_SIENNA1: 440>, None), 'Quantity_NOC_SIENNA2': (<Quantity_NameOfColor.Quantity_NOC_SIENNA2: 441>, None), 'Quantity_NOC_SIENNA3': (<Quantity_NameOfColor.Quantity_NOC_SIENNA3: 442>, None), 'Quantity_NOC_SIENNA4': (<Quantity_NameOfColor.Quantity_NOC_SIENNA4: 443>, None), 'Quantity_NOC_SKYBLUE': (<Quantity_NameOfColor.Quantity_NOC_SKYBLUE: 444>, None), 'Quantity_NOC_SKYBLUE1': (<Quantity_NameOfColor.Quantity_NOC_SKYBLUE1: 445>, None), 'Quantity_NOC_SKYBLUE2': (<Quantity_NameOfColor.Quantity_NOC_SKYBLUE2: 446>, None), 'Quantity_NOC_SKYBLUE3': (<Quantity_NameOfColor.Quantity_NOC_SKYBLUE3: 447>, None), 'Quantity_NOC_SKYBLUE4': (<Quantity_NameOfColor.Quantity_NOC_SKYBLUE4: 448>, None), 'Quantity_NOC_SLATEBLUE': (<Quantity_NameOfColor.Quantity_NOC_SLATEBLUE: 449>, None), 'Quantity_NOC_SLATEBLUE1': (<Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1: 450>, None), 'Quantity_NOC_SLATEBLUE2': (<Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2: 451>, None), 'Quantity_NOC_SLATEBLUE3': (<Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3: 452>, None), 'Quantity_NOC_SLATEBLUE4': (<Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4: 453>, None), 'Quantity_NOC_SLATEGRAY1': (<Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1: 454>, None), 'Quantity_NOC_SLATEGRAY2': (<Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2: 455>, None), 'Quantity_NOC_SLATEGRAY3': (<Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3: 456>, None), 'Quantity_NOC_SLATEGRAY4': (<Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4: 457>, None), 'Quantity_NOC_SLATEGRAY': (<Quantity_NameOfColor.Quantity_NOC_SLATEGRAY: 458>, None), 'Quantity_NOC_SNOW': (<Quantity_NameOfColor.Quantity_NOC_SNOW: 459>, None), 'Quantity_NOC_SNOW2': (<Quantity_NameOfColor.Quantity_NOC_SNOW2: 460>, None), 'Quantity_NOC_SNOW3': (<Quantity_NameOfColor.Quantity_NOC_SNOW3: 461>, None), 'Quantity_NOC_SNOW4': (<Quantity_NameOfColor.Quantity_NOC_SNOW4: 462>, None), 'Quantity_NOC_SPRINGGREEN': (<Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN: 463>, None), 'Quantity_NOC_SPRINGGREEN2': (<Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2: 464>, None), 'Quantity_NOC_SPRINGGREEN3': (<Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3: 465>, None), 'Quantity_NOC_SPRINGGREEN4': (<Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4: 466>, None), 'Quantity_NOC_STEELBLUE': (<Quantity_NameOfColor.Quantity_NOC_STEELBLUE: 467>, None), 'Quantity_NOC_STEELBLUE1': (<Quantity_NameOfColor.Quantity_NOC_STEELBLUE1: 468>, None), 'Quantity_NOC_STEELBLUE2': (<Quantity_NameOfColor.Quantity_NOC_STEELBLUE2: 469>, None), 'Quantity_NOC_STEELBLUE3': (<Quantity_NameOfColor.Quantity_NOC_STEELBLUE3: 470>, None), 'Quantity_NOC_STEELBLUE4': (<Quantity_NameOfColor.Quantity_NOC_STEELBLUE4: 471>, None), 'Quantity_NOC_TAN': (<Quantity_NameOfColor.Quantity_NOC_TAN: 472>, None), 'Quantity_NOC_TAN1': (<Quantity_NameOfColor.Quantity_NOC_TAN1: 473>, None), 'Quantity_NOC_TAN2': (<Quantity_NameOfColor.Quantity_NOC_TAN2: 474>, None), 'Quantity_NOC_TAN3': (<Quantity_NameOfColor.Quantity_NOC_TAN3: 475>, None), 'Quantity_NOC_TAN4': (<Quantity_NameOfColor.Quantity_NOC_TAN4: 476>, None), 'Quantity_NOC_THISTLE': (<Quantity_NameOfColor.Quantity_NOC_THISTLE: 477>, None), 'Quantity_NOC_THISTLE1': (<Quantity_NameOfColor.Quantity_NOC_THISTLE1: 478>, None), 'Quantity_NOC_THISTLE2': (<Quantity_NameOfColor.Quantity_NOC_THISTLE2: 479>, None), 'Quantity_NOC_THISTLE3': (<Quantity_NameOfColor.Quantity_NOC_THISTLE3: 480>, None), 'Quantity_NOC_THISTLE4': (<Quantity_NameOfColor.Quantity_NOC_THISTLE4: 481>, None), 'Quantity_NOC_TOMATO': (<Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>, None), 'Quantity_NOC_TOMATO1': (<Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>, None), 'Quantity_NOC_TOMATO2': (<Quantity_NameOfColor.Quantity_NOC_TOMATO2: 483>, None), 'Quantity_NOC_TOMATO3': (<Quantity_NameOfColor.Quantity_NOC_TOMATO3: 484>, None), 'Quantity_NOC_TOMATO4': (<Quantity_NameOfColor.Quantity_NOC_TOMATO4: 485>, None), 'Quantity_NOC_TURQUOISE': (<Quantity_NameOfColor.Quantity_NOC_TURQUOISE: 486>, None), 'Quantity_NOC_TURQUOISE1': (<Quantity_NameOfColor.Quantity_NOC_TURQUOISE1: 487>, None), 'Quantity_NOC_TURQUOISE2': (<Quantity_NameOfColor.Quantity_NOC_TURQUOISE2: 488>, None), 'Quantity_NOC_TURQUOISE3': (<Quantity_NameOfColor.Quantity_NOC_TURQUOISE3: 489>, None), 'Quantity_NOC_TURQUOISE4': (<Quantity_NameOfColor.Quantity_NOC_TURQUOISE4: 490>, None), 'Quantity_NOC_VIOLET': (<Quantity_NameOfColor.Quantity_NOC_VIOLET: 491>, None), 'Quantity_NOC_VIOLETRED': (<Quantity_NameOfColor.Quantity_NOC_VIOLETRED: 492>, None), 'Quantity_NOC_VIOLETRED1': (<Quantity_NameOfColor.Quantity_NOC_VIOLETRED1: 493>, None), 'Quantity_NOC_VIOLETRED2': (<Quantity_NameOfColor.Quantity_NOC_VIOLETRED2: 494>, None), 'Quantity_NOC_VIOLETRED3': (<Quantity_NameOfColor.Quantity_NOC_VIOLETRED3: 495>, None), 'Quantity_NOC_VIOLETRED4': (<Quantity_NameOfColor.Quantity_NOC_VIOLETRED4: 496>, None), 'Quantity_NOC_WHEAT': (<Quantity_NameOfColor.Quantity_NOC_WHEAT: 497>, None), 'Quantity_NOC_WHEAT1': (<Quantity_NameOfColor.Quantity_NOC_WHEAT1: 498>, None), 'Quantity_NOC_WHEAT2': (<Quantity_NameOfColor.Quantity_NOC_WHEAT2: 499>, None), 'Quantity_NOC_WHEAT3': (<Quantity_NameOfColor.Quantity_NOC_WHEAT3: 500>, None), 'Quantity_NOC_WHEAT4': (<Quantity_NameOfColor.Quantity_NOC_WHEAT4: 501>, None), 'Quantity_NOC_WHITESMOKE': (<Quantity_NameOfColor.Quantity_NOC_WHITESMOKE: 502>, None), 'Quantity_NOC_YELLOW': (<Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>, None), 'Quantity_NOC_YELLOW1': (<Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>, None), 'Quantity_NOC_YELLOW2': (<Quantity_NameOfColor.Quantity_NOC_YELLOW2: 504>, None), 'Quantity_NOC_YELLOW3': (<Quantity_NameOfColor.Quantity_NOC_YELLOW3: 505>, None), 'Quantity_NOC_YELLOW4': (<Quantity_NameOfColor.Quantity_NOC_YELLOW4: 506>, None), 'Quantity_NOC_YELLOWGREEN': (<Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN: 507>, None), 'Quantity_NOC_WHITE': (<Quantity_NameOfColor.Quantity_NOC_WHITE: 508>, None)}
    __members__: dict # value = {'Quantity_NOC_BLACK': <Quantity_NameOfColor.Quantity_NOC_BLACK: 0>, 'Quantity_NOC_MATRABLUE': <Quantity_NameOfColor.Quantity_NOC_MATRABLUE: 1>, 'Quantity_NOC_MATRAGRAY': <Quantity_NameOfColor.Quantity_NOC_MATRAGRAY: 2>, 'Quantity_NOC_ALICEBLUE': <Quantity_NameOfColor.Quantity_NOC_ALICEBLUE: 3>, 'Quantity_NOC_ANTIQUEWHITE': <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE: 4>, 'Quantity_NOC_ANTIQUEWHITE1': <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1: 5>, 'Quantity_NOC_ANTIQUEWHITE2': <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2: 6>, 'Quantity_NOC_ANTIQUEWHITE3': <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3: 7>, 'Quantity_NOC_ANTIQUEWHITE4': <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4: 8>, 'Quantity_NOC_AQUAMARINE1': <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1: 9>, 'Quantity_NOC_AQUAMARINE2': <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2: 10>, 'Quantity_NOC_AQUAMARINE4': <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4: 11>, 'Quantity_NOC_AZURE': <Quantity_NameOfColor.Quantity_NOC_AZURE: 12>, 'Quantity_NOC_AZURE2': <Quantity_NameOfColor.Quantity_NOC_AZURE2: 13>, 'Quantity_NOC_AZURE3': <Quantity_NameOfColor.Quantity_NOC_AZURE3: 14>, 'Quantity_NOC_AZURE4': <Quantity_NameOfColor.Quantity_NOC_AZURE4: 15>, 'Quantity_NOC_BEIGE': <Quantity_NameOfColor.Quantity_NOC_BEIGE: 16>, 'Quantity_NOC_BISQUE': <Quantity_NameOfColor.Quantity_NOC_BISQUE: 17>, 'Quantity_NOC_BISQUE2': <Quantity_NameOfColor.Quantity_NOC_BISQUE2: 18>, 'Quantity_NOC_BISQUE3': <Quantity_NameOfColor.Quantity_NOC_BISQUE3: 19>, 'Quantity_NOC_BISQUE4': <Quantity_NameOfColor.Quantity_NOC_BISQUE4: 20>, 'Quantity_NOC_BLANCHEDALMOND': <Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND: 21>, 'Quantity_NOC_BLUE': <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>, 'Quantity_NOC_BLUE1': <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>, 'Quantity_NOC_BLUE2': <Quantity_NameOfColor.Quantity_NOC_BLUE2: 23>, 'Quantity_NOC_BLUE3': <Quantity_NameOfColor.Quantity_NOC_BLUE3: 24>, 'Quantity_NOC_BLUE4': <Quantity_NameOfColor.Quantity_NOC_BLUE4: 25>, 'Quantity_NOC_BLUEVIOLET': <Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET: 26>, 'Quantity_NOC_BROWN': <Quantity_NameOfColor.Quantity_NOC_BROWN: 27>, 'Quantity_NOC_BROWN1': <Quantity_NameOfColor.Quantity_NOC_BROWN1: 28>, 'Quantity_NOC_BROWN2': <Quantity_NameOfColor.Quantity_NOC_BROWN2: 29>, 'Quantity_NOC_BROWN3': <Quantity_NameOfColor.Quantity_NOC_BROWN3: 30>, 'Quantity_NOC_BROWN4': <Quantity_NameOfColor.Quantity_NOC_BROWN4: 31>, 'Quantity_NOC_BURLYWOOD': <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD: 32>, 'Quantity_NOC_BURLYWOOD1': <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1: 33>, 'Quantity_NOC_BURLYWOOD2': <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2: 34>, 'Quantity_NOC_BURLYWOOD3': <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3: 35>, 'Quantity_NOC_BURLYWOOD4': <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4: 36>, 'Quantity_NOC_CADETBLUE': <Quantity_NameOfColor.Quantity_NOC_CADETBLUE: 37>, 'Quantity_NOC_CADETBLUE1': <Quantity_NameOfColor.Quantity_NOC_CADETBLUE1: 38>, 'Quantity_NOC_CADETBLUE2': <Quantity_NameOfColor.Quantity_NOC_CADETBLUE2: 39>, 'Quantity_NOC_CADETBLUE3': <Quantity_NameOfColor.Quantity_NOC_CADETBLUE3: 40>, 'Quantity_NOC_CADETBLUE4': <Quantity_NameOfColor.Quantity_NOC_CADETBLUE4: 41>, 'Quantity_NOC_CHARTREUSE': <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>, 'Quantity_NOC_CHARTREUSE1': <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>, 'Quantity_NOC_CHARTREUSE2': <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2: 43>, 'Quantity_NOC_CHARTREUSE3': <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3: 44>, 'Quantity_NOC_CHARTREUSE4': <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4: 45>, 'Quantity_NOC_CHOCOLATE': <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE: 46>, 'Quantity_NOC_CHOCOLATE1': <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1: 47>, 'Quantity_NOC_CHOCOLATE2': <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2: 48>, 'Quantity_NOC_CHOCOLATE3': <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3: 49>, 'Quantity_NOC_CHOCOLATE4': <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4: 50>, 'Quantity_NOC_CORAL': <Quantity_NameOfColor.Quantity_NOC_CORAL: 51>, 'Quantity_NOC_CORAL1': <Quantity_NameOfColor.Quantity_NOC_CORAL1: 52>, 'Quantity_NOC_CORAL2': <Quantity_NameOfColor.Quantity_NOC_CORAL2: 53>, 'Quantity_NOC_CORAL3': <Quantity_NameOfColor.Quantity_NOC_CORAL3: 54>, 'Quantity_NOC_CORAL4': <Quantity_NameOfColor.Quantity_NOC_CORAL4: 55>, 'Quantity_NOC_CORNFLOWERBLUE': <Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE: 56>, 'Quantity_NOC_CORNSILK1': <Quantity_NameOfColor.Quantity_NOC_CORNSILK1: 57>, 'Quantity_NOC_CORNSILK2': <Quantity_NameOfColor.Quantity_NOC_CORNSILK2: 58>, 'Quantity_NOC_CORNSILK3': <Quantity_NameOfColor.Quantity_NOC_CORNSILK3: 59>, 'Quantity_NOC_CORNSILK4': <Quantity_NameOfColor.Quantity_NOC_CORNSILK4: 60>, 'Quantity_NOC_CYAN': <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>, 'Quantity_NOC_CYAN1': <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>, 'Quantity_NOC_CYAN2': <Quantity_NameOfColor.Quantity_NOC_CYAN2: 62>, 'Quantity_NOC_CYAN3': <Quantity_NameOfColor.Quantity_NOC_CYAN3: 63>, 'Quantity_NOC_CYAN4': <Quantity_NameOfColor.Quantity_NOC_CYAN4: 64>, 'Quantity_NOC_DARKGOLDENROD': <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD: 65>, 'Quantity_NOC_DARKGOLDENROD1': <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1: 66>, 'Quantity_NOC_DARKGOLDENROD2': <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2: 67>, 'Quantity_NOC_DARKGOLDENROD3': <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3: 68>, 'Quantity_NOC_DARKGOLDENROD4': <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4: 69>, 'Quantity_NOC_DARKGREEN': <Quantity_NameOfColor.Quantity_NOC_DARKGREEN: 70>, 'Quantity_NOC_DARKKHAKI': <Quantity_NameOfColor.Quantity_NOC_DARKKHAKI: 71>, 'Quantity_NOC_DARKOLIVEGREEN': <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN: 72>, 'Quantity_NOC_DARKOLIVEGREEN1': <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1: 73>, 'Quantity_NOC_DARKOLIVEGREEN2': <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2: 74>, 'Quantity_NOC_DARKOLIVEGREEN3': <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3: 75>, 'Quantity_NOC_DARKOLIVEGREEN4': <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4: 76>, 'Quantity_NOC_DARKORANGE': <Quantity_NameOfColor.Quantity_NOC_DARKORANGE: 77>, 'Quantity_NOC_DARKORANGE1': <Quantity_NameOfColor.Quantity_NOC_DARKORANGE1: 78>, 'Quantity_NOC_DARKORANGE2': <Quantity_NameOfColor.Quantity_NOC_DARKORANGE2: 79>, 'Quantity_NOC_DARKORANGE3': <Quantity_NameOfColor.Quantity_NOC_DARKORANGE3: 80>, 'Quantity_NOC_DARKORANGE4': <Quantity_NameOfColor.Quantity_NOC_DARKORANGE4: 81>, 'Quantity_NOC_DARKORCHID': <Quantity_NameOfColor.Quantity_NOC_DARKORCHID: 82>, 'Quantity_NOC_DARKORCHID1': <Quantity_NameOfColor.Quantity_NOC_DARKORCHID1: 83>, 'Quantity_NOC_DARKORCHID2': <Quantity_NameOfColor.Quantity_NOC_DARKORCHID2: 84>, 'Quantity_NOC_DARKORCHID3': <Quantity_NameOfColor.Quantity_NOC_DARKORCHID3: 85>, 'Quantity_NOC_DARKORCHID4': <Quantity_NameOfColor.Quantity_NOC_DARKORCHID4: 86>, 'Quantity_NOC_DARKSALMON': <Quantity_NameOfColor.Quantity_NOC_DARKSALMON: 87>, 'Quantity_NOC_DARKSEAGREEN': <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN: 88>, 'Quantity_NOC_DARKSEAGREEN1': <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1: 89>, 'Quantity_NOC_DARKSEAGREEN2': <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2: 90>, 'Quantity_NOC_DARKSEAGREEN3': <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3: 91>, 'Quantity_NOC_DARKSEAGREEN4': <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4: 92>, 'Quantity_NOC_DARKSLATEBLUE': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE: 93>, 'Quantity_NOC_DARKSLATEGRAY1': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1: 94>, 'Quantity_NOC_DARKSLATEGRAY2': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2: 95>, 'Quantity_NOC_DARKSLATEGRAY3': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3: 96>, 'Quantity_NOC_DARKSLATEGRAY4': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4: 97>, 'Quantity_NOC_DARKSLATEGRAY': <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY: 98>, 'Quantity_NOC_DARKTURQUOISE': <Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE: 99>, 'Quantity_NOC_DARKVIOLET': <Quantity_NameOfColor.Quantity_NOC_DARKVIOLET: 100>, 'Quantity_NOC_DEEPPINK': <Quantity_NameOfColor.Quantity_NOC_DEEPPINK: 101>, 'Quantity_NOC_DEEPPINK2': <Quantity_NameOfColor.Quantity_NOC_DEEPPINK2: 102>, 'Quantity_NOC_DEEPPINK3': <Quantity_NameOfColor.Quantity_NOC_DEEPPINK3: 103>, 'Quantity_NOC_DEEPPINK4': <Quantity_NameOfColor.Quantity_NOC_DEEPPINK4: 104>, 'Quantity_NOC_DEEPSKYBLUE1': <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1: 105>, 'Quantity_NOC_DEEPSKYBLUE2': <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2: 106>, 'Quantity_NOC_DEEPSKYBLUE3': <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3: 107>, 'Quantity_NOC_DEEPSKYBLUE4': <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4: 108>, 'Quantity_NOC_DODGERBLUE1': <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1: 109>, 'Quantity_NOC_DODGERBLUE2': <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2: 110>, 'Quantity_NOC_DODGERBLUE3': <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3: 111>, 'Quantity_NOC_DODGERBLUE4': <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4: 112>, 'Quantity_NOC_FIREBRICK': <Quantity_NameOfColor.Quantity_NOC_FIREBRICK: 113>, 'Quantity_NOC_FIREBRICK1': <Quantity_NameOfColor.Quantity_NOC_FIREBRICK1: 114>, 'Quantity_NOC_FIREBRICK2': <Quantity_NameOfColor.Quantity_NOC_FIREBRICK2: 115>, 'Quantity_NOC_FIREBRICK3': <Quantity_NameOfColor.Quantity_NOC_FIREBRICK3: 116>, 'Quantity_NOC_FIREBRICK4': <Quantity_NameOfColor.Quantity_NOC_FIREBRICK4: 117>, 'Quantity_NOC_FLORALWHITE': <Quantity_NameOfColor.Quantity_NOC_FLORALWHITE: 118>, 'Quantity_NOC_FORESTGREEN': <Quantity_NameOfColor.Quantity_NOC_FORESTGREEN: 119>, 'Quantity_NOC_GAINSBORO': <Quantity_NameOfColor.Quantity_NOC_GAINSBORO: 120>, 'Quantity_NOC_GHOSTWHITE': <Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE: 121>, 'Quantity_NOC_GOLD': <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>, 'Quantity_NOC_GOLD1': <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>, 'Quantity_NOC_GOLD2': <Quantity_NameOfColor.Quantity_NOC_GOLD2: 123>, 'Quantity_NOC_GOLD3': <Quantity_NameOfColor.Quantity_NOC_GOLD3: 124>, 'Quantity_NOC_GOLD4': <Quantity_NameOfColor.Quantity_NOC_GOLD4: 125>, 'Quantity_NOC_GOLDENROD': <Quantity_NameOfColor.Quantity_NOC_GOLDENROD: 126>, 'Quantity_NOC_GOLDENROD1': <Quantity_NameOfColor.Quantity_NOC_GOLDENROD1: 127>, 'Quantity_NOC_GOLDENROD2': <Quantity_NameOfColor.Quantity_NOC_GOLDENROD2: 128>, 'Quantity_NOC_GOLDENROD3': <Quantity_NameOfColor.Quantity_NOC_GOLDENROD3: 129>, 'Quantity_NOC_GOLDENROD4': <Quantity_NameOfColor.Quantity_NOC_GOLDENROD4: 130>, 'Quantity_NOC_GRAY': <Quantity_NameOfColor.Quantity_NOC_GRAY: 131>, 'Quantity_NOC_GRAY0': <Quantity_NameOfColor.Quantity_NOC_GRAY0: 132>, 'Quantity_NOC_GRAY1': <Quantity_NameOfColor.Quantity_NOC_GRAY1: 133>, 'Quantity_NOC_GRAY2': <Quantity_NameOfColor.Quantity_NOC_GRAY2: 134>, 'Quantity_NOC_GRAY3': <Quantity_NameOfColor.Quantity_NOC_GRAY3: 135>, 'Quantity_NOC_GRAY4': <Quantity_NameOfColor.Quantity_NOC_GRAY4: 136>, 'Quantity_NOC_GRAY5': <Quantity_NameOfColor.Quantity_NOC_GRAY5: 137>, 'Quantity_NOC_GRAY6': <Quantity_NameOfColor.Quantity_NOC_GRAY6: 138>, 'Quantity_NOC_GRAY7': <Quantity_NameOfColor.Quantity_NOC_GRAY7: 139>, 'Quantity_NOC_GRAY8': <Quantity_NameOfColor.Quantity_NOC_GRAY8: 140>, 'Quantity_NOC_GRAY9': <Quantity_NameOfColor.Quantity_NOC_GRAY9: 141>, 'Quantity_NOC_GRAY10': <Quantity_NameOfColor.Quantity_NOC_GRAY10: 142>, 'Quantity_NOC_GRAY11': <Quantity_NameOfColor.Quantity_NOC_GRAY11: 143>, 'Quantity_NOC_GRAY12': <Quantity_NameOfColor.Quantity_NOC_GRAY12: 144>, 'Quantity_NOC_GRAY13': <Quantity_NameOfColor.Quantity_NOC_GRAY13: 145>, 'Quantity_NOC_GRAY14': <Quantity_NameOfColor.Quantity_NOC_GRAY14: 146>, 'Quantity_NOC_GRAY15': <Quantity_NameOfColor.Quantity_NOC_GRAY15: 147>, 'Quantity_NOC_GRAY16': <Quantity_NameOfColor.Quantity_NOC_GRAY16: 148>, 'Quantity_NOC_GRAY17': <Quantity_NameOfColor.Quantity_NOC_GRAY17: 149>, 'Quantity_NOC_GRAY18': <Quantity_NameOfColor.Quantity_NOC_GRAY18: 150>, 'Quantity_NOC_GRAY19': <Quantity_NameOfColor.Quantity_NOC_GRAY19: 151>, 'Quantity_NOC_GRAY20': <Quantity_NameOfColor.Quantity_NOC_GRAY20: 152>, 'Quantity_NOC_GRAY21': <Quantity_NameOfColor.Quantity_NOC_GRAY21: 153>, 'Quantity_NOC_GRAY22': <Quantity_NameOfColor.Quantity_NOC_GRAY22: 154>, 'Quantity_NOC_GRAY23': <Quantity_NameOfColor.Quantity_NOC_GRAY23: 155>, 'Quantity_NOC_GRAY24': <Quantity_NameOfColor.Quantity_NOC_GRAY24: 156>, 'Quantity_NOC_GRAY25': <Quantity_NameOfColor.Quantity_NOC_GRAY25: 157>, 'Quantity_NOC_GRAY26': <Quantity_NameOfColor.Quantity_NOC_GRAY26: 158>, 'Quantity_NOC_GRAY27': <Quantity_NameOfColor.Quantity_NOC_GRAY27: 159>, 'Quantity_NOC_GRAY28': <Quantity_NameOfColor.Quantity_NOC_GRAY28: 160>, 'Quantity_NOC_GRAY29': <Quantity_NameOfColor.Quantity_NOC_GRAY29: 161>, 'Quantity_NOC_GRAY30': <Quantity_NameOfColor.Quantity_NOC_GRAY30: 162>, 'Quantity_NOC_GRAY31': <Quantity_NameOfColor.Quantity_NOC_GRAY31: 163>, 'Quantity_NOC_GRAY32': <Quantity_NameOfColor.Quantity_NOC_GRAY32: 164>, 'Quantity_NOC_GRAY33': <Quantity_NameOfColor.Quantity_NOC_GRAY33: 165>, 'Quantity_NOC_GRAY34': <Quantity_NameOfColor.Quantity_NOC_GRAY34: 166>, 'Quantity_NOC_GRAY35': <Quantity_NameOfColor.Quantity_NOC_GRAY35: 167>, 'Quantity_NOC_GRAY36': <Quantity_NameOfColor.Quantity_NOC_GRAY36: 168>, 'Quantity_NOC_GRAY37': <Quantity_NameOfColor.Quantity_NOC_GRAY37: 169>, 'Quantity_NOC_GRAY38': <Quantity_NameOfColor.Quantity_NOC_GRAY38: 170>, 'Quantity_NOC_GRAY39': <Quantity_NameOfColor.Quantity_NOC_GRAY39: 171>, 'Quantity_NOC_GRAY40': <Quantity_NameOfColor.Quantity_NOC_GRAY40: 172>, 'Quantity_NOC_GRAY41': <Quantity_NameOfColor.Quantity_NOC_GRAY41: 173>, 'Quantity_NOC_GRAY42': <Quantity_NameOfColor.Quantity_NOC_GRAY42: 174>, 'Quantity_NOC_GRAY43': <Quantity_NameOfColor.Quantity_NOC_GRAY43: 175>, 'Quantity_NOC_GRAY44': <Quantity_NameOfColor.Quantity_NOC_GRAY44: 176>, 'Quantity_NOC_GRAY45': <Quantity_NameOfColor.Quantity_NOC_GRAY45: 177>, 'Quantity_NOC_GRAY46': <Quantity_NameOfColor.Quantity_NOC_GRAY46: 178>, 'Quantity_NOC_GRAY47': <Quantity_NameOfColor.Quantity_NOC_GRAY47: 179>, 'Quantity_NOC_GRAY48': <Quantity_NameOfColor.Quantity_NOC_GRAY48: 180>, 'Quantity_NOC_GRAY49': <Quantity_NameOfColor.Quantity_NOC_GRAY49: 181>, 'Quantity_NOC_GRAY50': <Quantity_NameOfColor.Quantity_NOC_GRAY50: 182>, 'Quantity_NOC_GRAY51': <Quantity_NameOfColor.Quantity_NOC_GRAY51: 183>, 'Quantity_NOC_GRAY52': <Quantity_NameOfColor.Quantity_NOC_GRAY52: 184>, 'Quantity_NOC_GRAY53': <Quantity_NameOfColor.Quantity_NOC_GRAY53: 185>, 'Quantity_NOC_GRAY54': <Quantity_NameOfColor.Quantity_NOC_GRAY54: 186>, 'Quantity_NOC_GRAY55': <Quantity_NameOfColor.Quantity_NOC_GRAY55: 187>, 'Quantity_NOC_GRAY56': <Quantity_NameOfColor.Quantity_NOC_GRAY56: 188>, 'Quantity_NOC_GRAY57': <Quantity_NameOfColor.Quantity_NOC_GRAY57: 189>, 'Quantity_NOC_GRAY58': <Quantity_NameOfColor.Quantity_NOC_GRAY58: 190>, 'Quantity_NOC_GRAY59': <Quantity_NameOfColor.Quantity_NOC_GRAY59: 191>, 'Quantity_NOC_GRAY60': <Quantity_NameOfColor.Quantity_NOC_GRAY60: 192>, 'Quantity_NOC_GRAY61': <Quantity_NameOfColor.Quantity_NOC_GRAY61: 193>, 'Quantity_NOC_GRAY62': <Quantity_NameOfColor.Quantity_NOC_GRAY62: 194>, 'Quantity_NOC_GRAY63': <Quantity_NameOfColor.Quantity_NOC_GRAY63: 195>, 'Quantity_NOC_GRAY64': <Quantity_NameOfColor.Quantity_NOC_GRAY64: 196>, 'Quantity_NOC_GRAY65': <Quantity_NameOfColor.Quantity_NOC_GRAY65: 197>, 'Quantity_NOC_GRAY66': <Quantity_NameOfColor.Quantity_NOC_GRAY66: 198>, 'Quantity_NOC_GRAY67': <Quantity_NameOfColor.Quantity_NOC_GRAY67: 199>, 'Quantity_NOC_GRAY68': <Quantity_NameOfColor.Quantity_NOC_GRAY68: 200>, 'Quantity_NOC_GRAY69': <Quantity_NameOfColor.Quantity_NOC_GRAY69: 201>, 'Quantity_NOC_GRAY70': <Quantity_NameOfColor.Quantity_NOC_GRAY70: 202>, 'Quantity_NOC_GRAY71': <Quantity_NameOfColor.Quantity_NOC_GRAY71: 203>, 'Quantity_NOC_GRAY72': <Quantity_NameOfColor.Quantity_NOC_GRAY72: 204>, 'Quantity_NOC_GRAY73': <Quantity_NameOfColor.Quantity_NOC_GRAY73: 205>, 'Quantity_NOC_GRAY74': <Quantity_NameOfColor.Quantity_NOC_GRAY74: 206>, 'Quantity_NOC_GRAY75': <Quantity_NameOfColor.Quantity_NOC_GRAY75: 207>, 'Quantity_NOC_GRAY76': <Quantity_NameOfColor.Quantity_NOC_GRAY76: 208>, 'Quantity_NOC_GRAY77': <Quantity_NameOfColor.Quantity_NOC_GRAY77: 209>, 'Quantity_NOC_GRAY78': <Quantity_NameOfColor.Quantity_NOC_GRAY78: 210>, 'Quantity_NOC_GRAY79': <Quantity_NameOfColor.Quantity_NOC_GRAY79: 211>, 'Quantity_NOC_GRAY80': <Quantity_NameOfColor.Quantity_NOC_GRAY80: 212>, 'Quantity_NOC_GRAY81': <Quantity_NameOfColor.Quantity_NOC_GRAY81: 213>, 'Quantity_NOC_GRAY82': <Quantity_NameOfColor.Quantity_NOC_GRAY82: 214>, 'Quantity_NOC_GRAY83': <Quantity_NameOfColor.Quantity_NOC_GRAY83: 215>, 'Quantity_NOC_GRAY85': <Quantity_NameOfColor.Quantity_NOC_GRAY85: 216>, 'Quantity_NOC_GRAY86': <Quantity_NameOfColor.Quantity_NOC_GRAY86: 217>, 'Quantity_NOC_GRAY87': <Quantity_NameOfColor.Quantity_NOC_GRAY87: 218>, 'Quantity_NOC_GRAY88': <Quantity_NameOfColor.Quantity_NOC_GRAY88: 219>, 'Quantity_NOC_GRAY89': <Quantity_NameOfColor.Quantity_NOC_GRAY89: 220>, 'Quantity_NOC_GRAY90': <Quantity_NameOfColor.Quantity_NOC_GRAY90: 221>, 'Quantity_NOC_GRAY91': <Quantity_NameOfColor.Quantity_NOC_GRAY91: 222>, 'Quantity_NOC_GRAY92': <Quantity_NameOfColor.Quantity_NOC_GRAY92: 223>, 'Quantity_NOC_GRAY93': <Quantity_NameOfColor.Quantity_NOC_GRAY93: 224>, 'Quantity_NOC_GRAY94': <Quantity_NameOfColor.Quantity_NOC_GRAY94: 225>, 'Quantity_NOC_GRAY95': <Quantity_NameOfColor.Quantity_NOC_GRAY95: 226>, 'Quantity_NOC_GRAY97': <Quantity_NameOfColor.Quantity_NOC_GRAY97: 227>, 'Quantity_NOC_GRAY98': <Quantity_NameOfColor.Quantity_NOC_GRAY98: 228>, 'Quantity_NOC_GRAY99': <Quantity_NameOfColor.Quantity_NOC_GRAY99: 229>, 'Quantity_NOC_GREEN': <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>, 'Quantity_NOC_GREEN1': <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>, 'Quantity_NOC_GREEN2': <Quantity_NameOfColor.Quantity_NOC_GREEN2: 231>, 'Quantity_NOC_GREEN3': <Quantity_NameOfColor.Quantity_NOC_GREEN3: 232>, 'Quantity_NOC_GREEN4': <Quantity_NameOfColor.Quantity_NOC_GREEN4: 233>, 'Quantity_NOC_GREENYELLOW': <Quantity_NameOfColor.Quantity_NOC_GREENYELLOW: 234>, 'Quantity_NOC_HONEYDEW': <Quantity_NameOfColor.Quantity_NOC_HONEYDEW: 235>, 'Quantity_NOC_HONEYDEW2': <Quantity_NameOfColor.Quantity_NOC_HONEYDEW2: 236>, 'Quantity_NOC_HONEYDEW3': <Quantity_NameOfColor.Quantity_NOC_HONEYDEW3: 237>, 'Quantity_NOC_HONEYDEW4': <Quantity_NameOfColor.Quantity_NOC_HONEYDEW4: 238>, 'Quantity_NOC_HOTPINK': <Quantity_NameOfColor.Quantity_NOC_HOTPINK: 239>, 'Quantity_NOC_HOTPINK1': <Quantity_NameOfColor.Quantity_NOC_HOTPINK1: 240>, 'Quantity_NOC_HOTPINK2': <Quantity_NameOfColor.Quantity_NOC_HOTPINK2: 241>, 'Quantity_NOC_HOTPINK3': <Quantity_NameOfColor.Quantity_NOC_HOTPINK3: 242>, 'Quantity_NOC_HOTPINK4': <Quantity_NameOfColor.Quantity_NOC_HOTPINK4: 243>, 'Quantity_NOC_INDIANRED': <Quantity_NameOfColor.Quantity_NOC_INDIANRED: 244>, 'Quantity_NOC_INDIANRED1': <Quantity_NameOfColor.Quantity_NOC_INDIANRED1: 245>, 'Quantity_NOC_INDIANRED2': <Quantity_NameOfColor.Quantity_NOC_INDIANRED2: 246>, 'Quantity_NOC_INDIANRED3': <Quantity_NameOfColor.Quantity_NOC_INDIANRED3: 247>, 'Quantity_NOC_INDIANRED4': <Quantity_NameOfColor.Quantity_NOC_INDIANRED4: 248>, 'Quantity_NOC_IVORY': <Quantity_NameOfColor.Quantity_NOC_IVORY: 249>, 'Quantity_NOC_IVORY2': <Quantity_NameOfColor.Quantity_NOC_IVORY2: 250>, 'Quantity_NOC_IVORY3': <Quantity_NameOfColor.Quantity_NOC_IVORY3: 251>, 'Quantity_NOC_IVORY4': <Quantity_NameOfColor.Quantity_NOC_IVORY4: 252>, 'Quantity_NOC_KHAKI': <Quantity_NameOfColor.Quantity_NOC_KHAKI: 253>, 'Quantity_NOC_KHAKI1': <Quantity_NameOfColor.Quantity_NOC_KHAKI1: 254>, 'Quantity_NOC_KHAKI2': <Quantity_NameOfColor.Quantity_NOC_KHAKI2: 255>, 'Quantity_NOC_KHAKI3': <Quantity_NameOfColor.Quantity_NOC_KHAKI3: 256>, 'Quantity_NOC_KHAKI4': <Quantity_NameOfColor.Quantity_NOC_KHAKI4: 257>, 'Quantity_NOC_LAVENDER': <Quantity_NameOfColor.Quantity_NOC_LAVENDER: 258>, 'Quantity_NOC_LAVENDERBLUSH1': <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1: 259>, 'Quantity_NOC_LAVENDERBLUSH2': <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2: 260>, 'Quantity_NOC_LAVENDERBLUSH3': <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3: 261>, 'Quantity_NOC_LAVENDERBLUSH4': <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4: 262>, 'Quantity_NOC_LAWNGREEN': <Quantity_NameOfColor.Quantity_NOC_LAWNGREEN: 263>, 'Quantity_NOC_LEMONCHIFFON1': <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1: 264>, 'Quantity_NOC_LEMONCHIFFON2': <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2: 265>, 'Quantity_NOC_LEMONCHIFFON3': <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3: 266>, 'Quantity_NOC_LEMONCHIFFON4': <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4: 267>, 'Quantity_NOC_LIGHTBLUE': <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE: 268>, 'Quantity_NOC_LIGHTBLUE1': <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1: 269>, 'Quantity_NOC_LIGHTBLUE2': <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2: 270>, 'Quantity_NOC_LIGHTBLUE3': <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3: 271>, 'Quantity_NOC_LIGHTBLUE4': <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4: 272>, 'Quantity_NOC_LIGHTCORAL': <Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL: 273>, 'Quantity_NOC_LIGHTCYAN': <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>, 'Quantity_NOC_LIGHTCYAN1': <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>, 'Quantity_NOC_LIGHTCYAN2': <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2: 275>, 'Quantity_NOC_LIGHTCYAN3': <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3: 276>, 'Quantity_NOC_LIGHTCYAN4': <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4: 277>, 'Quantity_NOC_LIGHTGOLDENROD': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD: 278>, 'Quantity_NOC_LIGHTGOLDENROD1': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1: 279>, 'Quantity_NOC_LIGHTGOLDENROD2': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2: 280>, 'Quantity_NOC_LIGHTGOLDENROD3': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3: 281>, 'Quantity_NOC_LIGHTGOLDENROD4': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4: 282>, 'Quantity_NOC_LIGHTGOLDENRODYELLOW': <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW: 283>, 'Quantity_NOC_LIGHTGRAY': <Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY: 284>, 'Quantity_NOC_LIGHTPINK': <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK: 285>, 'Quantity_NOC_LIGHTPINK1': <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1: 286>, 'Quantity_NOC_LIGHTPINK2': <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2: 287>, 'Quantity_NOC_LIGHTPINK3': <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3: 288>, 'Quantity_NOC_LIGHTPINK4': <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4: 289>, 'Quantity_NOC_LIGHTSALMON1': <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1: 290>, 'Quantity_NOC_LIGHTSALMON2': <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2: 291>, 'Quantity_NOC_LIGHTSALMON3': <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3: 292>, 'Quantity_NOC_LIGHTSALMON4': <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4: 293>, 'Quantity_NOC_LIGHTSEAGREEN': <Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN: 294>, 'Quantity_NOC_LIGHTSKYBLUE': <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE: 295>, 'Quantity_NOC_LIGHTSKYBLUE1': <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1: 296>, 'Quantity_NOC_LIGHTSKYBLUE2': <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2: 297>, 'Quantity_NOC_LIGHTSKYBLUE3': <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3: 298>, 'Quantity_NOC_LIGHTSKYBLUE4': <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4: 299>, 'Quantity_NOC_LIGHTSLATEBLUE': <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE: 300>, 'Quantity_NOC_LIGHTSLATEGRAY': <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY: 301>, 'Quantity_NOC_LIGHTSTEELBLUE': <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE: 302>, 'Quantity_NOC_LIGHTSTEELBLUE1': <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1: 303>, 'Quantity_NOC_LIGHTSTEELBLUE2': <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2: 304>, 'Quantity_NOC_LIGHTSTEELBLUE3': <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3: 305>, 'Quantity_NOC_LIGHTSTEELBLUE4': <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4: 306>, 'Quantity_NOC_LIGHTYELLOW': <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW: 307>, 'Quantity_NOC_LIGHTYELLOW2': <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2: 308>, 'Quantity_NOC_LIGHTYELLOW3': <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3: 309>, 'Quantity_NOC_LIGHTYELLOW4': <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4: 310>, 'Quantity_NOC_LIMEGREEN': <Quantity_NameOfColor.Quantity_NOC_LIMEGREEN: 311>, 'Quantity_NOC_LINEN': <Quantity_NameOfColor.Quantity_NOC_LINEN: 312>, 'Quantity_NOC_MAGENTA': <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>, 'Quantity_NOC_MAGENTA1': <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>, 'Quantity_NOC_MAGENTA2': <Quantity_NameOfColor.Quantity_NOC_MAGENTA2: 314>, 'Quantity_NOC_MAGENTA3': <Quantity_NameOfColor.Quantity_NOC_MAGENTA3: 315>, 'Quantity_NOC_MAGENTA4': <Quantity_NameOfColor.Quantity_NOC_MAGENTA4: 316>, 'Quantity_NOC_MAROON': <Quantity_NameOfColor.Quantity_NOC_MAROON: 317>, 'Quantity_NOC_MAROON1': <Quantity_NameOfColor.Quantity_NOC_MAROON1: 318>, 'Quantity_NOC_MAROON2': <Quantity_NameOfColor.Quantity_NOC_MAROON2: 319>, 'Quantity_NOC_MAROON3': <Quantity_NameOfColor.Quantity_NOC_MAROON3: 320>, 'Quantity_NOC_MAROON4': <Quantity_NameOfColor.Quantity_NOC_MAROON4: 321>, 'Quantity_NOC_MEDIUMAQUAMARINE': <Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE: 322>, 'Quantity_NOC_MEDIUMORCHID': <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID: 323>, 'Quantity_NOC_MEDIUMORCHID1': <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1: 324>, 'Quantity_NOC_MEDIUMORCHID2': <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2: 325>, 'Quantity_NOC_MEDIUMORCHID3': <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3: 326>, 'Quantity_NOC_MEDIUMORCHID4': <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4: 327>, 'Quantity_NOC_MEDIUMPURPLE': <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE: 328>, 'Quantity_NOC_MEDIUMPURPLE1': <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1: 329>, 'Quantity_NOC_MEDIUMPURPLE2': <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2: 330>, 'Quantity_NOC_MEDIUMPURPLE3': <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3: 331>, 'Quantity_NOC_MEDIUMPURPLE4': <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4: 332>, 'Quantity_NOC_MEDIUMSEAGREEN': <Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN: 333>, 'Quantity_NOC_MEDIUMSLATEBLUE': <Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE: 334>, 'Quantity_NOC_MEDIUMSPRINGGREEN': <Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN: 335>, 'Quantity_NOC_MEDIUMTURQUOISE': <Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE: 336>, 'Quantity_NOC_MEDIUMVIOLETRED': <Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED: 337>, 'Quantity_NOC_MIDNIGHTBLUE': <Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE: 338>, 'Quantity_NOC_MINTCREAM': <Quantity_NameOfColor.Quantity_NOC_MINTCREAM: 339>, 'Quantity_NOC_MISTYROSE': <Quantity_NameOfColor.Quantity_NOC_MISTYROSE: 340>, 'Quantity_NOC_MISTYROSE2': <Quantity_NameOfColor.Quantity_NOC_MISTYROSE2: 341>, 'Quantity_NOC_MISTYROSE3': <Quantity_NameOfColor.Quantity_NOC_MISTYROSE3: 342>, 'Quantity_NOC_MISTYROSE4': <Quantity_NameOfColor.Quantity_NOC_MISTYROSE4: 343>, 'Quantity_NOC_MOCCASIN': <Quantity_NameOfColor.Quantity_NOC_MOCCASIN: 344>, 'Quantity_NOC_NAVAJOWHITE1': <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1: 345>, 'Quantity_NOC_NAVAJOWHITE2': <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2: 346>, 'Quantity_NOC_NAVAJOWHITE3': <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3: 347>, 'Quantity_NOC_NAVAJOWHITE4': <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4: 348>, 'Quantity_NOC_NAVYBLUE': <Quantity_NameOfColor.Quantity_NOC_NAVYBLUE: 349>, 'Quantity_NOC_OLDLACE': <Quantity_NameOfColor.Quantity_NOC_OLDLACE: 350>, 'Quantity_NOC_OLIVEDRAB': <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB: 351>, 'Quantity_NOC_OLIVEDRAB1': <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1: 352>, 'Quantity_NOC_OLIVEDRAB2': <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2: 353>, 'Quantity_NOC_OLIVEDRAB3': <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3: 354>, 'Quantity_NOC_OLIVEDRAB4': <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4: 355>, 'Quantity_NOC_ORANGE': <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>, 'Quantity_NOC_ORANGE1': <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>, 'Quantity_NOC_ORANGE2': <Quantity_NameOfColor.Quantity_NOC_ORANGE2: 357>, 'Quantity_NOC_ORANGE3': <Quantity_NameOfColor.Quantity_NOC_ORANGE3: 358>, 'Quantity_NOC_ORANGE4': <Quantity_NameOfColor.Quantity_NOC_ORANGE4: 359>, 'Quantity_NOC_ORANGERED': <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>, 'Quantity_NOC_ORANGERED1': <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>, 'Quantity_NOC_ORANGERED2': <Quantity_NameOfColor.Quantity_NOC_ORANGERED2: 361>, 'Quantity_NOC_ORANGERED3': <Quantity_NameOfColor.Quantity_NOC_ORANGERED3: 362>, 'Quantity_NOC_ORANGERED4': <Quantity_NameOfColor.Quantity_NOC_ORANGERED4: 363>, 'Quantity_NOC_ORCHID': <Quantity_NameOfColor.Quantity_NOC_ORCHID: 364>, 'Quantity_NOC_ORCHID1': <Quantity_NameOfColor.Quantity_NOC_ORCHID1: 365>, 'Quantity_NOC_ORCHID2': <Quantity_NameOfColor.Quantity_NOC_ORCHID2: 366>, 'Quantity_NOC_ORCHID3': <Quantity_NameOfColor.Quantity_NOC_ORCHID3: 367>, 'Quantity_NOC_ORCHID4': <Quantity_NameOfColor.Quantity_NOC_ORCHID4: 368>, 'Quantity_NOC_PALEGOLDENROD': <Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD: 369>, 'Quantity_NOC_PALEGREEN': <Quantity_NameOfColor.Quantity_NOC_PALEGREEN: 370>, 'Quantity_NOC_PALEGREEN1': <Quantity_NameOfColor.Quantity_NOC_PALEGREEN1: 371>, 'Quantity_NOC_PALEGREEN2': <Quantity_NameOfColor.Quantity_NOC_PALEGREEN2: 372>, 'Quantity_NOC_PALEGREEN3': <Quantity_NameOfColor.Quantity_NOC_PALEGREEN3: 373>, 'Quantity_NOC_PALEGREEN4': <Quantity_NameOfColor.Quantity_NOC_PALEGREEN4: 374>, 'Quantity_NOC_PALETURQUOISE': <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE: 375>, 'Quantity_NOC_PALETURQUOISE1': <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1: 376>, 'Quantity_NOC_PALETURQUOISE2': <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2: 377>, 'Quantity_NOC_PALETURQUOISE3': <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3: 378>, 'Quantity_NOC_PALETURQUOISE4': <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4: 379>, 'Quantity_NOC_PALEVIOLETRED': <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED: 380>, 'Quantity_NOC_PALEVIOLETRED1': <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1: 381>, 'Quantity_NOC_PALEVIOLETRED2': <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2: 382>, 'Quantity_NOC_PALEVIOLETRED3': <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3: 383>, 'Quantity_NOC_PALEVIOLETRED4': <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4: 384>, 'Quantity_NOC_PAPAYAWHIP': <Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP: 385>, 'Quantity_NOC_PEACHPUFF': <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF: 386>, 'Quantity_NOC_PEACHPUFF2': <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2: 387>, 'Quantity_NOC_PEACHPUFF3': <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3: 388>, 'Quantity_NOC_PEACHPUFF4': <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4: 389>, 'Quantity_NOC_PERU': <Quantity_NameOfColor.Quantity_NOC_PERU: 390>, 'Quantity_NOC_PINK': <Quantity_NameOfColor.Quantity_NOC_PINK: 391>, 'Quantity_NOC_PINK1': <Quantity_NameOfColor.Quantity_NOC_PINK1: 392>, 'Quantity_NOC_PINK2': <Quantity_NameOfColor.Quantity_NOC_PINK2: 393>, 'Quantity_NOC_PINK3': <Quantity_NameOfColor.Quantity_NOC_PINK3: 394>, 'Quantity_NOC_PINK4': <Quantity_NameOfColor.Quantity_NOC_PINK4: 395>, 'Quantity_NOC_PLUM': <Quantity_NameOfColor.Quantity_NOC_PLUM: 396>, 'Quantity_NOC_PLUM1': <Quantity_NameOfColor.Quantity_NOC_PLUM1: 397>, 'Quantity_NOC_PLUM2': <Quantity_NameOfColor.Quantity_NOC_PLUM2: 398>, 'Quantity_NOC_PLUM3': <Quantity_NameOfColor.Quantity_NOC_PLUM3: 399>, 'Quantity_NOC_PLUM4': <Quantity_NameOfColor.Quantity_NOC_PLUM4: 400>, 'Quantity_NOC_POWDERBLUE': <Quantity_NameOfColor.Quantity_NOC_POWDERBLUE: 401>, 'Quantity_NOC_PURPLE': <Quantity_NameOfColor.Quantity_NOC_PURPLE: 402>, 'Quantity_NOC_PURPLE1': <Quantity_NameOfColor.Quantity_NOC_PURPLE1: 403>, 'Quantity_NOC_PURPLE2': <Quantity_NameOfColor.Quantity_NOC_PURPLE2: 404>, 'Quantity_NOC_PURPLE3': <Quantity_NameOfColor.Quantity_NOC_PURPLE3: 405>, 'Quantity_NOC_PURPLE4': <Quantity_NameOfColor.Quantity_NOC_PURPLE4: 406>, 'Quantity_NOC_RED': <Quantity_NameOfColor.Quantity_NOC_RED: 407>, 'Quantity_NOC_RED1': <Quantity_NameOfColor.Quantity_NOC_RED: 407>, 'Quantity_NOC_RED2': <Quantity_NameOfColor.Quantity_NOC_RED2: 408>, 'Quantity_NOC_RED3': <Quantity_NameOfColor.Quantity_NOC_RED3: 409>, 'Quantity_NOC_RED4': <Quantity_NameOfColor.Quantity_NOC_RED4: 410>, 'Quantity_NOC_ROSYBROWN': <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN: 411>, 'Quantity_NOC_ROSYBROWN1': <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1: 412>, 'Quantity_NOC_ROSYBROWN2': <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2: 413>, 'Quantity_NOC_ROSYBROWN3': <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3: 414>, 'Quantity_NOC_ROSYBROWN4': <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4: 415>, 'Quantity_NOC_ROYALBLUE': <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE: 416>, 'Quantity_NOC_ROYALBLUE1': <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1: 417>, 'Quantity_NOC_ROYALBLUE2': <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2: 418>, 'Quantity_NOC_ROYALBLUE3': <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3: 419>, 'Quantity_NOC_ROYALBLUE4': <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4: 420>, 'Quantity_NOC_SADDLEBROWN': <Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN: 421>, 'Quantity_NOC_SALMON': <Quantity_NameOfColor.Quantity_NOC_SALMON: 422>, 'Quantity_NOC_SALMON1': <Quantity_NameOfColor.Quantity_NOC_SALMON1: 423>, 'Quantity_NOC_SALMON2': <Quantity_NameOfColor.Quantity_NOC_SALMON2: 424>, 'Quantity_NOC_SALMON3': <Quantity_NameOfColor.Quantity_NOC_SALMON3: 425>, 'Quantity_NOC_SALMON4': <Quantity_NameOfColor.Quantity_NOC_SALMON4: 426>, 'Quantity_NOC_SANDYBROWN': <Quantity_NameOfColor.Quantity_NOC_SANDYBROWN: 427>, 'Quantity_NOC_SEAGREEN': <Quantity_NameOfColor.Quantity_NOC_SEAGREEN: 428>, 'Quantity_NOC_SEAGREEN1': <Quantity_NameOfColor.Quantity_NOC_SEAGREEN1: 429>, 'Quantity_NOC_SEAGREEN2': <Quantity_NameOfColor.Quantity_NOC_SEAGREEN2: 430>, 'Quantity_NOC_SEAGREEN3': <Quantity_NameOfColor.Quantity_NOC_SEAGREEN3: 431>, 'Quantity_NOC_SEAGREEN4': <Quantity_NameOfColor.Quantity_NOC_SEAGREEN4: 432>, 'Quantity_NOC_SEASHELL': <Quantity_NameOfColor.Quantity_NOC_SEASHELL: 433>, 'Quantity_NOC_SEASHELL2': <Quantity_NameOfColor.Quantity_NOC_SEASHELL2: 434>, 'Quantity_NOC_SEASHELL3': <Quantity_NameOfColor.Quantity_NOC_SEASHELL3: 435>, 'Quantity_NOC_SEASHELL4': <Quantity_NameOfColor.Quantity_NOC_SEASHELL4: 436>, 'Quantity_NOC_BEET': <Quantity_NameOfColor.Quantity_NOC_BEET: 437>, 'Quantity_NOC_TEAL': <Quantity_NameOfColor.Quantity_NOC_TEAL: 438>, 'Quantity_NOC_SIENNA': <Quantity_NameOfColor.Quantity_NOC_SIENNA: 439>, 'Quantity_NOC_SIENNA1': <Quantity_NameOfColor.Quantity_NOC_SIENNA1: 440>, 'Quantity_NOC_SIENNA2': <Quantity_NameOfColor.Quantity_NOC_SIENNA2: 441>, 'Quantity_NOC_SIENNA3': <Quantity_NameOfColor.Quantity_NOC_SIENNA3: 442>, 'Quantity_NOC_SIENNA4': <Quantity_NameOfColor.Quantity_NOC_SIENNA4: 443>, 'Quantity_NOC_SKYBLUE': <Quantity_NameOfColor.Quantity_NOC_SKYBLUE: 444>, 'Quantity_NOC_SKYBLUE1': <Quantity_NameOfColor.Quantity_NOC_SKYBLUE1: 445>, 'Quantity_NOC_SKYBLUE2': <Quantity_NameOfColor.Quantity_NOC_SKYBLUE2: 446>, 'Quantity_NOC_SKYBLUE3': <Quantity_NameOfColor.Quantity_NOC_SKYBLUE3: 447>, 'Quantity_NOC_SKYBLUE4': <Quantity_NameOfColor.Quantity_NOC_SKYBLUE4: 448>, 'Quantity_NOC_SLATEBLUE': <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE: 449>, 'Quantity_NOC_SLATEBLUE1': <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1: 450>, 'Quantity_NOC_SLATEBLUE2': <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2: 451>, 'Quantity_NOC_SLATEBLUE3': <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3: 452>, 'Quantity_NOC_SLATEBLUE4': <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4: 453>, 'Quantity_NOC_SLATEGRAY1': <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1: 454>, 'Quantity_NOC_SLATEGRAY2': <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2: 455>, 'Quantity_NOC_SLATEGRAY3': <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3: 456>, 'Quantity_NOC_SLATEGRAY4': <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4: 457>, 'Quantity_NOC_SLATEGRAY': <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY: 458>, 'Quantity_NOC_SNOW': <Quantity_NameOfColor.Quantity_NOC_SNOW: 459>, 'Quantity_NOC_SNOW2': <Quantity_NameOfColor.Quantity_NOC_SNOW2: 460>, 'Quantity_NOC_SNOW3': <Quantity_NameOfColor.Quantity_NOC_SNOW3: 461>, 'Quantity_NOC_SNOW4': <Quantity_NameOfColor.Quantity_NOC_SNOW4: 462>, 'Quantity_NOC_SPRINGGREEN': <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN: 463>, 'Quantity_NOC_SPRINGGREEN2': <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2: 464>, 'Quantity_NOC_SPRINGGREEN3': <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3: 465>, 'Quantity_NOC_SPRINGGREEN4': <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4: 466>, 'Quantity_NOC_STEELBLUE': <Quantity_NameOfColor.Quantity_NOC_STEELBLUE: 467>, 'Quantity_NOC_STEELBLUE1': <Quantity_NameOfColor.Quantity_NOC_STEELBLUE1: 468>, 'Quantity_NOC_STEELBLUE2': <Quantity_NameOfColor.Quantity_NOC_STEELBLUE2: 469>, 'Quantity_NOC_STEELBLUE3': <Quantity_NameOfColor.Quantity_NOC_STEELBLUE3: 470>, 'Quantity_NOC_STEELBLUE4': <Quantity_NameOfColor.Quantity_NOC_STEELBLUE4: 471>, 'Quantity_NOC_TAN': <Quantity_NameOfColor.Quantity_NOC_TAN: 472>, 'Quantity_NOC_TAN1': <Quantity_NameOfColor.Quantity_NOC_TAN1: 473>, 'Quantity_NOC_TAN2': <Quantity_NameOfColor.Quantity_NOC_TAN2: 474>, 'Quantity_NOC_TAN3': <Quantity_NameOfColor.Quantity_NOC_TAN3: 475>, 'Quantity_NOC_TAN4': <Quantity_NameOfColor.Quantity_NOC_TAN4: 476>, 'Quantity_NOC_THISTLE': <Quantity_NameOfColor.Quantity_NOC_THISTLE: 477>, 'Quantity_NOC_THISTLE1': <Quantity_NameOfColor.Quantity_NOC_THISTLE1: 478>, 'Quantity_NOC_THISTLE2': <Quantity_NameOfColor.Quantity_NOC_THISTLE2: 479>, 'Quantity_NOC_THISTLE3': <Quantity_NameOfColor.Quantity_NOC_THISTLE3: 480>, 'Quantity_NOC_THISTLE4': <Quantity_NameOfColor.Quantity_NOC_THISTLE4: 481>, 'Quantity_NOC_TOMATO': <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>, 'Quantity_NOC_TOMATO1': <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>, 'Quantity_NOC_TOMATO2': <Quantity_NameOfColor.Quantity_NOC_TOMATO2: 483>, 'Quantity_NOC_TOMATO3': <Quantity_NameOfColor.Quantity_NOC_TOMATO3: 484>, 'Quantity_NOC_TOMATO4': <Quantity_NameOfColor.Quantity_NOC_TOMATO4: 485>, 'Quantity_NOC_TURQUOISE': <Quantity_NameOfColor.Quantity_NOC_TURQUOISE: 486>, 'Quantity_NOC_TURQUOISE1': <Quantity_NameOfColor.Quantity_NOC_TURQUOISE1: 487>, 'Quantity_NOC_TURQUOISE2': <Quantity_NameOfColor.Quantity_NOC_TURQUOISE2: 488>, 'Quantity_NOC_TURQUOISE3': <Quantity_NameOfColor.Quantity_NOC_TURQUOISE3: 489>, 'Quantity_NOC_TURQUOISE4': <Quantity_NameOfColor.Quantity_NOC_TURQUOISE4: 490>, 'Quantity_NOC_VIOLET': <Quantity_NameOfColor.Quantity_NOC_VIOLET: 491>, 'Quantity_NOC_VIOLETRED': <Quantity_NameOfColor.Quantity_NOC_VIOLETRED: 492>, 'Quantity_NOC_VIOLETRED1': <Quantity_NameOfColor.Quantity_NOC_VIOLETRED1: 493>, 'Quantity_NOC_VIOLETRED2': <Quantity_NameOfColor.Quantity_NOC_VIOLETRED2: 494>, 'Quantity_NOC_VIOLETRED3': <Quantity_NameOfColor.Quantity_NOC_VIOLETRED3: 495>, 'Quantity_NOC_VIOLETRED4': <Quantity_NameOfColor.Quantity_NOC_VIOLETRED4: 496>, 'Quantity_NOC_WHEAT': <Quantity_NameOfColor.Quantity_NOC_WHEAT: 497>, 'Quantity_NOC_WHEAT1': <Quantity_NameOfColor.Quantity_NOC_WHEAT1: 498>, 'Quantity_NOC_WHEAT2': <Quantity_NameOfColor.Quantity_NOC_WHEAT2: 499>, 'Quantity_NOC_WHEAT3': <Quantity_NameOfColor.Quantity_NOC_WHEAT3: 500>, 'Quantity_NOC_WHEAT4': <Quantity_NameOfColor.Quantity_NOC_WHEAT4: 501>, 'Quantity_NOC_WHITESMOKE': <Quantity_NameOfColor.Quantity_NOC_WHITESMOKE: 502>, 'Quantity_NOC_YELLOW': <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>, 'Quantity_NOC_YELLOW1': <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>, 'Quantity_NOC_YELLOW2': <Quantity_NameOfColor.Quantity_NOC_YELLOW2: 504>, 'Quantity_NOC_YELLOW3': <Quantity_NameOfColor.Quantity_NOC_YELLOW3: 505>, 'Quantity_NOC_YELLOW4': <Quantity_NameOfColor.Quantity_NOC_YELLOW4: 506>, 'Quantity_NOC_YELLOWGREEN': <Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN: 507>, 'Quantity_NOC_WHITE': <Quantity_NameOfColor.Quantity_NOC_WHITE: 508>}
    pass
class Quantity_Period():
    """
    Manages date intervals. For example, a Period object gives the interval between two dates. A period is expressed in seconds and microseconds.
    """
    def Add(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        Adds one Period to another one.
        """
    def IsEqual(self,anOther : Quantity_Period) -> bool: 
        """
        Returns TRUE if both <me> and <other> are equal.
        """
    def IsLonger(self,anOther : Quantity_Period) -> bool: 
        """
        Returns TRUE if <me> is longer then <other>.
        """
    def IsShorter(self,anOther : Quantity_Period) -> bool: 
        """
        Returns TRUE if <me> is shorter than <other>.
        """
    @staticmethod
    @overload
    def IsValid_s(ss : int,mics : int=0) -> bool: 
        """
        Checks the validity of a Period in form (dd,hh,mn,ss,mil,mic) With: 0 <= dd 0 <= hh 0 <= mn 0 <= ss 0 <= mis 0 <= mics

        Checks the validity of a Period in form (ss,mic) With: 0 <= ss 0 <= mics
        """
    @staticmethod
    @overload
    def IsValid_s(dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> bool: ...
    @overload
    def SetValues(self,ss : int,mics : int=0) -> None: 
        """
        Assigns to this period the time interval defined - with dd days, hh hours, mn minutes, ss seconds, mis (defaulted to 0) milliseconds and mics (defaulted to 0) microseconds; or

        Assigns to this period the time interval defined - with Ss seconds and Mics (defaulted to 0) microseconds. Exceptions Quantity_PeriodDefinitionError: - if the number of seconds expressed either by: - dd days, hh hours, mn minutes and ss seconds, or - Ss is less than 0. - if the number of microseconds expressed either by: - mis milliseconds and mics microseconds, or - Mics is less than 0.
        """
    @overload
    def SetValues(self,dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: ...
    def Subtract(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        Subtracts one Period from another and returns the difference.
        """
    @overload
    def Values(self) -> Tuple[int, int, int, int, int, int]: 
        """
        Decomposes this period into a number of days,hours, minutes,seconds,milliseconds and microseconds Example of return values: 2 days, 15 hours, 0 minute , 0 second 0 millisecond and 0 microsecond

        Returns the number of seconds in Ss and the number of remainding microseconds in Mics of this period. Example of return values: 3600 seconds and 0 microseconds
        """
    @overload
    def Values(self) -> Tuple[int, int]: ...
    def __add__(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        None
        """
    @overload
    def __init__(self,ss : int,mics : int=0) -> None: ...
    @overload
    def __init__(self,dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: ...
    def __sub__(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        None
        """
    pass
class Quantity_PeriodDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Quantity', '__weakref__': <attribute '__weakref__' of 'Quantity_PeriodDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Quantity_PeriodDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class Quantity_PhysicalQuantity():
    """
    List of all physical quantities(Afnor)

    Members:

      Quantity_MASS

      Quantity_PLANEANGLE

      Quantity_SOLIDANGLE

      Quantity_LENGTH

      Quantity_AREA

      Quantity_VOLUME

      Quantity_SPEED

      Quantity_VELOCITY

      Quantity_ACCELERATION

      Quantity_ANGULARVELOCITY

      Quantity_FREQUENCY

      Quantity_TEMPERATURE

      Quantity_AMOUNTOFSUBSTANCE

      Quantity_DENSITY

      Quantity_MASSFLOW

      Quantity_VOLUMEFLOW

      Quantity_CONSUMPTION

      Quantity_MOMENTUM

      Quantity_KINETICMOMENT

      Quantity_MOMENTOFINERTIA

      Quantity_FORCE

      Quantity_MOMENTOFAFORCE

      Quantity_TORQUE

      Quantity_WEIGHT

      Quantity_PRESSURE

      Quantity_VISCOSITY

      Quantity_KINEMATICVISCOSITY

      Quantity_ENERGY

      Quantity_WORK

      Quantity_POWER

      Quantity_SURFACETENSION

      Quantity_COEFFICIENTOFEXPANSION

      Quantity_THERMALCONDUCTIVITY

      Quantity_SPECIFICHEATCAPACITY

      Quantity_ENTROPY

      Quantity_ENTHALPY

      Quantity_LUMINOUSINTENSITY

      Quantity_LUMINOUSFLUX

      Quantity_LUMINANCE

      Quantity_ILLUMINANCE

      Quantity_LUMINOUSEXPOSITION

      Quantity_LUMINOUSEFFICACITY

      Quantity_ELECTRICCHARGE

      Quantity_ELECTRICCURRENT

      Quantity_ELECTRICFIELDSTRENGTH

      Quantity_ELECTRICPOTENTIAL

      Quantity_ELECTRICCAPACITANCE

      Quantity_MAGNETICFLUX

      Quantity_MAGNETICFLUXDENSITY

      Quantity_MAGNETICFIELDSTRENGTH

      Quantity_RELUCTANCE

      Quantity_RESISTANCE

      Quantity_INDUCTANCE

      Quantity_CAPACITANCE

      Quantity_IMPEDANCE

      Quantity_ADMITTANCE

      Quantity_RESISTIVITY

      Quantity_CONDUCTIVITY

      Quantity_MOLARMASS

      Quantity_MOLARVOLUME

      Quantity_CONCENTRATION

      Quantity_MOLARCONCENTRATION

      Quantity_MOLARITY

      Quantity_SOUNDINTENSITY

      Quantity_ACOUSTICINTENSITY

      Quantity_ACTIVITY

      Quantity_ABSORBEDDOSE

      Quantity_DOSEEQUIVALENT
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    Quantity_ABSORBEDDOSE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE: 66>
    Quantity_ACCELERATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACCELERATION: 8>
    Quantity_ACOUSTICINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY: 64>
    Quantity_ACTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACTIVITY: 65>
    Quantity_ADMITTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ADMITTANCE: 55>
    Quantity_AMOUNTOFSUBSTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE: 12>
    Quantity_ANGULARVELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY: 9>
    Quantity_AREA: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_AREA: 4>
    Quantity_CAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CAPACITANCE: 53>
    Quantity_COEFFICIENTOFEXPANSION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION: 31>
    Quantity_CONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONCENTRATION: 60>
    Quantity_CONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY: 57>
    Quantity_CONSUMPTION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONSUMPTION: 16>
    Quantity_DENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_DENSITY: 13>
    Quantity_DOSEEQUIVALENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT: 67>
    Quantity_ELECTRICCAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE: 46>
    Quantity_ELECTRICCHARGE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE: 42>
    Quantity_ELECTRICCURRENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT: 43>
    Quantity_ELECTRICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH: 44>
    Quantity_ELECTRICPOTENTIAL: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL: 45>
    Quantity_ENERGY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENERGY: 27>
    Quantity_ENTHALPY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENTHALPY: 35>
    Quantity_ENTROPY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENTROPY: 34>
    Quantity_FORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_FORCE: 20>
    Quantity_FREQUENCY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_FREQUENCY: 10>
    Quantity_ILLUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ILLUMINANCE: 39>
    Quantity_IMPEDANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_IMPEDANCE: 54>
    Quantity_INDUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_INDUCTANCE: 52>
    Quantity_KINEMATICVISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY: 26>
    Quantity_KINETICMOMENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_KINETICMOMENT: 18>
    Quantity_LENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LENGTH: 3>
    Quantity_LUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINANCE: 38>
    Quantity_LUMINOUSEFFICACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY: 41>
    Quantity_LUMINOUSEXPOSITION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION: 40>
    Quantity_LUMINOUSFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX: 37>
    Quantity_LUMINOUSINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY: 36>
    Quantity_MAGNETICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH: 49>
    Quantity_MAGNETICFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX: 47>
    Quantity_MAGNETICFLUXDENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY: 48>
    Quantity_MASS: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MASS: 0>
    Quantity_MASSFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MASSFLOW: 14>
    Quantity_MOLARCONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION: 61>
    Quantity_MOLARITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARITY: 62>
    Quantity_MOLARMASS: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARMASS: 58>
    Quantity_MOLARVOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARVOLUME: 59>
    Quantity_MOMENTOFAFORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE: 21>
    Quantity_MOMENTOFINERTIA: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA: 19>
    Quantity_MOMENTUM: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTUM: 17>
    Quantity_PLANEANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_PLANEANGLE: 1>
    Quantity_POWER: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_POWER: 29>
    Quantity_PRESSURE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_PRESSURE: 24>
    Quantity_RELUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RELUCTANCE: 50>
    Quantity_RESISTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RESISTANCE: 51>
    Quantity_RESISTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RESISTIVITY: 56>
    Quantity_SOLIDANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SOLIDANGLE: 2>
    Quantity_SOUNDINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY: 63>
    Quantity_SPECIFICHEATCAPACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY: 33>
    Quantity_SPEED: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SPEED: 6>
    Quantity_SURFACETENSION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SURFACETENSION: 30>
    Quantity_TEMPERATURE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_TEMPERATURE: 11>
    Quantity_THERMALCONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY: 32>
    Quantity_TORQUE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_TORQUE: 22>
    Quantity_VELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VELOCITY: 7>
    Quantity_VISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VISCOSITY: 25>
    Quantity_VOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VOLUME: 5>
    Quantity_VOLUMEFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW: 15>
    Quantity_WEIGHT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_WEIGHT: 23>
    Quantity_WORK: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_WORK: 28>
    __entries: dict # value = {'Quantity_MASS': (<Quantity_PhysicalQuantity.Quantity_MASS: 0>, None), 'Quantity_PLANEANGLE': (<Quantity_PhysicalQuantity.Quantity_PLANEANGLE: 1>, None), 'Quantity_SOLIDANGLE': (<Quantity_PhysicalQuantity.Quantity_SOLIDANGLE: 2>, None), 'Quantity_LENGTH': (<Quantity_PhysicalQuantity.Quantity_LENGTH: 3>, None), 'Quantity_AREA': (<Quantity_PhysicalQuantity.Quantity_AREA: 4>, None), 'Quantity_VOLUME': (<Quantity_PhysicalQuantity.Quantity_VOLUME: 5>, None), 'Quantity_SPEED': (<Quantity_PhysicalQuantity.Quantity_SPEED: 6>, None), 'Quantity_VELOCITY': (<Quantity_PhysicalQuantity.Quantity_VELOCITY: 7>, None), 'Quantity_ACCELERATION': (<Quantity_PhysicalQuantity.Quantity_ACCELERATION: 8>, None), 'Quantity_ANGULARVELOCITY': (<Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY: 9>, None), 'Quantity_FREQUENCY': (<Quantity_PhysicalQuantity.Quantity_FREQUENCY: 10>, None), 'Quantity_TEMPERATURE': (<Quantity_PhysicalQuantity.Quantity_TEMPERATURE: 11>, None), 'Quantity_AMOUNTOFSUBSTANCE': (<Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE: 12>, None), 'Quantity_DENSITY': (<Quantity_PhysicalQuantity.Quantity_DENSITY: 13>, None), 'Quantity_MASSFLOW': (<Quantity_PhysicalQuantity.Quantity_MASSFLOW: 14>, None), 'Quantity_VOLUMEFLOW': (<Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW: 15>, None), 'Quantity_CONSUMPTION': (<Quantity_PhysicalQuantity.Quantity_CONSUMPTION: 16>, None), 'Quantity_MOMENTUM': (<Quantity_PhysicalQuantity.Quantity_MOMENTUM: 17>, None), 'Quantity_KINETICMOMENT': (<Quantity_PhysicalQuantity.Quantity_KINETICMOMENT: 18>, None), 'Quantity_MOMENTOFINERTIA': (<Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA: 19>, None), 'Quantity_FORCE': (<Quantity_PhysicalQuantity.Quantity_FORCE: 20>, None), 'Quantity_MOMENTOFAFORCE': (<Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE: 21>, None), 'Quantity_TORQUE': (<Quantity_PhysicalQuantity.Quantity_TORQUE: 22>, None), 'Quantity_WEIGHT': (<Quantity_PhysicalQuantity.Quantity_WEIGHT: 23>, None), 'Quantity_PRESSURE': (<Quantity_PhysicalQuantity.Quantity_PRESSURE: 24>, None), 'Quantity_VISCOSITY': (<Quantity_PhysicalQuantity.Quantity_VISCOSITY: 25>, None), 'Quantity_KINEMATICVISCOSITY': (<Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY: 26>, None), 'Quantity_ENERGY': (<Quantity_PhysicalQuantity.Quantity_ENERGY: 27>, None), 'Quantity_WORK': (<Quantity_PhysicalQuantity.Quantity_WORK: 28>, None), 'Quantity_POWER': (<Quantity_PhysicalQuantity.Quantity_POWER: 29>, None), 'Quantity_SURFACETENSION': (<Quantity_PhysicalQuantity.Quantity_SURFACETENSION: 30>, None), 'Quantity_COEFFICIENTOFEXPANSION': (<Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION: 31>, None), 'Quantity_THERMALCONDUCTIVITY': (<Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY: 32>, None), 'Quantity_SPECIFICHEATCAPACITY': (<Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY: 33>, None), 'Quantity_ENTROPY': (<Quantity_PhysicalQuantity.Quantity_ENTROPY: 34>, None), 'Quantity_ENTHALPY': (<Quantity_PhysicalQuantity.Quantity_ENTHALPY: 35>, None), 'Quantity_LUMINOUSINTENSITY': (<Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY: 36>, None), 'Quantity_LUMINOUSFLUX': (<Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX: 37>, None), 'Quantity_LUMINANCE': (<Quantity_PhysicalQuantity.Quantity_LUMINANCE: 38>, None), 'Quantity_ILLUMINANCE': (<Quantity_PhysicalQuantity.Quantity_ILLUMINANCE: 39>, None), 'Quantity_LUMINOUSEXPOSITION': (<Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION: 40>, None), 'Quantity_LUMINOUSEFFICACITY': (<Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY: 41>, None), 'Quantity_ELECTRICCHARGE': (<Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE: 42>, None), 'Quantity_ELECTRICCURRENT': (<Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT: 43>, None), 'Quantity_ELECTRICFIELDSTRENGTH': (<Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH: 44>, None), 'Quantity_ELECTRICPOTENTIAL': (<Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL: 45>, None), 'Quantity_ELECTRICCAPACITANCE': (<Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE: 46>, None), 'Quantity_MAGNETICFLUX': (<Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX: 47>, None), 'Quantity_MAGNETICFLUXDENSITY': (<Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY: 48>, None), 'Quantity_MAGNETICFIELDSTRENGTH': (<Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH: 49>, None), 'Quantity_RELUCTANCE': (<Quantity_PhysicalQuantity.Quantity_RELUCTANCE: 50>, None), 'Quantity_RESISTANCE': (<Quantity_PhysicalQuantity.Quantity_RESISTANCE: 51>, None), 'Quantity_INDUCTANCE': (<Quantity_PhysicalQuantity.Quantity_INDUCTANCE: 52>, None), 'Quantity_CAPACITANCE': (<Quantity_PhysicalQuantity.Quantity_CAPACITANCE: 53>, None), 'Quantity_IMPEDANCE': (<Quantity_PhysicalQuantity.Quantity_IMPEDANCE: 54>, None), 'Quantity_ADMITTANCE': (<Quantity_PhysicalQuantity.Quantity_ADMITTANCE: 55>, None), 'Quantity_RESISTIVITY': (<Quantity_PhysicalQuantity.Quantity_RESISTIVITY: 56>, None), 'Quantity_CONDUCTIVITY': (<Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY: 57>, None), 'Quantity_MOLARMASS': (<Quantity_PhysicalQuantity.Quantity_MOLARMASS: 58>, None), 'Quantity_MOLARVOLUME': (<Quantity_PhysicalQuantity.Quantity_MOLARVOLUME: 59>, None), 'Quantity_CONCENTRATION': (<Quantity_PhysicalQuantity.Quantity_CONCENTRATION: 60>, None), 'Quantity_MOLARCONCENTRATION': (<Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION: 61>, None), 'Quantity_MOLARITY': (<Quantity_PhysicalQuantity.Quantity_MOLARITY: 62>, None), 'Quantity_SOUNDINTENSITY': (<Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY: 63>, None), 'Quantity_ACOUSTICINTENSITY': (<Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY: 64>, None), 'Quantity_ACTIVITY': (<Quantity_PhysicalQuantity.Quantity_ACTIVITY: 65>, None), 'Quantity_ABSORBEDDOSE': (<Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE: 66>, None), 'Quantity_DOSEEQUIVALENT': (<Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT: 67>, None)}
    __members__: dict # value = {'Quantity_MASS': <Quantity_PhysicalQuantity.Quantity_MASS: 0>, 'Quantity_PLANEANGLE': <Quantity_PhysicalQuantity.Quantity_PLANEANGLE: 1>, 'Quantity_SOLIDANGLE': <Quantity_PhysicalQuantity.Quantity_SOLIDANGLE: 2>, 'Quantity_LENGTH': <Quantity_PhysicalQuantity.Quantity_LENGTH: 3>, 'Quantity_AREA': <Quantity_PhysicalQuantity.Quantity_AREA: 4>, 'Quantity_VOLUME': <Quantity_PhysicalQuantity.Quantity_VOLUME: 5>, 'Quantity_SPEED': <Quantity_PhysicalQuantity.Quantity_SPEED: 6>, 'Quantity_VELOCITY': <Quantity_PhysicalQuantity.Quantity_VELOCITY: 7>, 'Quantity_ACCELERATION': <Quantity_PhysicalQuantity.Quantity_ACCELERATION: 8>, 'Quantity_ANGULARVELOCITY': <Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY: 9>, 'Quantity_FREQUENCY': <Quantity_PhysicalQuantity.Quantity_FREQUENCY: 10>, 'Quantity_TEMPERATURE': <Quantity_PhysicalQuantity.Quantity_TEMPERATURE: 11>, 'Quantity_AMOUNTOFSUBSTANCE': <Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE: 12>, 'Quantity_DENSITY': <Quantity_PhysicalQuantity.Quantity_DENSITY: 13>, 'Quantity_MASSFLOW': <Quantity_PhysicalQuantity.Quantity_MASSFLOW: 14>, 'Quantity_VOLUMEFLOW': <Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW: 15>, 'Quantity_CONSUMPTION': <Quantity_PhysicalQuantity.Quantity_CONSUMPTION: 16>, 'Quantity_MOMENTUM': <Quantity_PhysicalQuantity.Quantity_MOMENTUM: 17>, 'Quantity_KINETICMOMENT': <Quantity_PhysicalQuantity.Quantity_KINETICMOMENT: 18>, 'Quantity_MOMENTOFINERTIA': <Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA: 19>, 'Quantity_FORCE': <Quantity_PhysicalQuantity.Quantity_FORCE: 20>, 'Quantity_MOMENTOFAFORCE': <Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE: 21>, 'Quantity_TORQUE': <Quantity_PhysicalQuantity.Quantity_TORQUE: 22>, 'Quantity_WEIGHT': <Quantity_PhysicalQuantity.Quantity_WEIGHT: 23>, 'Quantity_PRESSURE': <Quantity_PhysicalQuantity.Quantity_PRESSURE: 24>, 'Quantity_VISCOSITY': <Quantity_PhysicalQuantity.Quantity_VISCOSITY: 25>, 'Quantity_KINEMATICVISCOSITY': <Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY: 26>, 'Quantity_ENERGY': <Quantity_PhysicalQuantity.Quantity_ENERGY: 27>, 'Quantity_WORK': <Quantity_PhysicalQuantity.Quantity_WORK: 28>, 'Quantity_POWER': <Quantity_PhysicalQuantity.Quantity_POWER: 29>, 'Quantity_SURFACETENSION': <Quantity_PhysicalQuantity.Quantity_SURFACETENSION: 30>, 'Quantity_COEFFICIENTOFEXPANSION': <Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION: 31>, 'Quantity_THERMALCONDUCTIVITY': <Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY: 32>, 'Quantity_SPECIFICHEATCAPACITY': <Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY: 33>, 'Quantity_ENTROPY': <Quantity_PhysicalQuantity.Quantity_ENTROPY: 34>, 'Quantity_ENTHALPY': <Quantity_PhysicalQuantity.Quantity_ENTHALPY: 35>, 'Quantity_LUMINOUSINTENSITY': <Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY: 36>, 'Quantity_LUMINOUSFLUX': <Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX: 37>, 'Quantity_LUMINANCE': <Quantity_PhysicalQuantity.Quantity_LUMINANCE: 38>, 'Quantity_ILLUMINANCE': <Quantity_PhysicalQuantity.Quantity_ILLUMINANCE: 39>, 'Quantity_LUMINOUSEXPOSITION': <Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION: 40>, 'Quantity_LUMINOUSEFFICACITY': <Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY: 41>, 'Quantity_ELECTRICCHARGE': <Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE: 42>, 'Quantity_ELECTRICCURRENT': <Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT: 43>, 'Quantity_ELECTRICFIELDSTRENGTH': <Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH: 44>, 'Quantity_ELECTRICPOTENTIAL': <Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL: 45>, 'Quantity_ELECTRICCAPACITANCE': <Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE: 46>, 'Quantity_MAGNETICFLUX': <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX: 47>, 'Quantity_MAGNETICFLUXDENSITY': <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY: 48>, 'Quantity_MAGNETICFIELDSTRENGTH': <Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH: 49>, 'Quantity_RELUCTANCE': <Quantity_PhysicalQuantity.Quantity_RELUCTANCE: 50>, 'Quantity_RESISTANCE': <Quantity_PhysicalQuantity.Quantity_RESISTANCE: 51>, 'Quantity_INDUCTANCE': <Quantity_PhysicalQuantity.Quantity_INDUCTANCE: 52>, 'Quantity_CAPACITANCE': <Quantity_PhysicalQuantity.Quantity_CAPACITANCE: 53>, 'Quantity_IMPEDANCE': <Quantity_PhysicalQuantity.Quantity_IMPEDANCE: 54>, 'Quantity_ADMITTANCE': <Quantity_PhysicalQuantity.Quantity_ADMITTANCE: 55>, 'Quantity_RESISTIVITY': <Quantity_PhysicalQuantity.Quantity_RESISTIVITY: 56>, 'Quantity_CONDUCTIVITY': <Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY: 57>, 'Quantity_MOLARMASS': <Quantity_PhysicalQuantity.Quantity_MOLARMASS: 58>, 'Quantity_MOLARVOLUME': <Quantity_PhysicalQuantity.Quantity_MOLARVOLUME: 59>, 'Quantity_CONCENTRATION': <Quantity_PhysicalQuantity.Quantity_CONCENTRATION: 60>, 'Quantity_MOLARCONCENTRATION': <Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION: 61>, 'Quantity_MOLARITY': <Quantity_PhysicalQuantity.Quantity_MOLARITY: 62>, 'Quantity_SOUNDINTENSITY': <Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY: 63>, 'Quantity_ACOUSTICINTENSITY': <Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY: 64>, 'Quantity_ACTIVITY': <Quantity_PhysicalQuantity.Quantity_ACTIVITY: 65>, 'Quantity_ABSORBEDDOSE': <Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE: 66>, 'Quantity_DOSEEQUIVALENT': <Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT: 67>}
    pass
class Quantity_TypeOfColor():
    """
    Identifies color definition systems.

    Members:

      Quantity_TOC_RGB

      Quantity_TOC_sRGB

      Quantity_TOC_HLS

      Quantity_TOC_CIELab

      Quantity_TOC_CIELch
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
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
    Quantity_TOC_CIELab: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_CIELab: 3>
    Quantity_TOC_CIELch: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_CIELch: 4>
    Quantity_TOC_HLS: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_HLS: 2>
    Quantity_TOC_RGB: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_RGB: 0>
    Quantity_TOC_sRGB: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_sRGB: 1>
    __entries: dict # value = {'Quantity_TOC_RGB': (<Quantity_TypeOfColor.Quantity_TOC_RGB: 0>, None), 'Quantity_TOC_sRGB': (<Quantity_TypeOfColor.Quantity_TOC_sRGB: 1>, None), 'Quantity_TOC_HLS': (<Quantity_TypeOfColor.Quantity_TOC_HLS: 2>, None), 'Quantity_TOC_CIELab': (<Quantity_TypeOfColor.Quantity_TOC_CIELab: 3>, None), 'Quantity_TOC_CIELch': (<Quantity_TypeOfColor.Quantity_TOC_CIELch: 4>, None)}
    __members__: dict # value = {'Quantity_TOC_RGB': <Quantity_TypeOfColor.Quantity_TOC_RGB: 0>, 'Quantity_TOC_sRGB': <Quantity_TypeOfColor.Quantity_TOC_sRGB: 1>, 'Quantity_TOC_HLS': <Quantity_TypeOfColor.Quantity_TOC_HLS: 2>, 'Quantity_TOC_CIELab': <Quantity_TypeOfColor.Quantity_TOC_CIELab: 3>, 'Quantity_TOC_CIELch': <Quantity_TypeOfColor.Quantity_TOC_CIELch: 4>}
    pass
Quantity_ABSORBEDDOSE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE: 66>
Quantity_ACCELERATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACCELERATION: 8>
Quantity_ACOUSTICINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY: 64>
Quantity_ACTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ACTIVITY: 65>
Quantity_ADMITTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ADMITTANCE: 55>
Quantity_AMOUNTOFSUBSTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE: 12>
Quantity_ANGULARVELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY: 9>
Quantity_AREA: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_AREA: 4>
Quantity_CAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CAPACITANCE: 53>
Quantity_COEFFICIENTOFEXPANSION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION: 31>
Quantity_CONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONCENTRATION: 60>
Quantity_CONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY: 57>
Quantity_CONSUMPTION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_CONSUMPTION: 16>
Quantity_DENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_DENSITY: 13>
Quantity_DOSEEQUIVALENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT: 67>
Quantity_ELECTRICCAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE: 46>
Quantity_ELECTRICCHARGE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE: 42>
Quantity_ELECTRICCURRENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT: 43>
Quantity_ELECTRICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH: 44>
Quantity_ELECTRICPOTENTIAL: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL: 45>
Quantity_ENERGY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENERGY: 27>
Quantity_ENTHALPY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENTHALPY: 35>
Quantity_ENTROPY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ENTROPY: 34>
Quantity_FORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_FORCE: 20>
Quantity_FREQUENCY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_FREQUENCY: 10>
Quantity_ILLUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_ILLUMINANCE: 39>
Quantity_IMPEDANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_IMPEDANCE: 54>
Quantity_INDUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_INDUCTANCE: 52>
Quantity_KINEMATICVISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY: 26>
Quantity_KINETICMOMENT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_KINETICMOMENT: 18>
Quantity_LENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LENGTH: 3>
Quantity_LUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINANCE: 38>
Quantity_LUMINOUSEFFICACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY: 41>
Quantity_LUMINOUSEXPOSITION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION: 40>
Quantity_LUMINOUSFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX: 37>
Quantity_LUMINOUSINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY: 36>
Quantity_MAGNETICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH: 49>
Quantity_MAGNETICFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX: 47>
Quantity_MAGNETICFLUXDENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY: 48>
Quantity_MASS: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MASS: 0>
Quantity_MASSFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MASSFLOW: 14>
Quantity_MOLARCONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION: 61>
Quantity_MOLARITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARITY: 62>
Quantity_MOLARMASS: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARMASS: 58>
Quantity_MOLARVOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOLARVOLUME: 59>
Quantity_MOMENTOFAFORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE: 21>
Quantity_MOMENTOFINERTIA: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA: 19>
Quantity_MOMENTUM: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_MOMENTUM: 17>
Quantity_NOC_ALICEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ALICEBLUE: 3>
Quantity_NOC_ANTIQUEWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE: 4>
Quantity_NOC_ANTIQUEWHITE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1: 5>
Quantity_NOC_ANTIQUEWHITE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2: 6>
Quantity_NOC_ANTIQUEWHITE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3: 7>
Quantity_NOC_ANTIQUEWHITE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4: 8>
Quantity_NOC_AQUAMARINE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1: 9>
Quantity_NOC_AQUAMARINE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2: 10>
Quantity_NOC_AQUAMARINE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4: 11>
Quantity_NOC_AZURE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE: 12>
Quantity_NOC_AZURE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE2: 13>
Quantity_NOC_AZURE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE3: 14>
Quantity_NOC_AZURE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_AZURE4: 15>
Quantity_NOC_BEET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BEET: 437>
Quantity_NOC_BEIGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BEIGE: 16>
Quantity_NOC_BISQUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE: 17>
Quantity_NOC_BISQUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE2: 18>
Quantity_NOC_BISQUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE3: 19>
Quantity_NOC_BISQUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BISQUE4: 20>
Quantity_NOC_BLACK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLACK: 0>
Quantity_NOC_BLANCHEDALMOND: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND: 21>
Quantity_NOC_BLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>
Quantity_NOC_BLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE: 22>
Quantity_NOC_BLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE2: 23>
Quantity_NOC_BLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE3: 24>
Quantity_NOC_BLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUE4: 25>
Quantity_NOC_BLUEVIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET: 26>
Quantity_NOC_BROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN: 27>
Quantity_NOC_BROWN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN1: 28>
Quantity_NOC_BROWN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN2: 29>
Quantity_NOC_BROWN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN3: 30>
Quantity_NOC_BROWN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BROWN4: 31>
Quantity_NOC_BURLYWOOD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD: 32>
Quantity_NOC_BURLYWOOD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1: 33>
Quantity_NOC_BURLYWOOD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2: 34>
Quantity_NOC_BURLYWOOD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3: 35>
Quantity_NOC_BURLYWOOD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4: 36>
Quantity_NOC_CADETBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE: 37>
Quantity_NOC_CADETBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE1: 38>
Quantity_NOC_CADETBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE2: 39>
Quantity_NOC_CADETBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE3: 40>
Quantity_NOC_CADETBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CADETBLUE4: 41>
Quantity_NOC_CHARTREUSE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>
Quantity_NOC_CHARTREUSE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE: 42>
Quantity_NOC_CHARTREUSE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2: 43>
Quantity_NOC_CHARTREUSE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3: 44>
Quantity_NOC_CHARTREUSE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4: 45>
Quantity_NOC_CHOCOLATE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE: 46>
Quantity_NOC_CHOCOLATE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1: 47>
Quantity_NOC_CHOCOLATE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2: 48>
Quantity_NOC_CHOCOLATE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3: 49>
Quantity_NOC_CHOCOLATE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4: 50>
Quantity_NOC_CORAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL: 51>
Quantity_NOC_CORAL1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL1: 52>
Quantity_NOC_CORAL2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL2: 53>
Quantity_NOC_CORAL3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL3: 54>
Quantity_NOC_CORAL4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORAL4: 55>
Quantity_NOC_CORNFLOWERBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE: 56>
Quantity_NOC_CORNSILK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK1: 57>
Quantity_NOC_CORNSILK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK2: 58>
Quantity_NOC_CORNSILK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK3: 59>
Quantity_NOC_CORNSILK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CORNSILK4: 60>
Quantity_NOC_CYAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>
Quantity_NOC_CYAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN: 61>
Quantity_NOC_CYAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN2: 62>
Quantity_NOC_CYAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN3: 63>
Quantity_NOC_CYAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_CYAN4: 64>
Quantity_NOC_DARKGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD: 65>
Quantity_NOC_DARKGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1: 66>
Quantity_NOC_DARKGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2: 67>
Quantity_NOC_DARKGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3: 68>
Quantity_NOC_DARKGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4: 69>
Quantity_NOC_DARKGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKGREEN: 70>
Quantity_NOC_DARKKHAKI: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKKHAKI: 71>
Quantity_NOC_DARKOLIVEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN: 72>
Quantity_NOC_DARKOLIVEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1: 73>
Quantity_NOC_DARKOLIVEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2: 74>
Quantity_NOC_DARKOLIVEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3: 75>
Quantity_NOC_DARKOLIVEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4: 76>
Quantity_NOC_DARKORANGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE: 77>
Quantity_NOC_DARKORANGE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE1: 78>
Quantity_NOC_DARKORANGE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE2: 79>
Quantity_NOC_DARKORANGE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE3: 80>
Quantity_NOC_DARKORANGE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORANGE4: 81>
Quantity_NOC_DARKORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID: 82>
Quantity_NOC_DARKORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID1: 83>
Quantity_NOC_DARKORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID2: 84>
Quantity_NOC_DARKORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID3: 85>
Quantity_NOC_DARKORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKORCHID4: 86>
Quantity_NOC_DARKSALMON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSALMON: 87>
Quantity_NOC_DARKSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN: 88>
Quantity_NOC_DARKSEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1: 89>
Quantity_NOC_DARKSEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2: 90>
Quantity_NOC_DARKSEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3: 91>
Quantity_NOC_DARKSEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4: 92>
Quantity_NOC_DARKSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE: 93>
Quantity_NOC_DARKSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY: 98>
Quantity_NOC_DARKSLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1: 94>
Quantity_NOC_DARKSLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2: 95>
Quantity_NOC_DARKSLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3: 96>
Quantity_NOC_DARKSLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4: 97>
Quantity_NOC_DARKTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE: 99>
Quantity_NOC_DARKVIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DARKVIOLET: 100>
Quantity_NOC_DEEPPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK: 101>
Quantity_NOC_DEEPPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK2: 102>
Quantity_NOC_DEEPPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK3: 103>
Quantity_NOC_DEEPPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPPINK4: 104>
Quantity_NOC_DEEPSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1: 105>
Quantity_NOC_DEEPSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2: 106>
Quantity_NOC_DEEPSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3: 107>
Quantity_NOC_DEEPSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4: 108>
Quantity_NOC_DODGERBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1: 109>
Quantity_NOC_DODGERBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2: 110>
Quantity_NOC_DODGERBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3: 111>
Quantity_NOC_DODGERBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4: 112>
Quantity_NOC_FIREBRICK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK: 113>
Quantity_NOC_FIREBRICK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK1: 114>
Quantity_NOC_FIREBRICK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK2: 115>
Quantity_NOC_FIREBRICK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK3: 116>
Quantity_NOC_FIREBRICK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FIREBRICK4: 117>
Quantity_NOC_FLORALWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FLORALWHITE: 118>
Quantity_NOC_FORESTGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_FORESTGREEN: 119>
Quantity_NOC_GAINSBORO: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GAINSBORO: 120>
Quantity_NOC_GHOSTWHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE: 121>
Quantity_NOC_GOLD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>
Quantity_NOC_GOLD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD: 122>
Quantity_NOC_GOLD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD2: 123>
Quantity_NOC_GOLD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD3: 124>
Quantity_NOC_GOLD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLD4: 125>
Quantity_NOC_GOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD: 126>
Quantity_NOC_GOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD1: 127>
Quantity_NOC_GOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD2: 128>
Quantity_NOC_GOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD3: 129>
Quantity_NOC_GOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GOLDENROD4: 130>
Quantity_NOC_GRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY: 131>
Quantity_NOC_GRAY0: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY0: 132>
Quantity_NOC_GRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY1: 133>
Quantity_NOC_GRAY10: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY10: 142>
Quantity_NOC_GRAY11: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY11: 143>
Quantity_NOC_GRAY12: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY12: 144>
Quantity_NOC_GRAY13: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY13: 145>
Quantity_NOC_GRAY14: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY14: 146>
Quantity_NOC_GRAY15: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY15: 147>
Quantity_NOC_GRAY16: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY16: 148>
Quantity_NOC_GRAY17: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY17: 149>
Quantity_NOC_GRAY18: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY18: 150>
Quantity_NOC_GRAY19: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY19: 151>
Quantity_NOC_GRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY2: 134>
Quantity_NOC_GRAY20: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY20: 152>
Quantity_NOC_GRAY21: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY21: 153>
Quantity_NOC_GRAY22: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY22: 154>
Quantity_NOC_GRAY23: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY23: 155>
Quantity_NOC_GRAY24: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY24: 156>
Quantity_NOC_GRAY25: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY25: 157>
Quantity_NOC_GRAY26: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY26: 158>
Quantity_NOC_GRAY27: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY27: 159>
Quantity_NOC_GRAY28: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY28: 160>
Quantity_NOC_GRAY29: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY29: 161>
Quantity_NOC_GRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY3: 135>
Quantity_NOC_GRAY30: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY30: 162>
Quantity_NOC_GRAY31: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY31: 163>
Quantity_NOC_GRAY32: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY32: 164>
Quantity_NOC_GRAY33: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY33: 165>
Quantity_NOC_GRAY34: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY34: 166>
Quantity_NOC_GRAY35: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY35: 167>
Quantity_NOC_GRAY36: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY36: 168>
Quantity_NOC_GRAY37: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY37: 169>
Quantity_NOC_GRAY38: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY38: 170>
Quantity_NOC_GRAY39: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY39: 171>
Quantity_NOC_GRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY4: 136>
Quantity_NOC_GRAY40: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY40: 172>
Quantity_NOC_GRAY41: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY41: 173>
Quantity_NOC_GRAY42: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY42: 174>
Quantity_NOC_GRAY43: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY43: 175>
Quantity_NOC_GRAY44: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY44: 176>
Quantity_NOC_GRAY45: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY45: 177>
Quantity_NOC_GRAY46: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY46: 178>
Quantity_NOC_GRAY47: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY47: 179>
Quantity_NOC_GRAY48: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY48: 180>
Quantity_NOC_GRAY49: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY49: 181>
Quantity_NOC_GRAY5: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY5: 137>
Quantity_NOC_GRAY50: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY50: 182>
Quantity_NOC_GRAY51: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY51: 183>
Quantity_NOC_GRAY52: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY52: 184>
Quantity_NOC_GRAY53: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY53: 185>
Quantity_NOC_GRAY54: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY54: 186>
Quantity_NOC_GRAY55: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY55: 187>
Quantity_NOC_GRAY56: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY56: 188>
Quantity_NOC_GRAY57: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY57: 189>
Quantity_NOC_GRAY58: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY58: 190>
Quantity_NOC_GRAY59: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY59: 191>
Quantity_NOC_GRAY6: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY6: 138>
Quantity_NOC_GRAY60: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY60: 192>
Quantity_NOC_GRAY61: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY61: 193>
Quantity_NOC_GRAY62: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY62: 194>
Quantity_NOC_GRAY63: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY63: 195>
Quantity_NOC_GRAY64: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY64: 196>
Quantity_NOC_GRAY65: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY65: 197>
Quantity_NOC_GRAY66: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY66: 198>
Quantity_NOC_GRAY67: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY67: 199>
Quantity_NOC_GRAY68: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY68: 200>
Quantity_NOC_GRAY69: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY69: 201>
Quantity_NOC_GRAY7: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY7: 139>
Quantity_NOC_GRAY70: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY70: 202>
Quantity_NOC_GRAY71: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY71: 203>
Quantity_NOC_GRAY72: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY72: 204>
Quantity_NOC_GRAY73: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY73: 205>
Quantity_NOC_GRAY74: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY74: 206>
Quantity_NOC_GRAY75: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY75: 207>
Quantity_NOC_GRAY76: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY76: 208>
Quantity_NOC_GRAY77: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY77: 209>
Quantity_NOC_GRAY78: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY78: 210>
Quantity_NOC_GRAY79: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY79: 211>
Quantity_NOC_GRAY8: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY8: 140>
Quantity_NOC_GRAY80: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY80: 212>
Quantity_NOC_GRAY81: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY81: 213>
Quantity_NOC_GRAY82: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY82: 214>
Quantity_NOC_GRAY83: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY83: 215>
Quantity_NOC_GRAY85: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY85: 216>
Quantity_NOC_GRAY86: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY86: 217>
Quantity_NOC_GRAY87: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY87: 218>
Quantity_NOC_GRAY88: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY88: 219>
Quantity_NOC_GRAY89: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY89: 220>
Quantity_NOC_GRAY9: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY9: 141>
Quantity_NOC_GRAY90: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY90: 221>
Quantity_NOC_GRAY91: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY91: 222>
Quantity_NOC_GRAY92: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY92: 223>
Quantity_NOC_GRAY93: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY93: 224>
Quantity_NOC_GRAY94: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY94: 225>
Quantity_NOC_GRAY95: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY95: 226>
Quantity_NOC_GRAY97: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY97: 227>
Quantity_NOC_GRAY98: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY98: 228>
Quantity_NOC_GRAY99: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GRAY99: 229>
Quantity_NOC_GREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>
Quantity_NOC_GREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN: 230>
Quantity_NOC_GREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN2: 231>
Quantity_NOC_GREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN3: 232>
Quantity_NOC_GREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREEN4: 233>
Quantity_NOC_GREENYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_GREENYELLOW: 234>
Quantity_NOC_HONEYDEW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW: 235>
Quantity_NOC_HONEYDEW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW2: 236>
Quantity_NOC_HONEYDEW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW3: 237>
Quantity_NOC_HONEYDEW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HONEYDEW4: 238>
Quantity_NOC_HOTPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK: 239>
Quantity_NOC_HOTPINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK1: 240>
Quantity_NOC_HOTPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK2: 241>
Quantity_NOC_HOTPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK3: 242>
Quantity_NOC_HOTPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_HOTPINK4: 243>
Quantity_NOC_INDIANRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED: 244>
Quantity_NOC_INDIANRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED1: 245>
Quantity_NOC_INDIANRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED2: 246>
Quantity_NOC_INDIANRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED3: 247>
Quantity_NOC_INDIANRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_INDIANRED4: 248>
Quantity_NOC_IVORY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY: 249>
Quantity_NOC_IVORY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY2: 250>
Quantity_NOC_IVORY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY3: 251>
Quantity_NOC_IVORY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_IVORY4: 252>
Quantity_NOC_KHAKI: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI: 253>
Quantity_NOC_KHAKI1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI1: 254>
Quantity_NOC_KHAKI2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI2: 255>
Quantity_NOC_KHAKI3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI3: 256>
Quantity_NOC_KHAKI4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_KHAKI4: 257>
Quantity_NOC_LAVENDER: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDER: 258>
Quantity_NOC_LAVENDERBLUSH1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1: 259>
Quantity_NOC_LAVENDERBLUSH2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2: 260>
Quantity_NOC_LAVENDERBLUSH3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3: 261>
Quantity_NOC_LAVENDERBLUSH4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4: 262>
Quantity_NOC_LAWNGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LAWNGREEN: 263>
Quantity_NOC_LEMONCHIFFON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1: 264>
Quantity_NOC_LEMONCHIFFON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2: 265>
Quantity_NOC_LEMONCHIFFON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3: 266>
Quantity_NOC_LEMONCHIFFON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4: 267>
Quantity_NOC_LIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE: 268>
Quantity_NOC_LIGHTBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1: 269>
Quantity_NOC_LIGHTBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2: 270>
Quantity_NOC_LIGHTBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3: 271>
Quantity_NOC_LIGHTBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4: 272>
Quantity_NOC_LIGHTCORAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL: 273>
Quantity_NOC_LIGHTCYAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>
Quantity_NOC_LIGHTCYAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN: 274>
Quantity_NOC_LIGHTCYAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2: 275>
Quantity_NOC_LIGHTCYAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3: 276>
Quantity_NOC_LIGHTCYAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4: 277>
Quantity_NOC_LIGHTGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD: 278>
Quantity_NOC_LIGHTGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1: 279>
Quantity_NOC_LIGHTGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2: 280>
Quantity_NOC_LIGHTGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3: 281>
Quantity_NOC_LIGHTGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4: 282>
Quantity_NOC_LIGHTGOLDENRODYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW: 283>
Quantity_NOC_LIGHTGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY: 284>
Quantity_NOC_LIGHTPINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK: 285>
Quantity_NOC_LIGHTPINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1: 286>
Quantity_NOC_LIGHTPINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2: 287>
Quantity_NOC_LIGHTPINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3: 288>
Quantity_NOC_LIGHTPINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4: 289>
Quantity_NOC_LIGHTSALMON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1: 290>
Quantity_NOC_LIGHTSALMON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2: 291>
Quantity_NOC_LIGHTSALMON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3: 292>
Quantity_NOC_LIGHTSALMON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4: 293>
Quantity_NOC_LIGHTSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN: 294>
Quantity_NOC_LIGHTSKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE: 295>
Quantity_NOC_LIGHTSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1: 296>
Quantity_NOC_LIGHTSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2: 297>
Quantity_NOC_LIGHTSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3: 298>
Quantity_NOC_LIGHTSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4: 299>
Quantity_NOC_LIGHTSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE: 300>
Quantity_NOC_LIGHTSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY: 301>
Quantity_NOC_LIGHTSTEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE: 302>
Quantity_NOC_LIGHTSTEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1: 303>
Quantity_NOC_LIGHTSTEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2: 304>
Quantity_NOC_LIGHTSTEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3: 305>
Quantity_NOC_LIGHTSTEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4: 306>
Quantity_NOC_LIGHTYELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW: 307>
Quantity_NOC_LIGHTYELLOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2: 308>
Quantity_NOC_LIGHTYELLOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3: 309>
Quantity_NOC_LIGHTYELLOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4: 310>
Quantity_NOC_LIMEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LIMEGREEN: 311>
Quantity_NOC_LINEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_LINEN: 312>
Quantity_NOC_MAGENTA: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>
Quantity_NOC_MAGENTA1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA: 313>
Quantity_NOC_MAGENTA2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA2: 314>
Quantity_NOC_MAGENTA3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA3: 315>
Quantity_NOC_MAGENTA4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAGENTA4: 316>
Quantity_NOC_MAROON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON: 317>
Quantity_NOC_MAROON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON1: 318>
Quantity_NOC_MAROON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON2: 319>
Quantity_NOC_MAROON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON3: 320>
Quantity_NOC_MAROON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MAROON4: 321>
Quantity_NOC_MATRABLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MATRABLUE: 1>
Quantity_NOC_MATRAGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MATRAGRAY: 2>
Quantity_NOC_MEDIUMAQUAMARINE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE: 322>
Quantity_NOC_MEDIUMORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID: 323>
Quantity_NOC_MEDIUMORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1: 324>
Quantity_NOC_MEDIUMORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2: 325>
Quantity_NOC_MEDIUMORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3: 326>
Quantity_NOC_MEDIUMORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4: 327>
Quantity_NOC_MEDIUMPURPLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE: 328>
Quantity_NOC_MEDIUMPURPLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1: 329>
Quantity_NOC_MEDIUMPURPLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2: 330>
Quantity_NOC_MEDIUMPURPLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3: 331>
Quantity_NOC_MEDIUMPURPLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4: 332>
Quantity_NOC_MEDIUMSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN: 333>
Quantity_NOC_MEDIUMSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE: 334>
Quantity_NOC_MEDIUMSPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN: 335>
Quantity_NOC_MEDIUMTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE: 336>
Quantity_NOC_MEDIUMVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED: 337>
Quantity_NOC_MIDNIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE: 338>
Quantity_NOC_MINTCREAM: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MINTCREAM: 339>
Quantity_NOC_MISTYROSE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE: 340>
Quantity_NOC_MISTYROSE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE2: 341>
Quantity_NOC_MISTYROSE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE3: 342>
Quantity_NOC_MISTYROSE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MISTYROSE4: 343>
Quantity_NOC_MOCCASIN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_MOCCASIN: 344>
Quantity_NOC_NAVAJOWHITE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1: 345>
Quantity_NOC_NAVAJOWHITE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2: 346>
Quantity_NOC_NAVAJOWHITE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3: 347>
Quantity_NOC_NAVAJOWHITE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4: 348>
Quantity_NOC_NAVYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_NAVYBLUE: 349>
Quantity_NOC_OLDLACE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLDLACE: 350>
Quantity_NOC_OLIVEDRAB: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB: 351>
Quantity_NOC_OLIVEDRAB1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1: 352>
Quantity_NOC_OLIVEDRAB2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2: 353>
Quantity_NOC_OLIVEDRAB3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3: 354>
Quantity_NOC_OLIVEDRAB4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4: 355>
Quantity_NOC_ORANGE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>
Quantity_NOC_ORANGE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE: 356>
Quantity_NOC_ORANGE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE2: 357>
Quantity_NOC_ORANGE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE3: 358>
Quantity_NOC_ORANGE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGE4: 359>
Quantity_NOC_ORANGERED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>
Quantity_NOC_ORANGERED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED: 360>
Quantity_NOC_ORANGERED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED2: 361>
Quantity_NOC_ORANGERED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED3: 362>
Quantity_NOC_ORANGERED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORANGERED4: 363>
Quantity_NOC_ORCHID: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID: 364>
Quantity_NOC_ORCHID1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID1: 365>
Quantity_NOC_ORCHID2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID2: 366>
Quantity_NOC_ORCHID3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID3: 367>
Quantity_NOC_ORCHID4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ORCHID4: 368>
Quantity_NOC_PALEGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD: 369>
Quantity_NOC_PALEGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN: 370>
Quantity_NOC_PALEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN1: 371>
Quantity_NOC_PALEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN2: 372>
Quantity_NOC_PALEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN3: 373>
Quantity_NOC_PALEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEGREEN4: 374>
Quantity_NOC_PALETURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE: 375>
Quantity_NOC_PALETURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1: 376>
Quantity_NOC_PALETURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2: 377>
Quantity_NOC_PALETURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3: 378>
Quantity_NOC_PALETURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4: 379>
Quantity_NOC_PALEVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED: 380>
Quantity_NOC_PALEVIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1: 381>
Quantity_NOC_PALEVIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2: 382>
Quantity_NOC_PALEVIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3: 383>
Quantity_NOC_PALEVIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4: 384>
Quantity_NOC_PAPAYAWHIP: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP: 385>
Quantity_NOC_PEACHPUFF: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF: 386>
Quantity_NOC_PEACHPUFF2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2: 387>
Quantity_NOC_PEACHPUFF3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3: 388>
Quantity_NOC_PEACHPUFF4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4: 389>
Quantity_NOC_PERU: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PERU: 390>
Quantity_NOC_PINK: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK: 391>
Quantity_NOC_PINK1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK1: 392>
Quantity_NOC_PINK2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK2: 393>
Quantity_NOC_PINK3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK3: 394>
Quantity_NOC_PINK4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PINK4: 395>
Quantity_NOC_PLUM: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM: 396>
Quantity_NOC_PLUM1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM1: 397>
Quantity_NOC_PLUM2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM2: 398>
Quantity_NOC_PLUM3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM3: 399>
Quantity_NOC_PLUM4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PLUM4: 400>
Quantity_NOC_POWDERBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_POWDERBLUE: 401>
Quantity_NOC_PURPLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE: 402>
Quantity_NOC_PURPLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE1: 403>
Quantity_NOC_PURPLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE2: 404>
Quantity_NOC_PURPLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE3: 405>
Quantity_NOC_PURPLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_PURPLE4: 406>
Quantity_NOC_RED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED: 407>
Quantity_NOC_RED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED: 407>
Quantity_NOC_RED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED2: 408>
Quantity_NOC_RED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED3: 409>
Quantity_NOC_RED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_RED4: 410>
Quantity_NOC_ROSYBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN: 411>
Quantity_NOC_ROSYBROWN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1: 412>
Quantity_NOC_ROSYBROWN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2: 413>
Quantity_NOC_ROSYBROWN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3: 414>
Quantity_NOC_ROSYBROWN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4: 415>
Quantity_NOC_ROYALBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE: 416>
Quantity_NOC_ROYALBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1: 417>
Quantity_NOC_ROYALBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2: 418>
Quantity_NOC_ROYALBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3: 419>
Quantity_NOC_ROYALBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4: 420>
Quantity_NOC_SADDLEBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN: 421>
Quantity_NOC_SALMON: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON: 422>
Quantity_NOC_SALMON1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON1: 423>
Quantity_NOC_SALMON2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON2: 424>
Quantity_NOC_SALMON3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON3: 425>
Quantity_NOC_SALMON4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SALMON4: 426>
Quantity_NOC_SANDYBROWN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SANDYBROWN: 427>
Quantity_NOC_SEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN: 428>
Quantity_NOC_SEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN1: 429>
Quantity_NOC_SEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN2: 430>
Quantity_NOC_SEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN3: 431>
Quantity_NOC_SEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEAGREEN4: 432>
Quantity_NOC_SEASHELL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL: 433>
Quantity_NOC_SEASHELL2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL2: 434>
Quantity_NOC_SEASHELL3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL3: 435>
Quantity_NOC_SEASHELL4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SEASHELL4: 436>
Quantity_NOC_SIENNA: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA: 439>
Quantity_NOC_SIENNA1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA1: 440>
Quantity_NOC_SIENNA2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA2: 441>
Quantity_NOC_SIENNA3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA3: 442>
Quantity_NOC_SIENNA4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SIENNA4: 443>
Quantity_NOC_SKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE: 444>
Quantity_NOC_SKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE1: 445>
Quantity_NOC_SKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE2: 446>
Quantity_NOC_SKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE3: 447>
Quantity_NOC_SKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SKYBLUE4: 448>
Quantity_NOC_SLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE: 449>
Quantity_NOC_SLATEBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1: 450>
Quantity_NOC_SLATEBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2: 451>
Quantity_NOC_SLATEBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3: 452>
Quantity_NOC_SLATEBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4: 453>
Quantity_NOC_SLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY: 458>
Quantity_NOC_SLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1: 454>
Quantity_NOC_SLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2: 455>
Quantity_NOC_SLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3: 456>
Quantity_NOC_SLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4: 457>
Quantity_NOC_SNOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW: 459>
Quantity_NOC_SNOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW2: 460>
Quantity_NOC_SNOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW3: 461>
Quantity_NOC_SNOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SNOW4: 462>
Quantity_NOC_SPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN: 463>
Quantity_NOC_SPRINGGREEN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2: 464>
Quantity_NOC_SPRINGGREEN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3: 465>
Quantity_NOC_SPRINGGREEN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4: 466>
Quantity_NOC_STEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE: 467>
Quantity_NOC_STEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE1: 468>
Quantity_NOC_STEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE2: 469>
Quantity_NOC_STEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE3: 470>
Quantity_NOC_STEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_STEELBLUE4: 471>
Quantity_NOC_TAN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN: 472>
Quantity_NOC_TAN1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN1: 473>
Quantity_NOC_TAN2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN2: 474>
Quantity_NOC_TAN3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN3: 475>
Quantity_NOC_TAN4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TAN4: 476>
Quantity_NOC_TEAL: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TEAL: 438>
Quantity_NOC_THISTLE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE: 477>
Quantity_NOC_THISTLE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE1: 478>
Quantity_NOC_THISTLE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE2: 479>
Quantity_NOC_THISTLE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE3: 480>
Quantity_NOC_THISTLE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_THISTLE4: 481>
Quantity_NOC_TOMATO: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>
Quantity_NOC_TOMATO1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO: 482>
Quantity_NOC_TOMATO2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO2: 483>
Quantity_NOC_TOMATO3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO3: 484>
Quantity_NOC_TOMATO4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TOMATO4: 485>
Quantity_NOC_TURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE: 486>
Quantity_NOC_TURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE1: 487>
Quantity_NOC_TURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE2: 488>
Quantity_NOC_TURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE3: 489>
Quantity_NOC_TURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_TURQUOISE4: 490>
Quantity_NOC_VIOLET: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLET: 491>
Quantity_NOC_VIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED: 492>
Quantity_NOC_VIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED1: 493>
Quantity_NOC_VIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED2: 494>
Quantity_NOC_VIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED3: 495>
Quantity_NOC_VIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_VIOLETRED4: 496>
Quantity_NOC_WHEAT: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT: 497>
Quantity_NOC_WHEAT1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT1: 498>
Quantity_NOC_WHEAT2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT2: 499>
Quantity_NOC_WHEAT3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT3: 500>
Quantity_NOC_WHEAT4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHEAT4: 501>
Quantity_NOC_WHITE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHITE: 508>
Quantity_NOC_WHITESMOKE: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_WHITESMOKE: 502>
Quantity_NOC_YELLOW: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>
Quantity_NOC_YELLOW1: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW: 503>
Quantity_NOC_YELLOW2: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW2: 504>
Quantity_NOC_YELLOW3: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW3: 505>
Quantity_NOC_YELLOW4: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOW4: 506>
Quantity_NOC_YELLOWGREEN: OCP.Quantity.Quantity_NameOfColor # value = <Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN: 507>
Quantity_PLANEANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_PLANEANGLE: 1>
Quantity_POWER: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_POWER: 29>
Quantity_PRESSURE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_PRESSURE: 24>
Quantity_RELUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RELUCTANCE: 50>
Quantity_RESISTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RESISTANCE: 51>
Quantity_RESISTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_RESISTIVITY: 56>
Quantity_SOLIDANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SOLIDANGLE: 2>
Quantity_SOUNDINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY: 63>
Quantity_SPECIFICHEATCAPACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY: 33>
Quantity_SPEED: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SPEED: 6>
Quantity_SURFACETENSION: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_SURFACETENSION: 30>
Quantity_TEMPERATURE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_TEMPERATURE: 11>
Quantity_THERMALCONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY: 32>
Quantity_TOC_CIELab: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_CIELab: 3>
Quantity_TOC_CIELch: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_CIELch: 4>
Quantity_TOC_HLS: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_HLS: 2>
Quantity_TOC_RGB: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_RGB: 0>
Quantity_TOC_sRGB: OCP.Quantity.Quantity_TypeOfColor # value = <Quantity_TypeOfColor.Quantity_TOC_sRGB: 1>
Quantity_TORQUE: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_TORQUE: 22>
Quantity_VELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VELOCITY: 7>
Quantity_VISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VISCOSITY: 25>
Quantity_VOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VOLUME: 5>
Quantity_VOLUMEFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW: 15>
Quantity_WEIGHT: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_WEIGHT: 23>
Quantity_WORK: OCP.Quantity.Quantity_PhysicalQuantity # value = <Quantity_PhysicalQuantity.Quantity_WORK: 28>
