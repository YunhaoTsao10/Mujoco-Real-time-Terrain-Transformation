import numpy as np
import time
import os

nrow = 100
ncol = 100

# 初始化变量以跟踪是否需要更新高度数据
update_heightmap = True
last_update_time = time.time() - 5  # 设置初始时间为5秒之前，以便立即触发更新

while True:
    current_time = time.time()
    
    # 检查是否已经过去了5秒
    if current_time - last_update_time >= 5:
        # 更新最后更新时间
        last_update_time = current_time

        # 切换模式
        update_heightmap = not update_heightmap

        if update_heightmap:
            # 创建楼梯形状的高度数据
            height_data = np.zeros((nrow, ncol), dtype=np.float32)
            step_size = 1.0
            for idx in range(nrow):
                stair_level = idx // 10
                for j in range(ncol):
                    height_data[idx, j] = step_size * stair_level
            print(f'{time.time()} : Staircase map generated.')
        else:
            # 生成随机高度数据
            height_data = np.random.rand(nrow, ncol)
            sequence = np.arange(1, nrow * ncol + 1, dtype=np.float32).reshape(nrow, ncol)
            height_data += sequence / 100  # 规范化数值范围
            print(f'{time.time()} : Random map generated.')

        # 将高度数据保存为二进制文件
        with open('heightmap.bin', 'wb') as f:
            f.write(np.array(nrow, dtype=np.int32).tobytes())
            f.write(np.array(ncol, dtype=np.int32).tobytes())
            f.write(height_data.astype(np.float32).tobytes())

    # 等待5秒
    time.sleep(5)
