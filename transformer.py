import pandas as pd
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


class Transformer:
    """
    Transformer class generates transformation code usind OpenAI 
    """
    def __init__(self):
        None
    
    def read_csv(csv):
        try:
            csv = pd.read_csv(csv)
            return csv
        except Exception as e:
            return str(e)
    
    def run_llmchain(llm,prompt,args):
        try:
            chain = LLMChain(llm=llm,prompt=prompt)
            return chain.run(args)
        except Exception as e:
            return str(e)
    