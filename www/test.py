import orm
from models import User, Blog, Comment
import asyncio

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    async def test():
        await orm.create_pool(loop, user = 'root', password = '', db = 'awesome')

        u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

        await u.save()

    loop.run_until_complete(test())
    loop.close()
# for x in test():
#     pass