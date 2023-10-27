# falcon-langchain

## Create a HuggingFace API key

Create a HuggingFace API key by following the instructions [here](https://huggingface.co/docs/hub/adding-a-file-to-a-model).
export HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

If you want to use .envrc. Add below in `.envrc`

```
export HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## Create a Conda environment 

```
conda env create langchain  python=3.10 -c conda-forge

conda activate langchain
```

## Install the required Python packages by running the following command in your terminal:
```
pip install -r requirements.txt
```

## Run the following command in your terminal to start the chat UI:

```
chainlit run app.py -w
```

This will launch the chat UI, allowing you to interact with the Falcon LLM model using LangChain.