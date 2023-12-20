#%%
import pandas as pd
from metapub import PubMedFetcher
from tqdm import tqdm
from Bio import Entrez, Medline
import pubmed_parser as pp
import json
import os
import time
import numpy as np
#%%
class PubMedSearcher:
    def __init__(self,cfg):
        self.query = cfg.query
        self.num_of_articles = cfg.num_of_articles
        self.folder_to_save = cfg.folder_to_save
        self.fetch = PubMedFetcher()
        self.email = cfg.email
        Entrez.email = self.email
    def get_articles(self):
        """Get list of PMIDs to your query
        """
        handle = Entrez.esearch(
            db="pubmed",
            term=self.query,
            retmax=self.num_of_articles,
            usehistory="y",
            prefix="xlink",
            sort='relevance'
        )
        search_results = Entrez.read(handle)
        handle.close()
        self.pmids = search_results["IdList"]
    def get_basic_information(self,pmid):
        """Get basic information for exact PMID
        """
        time.sleep(10)
        article_dict = {}
        article = self.fetch.article_by_pmid(pmid)
        article_dict['pmid'] = article.pmid
        article_dict['Title'] = article.title
        article_dict['url'] = article.url
        article_dict['pmc'] = article.pmc
        article_dict['year'] = article.year
        return article_dict
    def get_abstract_from_pmid(self,pmid):
        """Get abstract for exact PMID
        """
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
        record = Medline.read(handle)
        print(record)
        abstract = record.get('AB', None)
        handle.close()
        return abstract
    def download_free_articles(self,pmc):
        """Download articles and full text from PMCID
        """
        if pd.isnull(pmc):
            return None
        else:
            time.sleep(5)
            try:
                    ### take a paper xml
                handle = Entrez.efetch(db="pmc", id=pmc, rettype="full", retmode="xml")
                    ###
                xml_path = os.path.join(self.folder_to_save, pmc + ".xml")
                    # save xml
                with open(xml_path, "w") as f:
                    f.write(handle.read().decode("utf-8"))

                dict_meta = pp.parse_pubmed_xml(xml_path)
                dict_par = pp.parse_pubmed_paragraph(xml_path)

                meta_path = os.path.join(self.folder_to_save, pmc + ".meta.json")
                text_path = os.path.join(self.folder_to_save, pmc + ".txt")

                    ### save a paper meta info
                with open(meta_path, "w") as fp:
                    json.dump(dict_meta, fp)
                    ### save a paper text
                full_text = "\n".join([p["text"] for p in dict_par])
                with open(text_path, "w") as fp:
                    fp.write(full_text)
                handle.close()
                return full_text
            except Exception:
                print(f'{pmc} not found')
                return None
    def run_basic_preproc(self):
        """Run full pipeline for your query
        """
        self.get_articles()
        self.articles_df = pd.json_normalize([self.get_basic_information(x) for x in tqdm(self.pmids)])
        self.articles_df['abstract_from_pmid'] = [self.get_abstract_from_pmid(x) for x in self.articles_df['pmid']]
        self.articles_df['text_from_pmc'] = [self.download_free_articles(x) for x in self.articles_df['pmc']]