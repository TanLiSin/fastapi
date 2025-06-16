from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transaction_api import router as transaction_router
from verify_freshness_api import router as freshness_router

app = FastAPI()

# ✅ Add CORS middleware globally here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction_router)
app.include_router(freshness_router)
