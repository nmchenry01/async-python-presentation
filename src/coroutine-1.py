from pprint import pprint

async def something_async() -> str:
    return "I'm not really async!"

def main():
    coroutine = something_async()
    
    print(f"{coroutine}\n")
    pprint(dir(coroutine))

main()