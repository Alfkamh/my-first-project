import os

LANG = "ar"

def menu_ar():
    print("⚔ سقطرى - Suqutra Tool")
    print("اختر أحد الخيارات:")
    print("1. إنشاء APK خبيث")
    print("2. تشغيل Listener تلقائي")
    print("3. تغيير اللغة (العربية 🇾🇪 / English 🇺🇸)")
    print("4. خروج")

def menu_en():
    print("⚔ Suqutra Tool")
    print("Choose an option:")
    print("1. Create malicious APK")
    print("2. Start Listener")
    print("3. Change language (العربية 🇾🇪 / English 🇺🇸)")
    print("4. Exit")

def main():
    global LANG
    while True:
        os.system("clear")
        if LANG == "ar":
            menu_ar()
        else:
            menu_en()
        choice = input(">> ").strip()
        if choice == "1":
            print("🚧 جاري إنشاء APK (تحت التطوير)...")
        elif choice == "2":
            print("🚧 جاري تشغيل Listener (تحت التطوير)...")
        elif choice == "3":
            LANG = "en" if LANG == "ar" else "ar"
        elif choice == "4":
            break
        else:
            print("❌ خيار غير صالح")
        input("\nاضغط Enter للاستمرار...")

if __name__ == "__main__":
    main()
