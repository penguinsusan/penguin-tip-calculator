
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>펭귄의 더치페이 계산기 (•ө•)</title>
</head>
<body style="font-family:sans-serif; text-align:center; padding:30px;">
    <pre style="font-size:24px;">펭귄의 더치페이 계산기
(•ө•)
<)  )╯
 ,  ,</pre>

    <form method="post">
        <label>총 결제 금액은 얼마였나요? (KRW)</label><br>
        <input type="number" step="0.01" name="bill" required><br><br>

        <label>팁으로 몇 %%를 줄 생각인가요?</label><br>
        <select name="tip">
            <option value="0">0%</option>
            <option value="10">10%</option>
            <option value="12">12%</option>
            <option value="15">15%</option>
        </select><br><br>

        <label>식사한 인원은 몇 명인가요?</label><br>
        <input type="number" name="people" required><br><br>

        <input type="submit" value="계산하기">
    </form>

    {% if final_amount is not none %}
        <h2>한 사람 당 부담할 금액은 {{ final_amount }}원 입니다 ♥♥</h2>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def calculate():
    final_amount = None
    if request.method == "POST":
        try:
            bill = float(request.form["bill"])
            tip = int(request.form["tip"])
            people = int(request.form["people"])
            bill_with_tip = bill + (tip / 100) * bill
            bill_per_person = bill_with_tip / people
            final_amount = round(bill_per_person, 2)
        except:
            final_amount = "오류가 발생했어요!"

    return render_template_string(HTML_TEMPLATE, final_amount=final_amount)

app.run(host="0.0.0.0", port=3000)
