inventory_stock = 100
total_revenue = 0.0 
def add_stock(amount):
    global inventory_stock
    print(f"Đã nhập thành công {amount}")
    inventory_stock+=amount
    print(f"Tồn kho hiện tại {inventory_stock}")
def calculate_final_price(quantity, price):
    try_price=quantity * price
    sale=0
    if try_price>=1000:
        sale= try_price * 0.10
    more_sale=(try_price-sale) * 0.08
    last_price=(try_price-sale)+more_sale
    return last_price, sale,try_price,more_sale
def process_sale(quantity, price):
    global inventory_stock, total_revenue
    if inventory_stock<quantity:
        print(f"Hàng hiện tại không đủ để cung cấp.Hiện tại chỉ có {inventory_stock} ")
        return
    last_price, sale,try_price,more_sale=calculate_final_price(quantity,price)
    inventory_stock-=quantity
    total_revenue+=last_price

    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: {price}")
    print(f"Tạm tính: {try_price}")
    print(f"Giảm giá: {sale}")
    print(f"Thuế VAT: {more_sale}")
    print(f"Tổng thanh toán: {last_price}")
def print_report():
    global inventory_stock, total_revenue
    print(f"Tổng kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: {total_revenue}")
while True:
    choice=input('''========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
Chọn chức năng (1-4):''')
    match choice:
        case '1':
            amount=int(input("Nhập số lượng hàm muốn thêm" ))
            add_stock(amount)
        case '2':
            quantity=int(input("Nhập số lượng sản phẩm muốn mua: "))
            price=float(input("Nhập giá sản phẩm: "))
            process_sale(quantity, price)
        case '3':
            print_report()
        case '4':
            print("Thoát chương trình")
            break
        case _:
            print("Nhập sai dữ liệu")
