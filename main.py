from QuanLySinhVien import QuanLySinhVien

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    qlsv = QuanLySinhVien()
    while True:
        print("\nCHUONG TRINH QUAN LY SINH VIEN C#")
        print("*************************MENU**************************")
        print("**  1. Them sinh vien.                               **")
        print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
        print("**  3. Xoa sinh vien boi ID.                         **")
        print("**  4. Tim kiem sinh vien theo ten.                  **")
        print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
        print("**  6. Sap xep sinh vien theo ten.                   **")
        print("**  7. Sap xep sinh vien theo ID.                    **")
        print("**  8. Hien thi danh sach sinh vien.                 **")
        print("**  0. Thoat                                         **")
        print("*******************************************************")
        
        # try:
        n = int(input()) #string => ep kieu int .isnumeric()
        # except:
        #     print('input khong hop le, moi ban nhap lai')
        #     continue


        if n == 0:
            print("0. Thoat")
            break
        elif n==1:
            print("1. Them sinh vien.")

            while True:
                print('nhap id sv : ', end=' ')
                id = input()
                if id.isdigit():
                    print('nhap ten sv : ', end=' ')
                    name = input()

                    while True:
                        print('nhap sex sv -- 1/nam -- 0/nu: ', end=' ')
                        sex_option = input()
                        sex = ''
                        if sex_option.isdigit():
                            sex_option = int(sex_option)
                            if sex_option == 1:
                                sex = 'Nam'
                                break
                            elif sex_option == 0:
                                sex = 'Nu'
                                break
                            else:
                                print('***WARNING***: nhap sex la so nguyen duong 1/nam or 0/nu')
                        else:
                            print('***WARNING***: nhap sex la so nguyen duong 1/nam or 0/nu')

                    while True:
                        print('nhap age sv : ', end=' ')
                        age = input()
                        if age.isdigit():
                            age = int(age)
                            break
                        else:
                            print('***ERROR***:nhap age la so nguyen duong')

                    while True:
                        print('nhap diemToan sv : ', end=' ')
                        diemToan = input()
                        if isfloat(diemToan):
                            diemToan = float(diemToan)
                            if 0<=diemToan<=10:
                                break
                            else:
                                print('***ERROR***: hay nhap diem lon hon 0 va nho hon 10')
                            break
                        else:
                            print('***ERROR***:hay nhap kieu float')

                    while True:
                        print('nhap diemLy sv : ', end=' ')
                        diemLy = input() #float(num)
                        if isfloat(diemLy):
                            diemLy = float(diemLy)
                            if 0<=diemLy<=10:
                                break
                            else:
                                print('***ERROR***: hay nhap diem lon hon 0 va nho hon 10')
                        else:
                            print('***ERROR***:hay nhap kieu float')

                    while True:
                        print('nhap diemHoa sv : ', end=' ')
                        diemHoa = input()
                        if isfloat(diemHoa):
                            diemHoa = float(diemHoa)
                            if 0<=diemHoa<=10:
                                break
                            else:
                                print('***ERROR***: hay nhap diem lon hon 0 va nho hon 10')
                            break
                        else:
                            print('***ERROR***: hay nhap kieu float')

                    qlsv.addSV(int(id), name, sex, age, diemToan, diemLy, diemHoa)
                    break
                else:
                    print('***ERROR***:nhap id la so nguyen duong')
                    continue
        elif n==2:
            print("2. Cap nhat thong tin sinh vien boi ID.")
            print('nhap id sv : ', end=' ')
            id = int(input())
            qlsv.update_by_id(id)
        elif n==3:
            print("3. Xoa sinh vien boi ID.")

            print('nhap id sv : ', end=' ')
            id = int(input())

            qlsv.remove_by_id(id)
        elif n==4:
            print("4. Tim kiem sinh vien theo ten.")
            
            print('nhap ten sv : ', end=' ')
            name = input()

            qlsv.search_by_name(name)
        elif n==5:
            print("5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sort_average()
        elif n==6:
            print("6. Sap xep sinh vien theo ten.")
            sort_by_name()
        elif n==7:
            print("7. Sap xep sinh vien theo ID.")
            sort_by_id()
        elif n==8:
            print("8. Hien thi danh sach sinh vien.")
            qlsv.show()
        else:
            print('ban hay nhap so tu nhien tu 0->8')
        
