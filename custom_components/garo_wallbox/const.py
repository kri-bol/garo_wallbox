
DOMAIN = "garo_wallbox"

KEY_MAC = "mac"
KEY_IP = "ip"

TIMEOUT = 60

LOCAL_METER_PATH = "EXTERNAL"
GROUP_METER_PATH = "CENTRAL100"
GROUP101_METER_PATH = "CENTRAL101"
VOLTAGE = 230
CURRENT_DIVIDER = 10

SERVICE_SET_MODE = "set_mode"
SERVICE_SET_CURRENT_LIMIT = "set_current_limit"

ATTR_MODES = "modes"

GARO_PRODUCT_MAP = {
    1: 'GLBMW-T137FC',
    2: 'GLBMW-T237FC',
    3: 'GLBMW-T237WO',
    4: 'GLBW-T174FC-B',
    5: 'GLBW-T274FC-B',
    6: 'GLBMW-T274WO',
    7: 'GLBW-T137FC',
    8: 'GLBW-T237FC',
    9: 'GLBW-T237WO',
    10: 'GLBW-T174FC',
    11: 'GLBW-T274FC',
    12: 'GLBM-T274WO',
    13: 'GLBW-T222FC',
    14: 'GLBW-T222FC-B',
    15: 'GLBW-T222WO',
    16: 'GLBW-T222WO-B',
    17: 'GLB-T137FC',
    18: 'GLB-T237FC',
    19: 'GLB-T237WO',
    20: 'GLB-T174FC',
    21: 'GLB-T274FC',
    22: 'GLBM-T274WO-B',
    23: 'GLB-T222FC',
    24: 'GLB-T222FC-B',
    25: 'GLB-T222WO',
    26: 'GLB-T222WO-B',
    27: 'GLBMW-T274WO-B',
    28: 'GLB-T174FC-B',
    29: 'GLB-T274FC-B',
    30: 'GLBM-T237WO',
    31: 'GLBM-T137FC',
    32: 'GLBM-T237FC',
    33: 'GLBMMFF-T237WO',
    34: 'GLBMMFF-T274WO-B',
    35: 'GLBMMFF-T274WO',
    36: 'GLBMN-T222WO-B',
    37: 'GLB-MN-T222WO',
    38: 'GLBMMN-T222WO',
    39: 'GLBMB-T237WO',
    40: 'GLBMFF-T237WO-B',
    41: 'GLBMMFF-T237WO-B',
    42: 'GHL-T274WOI',
    43: 'GLBP-T237WO',
    44: 'GLBP-T137FC',
    45: 'GLBP-T222WO-B',
    46: 'GLBP-T222WO',
    47: 'GLBP-T222FC-B',
    48: 'GLBP-T222FC',
    49: 'GLBPW-T237WO',
    50: 'GLBPW-T137FC',
    51: 'GLBPW-T222WO-B',
    52: 'GLBPW-T222WO',
    53: 'GLBPW-T222FC-B',
    54: 'GLBPW-T222FC',
    55: 'GLBPMN-T222WO',
    56: 'GLBPMMN-T222WO',
    57: 'GLBDC-T137FC-A',
    58: 'GLBDC-T237FC-A',
    59: 'GLBDC-T274WO-A',
    60: 'GLBDCM-T137FC-A',
    61: 'GLBDCM-T237FC-A',
    62: 'GLBDCM-T274WO-A',
    63: 'GLBDCM-T274FC-A',
    64: 'GLBDC-T222FC-A',
    65: 'GLBDCM-T222FC',
    66: 'GLBDC-T222WO-A',
    67: 'GLBDCM-T222WO',
    68: 'GLBDC-T174FC',
    69: 'GLBDCM-T274WO',
    70: 'GLBDC-T222WO',
    71: 'GLBDC-T222FC',
    72: 'GLBDCMB-T274WO-A',
    73: 'GLBDCM-T274WO-A-NO',
    74: 'GLBDC-T174FC-A',
    75: 'GLBDC-T274FC',
    76: 'GLBPDC-T222FC-A',
    77: 'GLBPDCM-T222FC',
    78: 'GLBPDC-T222WO-A',
    79: 'GLBPDCM-T222WO',
    80: 'GLBPDC-T222WO',
    81: 'GLBPDC-T222FC',
    82: 'GLBDCM-T274FC',
    83: 'GLBDCW-T237FC-A VO',
    84: 'GLBDCWM-T137FC-A',
    85: 'GLBDCWM-T237FC-A',
    86: 'GGLBDCWM-T274WO-A',
    87: 'GLBDCWM-T222FC',
    88: 'GLBDCWM-T222WO',
    89: 'GLBDCWM-T274FC-A',
    90: 'GLBDCW-T211FC',
    91: 'GLBDCW-T222FC',
    92: 'GTCDC-T274WO',
    93: 'GTCDCM-T274WO',
    94: 'GTBDCM-T222WO-A',
    95: 'GTBDCM-T211FC-A',
    96: 'GTBDCM-T211FC-A',
    97: 'GTBDCM-T274FC-A',
    98: 'GTBDCMB-T274WO-A',
    99: 'GTBDCMB-T222WO-A',
    100: 'GTBDC-T222WO-A',
    101: 'GTBDC-T274WO-A',
    102: 'GTBDC-T274FC-A',
    103: 'GTBDCMW-T274WO-A',
    104: 'GTBDCMW-T222WO-A',
    105: 'GTBDCMW-T274FC-A',
    106: 'GTBDCMW-T211FC-A',
    107: 'GLBDCM-T222WO',
    108: 'GLBDCM-T274WO-A',
    109: 'GLBDCM-T222FK',
    110: 'GLBDCM-T222WO',
    111: 'GLBDCM-T274FK-A',
    112: 'GLBDCWM-T222FC8',
    113: 'GLBDCW-T222WOF-VCC',
    114: 'GLBDC-T274WO PME',
    115: 'GLBDC-T274FC PME',
    116: 'GTBDCMW-T222FC-A',
    117: 'GTBDCMW-T211FCL-A',
    118: 'GTBDCW-T211FCL-A',
    119: 'GLBDCMW-T211FC-VCC',
    120: 'GLBDCMW-T222FC-VCC',
    121: 'GLBDCW-T222FC-A-VCC',
    220: 'CLS1-DCM-W-T223WO-A',
    221: 'CLS1-DCM-W-T237WO-A',
}