# Consumer-to-Shop-Clothing-Retrieval-Using-Deep-Learning
This is a repository of Consumer-to-Shop Clothing Retrieval Using Deep Learning project in 2025-2, Computer Vision, Ewha Womans University. 

This project addresses the Consumer-to-Shop (C2S) fashion image retrieval problem by formulating it as a metric learning–based retrieval task. Using a sampled subset of the DeepFashion C2S dataset, we construct an embedding-based retrieval pipeline and analyze the impact of backbone selection, loss functions, and preprocessing strategies. EfficientNet-B3 with Batch-Hard Triplet Loss achieves the best overall performance among the tested configurations. We further demonstrate that careful preprocessing design and embedding dimension selection improve retrieval performance without modifying the model architecture. The final model achieves Recall@1, Recall@5 and Recall@10 of 0.6402, 0.7280 and 0.7751 on the test set, highlighting the importance of embedding design in consumer-to-shop fashion retrieval.

## Repository Structure

This repository is organized to clearly separate **intermediate experiments** from the **final demo used for evaluation**.

- **01_data/**  
  Scripts and artifacts related to dataset construction, filtering, and sampling.  

- **02_preprocessing/**  
  Exploratory notebooks and experiments on basic preprocessing strategies(stage1), and advanced preprocessing stategies after model selection including normalization, data augmentation, and domain gap analysis.

- **03_model_experiments/**  
  Model comparison and ablation experiments conducted during development, such as backbone selection and loss function exploration.

- **04_demo/**  
  **Final demo folder for evaluation.**  
  This directory contains the cleaned and finalized notebook(s) required to reproduce the final quantitative results and qualitative retrieval demo.  
  **Only this folder is needed to run the final Consumer-to-Shop retrieval demo.**

- **reports/**  
  Final report and presentation materials.
