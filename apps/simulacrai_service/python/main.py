import time
from ctransformers.langchain import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

print("Prompting LLM...")

llm = CTransformers(
    model='./models/guanaco-7B.ggmlv3.q4_0.bin',
    model_type='llama',
    callbacks=[StreamingStdOutCallbackHandler()]
)

prompt = """Convert the following to JSON:
```
name: "John Doe"
age: 42
```
"""
llm(prompt)