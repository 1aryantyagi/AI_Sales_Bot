import os
from enum import Enum, auto
from typing import List
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from Agents.tools import (
    get_product_info,
    generate_stripe_payment_link,
    check_mindware_compatibility,
    schedule_demo
)


class SalesAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        self.tools = [
            get_product_info,
            generate_stripe_payment_link,
            check_mindware_compatibility,
            schedule_demo
        ]
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a sales agent for Mindware Solutions. Focus on product info, compatibility checks, and closing sales."),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ])
        self.agent = create_openai_tools_agent(
            self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=self.tools, verbose=True)
        self.chat_history = []

    def process_input(self, user_input: str) -> str:
        response = self.agent_executor.invoke({
            "input": user_input,
            "chat_history": self.chat_history
        })
        self.chat_history.extend(
            [("human", user_input), ("ai", response["output"])])
        return response["output"]
