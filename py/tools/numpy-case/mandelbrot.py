import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(w, h=None, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    if h is None:
        h = w
    y, x = np.ogrid[-3/2:3/2:h * 1j, -9/4:3/4:w * 1j]  # 界定的复平面坐标系的横纵轴
    c = x + y * 1j  # 界定的复平面坐标系矩阵
    divtime = maxit + np.zeros(c.shape, dtype=int)  # 初始化的权重矩阵 = 轮数+零矩阵
    z = c  # 初始化的用于迭代的复平面坐标系矩阵z
    for i in range(maxit):
        z = z**2 + c  # mandelbrot集合迭代公式
        diverge = z * np.conj(z) > 2**2  # 计算本轮发散的布尔索引
        div_now = diverge & (divtime == maxit)  # 计算比上轮新增的布尔索引
        divtime[div_now] = i  # 为新增的发散设置权重
        z[diverge] = 2  # 为发散点的值赋值 简化后续运算
        '''
            这个值要大于根号2 如果不赋值 后续循环中将会溢出
            RuntimeWarning: overflow encountered in multiply
        '''
    return divtime


w = int(input("输入像素值"))
plt.imshow(mandelbrot(w))

ax = plt.gca()
ax.grid(True, linestyle='-.')
plt.yticks(np.mgrid[0:w:9j], np.mgrid[3/2:-3/2:9j])
plt.xticks(np.mgrid[0:w:9j], np.mgrid[-9/4:3/4:9j])
ax.spines['bottom'].set_position(('data', 1 / 2 * w))
ax.spines['left'].set_position(('data', 3 / 4 * w))
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
plt.tick_params(axis='x', colors='white')
plt.tick_params(axis='y', colors='white')
plt.savefig('./mandelbrot.png', format='png', transparent=True,
            dpi=300, pad_inches = 0 ,bbox_inches = 'tight')
plt.show()
