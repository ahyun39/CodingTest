select A.NAME, A.DATETIME
from ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
where B.DATETIME IS NULL
order by 2
LIMIT 3;