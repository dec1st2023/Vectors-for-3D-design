OUTPUT_DIR = "./outputs"
IMG_DIR = OUTPUT_DIR + "/img"

W = 135.0
L = 72.0
H = 27
ORIGIN_OFFSET = (4.5, 4.5, 4.5) #坐标轴偏移
CROSS_SECTION_WIDTH = 8.0 # 导管宽度
START = (0.0, 45.0, 9.0)
END = (0.0, 18.0, 9.0)

#  clearance
SELF_CLEARANCE = 9.0
STATIC_CLEARANCE = 0
OBSTACLE_CLEARANCE = 0


OBSTACLE_CUBE = (36.0 - 4.5, 99.0 + 4.5, 27.0 - 4.5, 36.0 + 4.5, 0.0 + 4.5, 27.0 + 4.5)
EXTRA_START_POINTS = [(-87.0, 36.0, 9.0), (-12.0, 36.0, 9.0), (-12.0, 45.0, 9.0), (0.0, 45.0, 9.0)]
EXTRA_END_POINTS = [(0.0, 18.0, 9.0), (-12.0, 18.0, 9.0), (-12.0, 27.0, 9.0), (-87.0, 27.0, 9.0)]
