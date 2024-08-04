import asyncio
import pickle

from ceylon import RunnerAgent

from agents.InterfaceAgent import InterfaceAgent
from agents.data_emitter_agent import DataEmitAgent
from agents.process_agent import ProcessAgent


async def main():
    runner = RunnerAgent(server_mode=True)

    interface_agent = InterfaceAgent(name="interface", role="Communicate with outside")
    processor_agent = ProcessAgent(name="processor", role="Process user requests")
    data_emitter_agent = DataEmitAgent(name="data_emitter", role="Process user requests")

    await runner.arun_admin(inputs=pickle.dumps({}), workers=[processor_agent, interface_agent, data_emitter_agent])


if __name__ == "__main__":
    # enable_log("info")
    asyncio.run(main())
