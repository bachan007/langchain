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
         On the basis of your expert nature, you will need to question on the basis of the information provided to you.
         Once you get the answer you need to understand the answer and if you have any further query then again ask the question.
         Or if you are satisfied with the answer, just read the information provided to you again and ask other question.
         By this way you will prove your intelligence of questioning and improve the answering capabilities.'''),
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

Read the above paragrapgh and ask the question, Whatever you feel necessary, you can ask in the form of question and 
you do not need to provide the answer, only oce question at a time.
'''

first_question = '''
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

your first question was : What is the difference between microeconomics and macroeconomics?
and you got the answer : Microeconomics focuses on the behavior and decision-making of individual economic units such as households, firms, and markets. It examines how these entities interact in markets to determine prices and allocate resources. Microeconomics looks at the supply and demand for goods and services, the determination of prices, and the impact of external factors like government policies or technological changes on economic outcomes.

On the other hand, macroeconomics is concerned with the overall performance of an economy, including topics such as inflation, unemployment, economic growth, and international trade. Macroeconomics examines how these aggregate economic variables are determined and how they interact to shape the overall performance of an economy. It looks at factors like GDP, inflation rate, employment rates, and balance of payments to understand the health of an economy.

In summary, microeconomics studies individual economic units and their behavior within markets, while macroeconomics examines the overall performance of an economy and the interactions between different variables that affect it. While microeconomics focuses on the micro aspects of the economy, macroeconomics looks at the big picture and how all the different components work together to shape economic outcomes.

You again asked the questions :
1. Can you explain the difference between positive and normative economics?
2. How does macroeconomics differ from other social sciences such as politics or sociology in terms of its methodology and scope?
3. What is the role of institutional factors in determining economic outcomes, according to development economics?

and you got the answers :
Of course! I'd be happy to help you with your questions.

1. Positive economics focuses on understanding how things work in the economy and the underlying causes of different economic phenomena, without making value judgments or recommendations. It is concerned with describing the world as it is rather than advocating for a particular policy or outcome. For example, positive economics might study the relationship between tax rates and government revenue, but it would not tell you whether a higher or lower tax rate is desirable.

Normative economics, on the other hand, involves making value judgments and recommending policies based on ethical or moral considerations. It is concerned with what should be rather than how things are. For example, normative economics might advocate for a particular tax rate based on its impact on income inequality or economic growth.

2. Macroeconomics differs from other social sciences such as politics or sociology in terms of its methodology and scope. Macroeconomics is concerned with the study of the economy as a whole, including topics such as inflation, unemployment, economic growth, and international trade. Its methodology involves using statistical methods and econometric techniques to analyze large-scale economic phenomena.

In contrast, politics and sociology are more focused on the study of individual actors and their interactions within society. While these fields may overlap with macroeconomics in terms of topics studied, they approach them from a different perspective and use different methodologies. For example, political science might study the impact of government policies on economic outcomes using case studies or comparative analysis, while sociology might examine how social norms and institutions shape economic behavior using qualitative methods.

3. Institutional factors play a crucial role in determining economic outcomes according to development economics. These factors include the legal system, political stability, property rights, and the quality of governance. Development economics argues that these institutional factors can significantly impact economic growth and development by influencing investment decisions, innovation, and the allocation of resources.

For example, a strong legal system can encourage investment by providing protection for property rights and promoting contract enforcement. Similarly, political stability can attract foreign investment and promote economic growth. On the other hand, weak institutions can hinder economic development by discouraging investment and undermining trust in the economy.

In conclusion, positive economics focuses on understanding how things work in the economy without making value judgments or recommendations, while normative economics involves making value judgments and recommending policies based on ethical or moral considerations. Macroeconomics differs from other social sciences such as politics or sociology in terms of its methodology and scope, with a focus on the study of the economy as a whole using statistical methods and econometric techniques. Finally, institutional factors play a crucial role in determining economic outcomes according to development economics, influencing investment decisions, innovation, and the allocation of resources through their impact on property rights, political stability, and governance quality.

Read the above paragrapgh and ask the question, Whatever you feel necessary, you can ask in the form of question and 
you do not need to provide the answer, only oce question at a time.
'''

# print(chain.invoke({'question':input_text}))
print(chain.invoke({'question':first_question}))