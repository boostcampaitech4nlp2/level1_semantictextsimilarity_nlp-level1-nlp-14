# Score 기록

### Base line code 
- epoch 1 : 0.7284
- epoch 50 : 0.8681

### Base line + Correlation Loss
- epoch 30 : 0.8741

### Model selection + hyperparameter searching
- roberta-large
    - batch_size 32, max_length 175, max_epoch 20, L1 loss
        - 0.9057
- koelectra-base-v3-discriminator
    - batch_size 8, max_length 175, max_epoch 20, Corr loss
        -0.9119
