import random, os, phonenumbers
from phonenumbers import carrier
from pyshade import *
from threading import Thread

_banner = """                                                                            
        ##### ##      /                                     ###          ##     
     ######  /###   #/                                     /####       ####  /  
    /#   /  /  ###  ##                                    /   ###      /####/   
   /    /  /    ### ##                                         ###    /   ##    
       /  /      ## ##                                          ###  /          
      ## ##      ## ##  /##      /###   ###  /###     /##        ###/           
      ## ##      ## ## / ###    / ###  / ###/ #### / / ###        ###           
    /### ##      /  ##/   ###  /   ###/   ##   ###/ /   ###       /###          
   / ### ##     /   ##     ## ##    ##    ##    ## ##    ###     /  ###         
      ## ######/    ##     ## ##    ##    ##    ## ########     /    ###        
      ## ######     ##     ## ##    ##    ##    ## #######     /      ###       
      ## ##         ##     ## ##    ##    ##    ## ##         /        ###      
      ## ##         ##     ## ##    ##    ##    ## ####    / /          ###   / 
      ## ##         ##     ##  ######     ###   ### ######/ /            ####/  
 ##   ## ##          ##    ##   ####       ###   ### ##### /              ###   
###   #  /                 /                                                    
 ###    /                 /                                                     
  #####/                 /                                                      
    ###                 /                                                       
                    Phone Debouncer -> By PLATIPUS#5696"""

val = 0

def all_debounce(display: str, name: str, country_code: int, iso: str):
    global val
    while True :
        try:    
            num = f"+{country_code}"+"".join(random.choice("0123456789") for _ in range(9))
            valid = phonenumbers.parse(num)
            opera = carrier.name_for_number(valid, iso) 

            os.makedirs(f"Valid/{name}/", exist_ok=True)

            if phonenumbers.is_valid_number(valid) and opera !="":
                val += 1
                Sys.Title(f"Nows@PLATIPUS ~ Phone Debouncer [Valid: {val}]")
                if display == 'T':
                    Mode.Horizontal(colors.purple_to_red,f"[+] Valid: {num}: [Counter : {val}]",5, False)

                if "e*Message" in opera:
                    opera = "eMessage"
                                                
                with open(f"Valid/{name}/{opera}.txt" , 'a+') as file :
                    file.write(num + '\n')
        except:
            pass
choice  = int(Mode.Vertical(colors.cyan_to_blue, _banner+"""\n
[0]All Country

[1]Afghanistan                     [42]Chad                [83]Grenada        [124]Macedonia                [165]Paraguay         [206]Svalbard
[2]Albania                         [43]Chile               [84]Guam           [125]Madagascar               [166]Peru             [207]Swaziland
[3]Algeria                         [44]China               [85]Guatemala      [126]Malawi                   [167]Philippines      [208]Sweden
[4]American Samoa                  [45]Christmas Island    [86]Guernsey       [127]Malaysia                 [168]Pitcairn         [209]Switzerland
[5]Andorra                         [46]Cocos Islands       [87]Guinea         [128]Maldives                 [169]Poland           [210]Syria
[6]Angola                          [47]Colombia            [88]Guinea-Bissau  [129]Mali                     [170]Portugal         [211]Taiwan
[7]Anguilla                        [48]Comoros             [89]Guyana         [130]Malta                    [171]Puerto Rico      [212]Tajikistan
[8]Antarctica                      [49]Cook Islands        [90]Haiti          [131]Marshall Islands         [172]Qatar            [213]Tanzania
[9]Antigua and Barbuda             [50]Costa Rica          [91]Honduras       [132]Mauritania               [173]Republic Congo   [214]Thailand
[10]Argentina                      [51]Croatia             [92]Hong Kong      [133]Mauritius                [174]Reunion          [215]Togo
[11]Armenia                        [52]Cuba                [93]Hungary        [134]Mayotte                  [175]Romania          [216]Tokelau
[12]Aruba                          [53]Curacao             [94]Iceland        [135]Mexico                   [176]Russia           [217]Tonga
[13]Australia                      [54]Cyprus              [95]India          [136]Micronesia               [177]Rwanda           [218]Trinidad
[14]Austria                        [55]Czech Republic      [96]Indonesia      [137]Moldova                  [178]Saint Barthelemy [219]Tunisia 
[15]Azerbaijan                     [56]Congo               [97]Iran           [138]Monaco                   [179]Saint Helena     [220]Turkey
[16]Bahamas                        [57]Denmark             [98]Iraq           [139]Mongolia                 [180]Saint Kitts      [221]Turkmenistan
[17]Bahrain                        [58]Djibouti            [99]Ireland        [140]Montenegro               [181]Saint Lucia      [222]Turks
[18]Bangladesh                     [59]Dominica            [100]Isle of Man   [141]Montserrat               [182]Saint Martin     [223]Tuvalu   
[19]Barbados                       [60]Dominican Republic  [101]Israel        [142]Morocco                  [183]Saint Pierre     [224]VirginIslands
[20]Belarus                        [61]East Timor          [102]Italy         [143]Mozambique               [184]Saint Vincent    [225]Uganda
[21]Belgium                        [62]Ecuador             [103]Ivory Coast   [144]Myanmar                  [185]Samoa            [226]Ukraine
[22]Belize                         [63]Egypt               [104]Jamaica       [145]Namibia                  [186]San Marino       [227]Emirates
[23]Benin                          [64]El Salvador         [105]Japan         [146]Nauru                    [187]Sao Tome         [228]UnitedKingdom
[24]Bermuda                        [65]Equatorial Guinea   [106]Jersey        [147]Nepal                    [188]Saudi Arabia     [229]UnitedStates
[25]Bhutan                         [66]Eritrea             [107]Jordan        [148]Netherlands              [189]Senegal          [230]Uruguay
[26]Bolivia                        [67]Estonia             [108]Kazakhstan    [149]Netherlands Antilles     [190]Serbia           [231]Uzbekistan
[27]Bosnia and Herzegovina         [68]Ethiopia            [109]Kenya         [150]New Caledonia            [191]Seychelles       [232]Vanuatu
[28]Botswana                       [69]Falkland Islands    [110]Kiribati      [151]New Zealand              [192]Sierra Leone     [233]Vatican
[29]Brazil                         [70]Faroe Islands       [111]Kosovo        [152]Nicaragua                [193]Singapore        [234]Venezuela
[30]British Indian Ocean Territory [71]Fiji                [112]Kuwait        [153]Niger                    [194]Sint Maartens    [235]Vietnam
[31]British Virgin Islands         [72]Finland             [113]Kyrgyzstan    [154]Nigeria                  [195]Slovakia         [236]Wallis
[32]Brunei                         [73]France              [114]Laos          [155]Niue                     [196]Slovenia         [237]WesternSahara
[33]Bulgaria                       [74]French Polynesia    [115]Latvia        [156]North Korea              [197]Solomon Islands  [238]Yemen
[34]Burkina Faso                   [75]Gabon               [116]Lebanon       [157]Northern Mariana Islands [198]Somalia          [239]Zambia
[35]Burundi                        [76]Gambia              [117]Lesotho       [158]Norway                   [199]South Africa     [240]Zimbabwe
[36]Cambodia                       [77]Georgia             [118]Liberia       [159]Oman                     [200]South Korea
[37]Cameroon                       [78]Germany             [119]Libya         [160]Pakistan                 [201]South Sudan
[38]Canada                         [79]Ghana               [120]Liechtenstein [161]Palau                    [202]Spain
[39]Cape Verde                     [80]Gibraltar           [121]Lithuania     [162]Palestine                [203]Sri Lanka
[40]Cayman Islands                 [81]Greece              [122]Luxembourg    [163]Panama                   [204]Sudan
[41]Central African Republic       [82]Greenland           [123]Macau         [164]Papua New Guinea         [205]Suriname

Your Choice > """,2 ,False, True))

list_iso = ['','afg', 'alb', 'dza', 'asm', 'and', 'ago', 'aia', 'ata', 'atg', 'arg', 'arm', 'abw', 'aus', 'aut', 'aze', 'bhs', 'bhr', 'bgd', 'brb', 'blr', 'bel', 'blz', 'ben', 'bmu', 'btn', 'bol', 'bih', 'bwa', 'bra', 'iot', 'vgb', 'brn', 'bgr', 'bfa', 'bdi', 'khm', 'cmr', 'can', 'cpv', 'cym', 'caf', 'tcd', 'chl', 'chn', 'cxr', 'cck', 'col', 'com', 'cok', 'cri', 'hrv', 'cub', 'cuw', 'cyp', 'cze', 'cod', 'dnk', 'dji', 'dma', 'dom', 'tls', 'ecu', 'egy', 'slv', 'gnq', 'eri', 'est', 'eth', 'flk', 'fro', 'fji', 'fin', 'fra', 'pyf', 'gab', 'gmb', 'geo', 'deu', 'gha', 'gib', 'grc', 'grl', 'grd', 'gum', 'gtm', 'ggy', 'gin', 'gnb', 'guy', 'hti', 'hnd', 'hkg', 'hun', 'isl', 'ind', 'idn', 'irn', 'irq', 'irl', 'imn', 'isr', 'ita', 'civ', 'jam', 'jpn', 'jey', 'jor', 'kaz', 'ken', 'kir', 'xkx', 'kwt', 'kgz', 'lao', 'lva', 'lbn', 'lso', 'lbr', 'lby', 'lie', 'ltu', 'lux', 'mac', 'mkd', 'mdg', 'mwi', 'mys', 'mdv', 'mli', 'mlt', 'mhl', 'mrt', 'mus', 'myt', 'mex', 'fsm', 'mda', 'mco', 'mng', 'mne', 'msr', 'mar', 'moz', 'mmr', 'nam', 'nru', 'npl', 'nld', 'ant', 'ncl', 'nzl', 'nic', 'ner', 'nga', 'niu', 'prk', 'mnp', 'nor', 'omn', 'pak', 'plw', 'pse', 'pan', 'png', 'pry', 'per', 'phl', 'pcn', 'pol', 'prt', 'pri', 'qat', 'cog', 'reu', 'rou', 'rus', 'rwa', 'blm', 'shn', 'kna', 'lca', 'maf', 'spm', 'vct', 'wsm', 'smr', 'stp', 'sau', 'sen', 'srb', 'syc', 'sle', 'sgp', 'sxm', 'svk', 'svn', 'slb', 'som', 'zaf', 'kor', 'ssd', 'esp', 'lka', 'sdn', 'sur', 'sjm', 'swz', 'swe', 'che', 'syr', 'twn', 'tjk', 'tza', 'tha', 'tgo', 'tkl', 'ton', 'tto', 'tun', 'tur', 'tkm', 'tca', 'tuv', 'vir', 'uga', 'ukr', 'are', 'gbr', 'usa', 'ury', 'uzb', 'vut', 'vat', 'ven', 'vnm', 'wlf', 'esh', 'yem', 'zmb', 'zwe']
list_country = ['','Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhuta', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Indian Ocean Territory ', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso ', 'Burundi', 'Cambodia ', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos Islands', 'Colombia', 'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic Congo', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthelemy', 'Saint Helena', 'Saint Kitts', 'Saint Lucia', 'Saint Martin', 'Saint Pierre', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maartens', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad', 'Tunisia ', 'Turkey', 'Turkmenistan', 'Turks', 'Tuvalu', 'VirginIslands', 'Uganda', 'Ukraine', 'Emirates', 'UnitedKingdom', 'UnitedStates', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'Wallis', 'WesternSahara', 'Yemen', 'Zambia', 'Zimbabwe']
list_country_code = ['', '93', '355', '213', '1-684', '376', '244', '1-264', '672', '1-268', '54', '347', '297', '61', '43', '994', '1-242', '973', '880', '1-246', '375', '32', '501', '229', '1-441', '975', '591', '387', '267', '55', '246', '1-284', '673', '359', '226', '257', '855', '237', '1', '238', '1-345', '236', '235', '56', '86', '61', '61', '57', '269', '682', '506', '385', '53', '599', '357', '420', '243', '45', '253', '1-767', '1-809, 1-829, 1-849', '670', '593', '20', '503', '240', '291', '372', '251', '500', '298', '679', '358', '33', '689', '241', '220', '995', '49', '233', '350', '30', '299', '1-473', '1-671', '502', '44-1481', '224', '245', '592', '509', '504', '852', '36', '354', '91', '62', '98', '964', '353', '44-1624', '972', '39', '225', '1-876', '81', '44-1534', '962', '7', '254', '686', '383', '965', '996', '856', '371', '961', '266', '231', '218', '423', '370', '352', '853', '389', '261', '265', '60', '960', '223', '356', '692', '222', '230', '262', '52', '691', '373', '377', '976', '382', '1-664', '212', '258', '95', '264', '674', '977', '31', '599', '687', '64', '505', '227', '234', '683', '850', '1-670', '47', '968', '92', '680', '970', '507', '675', '595', '51', '63', '64', '48', '351', '1-787, 1-939', '974', '242', '262', '40', '7', '250', '590', '290', '1-869', '1-758', '590', '508', '1-784', '685', '378', '239', '966', '221', '381', '248', '232', '65', '1-721', '421', '386', '677', '252', '27', '82', '211', '34', '94', '249', '597', '47', '268', '46', '41', '963', '886', '992', '255', '66', '228', '690', '676', '1-868', '216', '90', '993', '1-649', '688', '1-340', '256', '380', '971', '44', '1', '598', '998', '678', '379', '58', '84', '681', '212', '967', '260', '263']
print(list_country_code[142])
if choice != 0:
    all_debounce('T', list_country[choice], list_country_code[choice], list_iso[choice])
else:
    for i in range(241): 
        Thread(target=all_debounce, args=('T', list_country[i], list_country_code[i], list_iso[i]))
