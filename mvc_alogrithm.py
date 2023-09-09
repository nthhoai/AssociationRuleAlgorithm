import os

def rules():
        import sys
        sys.path.append("mvc_alogrithm")
        from controllers import data_mining_association_rules as dmar
        from models import clinical_features_patient as mcfp
        from views import view_rules as vr
        a1 = dmar.data_mining_association_rule("items.csv")
        #a1.handle_path()
        #a1.alogrithm_get_ordered_statistics()
        #a1.rule_DE1()
        #a2 = a.df_rule()
        a2 = a1.frequent()
        a3 = vr.view_rules()
        a3.display(a2)


while True:
    #os.system("cls")
    print("""
    CHƯƠNG TRÌNH THỬ NGHIỆM LUẬT KẾT HỢP
    1. Khai phá và tìm tập luật
    2. Chẩn đoán
    0. Exit
    """)
    choice = input("Nhập lựa chọn: ")
    if choice == '1':
        rules()
        #print(a2)
        os.system('pause')


    elif choice == '2':
        from views import clinical_features_patient as vcfp 
        from views import view_prediction as vp
        from controllers import convert_clinical_features_patient
        from controllers import partterns as p 
        p = p.parttern()
        p.check_rule()
        rule_prediction = p.find_rule() 
        vp = vp.view_prediction()
        vp.display(rule_prediction)
        print ("1: ", p.data)
        os.system('pause')


    elif choice == '0':    
        print("Kết thúc chương trình")
        break

    else:
        print("Vui lòng nhập lại!")
        os.system('pause')




