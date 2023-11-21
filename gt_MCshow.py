

import matplotlib
matplotlib.use('Qt5Agg')  # 也可以尝试 'TkAgg' 或其他支持交互式显示的后端
import vtk
from mcubes import marching_cubes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from data import binvox_rw
# 生成一个简单的三维标量数据网格
#with open('X:/study/shape/1airplane/1a32f10b20170883663e90eaf6b4ca52/model.binvox', 'rb')as f:
with open('X:/study/shape/4car/1a3b35be7a0acb2d9f2366ce3e663402/model.binvox', 'rb')as f:
    data = binvox_rw.read_as_3d_array(f)

# 设置等值面阈值
isovalue = 0.699999

# 执行 Marching Cubes
#vertices, triangles = marching_cubes(data.data, isovalue)

# 调整 Marching Cubes 等参数
vertices, triangles = marching_cubes(data.data, isovalue)


# 可视化结果
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(vertices[:, 0], vertices[:, 1], triangles, vertices[:, 2], cmap='viridis')
ax.azim =40   #水平角度
ax.elev =15    #俯仰角角度
ax.dist =7     #距离远近
#ax.axis('off')
plt.show()