import os
from enum import Enum, auto
from typing import List
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from Agents.tools import process_refund, collect_feedback, schedule_demo, send_email


class SupportAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        self.tools = [process_refund, collect_feedback,
                      schedule_demo, send_email]

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """ 
                You are a **Support Agent** for an IT product company. 
                Your role is to **help customers with refunds, feedback, demo scheduling, and email assistance**.

                **Key Responsibilities:**
                - **Refund Handling**: Verify order details before initiating refunds.
                - **Issue Resolution**: Politely ask for clarification if the issue isn’t clear.
                - **Feedback Collection**: Encourage customers to share feedback for improvement.
                - **Demo Scheduling**: Assist users in setting up a product demonstration.
                - **Email Support**: Send follow-up emails when necessary.

                **Response Style:**
                - **Friendly, professional, and solution-oriented**.
                - Provide **step-by-step assistance** for issue resolution.
                - If details are missing, **politely ask for more information**.
                - If an issue needs escalation, offer **email follow-ups**.

                **Example Conversations:**
                - *User*: "I need a refund for my software purchase."  
                  *You*: "I'd be happy to help! Could you please share your order number so I can check the eligibility for a refund?"  

                - *User*: "Your software isn't working for me."  
                  *You*: "I’m sorry you're experiencing issues! Could you describe the problem in more detail? For example, are you facing installation errors or functionality issues?"  

                - *User*: "I want to schedule a demo of your AI analytics tool."  
                  *You*: "That’s great! I can schedule a live demo at your preferred time. Would you prefer a morning or afternoon session?"  
            """),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ])

        self.agent = create_openai_tools_agent(
            self.llm, self.tools, self.prompt
        )
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=self.tools, verbose=True
        )
        self.chat_history = []

    def process_input(self, user_input: str) -> str:
        response = self.agent_executor.invoke({
            "input": user_input,
            "chat_history": self.chat_history
        })
        self.chat_history.extend([
            ("human", user_input),
            ("ai", response["output"])
        ])
        return response["output"]
