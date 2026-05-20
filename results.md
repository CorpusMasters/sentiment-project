\#  Sentiment Classification Results (BERT Fine-Tuning)



\## Model Details

\- Base model: bert-base-uncased

\- Fine-tuning method: Hugging Face Trainer (Supervised Fine-Tuning)

\- Number of classes: 5 (0–4)

\- Epochs: 3

\- Dataset: Custom sentiment dataset



\---



\##  Performance Metrics



\### Accuracy

\*\*Accuracy: 0.7355 (\~73.6%)\*\*



\---



\### Precision, Recall, F1-Score



| Class | Precision | Recall | F1-score | Support |

|------|----------|--------|----------|---------|

| 0 | 0.00 | 0.00 | 0.00 | 3 |

| 1 | 0.74 | 0.69 | 0.71 | 93 |

| 2 | 0.00 | 0.00 | 0.00 | 28 |

| 3 | 0.74 | 0.92 | 0.82 | 151 |

| 4 | 0.00 | 0.00 | 0.00 | 1 |



\---



\##  Confusion Matrix





\[\[ 0 0 0 3 0]

\[ 0 64 0 29 0]

\[ 0 10 0 18 0]

\[ 0 12 0 139 0]

\[ 0 1 0 0 0]]





\---



\##  Observations



\- The model performs well on class \*\*1 and 3\*\*, which dominate the dataset.

\- Classes \*\*0, 2, and 4 are never correctly predicted\*\*, indicating strong class imbalance.

\- The model is biased toward majority classes.

\- Recall for class 3 is high (0.92), showing strong learning for dominant patterns.



\---



\##  Limitations



\- Dataset is imbalanced

\- Small number of samples in minority classes

\- No advanced hyperparameter tuning applied



\---



\##  Possible Improvements



\- Apply class weighting or oversampling

\- Tune learning rate and batch size

\- Train for more epochs

\- Use stratified sampling

