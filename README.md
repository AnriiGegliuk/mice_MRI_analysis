# MRI Analysis project

Skull stripping is a key pre-processing technique in neuroimaging, aiming to remove non-brain structures like the skull, skin, muscles, and fat from brain images. Its goal is to isolate and focus on the brain, the primary structure of interest, enhancing data analysis by minimizing noise and bias from non-brain components. For this purpose, we are using and adapting to our needs [BEN's project](https://github.com/AnriiGegliuk/BEN_project) and part of it used [here.](https://github.com/AnriiGegliuk/BEN_project/blob/main/utils/new_mask.py)

![image](https://github.com/AnriiGegliuk/mice_MRI_analysis/assets/120349975/f3c74929-f38d-4250-99c8-67a66e3a60d9)


However, after processing our data, the following brain masks are generated (we are using [MRIcron](https://people.cas.sc.edu/rorden/mricron/index.HTML) to open raw and mask .NIfTI images):

![image](https://github.com/AnriiGegliuk/mice_MRI_analysis/assets/120349975/5912e6bf-99c7-4e37-a3bc-8dd6087bd009)

![image](https://github.com/AnriiGegliuk/mice_MRI_analysis/assets/120349975/d96f62b3-85ac-4997-92c9-e1bbcee86df3)

This project is focused on processing and analyzing 3D brain images of rodents, specifically mice, in the Neuroimaging Informatics Technology Initiative (NIfTI) format. The central task involves applying affine transformations to align these brain images with a standard anatomical space, which is essential for subsequent comparison and analysis.

![image](https://github.com/AnriiGegliuk/mice_MRI_analysis/assets/120349975/812500ad-9ccc-48a5-b2b1-29b6d5f53306)

The processing pipeline is built using Python, and specifically leverages the nibabel library for handling NIfTI images, and numpy for numerical operations. 

It consists of loading raw brain images and corresponding mask images, applying appropriate transformations, and saving the updated masks. Moreover, the project provides utilities for visualizing the 3D brain structures, using libraries such as nilearn and itkwidgets, which are valuable for quality control and exploration.


