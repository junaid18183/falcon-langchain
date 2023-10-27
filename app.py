from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain
import chainlit as cl

# question = "Write a Terraform code for creating EKS cluster with 3 nodes"

template = """Question: {question}

Answer: Let's think step by step."""

import os

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')

repo_id = 'tiiuae/falcon-7b-instruct'


llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,repo_id=repo_id, model_kwargs={"temperature": 0.6, "max_new_tokens": 500})


@cl.on_chat_start
async def main():
    # elements = []
    # content = "Hello there, I am Tars. How can I help you?"
    # await cl.Message(content=content, elements=elements).send()
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    cl.user_session.set('llm_chain', llm_chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get('llm_chain')

    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    print(res['text'])

    await cl.Message(content=res['text']).send()