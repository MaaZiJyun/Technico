import numpy as np

# 地球参数
earth_radius = 6371  # 地球半径，单位：km
earth_rotation_rate = 360 / 86164  # 地球自转速率，单位：度/秒（一天86164秒，旋转360°）
coverage_resolution = 1  # 地球覆盖分辨率，单位：度 （每经纬度点间的间隔）

# 卫星轨道参数
satellite_altitude = 500  # 卫星轨道高度，单位：km
orbit_inclination = 90  # 卫星轨道倾角，单位：度
orbit_period = 5400  # 单颗卫星的轨道周期，单位：秒
num_satellites = 3  # 卫星数量，假设分布均匀

# 设置模拟参数
time_interval = 10  # 时间间隔，单位：秒
max_orbits = 10000  # 最大模拟轨道周期数
num_points_per_orbit = int(orbit_period / time_interval)  # 每轨道周期的点数

# 初始化覆盖区域
covered_points = set()  # 使用集合记录已覆盖的地面点

# 模拟多个卫星的轨迹
for orbit in range(max_orbits):
    for sat_id in range(num_satellites):  # 遍历每颗卫星
        for t in range(num_points_per_orbit):
            # 当前时间
            current_time = orbit * orbit_period + t * time_interval
            
            # 当前卫星的轨道角度 (相对于轨道平面)，每颗卫星相位不同
            orbital_phase_offset = sat_id * (360 / num_satellites)  # 不同卫星的初始相位偏移
            orbit_angle = (360 / orbit_period) * current_time + orbital_phase_offset
            
            # 地面纬度 (由轨道倾角决定)
            lat = orbit_inclination * np.sin(np.radians(orbit_angle))  # 纬度跟随卫星的倾角变化
            
            # 地面经度 (由地球自转和卫星运动决定)
            lon = (earth_rotation_rate * current_time + orbit_angle) % 360  # 地球自转和卫星运动结合的经度变化
            
            # 记录覆盖点 (四舍五入到整数纬度和经度)
            covered_points.add((round(lat), round(lon)))
    
    # 判断是否覆盖所有区域
    if len(covered_points) >= (360 / coverage_resolution) * (180 / coverage_resolution):  # 近似覆盖全球所有整数经纬度点
        print(f"{num_satellites} 颗卫星需要 {orbit + 1} 个轨道周期才能覆盖地球上的所有点")
        break
else:
    print(f"在最大模拟轨道周期数内，{num_satellites} 颗卫星未能覆盖地球上的所有点")
