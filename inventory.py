products = [
    {'name': 'Coca Cola', 'price': 15000, 'qty': 20},
    {'name': 'Pepsi', 'price': 14000, 'qty': 15},
    {'name': 'Sting', 'price': 12000, 'qty': 10},
    {'name': '7Up', 'price': 13000, 'qty': 18}
]
def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()
