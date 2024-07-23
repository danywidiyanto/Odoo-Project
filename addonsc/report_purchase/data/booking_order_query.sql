-- data/booking_order_query.sql
SELECT
    pol.id AS id,
    po.date_order AS order_date,
    po.partner_id AS vendor_id,
    pol.product_id AS product_id,
    pol.product_qty AS quantity,
    pbo.booking_date AS booking_date
FROM
    purchase_order_line pol
JOIN
    purchase_order po ON pol.order_id = po.id
LEFT JOIN
    purchase_booking_order pbo ON pol.booking_order_id = pbo.id;
