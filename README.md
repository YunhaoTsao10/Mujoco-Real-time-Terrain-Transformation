先运行heightmap_generator生成地形的二进制文件，**这里heightdata数量不能超过10k。**  Run heightmap_generator.py to create the heightmap.bin file first, **the maximum number of heights can't exceed 10k.** 

## 宇树机器人h1的示例展示：Demo with Unitree h1:

![12月2日(1)](https://github.com/user-attachments/assets/486c312d-0a4c-4e68-b6e3-ad154563920f)

## 我参与的外骨骼项目的示例展示（不开源）：Demo with my exoskeleton project(not open sourced):

![12月2日](https://github.com/user-attachments/assets/10d1c6a7-ce05-482a-8821-a4e7618ccc2b)

这里主要是提供一个简单的实现在Mujoco仿真环境中实现地形实时变换的示例，示例当中的地形的变换高度是我随机生成的，后续你可以将高度值更改为实际雷达/深度相机感知到的点云值。这样就能实现真实场景的重构！  Here's a simple example of implementing real-time terrain modification in a MuJoCo simulation environment. In this example, the terrain height changes are randomly generated. Later, you can replace the height values with actual point cloud data from a radar or depth camera, which would enable the reconstruction of a real-world scenario!

## 相机点云数据生成mujoco地形示例（不开源）：Demo for converting live point cloud data to hfield data(not open sourced):

![pcl2hfield](https://github.com/user-attachments/assets/fc3abe86-3eed-4769-a615-d10c7b512360)



