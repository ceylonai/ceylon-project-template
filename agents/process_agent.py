import pickle

from ceylon import Agent
from loguru import logger


class ProcessAgent(Agent):

    async def on_message(self, agent_id: "str", data: "bytes", time: "int"):
        data = pickle.loads(data)
        logger.info(f"Received message from {agent_id}: {data}")

    async def run(self, inputs: "bytes"):
        logger.info(f"Process agent running with inputs: {inputs}")
