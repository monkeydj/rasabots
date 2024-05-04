# Any data models to be used in main notebook.
# Also some small utilities.

MOVEMENT_HIST = [
    'ts',
    'color',
    'x', 'y', 'z',  # point at time
    'dir_x', 'dir_y', 'dir_z',  # vector direction end
    'v_x', 'v_y', 'v_z',  # velocity vector
    'sp_x', 'sp_y', 'sp_z'  # spinning vector
]

CUE_SPECS = [
    'material',
    'tip_size',
    'weight',
    'balance_point'
]
