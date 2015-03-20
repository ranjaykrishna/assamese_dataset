export LD_LIBRARY_PATH='/home/stanford/cudnn-6.5-linux-R1:/usr/local/cuda/lib64:/opt/intel/composer_xe_2013_sp1.0.080/mkl/lib/intel64':$LD_LIBRARY_PATH
CAFFE=/home/karpathy/caffe3/build/tools
$CAFFE/caffe train --solver=solver.prototxt
