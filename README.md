# amdox-ai-task-optimizer
AI-powered decision support system that detects employee emotions using text and facial expressions to recommend suitable tasks with a privacy-first approach.


## Current Progress
- Project scope frozen (Text + Facial emotions)
- Folder structure finalized
- Emotion labels unified across modalities
- Text emotion preprocessing pipeline implemented

## Text Emotion Model – Design (Day 2)

### Preprocessing
- Lowercasing
- Noise removal (URLs, special characters)
- Stopword removal
- Lemmatization (not stemming)

### Feature Extraction
- TF-IDF Vectorization
- ngram_range = (1, 2) to capture context
- max_features = 5000 to avoid curse of dimensionality
- min_df = 2, max_df = 0.9 for noise control

### Model Choice
- Logistic Regression
- Chosen for interpretability and probabilistic output

### Confidence Score
- Derived from predict_proba
- Max class probability used as confidence
- Enables multi-modal emotion fusion later
