# App
SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 950

# Visualiser
FPS = 60
VIS_NODE_WIDTH = 100   # must be divisible by VIS_WINDOW_SIZE otherwise black bar
VIS_WINDOW_SIZE = 800
NODE_COUNT = VIS_NODE_WIDTH * VIS_NODE_WIDTH
NODE_SIZE = VIS_WINDOW_SIZE // VIS_NODE_WIDTH

# Graphics
ANIMATE_NODES = True
SCALE_ANIM_WITH_TIME = True
NODE_BORDER = True

if VIS_NODE_WIDTH >= 200:
    NODE_BORDER = False
    ANIMATE_NODES = False
    SCALE_ANIM_WITH_TIME = False

# Runtime
MIN_ALGORITHM_CALL_STEP = 500
TIMED_DAYS = 50

# Colours
BG_COLOUR = (50, 50, 50)
GRID_COLOUR = (80, 80, 80)
GRID_BORDER_COLOUR = (200, 200, 200)

HEALTHY = (128, 185, 105)
INFECTED_UNKNOWN = (200, 60, 60)
INFECTED_KNOWN = (167, 80, 80)
RECOVERED = (210, 210, 100)
DEAD = (60, 40, 60)