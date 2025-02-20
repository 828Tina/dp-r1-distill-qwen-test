from modelscope.msdatasets import MsDataset
ds = MsDataset.load('liucong/Chinese-DeepSeek-R1-Distill-data-110k',
                    subset_name='default', split='train', trust_remote_code=True)

# 打印前5个样本的数据格式
for i, sample in enumerate(ds):
    print(f"Sample {i+1}:")
    print(sample)
    if i >= 1:  # 只打印前5个样本
        break
