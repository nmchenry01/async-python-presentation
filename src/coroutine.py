from pprint import pprint

async def something_async():
    return "I'm not really async!"

def main():
    coroutine = something_async()
    print(coroutine)
    pprint(dir(coroutine))

main()