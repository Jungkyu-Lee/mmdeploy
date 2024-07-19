# _base_ = [
#     './pose-detection_static.py', '../_base_/backends/onnxruntime-fp16.py'
# ]

_base_ = [
    './pose-detection_static.py'
]

backend_config = dict(
    type='onnxruntime',
    precision='fp16',
    common_config=dict(
        # min_positive_val=1e-7,
        # max_finite_val=1e4,
        keep_io_types=False,
        disable_shape_infer=False,
        op_block_list=None,
        node_block_list=None))

onnx_config = dict(
    input_shape=[192, 256],
    output_names=['simcc_x', 'simcc_y'],
    dynamic_axes={
        'input': {
            0: 'batch',
        },
        'simcc_x': {
            0: 'batch'
        },
        'simcc_y': {
            0: 'batch'
        }
    })
