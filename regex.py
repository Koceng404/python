import re
import json


teks = '{"data":{"create_tweet":{"tweet_results":{"result":{"rest_id":"1665533975014567938","core":{"user_results":{"result":{"__typename":"User","id":"VXNlcjozNjYzNTUzMzk4","rest_id":"3663553398","affiliates_highlighted_label":{},"has_nft_avatar":false,"legacy":{"blocked_by":false,"blocking":false,"can_dm":true,"can_media_tag":true,"created_at":"Wed Sep 23 22:04:02 +0000 2015","default_profile":true,"default_profile_image":false,"description":"Nothing!","entities":{"description":{"urls":[]}},"fast_followers_count":0,"favourites_count":3995,"follow_request_sent":false,"followed_by":false,"followers_count":1102,"following":false,"friends_count":104,"has_custom_timelines":true,"is_translator":false,"listed_count":0,"location":"Solo","media_count":98673,"muting":false,"name":"\uD83D\uDCA6 Sukma","needs_phone_verification":false,"normal_followers_count":1102,"notifications":false,"pinned_tweet_ids_str":[],"possibly_sensitive":false,"profile_banner_url":"https://pbs.twimg.com/profile_banners/3663553398/1674260232","profile_image_url_https":"https://pbs.twimg.com/profile_images/1647795345869651969/BHv26ADu_normal.jpg","profile_interstitial_type":"","protected":false,"screen_name":"sukma_lelah","statuses_count":533387,"translator_type":"none","verified":false,"want_retweets":false,"withheld_in_countries":[]},"super_follow_eligible":false,"super_followed_by":false,"super_following":false}}},"unmention_info":{},"legacy":{"created_at":"Mon Jun 05 01:40:18 +0000 2023","conversation_id_str":"1596118935203893248","display_text_range":[14,106],"entities":{"media":[{"display_url":"pic.twitter.com/nPqn9JLIb2","expanded_url":"https://twitter.com/sukma_lelah/status/1665533975014567938/photo/1","id_str":"1665533967779659777","indices":[107,130],"media_url_https":"https://pbs.twimg.com/media/Fx0qUb7agAEoUqJ.jpg","type":"photo","url":"https://t.co/nPqn9JLIb2","features":{},"sizes":{"large":{"h":1080,"w":1080,"resize":"fit"},"medium":{"h":1080,"w":1080,"resize":"fit"},"small":{"h":680,"w":680,"resize":"fit"},"thumb":{"h":150,"w":150,"resize":"crop"}},"original_info":{"height":1080,"width":1080}}],"user_mentions":[{"id_str":"63433517","name":"3 Indonesia","screen_name":"triindonesia","indices":[0,13]}],"urls":[],"hashtags":[],"symbols":[]},"extended_entities":{"media":[{"display_url":"pic.twitter.com/nPqn9JLIb2","expanded_url":"https://twitter.com/sukma_lelah/status/1665533975014567938/photo/1","id_str":"1665533967779659777","indices":[107,130],"media_key":"3_1665533967779659777","media_url_https":"https://pbs.twimg.com/media/Fx0qUb7agAEoUqJ.jpg","type":"photo","url":"https://t.co/nPqn9JLIb2","features":{},"sizes":{"large":{"h":1080,"w":1080,"resize":"fit"},"medium":{"h":1080,"w":1080,"resize":"fit"},"small":{"h":680,"w":680,"resize":"fit"},"thumb":{"h":150,"w":150,"resize":"crop"}},"original_info":{"height":1080,"width":1080}}]},"favorite_count":0,"favorited":false,"full_text":"@triindonesia Terus berusahan untuk menjadi yang terbaik, \n\n susah banget tapi                      \n\n~ 37 https://t.co/nPqn9JLIb2","in_reply_to_screen_name":"sukma_lelah","in_reply_to_status_id_str":"1598518930779557888","in_reply_to_user_id_str":"3663553398","is_quote_status":false,"lang":"in","possibly_sensitive":false,"possibly_sensitive_editable":true,"quote_count":0,"reply_count":0,"retweet_count":0,"retweeted":false,"user_id_str":"3663553398","id_str":"1665533975014567938"}}}}}}'
              
babi = (f'{teks}')
textfile = ({babi})
matches = []
reg = re.compile(r'.*id_str\":\"([^\"]+)\".*')

for line in textfile:
     matches += reg.findall(line)
     print (matches)
 

 
example_string = (f'{teks}')
 
regex_pattern = r'.*id_str\":\"([^\"]+)\".*'
match = re.match(regex_pattern, example_string)
ambil = match.group(1)
f = open("logs.txt", "a")
f.write(f"{ambil} "+"\n")
f.close() 



print(ambil)
#textfile.close()

