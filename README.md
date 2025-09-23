# cits4012-group

## Timeline (Working chronologically)
1. September 22 11:59 PM : Complete preprocessing of dataset
2. September 26 11:59 PM : Train Model 1 (BiLSTM + Pool)
3. September 29 11:59 PM : Train Model 2 (BiLSTM + Attention)
4. October 2 11:59 PM : Train Model 3 (Transformer)
5. October 5 11:59 : Abalation studies
6. October 15 11:59 : Report


Objective
	•	Task: Natural Language Inference (NLI) for science questions.
	•	Input: premise (web sentences) + hypothesis (from exam Q&As).
	•	Output: classify as `entails` or `neutral`.
	•	Focus: RESEARCH PROCESS, not just accuracy.

Dataset
	•	Provided: train.json, val.json, test.json.
	•	Created formatted version for better readability: suffix `_formatted.json`
	•	Created mini versions of the dsets for quick research: suffix `_mini_ds.json`
	
Report Requirements (max 5 pages, ACL format, LaTeX only)
	1.	Title – project title + group number.
	2.	Abstract – <300 words: motivation, aims, contributions, findings.
	3.	Introduction – problem significance, difficulties, applications, overview of approach/results.
	4.	Methods –
	•	Design 3 substantially different models (e.g., RNN vs Transformer, not just RNN vs LSTM).
		•	First model is LSTM with Bi-Direction
		•	Second model is Transformers (this has attention mechanism)
	•	At least one with attention (novel application encouraged). 
		[ ] Transformer model by adding pooling or something 
	•	Equations, notations, architecture diagrams.

	•	Justification of design.
	5.	Experiment Setup – dataset analysis, implementation details (config, hyperparameters, training setup).
	6.	Results –
	•	Performance comparison of models.
	•	Ablation study on attention (positions/types).
	•	One more ablation study (hyperparams, pooling, etc.).
	7.	Qualitative Results – visualize attention weights on sample predictions; interpret them.
	8.	Conclusion – findings, achievements, limitations, future work.
	9.	Team Contribution – who did what (outside page limit).
	10.	References – BibTeX.

# Dataset Specification
## Train Dset
 - 23087
 - mini: 2000 
## Test Dset
 - 2125
 - mini: 200
## Validation Dset
 - 1303
 - mini: 120



# Cleaning
Handling Missing Data: Identify and handle any missing or incomplete data. This might involve removing entries with missing fields or filling in missing values if appropriate.
Text Normalization: Normalize the text data to reduce variability. This can include converting text to lowercase, removing punctuation, and handling contractions.
Removing Duplicates: Check for and remove any duplicate entries in the dataset to ensure that the model is not biased by repeated data.
Balancing the Dataset: Ensure that the dataset is balanced in terms of the classes (entails and neutral). If one class is overrepresented, consider techniques like undersampling, oversampling, or generating synthetic data to balance the classes.
Noise Reduction: Remove any irrelevant or noisy data that might not contribute to the task. This could include very short sentences, non-informative text, or entries with a lot of noise.
Tokenization and Lemmatization: Consider tokenizing the text and applying lemmatization or stemming to reduce words to their base or root form, which can help in reducing dimensionality.
