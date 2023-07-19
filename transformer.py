import pandas as pd
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


class Transformer:
    """
    Transformer class generates transformation code usind OpenAI 
    """
    def __init__(self):
        self.template_columns = None 
        self.source_columns = None
    
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
    
    def generate_transformations(self,template_upload,csv_upload,openai_api_key):
        template = self.read_csv(template_upload)
        source = self.read_csv(csv_upload)
        
        self.template_columns = template.columns.tolist()
        self.source_columns = source.columns.tolist()
        
