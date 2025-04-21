# SELECT : 출력하고 싶은 결과
    # COUNT : SELECT COUNT(*) : 집계함수 COUNT(열이름)
        # COUNT (AS 열이름)
        # COUNT (DISTINCT 열이름)
    # SUM : SUM(열이름) 집계함수 총 합계
    # AVG : AVG(열이름) 집계함수 평균
    # MIN : MIN(열이름) 최소값
    # MAX : MAX(열이름) 최대값
    # AS : AS 새로운 이름 : 별칭
# * : 전부(ALL)
# FROM : 테이블 이름
# INNER JOIN : 테이블 병합(테이블1과 테이블2 공통으로 있는 행만  출력
    # ON : ON 테이블1.열이름 = 테이블2.열이름
    #   ex) SELECT 열이름
            FROM 테이블1
            INNER JOIN 테이블2
            ON 테이블1.열이름 = 테이블2.열이름
# UNION : 테이블 쌓기(합치기) 
    # 열의 갯수가 같고, 열의 순서도 같아야한다. 데이터 타입 같아야 한다
    ex) SELECT 열이름 FROM 테이블1
        UNION (UNION ALL : 중복 다)
        SELECT 열이름 FROM 테이블2;
# WHERE : 조건문(필터링하는 것) 
    # WHERE 사용법 : AND , OR, !=
    # WHERE 나라 = '멕시코' AND 나이 = 30 : 두 개 이상 조건
    # WHERE 나라 = '멕시코' OR 나이 = 30  : 여러 조건 중 하나
    # WHERE 나라 != '멕시코' : 제외하고 싶은 필터 '멕시코'
    # WHERE 이름 LIKE 'TOM%' : 일정 패턴 찾을 때 TOM으로 시작하는 %
    # WHERE 이름 NOT LIKE '%y' : y로 끝나지 않는 
    # WHERE 이름 is NOT NULL : NULL 값 제외
# BETWEEN : BETWEEN 10 AND 20; 10-20 사이
# GROUP BY : 열 이름
# HAVING : 조건문 (WHERE 과 비슷하지만, GROUP BY 결과를 필터링)
# ORDER BY : 열 이름 ASC (DESC)
    # SELECT * FROM Products
    # WHERE ProductID BETWEEN 2 AND 3
    # ORDER BY Price DESC; : 가격 기준으로 내림차순 정렬
