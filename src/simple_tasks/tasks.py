from celeryapp import app


@app.task(ignore_result=True)
def hello() -> None:
    print("hello world")


@app.task(ignore_result=True)
def print_number(number: int = 0) -> None:
    print(f"Number is {number}")
