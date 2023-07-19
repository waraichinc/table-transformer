import pandas as pd
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


class Transformer:
    """
    Transformer class generates transformation code using OpenAI 
    """
    def __init__(self):
        self.template_columns = None 
        self.template_first_row = None
        self.source_columns = None
        self.source_first_row = None
    
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
        self.template_first_row = template.iloc[0].tolist()
        self.source_columns = source.columns.tolist()
        self.source_first_row = source.iloc[0].tolist()
        
        output = {}

        for col in self.template_columns:
            output[f"source_{col}_format"] = "format of the column in the source user data"
            output[f"template_{col}_format"] = "format of the column in the template data"
            output[f"source_{col}_datatype"] = "data type of the column in the source user data"
            output[f"template_{col}_datatype"] = "data type of the column in the template data"
            output[f"source_{col}_example_data"] = "example data of the column in the source user data"
            output[f"template_{col}_example_data"] = "example data of the column in the template data"
        
        example = """
        {
            "column_renames": {},
            "columns_to_remove": [list of columns to be removed],
            "columns_to_keep": [list of columns to be kept],
            "data_transformations":  %s
        }
        """ % output

        detailed_example = """
        Here column_renames is a mapping of user data columns to template data columns, for example:
        {
            "user_data_column_1": "template_data_column_1",
            "user_data_column_2": "template_data_column_2",
        }

        Here in data_transformations, while computing observe these very carefully:
        {
            "source_col_format": format of the column in the source user data
            "template_col_format": format of the column in the template data,
            "source_col_datatype": data type of the column in the source user data
            "template_col_datatype": data type of the column in the template data
            "source_col_example_data": example data of the column in the source user data
            "template_col_example_data": example data of the column in the template data
        }

        column is the column name in the template data
        """

        prompt = PromptTemplate(
            input_variables=["source_columns", "source_first_row", "template_columns", "template_first_row", "example", "detailed_example"],
            template="""
            Given the following information:

            - User_data columns: {source_columns}
            - User_data example row: {source_first_row}
            - Template_data columns: {template_columns}
            - Template_data example row: {template_first_row}

            Generate a JSON object detailing:

            1. Mapping of user data columns to template data columns (column_renames)
            
            2. Data transformations of format and data type, it also shows the example data of column (data_transformations) [CAUTION: data_transformations should fill all the values. If you don't want to change the format or datatype or firstdata, please fill the same value as the old one.]
            3. Columns to remove or keep (columns_to_remove, columns_to_keep)

            The output should follow JSON format, this is one of the example: {example}
            
            {detailed_example}
            
            """
        )

        llm = ChatOpenAI(model='gpt-3.5-turbo',openai_api_key=openai_api_key,temperature=0.3)
        return self.run_llmchain(llm, prompt, {
            'source_columns': self.source_columns,
            'source_first_row': self.source_first_row,
            'template_columns':self.template_columns,
            'template_first_row':self.template_first_row,
            'example':example,
            'detailed_example':detailed_example
        })
        
    

        
