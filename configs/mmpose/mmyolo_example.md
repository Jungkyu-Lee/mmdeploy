```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
DEPLOY_CFG_PATH=/home/jglee/projects/mmyolo/configs/deploy/detection_onnxruntime_dynamic.py
MODEL_CFG_PATH=/home/jglee/projects/mmyolo/train_aihub/m3/rtmdet_nano_syncbn_fast_8xb32-300e_coco.py
MODEL_CHECKPOINT_PATH=/home/jglee/projects/mmyolo/train_aihub/m3/epoch_295.pth
INPUT_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
TEST_IMG=/mnt/sdb1/datasets/qed_pose_eval/coco_format/images/982164601.png
WORK_DIR=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx
DEVICE=cpu
CALIB_DATA_CFG=None

python ${MMDEPLOY_DIR}/tools/deploy.py ${DEPLOY_CFG_PATH} ${MODEL_CFG_PATH} ${MODEL_CHECKPOINT_PATH} ${INPUT_IMG} \
--test-img ${TEST_IMG} \
--work-dir ${WORK_DIR} \
--calib-dataset-cfg ${CALIB_DATA_CFG} \
--device ${DEVICE} \
--log-level INFO \
--show \
--dump-info
```

```shell
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
DEPLOY_CFG=/home/jglee/projects/mmyolo/configs/deploy/detection_onnxruntime_dynamic.py
MODEL_CFG=/home/jglee/projects/mmyolo/configs/rtmdet/aihub/rtmdet_nano_syncbn_fast_8xb32-300e_coco_4gpu.py
BACKEND_MODEL_FILES=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx/end2end.onnx
DEVICE=cuda:0
WORK_DIR=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx
OUTPUT_IMAGE_DIR=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx/images
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
MMDEPLOY_DIR=/home/jglee/projects/mmdeploy
DEPLOY_CFG=/home/jglee/projects/mmyolo/configs/deploy/detection_onnxruntime_dynamic.py
MODEL_CFG=/home/jglee/projects/mmyolo/configs/rtmdet/aihub/rtmdet_nano_syncbn_fast_8xb32-300e_coco_4gpu.py
BACKEND_MODEL_FILES=/home/jglee/projects/mmyolo/train_aihub/m3/onnx/det_nano_300epoch_batch90.onnx
DEVICE=cuda:0
WORK_DIR=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx
OUTPUT_IMAGE_DIR=/home/jglee/projects/mmyolo//home/jglee/projects/mmyolo/train_aihub/m3/onnx/images
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
