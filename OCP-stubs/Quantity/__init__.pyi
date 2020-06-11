import OCP.Quantity
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
import OCP.Graphic3d
import OCP.TCollection
__all__  = [
"Quantity_Array1OfColor",
"Quantity_Array2OfColor",
"Quantity_Color",
"Quantity_ColorDefinitionError",
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
"Quantity_TOC_HLS",
"Quantity_TOC_RGB",
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
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
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
    def __init__(self,theBegin : Quantity_Color,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Quantity_Array1OfColor) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
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
        Move assignment. This array will borrow all the data from theOther. The moved object will be left unitialized and should not be used anymore.
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
    def __init__(self,theOther : Quantity_Array2OfColor) -> None: ...
    @overload
    def __init__(self,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self,theBegin : Quantity_Color,theRowLower : int,theRowUpper : int,theColLower : int,theColUpper : int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Quantity_Color():
    """
    This class allows the definition of a colour. The names of the colours are from the X11 specification. color object may be used for numerous applicative purposes. A color is defined by: - its respective quantities of red, green and blue (R-G-B values), or - its hue angle and its values of lightness and saturation (H-L-S values). These two color definition systems are equivalent. Use this class in conjunction with: - the Quantity_TypeOfColor enumeration which identifies the color definition system you are using, - the Quantity_NameOfColor enumeration which lists numerous predefined colors and identifies them by their name.
    """
    @staticmethod
    def Argb2color_s(theARGB : int,theColor : Quantity_Color) -> None: 
        """
        Convert integer ARGB value to Color. Alpha bits are ignored
        """
    def Blue(self) -> float: 
        """
        Returns the Blue component (quantity of blue) of the color within range [0.0; 1.0].
        """
    def ChangeContrast(self,ADelta : float) -> None: 
        """
        Increases or decreases the contrast by <ADelta>. <ADelta> is a percentage. Any value greater than zero will increase the contrast. The variation is expressed as a percentage of the current value. It is a variation of the saturation.
        """
    def ChangeIntensity(self,ADelta : float) -> None: 
        """
        Increases or decreases the intensity by <ADelta>. <ADelta> is a percentage. Any value greater than zero will increase the intensity. The variation is expressed as a percentage of the current value. It is a variation of the lightness.
        """
    @staticmethod
    def Color2argb_s(theColor : Quantity_Color) -> Tuple[int]: 
        """
        Convert the Color value to ARGB integer value. theARGB has Alpha equal to zero, so the output is formatted as 0x00RRGGBB
        """
    @staticmethod
    def ColorFromHex_s(theHexColorString : str,theColor : Quantity_Color) -> bool: 
        """
        Parses the string as a hex color (like "#FF0" for short RGB color, or "#FFFF00" for RGB color)
        """
    @staticmethod
    @overload
    def ColorFromName_s(theName : str,theColor : Quantity_NameOfColor) -> bool: 
        """
        Finds color from predefined names. For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK. Returns false if name is unknown.

        Finds color from predefined names. For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK. Returns false if name is unknown.
        """
    @staticmethod
    @overload
    def ColorFromName_s(theColorNameString : str,theColor : Quantity_Color) -> bool: ...
    @staticmethod
    def ColorToHex_s(theColor : Quantity_Color,theToPrefixHash : bool=True) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns hex sRGB string in format "#FFAAFF".
        """
    def Delta(self,AColor : Quantity_Color) -> Tuple[float, float]: 
        """
        Returns the percentage change of contrast and intensity between <me> and <AColor>. <DC> and <DI> are percentages, either positive or negative. The calculation is with respect to the current value of <me> If <DC> is positive then <me> is more contrasty. If <DI> is positive then <me> is more intense.
        """
    def Distance(self,AColor : Quantity_Color) -> float: 
        """
        Returns the distance between two colours. It's a value between 0 and the square root of 3 (the black/white distance)
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    @staticmethod
    def Epsilon_s() -> float: 
        """
        Returns the specified value used to compare <me> and an other color in IsDifferent and in IsEqual methods.
        """
    def Green(self) -> float: 
        """
        Returns the Green component (quantity of green) of the color within range [0.0; 1.0].
        """
    @staticmethod
    def HlsRgb_s(H : float,L : float,S : float) -> Tuple[float, float, float]: 
        """
        Converts HLS components into RGB ones.
        """
    def Hue(self) -> float: 
        """
        Returns the Hue component (hue angle) of the color in degrees within range [0.0; 360.0], 0.0 being Red. -1.0 is a special value reserved for grayscale color (S should be 0.0)
        """
    def IsDifferent(self,Other : Quantity_Color) -> bool: 
        """
        Returns Standard_True if the distance between <me> and <Other> is greater than Epsilon ().
        """
    def IsEqual(self,Other : Quantity_Color) -> bool: 
        """
        Returns true if the Other color is - different from, or - equal to this color. Two colors are considered to be equal if their distance is no greater than Epsilon(). These methods are aliases of operator != and operator ==.
        """
    def Light(self) -> float: 
        """
        Returns the Light component (value of the lightness) of the color within range [0.0; 1.0].
        """
    def Name(self) -> Quantity_NameOfColor: 
        """
        Returns the name of the color defined by its quantities of red R, green G and blue B; more precisely this is the nearest color from the Quantity_NameOfColor enumeration. Exceptions Standard_OutOfRange if R, G or B is less than 0. or greater than 1.
        """
    @staticmethod
    def Name_s(R : float,G : float,B : float) -> Quantity_NameOfColor: 
        """
        Returns the name of the colour for which the RGB components are nearest to <R>, <G> and <B>.
        """
    def Red(self) -> float: 
        """
        Returns the Red component (quantity of red) of the color within range [0.0; 1.0].
        """
    @staticmethod
    def RgbHls_s(R : float,G : float,B : float) -> Tuple[float, float, float]: 
        """
        Converts RGB components into HLS ones.
        """
    def Saturation(self) -> float: 
        """
        Returns the Saturation component (value of the saturation) of the color within range [0.0; 1.0].
        """
    @staticmethod
    def SetEpsilon_s(AnEpsilon : float) -> None: 
        """
        Sets the specified value used to compare <me> and an other color in IsDifferent and in IsEqual methods. Warning: The default value is 0.0001
        """
    @overload
    def SetValues(self,AName : Quantity_NameOfColor) -> None: 
        """
        Updates the colour <me> from the definition of the colour <AName>.

        Updates a color according to the mode specified by theType. Quantity_TOC_RGB: - theR1 the value of Red within range [0.0; 1.0] - theR2 the value of Green within range [0.0; 1.0] - theR3 the value of Blue within range [0.0; 1.0]
        """
    @overload
    def SetValues(self,theR1 : float,theR2 : float,theR3 : float,theType : Quantity_TypeOfColor) -> None: ...
    def SquareDistance(self,AColor : Quantity_Color) -> float: 
        """
        Returns the square of distance between two colours.
        """
    @staticmethod
    def StringName_s(AColor : Quantity_NameOfColor) -> str: 
        """
        Returns the name of the color identified by AName in the Quantity_NameOfColor enumeration. For example, the name of the color which corresponds to Quantity_NOC_BLACK is "BLACK". Exceptions Standard_OutOfRange if AName in not known in the Quantity_NameOfColor enumeration.
        """
    @staticmethod
    def Test_s() -> None: 
        """
        Internal test
        """
    def Values(self,theType : Quantity_TypeOfColor) -> Tuple[float, float, float]: 
        """
        Returns in theR1, theR2 and theR3 the components of this color according to the color system definition theType. If theType is Quantity_TOC_RGB: - theR1 the value of Red between 0.0 and 1.0 - theR2 the value of Green between 0.0 and 1.0 - theR3 the value of Blue between 0.0 and 1.0 If theType is Quantity_TOC_HLS: - theR1 is the Hue (H) angle in degrees within range [0.0; 360.0], 0.0 being Red. -1.0 is a special value reserved for grayscale color (S should be 0.0). - theR2 is the Lightness (L) within range [0.0; 1.0] - theR3 is the Saturation (S) within range [0.0; 1.0]
        """
    @overload
    def __init__(self,AName : Quantity_NameOfColor) -> None: ...
    @overload
    def __init__(self,theRgb : OCP.Graphic3d.Graphic3d_Vec3) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theR1 : float,theR2 : float,theR3 : float,theType : Quantity_TypeOfColor) -> None: ...
    pass
class Quantity_ColorDefinitionError(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Quantity', '__weakref__': <attribute '__weakref__' of 'Quantity_ColorDefinitionError' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Quantity_ColorDefinitionError' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
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
        Parses the string as a hex color (like "#FF0" for short RGB color, "#FF0F" for short RGBA color, "#FFFF00" for RGB color, or "#FFFF00FF" for RGBA color)
        """
    @staticmethod
    def ColorFromName_s(theColorNameString : str,theColor : Quantity_ColorRGBA) -> bool: 
        """
        Finds color from predefined names. For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK. Returns false if name is unknown. An alpha component is set to 1.0.
        """
    @staticmethod
    def ColorToHex_s(theColor : Quantity_ColorRGBA,theToPrefixHash : bool=True) -> OCP.TCollection.TCollection_AsciiString: 
        """
        Returns hex sRGBA string in format "#RRGGBBAA".
        """
    def DumpJson(self,theOStream : Any,theDepth : int=-1) -> None: 
        """
        Dumps the content of me into the stream
        """
    def GetRGB(self) -> Quantity_Color: 
        """
        Return RGB color value.
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
    def __init__(self,theRgba : OCP.Graphic3d.Graphic3d_Vec4) -> None: ...
    @overload
    def __init__(self,theRed : float,theGreen : float,theBlue : float,theAlpha : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theRgb : Quantity_Color,theAlpha : float) -> None: ...
    @overload
    def __init__(self,theRgb : Quantity_Color) -> None: ...
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
        Returns true if a year is a leap year. The leap years are divisable by 4 and not by 100 except the years divisable by 400.
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
    def IsKind(self,theType : OCP.Standard.Standard_Type) -> bool: 
        """
        Returns true if this is an instance of Type or an instance of any class that inherits from Type. Note that multiple inheritance is not supported by OCCT RTTI mechanism.

        Returns true if this is an instance of TypeName or an instance of any class that inherits from TypeName. Note that multiple inheritance is not supported by OCCT RTTI mechanism.
        """
    @overload
    def IsKind(self,theTypeName : str) -> bool: ...
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
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theOther : Quantity_Array1OfColor) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int,theValue : Quantity_Color) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> iterator: ...
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

      Quantity_NOC_GRAY2

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

      Quantity_NOC_GRAY3

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

      Quantity_NOC_GRAY4

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

      Quantity_NOC_GRAY5

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

      Quantity_NOC_GRAY6

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

      Quantity_NOC_GRAY7

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

      Quantity_NOC_GRAY8

      Quantity_NOC_GRAY80

      Quantity_NOC_GRAY81

      Quantity_NOC_GRAY82

      Quantity_NOC_GRAY83

      Quantity_NOC_GRAY85

      Quantity_NOC_GRAY86

      Quantity_NOC_GRAY87

      Quantity_NOC_GRAY88

      Quantity_NOC_GRAY89

      Quantity_NOC_GRAY9

      Quantity_NOC_GRAY90

      Quantity_NOC_GRAY91

      Quantity_NOC_GRAY92

      Quantity_NOC_GRAY93

      Quantity_NOC_GRAY94

      Quantity_NOC_GRAY95

      Quantity_NOC_GREEN

      Quantity_NOC_GREEN1

      Quantity_NOC_GREEN2

      Quantity_NOC_GREEN3

      Quantity_NOC_GREEN4

      Quantity_NOC_GREENYELLOW

      Quantity_NOC_GRAY97

      Quantity_NOC_GRAY98

      Quantity_NOC_GRAY99

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
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Quantity_NOC_ALICEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ALICEBLUE
    Quantity_NOC_ANTIQUEWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE
    Quantity_NOC_ANTIQUEWHITE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1
    Quantity_NOC_ANTIQUEWHITE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2
    Quantity_NOC_ANTIQUEWHITE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3
    Quantity_NOC_ANTIQUEWHITE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4
    Quantity_NOC_AQUAMARINE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1
    Quantity_NOC_AQUAMARINE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2
    Quantity_NOC_AQUAMARINE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4
    Quantity_NOC_AZURE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE
    Quantity_NOC_AZURE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE2
    Quantity_NOC_AZURE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE3
    Quantity_NOC_AZURE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE4
    Quantity_NOC_BEET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BEET
    Quantity_NOC_BEIGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BEIGE
    Quantity_NOC_BISQUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE
    Quantity_NOC_BISQUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE2
    Quantity_NOC_BISQUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE3
    Quantity_NOC_BISQUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE4
    Quantity_NOC_BLACK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLACK
    Quantity_NOC_BLANCHEDALMOND: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND
    Quantity_NOC_BLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE1
    Quantity_NOC_BLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE2
    Quantity_NOC_BLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE3
    Quantity_NOC_BLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE4
    Quantity_NOC_BLUEVIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET
    Quantity_NOC_BROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN
    Quantity_NOC_BROWN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN1
    Quantity_NOC_BROWN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN2
    Quantity_NOC_BROWN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN3
    Quantity_NOC_BROWN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN4
    Quantity_NOC_BURLYWOOD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD
    Quantity_NOC_BURLYWOOD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1
    Quantity_NOC_BURLYWOOD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2
    Quantity_NOC_BURLYWOOD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3
    Quantity_NOC_BURLYWOOD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4
    Quantity_NOC_CADETBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE
    Quantity_NOC_CADETBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE1
    Quantity_NOC_CADETBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE2
    Quantity_NOC_CADETBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE3
    Quantity_NOC_CADETBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE4
    Quantity_NOC_CHARTREUSE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE
    Quantity_NOC_CHARTREUSE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE1
    Quantity_NOC_CHARTREUSE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2
    Quantity_NOC_CHARTREUSE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3
    Quantity_NOC_CHARTREUSE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4
    Quantity_NOC_CHOCOLATE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE
    Quantity_NOC_CHOCOLATE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1
    Quantity_NOC_CHOCOLATE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2
    Quantity_NOC_CHOCOLATE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3
    Quantity_NOC_CHOCOLATE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4
    Quantity_NOC_CORAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL
    Quantity_NOC_CORAL1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL1
    Quantity_NOC_CORAL2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL2
    Quantity_NOC_CORAL3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL3
    Quantity_NOC_CORAL4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL4
    Quantity_NOC_CORNFLOWERBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE
    Quantity_NOC_CORNSILK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK1
    Quantity_NOC_CORNSILK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK2
    Quantity_NOC_CORNSILK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK3
    Quantity_NOC_CORNSILK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK4
    Quantity_NOC_CYAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN1
    Quantity_NOC_CYAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN2
    Quantity_NOC_CYAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN3
    Quantity_NOC_CYAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN4
    Quantity_NOC_DARKGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD
    Quantity_NOC_DARKGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1
    Quantity_NOC_DARKGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2
    Quantity_NOC_DARKGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3
    Quantity_NOC_DARKGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4
    Quantity_NOC_DARKGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGREEN
    Quantity_NOC_DARKKHAKI: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKKHAKI
    Quantity_NOC_DARKOLIVEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN
    Quantity_NOC_DARKOLIVEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1
    Quantity_NOC_DARKOLIVEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2
    Quantity_NOC_DARKOLIVEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3
    Quantity_NOC_DARKOLIVEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4
    Quantity_NOC_DARKORANGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE
    Quantity_NOC_DARKORANGE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE1
    Quantity_NOC_DARKORANGE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE2
    Quantity_NOC_DARKORANGE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE3
    Quantity_NOC_DARKORANGE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE4
    Quantity_NOC_DARKORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID
    Quantity_NOC_DARKORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID1
    Quantity_NOC_DARKORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID2
    Quantity_NOC_DARKORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID3
    Quantity_NOC_DARKORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID4
    Quantity_NOC_DARKSALMON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSALMON
    Quantity_NOC_DARKSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN
    Quantity_NOC_DARKSEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1
    Quantity_NOC_DARKSEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2
    Quantity_NOC_DARKSEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3
    Quantity_NOC_DARKSEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4
    Quantity_NOC_DARKSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE
    Quantity_NOC_DARKSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY
    Quantity_NOC_DARKSLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1
    Quantity_NOC_DARKSLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2
    Quantity_NOC_DARKSLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3
    Quantity_NOC_DARKSLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4
    Quantity_NOC_DARKTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE
    Quantity_NOC_DARKVIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKVIOLET
    Quantity_NOC_DEEPPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK
    Quantity_NOC_DEEPPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK2
    Quantity_NOC_DEEPPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK3
    Quantity_NOC_DEEPPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK4
    Quantity_NOC_DEEPSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1
    Quantity_NOC_DEEPSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2
    Quantity_NOC_DEEPSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3
    Quantity_NOC_DEEPSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4
    Quantity_NOC_DODGERBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1
    Quantity_NOC_DODGERBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2
    Quantity_NOC_DODGERBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3
    Quantity_NOC_DODGERBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4
    Quantity_NOC_FIREBRICK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK
    Quantity_NOC_FIREBRICK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK1
    Quantity_NOC_FIREBRICK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK2
    Quantity_NOC_FIREBRICK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK3
    Quantity_NOC_FIREBRICK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK4
    Quantity_NOC_FLORALWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FLORALWHITE
    Quantity_NOC_FORESTGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FORESTGREEN
    Quantity_NOC_GAINSBORO: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GAINSBORO
    Quantity_NOC_GHOSTWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE
    Quantity_NOC_GOLD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD
    Quantity_NOC_GOLD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD1
    Quantity_NOC_GOLD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD2
    Quantity_NOC_GOLD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD3
    Quantity_NOC_GOLD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD4
    Quantity_NOC_GOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD
    Quantity_NOC_GOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD1
    Quantity_NOC_GOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD2
    Quantity_NOC_GOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD3
    Quantity_NOC_GOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD4
    Quantity_NOC_GRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY
    Quantity_NOC_GRAY0: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY0
    Quantity_NOC_GRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY1
    Quantity_NOC_GRAY10: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY10
    Quantity_NOC_GRAY11: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY11
    Quantity_NOC_GRAY12: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY12
    Quantity_NOC_GRAY13: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY13
    Quantity_NOC_GRAY14: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY14
    Quantity_NOC_GRAY15: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY15
    Quantity_NOC_GRAY16: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY16
    Quantity_NOC_GRAY17: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY17
    Quantity_NOC_GRAY18: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY18
    Quantity_NOC_GRAY19: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY19
    Quantity_NOC_GRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY2
    Quantity_NOC_GRAY20: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY20
    Quantity_NOC_GRAY21: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY21
    Quantity_NOC_GRAY22: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY22
    Quantity_NOC_GRAY23: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY23
    Quantity_NOC_GRAY24: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY24
    Quantity_NOC_GRAY25: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY25
    Quantity_NOC_GRAY26: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY26
    Quantity_NOC_GRAY27: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY27
    Quantity_NOC_GRAY28: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY28
    Quantity_NOC_GRAY29: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY29
    Quantity_NOC_GRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY3
    Quantity_NOC_GRAY30: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY30
    Quantity_NOC_GRAY31: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY31
    Quantity_NOC_GRAY32: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY32
    Quantity_NOC_GRAY33: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY33
    Quantity_NOC_GRAY34: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY34
    Quantity_NOC_GRAY35: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY35
    Quantity_NOC_GRAY36: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY36
    Quantity_NOC_GRAY37: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY37
    Quantity_NOC_GRAY38: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY38
    Quantity_NOC_GRAY39: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY39
    Quantity_NOC_GRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY4
    Quantity_NOC_GRAY40: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY40
    Quantity_NOC_GRAY41: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY41
    Quantity_NOC_GRAY42: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY42
    Quantity_NOC_GRAY43: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY43
    Quantity_NOC_GRAY44: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY44
    Quantity_NOC_GRAY45: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY45
    Quantity_NOC_GRAY46: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY46
    Quantity_NOC_GRAY47: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY47
    Quantity_NOC_GRAY48: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY48
    Quantity_NOC_GRAY49: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY49
    Quantity_NOC_GRAY5: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY5
    Quantity_NOC_GRAY50: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY50
    Quantity_NOC_GRAY51: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY51
    Quantity_NOC_GRAY52: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY52
    Quantity_NOC_GRAY53: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY53
    Quantity_NOC_GRAY54: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY54
    Quantity_NOC_GRAY55: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY55
    Quantity_NOC_GRAY56: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY56
    Quantity_NOC_GRAY57: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY57
    Quantity_NOC_GRAY58: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY58
    Quantity_NOC_GRAY59: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY59
    Quantity_NOC_GRAY6: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY6
    Quantity_NOC_GRAY60: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY60
    Quantity_NOC_GRAY61: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY61
    Quantity_NOC_GRAY62: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY62
    Quantity_NOC_GRAY63: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY63
    Quantity_NOC_GRAY64: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY64
    Quantity_NOC_GRAY65: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY65
    Quantity_NOC_GRAY66: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY66
    Quantity_NOC_GRAY67: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY67
    Quantity_NOC_GRAY68: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY68
    Quantity_NOC_GRAY69: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY69
    Quantity_NOC_GRAY7: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY7
    Quantity_NOC_GRAY70: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY70
    Quantity_NOC_GRAY71: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY71
    Quantity_NOC_GRAY72: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY72
    Quantity_NOC_GRAY73: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY73
    Quantity_NOC_GRAY74: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY74
    Quantity_NOC_GRAY75: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY75
    Quantity_NOC_GRAY76: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY76
    Quantity_NOC_GRAY77: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY77
    Quantity_NOC_GRAY78: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY78
    Quantity_NOC_GRAY79: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY79
    Quantity_NOC_GRAY8: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY8
    Quantity_NOC_GRAY80: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY80
    Quantity_NOC_GRAY81: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY81
    Quantity_NOC_GRAY82: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY82
    Quantity_NOC_GRAY83: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY83
    Quantity_NOC_GRAY85: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY85
    Quantity_NOC_GRAY86: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY86
    Quantity_NOC_GRAY87: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY87
    Quantity_NOC_GRAY88: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY88
    Quantity_NOC_GRAY89: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY89
    Quantity_NOC_GRAY9: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY9
    Quantity_NOC_GRAY90: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY90
    Quantity_NOC_GRAY91: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY91
    Quantity_NOC_GRAY92: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY92
    Quantity_NOC_GRAY93: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY93
    Quantity_NOC_GRAY94: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY94
    Quantity_NOC_GRAY95: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY95
    Quantity_NOC_GRAY97: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY97
    Quantity_NOC_GRAY98: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY98
    Quantity_NOC_GRAY99: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY99
    Quantity_NOC_GREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN
    Quantity_NOC_GREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN1
    Quantity_NOC_GREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN2
    Quantity_NOC_GREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN3
    Quantity_NOC_GREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN4
    Quantity_NOC_GREENYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREENYELLOW
    Quantity_NOC_HONEYDEW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW
    Quantity_NOC_HONEYDEW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW2
    Quantity_NOC_HONEYDEW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW3
    Quantity_NOC_HONEYDEW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW4
    Quantity_NOC_HOTPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK
    Quantity_NOC_HOTPINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK1
    Quantity_NOC_HOTPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK2
    Quantity_NOC_HOTPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK3
    Quantity_NOC_HOTPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK4
    Quantity_NOC_INDIANRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED
    Quantity_NOC_INDIANRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED1
    Quantity_NOC_INDIANRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED2
    Quantity_NOC_INDIANRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED3
    Quantity_NOC_INDIANRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED4
    Quantity_NOC_IVORY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY
    Quantity_NOC_IVORY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY2
    Quantity_NOC_IVORY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY3
    Quantity_NOC_IVORY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY4
    Quantity_NOC_KHAKI: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI
    Quantity_NOC_KHAKI1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI1
    Quantity_NOC_KHAKI2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI2
    Quantity_NOC_KHAKI3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI3
    Quantity_NOC_KHAKI4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI4
    Quantity_NOC_LAVENDER: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDER
    Quantity_NOC_LAVENDERBLUSH1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1
    Quantity_NOC_LAVENDERBLUSH2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2
    Quantity_NOC_LAVENDERBLUSH3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3
    Quantity_NOC_LAVENDERBLUSH4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4
    Quantity_NOC_LAWNGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAWNGREEN
    Quantity_NOC_LEMONCHIFFON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1
    Quantity_NOC_LEMONCHIFFON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2
    Quantity_NOC_LEMONCHIFFON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3
    Quantity_NOC_LEMONCHIFFON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4
    Quantity_NOC_LIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE
    Quantity_NOC_LIGHTBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1
    Quantity_NOC_LIGHTBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2
    Quantity_NOC_LIGHTBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3
    Quantity_NOC_LIGHTBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4
    Quantity_NOC_LIGHTCORAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL
    Quantity_NOC_LIGHTCYAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN1
    Quantity_NOC_LIGHTCYAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2
    Quantity_NOC_LIGHTCYAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3
    Quantity_NOC_LIGHTCYAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4
    Quantity_NOC_LIGHTGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD
    Quantity_NOC_LIGHTGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1
    Quantity_NOC_LIGHTGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2
    Quantity_NOC_LIGHTGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3
    Quantity_NOC_LIGHTGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4
    Quantity_NOC_LIGHTGOLDENRODYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW
    Quantity_NOC_LIGHTGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY
    Quantity_NOC_LIGHTPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK
    Quantity_NOC_LIGHTPINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1
    Quantity_NOC_LIGHTPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2
    Quantity_NOC_LIGHTPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3
    Quantity_NOC_LIGHTPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4
    Quantity_NOC_LIGHTSALMON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1
    Quantity_NOC_LIGHTSALMON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2
    Quantity_NOC_LIGHTSALMON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3
    Quantity_NOC_LIGHTSALMON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4
    Quantity_NOC_LIGHTSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN
    Quantity_NOC_LIGHTSKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE
    Quantity_NOC_LIGHTSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1
    Quantity_NOC_LIGHTSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2
    Quantity_NOC_LIGHTSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3
    Quantity_NOC_LIGHTSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4
    Quantity_NOC_LIGHTSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE
    Quantity_NOC_LIGHTSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY
    Quantity_NOC_LIGHTSTEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE
    Quantity_NOC_LIGHTSTEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1
    Quantity_NOC_LIGHTSTEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2
    Quantity_NOC_LIGHTSTEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3
    Quantity_NOC_LIGHTSTEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4
    Quantity_NOC_LIGHTYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW
    Quantity_NOC_LIGHTYELLOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2
    Quantity_NOC_LIGHTYELLOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3
    Quantity_NOC_LIGHTYELLOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4
    Quantity_NOC_LIMEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIMEGREEN
    Quantity_NOC_LINEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LINEN
    Quantity_NOC_MAGENTA1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA1
    Quantity_NOC_MAGENTA2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA2
    Quantity_NOC_MAGENTA3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA3
    Quantity_NOC_MAGENTA4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA4
    Quantity_NOC_MAROON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON
    Quantity_NOC_MAROON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON1
    Quantity_NOC_MAROON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON2
    Quantity_NOC_MAROON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON3
    Quantity_NOC_MAROON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON4
    Quantity_NOC_MATRABLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MATRABLUE
    Quantity_NOC_MATRAGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MATRAGRAY
    Quantity_NOC_MEDIUMAQUAMARINE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE
    Quantity_NOC_MEDIUMORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID
    Quantity_NOC_MEDIUMORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1
    Quantity_NOC_MEDIUMORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2
    Quantity_NOC_MEDIUMORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3
    Quantity_NOC_MEDIUMORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4
    Quantity_NOC_MEDIUMPURPLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE
    Quantity_NOC_MEDIUMPURPLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1
    Quantity_NOC_MEDIUMPURPLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2
    Quantity_NOC_MEDIUMPURPLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3
    Quantity_NOC_MEDIUMPURPLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4
    Quantity_NOC_MEDIUMSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN
    Quantity_NOC_MEDIUMSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE
    Quantity_NOC_MEDIUMSPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN
    Quantity_NOC_MEDIUMTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE
    Quantity_NOC_MEDIUMVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED
    Quantity_NOC_MIDNIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE
    Quantity_NOC_MINTCREAM: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MINTCREAM
    Quantity_NOC_MISTYROSE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE
    Quantity_NOC_MISTYROSE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE2
    Quantity_NOC_MISTYROSE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE3
    Quantity_NOC_MISTYROSE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE4
    Quantity_NOC_MOCCASIN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MOCCASIN
    Quantity_NOC_NAVAJOWHITE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1
    Quantity_NOC_NAVAJOWHITE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2
    Quantity_NOC_NAVAJOWHITE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3
    Quantity_NOC_NAVAJOWHITE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4
    Quantity_NOC_NAVYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVYBLUE
    Quantity_NOC_OLDLACE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLDLACE
    Quantity_NOC_OLIVEDRAB: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB
    Quantity_NOC_OLIVEDRAB1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1
    Quantity_NOC_OLIVEDRAB2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2
    Quantity_NOC_OLIVEDRAB3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3
    Quantity_NOC_OLIVEDRAB4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4
    Quantity_NOC_ORANGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE
    Quantity_NOC_ORANGE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE1
    Quantity_NOC_ORANGE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE2
    Quantity_NOC_ORANGE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE3
    Quantity_NOC_ORANGE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE4
    Quantity_NOC_ORANGERED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED
    Quantity_NOC_ORANGERED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED1
    Quantity_NOC_ORANGERED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED2
    Quantity_NOC_ORANGERED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED3
    Quantity_NOC_ORANGERED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED4
    Quantity_NOC_ORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID
    Quantity_NOC_ORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID1
    Quantity_NOC_ORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID2
    Quantity_NOC_ORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID3
    Quantity_NOC_ORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID4
    Quantity_NOC_PALEGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD
    Quantity_NOC_PALEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN
    Quantity_NOC_PALEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN1
    Quantity_NOC_PALEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN2
    Quantity_NOC_PALEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN3
    Quantity_NOC_PALEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN4
    Quantity_NOC_PALETURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE
    Quantity_NOC_PALETURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1
    Quantity_NOC_PALETURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2
    Quantity_NOC_PALETURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3
    Quantity_NOC_PALETURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4
    Quantity_NOC_PALEVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED
    Quantity_NOC_PALEVIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1
    Quantity_NOC_PALEVIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2
    Quantity_NOC_PALEVIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3
    Quantity_NOC_PALEVIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4
    Quantity_NOC_PAPAYAWHIP: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP
    Quantity_NOC_PEACHPUFF: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF
    Quantity_NOC_PEACHPUFF2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2
    Quantity_NOC_PEACHPUFF3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3
    Quantity_NOC_PEACHPUFF4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4
    Quantity_NOC_PERU: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PERU
    Quantity_NOC_PINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK
    Quantity_NOC_PINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK1
    Quantity_NOC_PINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK2
    Quantity_NOC_PINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK3
    Quantity_NOC_PINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK4
    Quantity_NOC_PLUM: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM
    Quantity_NOC_PLUM1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM1
    Quantity_NOC_PLUM2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM2
    Quantity_NOC_PLUM3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM3
    Quantity_NOC_PLUM4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM4
    Quantity_NOC_POWDERBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_POWDERBLUE
    Quantity_NOC_PURPLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE
    Quantity_NOC_PURPLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE1
    Quantity_NOC_PURPLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE2
    Quantity_NOC_PURPLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE3
    Quantity_NOC_PURPLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE4
    Quantity_NOC_RED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED
    Quantity_NOC_RED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED1
    Quantity_NOC_RED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED2
    Quantity_NOC_RED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED3
    Quantity_NOC_RED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED4
    Quantity_NOC_ROSYBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN
    Quantity_NOC_ROSYBROWN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1
    Quantity_NOC_ROSYBROWN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2
    Quantity_NOC_ROSYBROWN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3
    Quantity_NOC_ROSYBROWN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4
    Quantity_NOC_ROYALBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE
    Quantity_NOC_ROYALBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1
    Quantity_NOC_ROYALBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2
    Quantity_NOC_ROYALBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3
    Quantity_NOC_ROYALBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4
    Quantity_NOC_SADDLEBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN
    Quantity_NOC_SALMON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON
    Quantity_NOC_SALMON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON1
    Quantity_NOC_SALMON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON2
    Quantity_NOC_SALMON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON3
    Quantity_NOC_SALMON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON4
    Quantity_NOC_SANDYBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SANDYBROWN
    Quantity_NOC_SEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN
    Quantity_NOC_SEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN1
    Quantity_NOC_SEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN2
    Quantity_NOC_SEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN3
    Quantity_NOC_SEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN4
    Quantity_NOC_SEASHELL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL
    Quantity_NOC_SEASHELL2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL2
    Quantity_NOC_SEASHELL3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL3
    Quantity_NOC_SEASHELL4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL4
    Quantity_NOC_SIENNA: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA
    Quantity_NOC_SIENNA1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA1
    Quantity_NOC_SIENNA2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA2
    Quantity_NOC_SIENNA3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA3
    Quantity_NOC_SIENNA4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA4
    Quantity_NOC_SKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE
    Quantity_NOC_SKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE1
    Quantity_NOC_SKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE2
    Quantity_NOC_SKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE3
    Quantity_NOC_SKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE4
    Quantity_NOC_SLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE
    Quantity_NOC_SLATEBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1
    Quantity_NOC_SLATEBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2
    Quantity_NOC_SLATEBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3
    Quantity_NOC_SLATEBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4
    Quantity_NOC_SLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY
    Quantity_NOC_SLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1
    Quantity_NOC_SLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2
    Quantity_NOC_SLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3
    Quantity_NOC_SLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4
    Quantity_NOC_SNOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW
    Quantity_NOC_SNOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW2
    Quantity_NOC_SNOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW3
    Quantity_NOC_SNOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW4
    Quantity_NOC_SPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN
    Quantity_NOC_SPRINGGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2
    Quantity_NOC_SPRINGGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3
    Quantity_NOC_SPRINGGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4
    Quantity_NOC_STEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE
    Quantity_NOC_STEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE1
    Quantity_NOC_STEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE2
    Quantity_NOC_STEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE3
    Quantity_NOC_STEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE4
    Quantity_NOC_TAN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN
    Quantity_NOC_TAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN1
    Quantity_NOC_TAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN2
    Quantity_NOC_TAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN3
    Quantity_NOC_TAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN4
    Quantity_NOC_TEAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TEAL
    Quantity_NOC_THISTLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE
    Quantity_NOC_THISTLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE1
    Quantity_NOC_THISTLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE2
    Quantity_NOC_THISTLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE3
    Quantity_NOC_THISTLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE4
    Quantity_NOC_TOMATO: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO
    Quantity_NOC_TOMATO1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO1
    Quantity_NOC_TOMATO2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO2
    Quantity_NOC_TOMATO3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO3
    Quantity_NOC_TOMATO4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO4
    Quantity_NOC_TURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE
    Quantity_NOC_TURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE1
    Quantity_NOC_TURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE2
    Quantity_NOC_TURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE3
    Quantity_NOC_TURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE4
    Quantity_NOC_VIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLET
    Quantity_NOC_VIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED
    Quantity_NOC_VIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED1
    Quantity_NOC_VIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED2
    Quantity_NOC_VIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED3
    Quantity_NOC_VIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED4
    Quantity_NOC_WHEAT: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT
    Quantity_NOC_WHEAT1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT1
    Quantity_NOC_WHEAT2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT2
    Quantity_NOC_WHEAT3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT3
    Quantity_NOC_WHEAT4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT4
    Quantity_NOC_WHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHITE
    Quantity_NOC_WHITESMOKE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHITESMOKE
    Quantity_NOC_YELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW
    Quantity_NOC_YELLOW1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW1
    Quantity_NOC_YELLOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW2
    Quantity_NOC_YELLOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW3
    Quantity_NOC_YELLOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW4
    Quantity_NOC_YELLOWGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN
    __entries: dict # value = {'Quantity_NOC_BLACK': (Quantity_NameOfColor.Quantity_NOC_BLACK, None), 'Quantity_NOC_MATRABLUE': (Quantity_NameOfColor.Quantity_NOC_MATRABLUE, None), 'Quantity_NOC_MATRAGRAY': (Quantity_NameOfColor.Quantity_NOC_MATRAGRAY, None), 'Quantity_NOC_ALICEBLUE': (Quantity_NameOfColor.Quantity_NOC_ALICEBLUE, None), 'Quantity_NOC_ANTIQUEWHITE': (Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE, None), 'Quantity_NOC_ANTIQUEWHITE1': (Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1, None), 'Quantity_NOC_ANTIQUEWHITE2': (Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2, None), 'Quantity_NOC_ANTIQUEWHITE3': (Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3, None), 'Quantity_NOC_ANTIQUEWHITE4': (Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4, None), 'Quantity_NOC_AQUAMARINE1': (Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1, None), 'Quantity_NOC_AQUAMARINE2': (Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2, None), 'Quantity_NOC_AQUAMARINE4': (Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4, None), 'Quantity_NOC_AZURE': (Quantity_NameOfColor.Quantity_NOC_AZURE, None), 'Quantity_NOC_AZURE2': (Quantity_NameOfColor.Quantity_NOC_AZURE2, None), 'Quantity_NOC_AZURE3': (Quantity_NameOfColor.Quantity_NOC_AZURE3, None), 'Quantity_NOC_AZURE4': (Quantity_NameOfColor.Quantity_NOC_AZURE4, None), 'Quantity_NOC_BEIGE': (Quantity_NameOfColor.Quantity_NOC_BEIGE, None), 'Quantity_NOC_BISQUE': (Quantity_NameOfColor.Quantity_NOC_BISQUE, None), 'Quantity_NOC_BISQUE2': (Quantity_NameOfColor.Quantity_NOC_BISQUE2, None), 'Quantity_NOC_BISQUE3': (Quantity_NameOfColor.Quantity_NOC_BISQUE3, None), 'Quantity_NOC_BISQUE4': (Quantity_NameOfColor.Quantity_NOC_BISQUE4, None), 'Quantity_NOC_BLANCHEDALMOND': (Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND, None), 'Quantity_NOC_BLUE1': (Quantity_NameOfColor.Quantity_NOC_BLUE1, None), 'Quantity_NOC_BLUE2': (Quantity_NameOfColor.Quantity_NOC_BLUE2, None), 'Quantity_NOC_BLUE3': (Quantity_NameOfColor.Quantity_NOC_BLUE3, None), 'Quantity_NOC_BLUE4': (Quantity_NameOfColor.Quantity_NOC_BLUE4, None), 'Quantity_NOC_BLUEVIOLET': (Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET, None), 'Quantity_NOC_BROWN': (Quantity_NameOfColor.Quantity_NOC_BROWN, None), 'Quantity_NOC_BROWN1': (Quantity_NameOfColor.Quantity_NOC_BROWN1, None), 'Quantity_NOC_BROWN2': (Quantity_NameOfColor.Quantity_NOC_BROWN2, None), 'Quantity_NOC_BROWN3': (Quantity_NameOfColor.Quantity_NOC_BROWN3, None), 'Quantity_NOC_BROWN4': (Quantity_NameOfColor.Quantity_NOC_BROWN4, None), 'Quantity_NOC_BURLYWOOD': (Quantity_NameOfColor.Quantity_NOC_BURLYWOOD, None), 'Quantity_NOC_BURLYWOOD1': (Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1, None), 'Quantity_NOC_BURLYWOOD2': (Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2, None), 'Quantity_NOC_BURLYWOOD3': (Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3, None), 'Quantity_NOC_BURLYWOOD4': (Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4, None), 'Quantity_NOC_CADETBLUE': (Quantity_NameOfColor.Quantity_NOC_CADETBLUE, None), 'Quantity_NOC_CADETBLUE1': (Quantity_NameOfColor.Quantity_NOC_CADETBLUE1, None), 'Quantity_NOC_CADETBLUE2': (Quantity_NameOfColor.Quantity_NOC_CADETBLUE2, None), 'Quantity_NOC_CADETBLUE3': (Quantity_NameOfColor.Quantity_NOC_CADETBLUE3, None), 'Quantity_NOC_CADETBLUE4': (Quantity_NameOfColor.Quantity_NOC_CADETBLUE4, None), 'Quantity_NOC_CHARTREUSE': (Quantity_NameOfColor.Quantity_NOC_CHARTREUSE, None), 'Quantity_NOC_CHARTREUSE1': (Quantity_NameOfColor.Quantity_NOC_CHARTREUSE1, None), 'Quantity_NOC_CHARTREUSE2': (Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2, None), 'Quantity_NOC_CHARTREUSE3': (Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3, None), 'Quantity_NOC_CHARTREUSE4': (Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4, None), 'Quantity_NOC_CHOCOLATE': (Quantity_NameOfColor.Quantity_NOC_CHOCOLATE, None), 'Quantity_NOC_CHOCOLATE1': (Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1, None), 'Quantity_NOC_CHOCOLATE2': (Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2, None), 'Quantity_NOC_CHOCOLATE3': (Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3, None), 'Quantity_NOC_CHOCOLATE4': (Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4, None), 'Quantity_NOC_CORAL': (Quantity_NameOfColor.Quantity_NOC_CORAL, None), 'Quantity_NOC_CORAL1': (Quantity_NameOfColor.Quantity_NOC_CORAL1, None), 'Quantity_NOC_CORAL2': (Quantity_NameOfColor.Quantity_NOC_CORAL2, None), 'Quantity_NOC_CORAL3': (Quantity_NameOfColor.Quantity_NOC_CORAL3, None), 'Quantity_NOC_CORAL4': (Quantity_NameOfColor.Quantity_NOC_CORAL4, None), 'Quantity_NOC_CORNFLOWERBLUE': (Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE, None), 'Quantity_NOC_CORNSILK1': (Quantity_NameOfColor.Quantity_NOC_CORNSILK1, None), 'Quantity_NOC_CORNSILK2': (Quantity_NameOfColor.Quantity_NOC_CORNSILK2, None), 'Quantity_NOC_CORNSILK3': (Quantity_NameOfColor.Quantity_NOC_CORNSILK3, None), 'Quantity_NOC_CORNSILK4': (Quantity_NameOfColor.Quantity_NOC_CORNSILK4, None), 'Quantity_NOC_CYAN1': (Quantity_NameOfColor.Quantity_NOC_CYAN1, None), 'Quantity_NOC_CYAN2': (Quantity_NameOfColor.Quantity_NOC_CYAN2, None), 'Quantity_NOC_CYAN3': (Quantity_NameOfColor.Quantity_NOC_CYAN3, None), 'Quantity_NOC_CYAN4': (Quantity_NameOfColor.Quantity_NOC_CYAN4, None), 'Quantity_NOC_DARKGOLDENROD': (Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD, None), 'Quantity_NOC_DARKGOLDENROD1': (Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1, None), 'Quantity_NOC_DARKGOLDENROD2': (Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2, None), 'Quantity_NOC_DARKGOLDENROD3': (Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3, None), 'Quantity_NOC_DARKGOLDENROD4': (Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4, None), 'Quantity_NOC_DARKGREEN': (Quantity_NameOfColor.Quantity_NOC_DARKGREEN, None), 'Quantity_NOC_DARKKHAKI': (Quantity_NameOfColor.Quantity_NOC_DARKKHAKI, None), 'Quantity_NOC_DARKOLIVEGREEN': (Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN, None), 'Quantity_NOC_DARKOLIVEGREEN1': (Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1, None), 'Quantity_NOC_DARKOLIVEGREEN2': (Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2, None), 'Quantity_NOC_DARKOLIVEGREEN3': (Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3, None), 'Quantity_NOC_DARKOLIVEGREEN4': (Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4, None), 'Quantity_NOC_DARKORANGE': (Quantity_NameOfColor.Quantity_NOC_DARKORANGE, None), 'Quantity_NOC_DARKORANGE1': (Quantity_NameOfColor.Quantity_NOC_DARKORANGE1, None), 'Quantity_NOC_DARKORANGE2': (Quantity_NameOfColor.Quantity_NOC_DARKORANGE2, None), 'Quantity_NOC_DARKORANGE3': (Quantity_NameOfColor.Quantity_NOC_DARKORANGE3, None), 'Quantity_NOC_DARKORANGE4': (Quantity_NameOfColor.Quantity_NOC_DARKORANGE4, None), 'Quantity_NOC_DARKORCHID': (Quantity_NameOfColor.Quantity_NOC_DARKORCHID, None), 'Quantity_NOC_DARKORCHID1': (Quantity_NameOfColor.Quantity_NOC_DARKORCHID1, None), 'Quantity_NOC_DARKORCHID2': (Quantity_NameOfColor.Quantity_NOC_DARKORCHID2, None), 'Quantity_NOC_DARKORCHID3': (Quantity_NameOfColor.Quantity_NOC_DARKORCHID3, None), 'Quantity_NOC_DARKORCHID4': (Quantity_NameOfColor.Quantity_NOC_DARKORCHID4, None), 'Quantity_NOC_DARKSALMON': (Quantity_NameOfColor.Quantity_NOC_DARKSALMON, None), 'Quantity_NOC_DARKSEAGREEN': (Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN, None), 'Quantity_NOC_DARKSEAGREEN1': (Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1, None), 'Quantity_NOC_DARKSEAGREEN2': (Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2, None), 'Quantity_NOC_DARKSEAGREEN3': (Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3, None), 'Quantity_NOC_DARKSEAGREEN4': (Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4, None), 'Quantity_NOC_DARKSLATEBLUE': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE, None), 'Quantity_NOC_DARKSLATEGRAY1': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1, None), 'Quantity_NOC_DARKSLATEGRAY2': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2, None), 'Quantity_NOC_DARKSLATEGRAY3': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3, None), 'Quantity_NOC_DARKSLATEGRAY4': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4, None), 'Quantity_NOC_DARKSLATEGRAY': (Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY, None), 'Quantity_NOC_DARKTURQUOISE': (Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE, None), 'Quantity_NOC_DARKVIOLET': (Quantity_NameOfColor.Quantity_NOC_DARKVIOLET, None), 'Quantity_NOC_DEEPPINK': (Quantity_NameOfColor.Quantity_NOC_DEEPPINK, None), 'Quantity_NOC_DEEPPINK2': (Quantity_NameOfColor.Quantity_NOC_DEEPPINK2, None), 'Quantity_NOC_DEEPPINK3': (Quantity_NameOfColor.Quantity_NOC_DEEPPINK3, None), 'Quantity_NOC_DEEPPINK4': (Quantity_NameOfColor.Quantity_NOC_DEEPPINK4, None), 'Quantity_NOC_DEEPSKYBLUE1': (Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1, None), 'Quantity_NOC_DEEPSKYBLUE2': (Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2, None), 'Quantity_NOC_DEEPSKYBLUE3': (Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3, None), 'Quantity_NOC_DEEPSKYBLUE4': (Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4, None), 'Quantity_NOC_DODGERBLUE1': (Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1, None), 'Quantity_NOC_DODGERBLUE2': (Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2, None), 'Quantity_NOC_DODGERBLUE3': (Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3, None), 'Quantity_NOC_DODGERBLUE4': (Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4, None), 'Quantity_NOC_FIREBRICK': (Quantity_NameOfColor.Quantity_NOC_FIREBRICK, None), 'Quantity_NOC_FIREBRICK1': (Quantity_NameOfColor.Quantity_NOC_FIREBRICK1, None), 'Quantity_NOC_FIREBRICK2': (Quantity_NameOfColor.Quantity_NOC_FIREBRICK2, None), 'Quantity_NOC_FIREBRICK3': (Quantity_NameOfColor.Quantity_NOC_FIREBRICK3, None), 'Quantity_NOC_FIREBRICK4': (Quantity_NameOfColor.Quantity_NOC_FIREBRICK4, None), 'Quantity_NOC_FLORALWHITE': (Quantity_NameOfColor.Quantity_NOC_FLORALWHITE, None), 'Quantity_NOC_FORESTGREEN': (Quantity_NameOfColor.Quantity_NOC_FORESTGREEN, None), 'Quantity_NOC_GAINSBORO': (Quantity_NameOfColor.Quantity_NOC_GAINSBORO, None), 'Quantity_NOC_GHOSTWHITE': (Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE, None), 'Quantity_NOC_GOLD': (Quantity_NameOfColor.Quantity_NOC_GOLD, None), 'Quantity_NOC_GOLD1': (Quantity_NameOfColor.Quantity_NOC_GOLD1, None), 'Quantity_NOC_GOLD2': (Quantity_NameOfColor.Quantity_NOC_GOLD2, None), 'Quantity_NOC_GOLD3': (Quantity_NameOfColor.Quantity_NOC_GOLD3, None), 'Quantity_NOC_GOLD4': (Quantity_NameOfColor.Quantity_NOC_GOLD4, None), 'Quantity_NOC_GOLDENROD': (Quantity_NameOfColor.Quantity_NOC_GOLDENROD, None), 'Quantity_NOC_GOLDENROD1': (Quantity_NameOfColor.Quantity_NOC_GOLDENROD1, None), 'Quantity_NOC_GOLDENROD2': (Quantity_NameOfColor.Quantity_NOC_GOLDENROD2, None), 'Quantity_NOC_GOLDENROD3': (Quantity_NameOfColor.Quantity_NOC_GOLDENROD3, None), 'Quantity_NOC_GOLDENROD4': (Quantity_NameOfColor.Quantity_NOC_GOLDENROD4, None), 'Quantity_NOC_GRAY': (Quantity_NameOfColor.Quantity_NOC_GRAY, None), 'Quantity_NOC_GRAY0': (Quantity_NameOfColor.Quantity_NOC_GRAY0, None), 'Quantity_NOC_GRAY1': (Quantity_NameOfColor.Quantity_NOC_GRAY1, None), 'Quantity_NOC_GRAY10': (Quantity_NameOfColor.Quantity_NOC_GRAY10, None), 'Quantity_NOC_GRAY11': (Quantity_NameOfColor.Quantity_NOC_GRAY11, None), 'Quantity_NOC_GRAY12': (Quantity_NameOfColor.Quantity_NOC_GRAY12, None), 'Quantity_NOC_GRAY13': (Quantity_NameOfColor.Quantity_NOC_GRAY13, None), 'Quantity_NOC_GRAY14': (Quantity_NameOfColor.Quantity_NOC_GRAY14, None), 'Quantity_NOC_GRAY15': (Quantity_NameOfColor.Quantity_NOC_GRAY15, None), 'Quantity_NOC_GRAY16': (Quantity_NameOfColor.Quantity_NOC_GRAY16, None), 'Quantity_NOC_GRAY17': (Quantity_NameOfColor.Quantity_NOC_GRAY17, None), 'Quantity_NOC_GRAY18': (Quantity_NameOfColor.Quantity_NOC_GRAY18, None), 'Quantity_NOC_GRAY19': (Quantity_NameOfColor.Quantity_NOC_GRAY19, None), 'Quantity_NOC_GRAY2': (Quantity_NameOfColor.Quantity_NOC_GRAY2, None), 'Quantity_NOC_GRAY20': (Quantity_NameOfColor.Quantity_NOC_GRAY20, None), 'Quantity_NOC_GRAY21': (Quantity_NameOfColor.Quantity_NOC_GRAY21, None), 'Quantity_NOC_GRAY22': (Quantity_NameOfColor.Quantity_NOC_GRAY22, None), 'Quantity_NOC_GRAY23': (Quantity_NameOfColor.Quantity_NOC_GRAY23, None), 'Quantity_NOC_GRAY24': (Quantity_NameOfColor.Quantity_NOC_GRAY24, None), 'Quantity_NOC_GRAY25': (Quantity_NameOfColor.Quantity_NOC_GRAY25, None), 'Quantity_NOC_GRAY26': (Quantity_NameOfColor.Quantity_NOC_GRAY26, None), 'Quantity_NOC_GRAY27': (Quantity_NameOfColor.Quantity_NOC_GRAY27, None), 'Quantity_NOC_GRAY28': (Quantity_NameOfColor.Quantity_NOC_GRAY28, None), 'Quantity_NOC_GRAY29': (Quantity_NameOfColor.Quantity_NOC_GRAY29, None), 'Quantity_NOC_GRAY3': (Quantity_NameOfColor.Quantity_NOC_GRAY3, None), 'Quantity_NOC_GRAY30': (Quantity_NameOfColor.Quantity_NOC_GRAY30, None), 'Quantity_NOC_GRAY31': (Quantity_NameOfColor.Quantity_NOC_GRAY31, None), 'Quantity_NOC_GRAY32': (Quantity_NameOfColor.Quantity_NOC_GRAY32, None), 'Quantity_NOC_GRAY33': (Quantity_NameOfColor.Quantity_NOC_GRAY33, None), 'Quantity_NOC_GRAY34': (Quantity_NameOfColor.Quantity_NOC_GRAY34, None), 'Quantity_NOC_GRAY35': (Quantity_NameOfColor.Quantity_NOC_GRAY35, None), 'Quantity_NOC_GRAY36': (Quantity_NameOfColor.Quantity_NOC_GRAY36, None), 'Quantity_NOC_GRAY37': (Quantity_NameOfColor.Quantity_NOC_GRAY37, None), 'Quantity_NOC_GRAY38': (Quantity_NameOfColor.Quantity_NOC_GRAY38, None), 'Quantity_NOC_GRAY39': (Quantity_NameOfColor.Quantity_NOC_GRAY39, None), 'Quantity_NOC_GRAY4': (Quantity_NameOfColor.Quantity_NOC_GRAY4, None), 'Quantity_NOC_GRAY40': (Quantity_NameOfColor.Quantity_NOC_GRAY40, None), 'Quantity_NOC_GRAY41': (Quantity_NameOfColor.Quantity_NOC_GRAY41, None), 'Quantity_NOC_GRAY42': (Quantity_NameOfColor.Quantity_NOC_GRAY42, None), 'Quantity_NOC_GRAY43': (Quantity_NameOfColor.Quantity_NOC_GRAY43, None), 'Quantity_NOC_GRAY44': (Quantity_NameOfColor.Quantity_NOC_GRAY44, None), 'Quantity_NOC_GRAY45': (Quantity_NameOfColor.Quantity_NOC_GRAY45, None), 'Quantity_NOC_GRAY46': (Quantity_NameOfColor.Quantity_NOC_GRAY46, None), 'Quantity_NOC_GRAY47': (Quantity_NameOfColor.Quantity_NOC_GRAY47, None), 'Quantity_NOC_GRAY48': (Quantity_NameOfColor.Quantity_NOC_GRAY48, None), 'Quantity_NOC_GRAY49': (Quantity_NameOfColor.Quantity_NOC_GRAY49, None), 'Quantity_NOC_GRAY5': (Quantity_NameOfColor.Quantity_NOC_GRAY5, None), 'Quantity_NOC_GRAY50': (Quantity_NameOfColor.Quantity_NOC_GRAY50, None), 'Quantity_NOC_GRAY51': (Quantity_NameOfColor.Quantity_NOC_GRAY51, None), 'Quantity_NOC_GRAY52': (Quantity_NameOfColor.Quantity_NOC_GRAY52, None), 'Quantity_NOC_GRAY53': (Quantity_NameOfColor.Quantity_NOC_GRAY53, None), 'Quantity_NOC_GRAY54': (Quantity_NameOfColor.Quantity_NOC_GRAY54, None), 'Quantity_NOC_GRAY55': (Quantity_NameOfColor.Quantity_NOC_GRAY55, None), 'Quantity_NOC_GRAY56': (Quantity_NameOfColor.Quantity_NOC_GRAY56, None), 'Quantity_NOC_GRAY57': (Quantity_NameOfColor.Quantity_NOC_GRAY57, None), 'Quantity_NOC_GRAY58': (Quantity_NameOfColor.Quantity_NOC_GRAY58, None), 'Quantity_NOC_GRAY59': (Quantity_NameOfColor.Quantity_NOC_GRAY59, None), 'Quantity_NOC_GRAY6': (Quantity_NameOfColor.Quantity_NOC_GRAY6, None), 'Quantity_NOC_GRAY60': (Quantity_NameOfColor.Quantity_NOC_GRAY60, None), 'Quantity_NOC_GRAY61': (Quantity_NameOfColor.Quantity_NOC_GRAY61, None), 'Quantity_NOC_GRAY62': (Quantity_NameOfColor.Quantity_NOC_GRAY62, None), 'Quantity_NOC_GRAY63': (Quantity_NameOfColor.Quantity_NOC_GRAY63, None), 'Quantity_NOC_GRAY64': (Quantity_NameOfColor.Quantity_NOC_GRAY64, None), 'Quantity_NOC_GRAY65': (Quantity_NameOfColor.Quantity_NOC_GRAY65, None), 'Quantity_NOC_GRAY66': (Quantity_NameOfColor.Quantity_NOC_GRAY66, None), 'Quantity_NOC_GRAY67': (Quantity_NameOfColor.Quantity_NOC_GRAY67, None), 'Quantity_NOC_GRAY68': (Quantity_NameOfColor.Quantity_NOC_GRAY68, None), 'Quantity_NOC_GRAY69': (Quantity_NameOfColor.Quantity_NOC_GRAY69, None), 'Quantity_NOC_GRAY7': (Quantity_NameOfColor.Quantity_NOC_GRAY7, None), 'Quantity_NOC_GRAY70': (Quantity_NameOfColor.Quantity_NOC_GRAY70, None), 'Quantity_NOC_GRAY71': (Quantity_NameOfColor.Quantity_NOC_GRAY71, None), 'Quantity_NOC_GRAY72': (Quantity_NameOfColor.Quantity_NOC_GRAY72, None), 'Quantity_NOC_GRAY73': (Quantity_NameOfColor.Quantity_NOC_GRAY73, None), 'Quantity_NOC_GRAY74': (Quantity_NameOfColor.Quantity_NOC_GRAY74, None), 'Quantity_NOC_GRAY75': (Quantity_NameOfColor.Quantity_NOC_GRAY75, None), 'Quantity_NOC_GRAY76': (Quantity_NameOfColor.Quantity_NOC_GRAY76, None), 'Quantity_NOC_GRAY77': (Quantity_NameOfColor.Quantity_NOC_GRAY77, None), 'Quantity_NOC_GRAY78': (Quantity_NameOfColor.Quantity_NOC_GRAY78, None), 'Quantity_NOC_GRAY79': (Quantity_NameOfColor.Quantity_NOC_GRAY79, None), 'Quantity_NOC_GRAY8': (Quantity_NameOfColor.Quantity_NOC_GRAY8, None), 'Quantity_NOC_GRAY80': (Quantity_NameOfColor.Quantity_NOC_GRAY80, None), 'Quantity_NOC_GRAY81': (Quantity_NameOfColor.Quantity_NOC_GRAY81, None), 'Quantity_NOC_GRAY82': (Quantity_NameOfColor.Quantity_NOC_GRAY82, None), 'Quantity_NOC_GRAY83': (Quantity_NameOfColor.Quantity_NOC_GRAY83, None), 'Quantity_NOC_GRAY85': (Quantity_NameOfColor.Quantity_NOC_GRAY85, None), 'Quantity_NOC_GRAY86': (Quantity_NameOfColor.Quantity_NOC_GRAY86, None), 'Quantity_NOC_GRAY87': (Quantity_NameOfColor.Quantity_NOC_GRAY87, None), 'Quantity_NOC_GRAY88': (Quantity_NameOfColor.Quantity_NOC_GRAY88, None), 'Quantity_NOC_GRAY89': (Quantity_NameOfColor.Quantity_NOC_GRAY89, None), 'Quantity_NOC_GRAY9': (Quantity_NameOfColor.Quantity_NOC_GRAY9, None), 'Quantity_NOC_GRAY90': (Quantity_NameOfColor.Quantity_NOC_GRAY90, None), 'Quantity_NOC_GRAY91': (Quantity_NameOfColor.Quantity_NOC_GRAY91, None), 'Quantity_NOC_GRAY92': (Quantity_NameOfColor.Quantity_NOC_GRAY92, None), 'Quantity_NOC_GRAY93': (Quantity_NameOfColor.Quantity_NOC_GRAY93, None), 'Quantity_NOC_GRAY94': (Quantity_NameOfColor.Quantity_NOC_GRAY94, None), 'Quantity_NOC_GRAY95': (Quantity_NameOfColor.Quantity_NOC_GRAY95, None), 'Quantity_NOC_GREEN': (Quantity_NameOfColor.Quantity_NOC_GREEN, None), 'Quantity_NOC_GREEN1': (Quantity_NameOfColor.Quantity_NOC_GREEN1, None), 'Quantity_NOC_GREEN2': (Quantity_NameOfColor.Quantity_NOC_GREEN2, None), 'Quantity_NOC_GREEN3': (Quantity_NameOfColor.Quantity_NOC_GREEN3, None), 'Quantity_NOC_GREEN4': (Quantity_NameOfColor.Quantity_NOC_GREEN4, None), 'Quantity_NOC_GREENYELLOW': (Quantity_NameOfColor.Quantity_NOC_GREENYELLOW, None), 'Quantity_NOC_GRAY97': (Quantity_NameOfColor.Quantity_NOC_GRAY97, None), 'Quantity_NOC_GRAY98': (Quantity_NameOfColor.Quantity_NOC_GRAY98, None), 'Quantity_NOC_GRAY99': (Quantity_NameOfColor.Quantity_NOC_GRAY99, None), 'Quantity_NOC_HONEYDEW': (Quantity_NameOfColor.Quantity_NOC_HONEYDEW, None), 'Quantity_NOC_HONEYDEW2': (Quantity_NameOfColor.Quantity_NOC_HONEYDEW2, None), 'Quantity_NOC_HONEYDEW3': (Quantity_NameOfColor.Quantity_NOC_HONEYDEW3, None), 'Quantity_NOC_HONEYDEW4': (Quantity_NameOfColor.Quantity_NOC_HONEYDEW4, None), 'Quantity_NOC_HOTPINK': (Quantity_NameOfColor.Quantity_NOC_HOTPINK, None), 'Quantity_NOC_HOTPINK1': (Quantity_NameOfColor.Quantity_NOC_HOTPINK1, None), 'Quantity_NOC_HOTPINK2': (Quantity_NameOfColor.Quantity_NOC_HOTPINK2, None), 'Quantity_NOC_HOTPINK3': (Quantity_NameOfColor.Quantity_NOC_HOTPINK3, None), 'Quantity_NOC_HOTPINK4': (Quantity_NameOfColor.Quantity_NOC_HOTPINK4, None), 'Quantity_NOC_INDIANRED': (Quantity_NameOfColor.Quantity_NOC_INDIANRED, None), 'Quantity_NOC_INDIANRED1': (Quantity_NameOfColor.Quantity_NOC_INDIANRED1, None), 'Quantity_NOC_INDIANRED2': (Quantity_NameOfColor.Quantity_NOC_INDIANRED2, None), 'Quantity_NOC_INDIANRED3': (Quantity_NameOfColor.Quantity_NOC_INDIANRED3, None), 'Quantity_NOC_INDIANRED4': (Quantity_NameOfColor.Quantity_NOC_INDIANRED4, None), 'Quantity_NOC_IVORY': (Quantity_NameOfColor.Quantity_NOC_IVORY, None), 'Quantity_NOC_IVORY2': (Quantity_NameOfColor.Quantity_NOC_IVORY2, None), 'Quantity_NOC_IVORY3': (Quantity_NameOfColor.Quantity_NOC_IVORY3, None), 'Quantity_NOC_IVORY4': (Quantity_NameOfColor.Quantity_NOC_IVORY4, None), 'Quantity_NOC_KHAKI': (Quantity_NameOfColor.Quantity_NOC_KHAKI, None), 'Quantity_NOC_KHAKI1': (Quantity_NameOfColor.Quantity_NOC_KHAKI1, None), 'Quantity_NOC_KHAKI2': (Quantity_NameOfColor.Quantity_NOC_KHAKI2, None), 'Quantity_NOC_KHAKI3': (Quantity_NameOfColor.Quantity_NOC_KHAKI3, None), 'Quantity_NOC_KHAKI4': (Quantity_NameOfColor.Quantity_NOC_KHAKI4, None), 'Quantity_NOC_LAVENDER': (Quantity_NameOfColor.Quantity_NOC_LAVENDER, None), 'Quantity_NOC_LAVENDERBLUSH1': (Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1, None), 'Quantity_NOC_LAVENDERBLUSH2': (Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2, None), 'Quantity_NOC_LAVENDERBLUSH3': (Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3, None), 'Quantity_NOC_LAVENDERBLUSH4': (Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4, None), 'Quantity_NOC_LAWNGREEN': (Quantity_NameOfColor.Quantity_NOC_LAWNGREEN, None), 'Quantity_NOC_LEMONCHIFFON1': (Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1, None), 'Quantity_NOC_LEMONCHIFFON2': (Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2, None), 'Quantity_NOC_LEMONCHIFFON3': (Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3, None), 'Quantity_NOC_LEMONCHIFFON4': (Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4, None), 'Quantity_NOC_LIGHTBLUE': (Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE, None), 'Quantity_NOC_LIGHTBLUE1': (Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1, None), 'Quantity_NOC_LIGHTBLUE2': (Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2, None), 'Quantity_NOC_LIGHTBLUE3': (Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3, None), 'Quantity_NOC_LIGHTBLUE4': (Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4, None), 'Quantity_NOC_LIGHTCORAL': (Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL, None), 'Quantity_NOC_LIGHTCYAN1': (Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN1, None), 'Quantity_NOC_LIGHTCYAN2': (Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2, None), 'Quantity_NOC_LIGHTCYAN3': (Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3, None), 'Quantity_NOC_LIGHTCYAN4': (Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4, None), 'Quantity_NOC_LIGHTGOLDENROD': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD, None), 'Quantity_NOC_LIGHTGOLDENROD1': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1, None), 'Quantity_NOC_LIGHTGOLDENROD2': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2, None), 'Quantity_NOC_LIGHTGOLDENROD3': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3, None), 'Quantity_NOC_LIGHTGOLDENROD4': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4, None), 'Quantity_NOC_LIGHTGOLDENRODYELLOW': (Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW, None), 'Quantity_NOC_LIGHTGRAY': (Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY, None), 'Quantity_NOC_LIGHTPINK': (Quantity_NameOfColor.Quantity_NOC_LIGHTPINK, None), 'Quantity_NOC_LIGHTPINK1': (Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1, None), 'Quantity_NOC_LIGHTPINK2': (Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2, None), 'Quantity_NOC_LIGHTPINK3': (Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3, None), 'Quantity_NOC_LIGHTPINK4': (Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4, None), 'Quantity_NOC_LIGHTSALMON1': (Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1, None), 'Quantity_NOC_LIGHTSALMON2': (Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2, None), 'Quantity_NOC_LIGHTSALMON3': (Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3, None), 'Quantity_NOC_LIGHTSALMON4': (Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4, None), 'Quantity_NOC_LIGHTSEAGREEN': (Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN, None), 'Quantity_NOC_LIGHTSKYBLUE': (Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE, None), 'Quantity_NOC_LIGHTSKYBLUE1': (Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1, None), 'Quantity_NOC_LIGHTSKYBLUE2': (Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2, None), 'Quantity_NOC_LIGHTSKYBLUE3': (Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3, None), 'Quantity_NOC_LIGHTSKYBLUE4': (Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4, None), 'Quantity_NOC_LIGHTSLATEBLUE': (Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE, None), 'Quantity_NOC_LIGHTSLATEGRAY': (Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY, None), 'Quantity_NOC_LIGHTSTEELBLUE': (Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE, None), 'Quantity_NOC_LIGHTSTEELBLUE1': (Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1, None), 'Quantity_NOC_LIGHTSTEELBLUE2': (Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2, None), 'Quantity_NOC_LIGHTSTEELBLUE3': (Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3, None), 'Quantity_NOC_LIGHTSTEELBLUE4': (Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4, None), 'Quantity_NOC_LIGHTYELLOW': (Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW, None), 'Quantity_NOC_LIGHTYELLOW2': (Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2, None), 'Quantity_NOC_LIGHTYELLOW3': (Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3, None), 'Quantity_NOC_LIGHTYELLOW4': (Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4, None), 'Quantity_NOC_LIMEGREEN': (Quantity_NameOfColor.Quantity_NOC_LIMEGREEN, None), 'Quantity_NOC_LINEN': (Quantity_NameOfColor.Quantity_NOC_LINEN, None), 'Quantity_NOC_MAGENTA1': (Quantity_NameOfColor.Quantity_NOC_MAGENTA1, None), 'Quantity_NOC_MAGENTA2': (Quantity_NameOfColor.Quantity_NOC_MAGENTA2, None), 'Quantity_NOC_MAGENTA3': (Quantity_NameOfColor.Quantity_NOC_MAGENTA3, None), 'Quantity_NOC_MAGENTA4': (Quantity_NameOfColor.Quantity_NOC_MAGENTA4, None), 'Quantity_NOC_MAROON': (Quantity_NameOfColor.Quantity_NOC_MAROON, None), 'Quantity_NOC_MAROON1': (Quantity_NameOfColor.Quantity_NOC_MAROON1, None), 'Quantity_NOC_MAROON2': (Quantity_NameOfColor.Quantity_NOC_MAROON2, None), 'Quantity_NOC_MAROON3': (Quantity_NameOfColor.Quantity_NOC_MAROON3, None), 'Quantity_NOC_MAROON4': (Quantity_NameOfColor.Quantity_NOC_MAROON4, None), 'Quantity_NOC_MEDIUMAQUAMARINE': (Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE, None), 'Quantity_NOC_MEDIUMORCHID': (Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID, None), 'Quantity_NOC_MEDIUMORCHID1': (Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1, None), 'Quantity_NOC_MEDIUMORCHID2': (Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2, None), 'Quantity_NOC_MEDIUMORCHID3': (Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3, None), 'Quantity_NOC_MEDIUMORCHID4': (Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4, None), 'Quantity_NOC_MEDIUMPURPLE': (Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE, None), 'Quantity_NOC_MEDIUMPURPLE1': (Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1, None), 'Quantity_NOC_MEDIUMPURPLE2': (Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2, None), 'Quantity_NOC_MEDIUMPURPLE3': (Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3, None), 'Quantity_NOC_MEDIUMPURPLE4': (Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4, None), 'Quantity_NOC_MEDIUMSEAGREEN': (Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN, None), 'Quantity_NOC_MEDIUMSLATEBLUE': (Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE, None), 'Quantity_NOC_MEDIUMSPRINGGREEN': (Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN, None), 'Quantity_NOC_MEDIUMTURQUOISE': (Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE, None), 'Quantity_NOC_MEDIUMVIOLETRED': (Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED, None), 'Quantity_NOC_MIDNIGHTBLUE': (Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE, None), 'Quantity_NOC_MINTCREAM': (Quantity_NameOfColor.Quantity_NOC_MINTCREAM, None), 'Quantity_NOC_MISTYROSE': (Quantity_NameOfColor.Quantity_NOC_MISTYROSE, None), 'Quantity_NOC_MISTYROSE2': (Quantity_NameOfColor.Quantity_NOC_MISTYROSE2, None), 'Quantity_NOC_MISTYROSE3': (Quantity_NameOfColor.Quantity_NOC_MISTYROSE3, None), 'Quantity_NOC_MISTYROSE4': (Quantity_NameOfColor.Quantity_NOC_MISTYROSE4, None), 'Quantity_NOC_MOCCASIN': (Quantity_NameOfColor.Quantity_NOC_MOCCASIN, None), 'Quantity_NOC_NAVAJOWHITE1': (Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1, None), 'Quantity_NOC_NAVAJOWHITE2': (Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2, None), 'Quantity_NOC_NAVAJOWHITE3': (Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3, None), 'Quantity_NOC_NAVAJOWHITE4': (Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4, None), 'Quantity_NOC_NAVYBLUE': (Quantity_NameOfColor.Quantity_NOC_NAVYBLUE, None), 'Quantity_NOC_OLDLACE': (Quantity_NameOfColor.Quantity_NOC_OLDLACE, None), 'Quantity_NOC_OLIVEDRAB': (Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB, None), 'Quantity_NOC_OLIVEDRAB1': (Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1, None), 'Quantity_NOC_OLIVEDRAB2': (Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2, None), 'Quantity_NOC_OLIVEDRAB3': (Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3, None), 'Quantity_NOC_OLIVEDRAB4': (Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4, None), 'Quantity_NOC_ORANGE': (Quantity_NameOfColor.Quantity_NOC_ORANGE, None), 'Quantity_NOC_ORANGE1': (Quantity_NameOfColor.Quantity_NOC_ORANGE1, None), 'Quantity_NOC_ORANGE2': (Quantity_NameOfColor.Quantity_NOC_ORANGE2, None), 'Quantity_NOC_ORANGE3': (Quantity_NameOfColor.Quantity_NOC_ORANGE3, None), 'Quantity_NOC_ORANGE4': (Quantity_NameOfColor.Quantity_NOC_ORANGE4, None), 'Quantity_NOC_ORANGERED': (Quantity_NameOfColor.Quantity_NOC_ORANGERED, None), 'Quantity_NOC_ORANGERED1': (Quantity_NameOfColor.Quantity_NOC_ORANGERED1, None), 'Quantity_NOC_ORANGERED2': (Quantity_NameOfColor.Quantity_NOC_ORANGERED2, None), 'Quantity_NOC_ORANGERED3': (Quantity_NameOfColor.Quantity_NOC_ORANGERED3, None), 'Quantity_NOC_ORANGERED4': (Quantity_NameOfColor.Quantity_NOC_ORANGERED4, None), 'Quantity_NOC_ORCHID': (Quantity_NameOfColor.Quantity_NOC_ORCHID, None), 'Quantity_NOC_ORCHID1': (Quantity_NameOfColor.Quantity_NOC_ORCHID1, None), 'Quantity_NOC_ORCHID2': (Quantity_NameOfColor.Quantity_NOC_ORCHID2, None), 'Quantity_NOC_ORCHID3': (Quantity_NameOfColor.Quantity_NOC_ORCHID3, None), 'Quantity_NOC_ORCHID4': (Quantity_NameOfColor.Quantity_NOC_ORCHID4, None), 'Quantity_NOC_PALEGOLDENROD': (Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD, None), 'Quantity_NOC_PALEGREEN': (Quantity_NameOfColor.Quantity_NOC_PALEGREEN, None), 'Quantity_NOC_PALEGREEN1': (Quantity_NameOfColor.Quantity_NOC_PALEGREEN1, None), 'Quantity_NOC_PALEGREEN2': (Quantity_NameOfColor.Quantity_NOC_PALEGREEN2, None), 'Quantity_NOC_PALEGREEN3': (Quantity_NameOfColor.Quantity_NOC_PALEGREEN3, None), 'Quantity_NOC_PALEGREEN4': (Quantity_NameOfColor.Quantity_NOC_PALEGREEN4, None), 'Quantity_NOC_PALETURQUOISE': (Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE, None), 'Quantity_NOC_PALETURQUOISE1': (Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1, None), 'Quantity_NOC_PALETURQUOISE2': (Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2, None), 'Quantity_NOC_PALETURQUOISE3': (Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3, None), 'Quantity_NOC_PALETURQUOISE4': (Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4, None), 'Quantity_NOC_PALEVIOLETRED': (Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED, None), 'Quantity_NOC_PALEVIOLETRED1': (Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1, None), 'Quantity_NOC_PALEVIOLETRED2': (Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2, None), 'Quantity_NOC_PALEVIOLETRED3': (Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3, None), 'Quantity_NOC_PALEVIOLETRED4': (Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4, None), 'Quantity_NOC_PAPAYAWHIP': (Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP, None), 'Quantity_NOC_PEACHPUFF': (Quantity_NameOfColor.Quantity_NOC_PEACHPUFF, None), 'Quantity_NOC_PEACHPUFF2': (Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2, None), 'Quantity_NOC_PEACHPUFF3': (Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3, None), 'Quantity_NOC_PEACHPUFF4': (Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4, None), 'Quantity_NOC_PERU': (Quantity_NameOfColor.Quantity_NOC_PERU, None), 'Quantity_NOC_PINK': (Quantity_NameOfColor.Quantity_NOC_PINK, None), 'Quantity_NOC_PINK1': (Quantity_NameOfColor.Quantity_NOC_PINK1, None), 'Quantity_NOC_PINK2': (Quantity_NameOfColor.Quantity_NOC_PINK2, None), 'Quantity_NOC_PINK3': (Quantity_NameOfColor.Quantity_NOC_PINK3, None), 'Quantity_NOC_PINK4': (Quantity_NameOfColor.Quantity_NOC_PINK4, None), 'Quantity_NOC_PLUM': (Quantity_NameOfColor.Quantity_NOC_PLUM, None), 'Quantity_NOC_PLUM1': (Quantity_NameOfColor.Quantity_NOC_PLUM1, None), 'Quantity_NOC_PLUM2': (Quantity_NameOfColor.Quantity_NOC_PLUM2, None), 'Quantity_NOC_PLUM3': (Quantity_NameOfColor.Quantity_NOC_PLUM3, None), 'Quantity_NOC_PLUM4': (Quantity_NameOfColor.Quantity_NOC_PLUM4, None), 'Quantity_NOC_POWDERBLUE': (Quantity_NameOfColor.Quantity_NOC_POWDERBLUE, None), 'Quantity_NOC_PURPLE': (Quantity_NameOfColor.Quantity_NOC_PURPLE, None), 'Quantity_NOC_PURPLE1': (Quantity_NameOfColor.Quantity_NOC_PURPLE1, None), 'Quantity_NOC_PURPLE2': (Quantity_NameOfColor.Quantity_NOC_PURPLE2, None), 'Quantity_NOC_PURPLE3': (Quantity_NameOfColor.Quantity_NOC_PURPLE3, None), 'Quantity_NOC_PURPLE4': (Quantity_NameOfColor.Quantity_NOC_PURPLE4, None), 'Quantity_NOC_RED': (Quantity_NameOfColor.Quantity_NOC_RED, None), 'Quantity_NOC_RED1': (Quantity_NameOfColor.Quantity_NOC_RED1, None), 'Quantity_NOC_RED2': (Quantity_NameOfColor.Quantity_NOC_RED2, None), 'Quantity_NOC_RED3': (Quantity_NameOfColor.Quantity_NOC_RED3, None), 'Quantity_NOC_RED4': (Quantity_NameOfColor.Quantity_NOC_RED4, None), 'Quantity_NOC_ROSYBROWN': (Quantity_NameOfColor.Quantity_NOC_ROSYBROWN, None), 'Quantity_NOC_ROSYBROWN1': (Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1, None), 'Quantity_NOC_ROSYBROWN2': (Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2, None), 'Quantity_NOC_ROSYBROWN3': (Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3, None), 'Quantity_NOC_ROSYBROWN4': (Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4, None), 'Quantity_NOC_ROYALBLUE': (Quantity_NameOfColor.Quantity_NOC_ROYALBLUE, None), 'Quantity_NOC_ROYALBLUE1': (Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1, None), 'Quantity_NOC_ROYALBLUE2': (Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2, None), 'Quantity_NOC_ROYALBLUE3': (Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3, None), 'Quantity_NOC_ROYALBLUE4': (Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4, None), 'Quantity_NOC_SADDLEBROWN': (Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN, None), 'Quantity_NOC_SALMON': (Quantity_NameOfColor.Quantity_NOC_SALMON, None), 'Quantity_NOC_SALMON1': (Quantity_NameOfColor.Quantity_NOC_SALMON1, None), 'Quantity_NOC_SALMON2': (Quantity_NameOfColor.Quantity_NOC_SALMON2, None), 'Quantity_NOC_SALMON3': (Quantity_NameOfColor.Quantity_NOC_SALMON3, None), 'Quantity_NOC_SALMON4': (Quantity_NameOfColor.Quantity_NOC_SALMON4, None), 'Quantity_NOC_SANDYBROWN': (Quantity_NameOfColor.Quantity_NOC_SANDYBROWN, None), 'Quantity_NOC_SEAGREEN': (Quantity_NameOfColor.Quantity_NOC_SEAGREEN, None), 'Quantity_NOC_SEAGREEN1': (Quantity_NameOfColor.Quantity_NOC_SEAGREEN1, None), 'Quantity_NOC_SEAGREEN2': (Quantity_NameOfColor.Quantity_NOC_SEAGREEN2, None), 'Quantity_NOC_SEAGREEN3': (Quantity_NameOfColor.Quantity_NOC_SEAGREEN3, None), 'Quantity_NOC_SEAGREEN4': (Quantity_NameOfColor.Quantity_NOC_SEAGREEN4, None), 'Quantity_NOC_SEASHELL': (Quantity_NameOfColor.Quantity_NOC_SEASHELL, None), 'Quantity_NOC_SEASHELL2': (Quantity_NameOfColor.Quantity_NOC_SEASHELL2, None), 'Quantity_NOC_SEASHELL3': (Quantity_NameOfColor.Quantity_NOC_SEASHELL3, None), 'Quantity_NOC_SEASHELL4': (Quantity_NameOfColor.Quantity_NOC_SEASHELL4, None), 'Quantity_NOC_BEET': (Quantity_NameOfColor.Quantity_NOC_BEET, None), 'Quantity_NOC_TEAL': (Quantity_NameOfColor.Quantity_NOC_TEAL, None), 'Quantity_NOC_SIENNA': (Quantity_NameOfColor.Quantity_NOC_SIENNA, None), 'Quantity_NOC_SIENNA1': (Quantity_NameOfColor.Quantity_NOC_SIENNA1, None), 'Quantity_NOC_SIENNA2': (Quantity_NameOfColor.Quantity_NOC_SIENNA2, None), 'Quantity_NOC_SIENNA3': (Quantity_NameOfColor.Quantity_NOC_SIENNA3, None), 'Quantity_NOC_SIENNA4': (Quantity_NameOfColor.Quantity_NOC_SIENNA4, None), 'Quantity_NOC_SKYBLUE': (Quantity_NameOfColor.Quantity_NOC_SKYBLUE, None), 'Quantity_NOC_SKYBLUE1': (Quantity_NameOfColor.Quantity_NOC_SKYBLUE1, None), 'Quantity_NOC_SKYBLUE2': (Quantity_NameOfColor.Quantity_NOC_SKYBLUE2, None), 'Quantity_NOC_SKYBLUE3': (Quantity_NameOfColor.Quantity_NOC_SKYBLUE3, None), 'Quantity_NOC_SKYBLUE4': (Quantity_NameOfColor.Quantity_NOC_SKYBLUE4, None), 'Quantity_NOC_SLATEBLUE': (Quantity_NameOfColor.Quantity_NOC_SLATEBLUE, None), 'Quantity_NOC_SLATEBLUE1': (Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1, None), 'Quantity_NOC_SLATEBLUE2': (Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2, None), 'Quantity_NOC_SLATEBLUE3': (Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3, None), 'Quantity_NOC_SLATEBLUE4': (Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4, None), 'Quantity_NOC_SLATEGRAY1': (Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1, None), 'Quantity_NOC_SLATEGRAY2': (Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2, None), 'Quantity_NOC_SLATEGRAY3': (Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3, None), 'Quantity_NOC_SLATEGRAY4': (Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4, None), 'Quantity_NOC_SLATEGRAY': (Quantity_NameOfColor.Quantity_NOC_SLATEGRAY, None), 'Quantity_NOC_SNOW': (Quantity_NameOfColor.Quantity_NOC_SNOW, None), 'Quantity_NOC_SNOW2': (Quantity_NameOfColor.Quantity_NOC_SNOW2, None), 'Quantity_NOC_SNOW3': (Quantity_NameOfColor.Quantity_NOC_SNOW3, None), 'Quantity_NOC_SNOW4': (Quantity_NameOfColor.Quantity_NOC_SNOW4, None), 'Quantity_NOC_SPRINGGREEN': (Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN, None), 'Quantity_NOC_SPRINGGREEN2': (Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2, None), 'Quantity_NOC_SPRINGGREEN3': (Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3, None), 'Quantity_NOC_SPRINGGREEN4': (Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4, None), 'Quantity_NOC_STEELBLUE': (Quantity_NameOfColor.Quantity_NOC_STEELBLUE, None), 'Quantity_NOC_STEELBLUE1': (Quantity_NameOfColor.Quantity_NOC_STEELBLUE1, None), 'Quantity_NOC_STEELBLUE2': (Quantity_NameOfColor.Quantity_NOC_STEELBLUE2, None), 'Quantity_NOC_STEELBLUE3': (Quantity_NameOfColor.Quantity_NOC_STEELBLUE3, None), 'Quantity_NOC_STEELBLUE4': (Quantity_NameOfColor.Quantity_NOC_STEELBLUE4, None), 'Quantity_NOC_TAN': (Quantity_NameOfColor.Quantity_NOC_TAN, None), 'Quantity_NOC_TAN1': (Quantity_NameOfColor.Quantity_NOC_TAN1, None), 'Quantity_NOC_TAN2': (Quantity_NameOfColor.Quantity_NOC_TAN2, None), 'Quantity_NOC_TAN3': (Quantity_NameOfColor.Quantity_NOC_TAN3, None), 'Quantity_NOC_TAN4': (Quantity_NameOfColor.Quantity_NOC_TAN4, None), 'Quantity_NOC_THISTLE': (Quantity_NameOfColor.Quantity_NOC_THISTLE, None), 'Quantity_NOC_THISTLE1': (Quantity_NameOfColor.Quantity_NOC_THISTLE1, None), 'Quantity_NOC_THISTLE2': (Quantity_NameOfColor.Quantity_NOC_THISTLE2, None), 'Quantity_NOC_THISTLE3': (Quantity_NameOfColor.Quantity_NOC_THISTLE3, None), 'Quantity_NOC_THISTLE4': (Quantity_NameOfColor.Quantity_NOC_THISTLE4, None), 'Quantity_NOC_TOMATO': (Quantity_NameOfColor.Quantity_NOC_TOMATO, None), 'Quantity_NOC_TOMATO1': (Quantity_NameOfColor.Quantity_NOC_TOMATO1, None), 'Quantity_NOC_TOMATO2': (Quantity_NameOfColor.Quantity_NOC_TOMATO2, None), 'Quantity_NOC_TOMATO3': (Quantity_NameOfColor.Quantity_NOC_TOMATO3, None), 'Quantity_NOC_TOMATO4': (Quantity_NameOfColor.Quantity_NOC_TOMATO4, None), 'Quantity_NOC_TURQUOISE': (Quantity_NameOfColor.Quantity_NOC_TURQUOISE, None), 'Quantity_NOC_TURQUOISE1': (Quantity_NameOfColor.Quantity_NOC_TURQUOISE1, None), 'Quantity_NOC_TURQUOISE2': (Quantity_NameOfColor.Quantity_NOC_TURQUOISE2, None), 'Quantity_NOC_TURQUOISE3': (Quantity_NameOfColor.Quantity_NOC_TURQUOISE3, None), 'Quantity_NOC_TURQUOISE4': (Quantity_NameOfColor.Quantity_NOC_TURQUOISE4, None), 'Quantity_NOC_VIOLET': (Quantity_NameOfColor.Quantity_NOC_VIOLET, None), 'Quantity_NOC_VIOLETRED': (Quantity_NameOfColor.Quantity_NOC_VIOLETRED, None), 'Quantity_NOC_VIOLETRED1': (Quantity_NameOfColor.Quantity_NOC_VIOLETRED1, None), 'Quantity_NOC_VIOLETRED2': (Quantity_NameOfColor.Quantity_NOC_VIOLETRED2, None), 'Quantity_NOC_VIOLETRED3': (Quantity_NameOfColor.Quantity_NOC_VIOLETRED3, None), 'Quantity_NOC_VIOLETRED4': (Quantity_NameOfColor.Quantity_NOC_VIOLETRED4, None), 'Quantity_NOC_WHEAT': (Quantity_NameOfColor.Quantity_NOC_WHEAT, None), 'Quantity_NOC_WHEAT1': (Quantity_NameOfColor.Quantity_NOC_WHEAT1, None), 'Quantity_NOC_WHEAT2': (Quantity_NameOfColor.Quantity_NOC_WHEAT2, None), 'Quantity_NOC_WHEAT3': (Quantity_NameOfColor.Quantity_NOC_WHEAT3, None), 'Quantity_NOC_WHEAT4': (Quantity_NameOfColor.Quantity_NOC_WHEAT4, None), 'Quantity_NOC_WHITESMOKE': (Quantity_NameOfColor.Quantity_NOC_WHITESMOKE, None), 'Quantity_NOC_YELLOW': (Quantity_NameOfColor.Quantity_NOC_YELLOW, None), 'Quantity_NOC_YELLOW1': (Quantity_NameOfColor.Quantity_NOC_YELLOW1, None), 'Quantity_NOC_YELLOW2': (Quantity_NameOfColor.Quantity_NOC_YELLOW2, None), 'Quantity_NOC_YELLOW3': (Quantity_NameOfColor.Quantity_NOC_YELLOW3, None), 'Quantity_NOC_YELLOW4': (Quantity_NameOfColor.Quantity_NOC_YELLOW4, None), 'Quantity_NOC_YELLOWGREEN': (Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN, None), 'Quantity_NOC_WHITE': (Quantity_NameOfColor.Quantity_NOC_WHITE, None)}
    __members__: dict # value = {'Quantity_NOC_BLACK': Quantity_NameOfColor.Quantity_NOC_BLACK, 'Quantity_NOC_MATRABLUE': Quantity_NameOfColor.Quantity_NOC_MATRABLUE, 'Quantity_NOC_MATRAGRAY': Quantity_NameOfColor.Quantity_NOC_MATRAGRAY, 'Quantity_NOC_ALICEBLUE': Quantity_NameOfColor.Quantity_NOC_ALICEBLUE, 'Quantity_NOC_ANTIQUEWHITE': Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE, 'Quantity_NOC_ANTIQUEWHITE1': Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1, 'Quantity_NOC_ANTIQUEWHITE2': Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2, 'Quantity_NOC_ANTIQUEWHITE3': Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3, 'Quantity_NOC_ANTIQUEWHITE4': Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4, 'Quantity_NOC_AQUAMARINE1': Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1, 'Quantity_NOC_AQUAMARINE2': Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2, 'Quantity_NOC_AQUAMARINE4': Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4, 'Quantity_NOC_AZURE': Quantity_NameOfColor.Quantity_NOC_AZURE, 'Quantity_NOC_AZURE2': Quantity_NameOfColor.Quantity_NOC_AZURE2, 'Quantity_NOC_AZURE3': Quantity_NameOfColor.Quantity_NOC_AZURE3, 'Quantity_NOC_AZURE4': Quantity_NameOfColor.Quantity_NOC_AZURE4, 'Quantity_NOC_BEIGE': Quantity_NameOfColor.Quantity_NOC_BEIGE, 'Quantity_NOC_BISQUE': Quantity_NameOfColor.Quantity_NOC_BISQUE, 'Quantity_NOC_BISQUE2': Quantity_NameOfColor.Quantity_NOC_BISQUE2, 'Quantity_NOC_BISQUE3': Quantity_NameOfColor.Quantity_NOC_BISQUE3, 'Quantity_NOC_BISQUE4': Quantity_NameOfColor.Quantity_NOC_BISQUE4, 'Quantity_NOC_BLANCHEDALMOND': Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND, 'Quantity_NOC_BLUE1': Quantity_NameOfColor.Quantity_NOC_BLUE1, 'Quantity_NOC_BLUE2': Quantity_NameOfColor.Quantity_NOC_BLUE2, 'Quantity_NOC_BLUE3': Quantity_NameOfColor.Quantity_NOC_BLUE3, 'Quantity_NOC_BLUE4': Quantity_NameOfColor.Quantity_NOC_BLUE4, 'Quantity_NOC_BLUEVIOLET': Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET, 'Quantity_NOC_BROWN': Quantity_NameOfColor.Quantity_NOC_BROWN, 'Quantity_NOC_BROWN1': Quantity_NameOfColor.Quantity_NOC_BROWN1, 'Quantity_NOC_BROWN2': Quantity_NameOfColor.Quantity_NOC_BROWN2, 'Quantity_NOC_BROWN3': Quantity_NameOfColor.Quantity_NOC_BROWN3, 'Quantity_NOC_BROWN4': Quantity_NameOfColor.Quantity_NOC_BROWN4, 'Quantity_NOC_BURLYWOOD': Quantity_NameOfColor.Quantity_NOC_BURLYWOOD, 'Quantity_NOC_BURLYWOOD1': Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1, 'Quantity_NOC_BURLYWOOD2': Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2, 'Quantity_NOC_BURLYWOOD3': Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3, 'Quantity_NOC_BURLYWOOD4': Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4, 'Quantity_NOC_CADETBLUE': Quantity_NameOfColor.Quantity_NOC_CADETBLUE, 'Quantity_NOC_CADETBLUE1': Quantity_NameOfColor.Quantity_NOC_CADETBLUE1, 'Quantity_NOC_CADETBLUE2': Quantity_NameOfColor.Quantity_NOC_CADETBLUE2, 'Quantity_NOC_CADETBLUE3': Quantity_NameOfColor.Quantity_NOC_CADETBLUE3, 'Quantity_NOC_CADETBLUE4': Quantity_NameOfColor.Quantity_NOC_CADETBLUE4, 'Quantity_NOC_CHARTREUSE': Quantity_NameOfColor.Quantity_NOC_CHARTREUSE, 'Quantity_NOC_CHARTREUSE1': Quantity_NameOfColor.Quantity_NOC_CHARTREUSE1, 'Quantity_NOC_CHARTREUSE2': Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2, 'Quantity_NOC_CHARTREUSE3': Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3, 'Quantity_NOC_CHARTREUSE4': Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4, 'Quantity_NOC_CHOCOLATE': Quantity_NameOfColor.Quantity_NOC_CHOCOLATE, 'Quantity_NOC_CHOCOLATE1': Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1, 'Quantity_NOC_CHOCOLATE2': Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2, 'Quantity_NOC_CHOCOLATE3': Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3, 'Quantity_NOC_CHOCOLATE4': Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4, 'Quantity_NOC_CORAL': Quantity_NameOfColor.Quantity_NOC_CORAL, 'Quantity_NOC_CORAL1': Quantity_NameOfColor.Quantity_NOC_CORAL1, 'Quantity_NOC_CORAL2': Quantity_NameOfColor.Quantity_NOC_CORAL2, 'Quantity_NOC_CORAL3': Quantity_NameOfColor.Quantity_NOC_CORAL3, 'Quantity_NOC_CORAL4': Quantity_NameOfColor.Quantity_NOC_CORAL4, 'Quantity_NOC_CORNFLOWERBLUE': Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE, 'Quantity_NOC_CORNSILK1': Quantity_NameOfColor.Quantity_NOC_CORNSILK1, 'Quantity_NOC_CORNSILK2': Quantity_NameOfColor.Quantity_NOC_CORNSILK2, 'Quantity_NOC_CORNSILK3': Quantity_NameOfColor.Quantity_NOC_CORNSILK3, 'Quantity_NOC_CORNSILK4': Quantity_NameOfColor.Quantity_NOC_CORNSILK4, 'Quantity_NOC_CYAN1': Quantity_NameOfColor.Quantity_NOC_CYAN1, 'Quantity_NOC_CYAN2': Quantity_NameOfColor.Quantity_NOC_CYAN2, 'Quantity_NOC_CYAN3': Quantity_NameOfColor.Quantity_NOC_CYAN3, 'Quantity_NOC_CYAN4': Quantity_NameOfColor.Quantity_NOC_CYAN4, 'Quantity_NOC_DARKGOLDENROD': Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD, 'Quantity_NOC_DARKGOLDENROD1': Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1, 'Quantity_NOC_DARKGOLDENROD2': Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2, 'Quantity_NOC_DARKGOLDENROD3': Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3, 'Quantity_NOC_DARKGOLDENROD4': Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4, 'Quantity_NOC_DARKGREEN': Quantity_NameOfColor.Quantity_NOC_DARKGREEN, 'Quantity_NOC_DARKKHAKI': Quantity_NameOfColor.Quantity_NOC_DARKKHAKI, 'Quantity_NOC_DARKOLIVEGREEN': Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN, 'Quantity_NOC_DARKOLIVEGREEN1': Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1, 'Quantity_NOC_DARKOLIVEGREEN2': Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2, 'Quantity_NOC_DARKOLIVEGREEN3': Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3, 'Quantity_NOC_DARKOLIVEGREEN4': Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4, 'Quantity_NOC_DARKORANGE': Quantity_NameOfColor.Quantity_NOC_DARKORANGE, 'Quantity_NOC_DARKORANGE1': Quantity_NameOfColor.Quantity_NOC_DARKORANGE1, 'Quantity_NOC_DARKORANGE2': Quantity_NameOfColor.Quantity_NOC_DARKORANGE2, 'Quantity_NOC_DARKORANGE3': Quantity_NameOfColor.Quantity_NOC_DARKORANGE3, 'Quantity_NOC_DARKORANGE4': Quantity_NameOfColor.Quantity_NOC_DARKORANGE4, 'Quantity_NOC_DARKORCHID': Quantity_NameOfColor.Quantity_NOC_DARKORCHID, 'Quantity_NOC_DARKORCHID1': Quantity_NameOfColor.Quantity_NOC_DARKORCHID1, 'Quantity_NOC_DARKORCHID2': Quantity_NameOfColor.Quantity_NOC_DARKORCHID2, 'Quantity_NOC_DARKORCHID3': Quantity_NameOfColor.Quantity_NOC_DARKORCHID3, 'Quantity_NOC_DARKORCHID4': Quantity_NameOfColor.Quantity_NOC_DARKORCHID4, 'Quantity_NOC_DARKSALMON': Quantity_NameOfColor.Quantity_NOC_DARKSALMON, 'Quantity_NOC_DARKSEAGREEN': Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN, 'Quantity_NOC_DARKSEAGREEN1': Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1, 'Quantity_NOC_DARKSEAGREEN2': Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2, 'Quantity_NOC_DARKSEAGREEN3': Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3, 'Quantity_NOC_DARKSEAGREEN4': Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4, 'Quantity_NOC_DARKSLATEBLUE': Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE, 'Quantity_NOC_DARKSLATEGRAY1': Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1, 'Quantity_NOC_DARKSLATEGRAY2': Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2, 'Quantity_NOC_DARKSLATEGRAY3': Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3, 'Quantity_NOC_DARKSLATEGRAY4': Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4, 'Quantity_NOC_DARKSLATEGRAY': Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY, 'Quantity_NOC_DARKTURQUOISE': Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE, 'Quantity_NOC_DARKVIOLET': Quantity_NameOfColor.Quantity_NOC_DARKVIOLET, 'Quantity_NOC_DEEPPINK': Quantity_NameOfColor.Quantity_NOC_DEEPPINK, 'Quantity_NOC_DEEPPINK2': Quantity_NameOfColor.Quantity_NOC_DEEPPINK2, 'Quantity_NOC_DEEPPINK3': Quantity_NameOfColor.Quantity_NOC_DEEPPINK3, 'Quantity_NOC_DEEPPINK4': Quantity_NameOfColor.Quantity_NOC_DEEPPINK4, 'Quantity_NOC_DEEPSKYBLUE1': Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1, 'Quantity_NOC_DEEPSKYBLUE2': Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2, 'Quantity_NOC_DEEPSKYBLUE3': Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3, 'Quantity_NOC_DEEPSKYBLUE4': Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4, 'Quantity_NOC_DODGERBLUE1': Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1, 'Quantity_NOC_DODGERBLUE2': Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2, 'Quantity_NOC_DODGERBLUE3': Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3, 'Quantity_NOC_DODGERBLUE4': Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4, 'Quantity_NOC_FIREBRICK': Quantity_NameOfColor.Quantity_NOC_FIREBRICK, 'Quantity_NOC_FIREBRICK1': Quantity_NameOfColor.Quantity_NOC_FIREBRICK1, 'Quantity_NOC_FIREBRICK2': Quantity_NameOfColor.Quantity_NOC_FIREBRICK2, 'Quantity_NOC_FIREBRICK3': Quantity_NameOfColor.Quantity_NOC_FIREBRICK3, 'Quantity_NOC_FIREBRICK4': Quantity_NameOfColor.Quantity_NOC_FIREBRICK4, 'Quantity_NOC_FLORALWHITE': Quantity_NameOfColor.Quantity_NOC_FLORALWHITE, 'Quantity_NOC_FORESTGREEN': Quantity_NameOfColor.Quantity_NOC_FORESTGREEN, 'Quantity_NOC_GAINSBORO': Quantity_NameOfColor.Quantity_NOC_GAINSBORO, 'Quantity_NOC_GHOSTWHITE': Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE, 'Quantity_NOC_GOLD': Quantity_NameOfColor.Quantity_NOC_GOLD, 'Quantity_NOC_GOLD1': Quantity_NameOfColor.Quantity_NOC_GOLD1, 'Quantity_NOC_GOLD2': Quantity_NameOfColor.Quantity_NOC_GOLD2, 'Quantity_NOC_GOLD3': Quantity_NameOfColor.Quantity_NOC_GOLD3, 'Quantity_NOC_GOLD4': Quantity_NameOfColor.Quantity_NOC_GOLD4, 'Quantity_NOC_GOLDENROD': Quantity_NameOfColor.Quantity_NOC_GOLDENROD, 'Quantity_NOC_GOLDENROD1': Quantity_NameOfColor.Quantity_NOC_GOLDENROD1, 'Quantity_NOC_GOLDENROD2': Quantity_NameOfColor.Quantity_NOC_GOLDENROD2, 'Quantity_NOC_GOLDENROD3': Quantity_NameOfColor.Quantity_NOC_GOLDENROD3, 'Quantity_NOC_GOLDENROD4': Quantity_NameOfColor.Quantity_NOC_GOLDENROD4, 'Quantity_NOC_GRAY': Quantity_NameOfColor.Quantity_NOC_GRAY, 'Quantity_NOC_GRAY0': Quantity_NameOfColor.Quantity_NOC_GRAY0, 'Quantity_NOC_GRAY1': Quantity_NameOfColor.Quantity_NOC_GRAY1, 'Quantity_NOC_GRAY10': Quantity_NameOfColor.Quantity_NOC_GRAY10, 'Quantity_NOC_GRAY11': Quantity_NameOfColor.Quantity_NOC_GRAY11, 'Quantity_NOC_GRAY12': Quantity_NameOfColor.Quantity_NOC_GRAY12, 'Quantity_NOC_GRAY13': Quantity_NameOfColor.Quantity_NOC_GRAY13, 'Quantity_NOC_GRAY14': Quantity_NameOfColor.Quantity_NOC_GRAY14, 'Quantity_NOC_GRAY15': Quantity_NameOfColor.Quantity_NOC_GRAY15, 'Quantity_NOC_GRAY16': Quantity_NameOfColor.Quantity_NOC_GRAY16, 'Quantity_NOC_GRAY17': Quantity_NameOfColor.Quantity_NOC_GRAY17, 'Quantity_NOC_GRAY18': Quantity_NameOfColor.Quantity_NOC_GRAY18, 'Quantity_NOC_GRAY19': Quantity_NameOfColor.Quantity_NOC_GRAY19, 'Quantity_NOC_GRAY2': Quantity_NameOfColor.Quantity_NOC_GRAY2, 'Quantity_NOC_GRAY20': Quantity_NameOfColor.Quantity_NOC_GRAY20, 'Quantity_NOC_GRAY21': Quantity_NameOfColor.Quantity_NOC_GRAY21, 'Quantity_NOC_GRAY22': Quantity_NameOfColor.Quantity_NOC_GRAY22, 'Quantity_NOC_GRAY23': Quantity_NameOfColor.Quantity_NOC_GRAY23, 'Quantity_NOC_GRAY24': Quantity_NameOfColor.Quantity_NOC_GRAY24, 'Quantity_NOC_GRAY25': Quantity_NameOfColor.Quantity_NOC_GRAY25, 'Quantity_NOC_GRAY26': Quantity_NameOfColor.Quantity_NOC_GRAY26, 'Quantity_NOC_GRAY27': Quantity_NameOfColor.Quantity_NOC_GRAY27, 'Quantity_NOC_GRAY28': Quantity_NameOfColor.Quantity_NOC_GRAY28, 'Quantity_NOC_GRAY29': Quantity_NameOfColor.Quantity_NOC_GRAY29, 'Quantity_NOC_GRAY3': Quantity_NameOfColor.Quantity_NOC_GRAY3, 'Quantity_NOC_GRAY30': Quantity_NameOfColor.Quantity_NOC_GRAY30, 'Quantity_NOC_GRAY31': Quantity_NameOfColor.Quantity_NOC_GRAY31, 'Quantity_NOC_GRAY32': Quantity_NameOfColor.Quantity_NOC_GRAY32, 'Quantity_NOC_GRAY33': Quantity_NameOfColor.Quantity_NOC_GRAY33, 'Quantity_NOC_GRAY34': Quantity_NameOfColor.Quantity_NOC_GRAY34, 'Quantity_NOC_GRAY35': Quantity_NameOfColor.Quantity_NOC_GRAY35, 'Quantity_NOC_GRAY36': Quantity_NameOfColor.Quantity_NOC_GRAY36, 'Quantity_NOC_GRAY37': Quantity_NameOfColor.Quantity_NOC_GRAY37, 'Quantity_NOC_GRAY38': Quantity_NameOfColor.Quantity_NOC_GRAY38, 'Quantity_NOC_GRAY39': Quantity_NameOfColor.Quantity_NOC_GRAY39, 'Quantity_NOC_GRAY4': Quantity_NameOfColor.Quantity_NOC_GRAY4, 'Quantity_NOC_GRAY40': Quantity_NameOfColor.Quantity_NOC_GRAY40, 'Quantity_NOC_GRAY41': Quantity_NameOfColor.Quantity_NOC_GRAY41, 'Quantity_NOC_GRAY42': Quantity_NameOfColor.Quantity_NOC_GRAY42, 'Quantity_NOC_GRAY43': Quantity_NameOfColor.Quantity_NOC_GRAY43, 'Quantity_NOC_GRAY44': Quantity_NameOfColor.Quantity_NOC_GRAY44, 'Quantity_NOC_GRAY45': Quantity_NameOfColor.Quantity_NOC_GRAY45, 'Quantity_NOC_GRAY46': Quantity_NameOfColor.Quantity_NOC_GRAY46, 'Quantity_NOC_GRAY47': Quantity_NameOfColor.Quantity_NOC_GRAY47, 'Quantity_NOC_GRAY48': Quantity_NameOfColor.Quantity_NOC_GRAY48, 'Quantity_NOC_GRAY49': Quantity_NameOfColor.Quantity_NOC_GRAY49, 'Quantity_NOC_GRAY5': Quantity_NameOfColor.Quantity_NOC_GRAY5, 'Quantity_NOC_GRAY50': Quantity_NameOfColor.Quantity_NOC_GRAY50, 'Quantity_NOC_GRAY51': Quantity_NameOfColor.Quantity_NOC_GRAY51, 'Quantity_NOC_GRAY52': Quantity_NameOfColor.Quantity_NOC_GRAY52, 'Quantity_NOC_GRAY53': Quantity_NameOfColor.Quantity_NOC_GRAY53, 'Quantity_NOC_GRAY54': Quantity_NameOfColor.Quantity_NOC_GRAY54, 'Quantity_NOC_GRAY55': Quantity_NameOfColor.Quantity_NOC_GRAY55, 'Quantity_NOC_GRAY56': Quantity_NameOfColor.Quantity_NOC_GRAY56, 'Quantity_NOC_GRAY57': Quantity_NameOfColor.Quantity_NOC_GRAY57, 'Quantity_NOC_GRAY58': Quantity_NameOfColor.Quantity_NOC_GRAY58, 'Quantity_NOC_GRAY59': Quantity_NameOfColor.Quantity_NOC_GRAY59, 'Quantity_NOC_GRAY6': Quantity_NameOfColor.Quantity_NOC_GRAY6, 'Quantity_NOC_GRAY60': Quantity_NameOfColor.Quantity_NOC_GRAY60, 'Quantity_NOC_GRAY61': Quantity_NameOfColor.Quantity_NOC_GRAY61, 'Quantity_NOC_GRAY62': Quantity_NameOfColor.Quantity_NOC_GRAY62, 'Quantity_NOC_GRAY63': Quantity_NameOfColor.Quantity_NOC_GRAY63, 'Quantity_NOC_GRAY64': Quantity_NameOfColor.Quantity_NOC_GRAY64, 'Quantity_NOC_GRAY65': Quantity_NameOfColor.Quantity_NOC_GRAY65, 'Quantity_NOC_GRAY66': Quantity_NameOfColor.Quantity_NOC_GRAY66, 'Quantity_NOC_GRAY67': Quantity_NameOfColor.Quantity_NOC_GRAY67, 'Quantity_NOC_GRAY68': Quantity_NameOfColor.Quantity_NOC_GRAY68, 'Quantity_NOC_GRAY69': Quantity_NameOfColor.Quantity_NOC_GRAY69, 'Quantity_NOC_GRAY7': Quantity_NameOfColor.Quantity_NOC_GRAY7, 'Quantity_NOC_GRAY70': Quantity_NameOfColor.Quantity_NOC_GRAY70, 'Quantity_NOC_GRAY71': Quantity_NameOfColor.Quantity_NOC_GRAY71, 'Quantity_NOC_GRAY72': Quantity_NameOfColor.Quantity_NOC_GRAY72, 'Quantity_NOC_GRAY73': Quantity_NameOfColor.Quantity_NOC_GRAY73, 'Quantity_NOC_GRAY74': Quantity_NameOfColor.Quantity_NOC_GRAY74, 'Quantity_NOC_GRAY75': Quantity_NameOfColor.Quantity_NOC_GRAY75, 'Quantity_NOC_GRAY76': Quantity_NameOfColor.Quantity_NOC_GRAY76, 'Quantity_NOC_GRAY77': Quantity_NameOfColor.Quantity_NOC_GRAY77, 'Quantity_NOC_GRAY78': Quantity_NameOfColor.Quantity_NOC_GRAY78, 'Quantity_NOC_GRAY79': Quantity_NameOfColor.Quantity_NOC_GRAY79, 'Quantity_NOC_GRAY8': Quantity_NameOfColor.Quantity_NOC_GRAY8, 'Quantity_NOC_GRAY80': Quantity_NameOfColor.Quantity_NOC_GRAY80, 'Quantity_NOC_GRAY81': Quantity_NameOfColor.Quantity_NOC_GRAY81, 'Quantity_NOC_GRAY82': Quantity_NameOfColor.Quantity_NOC_GRAY82, 'Quantity_NOC_GRAY83': Quantity_NameOfColor.Quantity_NOC_GRAY83, 'Quantity_NOC_GRAY85': Quantity_NameOfColor.Quantity_NOC_GRAY85, 'Quantity_NOC_GRAY86': Quantity_NameOfColor.Quantity_NOC_GRAY86, 'Quantity_NOC_GRAY87': Quantity_NameOfColor.Quantity_NOC_GRAY87, 'Quantity_NOC_GRAY88': Quantity_NameOfColor.Quantity_NOC_GRAY88, 'Quantity_NOC_GRAY89': Quantity_NameOfColor.Quantity_NOC_GRAY89, 'Quantity_NOC_GRAY9': Quantity_NameOfColor.Quantity_NOC_GRAY9, 'Quantity_NOC_GRAY90': Quantity_NameOfColor.Quantity_NOC_GRAY90, 'Quantity_NOC_GRAY91': Quantity_NameOfColor.Quantity_NOC_GRAY91, 'Quantity_NOC_GRAY92': Quantity_NameOfColor.Quantity_NOC_GRAY92, 'Quantity_NOC_GRAY93': Quantity_NameOfColor.Quantity_NOC_GRAY93, 'Quantity_NOC_GRAY94': Quantity_NameOfColor.Quantity_NOC_GRAY94, 'Quantity_NOC_GRAY95': Quantity_NameOfColor.Quantity_NOC_GRAY95, 'Quantity_NOC_GREEN': Quantity_NameOfColor.Quantity_NOC_GREEN, 'Quantity_NOC_GREEN1': Quantity_NameOfColor.Quantity_NOC_GREEN1, 'Quantity_NOC_GREEN2': Quantity_NameOfColor.Quantity_NOC_GREEN2, 'Quantity_NOC_GREEN3': Quantity_NameOfColor.Quantity_NOC_GREEN3, 'Quantity_NOC_GREEN4': Quantity_NameOfColor.Quantity_NOC_GREEN4, 'Quantity_NOC_GREENYELLOW': Quantity_NameOfColor.Quantity_NOC_GREENYELLOW, 'Quantity_NOC_GRAY97': Quantity_NameOfColor.Quantity_NOC_GRAY97, 'Quantity_NOC_GRAY98': Quantity_NameOfColor.Quantity_NOC_GRAY98, 'Quantity_NOC_GRAY99': Quantity_NameOfColor.Quantity_NOC_GRAY99, 'Quantity_NOC_HONEYDEW': Quantity_NameOfColor.Quantity_NOC_HONEYDEW, 'Quantity_NOC_HONEYDEW2': Quantity_NameOfColor.Quantity_NOC_HONEYDEW2, 'Quantity_NOC_HONEYDEW3': Quantity_NameOfColor.Quantity_NOC_HONEYDEW3, 'Quantity_NOC_HONEYDEW4': Quantity_NameOfColor.Quantity_NOC_HONEYDEW4, 'Quantity_NOC_HOTPINK': Quantity_NameOfColor.Quantity_NOC_HOTPINK, 'Quantity_NOC_HOTPINK1': Quantity_NameOfColor.Quantity_NOC_HOTPINK1, 'Quantity_NOC_HOTPINK2': Quantity_NameOfColor.Quantity_NOC_HOTPINK2, 'Quantity_NOC_HOTPINK3': Quantity_NameOfColor.Quantity_NOC_HOTPINK3, 'Quantity_NOC_HOTPINK4': Quantity_NameOfColor.Quantity_NOC_HOTPINK4, 'Quantity_NOC_INDIANRED': Quantity_NameOfColor.Quantity_NOC_INDIANRED, 'Quantity_NOC_INDIANRED1': Quantity_NameOfColor.Quantity_NOC_INDIANRED1, 'Quantity_NOC_INDIANRED2': Quantity_NameOfColor.Quantity_NOC_INDIANRED2, 'Quantity_NOC_INDIANRED3': Quantity_NameOfColor.Quantity_NOC_INDIANRED3, 'Quantity_NOC_INDIANRED4': Quantity_NameOfColor.Quantity_NOC_INDIANRED4, 'Quantity_NOC_IVORY': Quantity_NameOfColor.Quantity_NOC_IVORY, 'Quantity_NOC_IVORY2': Quantity_NameOfColor.Quantity_NOC_IVORY2, 'Quantity_NOC_IVORY3': Quantity_NameOfColor.Quantity_NOC_IVORY3, 'Quantity_NOC_IVORY4': Quantity_NameOfColor.Quantity_NOC_IVORY4, 'Quantity_NOC_KHAKI': Quantity_NameOfColor.Quantity_NOC_KHAKI, 'Quantity_NOC_KHAKI1': Quantity_NameOfColor.Quantity_NOC_KHAKI1, 'Quantity_NOC_KHAKI2': Quantity_NameOfColor.Quantity_NOC_KHAKI2, 'Quantity_NOC_KHAKI3': Quantity_NameOfColor.Quantity_NOC_KHAKI3, 'Quantity_NOC_KHAKI4': Quantity_NameOfColor.Quantity_NOC_KHAKI4, 'Quantity_NOC_LAVENDER': Quantity_NameOfColor.Quantity_NOC_LAVENDER, 'Quantity_NOC_LAVENDERBLUSH1': Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1, 'Quantity_NOC_LAVENDERBLUSH2': Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2, 'Quantity_NOC_LAVENDERBLUSH3': Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3, 'Quantity_NOC_LAVENDERBLUSH4': Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4, 'Quantity_NOC_LAWNGREEN': Quantity_NameOfColor.Quantity_NOC_LAWNGREEN, 'Quantity_NOC_LEMONCHIFFON1': Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1, 'Quantity_NOC_LEMONCHIFFON2': Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2, 'Quantity_NOC_LEMONCHIFFON3': Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3, 'Quantity_NOC_LEMONCHIFFON4': Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4, 'Quantity_NOC_LIGHTBLUE': Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE, 'Quantity_NOC_LIGHTBLUE1': Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1, 'Quantity_NOC_LIGHTBLUE2': Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2, 'Quantity_NOC_LIGHTBLUE3': Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3, 'Quantity_NOC_LIGHTBLUE4': Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4, 'Quantity_NOC_LIGHTCORAL': Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL, 'Quantity_NOC_LIGHTCYAN1': Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN1, 'Quantity_NOC_LIGHTCYAN2': Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2, 'Quantity_NOC_LIGHTCYAN3': Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3, 'Quantity_NOC_LIGHTCYAN4': Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4, 'Quantity_NOC_LIGHTGOLDENROD': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD, 'Quantity_NOC_LIGHTGOLDENROD1': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1, 'Quantity_NOC_LIGHTGOLDENROD2': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2, 'Quantity_NOC_LIGHTGOLDENROD3': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3, 'Quantity_NOC_LIGHTGOLDENROD4': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4, 'Quantity_NOC_LIGHTGOLDENRODYELLOW': Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW, 'Quantity_NOC_LIGHTGRAY': Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY, 'Quantity_NOC_LIGHTPINK': Quantity_NameOfColor.Quantity_NOC_LIGHTPINK, 'Quantity_NOC_LIGHTPINK1': Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1, 'Quantity_NOC_LIGHTPINK2': Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2, 'Quantity_NOC_LIGHTPINK3': Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3, 'Quantity_NOC_LIGHTPINK4': Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4, 'Quantity_NOC_LIGHTSALMON1': Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1, 'Quantity_NOC_LIGHTSALMON2': Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2, 'Quantity_NOC_LIGHTSALMON3': Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3, 'Quantity_NOC_LIGHTSALMON4': Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4, 'Quantity_NOC_LIGHTSEAGREEN': Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN, 'Quantity_NOC_LIGHTSKYBLUE': Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE, 'Quantity_NOC_LIGHTSKYBLUE1': Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1, 'Quantity_NOC_LIGHTSKYBLUE2': Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2, 'Quantity_NOC_LIGHTSKYBLUE3': Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3, 'Quantity_NOC_LIGHTSKYBLUE4': Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4, 'Quantity_NOC_LIGHTSLATEBLUE': Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE, 'Quantity_NOC_LIGHTSLATEGRAY': Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY, 'Quantity_NOC_LIGHTSTEELBLUE': Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE, 'Quantity_NOC_LIGHTSTEELBLUE1': Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1, 'Quantity_NOC_LIGHTSTEELBLUE2': Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2, 'Quantity_NOC_LIGHTSTEELBLUE3': Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3, 'Quantity_NOC_LIGHTSTEELBLUE4': Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4, 'Quantity_NOC_LIGHTYELLOW': Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW, 'Quantity_NOC_LIGHTYELLOW2': Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2, 'Quantity_NOC_LIGHTYELLOW3': Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3, 'Quantity_NOC_LIGHTYELLOW4': Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4, 'Quantity_NOC_LIMEGREEN': Quantity_NameOfColor.Quantity_NOC_LIMEGREEN, 'Quantity_NOC_LINEN': Quantity_NameOfColor.Quantity_NOC_LINEN, 'Quantity_NOC_MAGENTA1': Quantity_NameOfColor.Quantity_NOC_MAGENTA1, 'Quantity_NOC_MAGENTA2': Quantity_NameOfColor.Quantity_NOC_MAGENTA2, 'Quantity_NOC_MAGENTA3': Quantity_NameOfColor.Quantity_NOC_MAGENTA3, 'Quantity_NOC_MAGENTA4': Quantity_NameOfColor.Quantity_NOC_MAGENTA4, 'Quantity_NOC_MAROON': Quantity_NameOfColor.Quantity_NOC_MAROON, 'Quantity_NOC_MAROON1': Quantity_NameOfColor.Quantity_NOC_MAROON1, 'Quantity_NOC_MAROON2': Quantity_NameOfColor.Quantity_NOC_MAROON2, 'Quantity_NOC_MAROON3': Quantity_NameOfColor.Quantity_NOC_MAROON3, 'Quantity_NOC_MAROON4': Quantity_NameOfColor.Quantity_NOC_MAROON4, 'Quantity_NOC_MEDIUMAQUAMARINE': Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE, 'Quantity_NOC_MEDIUMORCHID': Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID, 'Quantity_NOC_MEDIUMORCHID1': Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1, 'Quantity_NOC_MEDIUMORCHID2': Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2, 'Quantity_NOC_MEDIUMORCHID3': Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3, 'Quantity_NOC_MEDIUMORCHID4': Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4, 'Quantity_NOC_MEDIUMPURPLE': Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE, 'Quantity_NOC_MEDIUMPURPLE1': Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1, 'Quantity_NOC_MEDIUMPURPLE2': Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2, 'Quantity_NOC_MEDIUMPURPLE3': Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3, 'Quantity_NOC_MEDIUMPURPLE4': Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4, 'Quantity_NOC_MEDIUMSEAGREEN': Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN, 'Quantity_NOC_MEDIUMSLATEBLUE': Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE, 'Quantity_NOC_MEDIUMSPRINGGREEN': Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN, 'Quantity_NOC_MEDIUMTURQUOISE': Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE, 'Quantity_NOC_MEDIUMVIOLETRED': Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED, 'Quantity_NOC_MIDNIGHTBLUE': Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE, 'Quantity_NOC_MINTCREAM': Quantity_NameOfColor.Quantity_NOC_MINTCREAM, 'Quantity_NOC_MISTYROSE': Quantity_NameOfColor.Quantity_NOC_MISTYROSE, 'Quantity_NOC_MISTYROSE2': Quantity_NameOfColor.Quantity_NOC_MISTYROSE2, 'Quantity_NOC_MISTYROSE3': Quantity_NameOfColor.Quantity_NOC_MISTYROSE3, 'Quantity_NOC_MISTYROSE4': Quantity_NameOfColor.Quantity_NOC_MISTYROSE4, 'Quantity_NOC_MOCCASIN': Quantity_NameOfColor.Quantity_NOC_MOCCASIN, 'Quantity_NOC_NAVAJOWHITE1': Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1, 'Quantity_NOC_NAVAJOWHITE2': Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2, 'Quantity_NOC_NAVAJOWHITE3': Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3, 'Quantity_NOC_NAVAJOWHITE4': Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4, 'Quantity_NOC_NAVYBLUE': Quantity_NameOfColor.Quantity_NOC_NAVYBLUE, 'Quantity_NOC_OLDLACE': Quantity_NameOfColor.Quantity_NOC_OLDLACE, 'Quantity_NOC_OLIVEDRAB': Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB, 'Quantity_NOC_OLIVEDRAB1': Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1, 'Quantity_NOC_OLIVEDRAB2': Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2, 'Quantity_NOC_OLIVEDRAB3': Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3, 'Quantity_NOC_OLIVEDRAB4': Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4, 'Quantity_NOC_ORANGE': Quantity_NameOfColor.Quantity_NOC_ORANGE, 'Quantity_NOC_ORANGE1': Quantity_NameOfColor.Quantity_NOC_ORANGE1, 'Quantity_NOC_ORANGE2': Quantity_NameOfColor.Quantity_NOC_ORANGE2, 'Quantity_NOC_ORANGE3': Quantity_NameOfColor.Quantity_NOC_ORANGE3, 'Quantity_NOC_ORANGE4': Quantity_NameOfColor.Quantity_NOC_ORANGE4, 'Quantity_NOC_ORANGERED': Quantity_NameOfColor.Quantity_NOC_ORANGERED, 'Quantity_NOC_ORANGERED1': Quantity_NameOfColor.Quantity_NOC_ORANGERED1, 'Quantity_NOC_ORANGERED2': Quantity_NameOfColor.Quantity_NOC_ORANGERED2, 'Quantity_NOC_ORANGERED3': Quantity_NameOfColor.Quantity_NOC_ORANGERED3, 'Quantity_NOC_ORANGERED4': Quantity_NameOfColor.Quantity_NOC_ORANGERED4, 'Quantity_NOC_ORCHID': Quantity_NameOfColor.Quantity_NOC_ORCHID, 'Quantity_NOC_ORCHID1': Quantity_NameOfColor.Quantity_NOC_ORCHID1, 'Quantity_NOC_ORCHID2': Quantity_NameOfColor.Quantity_NOC_ORCHID2, 'Quantity_NOC_ORCHID3': Quantity_NameOfColor.Quantity_NOC_ORCHID3, 'Quantity_NOC_ORCHID4': Quantity_NameOfColor.Quantity_NOC_ORCHID4, 'Quantity_NOC_PALEGOLDENROD': Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD, 'Quantity_NOC_PALEGREEN': Quantity_NameOfColor.Quantity_NOC_PALEGREEN, 'Quantity_NOC_PALEGREEN1': Quantity_NameOfColor.Quantity_NOC_PALEGREEN1, 'Quantity_NOC_PALEGREEN2': Quantity_NameOfColor.Quantity_NOC_PALEGREEN2, 'Quantity_NOC_PALEGREEN3': Quantity_NameOfColor.Quantity_NOC_PALEGREEN3, 'Quantity_NOC_PALEGREEN4': Quantity_NameOfColor.Quantity_NOC_PALEGREEN4, 'Quantity_NOC_PALETURQUOISE': Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE, 'Quantity_NOC_PALETURQUOISE1': Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1, 'Quantity_NOC_PALETURQUOISE2': Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2, 'Quantity_NOC_PALETURQUOISE3': Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3, 'Quantity_NOC_PALETURQUOISE4': Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4, 'Quantity_NOC_PALEVIOLETRED': Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED, 'Quantity_NOC_PALEVIOLETRED1': Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1, 'Quantity_NOC_PALEVIOLETRED2': Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2, 'Quantity_NOC_PALEVIOLETRED3': Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3, 'Quantity_NOC_PALEVIOLETRED4': Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4, 'Quantity_NOC_PAPAYAWHIP': Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP, 'Quantity_NOC_PEACHPUFF': Quantity_NameOfColor.Quantity_NOC_PEACHPUFF, 'Quantity_NOC_PEACHPUFF2': Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2, 'Quantity_NOC_PEACHPUFF3': Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3, 'Quantity_NOC_PEACHPUFF4': Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4, 'Quantity_NOC_PERU': Quantity_NameOfColor.Quantity_NOC_PERU, 'Quantity_NOC_PINK': Quantity_NameOfColor.Quantity_NOC_PINK, 'Quantity_NOC_PINK1': Quantity_NameOfColor.Quantity_NOC_PINK1, 'Quantity_NOC_PINK2': Quantity_NameOfColor.Quantity_NOC_PINK2, 'Quantity_NOC_PINK3': Quantity_NameOfColor.Quantity_NOC_PINK3, 'Quantity_NOC_PINK4': Quantity_NameOfColor.Quantity_NOC_PINK4, 'Quantity_NOC_PLUM': Quantity_NameOfColor.Quantity_NOC_PLUM, 'Quantity_NOC_PLUM1': Quantity_NameOfColor.Quantity_NOC_PLUM1, 'Quantity_NOC_PLUM2': Quantity_NameOfColor.Quantity_NOC_PLUM2, 'Quantity_NOC_PLUM3': Quantity_NameOfColor.Quantity_NOC_PLUM3, 'Quantity_NOC_PLUM4': Quantity_NameOfColor.Quantity_NOC_PLUM4, 'Quantity_NOC_POWDERBLUE': Quantity_NameOfColor.Quantity_NOC_POWDERBLUE, 'Quantity_NOC_PURPLE': Quantity_NameOfColor.Quantity_NOC_PURPLE, 'Quantity_NOC_PURPLE1': Quantity_NameOfColor.Quantity_NOC_PURPLE1, 'Quantity_NOC_PURPLE2': Quantity_NameOfColor.Quantity_NOC_PURPLE2, 'Quantity_NOC_PURPLE3': Quantity_NameOfColor.Quantity_NOC_PURPLE3, 'Quantity_NOC_PURPLE4': Quantity_NameOfColor.Quantity_NOC_PURPLE4, 'Quantity_NOC_RED': Quantity_NameOfColor.Quantity_NOC_RED, 'Quantity_NOC_RED1': Quantity_NameOfColor.Quantity_NOC_RED1, 'Quantity_NOC_RED2': Quantity_NameOfColor.Quantity_NOC_RED2, 'Quantity_NOC_RED3': Quantity_NameOfColor.Quantity_NOC_RED3, 'Quantity_NOC_RED4': Quantity_NameOfColor.Quantity_NOC_RED4, 'Quantity_NOC_ROSYBROWN': Quantity_NameOfColor.Quantity_NOC_ROSYBROWN, 'Quantity_NOC_ROSYBROWN1': Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1, 'Quantity_NOC_ROSYBROWN2': Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2, 'Quantity_NOC_ROSYBROWN3': Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3, 'Quantity_NOC_ROSYBROWN4': Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4, 'Quantity_NOC_ROYALBLUE': Quantity_NameOfColor.Quantity_NOC_ROYALBLUE, 'Quantity_NOC_ROYALBLUE1': Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1, 'Quantity_NOC_ROYALBLUE2': Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2, 'Quantity_NOC_ROYALBLUE3': Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3, 'Quantity_NOC_ROYALBLUE4': Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4, 'Quantity_NOC_SADDLEBROWN': Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN, 'Quantity_NOC_SALMON': Quantity_NameOfColor.Quantity_NOC_SALMON, 'Quantity_NOC_SALMON1': Quantity_NameOfColor.Quantity_NOC_SALMON1, 'Quantity_NOC_SALMON2': Quantity_NameOfColor.Quantity_NOC_SALMON2, 'Quantity_NOC_SALMON3': Quantity_NameOfColor.Quantity_NOC_SALMON3, 'Quantity_NOC_SALMON4': Quantity_NameOfColor.Quantity_NOC_SALMON4, 'Quantity_NOC_SANDYBROWN': Quantity_NameOfColor.Quantity_NOC_SANDYBROWN, 'Quantity_NOC_SEAGREEN': Quantity_NameOfColor.Quantity_NOC_SEAGREEN, 'Quantity_NOC_SEAGREEN1': Quantity_NameOfColor.Quantity_NOC_SEAGREEN1, 'Quantity_NOC_SEAGREEN2': Quantity_NameOfColor.Quantity_NOC_SEAGREEN2, 'Quantity_NOC_SEAGREEN3': Quantity_NameOfColor.Quantity_NOC_SEAGREEN3, 'Quantity_NOC_SEAGREEN4': Quantity_NameOfColor.Quantity_NOC_SEAGREEN4, 'Quantity_NOC_SEASHELL': Quantity_NameOfColor.Quantity_NOC_SEASHELL, 'Quantity_NOC_SEASHELL2': Quantity_NameOfColor.Quantity_NOC_SEASHELL2, 'Quantity_NOC_SEASHELL3': Quantity_NameOfColor.Quantity_NOC_SEASHELL3, 'Quantity_NOC_SEASHELL4': Quantity_NameOfColor.Quantity_NOC_SEASHELL4, 'Quantity_NOC_BEET': Quantity_NameOfColor.Quantity_NOC_BEET, 'Quantity_NOC_TEAL': Quantity_NameOfColor.Quantity_NOC_TEAL, 'Quantity_NOC_SIENNA': Quantity_NameOfColor.Quantity_NOC_SIENNA, 'Quantity_NOC_SIENNA1': Quantity_NameOfColor.Quantity_NOC_SIENNA1, 'Quantity_NOC_SIENNA2': Quantity_NameOfColor.Quantity_NOC_SIENNA2, 'Quantity_NOC_SIENNA3': Quantity_NameOfColor.Quantity_NOC_SIENNA3, 'Quantity_NOC_SIENNA4': Quantity_NameOfColor.Quantity_NOC_SIENNA4, 'Quantity_NOC_SKYBLUE': Quantity_NameOfColor.Quantity_NOC_SKYBLUE, 'Quantity_NOC_SKYBLUE1': Quantity_NameOfColor.Quantity_NOC_SKYBLUE1, 'Quantity_NOC_SKYBLUE2': Quantity_NameOfColor.Quantity_NOC_SKYBLUE2, 'Quantity_NOC_SKYBLUE3': Quantity_NameOfColor.Quantity_NOC_SKYBLUE3, 'Quantity_NOC_SKYBLUE4': Quantity_NameOfColor.Quantity_NOC_SKYBLUE4, 'Quantity_NOC_SLATEBLUE': Quantity_NameOfColor.Quantity_NOC_SLATEBLUE, 'Quantity_NOC_SLATEBLUE1': Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1, 'Quantity_NOC_SLATEBLUE2': Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2, 'Quantity_NOC_SLATEBLUE3': Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3, 'Quantity_NOC_SLATEBLUE4': Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4, 'Quantity_NOC_SLATEGRAY1': Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1, 'Quantity_NOC_SLATEGRAY2': Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2, 'Quantity_NOC_SLATEGRAY3': Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3, 'Quantity_NOC_SLATEGRAY4': Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4, 'Quantity_NOC_SLATEGRAY': Quantity_NameOfColor.Quantity_NOC_SLATEGRAY, 'Quantity_NOC_SNOW': Quantity_NameOfColor.Quantity_NOC_SNOW, 'Quantity_NOC_SNOW2': Quantity_NameOfColor.Quantity_NOC_SNOW2, 'Quantity_NOC_SNOW3': Quantity_NameOfColor.Quantity_NOC_SNOW3, 'Quantity_NOC_SNOW4': Quantity_NameOfColor.Quantity_NOC_SNOW4, 'Quantity_NOC_SPRINGGREEN': Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN, 'Quantity_NOC_SPRINGGREEN2': Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2, 'Quantity_NOC_SPRINGGREEN3': Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3, 'Quantity_NOC_SPRINGGREEN4': Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4, 'Quantity_NOC_STEELBLUE': Quantity_NameOfColor.Quantity_NOC_STEELBLUE, 'Quantity_NOC_STEELBLUE1': Quantity_NameOfColor.Quantity_NOC_STEELBLUE1, 'Quantity_NOC_STEELBLUE2': Quantity_NameOfColor.Quantity_NOC_STEELBLUE2, 'Quantity_NOC_STEELBLUE3': Quantity_NameOfColor.Quantity_NOC_STEELBLUE3, 'Quantity_NOC_STEELBLUE4': Quantity_NameOfColor.Quantity_NOC_STEELBLUE4, 'Quantity_NOC_TAN': Quantity_NameOfColor.Quantity_NOC_TAN, 'Quantity_NOC_TAN1': Quantity_NameOfColor.Quantity_NOC_TAN1, 'Quantity_NOC_TAN2': Quantity_NameOfColor.Quantity_NOC_TAN2, 'Quantity_NOC_TAN3': Quantity_NameOfColor.Quantity_NOC_TAN3, 'Quantity_NOC_TAN4': Quantity_NameOfColor.Quantity_NOC_TAN4, 'Quantity_NOC_THISTLE': Quantity_NameOfColor.Quantity_NOC_THISTLE, 'Quantity_NOC_THISTLE1': Quantity_NameOfColor.Quantity_NOC_THISTLE1, 'Quantity_NOC_THISTLE2': Quantity_NameOfColor.Quantity_NOC_THISTLE2, 'Quantity_NOC_THISTLE3': Quantity_NameOfColor.Quantity_NOC_THISTLE3, 'Quantity_NOC_THISTLE4': Quantity_NameOfColor.Quantity_NOC_THISTLE4, 'Quantity_NOC_TOMATO': Quantity_NameOfColor.Quantity_NOC_TOMATO, 'Quantity_NOC_TOMATO1': Quantity_NameOfColor.Quantity_NOC_TOMATO1, 'Quantity_NOC_TOMATO2': Quantity_NameOfColor.Quantity_NOC_TOMATO2, 'Quantity_NOC_TOMATO3': Quantity_NameOfColor.Quantity_NOC_TOMATO3, 'Quantity_NOC_TOMATO4': Quantity_NameOfColor.Quantity_NOC_TOMATO4, 'Quantity_NOC_TURQUOISE': Quantity_NameOfColor.Quantity_NOC_TURQUOISE, 'Quantity_NOC_TURQUOISE1': Quantity_NameOfColor.Quantity_NOC_TURQUOISE1, 'Quantity_NOC_TURQUOISE2': Quantity_NameOfColor.Quantity_NOC_TURQUOISE2, 'Quantity_NOC_TURQUOISE3': Quantity_NameOfColor.Quantity_NOC_TURQUOISE3, 'Quantity_NOC_TURQUOISE4': Quantity_NameOfColor.Quantity_NOC_TURQUOISE4, 'Quantity_NOC_VIOLET': Quantity_NameOfColor.Quantity_NOC_VIOLET, 'Quantity_NOC_VIOLETRED': Quantity_NameOfColor.Quantity_NOC_VIOLETRED, 'Quantity_NOC_VIOLETRED1': Quantity_NameOfColor.Quantity_NOC_VIOLETRED1, 'Quantity_NOC_VIOLETRED2': Quantity_NameOfColor.Quantity_NOC_VIOLETRED2, 'Quantity_NOC_VIOLETRED3': Quantity_NameOfColor.Quantity_NOC_VIOLETRED3, 'Quantity_NOC_VIOLETRED4': Quantity_NameOfColor.Quantity_NOC_VIOLETRED4, 'Quantity_NOC_WHEAT': Quantity_NameOfColor.Quantity_NOC_WHEAT, 'Quantity_NOC_WHEAT1': Quantity_NameOfColor.Quantity_NOC_WHEAT1, 'Quantity_NOC_WHEAT2': Quantity_NameOfColor.Quantity_NOC_WHEAT2, 'Quantity_NOC_WHEAT3': Quantity_NameOfColor.Quantity_NOC_WHEAT3, 'Quantity_NOC_WHEAT4': Quantity_NameOfColor.Quantity_NOC_WHEAT4, 'Quantity_NOC_WHITESMOKE': Quantity_NameOfColor.Quantity_NOC_WHITESMOKE, 'Quantity_NOC_YELLOW': Quantity_NameOfColor.Quantity_NOC_YELLOW, 'Quantity_NOC_YELLOW1': Quantity_NameOfColor.Quantity_NOC_YELLOW1, 'Quantity_NOC_YELLOW2': Quantity_NameOfColor.Quantity_NOC_YELLOW2, 'Quantity_NOC_YELLOW3': Quantity_NameOfColor.Quantity_NOC_YELLOW3, 'Quantity_NOC_YELLOW4': Quantity_NameOfColor.Quantity_NOC_YELLOW4, 'Quantity_NOC_YELLOWGREEN': Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN, 'Quantity_NOC_WHITE': Quantity_NameOfColor.Quantity_NOC_WHITE}
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
    def IsValid_s(dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> bool: 
        """
        Checks the validity of a Period in form (dd,hh,mn,ss,mil,mic) With: 0 <= dd 0 <= hh 0 <= mn 0 <= ss 0 <= mis 0 <= mics

        Checks the validity of a Period in form (ss,mic) With: 0 <= ss 0 <= mics
        """
    @staticmethod
    @overload
    def IsValid_s(ss : int,mics : int=0) -> bool: ...
    @overload
    def SetValues(self,dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: 
        """
        Assigns to this period the time interval defined - with dd days, hh hours, mn minutes, ss seconds, mis (defaulted to 0) milliseconds and mics (defaulted to 0) microseconds; or

        Assigns to this period the time interval defined - with Ss seconds and Mics (defaulted to 0) microseconds. Exceptions Quantity_PeriodDefinitionError: - if the number of seconds expressed either by: - dd days, hh hours, mn minutes and ss seconds, or - Ss is less than 0. - if the number of microseconds expressed either by: - mis milliseconds and mics microseconds, or - Mics is less than 0.
        """
    @overload
    def SetValues(self,ss : int,mics : int=0) -> None: ...
    def Subtract(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        Subtracts one Period from another and returns the difference.
        """
    @overload
    def Values(self) -> Tuple[int, int]: 
        """
        Decomposes this period into a number of days,hours, minutes,seconds,milliseconds and microseconds Example of return values: 2 days, 15 hours, 0 minute , 0 second 0 millisecond and 0 microsecond

        Returns the number of seconds in Ss and the number of remainding microseconds in Mics of this period. Example of return values: 3600 seconds and 0 microseconds
        """
    @overload
    def Values(self) -> Tuple[int, int, int, int, int, int]: ...
    def __add__(self,anOther : Quantity_Period) -> Quantity_Period: 
        """
        None
        """
    @overload
    def __init__(self,dd : int,hh : int,mn : int,ss : int,mis : int=0,mics : int=0) -> None: ...
    @overload
    def __init__(self,ss : int,mics : int=0) -> None: ...
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
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Quantity_ABSORBEDDOSE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE
    Quantity_ACCELERATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACCELERATION
    Quantity_ACOUSTICINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY
    Quantity_ACTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACTIVITY
    Quantity_ADMITTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ADMITTANCE
    Quantity_AMOUNTOFSUBSTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE
    Quantity_ANGULARVELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY
    Quantity_AREA: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_AREA
    Quantity_CAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CAPACITANCE
    Quantity_COEFFICIENTOFEXPANSION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION
    Quantity_CONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONCENTRATION
    Quantity_CONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY
    Quantity_CONSUMPTION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONSUMPTION
    Quantity_DENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_DENSITY
    Quantity_DOSEEQUIVALENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT
    Quantity_ELECTRICCAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE
    Quantity_ELECTRICCHARGE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE
    Quantity_ELECTRICCURRENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT
    Quantity_ELECTRICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH
    Quantity_ELECTRICPOTENTIAL: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL
    Quantity_ENERGY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENERGY
    Quantity_ENTHALPY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENTHALPY
    Quantity_ENTROPY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENTROPY
    Quantity_FORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_FORCE
    Quantity_FREQUENCY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_FREQUENCY
    Quantity_ILLUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ILLUMINANCE
    Quantity_IMPEDANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_IMPEDANCE
    Quantity_INDUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_INDUCTANCE
    Quantity_KINEMATICVISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY
    Quantity_KINETICMOMENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_KINETICMOMENT
    Quantity_LENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LENGTH
    Quantity_LUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINANCE
    Quantity_LUMINOUSEFFICACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY
    Quantity_LUMINOUSEXPOSITION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION
    Quantity_LUMINOUSFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX
    Quantity_LUMINOUSINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY
    Quantity_MAGNETICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH
    Quantity_MAGNETICFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX
    Quantity_MAGNETICFLUXDENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY
    Quantity_MASS: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MASS
    Quantity_MASSFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MASSFLOW
    Quantity_MOLARCONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION
    Quantity_MOLARITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARITY
    Quantity_MOLARMASS: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARMASS
    Quantity_MOLARVOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARVOLUME
    Quantity_MOMENTOFAFORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE
    Quantity_MOMENTOFINERTIA: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA
    Quantity_MOMENTUM: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTUM
    Quantity_PLANEANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_PLANEANGLE
    Quantity_POWER: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_POWER
    Quantity_PRESSURE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_PRESSURE
    Quantity_RELUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RELUCTANCE
    Quantity_RESISTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RESISTANCE
    Quantity_RESISTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RESISTIVITY
    Quantity_SOLIDANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SOLIDANGLE
    Quantity_SOUNDINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY
    Quantity_SPECIFICHEATCAPACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY
    Quantity_SPEED: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SPEED
    Quantity_SURFACETENSION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SURFACETENSION
    Quantity_TEMPERATURE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_TEMPERATURE
    Quantity_THERMALCONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY
    Quantity_TORQUE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_TORQUE
    Quantity_VELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VELOCITY
    Quantity_VISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VISCOSITY
    Quantity_VOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VOLUME
    Quantity_VOLUMEFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW
    Quantity_WEIGHT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_WEIGHT
    Quantity_WORK: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_WORK
    __entries: dict # value = {'Quantity_MASS': (Quantity_PhysicalQuantity.Quantity_MASS, None), 'Quantity_PLANEANGLE': (Quantity_PhysicalQuantity.Quantity_PLANEANGLE, None), 'Quantity_SOLIDANGLE': (Quantity_PhysicalQuantity.Quantity_SOLIDANGLE, None), 'Quantity_LENGTH': (Quantity_PhysicalQuantity.Quantity_LENGTH, None), 'Quantity_AREA': (Quantity_PhysicalQuantity.Quantity_AREA, None), 'Quantity_VOLUME': (Quantity_PhysicalQuantity.Quantity_VOLUME, None), 'Quantity_SPEED': (Quantity_PhysicalQuantity.Quantity_SPEED, None), 'Quantity_VELOCITY': (Quantity_PhysicalQuantity.Quantity_VELOCITY, None), 'Quantity_ACCELERATION': (Quantity_PhysicalQuantity.Quantity_ACCELERATION, None), 'Quantity_ANGULARVELOCITY': (Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY, None), 'Quantity_FREQUENCY': (Quantity_PhysicalQuantity.Quantity_FREQUENCY, None), 'Quantity_TEMPERATURE': (Quantity_PhysicalQuantity.Quantity_TEMPERATURE, None), 'Quantity_AMOUNTOFSUBSTANCE': (Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE, None), 'Quantity_DENSITY': (Quantity_PhysicalQuantity.Quantity_DENSITY, None), 'Quantity_MASSFLOW': (Quantity_PhysicalQuantity.Quantity_MASSFLOW, None), 'Quantity_VOLUMEFLOW': (Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW, None), 'Quantity_CONSUMPTION': (Quantity_PhysicalQuantity.Quantity_CONSUMPTION, None), 'Quantity_MOMENTUM': (Quantity_PhysicalQuantity.Quantity_MOMENTUM, None), 'Quantity_KINETICMOMENT': (Quantity_PhysicalQuantity.Quantity_KINETICMOMENT, None), 'Quantity_MOMENTOFINERTIA': (Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA, None), 'Quantity_FORCE': (Quantity_PhysicalQuantity.Quantity_FORCE, None), 'Quantity_MOMENTOFAFORCE': (Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE, None), 'Quantity_TORQUE': (Quantity_PhysicalQuantity.Quantity_TORQUE, None), 'Quantity_WEIGHT': (Quantity_PhysicalQuantity.Quantity_WEIGHT, None), 'Quantity_PRESSURE': (Quantity_PhysicalQuantity.Quantity_PRESSURE, None), 'Quantity_VISCOSITY': (Quantity_PhysicalQuantity.Quantity_VISCOSITY, None), 'Quantity_KINEMATICVISCOSITY': (Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY, None), 'Quantity_ENERGY': (Quantity_PhysicalQuantity.Quantity_ENERGY, None), 'Quantity_WORK': (Quantity_PhysicalQuantity.Quantity_WORK, None), 'Quantity_POWER': (Quantity_PhysicalQuantity.Quantity_POWER, None), 'Quantity_SURFACETENSION': (Quantity_PhysicalQuantity.Quantity_SURFACETENSION, None), 'Quantity_COEFFICIENTOFEXPANSION': (Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION, None), 'Quantity_THERMALCONDUCTIVITY': (Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY, None), 'Quantity_SPECIFICHEATCAPACITY': (Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY, None), 'Quantity_ENTROPY': (Quantity_PhysicalQuantity.Quantity_ENTROPY, None), 'Quantity_ENTHALPY': (Quantity_PhysicalQuantity.Quantity_ENTHALPY, None), 'Quantity_LUMINOUSINTENSITY': (Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY, None), 'Quantity_LUMINOUSFLUX': (Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX, None), 'Quantity_LUMINANCE': (Quantity_PhysicalQuantity.Quantity_LUMINANCE, None), 'Quantity_ILLUMINANCE': (Quantity_PhysicalQuantity.Quantity_ILLUMINANCE, None), 'Quantity_LUMINOUSEXPOSITION': (Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION, None), 'Quantity_LUMINOUSEFFICACITY': (Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY, None), 'Quantity_ELECTRICCHARGE': (Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE, None), 'Quantity_ELECTRICCURRENT': (Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT, None), 'Quantity_ELECTRICFIELDSTRENGTH': (Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH, None), 'Quantity_ELECTRICPOTENTIAL': (Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL, None), 'Quantity_ELECTRICCAPACITANCE': (Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE, None), 'Quantity_MAGNETICFLUX': (Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX, None), 'Quantity_MAGNETICFLUXDENSITY': (Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY, None), 'Quantity_MAGNETICFIELDSTRENGTH': (Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH, None), 'Quantity_RELUCTANCE': (Quantity_PhysicalQuantity.Quantity_RELUCTANCE, None), 'Quantity_RESISTANCE': (Quantity_PhysicalQuantity.Quantity_RESISTANCE, None), 'Quantity_INDUCTANCE': (Quantity_PhysicalQuantity.Quantity_INDUCTANCE, None), 'Quantity_CAPACITANCE': (Quantity_PhysicalQuantity.Quantity_CAPACITANCE, None), 'Quantity_IMPEDANCE': (Quantity_PhysicalQuantity.Quantity_IMPEDANCE, None), 'Quantity_ADMITTANCE': (Quantity_PhysicalQuantity.Quantity_ADMITTANCE, None), 'Quantity_RESISTIVITY': (Quantity_PhysicalQuantity.Quantity_RESISTIVITY, None), 'Quantity_CONDUCTIVITY': (Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY, None), 'Quantity_MOLARMASS': (Quantity_PhysicalQuantity.Quantity_MOLARMASS, None), 'Quantity_MOLARVOLUME': (Quantity_PhysicalQuantity.Quantity_MOLARVOLUME, None), 'Quantity_CONCENTRATION': (Quantity_PhysicalQuantity.Quantity_CONCENTRATION, None), 'Quantity_MOLARCONCENTRATION': (Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION, None), 'Quantity_MOLARITY': (Quantity_PhysicalQuantity.Quantity_MOLARITY, None), 'Quantity_SOUNDINTENSITY': (Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY, None), 'Quantity_ACOUSTICINTENSITY': (Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY, None), 'Quantity_ACTIVITY': (Quantity_PhysicalQuantity.Quantity_ACTIVITY, None), 'Quantity_ABSORBEDDOSE': (Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE, None), 'Quantity_DOSEEQUIVALENT': (Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT, None)}
    __members__: dict # value = {'Quantity_MASS': Quantity_PhysicalQuantity.Quantity_MASS, 'Quantity_PLANEANGLE': Quantity_PhysicalQuantity.Quantity_PLANEANGLE, 'Quantity_SOLIDANGLE': Quantity_PhysicalQuantity.Quantity_SOLIDANGLE, 'Quantity_LENGTH': Quantity_PhysicalQuantity.Quantity_LENGTH, 'Quantity_AREA': Quantity_PhysicalQuantity.Quantity_AREA, 'Quantity_VOLUME': Quantity_PhysicalQuantity.Quantity_VOLUME, 'Quantity_SPEED': Quantity_PhysicalQuantity.Quantity_SPEED, 'Quantity_VELOCITY': Quantity_PhysicalQuantity.Quantity_VELOCITY, 'Quantity_ACCELERATION': Quantity_PhysicalQuantity.Quantity_ACCELERATION, 'Quantity_ANGULARVELOCITY': Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY, 'Quantity_FREQUENCY': Quantity_PhysicalQuantity.Quantity_FREQUENCY, 'Quantity_TEMPERATURE': Quantity_PhysicalQuantity.Quantity_TEMPERATURE, 'Quantity_AMOUNTOFSUBSTANCE': Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE, 'Quantity_DENSITY': Quantity_PhysicalQuantity.Quantity_DENSITY, 'Quantity_MASSFLOW': Quantity_PhysicalQuantity.Quantity_MASSFLOW, 'Quantity_VOLUMEFLOW': Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW, 'Quantity_CONSUMPTION': Quantity_PhysicalQuantity.Quantity_CONSUMPTION, 'Quantity_MOMENTUM': Quantity_PhysicalQuantity.Quantity_MOMENTUM, 'Quantity_KINETICMOMENT': Quantity_PhysicalQuantity.Quantity_KINETICMOMENT, 'Quantity_MOMENTOFINERTIA': Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA, 'Quantity_FORCE': Quantity_PhysicalQuantity.Quantity_FORCE, 'Quantity_MOMENTOFAFORCE': Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE, 'Quantity_TORQUE': Quantity_PhysicalQuantity.Quantity_TORQUE, 'Quantity_WEIGHT': Quantity_PhysicalQuantity.Quantity_WEIGHT, 'Quantity_PRESSURE': Quantity_PhysicalQuantity.Quantity_PRESSURE, 'Quantity_VISCOSITY': Quantity_PhysicalQuantity.Quantity_VISCOSITY, 'Quantity_KINEMATICVISCOSITY': Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY, 'Quantity_ENERGY': Quantity_PhysicalQuantity.Quantity_ENERGY, 'Quantity_WORK': Quantity_PhysicalQuantity.Quantity_WORK, 'Quantity_POWER': Quantity_PhysicalQuantity.Quantity_POWER, 'Quantity_SURFACETENSION': Quantity_PhysicalQuantity.Quantity_SURFACETENSION, 'Quantity_COEFFICIENTOFEXPANSION': Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION, 'Quantity_THERMALCONDUCTIVITY': Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY, 'Quantity_SPECIFICHEATCAPACITY': Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY, 'Quantity_ENTROPY': Quantity_PhysicalQuantity.Quantity_ENTROPY, 'Quantity_ENTHALPY': Quantity_PhysicalQuantity.Quantity_ENTHALPY, 'Quantity_LUMINOUSINTENSITY': Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY, 'Quantity_LUMINOUSFLUX': Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX, 'Quantity_LUMINANCE': Quantity_PhysicalQuantity.Quantity_LUMINANCE, 'Quantity_ILLUMINANCE': Quantity_PhysicalQuantity.Quantity_ILLUMINANCE, 'Quantity_LUMINOUSEXPOSITION': Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION, 'Quantity_LUMINOUSEFFICACITY': Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY, 'Quantity_ELECTRICCHARGE': Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE, 'Quantity_ELECTRICCURRENT': Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT, 'Quantity_ELECTRICFIELDSTRENGTH': Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH, 'Quantity_ELECTRICPOTENTIAL': Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL, 'Quantity_ELECTRICCAPACITANCE': Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE, 'Quantity_MAGNETICFLUX': Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX, 'Quantity_MAGNETICFLUXDENSITY': Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY, 'Quantity_MAGNETICFIELDSTRENGTH': Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH, 'Quantity_RELUCTANCE': Quantity_PhysicalQuantity.Quantity_RELUCTANCE, 'Quantity_RESISTANCE': Quantity_PhysicalQuantity.Quantity_RESISTANCE, 'Quantity_INDUCTANCE': Quantity_PhysicalQuantity.Quantity_INDUCTANCE, 'Quantity_CAPACITANCE': Quantity_PhysicalQuantity.Quantity_CAPACITANCE, 'Quantity_IMPEDANCE': Quantity_PhysicalQuantity.Quantity_IMPEDANCE, 'Quantity_ADMITTANCE': Quantity_PhysicalQuantity.Quantity_ADMITTANCE, 'Quantity_RESISTIVITY': Quantity_PhysicalQuantity.Quantity_RESISTIVITY, 'Quantity_CONDUCTIVITY': Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY, 'Quantity_MOLARMASS': Quantity_PhysicalQuantity.Quantity_MOLARMASS, 'Quantity_MOLARVOLUME': Quantity_PhysicalQuantity.Quantity_MOLARVOLUME, 'Quantity_CONCENTRATION': Quantity_PhysicalQuantity.Quantity_CONCENTRATION, 'Quantity_MOLARCONCENTRATION': Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION, 'Quantity_MOLARITY': Quantity_PhysicalQuantity.Quantity_MOLARITY, 'Quantity_SOUNDINTENSITY': Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY, 'Quantity_ACOUSTICINTENSITY': Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY, 'Quantity_ACTIVITY': Quantity_PhysicalQuantity.Quantity_ACTIVITY, 'Quantity_ABSORBEDDOSE': Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE, 'Quantity_DOSEEQUIVALENT': Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT}
    pass
class Quantity_TypeOfColor():
    """
    Identifies color definition systems - Quantity_TOC_RGB: with this system a color is defined by its quantities of red, green and blue (R-G-B values). - Quantity_TOC_HLS: with this system a color is defined by its hue angle and its lightness and saturation values (H-L-S values). A Quantity_Color object may define a color from three values R-G-B or H-L-S according to a given color definition system.

    Members:

      Quantity_TOC_RGB

      Quantity_TOC_HLS
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    Quantity_TOC_HLS: OCP.Quantity.Quantity_TypeOfColor # value = Quantity_TypeOfColor.Quantity_TOC_HLS
    Quantity_TOC_RGB: OCP.Quantity.Quantity_TypeOfColor # value = Quantity_TypeOfColor.Quantity_TOC_RGB
    __entries: dict # value = {'Quantity_TOC_RGB': (Quantity_TypeOfColor.Quantity_TOC_RGB, None), 'Quantity_TOC_HLS': (Quantity_TypeOfColor.Quantity_TOC_HLS, None)}
    __members__: dict # value = {'Quantity_TOC_RGB': Quantity_TypeOfColor.Quantity_TOC_RGB, 'Quantity_TOC_HLS': Quantity_TypeOfColor.Quantity_TOC_HLS}
    pass
Quantity_ABSORBEDDOSE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ABSORBEDDOSE
Quantity_ACCELERATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACCELERATION
Quantity_ACOUSTICINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACOUSTICINTENSITY
Quantity_ACTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ACTIVITY
Quantity_ADMITTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ADMITTANCE
Quantity_AMOUNTOFSUBSTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_AMOUNTOFSUBSTANCE
Quantity_ANGULARVELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ANGULARVELOCITY
Quantity_AREA: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_AREA
Quantity_CAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CAPACITANCE
Quantity_COEFFICIENTOFEXPANSION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_COEFFICIENTOFEXPANSION
Quantity_CONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONCENTRATION
Quantity_CONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONDUCTIVITY
Quantity_CONSUMPTION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_CONSUMPTION
Quantity_DENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_DENSITY
Quantity_DOSEEQUIVALENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_DOSEEQUIVALENT
Quantity_ELECTRICCAPACITANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCAPACITANCE
Quantity_ELECTRICCHARGE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCHARGE
Quantity_ELECTRICCURRENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICCURRENT
Quantity_ELECTRICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICFIELDSTRENGTH
Quantity_ELECTRICPOTENTIAL: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ELECTRICPOTENTIAL
Quantity_ENERGY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENERGY
Quantity_ENTHALPY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENTHALPY
Quantity_ENTROPY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ENTROPY
Quantity_FORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_FORCE
Quantity_FREQUENCY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_FREQUENCY
Quantity_ILLUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_ILLUMINANCE
Quantity_IMPEDANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_IMPEDANCE
Quantity_INDUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_INDUCTANCE
Quantity_KINEMATICVISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_KINEMATICVISCOSITY
Quantity_KINETICMOMENT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_KINETICMOMENT
Quantity_LENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LENGTH
Quantity_LUMINANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINANCE
Quantity_LUMINOUSEFFICACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSEFFICACITY
Quantity_LUMINOUSEXPOSITION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSEXPOSITION
Quantity_LUMINOUSFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSFLUX
Quantity_LUMINOUSINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_LUMINOUSINTENSITY
Quantity_MAGNETICFIELDSTRENGTH: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFIELDSTRENGTH
Quantity_MAGNETICFLUX: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFLUX
Quantity_MAGNETICFLUXDENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MAGNETICFLUXDENSITY
Quantity_MASS: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MASS
Quantity_MASSFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MASSFLOW
Quantity_MOLARCONCENTRATION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARCONCENTRATION
Quantity_MOLARITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARITY
Quantity_MOLARMASS: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARMASS
Quantity_MOLARVOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOLARVOLUME
Quantity_MOMENTOFAFORCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTOFAFORCE
Quantity_MOMENTOFINERTIA: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTOFINERTIA
Quantity_MOMENTUM: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_MOMENTUM
Quantity_NOC_ALICEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ALICEBLUE
Quantity_NOC_ANTIQUEWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE
Quantity_NOC_ANTIQUEWHITE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE1
Quantity_NOC_ANTIQUEWHITE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE2
Quantity_NOC_ANTIQUEWHITE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE3
Quantity_NOC_ANTIQUEWHITE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ANTIQUEWHITE4
Quantity_NOC_AQUAMARINE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE1
Quantity_NOC_AQUAMARINE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE2
Quantity_NOC_AQUAMARINE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AQUAMARINE4
Quantity_NOC_AZURE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE
Quantity_NOC_AZURE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE2
Quantity_NOC_AZURE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE3
Quantity_NOC_AZURE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_AZURE4
Quantity_NOC_BEET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BEET
Quantity_NOC_BEIGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BEIGE
Quantity_NOC_BISQUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE
Quantity_NOC_BISQUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE2
Quantity_NOC_BISQUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE3
Quantity_NOC_BISQUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BISQUE4
Quantity_NOC_BLACK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLACK
Quantity_NOC_BLANCHEDALMOND: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLANCHEDALMOND
Quantity_NOC_BLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE1
Quantity_NOC_BLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE2
Quantity_NOC_BLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE3
Quantity_NOC_BLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUE4
Quantity_NOC_BLUEVIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BLUEVIOLET
Quantity_NOC_BROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN
Quantity_NOC_BROWN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN1
Quantity_NOC_BROWN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN2
Quantity_NOC_BROWN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN3
Quantity_NOC_BROWN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BROWN4
Quantity_NOC_BURLYWOOD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD
Quantity_NOC_BURLYWOOD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD1
Quantity_NOC_BURLYWOOD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD2
Quantity_NOC_BURLYWOOD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD3
Quantity_NOC_BURLYWOOD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_BURLYWOOD4
Quantity_NOC_CADETBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE
Quantity_NOC_CADETBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE1
Quantity_NOC_CADETBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE2
Quantity_NOC_CADETBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE3
Quantity_NOC_CADETBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CADETBLUE4
Quantity_NOC_CHARTREUSE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE
Quantity_NOC_CHARTREUSE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE1
Quantity_NOC_CHARTREUSE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE2
Quantity_NOC_CHARTREUSE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE3
Quantity_NOC_CHARTREUSE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHARTREUSE4
Quantity_NOC_CHOCOLATE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE
Quantity_NOC_CHOCOLATE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE1
Quantity_NOC_CHOCOLATE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE2
Quantity_NOC_CHOCOLATE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE3
Quantity_NOC_CHOCOLATE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CHOCOLATE4
Quantity_NOC_CORAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL
Quantity_NOC_CORAL1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL1
Quantity_NOC_CORAL2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL2
Quantity_NOC_CORAL3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL3
Quantity_NOC_CORAL4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORAL4
Quantity_NOC_CORNFLOWERBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNFLOWERBLUE
Quantity_NOC_CORNSILK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK1
Quantity_NOC_CORNSILK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK2
Quantity_NOC_CORNSILK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK3
Quantity_NOC_CORNSILK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CORNSILK4
Quantity_NOC_CYAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN1
Quantity_NOC_CYAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN2
Quantity_NOC_CYAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN3
Quantity_NOC_CYAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_CYAN4
Quantity_NOC_DARKGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD
Quantity_NOC_DARKGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD1
Quantity_NOC_DARKGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD2
Quantity_NOC_DARKGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD3
Quantity_NOC_DARKGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGOLDENROD4
Quantity_NOC_DARKGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKGREEN
Quantity_NOC_DARKKHAKI: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKKHAKI
Quantity_NOC_DARKOLIVEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN
Quantity_NOC_DARKOLIVEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN1
Quantity_NOC_DARKOLIVEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN2
Quantity_NOC_DARKOLIVEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN3
Quantity_NOC_DARKOLIVEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKOLIVEGREEN4
Quantity_NOC_DARKORANGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE
Quantity_NOC_DARKORANGE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE1
Quantity_NOC_DARKORANGE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE2
Quantity_NOC_DARKORANGE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE3
Quantity_NOC_DARKORANGE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORANGE4
Quantity_NOC_DARKORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID
Quantity_NOC_DARKORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID1
Quantity_NOC_DARKORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID2
Quantity_NOC_DARKORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID3
Quantity_NOC_DARKORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKORCHID4
Quantity_NOC_DARKSALMON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSALMON
Quantity_NOC_DARKSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN
Quantity_NOC_DARKSEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN1
Quantity_NOC_DARKSEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN2
Quantity_NOC_DARKSEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN3
Quantity_NOC_DARKSEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSEAGREEN4
Quantity_NOC_DARKSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEBLUE
Quantity_NOC_DARKSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY
Quantity_NOC_DARKSLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY1
Quantity_NOC_DARKSLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY2
Quantity_NOC_DARKSLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY3
Quantity_NOC_DARKSLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKSLATEGRAY4
Quantity_NOC_DARKTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKTURQUOISE
Quantity_NOC_DARKVIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DARKVIOLET
Quantity_NOC_DEEPPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK
Quantity_NOC_DEEPPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK2
Quantity_NOC_DEEPPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK3
Quantity_NOC_DEEPPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPPINK4
Quantity_NOC_DEEPSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE1
Quantity_NOC_DEEPSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE2
Quantity_NOC_DEEPSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE3
Quantity_NOC_DEEPSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DEEPSKYBLUE4
Quantity_NOC_DODGERBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE1
Quantity_NOC_DODGERBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE2
Quantity_NOC_DODGERBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE3
Quantity_NOC_DODGERBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_DODGERBLUE4
Quantity_NOC_FIREBRICK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK
Quantity_NOC_FIREBRICK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK1
Quantity_NOC_FIREBRICK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK2
Quantity_NOC_FIREBRICK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK3
Quantity_NOC_FIREBRICK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FIREBRICK4
Quantity_NOC_FLORALWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FLORALWHITE
Quantity_NOC_FORESTGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_FORESTGREEN
Quantity_NOC_GAINSBORO: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GAINSBORO
Quantity_NOC_GHOSTWHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GHOSTWHITE
Quantity_NOC_GOLD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD
Quantity_NOC_GOLD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD1
Quantity_NOC_GOLD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD2
Quantity_NOC_GOLD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD3
Quantity_NOC_GOLD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLD4
Quantity_NOC_GOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD
Quantity_NOC_GOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD1
Quantity_NOC_GOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD2
Quantity_NOC_GOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD3
Quantity_NOC_GOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GOLDENROD4
Quantity_NOC_GRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY
Quantity_NOC_GRAY0: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY0
Quantity_NOC_GRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY1
Quantity_NOC_GRAY10: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY10
Quantity_NOC_GRAY11: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY11
Quantity_NOC_GRAY12: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY12
Quantity_NOC_GRAY13: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY13
Quantity_NOC_GRAY14: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY14
Quantity_NOC_GRAY15: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY15
Quantity_NOC_GRAY16: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY16
Quantity_NOC_GRAY17: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY17
Quantity_NOC_GRAY18: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY18
Quantity_NOC_GRAY19: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY19
Quantity_NOC_GRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY2
Quantity_NOC_GRAY20: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY20
Quantity_NOC_GRAY21: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY21
Quantity_NOC_GRAY22: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY22
Quantity_NOC_GRAY23: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY23
Quantity_NOC_GRAY24: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY24
Quantity_NOC_GRAY25: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY25
Quantity_NOC_GRAY26: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY26
Quantity_NOC_GRAY27: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY27
Quantity_NOC_GRAY28: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY28
Quantity_NOC_GRAY29: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY29
Quantity_NOC_GRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY3
Quantity_NOC_GRAY30: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY30
Quantity_NOC_GRAY31: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY31
Quantity_NOC_GRAY32: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY32
Quantity_NOC_GRAY33: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY33
Quantity_NOC_GRAY34: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY34
Quantity_NOC_GRAY35: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY35
Quantity_NOC_GRAY36: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY36
Quantity_NOC_GRAY37: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY37
Quantity_NOC_GRAY38: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY38
Quantity_NOC_GRAY39: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY39
Quantity_NOC_GRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY4
Quantity_NOC_GRAY40: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY40
Quantity_NOC_GRAY41: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY41
Quantity_NOC_GRAY42: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY42
Quantity_NOC_GRAY43: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY43
Quantity_NOC_GRAY44: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY44
Quantity_NOC_GRAY45: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY45
Quantity_NOC_GRAY46: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY46
Quantity_NOC_GRAY47: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY47
Quantity_NOC_GRAY48: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY48
Quantity_NOC_GRAY49: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY49
Quantity_NOC_GRAY5: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY5
Quantity_NOC_GRAY50: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY50
Quantity_NOC_GRAY51: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY51
Quantity_NOC_GRAY52: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY52
Quantity_NOC_GRAY53: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY53
Quantity_NOC_GRAY54: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY54
Quantity_NOC_GRAY55: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY55
Quantity_NOC_GRAY56: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY56
Quantity_NOC_GRAY57: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY57
Quantity_NOC_GRAY58: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY58
Quantity_NOC_GRAY59: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY59
Quantity_NOC_GRAY6: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY6
Quantity_NOC_GRAY60: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY60
Quantity_NOC_GRAY61: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY61
Quantity_NOC_GRAY62: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY62
Quantity_NOC_GRAY63: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY63
Quantity_NOC_GRAY64: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY64
Quantity_NOC_GRAY65: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY65
Quantity_NOC_GRAY66: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY66
Quantity_NOC_GRAY67: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY67
Quantity_NOC_GRAY68: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY68
Quantity_NOC_GRAY69: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY69
Quantity_NOC_GRAY7: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY7
Quantity_NOC_GRAY70: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY70
Quantity_NOC_GRAY71: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY71
Quantity_NOC_GRAY72: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY72
Quantity_NOC_GRAY73: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY73
Quantity_NOC_GRAY74: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY74
Quantity_NOC_GRAY75: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY75
Quantity_NOC_GRAY76: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY76
Quantity_NOC_GRAY77: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY77
Quantity_NOC_GRAY78: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY78
Quantity_NOC_GRAY79: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY79
Quantity_NOC_GRAY8: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY8
Quantity_NOC_GRAY80: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY80
Quantity_NOC_GRAY81: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY81
Quantity_NOC_GRAY82: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY82
Quantity_NOC_GRAY83: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY83
Quantity_NOC_GRAY85: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY85
Quantity_NOC_GRAY86: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY86
Quantity_NOC_GRAY87: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY87
Quantity_NOC_GRAY88: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY88
Quantity_NOC_GRAY89: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY89
Quantity_NOC_GRAY9: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY9
Quantity_NOC_GRAY90: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY90
Quantity_NOC_GRAY91: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY91
Quantity_NOC_GRAY92: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY92
Quantity_NOC_GRAY93: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY93
Quantity_NOC_GRAY94: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY94
Quantity_NOC_GRAY95: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY95
Quantity_NOC_GRAY97: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY97
Quantity_NOC_GRAY98: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY98
Quantity_NOC_GRAY99: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GRAY99
Quantity_NOC_GREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN
Quantity_NOC_GREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN1
Quantity_NOC_GREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN2
Quantity_NOC_GREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN3
Quantity_NOC_GREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREEN4
Quantity_NOC_GREENYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_GREENYELLOW
Quantity_NOC_HONEYDEW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW
Quantity_NOC_HONEYDEW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW2
Quantity_NOC_HONEYDEW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW3
Quantity_NOC_HONEYDEW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HONEYDEW4
Quantity_NOC_HOTPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK
Quantity_NOC_HOTPINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK1
Quantity_NOC_HOTPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK2
Quantity_NOC_HOTPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK3
Quantity_NOC_HOTPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_HOTPINK4
Quantity_NOC_INDIANRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED
Quantity_NOC_INDIANRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED1
Quantity_NOC_INDIANRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED2
Quantity_NOC_INDIANRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED3
Quantity_NOC_INDIANRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_INDIANRED4
Quantity_NOC_IVORY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY
Quantity_NOC_IVORY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY2
Quantity_NOC_IVORY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY3
Quantity_NOC_IVORY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_IVORY4
Quantity_NOC_KHAKI: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI
Quantity_NOC_KHAKI1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI1
Quantity_NOC_KHAKI2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI2
Quantity_NOC_KHAKI3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI3
Quantity_NOC_KHAKI4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_KHAKI4
Quantity_NOC_LAVENDER: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDER
Quantity_NOC_LAVENDERBLUSH1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH1
Quantity_NOC_LAVENDERBLUSH2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH2
Quantity_NOC_LAVENDERBLUSH3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH3
Quantity_NOC_LAVENDERBLUSH4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAVENDERBLUSH4
Quantity_NOC_LAWNGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LAWNGREEN
Quantity_NOC_LEMONCHIFFON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON1
Quantity_NOC_LEMONCHIFFON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON2
Quantity_NOC_LEMONCHIFFON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON3
Quantity_NOC_LEMONCHIFFON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LEMONCHIFFON4
Quantity_NOC_LIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE
Quantity_NOC_LIGHTBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE1
Quantity_NOC_LIGHTBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE2
Quantity_NOC_LIGHTBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE3
Quantity_NOC_LIGHTBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTBLUE4
Quantity_NOC_LIGHTCORAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCORAL
Quantity_NOC_LIGHTCYAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN1
Quantity_NOC_LIGHTCYAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN2
Quantity_NOC_LIGHTCYAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN3
Quantity_NOC_LIGHTCYAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTCYAN4
Quantity_NOC_LIGHTGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD
Quantity_NOC_LIGHTGOLDENROD1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD1
Quantity_NOC_LIGHTGOLDENROD2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD2
Quantity_NOC_LIGHTGOLDENROD3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD3
Quantity_NOC_LIGHTGOLDENROD4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENROD4
Quantity_NOC_LIGHTGOLDENRODYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGOLDENRODYELLOW
Quantity_NOC_LIGHTGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTGRAY
Quantity_NOC_LIGHTPINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK
Quantity_NOC_LIGHTPINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK1
Quantity_NOC_LIGHTPINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK2
Quantity_NOC_LIGHTPINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK3
Quantity_NOC_LIGHTPINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTPINK4
Quantity_NOC_LIGHTSALMON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON1
Quantity_NOC_LIGHTSALMON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON2
Quantity_NOC_LIGHTSALMON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON3
Quantity_NOC_LIGHTSALMON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSALMON4
Quantity_NOC_LIGHTSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSEAGREEN
Quantity_NOC_LIGHTSKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE
Quantity_NOC_LIGHTSKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE1
Quantity_NOC_LIGHTSKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE2
Quantity_NOC_LIGHTSKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE3
Quantity_NOC_LIGHTSKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSKYBLUE4
Quantity_NOC_LIGHTSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEBLUE
Quantity_NOC_LIGHTSLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSLATEGRAY
Quantity_NOC_LIGHTSTEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE
Quantity_NOC_LIGHTSTEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE1
Quantity_NOC_LIGHTSTEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE2
Quantity_NOC_LIGHTSTEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE3
Quantity_NOC_LIGHTSTEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTSTEELBLUE4
Quantity_NOC_LIGHTYELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW
Quantity_NOC_LIGHTYELLOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW2
Quantity_NOC_LIGHTYELLOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW3
Quantity_NOC_LIGHTYELLOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIGHTYELLOW4
Quantity_NOC_LIMEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LIMEGREEN
Quantity_NOC_LINEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_LINEN
Quantity_NOC_MAGENTA1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA1
Quantity_NOC_MAGENTA2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA2
Quantity_NOC_MAGENTA3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA3
Quantity_NOC_MAGENTA4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAGENTA4
Quantity_NOC_MAROON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON
Quantity_NOC_MAROON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON1
Quantity_NOC_MAROON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON2
Quantity_NOC_MAROON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON3
Quantity_NOC_MAROON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MAROON4
Quantity_NOC_MATRABLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MATRABLUE
Quantity_NOC_MATRAGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MATRAGRAY
Quantity_NOC_MEDIUMAQUAMARINE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMAQUAMARINE
Quantity_NOC_MEDIUMORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID
Quantity_NOC_MEDIUMORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID1
Quantity_NOC_MEDIUMORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID2
Quantity_NOC_MEDIUMORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID3
Quantity_NOC_MEDIUMORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMORCHID4
Quantity_NOC_MEDIUMPURPLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE
Quantity_NOC_MEDIUMPURPLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE1
Quantity_NOC_MEDIUMPURPLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE2
Quantity_NOC_MEDIUMPURPLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE3
Quantity_NOC_MEDIUMPURPLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMPURPLE4
Quantity_NOC_MEDIUMSEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSEAGREEN
Quantity_NOC_MEDIUMSLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSLATEBLUE
Quantity_NOC_MEDIUMSPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMSPRINGGREEN
Quantity_NOC_MEDIUMTURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMTURQUOISE
Quantity_NOC_MEDIUMVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MEDIUMVIOLETRED
Quantity_NOC_MIDNIGHTBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MIDNIGHTBLUE
Quantity_NOC_MINTCREAM: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MINTCREAM
Quantity_NOC_MISTYROSE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE
Quantity_NOC_MISTYROSE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE2
Quantity_NOC_MISTYROSE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE3
Quantity_NOC_MISTYROSE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MISTYROSE4
Quantity_NOC_MOCCASIN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_MOCCASIN
Quantity_NOC_NAVAJOWHITE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE1
Quantity_NOC_NAVAJOWHITE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE2
Quantity_NOC_NAVAJOWHITE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE3
Quantity_NOC_NAVAJOWHITE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVAJOWHITE4
Quantity_NOC_NAVYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_NAVYBLUE
Quantity_NOC_OLDLACE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLDLACE
Quantity_NOC_OLIVEDRAB: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB
Quantity_NOC_OLIVEDRAB1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB1
Quantity_NOC_OLIVEDRAB2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB2
Quantity_NOC_OLIVEDRAB3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB3
Quantity_NOC_OLIVEDRAB4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_OLIVEDRAB4
Quantity_NOC_ORANGE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE
Quantity_NOC_ORANGE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE1
Quantity_NOC_ORANGE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE2
Quantity_NOC_ORANGE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE3
Quantity_NOC_ORANGE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGE4
Quantity_NOC_ORANGERED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED
Quantity_NOC_ORANGERED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED1
Quantity_NOC_ORANGERED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED2
Quantity_NOC_ORANGERED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED3
Quantity_NOC_ORANGERED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORANGERED4
Quantity_NOC_ORCHID: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID
Quantity_NOC_ORCHID1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID1
Quantity_NOC_ORCHID2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID2
Quantity_NOC_ORCHID3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID3
Quantity_NOC_ORCHID4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ORCHID4
Quantity_NOC_PALEGOLDENROD: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGOLDENROD
Quantity_NOC_PALEGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN
Quantity_NOC_PALEGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN1
Quantity_NOC_PALEGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN2
Quantity_NOC_PALEGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN3
Quantity_NOC_PALEGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEGREEN4
Quantity_NOC_PALETURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE
Quantity_NOC_PALETURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE1
Quantity_NOC_PALETURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE2
Quantity_NOC_PALETURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE3
Quantity_NOC_PALETURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALETURQUOISE4
Quantity_NOC_PALEVIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED
Quantity_NOC_PALEVIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED1
Quantity_NOC_PALEVIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED2
Quantity_NOC_PALEVIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED3
Quantity_NOC_PALEVIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PALEVIOLETRED4
Quantity_NOC_PAPAYAWHIP: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PAPAYAWHIP
Quantity_NOC_PEACHPUFF: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF
Quantity_NOC_PEACHPUFF2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF2
Quantity_NOC_PEACHPUFF3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF3
Quantity_NOC_PEACHPUFF4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PEACHPUFF4
Quantity_NOC_PERU: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PERU
Quantity_NOC_PINK: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK
Quantity_NOC_PINK1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK1
Quantity_NOC_PINK2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK2
Quantity_NOC_PINK3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK3
Quantity_NOC_PINK4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PINK4
Quantity_NOC_PLUM: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM
Quantity_NOC_PLUM1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM1
Quantity_NOC_PLUM2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM2
Quantity_NOC_PLUM3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM3
Quantity_NOC_PLUM4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PLUM4
Quantity_NOC_POWDERBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_POWDERBLUE
Quantity_NOC_PURPLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE
Quantity_NOC_PURPLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE1
Quantity_NOC_PURPLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE2
Quantity_NOC_PURPLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE3
Quantity_NOC_PURPLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_PURPLE4
Quantity_NOC_RED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED
Quantity_NOC_RED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED1
Quantity_NOC_RED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED2
Quantity_NOC_RED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED3
Quantity_NOC_RED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_RED4
Quantity_NOC_ROSYBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN
Quantity_NOC_ROSYBROWN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN1
Quantity_NOC_ROSYBROWN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN2
Quantity_NOC_ROSYBROWN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN3
Quantity_NOC_ROSYBROWN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROSYBROWN4
Quantity_NOC_ROYALBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE
Quantity_NOC_ROYALBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE1
Quantity_NOC_ROYALBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE2
Quantity_NOC_ROYALBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE3
Quantity_NOC_ROYALBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_ROYALBLUE4
Quantity_NOC_SADDLEBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SADDLEBROWN
Quantity_NOC_SALMON: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON
Quantity_NOC_SALMON1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON1
Quantity_NOC_SALMON2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON2
Quantity_NOC_SALMON3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON3
Quantity_NOC_SALMON4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SALMON4
Quantity_NOC_SANDYBROWN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SANDYBROWN
Quantity_NOC_SEAGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN
Quantity_NOC_SEAGREEN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN1
Quantity_NOC_SEAGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN2
Quantity_NOC_SEAGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN3
Quantity_NOC_SEAGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEAGREEN4
Quantity_NOC_SEASHELL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL
Quantity_NOC_SEASHELL2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL2
Quantity_NOC_SEASHELL3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL3
Quantity_NOC_SEASHELL4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SEASHELL4
Quantity_NOC_SIENNA: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA
Quantity_NOC_SIENNA1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA1
Quantity_NOC_SIENNA2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA2
Quantity_NOC_SIENNA3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA3
Quantity_NOC_SIENNA4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SIENNA4
Quantity_NOC_SKYBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE
Quantity_NOC_SKYBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE1
Quantity_NOC_SKYBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE2
Quantity_NOC_SKYBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE3
Quantity_NOC_SKYBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SKYBLUE4
Quantity_NOC_SLATEBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE
Quantity_NOC_SLATEBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE1
Quantity_NOC_SLATEBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE2
Quantity_NOC_SLATEBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE3
Quantity_NOC_SLATEBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEBLUE4
Quantity_NOC_SLATEGRAY: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY
Quantity_NOC_SLATEGRAY1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY1
Quantity_NOC_SLATEGRAY2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY2
Quantity_NOC_SLATEGRAY3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY3
Quantity_NOC_SLATEGRAY4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SLATEGRAY4
Quantity_NOC_SNOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW
Quantity_NOC_SNOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW2
Quantity_NOC_SNOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW3
Quantity_NOC_SNOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SNOW4
Quantity_NOC_SPRINGGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN
Quantity_NOC_SPRINGGREEN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN2
Quantity_NOC_SPRINGGREEN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN3
Quantity_NOC_SPRINGGREEN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_SPRINGGREEN4
Quantity_NOC_STEELBLUE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE
Quantity_NOC_STEELBLUE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE1
Quantity_NOC_STEELBLUE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE2
Quantity_NOC_STEELBLUE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE3
Quantity_NOC_STEELBLUE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_STEELBLUE4
Quantity_NOC_TAN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN
Quantity_NOC_TAN1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN1
Quantity_NOC_TAN2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN2
Quantity_NOC_TAN3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN3
Quantity_NOC_TAN4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TAN4
Quantity_NOC_TEAL: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TEAL
Quantity_NOC_THISTLE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE
Quantity_NOC_THISTLE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE1
Quantity_NOC_THISTLE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE2
Quantity_NOC_THISTLE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE3
Quantity_NOC_THISTLE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_THISTLE4
Quantity_NOC_TOMATO: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO
Quantity_NOC_TOMATO1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO1
Quantity_NOC_TOMATO2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO2
Quantity_NOC_TOMATO3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO3
Quantity_NOC_TOMATO4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TOMATO4
Quantity_NOC_TURQUOISE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE
Quantity_NOC_TURQUOISE1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE1
Quantity_NOC_TURQUOISE2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE2
Quantity_NOC_TURQUOISE3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE3
Quantity_NOC_TURQUOISE4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_TURQUOISE4
Quantity_NOC_VIOLET: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLET
Quantity_NOC_VIOLETRED: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED
Quantity_NOC_VIOLETRED1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED1
Quantity_NOC_VIOLETRED2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED2
Quantity_NOC_VIOLETRED3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED3
Quantity_NOC_VIOLETRED4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_VIOLETRED4
Quantity_NOC_WHEAT: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT
Quantity_NOC_WHEAT1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT1
Quantity_NOC_WHEAT2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT2
Quantity_NOC_WHEAT3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT3
Quantity_NOC_WHEAT4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHEAT4
Quantity_NOC_WHITE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHITE
Quantity_NOC_WHITESMOKE: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_WHITESMOKE
Quantity_NOC_YELLOW: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW
Quantity_NOC_YELLOW1: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW1
Quantity_NOC_YELLOW2: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW2
Quantity_NOC_YELLOW3: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW3
Quantity_NOC_YELLOW4: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOW4
Quantity_NOC_YELLOWGREEN: OCP.Quantity.Quantity_NameOfColor # value = Quantity_NameOfColor.Quantity_NOC_YELLOWGREEN
Quantity_PLANEANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_PLANEANGLE
Quantity_POWER: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_POWER
Quantity_PRESSURE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_PRESSURE
Quantity_RELUCTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RELUCTANCE
Quantity_RESISTANCE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RESISTANCE
Quantity_RESISTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_RESISTIVITY
Quantity_SOLIDANGLE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SOLIDANGLE
Quantity_SOUNDINTENSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SOUNDINTENSITY
Quantity_SPECIFICHEATCAPACITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SPECIFICHEATCAPACITY
Quantity_SPEED: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SPEED
Quantity_SURFACETENSION: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_SURFACETENSION
Quantity_TEMPERATURE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_TEMPERATURE
Quantity_THERMALCONDUCTIVITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_THERMALCONDUCTIVITY
Quantity_TOC_HLS: OCP.Quantity.Quantity_TypeOfColor # value = Quantity_TypeOfColor.Quantity_TOC_HLS
Quantity_TOC_RGB: OCP.Quantity.Quantity_TypeOfColor # value = Quantity_TypeOfColor.Quantity_TOC_RGB
Quantity_TORQUE: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_TORQUE
Quantity_VELOCITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VELOCITY
Quantity_VISCOSITY: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VISCOSITY
Quantity_VOLUME: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VOLUME
Quantity_VOLUMEFLOW: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_VOLUMEFLOW
Quantity_WEIGHT: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_WEIGHT
Quantity_WORK: OCP.Quantity.Quantity_PhysicalQuantity # value = Quantity_PhysicalQuantity.Quantity_WORK
