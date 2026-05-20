import numpy as np
from sklearn.metrics import classification_report
from transformers import Trainer

# assumes you already trained model + dataset

preds = trainer.predict(dataset["validation"])

y_pred = np.argmax(preds.predictions, axis=1)
y_true = preds.label_ids

print(classification_report(y_true, y_pred))