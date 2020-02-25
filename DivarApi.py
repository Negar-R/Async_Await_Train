import aiohttp
import asyncio
import json


async def get_json(client , url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_divar_top(client , subreddit):
    content = await get_json(client , 'https://api.divar.ir/v8/web-search/tehran' + subreddit)
    data = json.loads(content.decode('utf-8'))
    print('** ** ' , type(data))
    for i in data['widget_list']:
        title = i['data']['title']
        description = i['data']['description']
        image_url = i['data']['image']

        print(title + ' : ' + description + ' ( ' + image_url + ' )')

    print('DONE:', subreddit + '\n')


async def main(client):
    while True:
        await asyncio.gather(get_divar_top(client , '/car?q='+'پراید') ,
                            get_divar_top(client , '/car?q='+'206') ,
                            get_divar_top(client , '/car?q='+'پیکان') ,
                            get_divar_top(client , ''+'همه'))

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop = loop) # Client session is the recommended interface for making HTTP requests.

asyncio.ensure_future(main(client))
loop.run_forever()