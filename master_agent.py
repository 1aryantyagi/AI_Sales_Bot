# master_agent.py
from enum import Enum
from langchain_openai import ChatOpenAI
from sales_agent import SalesAgent
from support_agent import SupportAgent
from technical_agent import TechnicalAgent
from billing_agent import BillingAgent


class MasterAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        self.agents = {
            "sales": SalesAgent(),
            "support": SupportAgent(),
            "technical": TechnicalAgent(),
            "billing": BillingAgent()
        }
        self.current_agent = "sales"

    def classify_intent(self, user_input: str) -> str:
        prompt = f"""Classify the user message into one category:
        - sales: Product questions, purchasing, demos
        - support: Returns, feedback, issues
        - technical: Compatibility, installation, requirements
        - billing: Payments, refunds, invoices
        
        Message: {user_input}
        Category:"""
        response = self.llm.invoke(prompt)
        return response.content.strip().lower()

    def process_input(self, user_input: str) -> str:
        new_agent = self.classify_intent(user_input)
        self.current_agent = new_agent if new_agent in self.agents else "sales"
        return self.agents[self.current_agent].process_input(user_input)
