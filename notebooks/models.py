"""
Any data models to be used in main notebooks.
With utilities.
"""

from numpy import linspace, int16

# NOTE: just in case for later analyses
BALL_WGT_MIN, BALL_WGT_MAX = 205, 220  # in grams

CUE_SPECS = [
    'material',
    'tip_size',
    'tip_hardness',
    'weight',
    'balance_point'
]

CUE_WGT_MIN, CUE_WGT_MAX = 420, 550  # in grams
CUE_WGT_RANGE = linspace(
    CUE_WGT_MIN, CUE_WGT_MAX,
    num=(CUE_WGT_MAX - CUE_WGT_MIN)//10,
    dtype=int16,
)

BRDG_LEN_MIN, BRDG_LEN_MAX = 1, 25  # in cm

VEL_MIN, VEL_MAX = 0.05, 3.5  # m/s, from caromball.com
VEL_RANGE = linspace(
    VEL_MIN, VEL_MAX, num=50,
)

MOVEMENT_HIST = [
    'ts',
    'ball_color',
    # this coordination will be relative to table
    'x', 'y', 'z',  # point at time
    # these vectors are centered at ball centre
    'dir_x', 'dir_y', 'dir_z',  # vector direction end
    'v_x', 'v_y', 'v_z',  # velocity vector
    'sp_x', 'sp_y', 'sp_z'  # spinning vector
]
