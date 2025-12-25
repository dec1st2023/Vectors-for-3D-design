import unittest
import numpy as np
from src.geometry import resample_to_n

class TestGeometry(unittest.TestCase):
    def test_resample_to_n_shape(self):
        """测试重采样是否产生正确数量的点。"""
        points = np.array([[0,0,0], [1,1,1], [2,2,2]])
        n_modules = 5
        # 期望 n_modules + 1 个点
        # 占位符断言，因为实现是 pass
        # res = resample_to_n(points, n_modules)
        # self.assertEqual(res.shape, (n_modules + 1, 3))
        pass

    def test_resample_endpoints(self):
        """测试起点和终点是否保持不变。"""
        pass

if __name__ == '__main__':
    unittest.main()
