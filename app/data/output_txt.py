from typing import List
from gspread.models import Cell


def output_select_spending_for_month(
        month: str, food: List[Cell], miscellaneous: List[Cell],
        eating_out: List[Cell], other: List[Cell], total: Cell):
    text = f'''
【{month}の支出を表示】
-------------------------
・食料品
　　現金    {food[0].value}
　　クレカ  {food[1].value}
　　合計    {food[2].value}
-------------------------
・雑費
　　現金    {miscellaneous[0].value}
　　クレカ  {miscellaneous[1].value}
　　合計    {miscellaneous[2].value}
-------------------------
・外食費
　　現金    {eating_out[0].value}
　　クレカ  {eating_out[1].value}
　　合計    {eating_out[2].value}
-------------------------
・その他
　　現金    {other[0].value}
　　クレカ  {other[1].value}
　　合計    {other[2].value}
-------------------------
・合計      {total.value}
-------------------------
'''
    print(text)
