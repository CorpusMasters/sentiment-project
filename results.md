

# Sentiment Classification using Fine-Tuned BERT

## Model
bert-base-uncased fine-tuned using Hugging Face Transformers

## Task
5-class sentiment classification:
- 0: negative
- 1: positive
- 2: neutral
- 3: sarcastic
- 4: mixed

## Dataset
TSV dataset:
- Train: 2062 samples
- Validation: 272 samples
- Test: 276 samples

## Training Setup
- Model: BERT (bert-base-uncased)
- Epochs: 3
- Optimizer: AdamW (default Trainer settings)
- Loss: Cross-entropy
- Batch size: default Trainer configuration

## Results

### Accuracy
0.7355 (73.55%)

### Classification Report

- Class 0: precision 0.00, recall 0.00, F1 0.00 (support: 3)
- Class 1: precision 0.74, recall 0.69, F1 0.71 (support: 93)
- Class 2: precision 0.00, recall 0.00, F1 0.00 (support: 28)
- Class 3: precision 0.74, recall 0.92, F1 0.82 (support: 151)
- Class 4: precision 0.00, recall 0.00, F1 0.00 (support: 1)

### Confusion Matrix

[[ 0 0 0 3 0]
[ 0 64 0 29 0]
[ 0 10 0 18 0]
[ 0 12 0 139 0]
[ 0 1 0 0 0]]


## Observations
- The model performs well on majority classes (1 and 3).
- Minority classes (0, 2, 4) are not learned well due to class imbalance.
- The dataset is highly imbalanced, which affects macro F1-score.
- Model is biased toward majority classes.

## Conclusion
A BERT-based classifier was successfully fine-tuned on a 5-class sentiment dataset. While overall accuracy is 73.55%, performance is limited by class imbalance. Future improvements could include class weighting, oversampling, or merging rare classes.