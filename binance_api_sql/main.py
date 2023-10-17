import tolerant_requests as tr
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

def list_item_to_str(arg_list):
    list_for_return = list()
    for item in arg_list:
        list_for_return.append(str(item))
    return list_for_return

symbol_for_keis = 'OPUSDT'
parametrs = {'symbol': symbol_for_keis, 'interval': '1m'}
klines_info = tr.get("https://api.binance.com/api/v3/klines", params=parametrs, type_response='json')
klines_info_str_list = list()

for item in klines_info:
    klines_info_str_list.append(list_item_to_str(item))
print(klines_info_str_list)

#создание бд
#строчка подключения
sqlite_database = 'sqlite:///OPUSDT_kline_info.db'

#Создаем движек sqlalchemy
engine = create_engine(sqlite_database)

#Создаем класс, объекты которого будут храниться в бд
class Base(DeclarativeBase): pass

class Kline(Base):
    __tablename__ = 'Klines_info'
    klineid = Column(Integer, primary_key=True, index=True)
    Kline_open_time = Column(String)
    Open_price = Column(String)
    High_price = Column(String)
    Low_price = Column(String)
    Close_price = Column(String)
    Volume = Column(String)
    Kline_Close_time = Column(String)
    Quote_asset_volume = Column(String)
    Number_of_trades = Column(String)
    Taker_buy_base_asset_volume = Column(String)
    Taker_buy_quote_asset_volume = Column(String)
    Unused_field_ignore = Column(String)

#Создаем таблицу
Base.metadata.create_all(bind = engine)

def db_test():
    with Session(autoflush=False, bind=engine) as db:
        object_list = db.query(Kline).all()
        KOT_list = list()
        for item in object_list:
            print(item.klineid,
                  item.Kline_open_time,
                  item.Open_price,
                  item.High_price,
                  item.Low_price,
                  item.Close_price,
                  item.Volume,
                  item.Kline_Close_time,
                  item.Quote_asset_volume,
                  item.Number_of_trades,
                  item.Taker_buy_base_asset_volume,
                  item.Taker_buy_quote_asset_volume,
                  item.Unused_field_ignore)

            KOT_list.append(item.Kline_open_time)
        # print(*KOT_list, sep='\n')
        # print(KOT_list[0], KOT_list[-2], KOT_list[-1])
        # print(len(KOT_list))


#Создаем сессию для подключения к бд
# def session_changes(list_of_values):
#     with Session(autoflush=False, bind=engine) as db:
#         object_list = db.query(Kline).all()
#         KOT_list = list()
#         for item in object_list:
#             KOT_list.append(item.Kline_open_time)
#
#         kline = Kline(
#                 Kline_open_time=list_of_values[0],
#                 Open_price=list_of_values[1],
#                 High_price=list_of_values[2],
#                 Low_price=list_of_values[3],
#                 Close_price=list_of_values[4],
#                 Volume=list_of_values[5],
#                 Kline_Close_time=list_of_values[6],
#                 Quote_asset_volume=list_of_values[7],
#                 Number_of_trades=list_of_values[8],
#                 Taker_buy_base_asset_volume=list_of_values[9],
#                 Taker_buy_quote_asset_volume=list_of_values[10],
#                 Unused_field_ignore=list_of_values[11])
#         if kline.Kline_open_time not in KOT_list:
#             db.add(kline)
#             db.commit()
#         else:
#             first = db.query(Kline).filter(Kline.Kline_open_time == list_of_values[0]).first()
#             first.Open_price = list_of_values[1]
#             first.High_price = list_of_values[2]
#             first.Low_price = list_of_values[3]
#             first.Close_price = list_of_values[4]
#             first.Volume = list_of_values[5]
#             first.Kline_Close_time = list_of_values[6]
#             first.Quote_asset_volume = list_of_values[7]
#             first.Number_of_trades = list_of_values[8]
#             first.Taker_buy_base_asset_volume = list_of_values[9]
#             first.Taker_buy_quote_asset_volume = list_of_values[10]
#             first.Unused_field_ignore = list_of_values[11]
#             db.commit()

def session_changes():
    with Session(autoflush=False, bind=engine) as db:
        object_list = db.query(Kline).all()
        klines_with_match_list = list()
        for response_item in klines_info_str_list:
            for item in object_list:
                if item.Kline_open_time == response_item[0]:
                    if response_item not in klines_with_match_list:
                        klines_with_match_list.append(response_item)
                    item.Open_price = response_item[1]
                    item.High_price = response_item[2]
                    item.Low_price = response_item[3]
                    item.Close_price = response_item[4]
                    item.Volume = response_item[5]
                    item.Kline_Close_time = response_item[6]
                    item.Quote_asset_volume = response_item[7]
                    item.Number_of_trades = response_item[8]
                    item.Taker_buy_base_asset_volume = response_item[9]
                    item.Taker_buy_quote_asset_volume = response_item[10]
                    item.Unused_field_ignore = response_item[11]
        for response_item in klines_info_str_list:
            if response_item not in klines_with_match_list:
                kline = Kline(
                    Kline_open_time=response_item[0],
                    Open_price=response_item[1],
                    High_price=response_item[2],
                    Low_price=response_item[3],
                    Close_price=response_item[4],
                    Volume=response_item[5],
                    Kline_Close_time=response_item[6],
                    Quote_asset_volume=response_item[7],
                    Number_of_trades=response_item[8],
                    Taker_buy_base_asset_volume=response_item[9],
                    Taker_buy_quote_asset_volume=response_item[10],
                    Unused_field_ignore=response_item[11])
                db.add(kline)
        db.commit()

# for item in klines_info_str_list:
#     session_changes(item)
# db_test()

session_changes()
db_test()




