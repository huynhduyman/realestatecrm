import pytz
from django.utils.translation import ugettext_lazy as _


INDCHOICES = (
    ('ADVERTISING', 'ADVERTISING'),
    ('AGRICULTURE', 'AGRICULTURE'),
    ('APPAREL & ACCESSORIES', 'APPAREL & ACCESSORIES'),
    ('AUTOMOTIVE', 'AUTOMOTIVE'),
    ('BANKING', 'BANKING'),
    ('BIOTECHNOLOGY', 'BIOTECHNOLOGY'),
    ('BUILDING MATERIALS & EQUIPMENT', 'BUILDING MATERIALS & EQUIPMENT'),
    ('CHEMICAL', 'CHEMICAL'),
    ('COMPUTER', 'COMPUTER'),
    ('EDUCATION', 'EDUCATION'),
    ('ELECTRONICS', 'ELECTRONICS'),
    ('ENERGY', 'ENERGY'),
    ('ENTERTAINMENT & LEISURE', 'ENTERTAINMENT & LEISURE'),
    ('FINANCE', 'FINANCE'),
    ('FOOD & BEVERAGE', 'FOOD & BEVERAGE'),
    ('GROCERY', 'GROCERY'),
    ('HEALTHCARE', 'HEALTHCARE'),
    ('INSURANCE', 'INSURANCE'),
    ('LEGAL', 'LEGAL'),
    ('MANUFACTURING', 'MANUFACTURING'),
    ('PUBLISHING', 'PUBLISHING'),
    ('REAL ESTATE', 'REAL ESTATE'),
    ('SERVICE', 'SERVICE'),
    ('SOFTWARE', 'SOFTWARE'),
    ('SPORTS', 'SPORTS'),
    ('TECHNOLOGY', 'TECHNOLOGY'),
    ('TELECOMMUNICATIONS', 'TELECOMMUNICATIONS'),
    ('TELEVISION', 'TELEVISION'),
    ('TRANSPORTATION', 'TRANSPORTATION'),
    ('VENTURE CAPITAL', 'VENTURE CAPITAL'),
)

TYPECHOICES = (
    ('CUSTOMER', 'CUSTOMER'),
    ('INVESTOR', 'INVESTOR'),
    ('PARTNER', 'PARTNER'),
    ('RESELLER', 'RESELLER'),
)

ROLES = (
    ('ADMIN', 'ADMIN'),
    ('USER', 'USER'),
)

LEAD_STATUS = (
    ('assigned', 'Assigned'),
    ('in process', 'Đang xử lý'),
    ('converted', 'Chuyển thành khách hàng'),
    ('recycled', 'Recycled (Xoay vòng lại)'),
    ('closed', 'Đã đóng')
)


LEAD_SOURCE = (
    ('call', 'Cuộc gọi điện thoại'),
    ('email', 'Email'),
    ('existing customer', 'Khách hàng hiện tại'),
    ('partner', 'Đối tác'),
    ('public relations', 'Quan hệ cộng đồng'),
    ('campaign', 'Chiến dịch'),
    ('other', 'Khác'),
)

STATUS_CHOICE = (
    ("New", "Mới"),
    ('Assigned', 'Assigned'),
    ('Pending', 'Đang xử lý'),
    ('Closed', 'Đóng'),
    ('Rejected', 'Từ chối'),
    ('Duplicate', 'Trùng lặp'),
)

PRIORITY_CHOICE = (
    ("Low", "Thấp"),
    ('Normal', 'Bình thường'),
    ('High', 'Cao'),
    ('Urgent', 'Khẩn cấp')
)

CASE_TYPE = (
    ("Question", "Khách Hàng | Câu hỏi"),
    ('Đặt cọc', 'Khách Hàng | Đặt cọc'),
    ('Ký hợp đồng mua bán', 'Khách Hàng | Ký hợp đồng mua bán'),
    ('Sang tên', 'Khách Hàng | Sang tên sổ đỏ/hồng'),
    ('Problem', 'Khách Hàng | Vấn đề'),
    ("Hẹn lịch Xem Nhà", "Chủ Nhà | Hẹn lịch Xem Nhà"),
    ("Thông tin về tranh chấp", "Chủ Nhà | Thông tin về tranh chấp"),
    ("Sang tên sổ đỏ", "Chủ Nhà | Sang tên sổ đỏ"),
    ("Ký hợp đồng môi giới", "Chủ Nhà | Ký hợp đồng môi giới"),
    ("Giao tiền, giao giấy tờ", "Chủ Nhà | Giao tiền, giao giấy tờ"),
    ("Thương lượng giá bán", "Chủ Nhà | Thương lượng giá bán"),
    ("Thương lượng phí môi giới", "Chủ Nhà | Thương lượng phí môi giới"),
)

STAGES = (
    ('Lên lịch hẹn xem nhà', 'Lên lịch hẹn xem nhà (20%)'),
    ('Phân tích nhu cầu', 'Phân tích nhu cầu'),
    ('Đủ điều kiện để mua', 'Đủ điều kiện để mua (40%)'),
    ('Quyết định mua', 'Quyết định mua'),
    ('Có thể ký hợp đồng', 'Có thể ký hợp đồng (90%)'),
    #('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'),
    #('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'),
    ('Thương lượng giá', 'Thương lượng giá'),
    ('CLOSED WON', 'Closed won (100% Won)'),
    ('CLOSED LOST', 'Closed lost (0% Lost)'),
)

SOURCES = (
    ('NONE', 'NONE'),
    ('CALL', 'Cuộc gọi điện thoại'),
    ('EMAIL', ' EMAIL'),
    ('EXISTING CUSTOMER', 'Khách hàng hiện tại'),
    ('PARTNER', 'Đối tác'),
    ('PUBLIC RELATIONS', 'Quan hệ cộng đồng'),
    ('CAMPAIGN', 'Chiến dịch'),
    ('WEBSITE', 'WEBSITE'),
    ('OTHER', 'Khác'),
)

EVENT_PARENT_TYPE = (
    (10, 'Account'),
    (13, 'Lead'),
    (14, 'Opportunity'),
    (11, 'Case')
)

EVENT_STATUS = (
    ('Planned', 'Planned'),
    ('Held', 'Held'),
    ('Not Held', 'Not Held'),
    ('Not Started', 'Not Started'),
    ('Started', 'Started'),
    ('Completed', 'Completed'),
    ('Canceled', 'Canceled'),
    ('Deferred', 'Deferred')
)


COUNTRIES = (
    ('VN', _('Viet Nam')),
    ('GB', _('United Kingdom')),
    ('AF', _('Afghanistan')),
    ('AX', _('Aland Islands')),
    ('AL', _('Albania')),
    ('DZ', _('Algeria')),
    ('AS', _('American Samoa')),
    ('AD', _('Andorra')),
    ('AO', _('Angola')),
    ('AI', _('Anguilla')),
    ('AQ', _('Antarctica')),
    ('AG', _('Antigua and Barbuda')),
    ('AR', _('Argentina')),
    ('AM', _('Armenia')),
    ('AW', _('Aruba')),
    ('AU', _('Australia')),
    ('AT', _('Austria')),
    ('AZ', _('Azerbaijan')),
    ('BS', _('Bahamas')),
    ('BH', _('Bahrain')),
    ('BD', _('Bangladesh')),
    ('BB', _('Barbados')),
    ('BY', _('Belarus')),
    ('BE', _('Belgium')),
    ('BZ', _('Belize')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BT', _('Bhutan')),
    ('BO', _('Bolivia')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BW', _('Botswana')),
    ('BV', _('Bouvet Island')),
    ('BR', _('Brazil')),
    ('IO', _('British Indian Ocean Territory')),
    ('BN', _('Brunei Darussalam')),
    ('BG', _('Bulgaria')),
    ('BF', _('Burkina Faso')),
    ('BI', _('Burundi')),
    ('KH', _('Cambodia')),
    ('CM', _('Cameroon')),
    ('CA', _('Canada')),
    ('CV', _('Cape Verde')),
    ('KY', _('Cayman Islands')),
    ('CF', _('Central African Republic')),
    ('TD', _('Chad')),
    ('CL', _('Chile')),
    ('CN', _('China')),
    ('CX', _('Christmas Island')),
    ('CC', _('Cocos (Keeling) Islands')),
    ('CO', _('Colombia')),
    ('KM', _('Comoros')),
    ('CG', _('Congo')),
    ('CD', _('Congo, The Democratic Republic of the')),
    ('CK', _('Cook Islands')),
    ('CR', _('Costa Rica')),
    ('CI', _('Cote d\'Ivoire')),
    ('HR', _('Croatia')),
    ('CU', _('Cuba')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DK', _('Denmark')),
    ('DJ', _('Djibouti')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('EC', _('Ecuador')),
    ('EG', _('Egypt')),
    ('SV', _('El Salvador')),
    ('GQ', _('Equatorial Guinea')),
    ('ER', _('Eritrea')),
    ('EE', _('Estonia')),
    ('ET', _('Ethiopia')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FO', _('Faroe Islands')),
    ('FJ', _('Fiji')),
    ('FI', _('Finland')),
    ('FR', _('France')),
    ('GF', _('French Guiana')),
    ('PF', _('French Polynesia')),
    ('TF', _('French Southern Territories')),
    ('GA', _('Gabon')),
    ('GM', _('Gambia')),
    ('GE', _('Georgia')),
    ('DE', _('Germany')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GR', _('Greece')),
    ('GL', _('Greenland')),
    ('GD', _('Grenada')),
    ('GP', _('Guadeloupe')),
    ('GU', _('Guam')),
    ('GT', _('Guatemala')),
    ('GG', _('Guernsey')),
    ('GN', _('Guinea')),
    ('GW', _('Guinea-Bissau')),
    ('GY', _('Guyana')),
    ('HT', _('Haiti')),
    ('HM', _('Heard Island and McDonald Islands')),
    ('VA', _('Holy See (Vatican City State)')),
    ('HN', _('Honduras')),
    ('HK', _('Hong Kong')),
    ('HU', _('Hungary')),
    ('IS', _('Iceland')),
    ('IN', _('India')),
    ('ID', _('Indonesia')),
    ('IR', _('Iran, Islamic Republic of')),
    ('IQ', _('Iraq')),
    ('IE', _('Ireland')),
    ('IM', _('Isle of Man')),
    ('IL', _('Israel')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JP', _('Japan')),
    ('JE', _('Jersey')),
    ('JO', _('Jordan')),
    ('KZ', _('Kazakhstan')),
    ('KE', _('Kenya')),
    ('KI', _('Kiribati')),
    ('KP', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('KW', _('Kuwait')),
    ('KG', _('Kyrgyzstan')),
    ('LA', _('Lao People\'s Democratic Republic')),
    ('LV', _('Latvia')),
    ('LB', _('Lebanon')),
    ('LS', _('Lesotho')),
    ('LR', _('Liberia')),
    ('LY', _('Libyan Arab Jamahiriya')),
    ('LI', _('Liechtenstein')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('MO', _('Macao')),
    ('MK', _('Macedonia, The Former Yugoslav Republic of')),
    ('MG', _('Madagascar')),
    ('MW', _('Malawi')),
    ('MY', _('Malaysia')),
    ('MV', _('Maldives')),
    ('ML', _('Mali')),
    ('MT', _('Malta')),
    ('MH', _('Marshall Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MU', _('Mauritius')),
    ('YT', _('Mayotte')),
    ('MX', _('Mexico')),
    ('FM', _('Micronesia, Federated States of')),
    ('MD', _('Moldova')),
    ('MC', _('Monaco')),
    ('MN', _('Mongolia')),
    ('ME', _('Montenegro')),
    ('MS', _('Montserrat')),
    ('MA', _('Morocco')),
    ('MZ', _('Mozambique')),
    ('MM', _('Myanmar')),
    ('NA', _('Namibia')),
    ('NR', _('Nauru')),
    ('NP', _('Nepal')),
    ('NL', _('Netherlands')),
    ('AN', _('Netherlands Antilles')),
    ('NC', _('New Caledonia')),
    ('NZ', _('New Zealand')),
    ('NI', _('Nicaragua')),
    ('NE', _('Niger')),
    ('NG', _('Nigeria')),
    ('NU', _('Niue')),
    ('NF', _('Norfolk Island')),
    ('MP', _('Northern Mariana Islands')),
    ('NO', _('Norway')),
    ('OM', _('Oman')),
    ('PK', _('Pakistan')),
    ('PW', _('Palau')),
    ('PS', _('Palestinian Territory, Occupied')),
    ('PA', _('Panama')),
    ('PG', _('Papua New Guinea')),
    ('PY', _('Paraguay')),
    ('PE', _('Peru')),
    ('PH', _('Philippines')),
    ('PN', _('Pitcairn')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('PR', _('Puerto Rico')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('BL', _('Saint Barthelemy')),
    ('SH', _('Saint Helena')),
    ('KN', _('Saint Kitts and Nevis')),
    ('LC', _('Saint Lucia')),
    ('MF', _('Saint Martin')),
    ('PM', _('Saint Pierre and Miquelon')),
    ('VC', _('Saint Vincent and the Grenadines')),
    ('WS', _('Samoa')),
    ('SM', _('San Marino')),
    ('ST', _('Sao Tome and Principe')),
    ('SA', _('Saudi Arabia')),
    ('SN', _('Senegal')),
    ('RS', _('Serbia')),
    ('SC', _('Seychelles')),
    ('SL', _('Sierra Leone')),
    ('SG', _('Singapore')),
    ('SK', _('Slovakia')),
    ('SI', _('Slovenia')),
    ('SB', _('Solomon Islands')),
    ('SO', _('Somalia')),
    ('ZA', _('South Africa')),
    ('GS', _('South Georgia and the South Sandwich Islands')),
    ('ES', _('Spain')),
    ('LK', _('Sri Lanka')),
    ('SD', _('Sudan')),
    ('SR', _('Suriname')),
    ('SJ', _('Svalbard and Jan Mayen')),
    ('SZ', _('Swaziland')),
    ('SE', _('Sweden')),
    ('CH', _('Switzerland')),
    ('SY', _('Syrian Arab Republic')),
    ('TW', _('Taiwan, Province of China')),
    ('TJ', _('Tajikistan')),
    ('TZ', _('Tanzania, United Republic of')),
    ('TH', _('Thailand')),
    ('TL', _('Timor-Leste')),
    ('TG', _('Togo')),
    ('TK', _('Tokelau')),
    ('TO', _('Tonga')),
    ('TT', _('Trinidad and Tobago')),
    ('TN', _('Tunisia')),
    ('TR', _('Turkey')),
    ('TM', _('Turkmenistan')),
    ('TC', _('Turks and Caicos Islands')),
    ('TV', _('Tuvalu')),
    ('UG', _('Uganda')),
    ('UA', _('Ukraine')),
    ('AE', _('United Arab Emirates')),
    ('US', _('United States')),
    ('UM', _('United States Minor Outlying Islands')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VU', _('Vanuatu')),
    ('VE', _('Venezuela')),
    ('VG', _('Virgin Islands, British')),
    ('VI', _('Virgin Islands, U.S.')),
    ('WF', _('Wallis and Futuna')),
    ('EH', _('Western Sahara')),
    ('YE', _('Yemen')),
    ('ZM', _('Zambia')),
    ('ZW', _('Zimbabwe')),
)

CURRENCY_CODES = (
    ('VND', _('VND, Dong')),
    ('USD', _('$, Dollar')),
)


def return_complete_address(self):
    address = ""
    if self.address_line:
        address += self.address_line
    if self.street:
        if address:
            address += ", " + self.street
        else:
            address += self.street
    if self.city:
        if address:
            address += ", " + self.city
        else:
            address += self.city
    if self.state:
        if address:
            address += ", " + self.state
        else:
            address += self.state
    if self.postcode:
        if address:
            address += ", " + self.postcode
        else:
            address += self.postcode
    if self.country:
        if address:
            address += ", " + self.get_country_display()
        else:
            address += self.get_country_display()
    return address


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def convert_to_custom_timezone(custom_date, custom_timezone, to_utc=False):
    user_time_zone = pytz.timezone(custom_timezone)
    if to_utc:
        custom_date = user_time_zone.localize(custom_date.replace(tzinfo=None))
        user_time_zone = pytz.UTC
    return custom_date.astimezone(user_time_zone)
