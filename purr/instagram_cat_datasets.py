from os import PathLike

import torchvision.io
from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co
import torchvision
from torchvision.datasets.folder import default_loader

import glob
from typing import AnyStr, Generator


class InstagramEarDataset(Dataset):
    def __init__(self, files: list[PathLike], transform=None, target_transform=None, loader=default_loader):
        self.img_labels = len(files) * [0]
        self.img_list = files
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, idx) -> T_co:
        img_path = self.img_list[idx]
        img = self.loader(str(img_path))
        label = self.img_labels[idx]
        if self.transform:
            img = self.transform(img)
        if self.target_transform:
            label = self.target_transform(label)
        return img, label
