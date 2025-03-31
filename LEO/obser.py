import numpy as np
import matplotlib.pyplot as plt

# 地球参数
earth_radius = 6371  # 地球半径，单位：km
earth_rotation_rate = 360 / 86164  # 地球自转速率，单位：度/秒（一天86164秒，旋转360°）

# 卫星轨道参数
satellite_altitude = 600  # 卫星轨道高度，单位：km
orbit_inclination = 90  # 卫星轨道倾角，单位：度
orbit_period = 90 * 60  # 卫星一圈轨道周期，单位：秒

# 轨迹计算参数
time_interval = 10  # 时间间隔，单位：秒
total_time = 10 * orbit_period  # 模拟时间，模拟10个轨道周期
num_points = int(total_time / time_interval)  # 计算轨迹的点数

# 角速度
satellite_angular_velocity = 360 / orbit_period  # 卫星的轨道运动角速度，单位：度/秒

# 初始化轨迹数据
times = np.linspace(0, total_time, num_points)  # 时间序列
longitude = []
latitude = []

# 计算轨迹投影
for t in times:
    # 卫星的轨道角度 (相对于轨道平面)
    orbit_angle = satellite_angular_velocity * t  # 卫星在轨道平面的当前位置（度）
    
    # 计算地面轨迹投影的纬度
    lat = orbit_inclination * np.sin(np.radians(orbit_angle))  # 纬度跟随卫星的倾角变化
    
    # 计算地球自转导致的地面经度变化
    lon = (earth_rotation_rate * t + orbit_angle) % 360  # 地球自转和卫星运动结合的经度变化
    
    longitude.append(lon)
    latitude.append(lat)

# 转换为数组
longitude = np.array(longitude)
latitude = np.array(latitude)

# 绘制卫星地面轨迹
plt.figure(figsize=(12, 6), dpi=100)

# 控制线段宽度
line_width = 3  # 设置线段宽度

# 分段绘制轨迹，避免连接末尾的直线
orbit_points = int(orbit_period / time_interval)  # 每个轨道周期的点数
for i in range(0, len(longitude), orbit_points):
    # 每次绘制一个轨道周期的轨迹
    plt.plot(longitude[i:i + orbit_points], latitude[i:i + orbit_points], 
             linewidth=line_width, label=f"Orbit {i // orbit_points + 1}" if i == 0 else None)

plt.title("Satellite Ground Track Projection")
plt.xlabel("Longitude (degrees)")
plt.ylabel("Latitude (degrees)")
plt.xlim(0, 360)
plt.ylim(-90, 90)
plt.grid(True)
plt.legend()
plt.show()
