-- ex: set ts=4 et:

-- 
-- 
-- 

begin;

drop table if exists givenname_gender_summary;
create table givenname_gender_summary (
    id      integer not null primary key, -- TODO: WITHOUT ROWID
    name    text    not null unique,
    fcnt    integer not null,
    mcnt    integer not null,
    total   integer not null
);

insert into givenname_gender_summary (name, fcnt, mcnt, total)
select name,sum(f),sum(m),sum(total)
from (
    select
        name,
        sum(total * (gender='F')) as f,
        sum(total*(gender='M')) as m,
        sum(total) as total
    from givenname_birthyear
    group by name,gender
) group by name;

commit;

