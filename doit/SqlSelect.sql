# SELECT : 출력하고 싶은 결과
    # COUNT : SELECT COUNT(*) : 집계함수 COUNT(열이름)
        # COUNT (AS 열이름)
        # COUNT (DISTINCT 열이름)
    # SUM : SUM(열이름) 집계함수 총 합계
    # AVG : AVG(열이름) 집계함수 평균
    # MIN : MIN(열이름) 최소값
    # MAX : MAX(열이름) 최대값
# * : 전부(ALL)
# FROM : 테이블 이름
# WHERE : 조건문(필터링하는 것) 
    # WHERE 사용법 : AND , OR, !=
    # WHERE 나라 = '멕시코' AND 나이 = 30 : 두 개 이상 조건
    # WHERE 나라 = '멕시코' OR 나이 = 30  : 여러 조건 중 하나
    # WHERE 나라 != '멕시코' : 제외하고 싶은 필터 '멕시코'
    # WHERE 이름 LIKE 'TOM%' : 일정 패턴 찾을 때 TOM으로 시작하는 %
    # WHERE 이름 NOT LIKE '%y' : y로 끝나지 않는 
# BETWEEN : BETWEEN 10 AND 20; 10-20 사이
# GROUP BY : 열 이름
# HAVING : 조건문 
# ORDER BY : 열 이름 ASC (DESC)
    # SELECT * FROM Products
    # WHERE ProductID BETWEEN 2 AND 3
    # ORDER BY Price DESC; : 가격 기준으로 내림차순 정렬

