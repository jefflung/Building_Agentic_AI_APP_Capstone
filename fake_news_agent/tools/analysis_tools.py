import re
#URL input support
import requests
from bs4 import BeautifulSoup

from langchain_core.tools import tool

@tool
def extract_claims(text: str) -> list:
    """
    Extract key claims from a text by splitting into sentences.

    Args:
        text: The input article or statement.

    Returns:
        A list of up to 3 extracted claims.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)
    claims = [s.strip() for s in sentences if len(s.strip()) > 20]
    return claims[:3]

@tool
def detect_bias(text: str) -> int:
    """
    Detect biased or emotionally charged language.

    Args:
        text: Input text to analyze.

    Returns:
        An integer bias score between 0 and 100.
    """
    text = text.lower()
    bias_words = ["always", "never", "guaranteed", "miracle", "breakthrough", "cure"]

    score = sum(15 for w in bias_words if w in text)
    return min(score, 100)

@tool
def classify_risk(text: str, bias_score: int) -> str:
    """
    Classify misinformation risk based on bias score and medical keywords.

    Args:
        text: The input text.
        bias_score: Bias score from detect_bias().

    Returns:
        "High", "Medium", or "Low" risk.
    """
    medical_keywords = ["cancer", "drug", "disease"]
    is_medical = any(w in text.lower() for w in medical_keywords)

    if bias_score > 60 and is_medical:
        return "High"
    elif bias_score > 40:
        return "Medium"
    else:
        return "Low"

@tool
def web_search_tool(query: str) -> str:
    """
    Perform a simple fact-checking lookup for known misinformation patterns.

    Args:
        query: Search query or claim.

    Returns:
        A short fact-checking response.
    """
    if "cancer cure" in query.lower():
        return "No scientific evidence supports a guaranteed cancer cure."
    return "No strong evidence found."

@tool
def fetch_article_from_url(url: str) -> str:
    """
    Fetch article text from a URL.

    Args:
        url: The article link.

    Returns:
        Extracted text content (limited length).
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text[:2000]  # limit length (IMPORTANT)

    except Exception:
        return "Failed to fetch article content."