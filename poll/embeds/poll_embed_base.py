from typing import Optional
import disnake

from poll.embeds import colours


class PollEmbedBase(disnake.Embed):
	"""A base class for poll embeds. This only sets the colour, title question, and optionally a description."""

	def __init__(self, question: str, description: Optional[str] = None):
		super().__init__(
			title=f"📊 {question}",
			colour=colours.blurple,
			description=description or "",
		)
