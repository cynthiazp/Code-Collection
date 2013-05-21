select sum(m.count * q.count) as val 
from (
select 'q' as docid, 'washington' as term, 1 as count 
union
select 'q' as docid, 'taxes' as term, 1 as count
union 
select 'q' as docid, 'treasury' as term, 1 as count
) as q,
(select * from Frequency ) as m
where m.term = q.term 
group by m.docid, q.docid
order by val desc limit 1;


--select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="10080_txt_crude" or f1.docid="17035_txt_earn";

--select m,a,b from (
--(select val as m from 
--(select A.row_id as row, B.row_id as col, sum(A.count * B.count) as val
--from
--(select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="10080_txt_crude") A, 
--(select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="17035_txt_earn") B 
--where A.col_id = B.col_id group by A.row_id, B.row_id)
--where row="10080_txt_crude" and col="17035_txt_earn"),
--(select sum(count*count) as a from frequency where docid="10080_txt_crude"),
--(select sum(count*count) as b from frequency where docid="17035_txt_earn")
--);

