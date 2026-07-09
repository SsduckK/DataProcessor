import numpy as np
from pathlib import Path

import nuscenes


class DataManager:
    """
    based on nuScenes data
    """

    def __init__(self, data_path, path_preprocss=True):
        processed_path = None
        if path_preprocss:
            base_path = Path(__file__).resolve()
            processed_path = base_path.parent.parent.parent / "data"
        else:
            processed_path = data_path
        self.data = self.dataloader(processed_path)

    def dataloader(self, path):
        nusc = nuscenes.NuScenes(version="v1.0-mini", dataroot=path)
        return nusc


class LiDARMultiSweeper:
    """
    based on nuScenes
    """

    def __init__(self, dataset):
        self.nusc = dataset


def main():
    print("this is main of LiDAR multi sweep board")
    DM = DataManager("")


if __name__ == "__main__":
    main()
