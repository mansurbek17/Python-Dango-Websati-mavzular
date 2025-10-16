# THREEDLAR

#  Thread (Ip) nima?
#  Thread — bu bitta dastur ichida bir nechta mustaqil bajariladigan kod oqimi.
#  Ular bir xil xotirada ishlaydi, shuning uchun o‘zaro oson ma'lumot almasha oladi

import time, os
from threading import  Thread, current_thread
from multiprocessing import Process,current_process


count=100_000_000
sleep=10

# def io_b(sec):
#     p_id=os.getpid()
#     print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi")
#     time.sleep(sleep)
#     print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish yakunlandi")

def cpu_b(k):
    p_id=os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi")
    while k>0:
        k-=1
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish yakunlandi")

if __name__=="__main__":
    s_time=time.time()
    # 1-single threed io_b
    # io_b(sleep)
    # io_b(sleep)
    # 2-multithreed - io_b
    # t1=Thread(target=io_b,args=(sleep, ))
    # t2 = Thread(target=io_b, args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 3-singlethreed cpu_b
    # cpu_b(count)
    # cpu_b(count)

    # 4-multithreed cpu_i
    # t1=Thread(target=cpu_b,args=(count,))
    # t2=Thread(target=cpu_b,args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    #
    # 5-multiprocessing cpu_b
    # p1=Process(target=cpu_b,args=(count,))
    # p2 = Process(target=cpu_b, args=(count,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # 6-multiprocessing io_b
    # p1 = Process(target=io_b, args=(sleep,))
    # p2 = Process(target=io_b, args=(sleep,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    e_time=time.time()

    print("vaqt - ", e_time-s_time)


# 🔹 Nima uchun threadlar kerak?
#
# Threadlar quyidagi holatlarda foydali:
# Foydalanuvchi interfeyslarini “muzlatib” qo‘ymaslik (GUI dasturlarda)
# Tarmoqli so‘rovlar bilan ishlash (API chaqiriqlari)
# Sekin ishlovchi operatsiyalarni fon jarayonga o‘tkazish (masalan, fayl yuklash)