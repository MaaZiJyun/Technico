import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 参数设置
omega_s = 1.0  # 点 s 的角速度
omega_e = 0.8  # 点 e 的角速度
theta = np.pi / 4  # 两轨迹平面之间的夹角（45度）

# 时间范围
time = np.linspace(0, 20, 1000)  # 时间点
radius = 1  # 球面半径

# 点 s 的轨迹（平行于 x-y 平面）
x_s = radius * np.cos(omega_s * time)
y_s = radius * np.sin(omega_s * time)
z_s = np.zeros_like(time)  # z 坐标固定为 0

# 点 e 的轨迹（绕 z-y 平面旋转，考虑夹角 theta）
x_e = radius * np.cos(omega_e * time) * np.sin(theta)
y_e = radius * np.cos(omega_e * time) * np.cos(theta)
z_e = radius * np.sin(omega_e * time)

# 计算两点相会的周期
relative_omega = abs(omega_s - omega_e * np.cos(theta))
T_meet = 2 * np.pi / relative_omega
print(f"两点的相会周期为: {T_meet:.2f} 时间单位")

# 创建 3D 动态绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_title("两点在球面上的运动轨迹")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# 初始化点和轨迹
point_s, = ax.plot([], [], [], 'ro', label='点 s')  # 点 s
point_e, = ax.plot([], [], [], 'bo', label='点 e')  # 点 e
trajectory_s, = ax.plot([], [], [], 'r--', alpha=0.5)  # 点 s 的轨迹
trajectory_e, = ax.plot([], [], [], 'b--', alpha=0.5)  # 点 e 的轨迹

# 动画更新函数
def update(frame):
    # 更新点的位置
    point_s.set_data([x_s[frame]], [y_s[frame]])  # x 和 y 数据需要是列表
    point_s.set_3d_properties([z_s[frame]])  # z 数据需要是列表
    
    point_e.set_data([x_e[frame]], [y_e[frame]])  # x 和 y 数据需要是列表
    point_e.set_3d_properties([z_e[frame]])  # z 数据需要是列表
    
    # 更新轨迹
    trajectory_s.set_data(x_s[:frame], y_s[:frame])
    trajectory_s.set_3d_properties(z_s[:frame])
    
    trajectory_e.set_data(x_e[:frame], y_e[:frame])
    trajectory_e.set_3d_properties(z_e[:frame])
    
    return point_s, point_e, trajectory_s, trajectory_e

# 创建动画
ani = FuncAnimation(fig, update, frames=len(time), interval=20, blit=False)

# 添加图例
ax.legend()

plt.show()
