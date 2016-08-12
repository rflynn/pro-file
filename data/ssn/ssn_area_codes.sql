
create table ssn_area_codes (
    area_lo  char(3) not null,
    area_hi  char(3) not null,
    state    char(2),
    location text
);

.mode csv
.import ssn_area_codes.csv ssn_area_codes

create index idx_ssn_area_codes_area on ssn_area_codes (area_lo, area_hi);
update ssn_area_codes set state=null where state='';
update ssn_area_codes set location=null where location='';
