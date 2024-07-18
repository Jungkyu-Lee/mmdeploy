import coremltools as ct
from PIL import Image
import numpy as np

import time

def tic():
    return time.time()

def toc(start_time):
    elapsed_time = time.time() - start_time
    return elapsed_time

# Core ML 모델 로드
start_time = tic()
model = ct.models.MLModel('work_dir/mmdet_rtmdet_s_creatz_club/end2end.mlpackage')
elapsed_time = toc(start_time)
print(f"Elapsed time: {elapsed_time} seconds")

# 입력 이미지 로드 및 전처리
start_time = tic()
input_image = Image.open('../mmdetection/demo/test.png').resize((320, 320))
elapsed_time = toc(start_time)
print(f"Elapsed time: {elapsed_time} seconds")
input_array = np.array(input_image).astype(np.float32) / 255.0
reshaped_image = np.expand_dims(np.transpose(input_array[:,:,0:3], (2, 0, 1)), axis=0)
# reshaped_image = np.tile(reshaped_image, (16, 1, 1, 1))

print(reshaped_image.shape)

# 입력 배열을 모델의 입력 형식에 맞게 변환
# input_array = np.transpose(input_array, (2, 0, 1))  # (H, W, C) -> (C, H, W)
# input_array = np.expand_dims(input_array, axis=0)  # (C, H, W) -> (1, C, H, W)

# device = ct..Device.find_available(device_type=ct.DeviceType.GPU)
# print(device)
# print('input_data', input_data['input_1'].shape)
start_time = tic()
# input_name = model.input_description
# print('input_name', input_name)
print('input_image', reshaped_image.shape)
input_data = {'input': reshaped_image}
for _ in range(100):
    output = model.predict(input_data)
elapsed_time = toc(start_time)
# print(output)
print(f"Elapsed time: {elapsed_time} seconds")
print(output)