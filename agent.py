from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from prompt import AGENT_INSTRUCTION, AGENT_RESPONSE
import asyncio
import logging

# Suppress Google truncate warnings
logging.getLogger("livekit.plugins.google").setLevel(logging.ERROR)

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTION)

async def entrypoint(ctx: agents.JobContext):
    # Use your API key here (replace with environment variable in production)
    api_key = "AIzaSyA8sFNu83NG_uLjxvbukUFdtwdHBDYuMPk"

    # Create agent session
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",
            temperature=0.8,
            api_key=api_key,
            instructions=AGENT_INSTRUCTION,
        )
    )

    # Start session
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Wait for model initialization to avoid generation_created timeout
    await asyncio.sleep(1.5)

    # Manage conversation history manually
    MAX_HISTORY = 10
    history = []

    # Retry mechanism to handle transient timeouts
    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        try:
            # Add user instruction to history
            history.append(AGENT_RESPONSE)
            if len(history) > MAX_HISTORY:
                history = history[-MAX_HISTORY:]  # keep last 10 messages

            combined_instructions = "\n".join(history)

            # Generate reply safely
            reply = await asyncio.wait_for(
                session.generate_reply(instructions=combined_instructions),
                timeout=30  # seconds
            )

            # Handle SpeechHandle: save audio to file
            if hasattr(reply, "get_audio_bytes"):
                audio_bytes = await reply.get_audio_bytes()
                with open("reply.wav", "wb") as f:
                    f.write(audio_bytes)
                print("Reply audio saved as reply.wav")
            else:
                print("Reply generated:", reply)

            # Successfully generated, exit retry loop
            break

        except asyncio.TimeoutError:
            print(f"[Attempt {attempt+1}] Reply generation timed out, retrying...")
            await asyncio.sleep(1)
        except Exception as e:
            # Catch internal LiveKit task errors (can safely ignore if reply exists)
            print(f"[Attempt {attempt+1}] Internal LiveKit error (ignored if reply exists):", e)
            await asyncio.sleep(1)
    else:
        print("Failed to generate reply after maximum retries.")

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
