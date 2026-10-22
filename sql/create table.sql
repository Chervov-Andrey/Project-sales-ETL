-- public.sales определение

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	sale_date date NOT NULL,
	doc_id varchar NOT NULL,
	item varchar NOT NULL,
	category varchar NOT NULL,
	amount int4 NOT NULL,
	price numeric NOT NULL,
	discount numeric NOT NULL,
	CONSTRAINT sales_amount_not_null NOT NULL amount,
	CONSTRAINT sales_category_not_null NOT NULL category,
	CONSTRAINT sales_discount_not_null NOT NULL discount,
	CONSTRAINT sales_doc_id_not_null NOT NULL doc_id,
	CONSTRAINT sales_item_not_null NOT NULL item,
	CONSTRAINT sales_price_not_null NOT NULL price,
	CONSTRAINT sales_sale_date_not_null NOT NULL sale_date
);