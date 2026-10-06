# from fastapi import FastAPI
# from langgraph.graph import StateGraph

# from collector import collect_profile
# from suggest import suggest_allocation
# from recommend import recommend_assets


# app=FastAPI()

# graph = StateGraph(dict)

# graph.add_node("profile", collect_profile)
# graph.add_node("allocation", suggest_allocation)
# graph.add_node("recommendations", recommend_assets)

# graph.set_entry_point("profile")

# graph.add_edge("profile", "allocation")
# graph.add_edge("allocation", "recommendations")

# graph.set_finish_point("recommendations")

# runnable = graph.compile()


# ### App routes
# @app.get("/")
# def home():
#     return {
#         "message": "Investment Allocator Agent is running"
#     }
    
# @app.get("/allocate")
# def allocate():

#     result = runnable.invoke({})

#     return {
#         "profile": result["profile"],
#         "allocation": result["allocation"].content,
#         "recommendations": result["recommendations"].content
#     }



#######################################################

## Through input from user using full streamlit app

from fastapi import FastAPI, HTTPException
from groq import APIConnectionError, AuthenticationError
from pydantic import BaseModel
from langgraph.graph import StateGraph

from collector import collect_profile
from suggest import suggest_allocation
from recommend import recommend_assets


app = FastAPI()


# ============================================================
# USER PROFILE
# ============================================================

class Profile(BaseModel):

    age: int
    goal: str
    horizon: int
    risk: str


# ============================================================
# LANGGRAPH
# ============================================================

graph = StateGraph(dict)

graph.add_node(
    "profile",
    collect_profile
)

graph.add_node(
    "allocation",
    suggest_allocation
)

graph.add_node(
    "recommendations",
    recommend_assets
)

graph.set_entry_point(
    "profile"
)

graph.add_edge(
    "profile",
    "allocation"
)

graph.add_edge(
    "allocation",
    "recommendations"
)

graph.set_finish_point(
    "recommendations"
)

runnable = graph.compile()


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "InvestAI Investment Allocator is running"
    }


# ============================================================
# ALLOCATE
# ============================================================

@app.post("/allocate")
def allocate(profile: Profile):

    initial_state = {
        "profile": profile.model_dump()
    }

    try:
        result = runnable.invoke(initial_state)
    except AuthenticationError as exc:
        raise HTTPException(
            status_code=503,
            detail="Groq authentication failed. Check the GROQ_API_KEY value in .env.",
        ) from exc
    except APIConnectionError as exc:
        raise HTTPException(
            status_code=503,
            detail="Cannot connect to Groq. Check your internet connection and firewall settings.",
        ) from exc

    return {
        "profile": result["profile"],

        "allocation":
            result["allocation"].content,

        "recommendations":
            result["recommendations"].content
    }
