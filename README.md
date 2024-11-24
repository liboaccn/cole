
# CoLE: A Collaborative Legal Expert Prompting Framework for Large Language Models in Law
## Overview

This repository contains the code and datasets used in our research paper on CoLE: A Collaborative Legal Expert Prompting Framework for Large Language Models in Law.
## Code

To run the main script, use the following command:
```bash
python main.py -d JQA -t 0.6 -c 0
```
**Note**: We have only open-sourced part of the code. The remaining code will be gradually released.



## Datasets

We evaluate CoLE on large-scale publicly available benchmark datasets of LLM in laws, along with our self-built dataset. The datasets include:

- **CAIL2018 (C18)**: Contains 500 single-selection questions, sourced from the open dataset of the China Law Research Cup 2018 Judicial Artificial Intelligence Challenge.
- **CAIL2019 (C19)**: Contains 500 multiple-selection questions, sourced from the China Law Research Cup 2019 Judicial Artificial Intelligence Challenge.
- **CAIL2022 (C22)**: Includes 500 single-selection questions, sourced from the China Law Research Cup 2022 Judicial Artificial Intelligence Challenge open dataset.
- **CrimeKgAssitant (CA)**: Contains 500 single-selection questions from the Crime Assistant, including crime type prediction and crime consult service based on NLP methods and crime KG.
- **JEC_QA (JQA)**: Includes 500 single-selection questions, sourced from the National Judicial Examination of China.
- **LAW_GPT (LG)**: Contains 500 legal Q&A questions, sourced from the large legal model LAW_GPT’s open dataset on GitHub.
- **LawLLM (LM)**: Contains 300 legal Q&A questions, sourced from the large legal model LawLLM’s open dataset on HuggingFace.
- **HanFei (HF)**: Includes 11,098 legal Q&A questions, sourced from the large legal model HanFei’s open dataset on GitHub.
- **Lawyer-LLaMA (LLA)**: Includes 21,476 legal Q&A questions, sourced from the large legal model Lawyer-LLaMA’s open dataset on HuggingFace.
