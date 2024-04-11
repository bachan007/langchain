import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


prompt = ChatPromptTemplate.from_messages(
    [
        ('system','''You are an expert in the Financial Domain.
         You can think of you as an economical expert, finance professor, economical advisor or financial expert.
         You posses all the expert advice regarding the finance or economic domain.
         On the basis of your expert nature, you will answer the queries.'''),
         ('user','Question:{question}')
    ]
)

llm = Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

input_text = '''
The economic domain refers to the study of the production, distribution, and consumption of goods and services in an economy. It encompasses a wide range of topics, 
including:

1. Microeconomics: The study of individual economic units such as households, firms, and markets. It examines the behavior of consumers and firms, and how they interact 
in markets to determine prices and allocate resources.
2. Macroeconomics: The study of the economy as a whole, including topics such as inflation, unemployment, economic growth, and international trade.
3. International Trade: The study of the exchange of goods and services between different countries. It examines the reasons why countries engage in international trade, 
the effects of trade on the economy, and the policies that governments use to regulate trade.
4. Development Economics: The study of economic development and growth in low-income countries. It explores the factors that influence economic development, including 
institutions, infrastructure, human capital, and foreign aid.
5. Public Finance: The study of how governments raise revenue and allocate resources to meet public expenditures. It examines the different taxation systems, government 
spending priorities, and the impact of government policies on economic growth and stability.
6. Labor Economics: The study of the labor market and the behavior of workers and employers. It explores topics such as wage determination, labor productivity, and the 
impact of labor market institutions on economic outcomes.
7. Environmental Economics: The study of the economic impact of environmental policies and the value of natural resources. It examines the economic costs and benefits of 
pollution control, climate change mitigation, and other environmental policies.
8. Health Economics: The study of the economic factors that influence health outcomes and the allocation of healthcare resources. It explores topics such as the 
cost-effectiveness of medical interventions, the impact of health insurance on access to care, and the role of government in regulating the healthcare market.
9. Technology and Innovation Economics: The study of the economic impact of technological change and innovation. It explores topics such as the diffusion of new 
technologies, the impact of R&D investments on productivity growth, and the role of intellectual property rights in promoting innovation.
10. Behavioral Economics: The study of how psychological, social, and emotional factors influence economic decisions. It explores topics such as the role of cognitive 
biases in consumer choice, the impact of social norms on behavior, and the use of behavioral insights in policy design.

These are just a few examples of the many subfields within economics. Each subfield approaches the study of economic phenomena from a different perspective, providing a 
more comprehensive understanding of the complex interactions within an economy.

Read the above paragrapgh and answer the question:

1. Can you explain the difference between positive and normative economics?
2. How does macroeconomics differ from other social sciences such as politics or sociology in terms of its methodology and scope?
3. What is the role of institutional factors in determining economic outcomes, according to development economics?
'''


print(chain.invoke({'question':input_text}))