products = [
    {'name': 'Coca Cola', 'price': 15000, 'qty': 20},
    {'name': 'Pepsi', 'price': 14000, 'qty': 15},
    {'name': 'Sting', 'price': 12000, 'qty': 10},
    {'name': '7Up', 'price': 13000, 'qty': 18}
]
def add_product():   # không có tham số vì sẽ input bên trong
    name = input("Nhập tên sản phẩm: ").strip()
    if not name:
        print("Tên sản phẩm không được để trống.")
        return

    try:
        price = int(input("Nhập giá bán: ").strip())
        quantity = int(input("Nhập số lượng tồn kho: ").strip())
    except ValueError:
        print("Giá và số lượng phải là số nguyên. Thao tác bị hủy.")
        return

    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)
    print(f">>> Đã thêm: {name} - {price}đ - SL: {quantity}")
def view_inventory():
    print("\n--- DANH SÁCH SẢN PHẨM TRONG KHO ---")
    if not products:
        print("Kho đang trống.")
        return
    
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['name']} - Giá: {p['price']}đ - SL: {p['qty']}")
def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()
