import asyncio
import pickle

from ceylon import RunnerAgent

from agents.InterfaceAgent import InterfaceAgent


async def main():
    runner = RunnerAgent("main", port=8888, server_mode=True)

    interface_agent = InterfaceAgent(name="interface", role="Communicate with outside")

    await runner.arun_admin(inputs=pickle.dumps({}), workers=[interface_agent])


if __name__ == "__main__":
    asyncio.run(main())
