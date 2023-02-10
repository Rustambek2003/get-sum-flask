from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/api/get-sum/', methods=['GET'])
def get_sum():
    """
    this function returns sum of two number from request data.

    Returns:
        json: sum of two number

    Note:
        request data will be like this:
            /api/get-sum/?a=1&b=2
            
        response data will be like this:
            {
                "sum": 3
            }
    """
    
    a = request.args.get("a",0)
    b = request.args.get('b',0)

    sum = {
        "sum":int(a)+int(b)
    }

    sum = json.dumps(sum,indent=4)
    return sum


if __name__ == "__main__":
    app.run()