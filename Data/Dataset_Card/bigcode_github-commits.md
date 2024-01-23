



Samples: 76674567
76,674,567


SQL queries executed one-by-one. They're split up as BigQuery was raising `Resources exceeded during query execution` when running all in one.

```sql
SELECT
  commit, difference, subject, message, unnested_repo_name
FROM (
  SELECT
    repo_name,
    lang.name AS language_name
  FROM
    `bigquery-public-data.github_repos.languages` AS lang_table,
    UNNEST(LANGUAGE) AS lang) lang_table
JOIN
  `bigquery-public-data.github_repos.licenses` AS license_table
ON
  license_table.repo_name = lang_table.repo_name
JOIN (
  SELECT
    *
  FROM
    `bigquery-public-data.github_repos.commits` AS commits_table,
    UNNEST(repo_name) AS unnested_repo_name) commits_table
ON
  commits_table.unnested_repo_name = lang_table.repo_name
WHERE
  ((license_table.license LIKE 'mit')
    OR (license_table.license LIKE 'artistic-2.0')
    OR (license_table.license LIKE 'isc')
    OR (license_table.license LIKE 'cc0-1.0')
    OR (license_table.license LIKE 'epl-1.0')
    OR (license_table.license LIKE 'mpl-2.0')
    OR (license_table.license LIKE 'unlicense')
    OR (license_table.license LIKE 'apache-2.0')
    OR (license_table.license LIKE 'bsd-3-clause')
    OR (license_table.license LIKE 'agpl-3.0')
    OR (license_table.license LIKE 'lgpl-2.1')
    OR (license_table.license LIKE 'bsd-2-clause'))
  AND ( (lang_table.language_name LIKE 'Python')
    OR (lang_table.language_name LIKE 'Java')
    OR (lang_table.language_name LIKE 'JavaScript')
    OR (lang_table.language_name LIKE 'HTML')
    OR (lang_table.language_name LIKE 'Common Lisp')
    OR (lang_table.language_name LIKE 'Shell')
    OR (lang_table.language_name LIKE 'R')
    OR (lang_table.language_name LIKE 'Perl%')
    OR (lang_table.language_name LIKE 'SQL')
    OR (lang_table.language_name LIKE 'C')
    OR (lang_table.language_name LIKE 'C#')
    OR (lang_table.language_name LIKE 'C++')
    OR (lang_table.language_name LIKE 'TypeScript')
    OR (lang_table.language_name LIKE 'Go')
    OR (lang_table.language_name LIKE 'Rust')
    OR (lang_table.language_name LIKE 'Swift')
    OR (lang_table.language_name LIKE 'PHP')
    OR (lang_table.language_name LIKE 'Dart')
    OR (lang_table.language_name LIKE 'Kotlin')
    OR (lang_table.language_name LIKE 'Matlab')
    OR (lang_table.language_name LIKE 'MATLAB')
    OR (lang_table.language_name LIKE 'Ruby') )
AND
  LENGTH(commits_table.message) > 5
AND 
  LENGTH(commits_table.message) < 10000
AND LOWER(commits_table.message) NOT LIKE 'update readme.md'
AND LOWER(commits_table.message) NOT LIKE 'initial commit'
AND LOWER(commits_table.message) NOT LIKE 'update'
AND LOWER(commits_table.message) NOT LIKE 'mirroring from micro.blog.'
AND LOWER(commits_table.message) NOT LIKE 'update data.json'
AND LOWER(commits_table.message) NOT LIKE 'update data.js'
AND LOWER(commits_table.message) NOT LIKE 'add files via upload'
AND LOWER(commits_table.message) NOT LIKE 'update readme'
AND LOWER(commits_table.message) NOT LIKE "can't you see i'm updating the time?"
AND LOWER(commits_table.message) NOT LIKE 'pi push'
AND LOWER(commits_table.message) NOT LIKE 'dummy'
AND LOWER(commits_table.message) NOT LIKE 'update index.html'
AND LOWER(commits_table.message) NOT LIKE 'first commit'
AND LOWER(commits_table.message) NOT LIKE 'create readme.md'
AND LOWER(commits_table.message) NOT LIKE 'heartbeat update'
AND LOWER(commits_table.message) NOT LIKE 'updated readme'
AND LOWER(commits_table.message) NOT LIKE 'update log'
AND LOWER(commits_table.message) NOT LIKE 'test'
AND LOWER(commits_table.message) NOT LIKE 'no message'
AND LOWER(commits_table.message) NOT LIKE 'readme'
AND LOWER(commits_table.message) NOT LIKE 'wip'
AND LOWER(commits_table.message) NOT LIKE 'updates'
AND LOWER(commits_table.message) NOT LIKE 'first commit'
AND LOWER(commits_table.message) NOT LIKE 'commit'
AND LOWER(commits_table.message) NOT LIKE 'update _config.yaml'
AND LOWER(commits_table.message) NOT LIKE 'update data.json'
AND LOWER(commits_table.message) NOT LIKE 'update data.js'
AND LOWER(commits_table.message) NOT LIKE 'merge%';
```

3,641,694,786


```sql
SELECT commit, subject, message, STRING_AGG(unnested_repo_name) AS repos
FROM `huggingface-ml.commits_table_24122022.commits_table_base`
GROUP BY commit, subject, message
```

```sql
SELECT *
FROM (
  SELECT
    commit,subject,message,repos,difference
  FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup` AS commits_table_dedup
JOIN (
  SELECT
    commit AS commit_base,difference
  FROM
    `bigquery-public-data.github_repos.commits` AS commits_table_base
  ) commits_table_base
ON
  commits_table_base.commit_base = commits_table_dedup.commit
)
```

```sql
SELECT
    commit,subject,message,repos,d.old_path as old_file,d.new_path as new_file
FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup_difference` AS commits_table,
    UNNEST(difference) AS d
WHERE (d.old_path = d.new_path) AND (d.old_path IS NOT NULL) AND (d.new_path IS NOT NULL)
```

```sql
SELECT commit,subject,message,repos,old_file,new_file
FROM (
(
  SELECT commit AS commit_base
  FROM `huggingface-ml.commits_table_24122022.commits_table_dedup_files`
  GROUP BY commit
  HAVING COUNT(*) = 1
)
JOIN (
  SELECT
    commit,subject,message,repos,old_file,new_file
  FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup_files` AS commits_table_base
  ) commits_table_base
ON commits_table_base.commit = commit_base
)
```


Then export the final dataset from GCP to a bucket as parquet files.
Then copy those parquet files to the hf dataset on an instance.






### Redoing it to add licenses




Samples: 76674567
76,674,567


SQL queries executed one-by-one. They're split up as BigQuery was raising `Resources exceeded during query execution` when running all in one.

```sql
SELECT
  commit, difference, subject, message, unnested_repo_name, license
FROM (
  SELECT
    repo_name,
    lang.name AS language_name
  FROM
    `bigquery-public-data.github_repos.languages` AS lang_table,
    UNNEST(LANGUAGE) AS lang) lang_table
JOIN
  `bigquery-public-data.github_repos.licenses` AS license_table
ON
  license_table.repo_name = lang_table.repo_name
JOIN (
  SELECT
    *
  FROM
    `bigquery-public-data.github_repos.commits` AS commits_table,
    UNNEST(repo_name) AS unnested_repo_name) commits_table
ON
  commits_table.unnested_repo_name = lang_table.repo_name
WHERE
  ((license_table.license LIKE 'mit')
    OR (license_table.license LIKE 'artistic-2.0')
    OR (license_table.license LIKE 'isc')
    OR (license_table.license LIKE 'cc0-1.0')
    OR (license_table.license LIKE 'epl-1.0')
    OR (license_table.license LIKE 'mpl-2.0')
    OR (license_table.license LIKE 'unlicense')
    OR (license_table.license LIKE 'apache-2.0')
    OR (license_table.license LIKE 'bsd-3-clause')
    OR (license_table.license LIKE 'agpl-3.0')
    OR (license_table.license LIKE 'lgpl-2.1')
    OR (license_table.license LIKE 'bsd-2-clause'))
  AND ( (lang_table.language_name LIKE 'Python')
    OR (lang_table.language_name LIKE 'Java')
    OR (lang_table.language_name LIKE 'JavaScript')
    OR (lang_table.language_name LIKE 'HTML')
    OR (lang_table.language_name LIKE 'Common Lisp')
    OR (lang_table.language_name LIKE 'Shell')
    OR (lang_table.language_name LIKE 'R')
    OR (lang_table.language_name LIKE 'Perl%')
    OR (lang_table.language_name LIKE 'SQL')
    OR (lang_table.language_name LIKE 'C')
    OR (lang_table.language_name LIKE 'C#')
    OR (lang_table.language_name LIKE 'C++')
    OR (lang_table.language_name LIKE 'TypeScript')
    OR (lang_table.language_name LIKE 'Go')
    OR (lang_table.language_name LIKE 'Rust')
    OR (lang_table.language_name LIKE 'Swift')
    OR (lang_table.language_name LIKE 'PHP')
    OR (lang_table.language_name LIKE 'Dart')
    OR (lang_table.language_name LIKE 'Kotlin')
    OR (lang_table.language_name LIKE 'Matlab')
    OR (lang_table.language_name LIKE 'MATLAB')
    OR (lang_table.language_name LIKE 'Ruby') )
AND
  LENGTH(commits_table.message) > 5
AND 
  LENGTH(commits_table.message) < 10000
AND LOWER(commits_table.message) NOT LIKE 'update readme.md'
AND LOWER(commits_table.message) NOT LIKE 'initial commit'
AND LOWER(commits_table.message) NOT LIKE 'update'
AND LOWER(commits_table.message) NOT LIKE 'mirroring from micro.blog.'
AND LOWER(commits_table.message) NOT LIKE 'update data.json'
AND LOWER(commits_table.message) NOT LIKE 'update data.js'
AND LOWER(commits_table.message) NOT LIKE 'add files via upload'
AND LOWER(commits_table.message) NOT LIKE 'update readme'
AND LOWER(commits_table.message) NOT LIKE "can't you see i'm updating the time?"
AND LOWER(commits_table.message) NOT LIKE 'pi push'
AND LOWER(commits_table.message) NOT LIKE 'dummy'
AND LOWER(commits_table.message) NOT LIKE 'update index.html'
AND LOWER(commits_table.message) NOT LIKE 'first commit'
AND LOWER(commits_table.message) NOT LIKE 'create readme.md'
AND LOWER(commits_table.message) NOT LIKE 'heartbeat update'
AND LOWER(commits_table.message) NOT LIKE 'updated readme'
AND LOWER(commits_table.message) NOT LIKE 'update log'
AND LOWER(commits_table.message) NOT LIKE 'test'
AND LOWER(commits_table.message) NOT LIKE 'no message'
AND LOWER(commits_table.message) NOT LIKE 'readme'
AND LOWER(commits_table.message) NOT LIKE 'wip'
AND LOWER(commits_table.message) NOT LIKE 'updates'
AND LOWER(commits_table.message) NOT LIKE 'first commit'
AND LOWER(commits_table.message) NOT LIKE 'commit'
AND LOWER(commits_table.message) NOT LIKE 'update _config.yaml'
AND LOWER(commits_table.message) NOT LIKE 'update data.json'
AND LOWER(commits_table.message) NOT LIKE 'update data.js'
AND LOWER(commits_table.message) NOT LIKE 'merge%';
```



3,641,694,786


```sql
SELECT commit, subject, message, STRING_AGG(unnested_repo_name), license AS repos
FROM `huggingface-ml.commits_table_24122022.commits_table_base`
GROUP BY commit, subject, message, license
```

```sql
SELECT *
FROM (
  SELECT
    commit,subject,message,repos,difference,license
  FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup` AS commits_table_dedup
JOIN (
  SELECT
    commit AS commit_base,difference
  FROM
    `bigquery-public-data.github_repos.commits` AS commits_table_base
  ) commits_table_base
ON
  commits_table_base.commit_base = commits_table_dedup.commit
)
```

```sql
SELECT
    commit,subject,message,repos,license,d.old_path as old_file,d.new_path as new_file
FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup_difference` AS commits_table,
    UNNEST(difference) AS d
WHERE (d.old_path = d.new_path) AND (d.old_path IS NOT NULL) AND (d.new_path IS NOT NULL)
```

```sql
SELECT commit,repos,licenses
FROM (
(
  SELECT commit AS commit_base
  FROM `huggingface-ml.commits_table_24122022.commits_table_dedup_files`
  GROUP BY commit
  HAVING COUNT(*) = 1
)
JOIN (
  SELECT
    commit,subject,message,repos,old_file,new_file
  FROM
    `huggingface-ml.commits_table_24122022.commits_table_dedup_files` AS commits_table_base
  ) commits_table_base
ON commits_table_base.commit = commit_base
)
```


Then export the final dataset from GCP to a bucket as parquet files.
Then copy those parquet files to the hf dataset on an instance.



