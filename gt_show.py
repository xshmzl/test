import matplotlib.pyplot as plt

from data import binvox_rw
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np



# 指定Binvox文件路径
with open('X:/study/shape/1airplane/1a32f10b20170883663e90eaf6b4ca52/model.binvox', 'rb')as f:
    vox=binvox_rw.read_as_3d_array(f)
    pred_3d=np.asarray(vox.data,dtype=np.float32)
    pred_3d = np.transpose(pred_3d, (0, 2, 1))

# 获取体素数据
voxels = vox.data

ax2 = plt.figure(figsize=(6, 6), dpi=300).add_subplot(projection='3d')     #6*6的大小
ax2.voxels(pred_3d, facecolors='w', edgecolor='k', shade=True, linewidths=0.2)


ax2.azim =40   #水平角度
ax2.elev =15    #俯仰角角度
ax2.dist =7     #距离远近
#ax2.axis('off')
plt.show()
