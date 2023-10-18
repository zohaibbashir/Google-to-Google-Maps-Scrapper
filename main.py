

from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse
from bs4 import BeautifulSoup

l1=[]
l2=[]
  # Lists

name_list = []
address_list = []
address_line_list = []
area_list = []
zip_code_list = []
country_list = []
located_in_list = []
website_list = []
phone_number_list = []
reviews_count_list = []
reviews_average_list = []
in_store_shopping_list = []
in_store_pickup_list = []
store_delivery_list = []
place_type_list = []
opens_at_list = []
about_list = []
orders_links1_list = []
orders_links2_list = []
orders_links3_list = []
facebook_link_list = []
twitter_link_list = []
instagram_link_list = []
tiktok_link_list = []
linkedin_link_list = []



Name = ""
Address = ""
Address_line = ""
Area = ""
Zip_Code = ""
Country = ""
Located_In = ""
Website = ""
Phone_Number = ""
Reviews_Count = 0
Reviews_Average = 0
In_Store_Shopping = ""
In_Store_Pickup = ""
Store_Delivery = ""
Place_Type = ""
Opens_At = ""
About = ""

Orders_Links1 = ""
Orders_Links2 = ""
Orders_Links3 = ""
Facebook_Link = ""
Twitter_Link = ""
Instagram_Link = ""
TikTok_Link = ""
Linkedin_Link = ""

  




def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com", timeout=60000)
        
        page.wait_for_timeout(1000)

        page.locator('//textarea[@type="search"]').fill(search_for)
        page.wait_for_timeout(1000)

        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)
        

        # scrolling
        #page.hover('//a[contains(@href, "https://www.google.com/maps/place")]')

        

        xpath='//div[@class="iNTie"]//a'
        more_locations_link = page.locator(xpath)
        # print(more_locations_link)
        if more_locations_link:
            more_locations_link.click()
            page.wait_for_timeout(1000)
        
        
        

        
        Page_Count=1
        while True:
            
            page.hover('//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]')
            previously_counted = 0
            while True:
                page.mouse.wheel(0, 10000)
                page.wait_for_timeout(3000)

                if (page.locator('//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]').count() >= total):
                    listings = page.locator( '//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]').all()[:total]
                    listings = [listing.locator("xpath=..") for listing in listings]
                    print(f"Total Listings Found: {len(listings)} on Page: {Page_Count}")
                    break
                else:
                    
                    if (page.locator( '//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]').count()== previously_counted ):
                        listings = page.locator( '//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]').all()
                        print(f"Arrived at all available\nTotal Listings Found: {len(listings)} on Page: {Page_Count}")
                        break
                    else:
                        previously_counted = page.locator('//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]' ).count()
                        print(f"Current Listings Found: ", page.locator( '//div[@class="VkpGBb"]//a[contains(@jsname,"kj0dLd")]').count(), )

            
            page_content = page.content()
            soup = BeautifulSoup(page_content, 'html.parser')
            next_page=soup.find_all("td", {"class" : "d6cvqb BBwThe"})
            Page_Count+=1
                
            # scraping
            for listing in listings:
                listing.click()
                check_here=False
                page.wait_for_timeout(5000)

                name_xpath = '//div[@class="SPZz6b"]//h2'
                address_xpath = '//span[@class="LrzXr"]'
                website_xpath = '//div[@class="PDzHbe" and text()="Website"]/ancestor::a[1]'
                phone_number_xpath = '//span[@class="LrzXr zdqRlf kno-fv"]'
                reviews_count_xpath = '//div[@class="CJQ04"]//span[@class="RDApEe YrbPuc"]'
                reviews_average_xpath = '//div[@class="CJQ04"]//span[@class="yi40Hd YrbPuc"]'
                
                # services='//div[@class="wDYxhc NFQFxe viOShc"]//div[contains(@data-hveid,"CB")]'#store
                services='//div[@class="wDYxhc NFQFxe viOShc"]//div[contains(@data-hveid,"CB")]//..//div//span[contains(text(),"Service")]//..//..//div'
                services2='//div[@class="wDYxhc NFQFxe"]//div[contains(@data-hveid,"CB") and (text())]'
                opens_at_xpath='//span[@class="JjSWRd"]'#time
                place_type_xpath='//span[@class="YhemCb" and not(@data-ved)]'#type of place
                intro_xpath='//div[@class="wDYxhc NFQFxe"]//c-wiz[@jsrenderer="bHxjwf"]'
                located_in_xpath='//div[@class="zloOqf pNrDqb"]//a'
                orders_xpath='//div[@class="JV5xkf"]//div//b[contains(text(),"Order")]//..//a[1]'
                check_order_xpath='//div[@class="JV5xkf"]//div//b[contains(text(),"Order")]'
                orders_xpath2='//div[@class="JV5xkf"]//div//b[contains(text(),"Order")]//..//a[2]'
                orders_xpath3='//div[@class="JV5xkf"]//div//b[contains(text(),"Order")]//..//a[3]'
                
                
                facebook_xpath='//div[@class="OOijTb P6Tjc gDQYEd Dy8CGd"]//div[@class="PZPZlf dRrfkf kno-vrt-t"]//a[contains(@href,"face")]'
                insta_xpath='//div[@class="OOijTb P6Tjc gDQYEd Dy8CGd"]//div[@class="PZPZlf dRrfkf kno-vrt-t"]//a[contains(@href,"insta")]'
                twitter_xpath='//div[@class="OOijTb P6Tjc gDQYEd Dy8CGd"]//div[@class="PZPZlf dRrfkf kno-vrt-t"]//a[contains(@href,"twit")]'
                tiktok_xpath='//div[@class="OOijTb P6Tjc gDQYEd Dy8CGd"]//div[@class="PZPZlf dRrfkf kno-vrt-t"]//a[contains(@href,"tiktok")]'
                linkedin_xpath='//div[@class="OOijTb P6Tjc gDQYEd Dy8CGd"]//div[@class="PZPZlf dRrfkf kno-vrt-t"]//a[contains(@href,"linkedin")]'
                
                
                if page.locator(intro_xpath).count() > 0:
                    temp = page.locator(intro_xpath).inner_text()
                    temp=temp.split('\n')
                    About=temp[1].replace('...  More','')
                    about_list.append(About)
                else:
                    About = "Not Given"
                    about_list.append(About)
                

                if page.locator(facebook_xpath).count() > 0:
                    temp = page.locator(facebook_xpath)
                    href_value = temp.get_attribute('href')
                    Facebook_Link = href_value
                    facebook_link_list.append(Facebook_Link)
                else:
                    Facebook_Link = "Not Given"
                    facebook_link_list.append(Facebook_Link)


                if page.locator(tiktok_xpath).count() > 0:
                    temp = page.locator(tiktok_xpath)
                    href_value = temp.get_attribute('href')
                    TikTok_Link = href_value
                    tiktok_link_list.append(TikTok_Link)
                else:
                    TikTok_Link = "Not Given"
                    tiktok_link_list.append(TikTok_Link)
                

                if page.locator(linkedin_xpath).count() > 0:
                    temp = page.locator(linkedin_xpath)
                    href_value = temp.get_attribute('href')
                    Linkedin_Link = href_value
                    linkedin_link_list.append(Linkedin_Link)
                else:
                    Linkedin_Link = "Not Given"
                    linkedin_link_list.append(Linkedin_Link)

                
                
                if page.locator(twitter_xpath).count() > 0:
                    temp = page.locator(twitter_xpath)
                    href_value = temp.get_attribute('href')
                    Twitter_Link = href_value
                    twitter_link_list.append(Twitter_Link)
                else:
                    Twitter_Link = "Not Given"
                    twitter_link_list.append(Twitter_Link)

                if page.locator(insta_xpath).count() > 0:
                    temp = page.locator(insta_xpath)
                    href_value = temp.get_attribute('href')
                    Instagram_Link = href_value
                    instagram_link_list.append(Instagram_Link)
                else:
                    Instagram_Link = "Not Given"
                    instagram_link_list.append(Instagram_Link)


                if page.locator(orders_xpath).count() > 0:
                    temp = page.locator(orders_xpath)
                    href_value = temp.get_attribute('href')
                    Orders_Links1=href_value
                    orders_links1_list.append(Orders_Links1)
                else:
                    Orders_Links1 = "Not Given"
                    orders_links1_list.append(Orders_Links1)


                if page.locator(orders_xpath2).count() > 0:
                    temp = page.locator(orders_xpath2)
                    href_value = temp.get_attribute('href')
                    Orders_Links2=href_value
                    orders_links2_list.append(Orders_Links2)
                else:
                    Orders_Links2 = "Not Given"
                    orders_links2_list.append(Orders_Links2)
                
                if page.locator(orders_xpath3).count() > 0:
                    temp = page.locator(orders_xpath3)
                    href_value = temp.get_attribute('href')
                    Orders_Links3=href_value
                    orders_links3_list.append(Orders_Links3)
                else:
                    Orders_Links3 = "Not Given"
                    orders_links3_list.append(Orders_Links3)

                if page.locator(located_in_xpath).count() > 0:
                    Located_In = page.locator(located_in_xpath).inner_text()
                    located_in_list.append(Located_In)
                else:
                    Located_In = "Not Given"
                    located_in_list.append(Located_In)
                
                if page.locator(reviews_count_xpath).count() > 0:
                    temp = page.locator(reviews_count_xpath).inner_text()
                    temp=temp.replace('(','').replace(')','').replace(',','')
                    if 'K' in temp:
                        num = int(float(temp.replace('K', '')) * 1000)
                        Reviews_Count=int(num)
                    else:
                        Reviews_Count=int(temp)
                    reviews_count_list.append(Reviews_Count)
                else:
                    Reviews_Count = ""
                    reviews_count_list.append(Reviews_Count)

                if page.locator(reviews_average_xpath).count() > 0:
                    temp = page.locator(reviews_average_xpath).inner_text()
                    temp=temp.replace(' ','')
                    Reviews_Average=float(temp)
                    reviews_average_list.append(Reviews_Average)
                else:
                    Reviews_Average = ""
                    reviews_average_list.append(Reviews_Average)


                if page.locator(services).count() > 0:
                    temp = page.locator(services).inner_text()
                    check_here=True
                    if 'Service options' not in temp:
                        In_Store_Shopping = "No"
                        In_Store_Pickup = "No"
                        Store_Delivery = "No"
                        in_store_shopping_list.append(In_Store_Shopping)
                        in_store_pickup_list.append(In_Store_Pickup)
                        store_delivery_list.append(Store_Delivery)
                    else:
                        temp=temp.replace('\xa0','')
                       
                        if 'shop' in temp:
                            In_Store_Shopping = 'Yes'
                            
                            
                        else:
                            In_Store_Shopping = 'No'
                            
                            
                            

                        if 'pick' in temp:
                            In_Store_Pickup = 'Yes'
                            
                        else:
                            In_Store_Pickup = 'No'
                            

                        if 'Delivery' in temp:
                            Store_Delivery = 'Yes'
                            
                        else:
                            Store_Delivery = 'No'
                        in_store_shopping_list.append(In_Store_Shopping)
                        in_store_pickup_list.append(In_Store_Pickup)
                        store_delivery_list.append(Store_Delivery)
                            
                else:
                    #l1.append("")
                    In_Store_Shopping = "No"
                    In_Store_Pickup = "No"
                    Store_Delivery = "No"
                    in_store_shopping_list.append(In_Store_Shopping)
                    in_store_pickup_list.append(In_Store_Pickup)
                    store_delivery_list.append(Store_Delivery)
                
                if check_here:
                    check_here=False
                    if page.locator(services2).count() > 0:
                        temp = page.locator(services2).inner_text()
                        if 'Service options' not in temp:
                            In_Store_Shopping = "No"
                            In_Store_Pickup = "No"
                            Store_Delivery = "No"
                            in_store_shopping_list.append(In_Store_Shopping)
                            in_store_pickup_list.append(In_Store_Pickup)
                            store_delivery_list.append(Store_Delivery)
                        else:
                            temp=temp.replace('\xa0','')
                            #print(temp)
                            #l1.append(temp)
                            if 'shop' in temp:
                                In_Store_Shopping = 'Yes'
                            else:
                                In_Store_Shopping = 'No'

                            if 'pick' in temp:
                                In_Store_Pickup = 'Yes'
                            else:
                                In_Store_Pickup = 'No'

                            if 'Delivery' in temp:
                                Store_Delivery = 'Yes'
                            else:
                                Store_Delivery = 'No'
                            in_store_shopping_list.append(In_Store_Shopping)
                            in_store_pickup_list.append(In_Store_Pickup)
                            store_delivery_list.append(Store_Delivery)
                else:
                    #l1.append("")
                    In_Store_Shopping = "No"
                    In_Store_Pickup = "No"
                    Store_Delivery = "No"
                    in_store_shopping_list.append(In_Store_Shopping)
                    in_store_pickup_list.append(In_Store_Pickup)
                    store_delivery_list.append(Store_Delivery)

                

                if page.locator(opens_at_xpath).count() > 0:
                    opens = page.locator(opens_at_xpath).inner_text()
                    opens=opens.split('⋅')
                    if(len(opens)>1):
                        opens=opens[1]
                        opens=opens.replace("\u202f","")
                    else:
                        opens=str(opens).replace("\u202f","")
                    Opens_At=opens
                    opens_at_list.append(Opens_At)
                else:
                    Opens_At = "Not Given"
                    opens_at_list.append(Opens_At)
            

                if page.locator(name_xpath).count() > 0:
                    Name = page.locator(name_xpath).inner_text()
                    name_list.append(Name)
                else:
                    Name = ""
                    name_list.append(Name)

                if page.locator(address_xpath).count() > 0:
                    Address = page.locator(address_xpath).inner_text()
                    address_list.append(Address)
                    address_token= page.locator(address_xpath).inner_text()
                    address_token=address_token.split(', ')
                    if(len(address_token))==5:
                        Address_line=address_token[0] + address_token[1]
                        Area=address_token[2]
                        Zip_Code=address_token[3]
                        Country=address_token[4]
                    else:
                        Address_line=address_token[0]
                        Area=address_token[1]
                        Zip_Code=address_token[2]
                        Country=address_token[3]
                    address_line_list.append(Address_line)
                    area_list.append(Area)
                    zip_code_list.append(Zip_Code)
                    country_list.append(Country)

                else:
                    Address = "Not Given"
                    address_list.append(Address)

                if page.locator(website_xpath).count() > 0:
                    temp = page.locator(website_xpath)
                    href_value = temp.get_attribute('href')
                    Website=href_value
                    website_list.append(Website)
                else:
                    Website = "Not Given"
                    website_list.append(Website)

                if page.locator(phone_number_xpath).count() > 0:
                    Phone_Number = page.locator(phone_number_xpath).inner_text()
                    phone_number_list.append(Phone_Number)
                else:
                    Phone_Number = "Not Given"
                    phone_number_list.append(Phone_Number)


                if page.locator(place_type_xpath).count() > 0:
                    Place_Type = page.locator(place_type_xpath).inner_text()
                    place_type_list.append(Place_Type)
                else:
                    Place_Type = "Not Given"
                    place_type_list.append(Place_Type)
                
                
                

                #conditions for next page
            go_to_next_page=False
            for check in next_page:
                con=check.find("a", {"id": "pnnext"})
                if(con):
                    go_to_next_page=True
                else:
                    continue
            if(go_to_next_page):
                xpath='//table[@class="AaVjTc"]//td[@class="d6cvqb BBwThe"][2]//a'
                more_locations_link = page.locator(xpath)
                # print(more_locations_link)
                if more_locations_link:
                    more_locations_link.click()
                    page.wait_for_timeout(5000)

            else:
                break

       
        browser.close()
        df = pd.DataFrame(list(zip(name_list, address_list, address_line_list, area_list, zip_code_list, country_list, located_in_list, website_list,phone_number_list,reviews_count_list, reviews_average_list,in_store_shopping_list,in_store_pickup_list,store_delivery_list,place_type_list, opens_at_list,about_list,orders_links1_list,orders_links2_list,orders_links3_list, facebook_link_list, twitter_link_list, instagram_link_list, tiktok_link_list,linkedin_link_list)),
                           columns =["Name","Address","Address Line","Area","Zip Code", "Country", "Located in", "Website", "Phone Number", "Reviews Count", "Reviews Average","In Store Shopping", "In Store Pickup","Store Delivery","Place Type","Opens at","About","Orders Links1", "Orders Links2", "Orders Links3", "Facebook Link", "Twitter Link", "Instagram Link", "TikTok Link", "Linkedin Link"])
        columns_to_delete = []
        for col in df.columns:
            if df[col].nunique() == 1:
                columns_to_delete.append(col)

        df.drop(columns=columns_to_delete, inplace=True)
        df.to_csv(r'results.csv', index = False)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
    parser.add_argument("-t", "--total", type=int)
    args = parser.parse_args()

    if args.search:
        search_for = args.search
    else:
       
        search_for = "subways restaurants in us"

    
    if args.total:
        total = args.total
    else:
        total = 1

    main()
