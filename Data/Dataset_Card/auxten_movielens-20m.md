---
license: apache-2.0
---

Movielens 20m data with split training and test set by userId for GAUC.
More details could be see at:

https://github.com/auxten/edgeRec/blob/main/example/movielens/readme.md

## User split
user split status in `user` table, see SQL below:
```sql
create table movies
(
    movieId INTEGER,
    title   TEXT,
    genres  TEXT
);

create table ratings
(
    userId INTEGER,
    movieId INTEGER,
    rating FLOAT,
    timestamp INTEGER
);

create table tags
(
    userId    INTEGER,
    movieId   INTEGER,
    tag       TEXT,
    timestamp INTEGER
);

-- import data from csv, do it with any tool

select count(distinct userId) from ratings; -- 138,493 users

create table user as select distinct userId, 0 as is_train  from ratings;

-- choose 100000 random user as train user
update user
set is_train = 1
where userId in
      (SELECT userId
       FROM (select distinct userId from ratings)
       ORDER BY RANDOM()
       LIMIT 100000);

select count(*) from user where is_train != 1; -- 38,493 test users

-- split train and test set of movielens-20m ratings
create table ratings_train as
select r.userId, movieId, rating, timestamp
from ratings r
         left join user u on r.userId = u.userId
where is_train = 1;
create table ratings_test as
select r.userId, movieId, rating, timestamp
from ratings r
         left join user u on r.userId = u.userId
where is_train = 0;

select count(*) from ratings_train; --14,393,526
select count(*) from ratings_test;  --5,606,737
select count(*) from ratings;       --20,000,263
```

## User feature
`user_feature_train` and `user_feature_test` are pre-processed user feature
see SQL below:
```sql
--  user feature prepare
create table user_feature_train as
select r1.userId, ugenres, avgRating, cntRating
from
(
    select userId, avg(rating) as avgRating,
           count(rating) cntRating
    from ratings_train r1 group by userId
) r1 left join (
    select userId,
           group_concat(genres) as ugenres
    from ratings_train r
             left join movies t2 on r.movieId = t2.movieId
    where r.rating > 3.5
    group by userId
) r2 on r2.userId = r1.userId

--  user feature prepare
create table user_feature_test as
select r1.userId, ugenres, avgRating, cntRating
from
(
    select userId, avg(rating) as avgRating,
           count(rating) cntRating
    from ratings_test r1 group by userId
) r1 left join (
    select userId,
           group_concat(genres) as ugenres
    from ratings_test r
             left join movies t2 on r.movieId = t2.movieId
    where r.rating > 3.5
    group by userId
) r2 on r2.userId = r1.userId
```

## User behavior

```sql
create table ub_train as
select userId, group_concat(movieId) movieIds ,group_concat(timestamp) timestamps from ratings_train_desc group by userId order by timestamp

create table ub_test as
select userId, group_concat(movieId) movieIds ,group_concat(timestamp) timestamps from ratings_test_desc group by userId order by timestamp

create table ratings_train_desc as
select r.userId, movieId, rating, timestamp
from ratings_train r order by r.userId, timestamp desc;

create table ratings_test_desc as
select r.userId, movieId, rating, timestamp
from ratings_test r order by r.userId, timestamp desc;
```

