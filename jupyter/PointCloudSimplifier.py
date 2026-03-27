# PCD File opener

import open3d as o3d
import os
import numpy as np

# import subprocess

def main():
    print("Hello, World!")
    
    files = os.listdir("pointCloudsReal")
    # file = files[0]
    # print(file)
    """
    points = np.loadtxt(f"pointCloudsReal/{file}", delimiter=",")

    print(type(points))
    N = points.shape[0]
    idx = np.random.choice(N, size=1000, replace=False)
    sample = points[idx]

    np.savetxt(f"pointCloudsRandom/{file[:len(file) - 4]}Random.txt", sample, fmt="%.6f")
    """
    for file in files:
        print(file)
        points = np.loadtxt(f"pointCloudsReal/{file}", delimiter=",")

        N = points.shape[0]
        idx = np.random.choice(N, size=1000, replace=False)
        sample = points[idx]

        np.savetxt(f"pointCloudsRandom/{file[:len(file) - 4]}Random.txt", sample, fmt="%.6f")

    """
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    print("Loaded point count:", len(points))

    down = pcd.voxel_down_sample(voxel_size=0.015)
    down_points = np.asarray(down.points)
    print("Downsampled point count:", down_points.shape[0])

    np.savetxt(f"pointCloudsSimplified/{file[:len(file) - 4]}Simplified.txt", down_points, fmt="%.6f")
    """
    """
    for file in files:
        print(file)
        points = np.loadtxt(f"pointCloudsReal/{file}", delimiter=",")
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)

        down = pcd.voxel_down_sample(voxel_size=0.015)
        down_points = np.asarray(down.points)
        np.savetxt(f"pointCloudsSimplified/{file[:len(file) - 4]}Simplified.txt", down_points, fmt="%.6f")
    """
    
if __name__ == "__main__":
    main()