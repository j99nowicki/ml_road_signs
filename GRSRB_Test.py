import torch
import os
import pandas as pd
from torch.utils.data import Dataset
from PIL import Image

__name__ = 'GTSRB_Test'

class GTSRB_Test(Dataset):
    
    def __init__(self, images_dir='./source_data/test/GTSRB/Final_Test/Images', 
                 gt_csv_path='./source_data/test/GT-final_test.csv', transform=None):
        """
        Args:
            images_dir (string): Path to GTSRB images directory
            gt_csv_path: path to test ground truth csv file
            transform (callable, optional): Optional transform to be applied

        Attributes:
            classes (list): List of the class names.
            class_to_idx (dict): Dict with items (class_name, class_index).    
            
        """
        self.images_dir = images_dir
        self.gt_csv_path = gt_csv_path

        self.gt_data = pd.read_csv(gt_csv_path, header=0, sep=';')
        self.gt_data['_000ClassId']=gt_data.ClassId.astype(str).str.zfill(5)
        self.transform = transform
        
        classes, class_to_idx = self._find_classes(self )
        self.classes = classes
        self.class_to_idx = class_to_idx
        print(classes)

    def __len__(self):
        return len(self.gt_data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.images_dir, self.gt_data.iloc[idx, 0])
        img = Image.open(img_path)

        classId = self.gt_data.iloc[idx, '_000ClassId']

        if self.transform is not None:
            img = self.transform(img)
            
        return img, classId
    
    def _find_classes(self):
        """
        Finds the classes in the dataset

        Args:

        Returns:
            tuple: (classes, class_to_idx), class_to_idx is a dictionary.
        """
        print('hello')
        classes = pd.unique(gt_data['_000ClassId'])
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx