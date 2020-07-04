# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class act_admision_hotline_web(Action):

    def name(self) -> Text:
        return "act_admision_hotline_web"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "postback",
            "title": "Cách tuyển sinh 2020",
            "payload": "Cách tuyển sinh 2020"
        }
        button1 = {
            "type": "postback",
            "title": "Gọi trực tiếp",
            "payload": "Gọi trực tiếp"
        }
        button2 = {
            "type": "web_url",
            "url": "https://tuyensinh.ntu.edu.vn/?fbclid=IwAR277V_6NFYjhoYgTo6FDzD6rfTEPPQLJbTYWmyeHAnJgEgIi6py6G1pCok",
            "title": "Website tuyển sinh"
        }
        ret_text = "Mình có thể giúp gì cho bạn?"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []

class more_infor_way1(Action):

    def name(self) -> Text:
        return "more_infor_way1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://thisinh.thithptquocgia.edu.vn/",
            "title": "Đăng ký online"
        }
        ret_text = "Đăng ký hồ sơ tại trường THPT hiện đang học\nLink đăng ký online theo hệ thống của Bộ Giáo dục và Đào tạo"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class way1_front(Action):

    def name(self) -> Text:
        return "way1_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Tổng hợp thông tin về cách xét tuyển bằng điểm thi Tốt nghiệp THPT",
                                 image="https://scontent-hkt1-1.xx.fbcdn.net/v/t1.0-9/p720x720/103428467_4149833655034778_9214888897576009224_o.jpg?_nc_cat=106&_nc_sid=110474&_nc_ohc=4Z-_heI8-ykAX9vt017&_nc_ht=scontent-hkt1-1.xx&_nc_tp=6&oh=a893100339b739a961ee67b1e303a439&oe=5F1124D8")

        return []

class way1_back(Action):

    def name(self) -> Text:
        return "way1_back"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent-hkt1-1.xx.fbcdn.net/v/t1.0-9/p720x720/102326558_4149834608368016_5559910064336128177_o.jpg?_nc_cat=104&_nc_sid=110474&_nc_ohc=_Cxqdq1jZJAAX9e_5I5&_nc_ht=scontent-hkt1-1.xx&_nc_tp=6&oh=f4c530b07f87fcf7dfc3703e839d9659&oe=5F0D972D")

        return []

class way2_front(Action):

    def name(self) -> Text:
        return "way2_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về cách xét tuyển bằng điểm Xét tốt nghiệp THPT Quốc gia 2020",
                                 image="https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.0-9/p720x720/102312567_4149834398368037_6512956746752003800_o.jpg?_nc_cat=100&_nc_sid=110474&_nc_ohc=IcIzxGAWyGQAX-txIqR&_nc_ht=scontent.fsgn2-6.fna&_nc_tp=6&oh=151d2070c4dc5f4293e0b5ed03641493&oe=5F172DFE",)

        return []

class way2_back(Action):

    def name(self) -> Text:
        return "way2_back"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/p720x720/102408625_4149833858368091_6625207006115944170_o.jpg?_nc_cat=108&_nc_sid=110474&_nc_ohc=3ore74xOjjsAX9nnvmu&_nc_ht=scontent.fsgn2-3.fna&_nc_tp=6&oh=ab7b38f9506c93fc54f8f4f153a5620a&oe=5F1632C5")

        return []

class more_infor_way2(Action):

    def name(self) -> Text:
        return "more_infor_way2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://xettuyen.ntu.edu.vn/",
            "title": "Đk Online ĐH Nha Trang"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH Nha Trang"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class way3_front(Action):

    def name(self) -> Text:
        return "way3_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về cách xét tuyển bằng Điểm kỳ thi ĐGNL Đh Quốc gia Tp.HCM",
                                 image="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.0-9/p720x720/103110338_4149834185034725_7001519850147464325_o.jpg?_nc_cat=109&_nc_sid=110474&_nc_ohc=xP84_FLh8tUAX_dht6T&_nc_ht=scontent.fsgn2-4.fna&_nc_tp=6&oh=e9c73972e63c112c64c2fbebea39988c&oe=5F167541")

        return []

class way3_back(Action):

    def name(self) -> Text:
        return "way3_back"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/p720x720/103765033_4149834038368073_7877127494238702305_o.jpg?_nc_cat=108&_nc_sid=110474&_nc_ohc=a25Ox_3xKs4AX-2iIqI&_nc_ht=scontent.fsgn2-3.fna&_nc_tp=6&oh=16b72ccfa6fab023f2d6f1502e8158d7&oe=5F17467E")

        return []

class more_infor_way3(Action):

    def name(self) -> Text:
        return "more_infor_way3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://thinangluc.vnuhcm.edu.vn/dgnl/home.action",
            "title": "Kỳ thi ĐGNL ĐHQG-HCM"
        }
        button1 = {
            "type": "web_url",
            "url": "http://xettuyen.ntu.edu.vn/",
            "title": "Đk Online ĐH Nha Trang"
        }
        ret_text = "Link thông tin về kỳ thi đánh giá năng lực ĐHQG-HCM"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return []

class way4_front(Action):

    def name(self) -> Text:
        return "way4_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về cách xét tuyển thẳng",
                                 image="https://scontent.fsgn2-3.fna.fbcdn.net/v/t1.0-9/p720x720/103540627_4149833991701411_3392897730138958268_o.jpg?_nc_cat=108&_nc_sid=110474&_nc_ohc=LNWb-AwPHNgAX8vXYZF&_nc_ht=scontent.fsgn2-3.fna&_nc_tp=6&oh=3cb34b5dca833f14ce9f401918a0f10f&oe=5F186C04")

        return []

class way4_center(Action):

    def name(self) -> Text:
        return "way4_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent.fsgn2-4.fna.fbcdn.net/v/t1.0-9/p720x720/102664221_4149833778368099_2146002677581003414_o.jpg?_nc_cat=109&_nc_sid=110474&_nc_ohc=ErigaRzhC6QAX88q8ws&_nc_ht=scontent.fsgn2-4.fna&_nc_tp=6&oh=51c1fccda43812f39a0eb8d42b7c0407&oe=5F16D7E4")

        return []

class way4_back(Action):

    def name(self) -> Text:
        return "way4_back"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://scontent.fsgn2-2.fna.fbcdn.net/v/t1.0-9/p720x720/103979599_4149834491701361_5603723623457729652_o.jpg?_nc_cat=103&_nc_sid=110474&_nc_ohc=jGptf05RTCMAX8seRzw&_nc_ht=scontent.fsgn2-2.fna&_nc_tp=6&oh=727a9b03f352b0eab59faa35745c9bf2&oe=5F16254A")

        return []

class more_infor_way4(Action):

    def name(self) -> Text:
        return "more_infor_way4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinhso.vn/ban-tin-truoc-ky-thi/cac-truong-hop-duoc-tuyen-thang-vao-dai-hoc-c21640.html",
            "title": "Các trường ưu tiên"
        }
        ret_text = "Danh mục các trường THPT được ưu tiên (đối tượng 2.1)"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class link_fanpage(Action):

    def name(self) -> Text:
        return "link_fanpage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.facebook.com/tuyensinhdhnt/",
            "title": "Fanpage tuyển sinh"
        }
        ret_text = "Link Fanpage chính thức về thông tin tuyển sinh Đh Nha Trang. Bạn có thể theo dõi fanpage để cập nhật những thông tin nhanh và chính xác nhất về tuyển sinh."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class main_link(Action):

    def name(self) -> Text:
        return "main_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://www.ntu.edu.vn/",
            "title": "Website ĐH Nha Trang"
        }
        ret_text = "Link website chính thức của trường"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class admission_link(Action):

    def name(self) -> Text:
        return "admission_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinh.ntu.edu.vn/",
            "title": "Trang tuyển sinh"
        }
        ret_text = "Link trang tuyển sinh trường Đại học Nha Trang"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class more_informajor_2020mark(Action):

    def name(self) -> Text:
        return "more_informajor_2020mark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinh.ntu.edu.vn/%C4%90e-an-tuyen-sinh/Nganh-nghe-va-chi-tieu",
            "title": "Thông tin chi tiết"
        }
        ret_text = "Thông tin về ngành và điểm năm 2020"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class link_register_online(Action):

    def name(self) -> Text:
        return "link_register_online"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://xettuyen.ntu.edu.vn/",
            "title": "Đăng ký online"
        }
        button1 = {
            "type": "web_url",
            "url": "https://www.facebook.com/tuyensinhdhnt/",
            "title": "Fanpage tuyển sinh"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH Nha Trang.\nBạn cũng có thể theo dõi fanpage bên dưới để cập nhật thông tin liên tục."
        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return []

class link_form_regis(Action):

    def name(self) -> Text:
        return "link_form_regis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinh.ntu.edu.vn/%C4%90e-an-tuyen-sinh/phieu-xet-tuyen?fbclid=IwAR3p-GASOYTmkLB-SGFUfIrVRgPoRDBd9DUovaLnhT1wrmXvv6T4Btxvf7s",
            "title": "Phiếu đk xét tuyển"
        }
        ret_text = "Mẫu phiếu đăng ký xét tuyển Đh Nha Trang 2020"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class act_admission_ways(Action):

    def name(self) -> Text:
        return "act_admission_ways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Trường ĐH Nha Trang có 4 cách tuyển sinh\nCách 1: Điểm thi tốt nghiệp THPT\nCách 2: Điểm xét THPT quốc gia năm 2020\nCách 3: Điểm thi đánh giá năng lực Đh quốc gia TPHCM năm 2020\nCách 4: Xét tuyển thẳng",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Điểm thi TN THPT",
                    "payload": "Điểm thi TN THPT",
                },
                {
                    "content_type": "text",
                    "title": "Điểm xét THPT 2020",
                    "payload": "Điểm xét THPT 2020",
                },
                {
                    "content_type": "text",
                    "title": "Điểm thi ĐGNL TPHCM 2020",
                    "payload": "Điểm thi ĐGNL TPHCM 2020",
                },
                {
                    "content_type":"text",
                    "title": "Xét tuyển thẳng",
                    "payload":"Xét tuyển thẳng",
                }
            ]
        }

        dispatcher.utter_message(json_message=message)

        return []

class act_contact_hotline(Action):

    def name(self) -> Text:
        return "act_contact_hotline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "phone_number",
            "title": "02583831148",
            "payload": "02583831148"
        }
        button1 = {
            "type": "phone_number",
            "title": "02583831145",
            "payload": "02583831145"
        }
        ret_text = "Bạn có thể gọi điện thoại trực tiếp vào hai đầu số này"

        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return[]

class to_roi(Action):

    def name(self) -> Text:
        return "to_roi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        to_roi = []
        truoc = {
            "name": "Thông tin tuyển sinh",
            "image_url": "https://scontent.fdad3-2.fna.fbcdn.net/v/t1.6435-9/94565835_3968471509837661_2442480715061788672_n.jpg?_nc_cat=104&_nc_sid=b96e70&_nc_ohc=F513FQTO1bYAX9xwbMi&_nc_ht=scontent.fdad3-2.fna&oh=544cada6d9c95e0adadcee238059db21&oe=5F246C57",
            "intro": "Đại học Nha Trang",
            "link": "https://www.facebook.com/tuyensinhdhnt/",

        }
        to_roi.append(truoc)
        sau = {
            "name": "Thông tin tuyển sinh",
            "image_url": "https://scontent.fdad3-2.fna.fbcdn.net/v/t1.6435-9/94458621_3968475093170636_5869475098095779840_n.jpg?_nc_cat=104&_nc_sid=b96e70&_nc_ohc=Kz5qWBN69RoAX_KX-Z3&_nc_ht=scontent.fdad3-2.fna&oh=a5787b577f4097f9bc750d11c56952dd&oe=5F24EB3F",
            "intro": "Đại học Nha Trang",
            "link": "https://www.facebook.com/tuyensinhdhnt/",

        }
        to_roi.append(sau)

        template_items = []
        for toroi in to_roi:

            template_item = {
                "title": toroi['name'],
                "image_url": toroi['image_url'],
                "subtitle": toroi['intro'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": toroi['link'],
                        "title": "Xem ngay"
                    }
                ]
            }
            template_items.append(template_item)

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": template_items

                }
            }
        }
        ret_text = "Bạn có thể xem những thông tin cơ bản trong hình dưới:"
        print(message_str)
        dispatcher.utter_message(text=ret_text, json_message=message_str)

        return []

class basic_infor_about_nhatrang_university(Action):

    def name(self) -> Text:
        return "basic_infor_about_nhatrang_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "title": "http://www.ntu.edu.vn/",
            "payload": "Trang chủ Đh Nha Trang"
        }
        button1 = {
            "type": "web_url",
            "title": "https://www.facebook.com/daihocnhatrang/",
            "payload": "Fanpage chính thức"
        }
        ret_text = "Bạn có thể tham khảo một số thông tin cơ bản về trường qua trang chủ và Fanpage của nhà trường"

        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return[]

class how_to_apply(Action):

    def name(self) -> Text:
        return "how_to_apply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Cách nộp hồ sơ qua bưu điện hoặc trực tiếp tại trường Đh Nha Trang",
                                 image="https://scontent.fsgn2-5.fna.fbcdn.net/v/t1.0-9/p720x720/103149358_4149834235034720_2142719067723081087_o.jpg?_nc_cat=106&_nc_sid=110474&_nc_ohc=2MLPav7bPzcAX_eGiCZ&_nc_ht=scontent.fsgn2-5.fna&_nc_tp=6&oh=469c085e4f81ab5a5f0e135d0a504354&oe=5F178B76")

        return []