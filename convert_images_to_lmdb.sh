export LD_LIBRARY_PATH='/home/stanford/cudnn-6.5-linux-R1:/usr/local/cuda/lib64:/opt/intel/composer_xe_2013_sp1.0.080/mkl/lib/intel64':$LD_LIBRARY_PATH
CAFFE=/home/karpathy/caffe3/build/tools
$CAFFE/convert_imageset \
  --resize_height=256 \
  --resize_width=256 \
  --shuffle \
  /scail/data/group/vision/u/rak248/assamese_dataset/dataset/ \
  /scail/data/group/vision/u/rak248/assamese_dataset/dataset/LISTFILES.txt \
  /scail/data/group/vision/u/rak248/assamese_dataset/dataset_lmdb
