# 🚀 Geçersin Giriş Test Otomasyonu (Python + Selenium)

Bu proje, [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login) sitesindeki login formuna **geçersiz kullanıcı adı ve şifre girildiğinde hata mesajının doğru şekilde gösterilip gösterilmediğini test eder**.

Test otomasyonu, Python ve Selenium WebDriver kullanılarak yazılmıştır.

---

## 📌 Test Senaryosu

1. Chrome tarayıcısı açılır.
2. Login sayfasına gidilir: `https://the-internet.herokuapp.com/login`
3. Geçersiz kullanıcı adı ve şifre girilir.
4. Login butonuna tıklanır.
5. "Your username is invalid!" mesajının ekranda görünüp görünmediği kontrol edilir.
6. Tarayıcı kapatılır.

---

## 🧰 Kullanılan Teknolojiler

- Python 3.9
- Selenium WebDriver
- Chrome ve ChromeDriver
