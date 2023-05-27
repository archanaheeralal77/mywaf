# How to Evaluate WAF

We can use EvalWAF python script to test any WAF, if we run the script it will help to identify if WAF rules are being triggered or not.

Python should be already installed to run the script.

Once you Run the script you can see below HTTP response, if WAF rule triggered and WAF is under BLOCK/DENY mode, most of the WAF serves **403 error status code**:

which means WAF rule has been triggered

< **HTTP/2 403 **
< server: Varnish
< retry-after: 0
< content-type: text/plain
< accept-ranges: bytes
< via: 1.1 varnish, 1.1 varnish
< edge-control: max-age=120
< date: Sat, 27 May 2023 04:18:04 GMT
< strict-transport-security: max-age=63072000; includeSubDomains; preload
< x-served-by: cache-qpg1227-QPG, cache-hyd1100020-HYD
< x-cache: MISS, MISS
< x-cache-hits: 0, 0
< x-timer: S1685161085.616294,VS0,VE49
< content-length: 13
< 


If WAF rule is not triggered then then it will send 200 OK HTTP response code:

**< HTTP/2 200 
< content-type: text/html;charset=UTF-8
< set-cookie: mgaff_1=untracked; Max-Age=604800; Path=/; Secure; SameSite=Lax
< x-ua-compatible: IE=edge
< x-xoom-requestid: d80c6c95-61f7-4de6-93d7-034f4a5dec2c
< etag: "01f7bd82c35945ba6450cd53286f7a6a6"
< content-language: en-US
< set-cookie: AB_1=4641509365409731584; Max-Age=2147483647; Path=/; Secure; SameSite=Lax
< set-cookie: ts=vr%3D1c772e2766a24c08cce0b6ffcf7bbd6e%26vteXpYrS%3D1685163186%26vt%3D5722bb7f530646f1c60cb6ffcf7bbd6e%26vtyp%3Dnew%26vreXpYrS%3D1779769386; Max-Age=94608000; Domain=.xoom.com; Path=/; Secure; HttpOnly; SameSite=Lax
< set-cookie: xReCo=US; Max-Age=31536000;  Path=/; Secure; SameSite=Lax
< set-cookie: FGP_1=3fe0a61d-b090-4498-c4c4-b6ffcf7bbd6e; Max-Age=900; Path=/; Secure; HttpOnly; SameSite=Lax
< set-cookie: xTZ=America%2FLos_Angeles; Max-Age=31536000;  Path=/; Secure; SameSite=Lax
< set-cookie: xSoCu=USD; Max-Age=31536000;  Path=/; Secure; SameSite=Lax
< set-cookie: xGDPR=0; Max-Age=2018304000;  Path=/; Secure; SameSite=Lax
< set-cookie: loc_1=en_US; Max-Age=31536000;  Path=/; Secure; SameSite=Lax
< set-cookie: enforce_policy=ccpa; Max-Age=604800;  Path=/; Secure; SameSite=Lax
< set-cookie: referringUrl_1=; Max-Age=604800; Path=/; Secure; SameSite=Lax
**

We can use rl1.py script to test the rate limiting rule of WAF.

What is Rate Limit Rule --> RL WAF rule protects application from volumetric attack.
In the rate limit rule of WAF we can set the threshold to limit the http request.

What is volumetric attack? --> when attacker tries to send multiple request to dos your application. an attack can send milions of request in 1 minute on your application, in that case if your origin server is not upscalled then origin server will not be able to take the load and can be dosed or application can be crashed

Example: www.example.com/loginpage/ attacker might try to dos this login page by sending multiple request 

1000000 request/min

So using Rate Limit rule we can set the threshold to limit the request.

If you want only 100 request should be allowed for this page, then we can set the threashold to 100 req/min, if any request breaches the threshold then WAF will block the IP for certain time [Mostly 10 min is the penalty box] then request will not be allowed for the attackers IP for 10 mins.

After 10 min if any request triggers from the same attacker IP again request will be matched against the Rate Limit rule, if request doest breach the Rate Limit Threashold then request will be treated a normal request and request will be allowed by WAF.
