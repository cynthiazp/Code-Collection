select count(term_count) from (select count as term_count from frequency group by docid having sum(count)>300);
