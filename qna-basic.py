print("Hello")
from langchain import PromptTemplate, LLMChain
from langchain.llms import VertexAI

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = VertexAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))
