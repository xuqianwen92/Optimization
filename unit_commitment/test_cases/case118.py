"""
Units data for test cases
Data is obtained from
http://motor.ece.iit.edu/data/
"""
from numpy import array

# Transmission line data format
F_BUS = 0
T_BUS = 1
BR_X = 2
RATE_A = 3

# Generator format
GEN_BUS = 0
COST_C = 1
COST_B = 2
COST_A = 3
PG_MAX = 4
PG_MIN = 5
I0 = 6
MIN_DOWN = 7
MIN_UP = 8
RU = 9
RD = 10
COLD_START = 11


def case118():
    ppc = {"version": '2'}
    ppc["baseMVA"] = 100.0

    ppc["bus"] = array([
        0.014502809,
        0.005687008,
        0.011090068,
        0.008531852,
        0.014786757,
        0.00540306,
        0.019905868,
        0.013364336,
        0.009667646,
        0.003980638,
        0.025592877,
        0.00710943,
        0.003128792,
        0.017061025,
        0.012796438,
        0.005119111,
        0.003980638,
        0.002844844,
        0.001990319,
        0.017631601,
        0.004835162,
        0.006825481,
        0.012228541,
        0.016777076,
        0.006541533,
        0.016777076,
        0.009383698,
        0.0088158,
        0.007232653,
        0.005357521,
        0.009911413,
        0.009911413,
        0.004821769,
        0.004286017,
        0.01419743,
        0.007500529,
        0.009107785,
        0.005357521,
        0.023305215,
        0.004553893,
        0.004553893,
        0.004821769,
        0.006161149,
        0.030269992,
        0.01687619,
        0.022501587,
        0.003214512,
        0.003214512,
        0.074201662,
        0.020894331,
        0.020626455,
        0.010447165,
        0.007500529,
        0.017679818,
        0.018215571,
        0.012590174,
        0.018215571,
        0.016340438,
        0.019019199,
        0.010447165,
        0.034823885,
        0.014465306,
        0.005357521,
        0.002946636,
        0.006429025,
        0.005625397,
        0.01285805,
        0.020894331,
        0.017411942,
        0.003214512,
        0.008036281,
        0.011250794,
        0.010179289,
        0.004018141,
        0.009107785,
        0.009911413,
        0.005893273,
        0.00133938,
        0.006161149,
        0.010179289,
        0.008304157,
        0.01151867,
        0.007500529,
        0.000535752,
        0.002143008,
        0.010447165,
        0.006696901,
        0.002274268,
        0.006254905,
        0.005687008,
        0.008839909,
    ])

    ppc["gen"] = array([
        [4, 31.67, 26.2438, 0.069663, 30, 1, 1, 1, 15, 15, 40],
        [6, 31.67, 26.2438, 0.069663, 30, 5, 1, 1, 1, 15, 15, 40],
        [8, 31.67, 26.2438, 0.069663, 30, 5, 1, 1, 1, 15, 15, 40],
        [10, 6.78, 12.8875, 0.010875, 300, 150, 8, 8, 8, 150, 150, 440],
        [12, 6.78, 12.8875, 0.010875, 300, 100, 8, 8, 8, 150, 150, 110],
        [15, 31.67, 26.2438, 0.069663, 30, 10, 1, 1, 1, 15, 15, 40],
        [18, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [19, 31.67, 26.2438, 0.069663, 30, 5, 1, 1, 1, 15, 15, 40],
        [24, 31.67, 26.2438, 0.069663, 30, 5, 1, 1, 1, 15, 15, 40],
        [25, 6.78, 12.8875, 0.010875, 300, 100, 8, 8, 8, 150, 150, 100],
        [26, 32.96, 10.76, 0.003, 350, 100, 8, 8, 8, 175, 175, 100],
        [27, 31.67, 26.2438, 0.069663, 30, 8, 1, 1, 1, 15, 15, 40],
        [31, 31.67, 26.2438, 0.069663, 30, 8, 1, 1, 1, 15, 15, 40],
        [32, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [34, 31.67, 26.2438, 0.069663, 30, 8, 1, 1, 1, 15, 15, 40],
        [36, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [40, 31.67, 26.2438, 0.069663, 30, 8, 1, 1, 1, 15, 15, 40],
        [42, 31.67, 26.2438, 0.069663, 30, 8, 1, 1, 1, 15, 15, 40],
        [46, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 59],
        [49, 28, 12.3299, 0.002401, 250, 50, 8, 8, 8, 125, 125, 100],
        [54, 28, 12.3299, 0.002401, 250, 50, 8, 8, 8, 125, 125, 100],
        [55, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [56, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [59, 39, 13.29, 0.0044, 200, 50, 10, 8, 8, 100, 100, 100],
        [61, 39, 13.29, 0.0044, 200, 50, 10, 8, 8, 100, 100, 100],
        [62, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [65, 64.16, 8.3391, 0.01059, 420, 100, 10, 10, 10, 210, 210, 250],
        [66, 64.16, 8.3391, 0.01059, 420, 100, 10, 10, 10, 210, 210, 250],
        [69, 6.78, 12.8875, 0.010875, 300, 80, 10, 8, 8, 150, 150, 100],
        [70, 74.33, 15.4708, 0.045923, 80, 30, 4, 4, 4, 40, 40, 45],
        [72, 31.67, 26.2438, 0.069663, 30, 10, 1, 1, 1, 15, 15, 40],
        [73, 31.67, 26.2438, 0.069663, 30, 5, 1, 1, 1, 15, 15, 40],
        [74, 17.95, 37.6968, 0.028302, 20, 5, 1, 1, 1, 10, 10, 30],
        [76, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [77, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [80, 6.78, 12.8875, 0.010875, 300, 150, 10, 8, 8, 150, 150, 440],
        [82, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [85, 31.67, 26.2438, 0.069663, 30, 10, 1, 1, 1, 15, 15, 40],
        [87, 32.96, 10.76, 0.003, 300, 100, 10, 8, 8, 150, 150, 440],
        [89, 6.78, 12.8875, 0.010875, 200, 50, 10, 8, 8, 100, 100, 400],
        [90, 17.95, 37.6968, 0.028302, 20, 8, 1, 1, 1, 10, 10, 30],
        [91, 58.81, 22.9423, 0.009774, 50, 20, 1, 1, 1, 25, 25, 45],
        [92, 6.78, 12.8875, 0.010875, 300, 100, 8, 8, 8, 150, 150, 100],
        [99, 6.78, 12.8875, 0.010875, 300, 100, 8, 8, 8, 150, 150, 100],
        [100, 6.78, 12.8875, 0.010875, 300, 100, 8, 8, 8, 150, 150, 110],
        [103, 17.95, 37.6968, 0.028302, 20, 8, 1, 1, 1, 10, 10, 30],
        [104, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [105, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [107, 17.95, 37.6968, 0.028302, 20, 8, 1, 1, 1, 10, 10, 30],
        [110, 58.81, 22.9423, 0.009774, 50, 25, 2, 2, 2, 25, 25, 45],
        [111, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [112, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [113, 10.15, 17.82, 0.0128, 100, 25, 5, 5, 5, 50, 50, 50],
        [116, 58.81, 22.9423, 0.009774, 50, 25, 2, 2, 2, 25, 25, 45]
    ])
    ppc["line"] = array([
        [1, 2, 0.0999, 175],
        [1, 3, 0.0424, 175],
        [4, 5, 0.00798, 500],
        [3, 5, 0.108, 175],
        [5, 6, 0.054, 175],
        [6, 7, 0.0208, 175],
        [8, 9, 0.0305, 500],
        [8, 5, 0.0267, 500],
        [9, 10, 0.0322, 500],
        [4, 11, 0.0688, 175],
        [5, 11, 0.0682, 175],
        [11, 12, 0.0196, 175],
        [2, 12, 0.0616, 175],
        [3, 12, 0.16, 175],
        [7, 12, 0.034, 175],
        [11, 13, 0.0731, 175],
        [12, 14, 0.0707, 175],
        [13, 15, 0.2444, 175],
        [14, 15, 0.195, 175],
        [12, 16, 0.0834, 175],
        [15, 17, 0.0437, 500],
        [16, 17, 0.1801, 175],
        [17, 18, 0.0505, 175],
        [18, 19, 0.0493, 175],
        [19, 20, 0.117, 175],
        [15, 19, 0.0394, 175],
        [20, 21, 0.0849, 175],
        [21, 22, 0.097, 175],
        [22, 23, 0.159, 175],
        [23, 24, 0.0492, 175],
        [23, 25, 0.08, 500],
        [26, 25, 0.0382, 500],
        [25, 27, 0.163, 500],
        [27, 28, 0.0855, 175],
        [28, 29, 0.0943, 175],
        [30, 17, 0.0388, 500],
        [8, 30, 0.0504, 175],
        [26, 30, 0.086, 500],
        [17, 31, 0.1563, 175],
        [29, 31, 0.0331, 175],
        [23, 32, 0.1153, 140],
        [31, 32, 0.0985, 175],
        [27, 32, 0.0755, 175],
        [15, 33, 0.1244, 175],
        [19, 34, 0.247, 175],
        [35, 36, 0.0102, 175],
        [35, 37, 0.0497, 175],
        [33, 37, 0.142, 175],
        [34, 36, 0.0268, 175],
        [34, 37, 0.0094, 500],
        [38, 37, 0.0375, 500],
        [37, 39, 0.106, 175],
        [37, 40, 0.168, 175],
        [30, 38, 0.054, 175],
        [39, 40, 0.0605, 175],
        [40, 41, 0.0487, 175],
        [40, 42, 0.183, 175],
        [41, 42, 0.135, 175],
        [43, 44, 0.2454, 175],
        [34, 43, 0.1681, 175],
        [44, 45, 0.0901, 175],
        [45, 46, 0.1356, 175],
        [46, 47, 0.127, 175],
        [46, 48, 0.189, 175],
        [47, 49, 0.0625, 175],
        [42, 49, 0.323, 175],
        [42, 49, 0.323, 175],
        [45, 49, 0.186, 175],
        [48, 49, 0.0505, 175],
        [49, 50, 0.0752, 175],
        [49, 51, 0.137, 175],
        [51, 52, 0.0588, 175],
        [52, 53, 0.1635, 175],
        [53, 54, 0.122, 175],
        [49, 54, 0.289, 175],
        [49, 54, 0.291, 175],
        [54, 55, 0.0707, 175],
        [54, 56, 0.00955, 175],
        [55, 56, 0.0151, 175],
        [56, 57, 0.0966, 175],
        [50, 57, 0.134, 175],
        [56, 58, 0.0966, 175],
        [51, 58, 0.0719, 175],
        [54, 59, 0.2293, 175],
        [56, 59, 0.251, 175],
        [56, 59, 0.239, 175],
        [55, 59, 0.2158, 175],
        [59, 60, 0.145, 175],
        [59, 61, 0.15, 175],
        [60, 61, 0.0135, 500],
        [60, 62, 0.0561, 175],
        [61, 62, 0.0376, 175],
        [63, 59, 0.0386, 500],
        [63, 64, 0.02, 500],
        [64, 61, 0.0268, 500],
        [38, 65, 0.0986, 500],
        [64, 65, 0.0302, 500],
        [49, 66, 0.0919, 500],
        [49, 66, 0.0919, 500],
        [62, 66, 0.218, 175],
        [62, 67, 0.117, 175],
        [65, 66, 0.037, 500],
        [66, 67, 0.1015, 175],
        [65, 68, 0.016, 500],
        [47, 69, 0.2778, 175],
        [49, 69, 0.324, 175],
        [68, 69, 0.037, 500],
        [69, 70, 0.127, 500],
        [24, 70, 0.4115, 175],
        [70, 71, 0.0355, 175],
        [24, 72, 0.196, 175],
        [71, 72, 0.18, 175],
        [71, 73, 0.0454, 175],
        [70, 74, 0.1323, 175],
        [70, 75, 0.141, 175],
        [69, 75, 0.122, 500],
        [74, 75, 0.0406, 175],
        [76, 77, 0.148, 175],
        [69, 77, 0.101, 175],
        [75, 77, 0.1999, 175],
        [77, 78, 0.0124, 175],
        [78, 79, 0.0244, 175],
        [77, 80, 0.0485, 500],
        [77, 80, 0.105, 500],
        [79, 80, 0.0704, 175],
        [68, 81, 0.0202, 500],
        [81, 80, 0.037, 500],
        [77, 82, 0.0853, 200],
        [82, 83, 0.03665, 200],
        [83, 84, 0.132, 175],
        [83, 85, 0.148, 175],
        [84, 85, 0.0641, 175],
        [85, 86, 0.123, 500],
        [86, 87, 0.2074, 500],
        [85, 88, 0.102, 175],
        [85, 89, 0.173, 175],
        [88, 89, 0.0712, 500],
        [89, 90, 0.188, 500],
        [89, 90, 0.0997, 500],
        [90, 91, 0.0836, 175],
        [89, 92, 0.0505, 500],
        [89, 92, 0.1581, 500],
        [91, 92, 0.1272, 175],
        [92, 93, 0.0848, 175],
        [92, 94, 0.158, 175],
        [93, 94, 0.0732, 175],
        [94, 95, 0.0434, 175],
        [80, 96, 0.182, 175],
        [82, 96, 0.053, 175],
        [94, 96, 0.0869, 175],
        [80, 97, 0.0934, 175],
        [80, 98, 0.108, 175],
        [80, 99, 0.206, 200],
        [92, 100, 0.295, 175],
        [94, 100, 0.058, 175],
        [95, 96, 0.0547, 175],
        [96, 97, 0.0885, 175],
        [98, 100, 0.179, 175],
        [99, 100, 0.0813, 175],
        [100, 101, 0.1262, 175],
        [92, 102, 0.0559, 175],
        [101, 102, 0.112, 175],
        [100, 103, 0.0525, 500],
        [100, 104, 0.204, 175],
        [103, 104, 0.1584, 175],
        [103, 105, 0.1625, 175],
        [100, 106, 0.229, 175],
        [104, 105, 0.0378, 175],
        [105, 106, 0.0547, 175],
        [105, 107, 0.183, 175],
        [105, 108, 0.0703, 175],
        [106, 107, 0.183, 175],
        [108, 109, 0.0288, 175],
        [103, 110, 0.1813, 175],
        [109, 110, 0.0762, 175],
        [110, 111, 0.0755, 175],
        [110, 112, 0.064, 175],
        [17, 113, 0.0301, 175],
        [32, 113, 0.203, 500],
        [32, 114, 0.0612, 175],
        [27, 115, 0.0741, 175],
        [114, 115, 0.0104, 175],
        [68, 116, 0.00405, 500],
        [12, 117, 0.14, 175],
        [75, 118, 0.0481, 175],
        [76, 118, 0.0544, 175],
    ])

    ppc["Load_profile"] = array([4620,
                                 4356,
                                 3828,
                                 2640,
                                 3300,
                                 3960,
                                 4620,
                                 5148,
                                 5412,
                                 5808,
                                 5874,
                                 5544,
                                 5280,
                                 5016,
                                 5808,
                                 5940,
                                 5610,
                                 5874,
                                 6204,
                                 6468,
                                 6600,
                                 5940,
                                 5742,
                                 5412])

    return ppc
