# Generated from LA.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,70,566,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,
        1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,43,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,46,
        1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,51,1,52,
        1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,56,1,56,
        1,57,1,57,1,57,1,58,1,58,1,59,4,59,474,8,59,11,59,12,59,475,1,60,
        4,60,479,8,60,11,60,12,60,480,1,60,1,60,4,60,485,8,60,11,60,12,60,
        486,3,60,489,8,60,1,61,1,61,1,62,1,62,1,62,1,62,5,62,497,8,62,10,
        62,12,62,500,9,62,1,63,1,63,5,63,504,8,63,10,63,12,63,507,9,63,1,
        63,1,63,3,63,511,8,63,1,63,3,63,514,8,63,1,63,1,63,1,64,1,64,5,64,
        520,8,64,10,64,12,64,523,9,64,1,64,3,64,526,8,64,1,64,3,64,529,8,
        64,1,65,1,65,1,65,5,65,534,8,65,10,65,12,65,537,9,65,1,65,1,65,1,
        66,1,66,1,66,5,66,544,8,66,10,66,12,66,547,9,66,1,66,3,66,550,8,
        66,1,66,3,66,553,8,66,1,67,1,67,1,67,1,67,3,67,559,8,67,1,68,1,68,
        1,68,1,68,1,69,1,69,0,0,70,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,
        42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,
        105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,
        62,125,63,127,64,129,65,131,66,133,67,135,68,137,69,139,70,1,0,6,
        2,0,65,90,97,122,4,0,10,10,13,13,123,123,125,125,4,0,10,10,13,13,
        34,34,92,92,2,0,34,34,92,92,3,0,9,10,13,13,32,32,1,0,97,97,585,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,
        0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,
        0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,
        0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,
        1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,
        0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,
        0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,
        129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,
        0,0,0,139,1,0,0,0,1,141,1,0,0,0,3,151,1,0,0,0,5,165,1,0,0,0,7,173,
        1,0,0,0,9,183,1,0,0,0,11,185,1,0,0,0,13,187,1,0,0,0,15,192,1,0,0,
        0,17,194,1,0,0,0,19,196,1,0,0,0,21,198,1,0,0,0,23,200,1,0,0,0,25,
        208,1,0,0,0,27,216,1,0,0,0,29,221,1,0,0,0,31,228,1,0,0,0,33,230,
        1,0,0,0,35,241,1,0,0,0,37,247,1,0,0,0,39,256,1,0,0,0,41,269,1,0,
        0,0,43,282,1,0,0,0,45,284,1,0,0,0,47,286,1,0,0,0,49,303,1,0,0,0,
        51,310,1,0,0,0,53,321,1,0,0,0,55,325,1,0,0,0,57,330,1,0,0,0,59,338,
        1,0,0,0,61,341,1,0,0,0,63,347,1,0,0,0,65,354,1,0,0,0,67,360,1,0,
        0,0,69,365,1,0,0,0,71,370,1,0,0,0,73,379,1,0,0,0,75,384,1,0,0,0,
        77,387,1,0,0,0,79,391,1,0,0,0,81,396,1,0,0,0,83,405,1,0,0,0,85,414,
        1,0,0,0,87,427,1,0,0,0,89,435,1,0,0,0,91,438,1,0,0,0,93,440,1,0,
        0,0,95,442,1,0,0,0,97,444,1,0,0,0,99,446,1,0,0,0,101,448,1,0,0,0,
        103,450,1,0,0,0,105,453,1,0,0,0,107,456,1,0,0,0,109,459,1,0,0,0,
        111,461,1,0,0,0,113,463,1,0,0,0,115,467,1,0,0,0,117,470,1,0,0,0,
        119,473,1,0,0,0,121,478,1,0,0,0,123,490,1,0,0,0,125,492,1,0,0,0,
        127,501,1,0,0,0,129,517,1,0,0,0,131,530,1,0,0,0,133,540,1,0,0,0,
        135,558,1,0,0,0,137,560,1,0,0,0,139,564,1,0,0,0,141,142,5,97,0,0,
        142,143,5,108,0,0,143,144,5,103,0,0,144,145,5,111,0,0,145,146,5,
        114,0,0,146,147,5,105,0,0,147,148,5,116,0,0,148,149,5,109,0,0,149,
        150,5,111,0,0,150,2,1,0,0,0,151,152,5,102,0,0,152,153,5,105,0,0,
        153,154,5,109,0,0,154,155,5,95,0,0,155,156,5,97,0,0,156,157,5,108,
        0,0,157,158,5,103,0,0,158,159,5,111,0,0,159,160,5,114,0,0,160,161,
        5,105,0,0,161,162,5,116,0,0,162,163,5,109,0,0,163,164,5,111,0,0,
        164,4,1,0,0,0,165,166,5,100,0,0,166,167,5,101,0,0,167,168,5,99,0,
        0,168,169,5,108,0,0,169,170,5,97,0,0,170,171,5,114,0,0,171,172,5,
        101,0,0,172,6,1,0,0,0,173,174,5,99,0,0,174,175,5,111,0,0,175,176,
        5,110,0,0,176,177,5,115,0,0,177,178,5,116,0,0,178,179,5,97,0,0,179,
        180,5,110,0,0,180,181,5,116,0,0,181,182,5,101,0,0,182,8,1,0,0,0,
        183,184,5,58,0,0,184,10,1,0,0,0,185,186,5,61,0,0,186,12,1,0,0,0,
        187,188,5,116,0,0,188,189,5,105,0,0,189,190,5,112,0,0,190,191,5,
        111,0,0,191,14,1,0,0,0,192,193,5,44,0,0,193,16,1,0,0,0,194,195,5,
        46,0,0,195,18,1,0,0,0,196,197,5,91,0,0,197,20,1,0,0,0,198,199,5,
        93,0,0,199,22,1,0,0,0,200,201,5,108,0,0,201,202,5,105,0,0,202,203,
        5,116,0,0,203,204,5,101,0,0,204,205,5,114,0,0,205,206,5,97,0,0,206,
        207,5,108,0,0,207,24,1,0,0,0,208,209,5,105,0,0,209,210,5,110,0,0,
        210,211,5,116,0,0,211,212,5,101,0,0,212,213,5,105,0,0,213,214,5,
        114,0,0,214,215,5,111,0,0,215,26,1,0,0,0,216,217,5,114,0,0,217,218,
        5,101,0,0,218,219,5,97,0,0,219,220,5,108,0,0,220,28,1,0,0,0,221,
        222,5,108,0,0,222,223,5,111,0,0,223,224,5,103,0,0,224,225,5,105,
        0,0,225,226,5,99,0,0,226,227,5,111,0,0,227,30,1,0,0,0,228,229,5,
        94,0,0,229,32,1,0,0,0,230,231,5,118,0,0,231,232,5,101,0,0,232,233,
        5,114,0,0,233,234,5,100,0,0,234,235,5,97,0,0,235,236,5,100,0,0,236,
        237,5,101,0,0,237,238,5,105,0,0,238,239,5,114,0,0,239,240,5,111,
        0,0,240,34,1,0,0,0,241,242,5,102,0,0,242,243,5,97,0,0,243,244,5,
        108,0,0,244,245,5,115,0,0,245,246,5,111,0,0,246,36,1,0,0,0,247,248,
        5,114,0,0,248,249,5,101,0,0,249,250,5,103,0,0,250,251,5,105,0,0,
        251,252,5,115,0,0,252,253,5,116,0,0,253,254,5,114,0,0,254,255,5,
        111,0,0,255,38,1,0,0,0,256,257,5,102,0,0,257,258,5,105,0,0,258,259,
        5,109,0,0,259,260,5,95,0,0,260,261,5,114,0,0,261,262,5,101,0,0,262,
        263,5,103,0,0,263,264,5,105,0,0,264,265,5,115,0,0,265,266,5,116,
        0,0,266,267,5,114,0,0,267,268,5,111,0,0,268,40,1,0,0,0,269,270,5,
        112,0,0,270,271,5,114,0,0,271,272,5,111,0,0,272,273,5,99,0,0,273,
        274,5,101,0,0,274,275,5,100,0,0,275,276,5,105,0,0,276,277,5,109,
        0,0,277,278,5,101,0,0,278,279,5,110,0,0,279,280,5,116,0,0,280,281,
        5,111,0,0,281,42,1,0,0,0,282,283,5,40,0,0,283,44,1,0,0,0,284,285,
        5,41,0,0,285,46,1,0,0,0,286,287,5,102,0,0,287,288,5,105,0,0,288,
        289,5,109,0,0,289,290,5,95,0,0,290,291,5,112,0,0,291,292,5,114,0,
        0,292,293,5,111,0,0,293,294,5,99,0,0,294,295,5,101,0,0,295,296,5,
        100,0,0,296,297,5,105,0,0,297,298,5,109,0,0,298,299,5,101,0,0,299,
        300,5,110,0,0,300,301,5,116,0,0,301,302,5,111,0,0,302,48,1,0,0,0,
        303,304,5,102,0,0,304,305,5,117,0,0,305,306,5,110,0,0,306,307,5,
        99,0,0,307,308,5,97,0,0,308,309,5,111,0,0,309,50,1,0,0,0,310,311,
        5,102,0,0,311,312,5,105,0,0,312,313,5,109,0,0,313,314,5,95,0,0,314,
        315,5,102,0,0,315,316,5,117,0,0,316,317,5,110,0,0,317,318,5,99,0,
        0,318,319,5,97,0,0,319,320,5,111,0,0,320,52,1,0,0,0,321,322,5,118,
        0,0,322,323,5,97,0,0,323,324,5,114,0,0,324,54,1,0,0,0,325,326,5,
        108,0,0,326,327,5,101,0,0,327,328,5,105,0,0,328,329,5,97,0,0,329,
        56,1,0,0,0,330,331,5,101,0,0,331,332,5,115,0,0,332,333,5,99,0,0,
        333,334,5,114,0,0,334,335,5,101,0,0,335,336,5,118,0,0,336,337,5,
        97,0,0,337,58,1,0,0,0,338,339,5,115,0,0,339,340,5,101,0,0,340,60,
        1,0,0,0,341,342,5,101,0,0,342,343,5,110,0,0,343,344,5,116,0,0,344,
        345,5,97,0,0,345,346,5,111,0,0,346,62,1,0,0,0,347,348,5,102,0,0,
        348,349,5,105,0,0,349,350,5,109,0,0,350,351,5,95,0,0,351,352,5,115,
        0,0,352,353,5,101,0,0,353,64,1,0,0,0,354,355,5,115,0,0,355,356,5,
        101,0,0,356,357,5,110,0,0,357,358,5,97,0,0,358,359,5,111,0,0,359,
        66,1,0,0,0,360,361,5,99,0,0,361,362,5,97,0,0,362,363,5,115,0,0,363,
        364,5,111,0,0,364,68,1,0,0,0,365,366,5,115,0,0,366,367,5,101,0,0,
        367,368,5,106,0,0,368,369,5,97,0,0,369,70,1,0,0,0,370,371,5,102,
        0,0,371,372,5,105,0,0,372,373,5,109,0,0,373,374,5,95,0,0,374,375,
        5,99,0,0,375,376,5,97,0,0,376,377,5,115,0,0,377,378,5,111,0,0,378,
        72,1,0,0,0,379,380,5,112,0,0,380,381,5,97,0,0,381,382,5,114,0,0,
        382,383,5,97,0,0,383,74,1,0,0,0,384,385,5,60,0,0,385,386,5,45,0,
        0,386,76,1,0,0,0,387,388,5,97,0,0,388,389,5,116,0,0,389,390,5,101,
        0,0,390,78,1,0,0,0,391,392,5,102,0,0,392,393,5,97,0,0,393,394,5,
        99,0,0,394,395,5,97,0,0,395,80,1,0,0,0,396,397,5,102,0,0,397,398,
        5,105,0,0,398,399,5,109,0,0,399,400,5,95,0,0,400,401,5,112,0,0,401,
        402,5,97,0,0,402,403,5,114,0,0,403,404,5,97,0,0,404,82,1,0,0,0,405,
        406,5,101,0,0,406,407,5,110,0,0,407,408,5,113,0,0,408,409,5,117,
        0,0,409,410,5,97,0,0,410,411,5,110,0,0,411,412,5,116,0,0,412,413,
        5,111,0,0,413,84,1,0,0,0,414,415,5,102,0,0,415,416,5,105,0,0,416,
        417,5,109,0,0,417,418,5,95,0,0,418,419,5,101,0,0,419,420,5,110,0,
        0,420,421,5,113,0,0,421,422,5,117,0,0,422,423,5,97,0,0,423,424,5,
        110,0,0,424,425,5,116,0,0,425,426,5,111,0,0,426,86,1,0,0,0,427,428,
        5,114,0,0,428,429,5,101,0,0,429,430,5,116,0,0,430,431,5,111,0,0,
        431,432,5,114,0,0,432,433,5,110,0,0,433,434,5,101,0,0,434,88,1,0,
        0,0,435,436,5,46,0,0,436,437,5,46,0,0,437,90,1,0,0,0,438,439,5,45,
        0,0,439,92,1,0,0,0,440,441,5,43,0,0,441,94,1,0,0,0,442,443,5,42,
        0,0,443,96,1,0,0,0,444,445,5,47,0,0,445,98,1,0,0,0,446,447,5,37,
        0,0,447,100,1,0,0,0,448,449,5,38,0,0,449,102,1,0,0,0,450,451,5,60,
        0,0,451,452,5,62,0,0,452,104,1,0,0,0,453,454,5,62,0,0,454,455,5,
        61,0,0,455,106,1,0,0,0,456,457,5,60,0,0,457,458,5,61,0,0,458,108,
        1,0,0,0,459,460,5,62,0,0,460,110,1,0,0,0,461,462,5,60,0,0,462,112,
        1,0,0,0,463,464,5,110,0,0,464,465,5,97,0,0,465,466,5,111,0,0,466,
        114,1,0,0,0,467,468,5,111,0,0,468,469,5,117,0,0,469,116,1,0,0,0,
        470,471,5,101,0,0,471,118,1,0,0,0,472,474,2,48,57,0,473,472,1,0,
        0,0,474,475,1,0,0,0,475,473,1,0,0,0,475,476,1,0,0,0,476,120,1,0,
        0,0,477,479,2,48,57,0,478,477,1,0,0,0,479,480,1,0,0,0,480,478,1,
        0,0,0,480,481,1,0,0,0,481,488,1,0,0,0,482,484,5,46,0,0,483,485,2,
        48,57,0,484,483,1,0,0,0,485,486,1,0,0,0,486,484,1,0,0,0,486,487,
        1,0,0,0,487,489,1,0,0,0,488,482,1,0,0,0,488,489,1,0,0,0,489,122,
        1,0,0,0,490,491,2,48,57,0,491,124,1,0,0,0,492,498,7,0,0,0,493,497,
        7,0,0,0,494,497,3,123,61,0,495,497,5,95,0,0,496,493,1,0,0,0,496,
        494,1,0,0,0,496,495,1,0,0,0,497,500,1,0,0,0,498,496,1,0,0,0,498,
        499,1,0,0,0,499,126,1,0,0,0,500,498,1,0,0,0,501,505,5,123,0,0,502,
        504,8,1,0,0,503,502,1,0,0,0,504,507,1,0,0,0,505,503,1,0,0,0,505,
        506,1,0,0,0,506,508,1,0,0,0,507,505,1,0,0,0,508,510,5,125,0,0,509,
        511,5,13,0,0,510,509,1,0,0,0,510,511,1,0,0,0,511,513,1,0,0,0,512,
        514,5,10,0,0,513,512,1,0,0,0,513,514,1,0,0,0,514,515,1,0,0,0,515,
        516,6,63,0,0,516,128,1,0,0,0,517,521,5,123,0,0,518,520,8,1,0,0,519,
        518,1,0,0,0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,
        525,1,0,0,0,523,521,1,0,0,0,524,526,5,13,0,0,525,524,1,0,0,0,525,
        526,1,0,0,0,526,528,1,0,0,0,527,529,5,10,0,0,528,527,1,0,0,0,528,
        529,1,0,0,0,529,130,1,0,0,0,530,535,5,34,0,0,531,534,3,135,67,0,
        532,534,8,2,0,0,533,531,1,0,0,0,533,532,1,0,0,0,534,537,1,0,0,0,
        535,533,1,0,0,0,535,536,1,0,0,0,536,538,1,0,0,0,537,535,1,0,0,0,
        538,539,5,34,0,0,539,132,1,0,0,0,540,545,5,34,0,0,541,544,3,135,
        67,0,542,544,8,3,0,0,543,541,1,0,0,0,543,542,1,0,0,0,544,547,1,0,
        0,0,545,543,1,0,0,0,545,546,1,0,0,0,546,549,1,0,0,0,547,545,1,0,
        0,0,548,550,5,13,0,0,549,548,1,0,0,0,549,550,1,0,0,0,550,552,1,0,
        0,0,551,553,5,10,0,0,552,551,1,0,0,0,552,553,1,0,0,0,553,134,1,0,
        0,0,554,555,5,92,0,0,555,559,5,39,0,0,556,557,5,92,0,0,557,559,5,
        110,0,0,558,554,1,0,0,0,558,556,1,0,0,0,559,136,1,0,0,0,560,561,
        7,4,0,0,561,562,1,0,0,0,562,563,6,68,0,0,563,138,1,0,0,0,564,565,
        8,5,0,0,565,140,1,0,0,0,20,0,475,480,486,488,496,498,505,510,513,
        521,525,528,533,535,543,545,549,552,558,1,6,0,0
    ]

class LALexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    NUM_INT = 60
    NUM_REAL = 61
    Digito = 62
    IDENT = 63
    Comentario = 64
    Nao_Fechado = 65
    CADEIA = 66
    Literal_Nao_Fechada = 67
    ESC_SEQ = 68
    WS = 69
    ERR = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'algoritmo'", "'fim_algoritmo'", "'declare'", "'constante'", 
            "':'", "'='", "'tipo'", "','", "'.'", "'['", "']'", "'literal'", 
            "'inteiro'", "'real'", "'logico'", "'^'", "'verdadeiro'", "'falso'", 
            "'registro'", "'fim_registro'", "'procedimento'", "'('", "')'", 
            "'fim_procedimento'", "'funcao'", "'fim_funcao'", "'var'", "'leia'", 
            "'escreva'", "'se'", "'entao'", "'fim_se'", "'senao'", "'caso'", 
            "'seja'", "'fim_caso'", "'para'", "'<-'", "'ate'", "'faca'", 
            "'fim_para'", "'enquanto'", "'fim_enquanto'", "'retorne'", "'..'", 
            "'-'", "'+'", "'*'", "'/'", "'%'", "'&'", "'<>'", "'>='", "'<='", 
            "'>'", "'<'", "'nao'", "'ou'", "'e'" ]

    symbolicNames = [ "<INVALID>",
            "NUM_INT", "NUM_REAL", "Digito", "IDENT", "Comentario", "Nao_Fechado", 
            "CADEIA", "Literal_Nao_Fechada", "ESC_SEQ", "WS", "ERR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "NUM_INT", "NUM_REAL", "Digito", 
                  "IDENT", "Comentario", "Nao_Fechado", "CADEIA", "Literal_Nao_Fechada", 
                  "ESC_SEQ", "WS", "ERR" ]

    grammarFileName = "LA.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


