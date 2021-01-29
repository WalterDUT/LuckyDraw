from django.db import models
import pandas as pd
import numpy as np


# Create your models here.
class Customer(models.Model):
    number = models.IntegerField(max_length=1000)
    name = models.CharField(max_length=1000, blank=True)


def handle_uploaded_file(requestFile):
    pass


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


def import_data(file_read):
    xl = pd.ExcelFile(file_read)
    with open(file_read, "r") as cus_list:
        data = pd.read_excel(xl, 0, header=None)
        # print(data)
        luckyNumber = data.iloc[:, 7]
        cus = data.iloc[:, 1]
        list = {}
        for i in range(1, len(luckyNumber)):
            list[luckyNumber[i]] = cus[i]
            # pass
        # print(a)
        print(list)
        cus_list.close()
    return list


def random_cus(length):
    list_rand = np.random.randint(length, size=100)
    print(list_rand)
    return list_rand


def chose_cus(list_cus):
    flagFirst = {"name": None, "status": False}
    flagSecond = {"name": None, "status": False}
    flagThird1 = {"name": None, "status": False}
    flagThird2 = {"name": None, "status": False}
    # return_data = {flagFirst, flagSecond, flagThird1, flagThird2}
    while True:
        flagComplete = False
        list_lucky_rand = random_cus(100)
        for i in list_lucky_rand:
            if i in list_cus:
                if flagFirst["status"] == False:
                    print("Giai nhat thuoc ve", list_cus[i], "mang ma so:", i)
                    flagFirst["status"] = True
                    flagFirst["name"] = list_cus[i]
                    continue
                elif flagSecond["status"] == False and flagFirst["name"] != list_cus[i]:
                    print("Giai nhi thuoc ve", list_cus[i], "mang ma so:", i)
                    flagSecond["status"] = True
                    flagSecond["name"] = list_cus[i]
                    continue
                elif (
                        flagThird1["status"] == False
                        and flagFirst["name"] != list_cus[i]
                        and flagSecond["name"] != list_cus[i]
                ):
                    print("Giai ba thuoc ve", list_cus[i], "mang ma so:", i)
                    flagThird1["status"] = True
                    flagThird1["name"] = list_cus[i]
                    continue
                else:
                    if (
                            flagFirst["name"] != list_cus[i]
                            and flagThird1["name"] != list_cus[i]
                            and flagSecond["name"] != list_cus[i]
                    ):
                        print("Giai ba thuoc ve", list_cus[i], "mang ma so:", i)
                        flagThird2["status"] = True
                        flagThird2["name"] = list_cus[i]
                        flagComplete = True
                        break
            else:
                continue
        if flagComplete == True:
            break
    # return return_data
    return 0
