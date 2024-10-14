# Any data models to be used in main notebooks.
# With utilities.

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

CUE_SPECS = [
    'material',
    'tip_size',
    'tip_hardness',
    'weight',
    'balance_point'
]
