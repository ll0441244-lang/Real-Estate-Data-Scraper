import pandas as pd
from bs4 import BeautifulSoup

def scrape_local_data():
    # هنا وضعنا كود الـ HTML الخاص بموقع العقارات داخل الكود مباشرة (لن نحتاج إنترنت!)
    html_content = """
    <html>
        <body>
            <div class="col-sm-4 col-lg-4 col-md-4">
                <h4>شقة فاخرة لقطة</h4>
                <h4 class="pull-right">$150,000</h4>
                <p class="description">شقة ممتازة تحتوي على 3 غرف وحمامين ومطبخ راكب في وسط المدينة.</p>
            </div>
            <div class="col-sm-4 col-lg-4 col-md-4">
                <h4>فيلا مستقلة مسبح</h4>
                <h4 class="pull-right">$450,000</h4>
                <p class="description">فيلا واسعة مع حديقة كبيرة ومسبح خاص ونظام أمني متكامل.</p>
            </div>
            <div class="col-sm-4 col-lg-4 col-md-4">
                <h4>ستوديو مفروش قريباً</h4>
                <h4 class="pull-right">$60,000</h4>
                <p class="description">ستوديو مجهز بالكامل ومناسب للطلاب أو المستثمرين قرب الجامعة.</p>
            </div>
        </body>
    </html>
    """
    
    # نقوم بطبخ النص باستخدام BeautifulSoup مباشرة دون الحاجة لـ requests
    soup = BeautifulSoup(html_content, "html.parser")
    
    # نفس الكلاسات التي بحثنا عنها سابقاً
    articles = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
    
    properties_data = []

    for article in articles:
        try:
            title = article.find('h4').text.strip()
            # السعر مخزن في الـ h4 الثاني الذي يحمل كلاس pull-right
            price = article.find('h4', class_='pull-right').text.strip()
            description = article.find('p', class_='description').text.strip()
            
            properties_data.append({
                "اسم العقار / العنوان": title,
                "السعر": price,
                "الوصف والتفاصيل": description
            })
        except AttributeError:
            continue
    
    # تحويل البيانات لجدول وحفظها
    df = pd.DataFrame(properties_data)
    df.to_csv("my_first_project.csv", index=False, encoding="utf-8-sig")
    df.to_excel("my_first_project.xlsx", index=False)
    
    print("✅ نجح الأمر بالكامل! تم توليد ملفات Excel و CSV بنجاح بدون الحاجة للإنترنت!")

if __name__ == "__main__":
    scrape_local_data()
