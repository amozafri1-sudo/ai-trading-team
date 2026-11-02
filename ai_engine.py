import os
import logging
from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

class AIEngine:
    def __init__(self):
        self.client = None
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key:
            self.client = AsyncOpenAI(api_key=api_key)

    async def analyze(self, market_data):
        if not self.client:
            return {
                "status": "unavailable",
                "analysis": "OpenAI API key is not configured."
            }

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a cautious financial market analyst. "
                            "Analyze data, explain uncertainty, and never "
                            "guarantee profits or invent missing data."
                        )
                    },
                    {
                        "role": "user",
                        "content": str(market_data)
                    }
                ],
                temperature=0.2
            )

            return {
                "status": "success",
                "analysis": response.choices[0].message.content
            }

        except Exception:
            logger.exception("AI analysis failed")
            return {
                "status": "error",
                "analysis": "Analysis is temporarily unavailable."
            }
