from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # 세션을 사용하기 위한 키 설정

@app.route('/')
def index():
    # 세션에서 tasks 가져오기 (없으면 빈 딕셔너리)
    tasks = session.get("tasks", {})
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    time = request.form.get('time')
    task = request.form.get('task')

    if time and task:
        tasks = session.get("tasks", {})  # 세션에서 현재 task 가져오기
        tasks[time] = task  # 시간별 Task 저장
        session["tasks"] = tasks  # 세션에 다시 저장
        session.modified = True  # 세션 수정 플래그 설정

    return redirect(url_for('index'))

@app.route('/delete/<time>')
def delete(time):
    tasks = session.get("tasks", {})

    if time in tasks:
        del tasks[time]  # 해당 시간의 Task 삭제
        session["tasks"] = tasks  # 세션에 다시 저장
        session.modified = True

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

