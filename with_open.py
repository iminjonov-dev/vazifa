with open('test_1.txt', 'w') as file:
    for i in range(1, 101):
        file.write(str(i) + '\n')

# with open context managerni bu test_1.txt fayilni ichidan "w" = write yozish modi boyicha test_1 faylini ichiga yozadi
#  file.write orqali string malumot turida yozadi
# har bir sonni yangi qatordan yozish uchun \n dan yoki \t dan foydalaniladi

if __name__ == "__main__":
    pass