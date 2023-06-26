import pandas as pd
import numpy as np
import nibabel as nib
import os



# path to directory
data_dir = '/home/sharapova/test/new_data_2506'

# data folders input and output
raw_dir = os.path.join(data_dir, 'raw')
mask_dir = os.path.join(data_dir, 'mask')
new_mask_dir = os.path.join(data_dir, 'new_mask')
raw_files = os.listdir(raw_dir)


def update_header_and_save(raw_filepath, mask_filepath, new_mask_filepath):
    raw_img = nib.load(raw_filepath)
    mask_img = nib.load(mask_filepath)

    # values to update
    attributes = ['extents', 'dim_info', 'slice_end', 'cal_max', 'cal_min', 
                  'glmax', 'glmin', 'srow_x', 'srow_y', 'srow_z']

    header = mask_img.header.copy()
    for attr in attributes:
        header[attr] = raw_img.header[attr]

    new_affine = np.eye(4)
    new_affine[:-1, :] = np.array([header['srow_x'], header['srow_y'], header['srow_z']])

    # saving an img to new folder
    updated_mask_img = nib.Nifti1Image(mask_img.get_fdata(), new_affine, header)
    nib.save(updated_mask_img, new_mask_filepath)


for raw_file in raw_files:
    raw_filepath = os.path.join(raw_dir, raw_file)
    mask_filepath = os.path.join(mask_dir, raw_file)
    new_mask_filepath = os.path.join(new_mask_dir, os.path.splitext(raw_file)[0] + '_mask.nii')
    update_header_and_save(raw_filepath, mask_filepath, new_mask_filepath)

print('\n**********\t', f'New masks generated & saved in {new_mask_filepath}', '\t**********\n')