import os
from enum import Enum, auto
from typing import List
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from sales_tools import get_product_info, generate_stripe_payment_link, check_mindware_compatibility


class SalesStage(Enum):
    INTRODUCTION = auto()
    QUALIFICATION = auto()
    VALUE_PROPOSITION = auto()
    NEEDS_ANALYSIS = auto()
    SOLUTION_PRESENTATION = auto()
    OBJECTION_HANDLING = auto()
    CLOSE = auto()
    END = auto()


class SalesAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        self.tools = [get_product_info,
                      generate_stripe_payment_link, check_mindware_compatibility]
        self.stage = SalesStage.INTRODUCTION
        self.chat_history = []

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self._get_stage_prompt()),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ])

        self.agent = create_openai_tools_agent(
            self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=self.tools, verbose=True)

    def _get_stage_prompt(self) -> str:
        stage_prompts = {
            SalesStage.INTRODUCTION: (
                "Hello! I'm Mia from Mindware Solutions. We specialize in enterprise IT solutions "
                "that enhance efficiency and scalability. How can I assist you today?"
            ),
            SalesStage.QUALIFICATION: (
                "Before we proceed, may I know if you're the decision-maker for IT solutions at your company, "
                "or should we involve someone else?"
            ),
            SalesStage.VALUE_PROPOSITION: (
                "Our solutions help businesses reduce costs, enhance security, and improve operational efficiency. "
                "Many clients report a 40% improvement in workflow optimization. What key challenges are you facing?"
            ),
            SalesStage.NEEDS_ANALYSIS: (
                "Tell me more about your current IT setup. What tools do you use? Any pain points you’d like to address?"
            ),
            SalesStage.SOLUTION_PRESENTATION: (
                "Based on what you've shared, I recommend the following solutions from our catalog. "
                "Let me fetch the best options for you."
            ),
            SalesStage.OBJECTION_HANDLING: (
                "I understand concerns about cost and implementation. We offer flexible plans, and our clients "
                "see a quick return on investment. Would you like to see case studies from your industry?"
            ),
            SalesStage.CLOSE: (
                "Let's move forward. I can generate a secure payment link for you, or schedule a demo. What works best?"
            ),
            SalesStage.END: (
                "Thank you for your time! I’ll follow up with additional details. Have a great day!"
            ),
        }
        return stage_prompts[self.stage]

    def _transition_stage(self, user_input: str):
        stage_transitions = {
            SalesStage.INTRODUCTION: SalesStage.QUALIFICATION,
            SalesStage.QUALIFICATION: SalesStage.VALUE_PROPOSITION,
            SalesStage.VALUE_PROPOSITION: SalesStage.NEEDS_ANALYSIS,
            SalesStage.NEEDS_ANALYSIS: SalesStage.SOLUTION_PRESENTATION,
            SalesStage.SOLUTION_PRESENTATION: SalesStage.OBJECTION_HANDLING,
            SalesStage.OBJECTION_HANDLING: SalesStage.CLOSE,
            SalesStage.CLOSE: SalesStage.END
        }
        if self.stage in stage_transitions:
            self.stage = stage_transitions[self.stage]

    def process_input(self, user_input: str) -> str:
        if self.stage == SalesStage.END:
            return "Thank you for your time. Have a great day!"

        response = self.agent_executor.invoke({
            "input": user_input,
            "chat_history": self.chat_history
        })

        self.chat_history.append(("human", user_input))
        self.chat_history.append(("ai", response["output"]))

        self._transition_stage(user_input)
        return response["output"]


# Example Usage
if __name__ == "__main__":
    agent = SalesAgent()
    print("AI: Hello! Welcome to Mindware Solutions. I'm Mia, your digital sales assistant. How can I help you today?")
    while agent.stage != SalesStage.END:
        user_input = input("You: ")
        response = agent.process_input(user_input)
        print(f"AI: {response}")
    print("AI: Thank you for considering Mindware Solutions. We'll follow up shortly!")
