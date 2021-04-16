import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Black-Storage-Without/dp/B07XD2G5BW/ref=rtpb_2?pd_rd_w=tnxl7&pf_rd_p=83ec62d7-0656-4d5e-84a0-b6dd7a104840&pf_rd_r=MS16JECPANWVAAGERVS1&pd_rd_r=4927c05b-d984-4c5c-a61f-0cb7c8a89350&pd_rd_wg=8YEz5&pd_rd_i=B07XD2G5BW&psc=1",
        "name": "Samsung Galaxy A51 (Black, 6GB RAM, 128GB Storage)",
        "target_price": 20000
    },
    {
        "product_url": "https://www.amazon.in/dp/B0869855B8/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B0869855B8&pd_rd_w=Tl4AD&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=YzQoW&pf_rd_r=P8EKFCCXF1CKA89ZAMT8&pd_rd_r=fa3e46fc-fb0c-47fe-b2ae-0cf1a7ec9549&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUVNGUEpQMEVFVVNYJmVuY3J5cHRlZElkPUEwNTk4MDEyRFJVVTVaTUVRNlFNJmVuY3J5cHRlZEFkSWQ9QTA2ODY2NzMzUjgwTzZKNlBLN1FFJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name": "OnePlus Nord 5G (Blue Marble, 12GB RAM, 256GB Storage)",
        "target_price":28000
    },
    {
        "product_url": "https://www.amazon.in/dp/B077PWBC78/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=2Dg7vBmXUjNVcDipAU5JwQ&hsa_cr_id=6934406210302&pd_rd_plhdr=t&pd_rd_r=a814e397-25e3-49b1-abf4-7bad6fd9e408&pd_rd_w=MdWW7&pd_rd_wg=RGK0I&ref_=sbx_be_s_sparkle_mcd_asin_0_img",
        "name": "Redmi Note 9 Pro (Interstellar Black, 4GB RAM, 64GB Storage)",
        "target_price":17000
    },
    {
        "product_url": "https://www.amazon.in/gp/product/B08696W3B3/ref=s9_acss_bw_cg_Budget_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=JSE2S80VYSC1WBCDK9PH&pf_rd_t=101&pf_rd_p=3921ea48-93c2-4bd3-b626-c5ded9dbcc10&pf_rd_i=1389401031",
        "name": "Redmi 9 (Sporty Orange, 4GB RAM, 64GB Storage)",
        "target_price": 9000
    },
    {
        "product_url": "https://www.amazon.in/dp/B08V9ZNGTY/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08V9ZNGTY&pd_rd_w=SdoKZ&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=jtr5M&pf_rd_r=AJ9TTC8CQ72QWE5EAP2A&pd_rd_r=97be412f-bd11-4548-9116-132c3f4f8ab1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVk1LS0JRNjJLUDg2JmVuY3J5cHRlZElkPUEwMzg2MzkyMzJWMVNTVVM3RFBZMyZlbmNyeXB0ZWRBZElkPUEwMzEyMjY2MzU1OVMxSlE4VDJaNyZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "OPPO F19 (Midnight Blue, 6GB RAM, 128GB Storage)",
        "target_price": 17000
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")



    return product_price.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()