from fastapi import FastAPI
from pydantic import BaseModel
from utils import detect_category
from utils import generate_summary, generate_headlines

app = FastAPI()


class ArticleRequest(BaseModel):
    article: str
    tone: str
    language: str


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }


@app.post("/generate")
def generate(req: ArticleRequest):
    category = detect_category(req.article)

    try:

        summary = generate_summary(
        req.article,
        req.language
    )

        headlines = generate_headlines(
            req.article,
            req.tone,
            req.language
)

        return {
    "category": category,
    "summary": summary,
    "headlines": headlines
}

    except Exception as e:

        print("BACKEND ERROR:", str(e))

        return {
            "error": str(e)
        }