from ceylon import Agent, on_message
from loguru import logger

from data.user_details import UserDetails


class ProcessAgent(Agent):

    @on_message(UserDetails)
    async def on_user_details(self, user_details: UserDetails):
        logger.info(f"Received user details: {user_details}")

    async def run(self, inputs: "bytes"):
        logger.info(f"Process agent running with inputs: {inputs}")
