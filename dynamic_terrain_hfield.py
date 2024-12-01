import time
import mujoco as mj
import mujoco.viewer as mj_viewer
import numpy as np

# 加载模型文件
model = mj.MjModel.from_xml_path('terrain.xml')
data = mj.MjData(model)

# 获取 timestep 设置（从 XML 文件读取）
timestep = model.opt.timestep  # 获取 XML 文件中设置的 timestep

# 创建 viewer
viewer = mj_viewer.launch_passive(model, data)

# 设置摄像机参数
viewer.cam.type = mj.mjtCamera.mjCAMERA_FREE
viewer.cam.lookat = [0, 0, 0]
viewer.cam.distance = 20
viewer.cam.azimuth = 45
viewer.cam.elevation = -10

viewer.sync()

# 控制 hfield 更新的频率
hfield_update_interval = 20  # 每10步更新一次
hfield_step_counter = 0

# 主循环
while viewer.is_running():
    step_start = time.time()

    # 仅每隔一定步数更新一次 hfield
    if hfield_step_counter % hfield_update_interval == 0:
        for i, _ in enumerate(model.hfield_data):
            model.hfield_data[i] = np.random.uniform(low=0, high=1)
        viewer.update_hfield(0)

    # 执行物理步进，更新小球状态
    mj.mj_step(model, data)

    # 同步物理和渲染状态
    viewer.sync()

    # 增加步数计数
    hfield_step_counter += 1

    # 计算下一次步进的时间
    time_until_next_step = timestep - (time.time() - step_start)
    if time_until_next_step > 0:
        time.sleep(time_until_next_step)
