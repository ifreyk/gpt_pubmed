#%%
from undetected_chromedriver import Chrome, ChromeOptions
import g4f
from g4f.Provider import (
    Bard,
    Poe,
    AItianhuSpace,
    MyShell,
    PerplexityAi,
    GPTalk
)
#%%
class OpenAiManager:
    """
    Class for GPT communication
    """
    def __init__(self):
        pass
    def choose_provider(self,provier_my):
        providers_dict = {'GPTalk':g4f.Provider.GPTalk,
                          'MyShell':g4f.Provider.MyShell,
                          'ChatBase':g4f.Provider.ChatBase,
                          'FakeGpt':g4f.Provider.FakeGpt,
                          'FreeGpt':g4f.Provider.FreeGpt,
                          'Hashnode':g4f.Provider.Hashnode}
        return providers_dict[provier_my]
    def open_web(self):
        self.options = ChromeOptions()
        self.options.add_argument("--incognito");
        self.webdriver = Chrome(options=self.options, headless=True)
    def chatgpt_client(self,text,question,provider_my='GPTalk'):
        """Answers questions about the selected article 

        Args:
            text (str): Article full text or abstract
            question (str): Question
            provider (str, optional): Prover to run gpt on. Defaults to GPTalk. List of Providers [GPTalk,PerplexityAi,MyShell]. Others here https://github.com/xtekky/gpt4free/tree/main

        Returns:
            str: Answer to your question
        """
        provider = self.choose_provider(provider_my)
        try:
            completion = g4f.ChatCompletion.create(temperature=0.5,
            model=g4f.models.default,
            provider=provider,
            webdriver=self.webdriver,
            timeout=120,
            messages=[{"role": "system", "content": "You are Molecular Biologist you will need to answer the few questions only according to article information"},
                        {"role": "user", "content": f'Here is the article.\n {text}.Here is the questions {question}'}])
            
            return completion
        except Exception as e:
            print(e)
            return 'Error'
    def close_web(self):
        self.webdriver.quit()
