import numpy as np
import matplotlib.pyplot as plt

# 参数设置
T_orbit = 90  # 卫星轨道周期（分钟）
theta = 60    # 卫星轨道最大纬度（度）
omega_earth = 360 / 1440  # 地球自转角速度（度/分钟），1440分钟为一天
omega_sat = 360 / T_orbit  # 卫星轨道角速度（度/分钟）
x_p = 30       # 观测点纬度（赤道）

# 时间范围
time = np.linspace(0, 8 * T_orbit, 1000)  # 两个轨道周期内的时间点

# 计算纬度
x_s = theta * np.sin(2 * np.pi * time / T_orbit)  # 卫星纬度
x_p_array = np.full_like(time, x_p)              # 观测点纬度（固定值）

# 计算经度
y_s = omega_sat * np.cos(np.radians(theta)) * time  # 修正卫星经度变化公式
y_p = omega_earth * time                            # 观测点经度

# 创建子图
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# 绘制纬度变化图
axs[0].plot(time, x_s, label="satellite latitude $x_s$", color="blue")
axs[0].plot(time, x_p_array, label="Latitude of observation point $x_p$", color="red", linestyle="--")
axs[0].set_ylabel("Latitude")
axs[1].set_xlabel("Time (mins)")
axs[0].set_title("Latitude and longitude over time")
axs[0].legend()
axs[0].grid(True)

# 绘制经度变化图
axs[1].plot(time, y_s % 360, label="satellite longitude $y_s$", color="blue")
axs[1].plot(time, y_p % 360, label="Longitude of the observation point $y_p$", color="red", linestyle="--")
axs[1].set_xlabel("Time (mins)")
axs[1].set_ylabel("Longitude")
axs[1].legend()
axs[1].grid(True)

# 显示图形
plt.tight_layout()
plt.show()
