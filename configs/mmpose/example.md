
make onnx
```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
MMPOSE_DIR=/home/jglee/projects/mmpose
DEPLOY_CFG_PATH=${MMDEPLOY_DIR}/configs/mmpose/pose-detection_simcc_onnxruntime_dynamic.py
MODEL_CFG_PATH=${MMPOSE_DIR}/configs/body_2d_keypoint/rtmpose/aihub/rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed.py
MODEL_CHECKPOINT_PATH=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/best_coco_AP_epoch_78.pth
INPUT_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
TEST_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
WORK_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx
DEVICE=cpu
CALIB_DATA_CFG=None

python3 ${MMDEPLOY_DIR}/tools/deploy.py \
${DEPLOY_CFG_PATH} \
${MODEL_CFG_PATH} \
${MODEL_CHECKPOINT_PATH} \
${INPUT_IMG} \
--test-img ${TEST_IMG} \
--work-dir ${WORK_DIR} \
--calib-dataset-cfg ${CALIB_DATA_CFG} \
--device ${DEVICE} \
--log-level INFO \
--show \
--dump-info
```

make tensorrt
```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
MMPOSE_DIR=/home/jglee/projects/mmpose
DEPLOY_CFG_PATH=${MMDEPLOY_DIR}/configs/mmpose/pose-detection_simcc_onnxruntime-fp16_dynamic.py
MODEL_CFG_PATH=${MMPOSE_DIR}/configs/body_2d_keypoint/rtmpose/aihub/rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed.py
MODEL_CHECKPOINT_PATH=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/best_coco_AP_epoch_78.pth
INPUT_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
TEST_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
WORK_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx16
DEVICE=cuda:0
CALIB_DATA_CFG=None

python3 ${MMDEPLOY_DIR}/tools/deploy.py \
${DEPLOY_CFG_PATH} \
${MODEL_CFG_PATH} \
${MODEL_CHECKPOINT_PATH} \
${INPUT_IMG} \
--test-img ${TEST_IMG} \
--work-dir ${WORK_DIR} \
--calib-dataset-cfg ${CALIB_DATA_CFG} \
--device ${DEVICE} \
--log-level INFO \
--show \
--dump-info
```

profiling
```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
MMPOSE_DIR=/home/jglee/projects/mmpose
cd ${MMDEPLOY_DIR}
DEPLOY_CFG_PATH=${MMDEPLOY_DIR}/configs/mmpose/pose-detection_simcc_onnxruntime_dynamic.py
MODEL_CFG_PATH=${MMPOSE_DIR}/configs/body_2d_keypoint/rtmpose/aihub/rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed.py
WORK_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx
python3 tools/profiler.py \
    ${DEPLOY_CFG_PATH} \
    ${MODEL_CFG_PATH} \
    /mnt/sdb1/datasets/qed_pose_eval/coco_format/images \
    --model ${WORK_DIR}/end2end.onnx \
    --shape 256x192 \
    --device cuda:0 \
    --batch-size 1 \
    --warmup 50 \
    --num-iter 200
```
rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed 
| batch size  | Latency/ms |   FPS   | 
|  1  |   5.275    | 189.561 |
|  32  |   0.767    | 1303.665 |
|  64  |   0.644    | 1552.171 |
|  128  |   0.62    | 1612.27 |

```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
MMPOSE_DIR=/home/jglee/projects/mmpose
cd ${MMDEPLOY_DIR}
DEPLOY_CFG_PATH=${MMDEPLOY_DIR}/configs/mmpose/pose-detection_simcc_onnxruntime-fp16_dynamic.py
MODEL_CFG_PATH=${MMPOSE_DIR}/configs/body_2d_keypoint/rtmpose/aihub/rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed.py
WORK_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx16
python3 tools/profiler.py \
    ${DEPLOY_CFG_PATH} \
    ${MODEL_CFG_PATH} \
    /mnt/sdb1/datasets/qed_pose_eval/coco_format/images \
    --model ${WORK_DIR}/end2end.onnx \
    --shape 256x192 \
    --device cuda:0 \
    --batch-size 32 \
    --warmup 50 \
    --num-iter 200
```

rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed , RTX A5000
| batch size  | Latency/ms |   FPS   | precision | memory
|  1  |   3.416    | 292.739 | fp32 | 3049MiB
|  32  |   0.636    | 1571.697 | fp32 | 3529MiB
|  32  |   0.39    | 2555.04 | fp16 | 3271MiB
|  64  |   0.644    | 1552.171 | fp32 | 4203MiB
|  128  |   0.62    | 1612.27 | fp32 |  5423MiB
|  128  |    0.44    | 2260.21 | fp16 | 4397MiB


```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
MMPOSE_DIR=/home/jglee/projects/mmpose
DEPLOY_CFG=${MMDEPLOY_DIR}/configs/mmpose/pose-detection_simcc_onnxruntime_dynamic.py
MODEL_CFG=${MMPOSE_DIR}/configs/body_2d_keypoint/rtmpose/aihub/rtmpose-m_8xb256-105e_aihub_coco-256x192_bugfix_qed.py
BACKEND_MODEL_FILES=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx/end2end.onnx
DEVICE=cuda:0
WORK_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx
OUTPUT_IMAGE_DIR=/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8/onnx/images
INTERVAL=10
BATCH_SIZE=32
python3 ${MMDEPLOY_DIR}/tools/test.py \
    ${DEPLOY_CFG} \
    ${MODEL_CFG} \
    --model ${BACKEND_MODEL_FILES} \
    --device ${DEVICE} \
    --work-dir ${WORK_DIR} \
    --show-dir ${OUTPUT_IMAGE_DIR} \
    --interval ${INTERVAL} \
    --speed-test \
    --batch-size ${BATCH_SIZE}
```

```shell
cd /Users/sweaterr/Models/mmpose/rtmpose_aihub_coco
rsync -avz -e "ssh -p 22554" jglee@61.74.163.66:/mnt/sdb1/models/mmpose/rtmpose_aihub_coco/m8 .
```