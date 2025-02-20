CUDA_VISIBLE_DEVICES=0 swift deploy \
    --model /home/jiangqiushan/Q/output/Qwen2.5-1.5B-Instruct/v10-20250219-172622/checkpoint-4250 \
    --infer_backend vllm \
    --served_model_name MathR-Distill-Qwen2.5-7B-Instruct \
    --gpu-memory-utilization 0.9 \
    --port 8801
