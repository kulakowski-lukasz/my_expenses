BEGIN;

--
-- Create model Category
--
CREATE TABLE "tracking_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "category_name" varchar(200) NOT NULL,
    "category_icon" varchar(100) NOT NULL
);

--
-- Create model CostFreq
--
CREATE TABLE "tracking_costfreq" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "frequency" varchar(200) NOT NULL,
    "is_regular" bool NOT NULL
);

--
-- Create model Expense
--
CREATE TABLE "tracking_expense" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "expense_date" date NOT NULL,
    "expense_amount" real NOT NULL,
    "comment" varchar(1000) NOT NULL,
    "category_id" bigint NOT NULL UNIQUE REFERENCES "tracking_category" ("id") DEFERRABLE INITIALLY DEFERRED
);

--
-- Add field cost_freq to category
--
CREATE TABLE "new__tracking_category" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "category_name" varchar(200) NOT NULL,
    "category_icon" varchar(100) NOT NULL,
    "cost_freq_id" bigint NOT NULL UNIQUE REFERENCES "tracking_costfreq" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO
    "new__tracking_category" (
        "id",
        "category_name",
        "category_icon",
        "cost_freq_id"
    )
SELECT
    "id",
    "category_name",
    "category_icon",
    NULL
FROM
    "tracking_category";

DROP TABLE "tracking_category";

ALTER TABLE
    "new__tracking_category" RENAME TO "tracking_category";

COMMIT;