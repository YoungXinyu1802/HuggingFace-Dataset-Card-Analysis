---
license: mit
---
# Mainfest
- CMeEE_train.json: 训练集 
- CMeEE_dev.json: 验证集
- CMeEE_test.json: 测试集
  - 提交的时候需要为每条记录填充"entities"字段，类型为列表。每个识别出来的实体必须包含"start_idx", "end_idx", "type"3个字段。
  - 提交的文件名为：CMeEE_test.json
- example_gold.json: 标准答案示例
- example_pred.json: 提交结果示例

评估指标以严格Micro-F1值为准