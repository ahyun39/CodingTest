SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE CONV(GENOTYPE,10,2) LIKE '1' OR 
      RIGHT(CONV(GENOTYPE,10,2), 3) IN ('101', '001', '100');