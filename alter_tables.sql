use DatabaseName;
ALTER TABLE cache DROP INDEX search_query;
ALTER TABLE cache DROP INDEX id_UNIQUE;
ALTER TABLE cache MODIFY created_at Datetime;
