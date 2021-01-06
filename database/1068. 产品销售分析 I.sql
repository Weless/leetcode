
# 方法1
select Product.product_name, year, price
from Sales
join Product
on Sales.product_id = Product.product_id

# 方法2：使用using减少代码量，using用在两个关联的表中字段名称相同的列
select product_name, year, price
from Sales
join Product
using (product_id)