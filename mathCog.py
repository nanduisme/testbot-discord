from discord.ext import commands


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def sort_numlist(self, nums: list):
        sorted_list = []
        for num in nums:
            def check(sorted_list=sorted_list, num=num):
                for x in sorted_list:
                    last = len(sorted_list)-1
                    if num <= x:
                        return (True, sorted_list.index(x))
                    elif num >= sorted_list[last] and x == sorted_list[last]:
                        return (False, sorted_list.index(x))

            get_back = check() if len(sorted_list) != 0 else (0, 0)
            to_insert, idx = get_back[0], get_back[1]

            if len(sorted_list) == 0:
                sorted_list.append(num)

            elif to_insert:
                sorted_list.insert(idx, num)
            elif not to_insert:
                sorted_list.append(num)

        return sorted_list

    def add_list(self, nums: list):
        sum = 0
        for num in nums:
            sum += num
        return sum

    @commands.command()
    async def mean(self, ctx, *nums):
        try:
            nums = [float(num) for num in nums]
        except:
            await ctx.send('Input error. Command cancelled.')
            return

        mean = self.add_list(nums)/float(len(nums))

        await ctx.send(f'The mean of `{nums}` is : `{mean}`')

    @commands.command()
    async def median(self, ctx, *nums):
        try:
            nums = [float(num) for num in nums]
        except:
            await ctx.send('Input error. Command cancelled.')
            return

        sorted_nums = self.sort_numlist(nums)
        if len(sorted_nums)%2 == 1:
            idx = int((len(sorted_nums)+1)/2)-1
            median = sorted_nums[idx]
        else:
            idx1 = int((len(sorted_nums)+1)/2)-1
            idx2 = int((len(sorted_nums))/2)-1
            median = (sorted_nums[idx1]+sorted_nums[idx2])/2

        await ctx.send(f'The median of `{sorted_nums}` is : `{median}`.')

    @commands.command()
    async def mode(self, ctx, *nums):
        try:
            nums = [float(num) for num in nums]
        except:
            await ctx.send('Input error. Command cancelled.')
            return

        modes = []
        for num in nums:
            count = 0
            for element in nums:
                if num == element:
                    count += 1

                    if len(modes) !=0:
                        for mode in modes:
                            if count >= mode[1]:
                                if mode[0] == num:
                                    mode[1] = count
                                elif [num, count] in modes:
                                    pass
                                else:
                                    modes.append([num, count])
                    else:
                        modes.append([num, count])
            
        count = modes[0][1]
        modes = [mode[0] for mode in modes]
        many = '(s)' if len(modes) > 1 else ''
        modes = modes[0] if len(modes) == 1 else [mode for mode in modes]

        await ctx.send(f'The mode{many} of `{self.sort_numlist(nums)}` is : `{modes}`. Occuring at a total of `{count}` times in the given data.')

def setup(bot):
    bot.add_cog(Math(bot))