#%%
from utils_my.preprocesser import PubMedSearcher
from config.config import PubmedSearcherConfig,GptConfig
from utils_my.gpt_manager import OpenAiManager
import pandas as pd
import g4f
from tqdm import tqdm
import numpy as np
import time
import os
#%%
cfg = PubmedSearcherConfig(query='rapamycin in aging',num_of_articles=10,email='erik69725@gmail.com')
pubmed = PubMedSearcher(cfg)
pubmed.run_basic_preproc()
#%%
df = pubmed.articles_df
#%%
gpt = OpenAiManager()
gpt.open_web()
gpt.chatgpt_client(df.loc[0,'text_from_pmc'],'Is rapamycin increasing lifespan write probability of that is the true from 0 to 1?',provider_my='FakeGpt')
gpt.close_web()