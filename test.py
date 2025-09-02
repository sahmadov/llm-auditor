import dotenv
dotenv.load_dotenv()  # May skip if you have exported environment variables.
from vertexai import agent_engines

agent_engine_id = "projects/773561763236/locations/us-central1/reasoningEngines/1403227525693308928"
user_input = "Double check this: Earth is further away from the Sun than Mars."

agent_engine = agent_engines.get(agent_engine_id)
session = agent_engine.create_session(user_id="new_user")
for event in agent_engine.stream_query(
    user_id=session["userId"], session_id=session["id"], message=user_input
):
    for part in event["content"]["parts"]:
        print(part["text"])