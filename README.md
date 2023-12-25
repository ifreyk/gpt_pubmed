# PubMed Article Downloader and Question Answering
## Introduction
Handling a vast number of articles can be time-consuming to analyze. To address this challenge, you can delegate the article analysis task to a Large Language Model (LLM). The LLM will read the articles and provide answers to your specific questions. This project is designed to streamline the process, replacing traditional search and analysis methods to save valuable time.
This repository provides a tool for downloading articles from PubMed and implementing automatic question-answering based on the content of these articles. The goal is to streamline the process of retrieving relevant scientific literature and extracting valuable information through a question-answering system.
## Results
To address this challenge, you must tackle two key issues: downloading articles from a database and analyzing them using LLM. The **PubMedSearcher** class handles the first task, finding the necessary number of relevant articles based on your search query and downloading the full text for free articles. The second challenge is addressed by the **OpenAiManager** class, which takes the full text of the article or abstract, along with the question you want to answer, and returns the answer to the question.
![image](https://github.com/ifreyk/gpt_pubmed/assets/52207629/ace93127-2320-4fa1-b055-d0dad5ce662e)

### Features
- **preprocesser.py**: Fetch articles from PubMed using queries.
- **gpt_manager.py**: Extract valuable insights from the downloaded articles by posing questions to the system.
### Getting Started
1. Clone the repository:
```
git clone https://github.com/ifreyk/gpt_pubmed.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Open application.py as a notebook:
Follow the code
