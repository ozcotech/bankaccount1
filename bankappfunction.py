# Banka Hesap Uygulaması (Function Örneği İle)
# Hesap Oluşturma Fonksiyonu
def createAccount(owner):
    account = {
        "owner": owner,
        "balance": 0
    }
    return account
# Para Yatırma İşlemi
def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        print("Yeni Bakiye: {:.2f}".format(account["balance"]))
    else:
        print("Geçersiz Tutar!")
# Para Çekme İşlemi
def withdraw(account, amount):
    if amount > 0 and amount <= account["balance"]:
        account["balance"] -= amount
        print("Yeni Bakiye: {:.2f}".format(account["balance"]))
    else:
        print("Geçersiz Tutar!")
# Bakiye Sorgulama İşlemi
def getBalance(account):
    print("Bakiye: {:.2f}".format(account["balance"]))
# Ana Program
print("Bankamızın Hesap Uygulamasına Hoşgeldiniz...")
owner = input("Hesap Sahibinin Adı: ")
account1 = createAccount(owner)
while True:
    print("Yapabileceğiniz İşlemler:")
    print("1. Para Yatırma")
    print("2. Para Çekme")
    print("3. Bakiye Sorgulama")
    print("4. Çıkış")
    choice = int(input("Seçiminiz (1-4): "))
    if choice == 1:
        amount = float(input("Yatırılacak Tutar: "))
        deposit(account1, amount)
    elif choice == 2:
        amount = float(input("Çekilecek Tutar: "))
        if amount > account1["balance"]:
            print("Yetersiz Bakiye!")
        else:
            withdraw(account1, amount)
    elif choice == 3:
        getBalance(account1)
    elif choice == 4:
        print("Çıkış Yapıldı.")
        break
    else:
        print("Geçersiz Seçim!")
