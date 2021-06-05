# 3D-ANAS
code for paper "3D-ANAS: 3D Asymmetric Neural ArchitectureSearch for Fast Hyperspectral Image Classification"

The core part is compressed into one_stage_nas.rar, before to use this, please uncompress this .rar file at first.

# searching an efficient structure. You can change settings in configs/dataset/**.yaml to tailor a new model for your own data
cd ./tools
python search.py --config-file '../configs/PaviaU/search_ad.yaml' --device '0'

# training the found model
cd ./tools
python train.py --config-file '../configs/PaviaU/train_ad.yaml' --device '0'

# predicting the final result 
cd ./tools
python infe.py --config-file '../configs/PaviaU/infe_ad.yaml' --device '0'

