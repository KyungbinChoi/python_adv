"""
AsyncIO - Implementation of Multi scrapping
- AsyncIO
    - 비동기 I/O Coroutine 작업을 위한 library
    - Generator : 반복적인 객제 return tㅏ용
    - Non-blocking 비동기 처리
        - Blocking I/O : 호출된 함수가 작업이 완료될 때 까지 제어권을 가지고 있어 타 함수는 대기
        - Non-blocking I/O : 호출된 함수가 (서브루틴) Return 후 호출된 함수(main routine) 에 제어권 전달 > 타 함수는 작업 지속
    - coroutine 의 확장판 격

    
"""
# Chapter07-01
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# non-blocking 비동기 처리

# Asyncio 웹 스크랩핑 실습
# aiohttp 권장
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()
# 서비스 방향이 비슷한 사이트로 실습 권장(예 : 게시판성 커뮤니티)
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://wemakeprice.com/']


async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return res.read()[0:5]

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    
    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료 까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)