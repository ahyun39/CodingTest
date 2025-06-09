with fish_cnt as (
    select fish_type, count(1) FISH_COUNT
    from FISH_INFO
    group by fish_type
)

select COUNT(1) FISH_COUNT
from FISH_INFO A LEFT JOIN FISH_NAME_INFO B ON A.FISH_TYPE = B.FISH_TYPE
where B.FISH_NAME in ('BASS', 'SNAPPER');