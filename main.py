from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import json 

app=Flask(__name__)
api=Api(app)

stock_put_args= reqparse.RequestParser()
stock_put_args.add_argument("shop_id", type=int, help="shop id is required.", required=True)
stock_put_args.add_argument("product_name", type=str, help="product_name is required.", required=True)
stock_put_args.add_argument("quantity", type=int, help="quantity is required.", required=True)
stock_put_args.add_argument("price", type=int, help="price is required.", required=True)
stock_put_args.add_argument("description", type=str, help="description", required=False)
stock_put_args.add_argument("avaliability_start", type=str, help="format spring-15-y1 is required.", required=True)
stock_put_args.add_argument("avaliability_period", type=str, help="format spring, year_round ... is required.", required=True)

# TODO: fix error methods 

# def abort_if_shop_id_doenst_exist(shop_id):
#     for i in range(len(stock_data)):
#         if stock_data[i]["shop_id"] == shop_id:
#             break
#         else:
#              abort(404, message= "shop_id not found...")

# def abort_if_product_id_doenst_exist(product_id, stock_data):
#     for i in range(len(stock_data)):
#         if stock_data[i]["product_id"] == product_id:
#             break
#         else:
#              abort(404, message= "product_id not found...")

class Stock(Resource):

    def get(self, product_id):
        with open('shop\stock.json', encoding="utf8") as f:
            stock_data = json.load(f)

        # abort_if_product_id_doenst_exist(product_id,stock_data)

        return stock_data[product_id], 201

    def put(self,product_id):

        with open('shop\stock.json', "r", encoding="utf8") as f:
            stock_data = json.load(f)

        args=stock_put_args.parse_args()

        stock_data.append(args)

        with open('shop\stock.json', 'w', encoding='utf-8') as f:
             json.dump(stock_data, f, ensure_ascii=False, indent=4)

        return stock_data[product_id], 201
    
api.add_resource(Stock, "/stock/<int:product_id>")

if __name__ == '__main__':
    app.run(debug=True)