SELECT NAME , COUNT(NAME) AS COUNT -- 동물의 이름을 선택, 같은 이름을 가진 동물의 수를 집계하여 'COUNT'라는 별칭으로 표시
FROM ANIMAL_INS
WHERE NAME IS NOT NULL  -- 이름이 없는(NULL) 동물은 제외 (NULL은 그룹화되지 않기 때문)
GROUP BY NAME   -- 이름별로 그룹화하여 같은 이름을 가진 동물끼리 묶음
HAVING COUNT(NAME) > 1  -- 그룹화된 이름 중에서 2번 이상 등장하는 경우만 필터링
ORDER BY NAME ASC;  -- 결과를 이름 기준 오름차순으로 정렬