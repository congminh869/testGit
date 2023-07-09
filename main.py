from student import Student
import numpy 

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def addSV(self, id, name, sex, age, diemToan, diemLy, diemHoa):
        sv = Student(id, name, sex, age, diemToan, diemLy, diemHoa)
        check_id = self.check_loopID(id)
        if check_id==False:
            self.listSinhVien.append(sv)
            return True
        else:
            print('loop id ', id)
            return False

    def show(self):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        for sv in self.listSinhVien:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                .format(sv.id, sv.name, sv.sex, sv.age, sv.diemToan, 
                    sv.diemLy, sv.diemHoa, sv.diem_TB, sv.hoc_luc))

    def show_sv(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                .format(sv.id, sv.name, sv.sex, sv.age, sv.diemToan, 
                    sv.diemLy, sv.diemHoa, sv.diem_TB, sv.hoc_luc))


    def check_loopID(self, id):
        '''
            return True => loop id
            return False => # id
        '''

        for sv in self.listSinhVien:
            id_sv = sv.id 
            if id == id_sv:
                return True
        return False

    def remove_by_id(self, id):
        idx_remove = None
        for idx, sv in enumerate(self.listSinhVien):
            id_sv = sv.id 
            if id == id_sv:
                idx_remove =idx
                break
        if idx_remove!=None:
            del self.listSinhVien[idx_remove]
        else:
            print('id ban nhap vao khong ton tai')

    def search_by_name(self, name):
        listSV = []
        for idx, sv in enumerate(self.listSinhVien):
            name_sv = sv.name
            # Dong => dong ; DOng => dong => DONG dong
            if (name.lower() in name_sv.lower()):
                listSV.append(sv)

        if len(listSV)>0:
            self.show_sv(listSV)
        else:
            print('khong co ten sinh vien nay')

    def sort_average(self):
        list_TB = []
        for idx, sv in enumerate(self.listSinhVien):
            diem_TB = sv.diem_TB
            list_TB.append(diem_TB)

        # sap xep mang tu nho den lon
        list_TB_numpy = numpy.array(list_TB)
        list_idx = numpy.argsort(list_TB_numpy, axis=0) # index from smalest to largeist

        list_sv = []
        for idx in list_idx:
            sv = self.listSinhVien[idx]
            list_sv.append(sv)

        self.show_sv(list_sv)

    def update_by_id(self, id):
        check_id = self.check_loopID(id)

        if check_id==True:
            self.remove_by_id(id)
            id, name, sex, age, diemToan, diemLy, diemHoa = themSV(id)

            sv = Student(id, name, sex, age, diemToan, diemLy, diemHoa)
            self.listSinhVien.append(sv)
            self.show()
        else:
            print('id khong ton tai')

    def save_sv():
        pass

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def add():
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

    return name, sex, age, diemToan, diemLy, diemHoa

def themSV(id = None):
    while True:
        if id is not None:
            name, sex, age, diemToan, diemLy, diemHoa = add()
            break 
        else:
            print('nhap id sv : ', end=' ')
            id = input()
            if id.isdigit():
                name, sex, age, diemToan, diemLy, diemHoa = add()
                break
            else:
                print('***ERROR***:nhap id la so nguyen duong')
                continue
    return int(id), name, sex, age, diemToan, diemLy, diemHoa

if __name__ == '__main__':
    qlsv = QuanLySinhVien()
    id = 1
    name = "Nguyen Van A"
    sex = "Nam"
    age = "20"
    diemToan = 10
    diemLy = 8
    diemHoa = 9

    qlsv.addSV(1,name, sex, age, diemToan, diemLy, diemHoa) # 0.0001s , input='dong Khai'
    qlsv.addSV(2,"B", sex, age, 2, 3, 4)
    qlsv.addSV(3,"C", sex, age, 6, 7, 7)
    qlsv.addSV(4,"D", sex, age, 9, 10, 10)
    qlsv.addSV(5,"E", sex, age, 5, 5, 6)
    qlsv.addSV(6,"F", sex, age, 5, 5, 5)
    qlsv.addSV(7,"Dong", sex, age, 9, 8, 5)
    qlsv.addSV(8,"Nguyen Van Dong", sex, age, 1, 1, 1)
    qlsv.addSV(9,"Dong", sex, age, 0, 0, 2)
    qlsv.addSV(99,"Bo", sex, age, 5, 0, 1)
    qlsv.addSV(98,"Nguyen Van B", sex, age, 4, 4, 4)
    qlsv.show()

    print('---------------remove ---------------')
    qlsv.remove_by_id(1)
    qlsv.show()

    print('--------------search name----------------')
    qlsv.search_by_name('d')

    print('-------------- sort_average ---------------')
    qlsv.sort_average()

    print('-------------- update_by_id ---------------')
    qlsv.update_by_id(2)
    # print('len : ',len(qlsv.listSinhVien))

    # for sv in qlsv.listSinhVien:
    #     print("sv.name : ", sv.name)
