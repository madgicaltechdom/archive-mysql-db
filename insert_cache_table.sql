use DatabaseName;
DROP PROCEDURE IF EXISTS insert_loop;
CREATE PROCEDURE insert_loop()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 50000 DO
        INSERT INTO cacheb (model_name, engine, lang, other_prop, request, response, created_at)
        VALUES (
            CONCAT('model_', i),
            CONCAT('engine_', i),
            CASE FLOOR(RAND() * 4)
                WHEN 0 THEN 'en'
                WHEN 1 THEN 'fr'
                WHEN 2 THEN 'es'
                WHEN 3 THEN 'de'
            END,
            CONCAT('prop_', i),
            SUBSTRING(MD5(RAND()), 1, 1000),
            UNHEX(SUBSTRING(MD5(RAND()), 1, 500)),
            DATE(DATE_ADD(CURDATE(), INTERVAL -FLOOR(RAND() * 180) DAY)) 
            -- DATE_ADD(CURDATE(), INTERVAL -FLOOR(RAND() * 180) DAY)
        );
        SET i = i + 1;
    END WHILE;
END;

CALL insert_loop();