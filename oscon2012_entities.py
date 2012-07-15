#!/usr/bin/env python
import requests
import json
from requests.auth import HTTPBasicAuth
#
# Get tweets w/ entities like hash tags, urls et al
#
# GET https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true
#          &include_rts=true&include_entities=true&user_id=ksankar
#
#
url='https://api.twitter.com/1/statuses/user_timeline.json'
payload={"screen_name":"ksankar","include_entities":"true"}
r = requests.get(url, params=payload)
print json.dumps(r.headers,sort_keys=True,indent=2)
print json.dumps(r.json,sort_keys=True,indent=2)
'''
Sample Output
{
  "cache-control": "no-cache, no-store, must-revalidate, pre-check=0, post-check=0",
  "content-encoding": "gzip",
  "content-length": "3625",
  "content-type": "application/json;charset=utf-8",
  "date": "Sat, 23 Jun 2012 03:21:55 GMT",
  "expires": "Tue, 31 Mar 1981 05:00:00 GMT",
  "last-modified": "Sat, 23 Jun 2012 03:21:55 GMT",
  "pragma": "no-cache",
  "server": "tfe",
  "set-cookie": "guest_id=\"v1:134042171518517476\";Expires=Mon, 23-Jun-14 03:21:55 GMT;Path=/;Domain=.twitter.com",
  "status": "200 OK",
  "x-frame-options": "SAMEORIGIN",
  "x-ratelimit-class": "api",
  "x-ratelimit-limit": "150",
  "x-ratelimit-remaining": "145",
  "x-ratelimit-reset": "1340424146",
  "x-transaction": "d4ccc45b3a7ca827"
}
[
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sat Jun 23 02:56:18 +0000 2012",
    "entities": {
      "hashtags": [
        {
          "indices": [
            0,
            20
          ],
          "text": "TheAdjustmentBureau"
        }
      ],
      "urls": [],
      "user_mentions": []
    },
    "favorited": false,
    "geo": null,
    "id": 216364026576384000,
    "id_str": "216364026576384000",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "#TheAdjustmentBureau Explore many paths knocking down obstacles;Freewill is a gift that you'll never know how to use until you fight for it",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sat Jun 23 00:49:57 +0000 2012",
    "entities": {
      "hashtags": [
        {
          "indices": [
            0,
            8
          ],
          "text": "Twitter"
        },
        {
          "indices": [
            132,
            140
          ],
          "text": "Oscon12"
        }
      ],
      "urls": [
        {
          "display_url": "goo.gl/fpxVE",
          "expanded_url": "http://goo.gl/fpxVE",
          "indices": [
            111,
            131
          ],
          "url": "http://t.co/pV3qxChr"
        }
      ],
      "user_mentions": [
        {
          "id": 20,
          "id_str": "20",
          "indices": [
            23,
            26
          ],
          "name": "Evan Williams",
          "screen_name": "ev"
        },
        {
          "id": 18,
          "id_str": "18",
          "indices": [
            31,
            36
          ],
          "name": "Adam Rugel",
          "screen_name": "Adam"
        },
        {
          "id": 16,
          "id_str": "16",
          "indices": [
            61,
            68
          ],
          "name": "Jeremy",
          "screen_name": "jeremy"
        },
        {
          "id": 15,
          "id_str": "15",
          "indices": [
            73,
            81
          ],
          "name": "crystal",
          "screen_name": "crystal"
        },
        {
          "id": 14,
          "id_str": "14",
          "indices": [
            86,
            91
          ],
          "name": "noah glass",
          "screen_name": "noah"
        },
        {
          "id": 13,
          "id_str": "13",
          "indices": [
            96,
            100
          ],
          "name": "Biz Stone",
          "screen_name": "biz"
        },
        {
          "id": 12,
          "id_str": "12",
          "indices": [
            105,
            110
          ],
          "name": "Jack Dorsey",
          "screen_name": "jack"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 216332231516491776,
    "id_str": "216332231516491776",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "#Twitter Trivia Id :20 @ev :18 @adam :17@tonystubblebine :16 @jeremy :15 @crystal :14 @noah :13 @biz :12 @jack http://t.co/pV3qxChr #Oscon12",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Thu Jun 21 05:12:14 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/xnDlY",
          "expanded_url": "http://goo.gl/xnDlY",
          "indices": [
            93,
            113
          ],
          "url": "http://t.co/ziDhnBBF"
        }
      ],
      "user_mentions": [
        {
          "id": 24925573,
          "id_str": "24925573",
          "indices": [
            0,
            11
          ],
          "name": "OKC THUNDER",
          "screen_name": "okcthunder"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 215673460565884929,
    "id_str": "215673460565884929",
    "in_reply_to_screen_name": "okcthunder",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": 24925573,
    "in_reply_to_user_id_str": "24925573",
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "@okcThunder The team is built upon a foundation of togetherness, brotherhood &amp; chemistry http://t.co/ziDhnBBF",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Thu Jun 21 04:41:42 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/hNBTl",
          "expanded_url": "http://goo.gl/hNBTl",
          "indices": [
            118,
            138
          ],
          "url": "http://t.co/7TTxzVNr"
        }
      ],
      "user_mentions": [
        {
          "id": 19923144,
          "id_str": "19923144",
          "indices": [
            139,
            143
          ],
          "name": "NBA",
          "screen_name": "NBA"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 215665776387043328,
    "id_str": "215665776387043328",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "This game is about makes &amp; misses;some nights you'll make/some nights you'll miss;but your effort has to be there http://t.co/7TTxzVNr @NBA",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Thu Jun 21 04:37:07 +0000 2012",
    "entities": {
      "hashtags": [
        {
          "indices": [
            0,
            14
          ],
          "text": "MarioChalmers"
        }
      ],
      "urls": [
        {
          "display_url": "goo.gl/hNBTl",
          "expanded_url": "http://goo.gl/hNBTl",
          "indices": [
            116,
            136
          ],
          "url": "http://t.co/7TTxzVNr"
        }
      ],
      "user_mentions": [
        {
          "id": 11026952,
          "id_str": "11026952",
          "indices": [
            15,
            25
          ],
          "name": "Miami HEAT",
          "screen_name": "MiamiHEAT"
        },
        {
          "id": 19923144,
          "id_str": "19923144",
          "indices": [
            26,
            30
          ],
          "name": "NBA",
          "screen_name": "NBA"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 215664622378819584,
    "id_str": "215664622378819584",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "#MarioChalmers @miamiheat @NBA \"A player with ample amounts of confidence, a self belief that can be very powerful\" http://t.co/7TTxzVNr",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 17 21:18:03 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/ikIHI",
          "expanded_url": "http://goo.gl/ikIHI",
          "indices": [
            69,
            89
          ],
          "url": "http://t.co/fLdcatmr"
        }
      ],
      "user_mentions": [
        {
          "id": 235261861,
          "id_str": "235261861",
          "indices": [
            57,
            68
          ],
          "name": "RStudio",
          "screen_name": "rstudioapp"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 214466965664825344,
    "id_str": "214466965664825344",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "\"Keep You Ideas Flexible &amp; Don't Ignore Details\" via @rstudioapp http://t.co/fLdcatmr",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Mon Jun 11 15:50:35 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/G6B1p",
          "expanded_url": "http://goo.gl/G6B1p",
          "indices": [
            120,
            140
          ],
          "url": "http://t.co/3vOg8x9H"
        }
      ],
      "user_mentions": [
        {
          "id": 691353,
          "id_str": "691353",
          "indices": [
            103,
            107
          ],
          "name": "Joi Ito",
          "screen_name": "Joi"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 212210225862811650,
    "id_str": "212210225862811650",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "Resilience instead of Strength;System focus  not Objects;Compasses not Maps;Practice instead of Theory @Joi MITMediaLab http://t.co/3vOg8x9H",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 10 19:06:33 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/M8Blc",
          "expanded_url": "http://goo.gl/M8Blc",
          "indices": [
            124,
            144
          ],
          "url": "http://t.co/lYevF6Hu"
        }
      ],
      "user_mentions": [
        {
          "id": 2425151,
          "id_str": "2425151",
          "indices": [
            0,
            9
          ],
          "name": "Facebook",
          "screen_name": "facebook"
        },
        {
          "id": 543377798,
          "id_str": "543377798",
          "indices": [
            99,
            114
          ],
          "name": "Friedman's Thoughts",
          "screen_name": "TheTomFriedman"
        },
        {
          "id": 807095,
          "id_str": "807095",
          "indices": [
            115,
            123
          ],
          "name": "The New York Times",
          "screen_name": "nytimes"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 211897157698076672,
    "id_str": "211897157698076672",
    "in_reply_to_screen_name": "facebook",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": 2425151,
    "in_reply_to_user_id_str": "2425151",
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "@Facebook helps communication;not collaboration i.e.leadership &amp; the ability to get stuff done @TheTomFriedman @nytimes http://t.co/lYevF6Hu",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 10 17:15:02 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/beSDC",
          "expanded_url": "http://goo.gl/beSDC",
          "indices": [
            62,
            82
          ],
          "url": "http://t.co/sWTCz7uA"
        }
      ],
      "user_mentions": [
        {
          "id": 8669812,
          "id_str": "8669812",
          "indices": [
            106,
            117
          ],
          "name": "Eytan Levit",
          "screen_name": "eytanlevit"
        },
        {
          "id": 33696409,
          "id_str": "33696409",
          "indices": [
            118,
            124
          ],
          "name": "Quora",
          "screen_name": "Quora"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 211869093693882368,
    "id_str": "211869093693882368",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 1,
    "retweeted": false,
    "source": "web",
    "text": "Startups: What does it feel like to be the CEO of a start-up? http://t.co/sWTCz7uA Well written answer by @eytanlevit @quora Took him 3 wks!",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 10 07:03:05 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/oMRpu",
          "expanded_url": "http://goo.gl/oMRpu",
          "indices": [
            123,
            143
          ],
          "url": "http://t.co/xYsa4AYU"
        }
      ],
      "user_mentions": []
    },
    "favorited": false,
    "geo": null,
    "id": 211715091647823872,
    "id_str": "211715091647823872",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "Rally was brash &amp; ostentatious. 3 towering figures rose above the fray,declaring their supremacy in bold,broad strokes http://t.co/xYsa4AYU",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 10 05:53:40 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [],
      "user_mentions": [
        {
          "id": 489750466,
          "id_str": "489750466",
          "indices": [
            0,
            12
          ],
          "name": "Monte Poole",
          "screen_name": "1MontePoole"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 211697620358414336,
    "id_str": "211697620358414336",
    "in_reply_to_screen_name": "1MontePoole",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": 489750466,
    "in_reply_to_user_id_str": "489750466",
    "place": null,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "@1MontePoole You got your wish. BTW, great article !",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Sun Jun 10 04:51:53 +0000 2012",
    "entities": {
      "hashtags": [
        {
          "indices": [
            49,
            61
          ],
          "text": "LebronJames"
        },
        {
          "indices": [
            62,
            74
          ],
          "text": "KevinDurant"
        }
      ],
      "urls": [
        {
          "display_url": "goo.gl/hNa0m",
          "expanded_url": "http://goo.gl/hNa0m",
          "indices": [
            120,
            140
          ],
          "url": "http://t.co/HD1zghRm"
        }
      ],
      "user_mentions": [
        {
          "id": 11026952,
          "id_str": "11026952",
          "indices": [
            0,
            10
          ],
          "name": "Miami HEAT",
          "screen_name": "MiamiHEAT"
        },
        {
          "id": 14148317,
          "id_str": "14148317",
          "indices": [
            15,
            29
          ],
          "name": "BostonCeltics",
          "screen_name": "BostonCeltics"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 211682070181838850,
    "id_str": "211682070181838850",
    "in_reply_to_screen_name": "MiamiHEAT",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": 11026952,
    "in_reply_to_user_id_str": "11026952",
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "@MiamiHeat ovr @BostonCeltics Looking forward to #LebronJames #KevinDurant \"immediate greatness vs enduring excellence\" http://t.co/HD1zghRm",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Tue Jun 05 04:53:38 +0000 2012",
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "display_url": "goo.gl/oRpoa",
          "expanded_url": "http://goo.gl/oRpoa",
          "indices": [
            87,
            107
          ],
          "url": "http://t.co/9oLgSEdq"
        }
      ],
      "user_mentions": [
        {
          "id": 269300372,
          "id_str": "269300372",
          "indices": [
            108,
            122
          ],
          "name": "Vikram Mansharamani",
          "screen_name": "boombustology"
        }
      ]
    },
    "favorited": false,
    "geo": null,
    "id": 209870572631502848,
    "id_str": "209870572631502848",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "The future may belong to generalists because they are better at navigating uncertainty http://t.co/9oLgSEdq @boombustology",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  },
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Mon Jun 04 16:18:52 +0000 2012",
    "entities": {
      "hashtags": [
        {
          "indices": [
            62,
            68
          ],
          "text": "Quora"
        }
      ],
      "urls": [
        {
          "display_url": "goo.gl/sHZSH",
          "expanded_url": "http://goo.gl/sHZSH",
          "indices": [
            69,
            89
          ],
          "url": "http://t.co/xHmsPkZY"
        }
      ],
      "user_mentions": []
    },
    "favorited": false,
    "geo": null,
    "id": 209680628059344897,
    "id_str": "209680628059344897",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "place": null,
    "possibly_sensitive": false,
    "retweet_count": 0,
    "retweeted": false,
    "source": "web",
    "text": "My answer to \"What do successful startups have in common?\" at #Quora http://t.co/xHmsPkZY What says thee ?",
    "truncated": false,
    "user": {
      "contributors_enabled": false,
      "created_at": "Sat Aug 23 21:06:58 +0000 2008",
      "default_profile": false,
      "default_profile_image": false,
      "description": "Technologist - Semantic Social Networking = DeComplexify-Contextualize-Network-Reason &amp; then Infer",
      "favourites_count": 8,
      "follow_request_sent": null,
      "followers_count": 217,
      "following": null,
      "friends_count": 59,
      "geo_enabled": true,
      "id": 15960972,
      "id_str": "15960972",
      "is_translator": false,
      "lang": "en",
      "listed_count": 33,
      "location": "San Jose, CA",
      "name": "ksankar",
      "notifications": null,
      "profile_background_color": "EDECE9",
      "profile_background_image_url": "http://a0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme3/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http://a0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_image_url_https": "https://si0.twimg.com/profile_images/76311317/AH09397_full_normal.jpg",
      "profile_link_color": "088253",
      "profile_sidebar_border_color": "D3D2CF",
      "profile_sidebar_fill_color": "E3E2DE",
      "profile_text_color": "634047",
      "profile_use_background_image": true,
      "protected": false,
      "screen_name": "ksankar",
      "show_all_inline_media": false,
      "statuses_count": 953,
      "time_zone": "Pacific Time (US & Canada)",
      "url": "http://doubleclix.wordpress.com/about/",
      "utc_offset": -28800,
      "verified": false
    }
  }
]

'''
