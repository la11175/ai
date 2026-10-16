from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    
    topic = ""
    feedback=""
    student_answer=""
    question_text = "請先選擇學習主題"
    if request.method == "POST":
        topic = request.form.get("topic","")
        action = request.form.get("action", "")
        print("我選擇的主題:",topic)
    
        if topic == "輸入輸出":
            question_text = "Python 使用哪個函數顯示文字？"
        elif topic == "條件判斷":
            question_text = "請讓使用者輸入一個數字，判斷這個數字是正數、負數還是 0。"
        elif topic == "迴圈":
            question_text = "請使用迴圈輸出 1 到 10 的數字。"
        elif topic == "串列":
            question_text = "請建立一個包含 5 個水果名稱的串列，並把所有水果輸出。"
        else:
            question_text = "請先選擇學習主題"
        # 判斷是否按下「提交答案」 (對應 Step 11)
        if action == "check" and topic == "輸入輸出":
            student_answer = request.form.get("student_answer", "")
            
            if student_answer == "B":
                feedback = "答對了！"
            else:
                feedback = "答錯了！"
    return render_template("index.html",
                           topic=topic,
                           question_text=question_text,
                           feedback=feedback
                           )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
