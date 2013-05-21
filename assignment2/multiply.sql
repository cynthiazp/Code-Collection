select val from (select A.row_num as row, B.col_num as col, sum(A.value * B.value) as val
    from A, B where A.col_num = B.row_num
    group by A.row_num, B.col_num)
where row=2 and col=3;
