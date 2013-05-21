--select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="10080_txt_crude" or f1.docid="17035_txt_earn";
select * from (
(select val as m from
(select A.row_id as row, B.row_id as col, sum(A.count * B.count) as val
from
(select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="10080_txt_crude") A, 
(select f1.docid as row_id, f1.term as col_id, f1.count as count from frequency f1 where f1.docid="17035_txt_earn") B 
where A.col_id = B.col_id group by A.row_id, B.row_id)
where row="10080_txt_crude" and col="17035_txt_earn")
,
(select sum(count*count) as a from frequency where docid="10080_txt_crude"),
(select sum(count*count) as b from frequency where docid="17035_txt_earn")
);

