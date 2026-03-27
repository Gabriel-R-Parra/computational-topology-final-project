# Hello again!

import subprocess
import os

def makeBarcodes(pointCloud: str):
    result = subprocess.run(
        ["./ripser", "--format", "point-cloud", f"../pointCloudsRandom/{pointCloud}"],
        capture_output=True,
        text=True
    )

    resultStart = (result.stdout).find("persistence intervals in dim 0:")
    resultEnd = (result.stdout).find("persistence intervals in dim 1:")

    resultDimZero = (result.stdout)[resultStart: resultEnd]
    resultDimOne = (result.stdout)[resultEnd:]

    # print("A")

    # print(result.stdout)
    # print(resultDimZero)
    # print(resultDimOne)

    pointCloudNoEnding = pointCloud[: -6]

    # "../persistenceBarcodes/{pointCloud[8:10]}/Dim0/{pointCloud[: len(pointCloud) - 14]}PBD0.txt"
    """
    with open(f"examples/pointclouds/Barcodes/Dim0/{pointCloudNoEnding}PBD0.txt", "w") as f:
        f.write(resultDimZero)
        # print("testing")

    with open(f"examples/pointclouds/Barcodes/Dim1/{pointCloudNoEnding}PBD1.txt", "w") as f:
        f.write(resultDimOne)
        # print("testing")
    """
    
    with open(f"../persistenceBarcodesRandom/{pointCloud[8:10]}/Dim0/{pointCloud[: len(pointCloud) - 20]}RandomPBD0.txt", "w") as f:
        f.write(resultDimZero)

    # print("B")

    with open(f"../persistenceBarcodesRandom/{pointCloud[8:10]}/Dim1/{pointCloud[: len(pointCloud) - 20]}RandomPBD1.txt", "w") as f:
        f.write(resultDimOne)

def main():
    print("Hello, World!")
    
    pointClouds = os.listdir("../pointCloudsRandom")
    # pointCloud = pointClouds[0]
    # print(pointCloud)
    # makeBarcodes(pointCloud)

    
    for pointCloud in pointClouds:
        print(pointCloud)
        # print(pointCloud[: len(pointCloud) - 14])
        makeBarcodes(pointCloud)
    
    # makeBarcodes("bottle-01PC.txt")

if __name__ == "__main__":
    main()