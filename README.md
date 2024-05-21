# autotest_sql
Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

SELECT c.login, COUNT("inDelivery")
FROM "Couriers" AS c
left join "Orders" AS o ON c.id = o."courierId"
Where o."inDelivery" = true
GROUP BY c.login;

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

SELECT track,
	CASE
		WHEN finished = true THEN 2
		WHEN cancelled = true THEN -1
		WHEN "inDelivery" = true THEN 1
		END
FROM "Orders";
