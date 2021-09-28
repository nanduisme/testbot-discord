from discord.ext import commands

def get_kwargs(func: callable):
    async def wrapper(*args):
        string = " ".join(args)
        await func(string)

    return wrapper

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coolbot")
    async def coolbot(self, ctx):
        await ctx.send("This bot is cool. :)")

    @commands.command()
    async def feedback(self, ctx: commands.context.Context, *feedback):

        """Get feedback from the users"""

        if len(feedback) == 0:
            await ctx.send(
                "❌ Oops! I think you forgot to give your feedback!", delete_after=5
            )
            return

        dev = self.bot.get_user(591078175778537512)
        feedback = "".join(f"{word} " for word in feedback)

        await dev.send(f"**{ctx.author.display_name}** from **{ctx.guild.name}** says: " + feedback)
        await ctx.reply(
            "Team Chitti thanks you for your valuable feedback! 😄", delete_after=30
        )

    @commands.command()
    async def ping(self, ctx):
    
        '''Ping latency'''
    
        await ctx.send(f'I am speed! `{round(self.bot.latency*1000, 1)} ms`')

    @commands.command()
    @get_kwargs
    async def echo(self, ctx, string):
        await ctx.send(string)


def setup(bot):
    bot.add_cog(MiscCommands(bot))
