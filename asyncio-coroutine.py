import time
import asyncio


async def delivery(menu, rider, cook_time):
    print("요기요 주문~ 요기요!")
    await asyncio.sleep(cook_time)
    print(f"{menu} 준비가 완료 되었습니다.")
    print(f"배정된 라이더 {rider}님이 {menu}을 배달을 시작하였습니다.")
    return f"{menu} 배달완료!"

# case 1
async def main():
    task1 = asyncio.create_task(delivery("굽네 오리지날", "배달왕", 2))
    task2 = asyncio.create_task(delivery("굽네 고추바사삭", "빛보다빨라", 1))
    await task1
    await task2

# case 2
# async def main():
#     await delivery("굽네 오리지날", "배달왕", 2)
#     await delivery("굽네 고추바사삭", "빛보다빨라", 1)

# case 3
# async def main():
#     result = await asyncio.gather(
#         delivery("굽네 오리지날", "배달왕", 2),
#         delivery("굽네 고추바사삭", "빛보다빨라", 1)
#     )
#     # gather -> list type
#     print(result)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)