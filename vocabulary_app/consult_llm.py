from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
#from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def translate_with_llm(word):
    template = """Como se dice "{frase}" en ingles? Tu respuesta debe ser un objeto de python con la siguiente estructura:
    (signo de llave de apertura)'palabra a traducir' : 'palabra traducida'(signo de apertura de cierre)
    Solo debes responder con la estructura antes descrita, nada mas.
    """

    llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
    prompt_template = PromptTemplate(input_variables=["frase"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    respuesta = chain.invoke(input={
        "frase": word,
    })

    return respuesta['text']
        

while True:
    word = translate_with_llm(input("Insert a word: "))
    print(word)