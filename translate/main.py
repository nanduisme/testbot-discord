import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from googletrans import Translator, LANGUAGES


class Cog(commands.Cog):

    """Translate Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def detectlang(self, ctx: Context, text: str = None):

        """$detectlang <text>"""

        if text is None:
            await ctx.send(
                embed=discord.Embed(
                    description="Wha...? What should i detect?", color=0xFF0000
                )
            )
            return

        translator = Translator()

        result = translator.detect(text)

        lang, certainity = LANGUAGES[result.lang].title(), result.confidence * 100

        await ctx.send(
            embed=discord.Embed(
                title=f"{lang}!",
                description=f"I'm `{int(certainity)}%` sure that `{text}` is in {lang}.",
                color=0xFF0000,
            )
        )

    @commands.command()
    async def langlist(self, ctx: Context):
    
        '''$langlist [langcode]'''
    
        langs = [f'`{lang}`, ' for lang in LANGUAGES]

        await ctx.send(embed=discord.Embed(
            title = 'Language Codes',
            description = ''.join(*langs)[-2]
        ))
    


def setup(bot):
    bot.add_cog(Cog(bot))