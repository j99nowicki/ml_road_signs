import torch
import os
import pandas as pd
from torch.utils.data import Dataset
from PIL import Image


class GTSRB_Test(Dataset):
    

    def __init__(self, images_dir='./source_data/test/GTSRB/Final_Test/Images', 
                 gt_csv_path='./source_data/test/GT-final_test.csv', transform=None):
        """
        Args:
            images_dir (string): Path to GTSRB images directory
            gt_csv_path: path to test ground truth csv file
            transform (callable, optional): Optional transform to be applied
        """
        self.images_dir = images_dir
        self.gt_csv_path = gt_csv_path

        self.gt_data = pd.read_csv(gt_csv_path, header=0)
        self.transform = transform

    def __len__(self):
        return len(self.gt_data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.images_dir, self.gt_data.iloc[idx, 0])
        img = Image.open(img_path)

        classId = '000'+self.gt_data.iloc[idx, 7]

        if self.transform is not None:
            img = self.transform(img)

        return img, classId