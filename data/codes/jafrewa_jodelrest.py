import stringimport randomimport jsonimport base64
import requests
__author__ = 'Jan'
'''Locations are formatted like this.location = {'latitude' : 0, 'longtitude' : 0, 'city' : 'City'}'''
class RESTClient(object): API_URL = 'https://api.go-tellm.com/api/v2'
 BASE_HEADERS = {"Connection": "keep-alive", "Accept-Encoding": "gzip", "Content-Type": "application/json; charset=UTF-8"}
 USER_AGENT = 'Jodel/65000 Dalvik/2.1.0 (Linux; U; Android 5.1.1; D6503 Build/23.4.A.1.232)'


 def new_device_uid(self): return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(63))
 def get_access_token(self):        city = self.location['city']        latitude = self.location['latitude']        longtitude = self.location['longtitude']        payload = {"client_id": "81e8a76e-1e02-4d17-9ba0-8a7020261b26", "device_uid": self.new_device_uid(), "location":                       {"loc_accuracy": 19.0, "city": city, "loc_coordinates":                            {"lat": latitude, "lng": longtitude}, "country": "DE"}                   }
        json_payload = json.dumps(payload)
 return self.do_post("/users/", json_payload).json()
 def get_karma(self): return self.do_get("/users/karma").json()['karma']
 def get_posts(self): return self.do_get("/posts/").json()['posts']
 def get_posts_raw(self): return self.do_get("/posts/").content
 def do_delete(self, url): return requests.delete(url, headers=self.headers)
 def set_pos(self, longtitude, latitude, city, country="DE"):        payload = {"location":                       {"loc_accuracy": 19.0, "city": city, "loc_coordinates":                            {"lat": latitude, "lng": longtitude}, "country": country}                   }
 self.location = {'latitude' : latitude, 'longtitude' : longtitude, 'city' : city}
        json_payload = json.dumps(payload)
 return self.do_put("/users/place", json_payload).content
 def post(self, text, country="DE", color="DD5F5F"):        city = self.location['city']        latitude = self.location['latitude']        longtitude = self.location['longtitude']        payload = {"color": color, "location":                       {"loc_accuracy": 10.0, "city": city, "loc_coordinates":                            {"lat": latitude, "lng": longtitude}, "country": country, "name": "41"}, "message": text                   }        json_payload = json.dumps(payload)
 return self.do_post("/posts/", json_payload)
 def post_comment(self, ancestor, text, country="DE", color="DD5F5F"):        city = self.location['city']        latitude = self.location['latitude']        longtitude = self.location['longtitude']        payload = {"ancestor": ancestor, "color": color, "location":                       {"loc_accuracy": 10.0, "city": city, "loc_coordinates":                            {"lat": latitude, "lng": longtitude}, "country": country, "name": "41"}, "message": text                   }        json_payload = json.dumps(payload)
 return self.do_post("/posts/", json_payload)
 def delete(self, postid): return self.do_delete('/posts/%s' % postid).content
 def post_image(self, file, country="DE", color="DD5F5F"):        city = self.location['city']        latitude = self.location['latitude']        longtitude = self.location['longtitude'] with open(file, "rb") as image_file:            encoded_string = base64.b64encode(image_file.read())        payload = {"color": color, "image": encoded_string, "location":                       {"loc_accuracy": 10.0, "city": city, "loc_coordinates":                            {"lat": latitude, "lng": longtitude}, "country": country, "name": "41"}, "message": "photo"                   }        json_payload = json.dumps(payload) return self.do_post("/posts/", json_payload)
 def get_my_posts(self): return self.do_get("/posts/mine/").content
 def upvote(self, postid): return self.do_put("/posts/%s/upvote" % postid, None).json()
 def downvote(self, postid): return self.do_put("/posts/%s/downvote" % postid, None).json()
 def new_acc(self):        access = self.get_access_token() self.set_pos(self.location['longtitude'], self.location['latitude'], self.location['city']) return "Bearer %s" % access['access_token']
 def __init__(self, location, auth=None, enable_tor=False): self.tor_enabled = enable_tor if self.tor_enabled: import socks import socket
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)            socket.socket = socks.socksocket
 self.headers = dict(self.BASE_HEADERS) self.headers['User-Agent'] = self.USER_AGENT self.location = location if auth is None:            auth = self.new_acc() self.headers['Authorization'] = auth self.auth = auth
 def do_post(self, url, payload): return requests.post("%s%s" % (self.API_URL, url), data=payload, headers=self.headers)
 def do_get(self, url): return requests.get("%s%s" % (self.API_URL, url), headers=self.headers)
 def do_put(self, url, payload=None): return requests.put("%s%s" % (self.API_URL, url), data=payload, headers=self.headers)
 def do_post(self, url, payload): return requests.post("%s%s" % (self.API_URL, url), data=payload, headers=self.headers)
 def close(self):        requests.session().close()