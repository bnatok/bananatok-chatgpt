import requests
import yfinance as yf
import re

NAVER_STOCK_DETAIL_URL = "https://m.stock.naver.com/api/stock/"
YAHOO_FINANCE_HOST = "https://finance.yahoo.com/quote/"


def get_tool_stock_price(stock_code):
    """주가정보 조회 반환"""
    try:
        print("Tool Stock price...: {}".format(stock_code))
        # 간혹 Naver의 stock_code가 035420.KS와 같은 포맷으로 올때가 있음
        stock_code_number = "".join(filter(str.isdigit, stock_code))
        stock_name = None
        if (
            stock_code_number and len(stock_code_number) >= 4
        ):  # 국내는 6자리지만 우선 4로 필터링
            response = requests.get(
                f"{NAVER_STOCK_DETAIL_URL}{stock_code_number}/basic"
            )
            data = response.json()
            stock_name = data.get("stockName")
        if not stock_name:  # 없는 경우 해외 주식 조회
            result = _get_usa_stock_price(stock_code)
            return result
        close_price = data["closePrice"]
        compare_to_previous_close_price = data["compareToPreviousClosePrice"]
        fluctuations_ratio = data["fluctuationsRatio"]
        stock_exchange_name = data["stockExchangeName"]
        compare_to_previous_price_text = data.get("compareToPreviousPrice", {}).get(
            "text", "알 수 없음"
        )

        answer = f"네이버 증권 기준으로{stock_exchange_name}에 상장된 {stock_name}({stock_code})의 주가는 {close_price}원이며, 전일 대비 {compare_to_previous_close_price}원 {compare_to_previous_price_text}, 등락률은 {fluctuations_ratio}%입니다."

        return answer
    except Exception as err:
        print("ERROR while stock price: {}".format(err))
        return "주가 정보를 조회할 수 없습니다"


def get_function_stock_price():
    return {
        "type": "function",
        "function": {
            "name": "get_tool_stock_price",
            "description": "Checking stock price information at the South Korean exchange",
            "parameters": {
                "type": "object",
                "properties": {
                    "stock_code": {
                        "type": "string",
                        "description": "stock tickers symbol",
                    },
                },
                "required": ["stock_code"],
            },
        },
    }


def _get_usa_stock_price(stock_code):
    """야후 파이낸스에서 특정 해외 종목정보 읽어오기"""
    tsla = yf.Ticker(stock_code)
    info = tsla.get_info()
    currency = info["currency"]
    current_price = info["currentPrice"]
    previous_close = info["previousClose"]

    # 가격 변동 계산
    price_change = current_price - previous_close
    percentage_change = (price_change / previous_close) * 100

    change_direction = "증가" if price_change > 0 else "감소"

    text = f"Yahoo finance 기준으로 {stock_code}의 현재 가격은 {currency} {current_price:.2f}이며, 전일 대비 {change_direction}했습니다. 가격 변동: {currency} {price_change:.2f} ({percentage_change:.2f}%)."

    return text
